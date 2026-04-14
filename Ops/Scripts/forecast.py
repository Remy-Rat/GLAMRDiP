"""
forecast.py — Stock-out forecast, days cover, inbound gaps, PO recommendations.

Usage:
    uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py AUS | \
    uv run --with pandas python3 Ops/Scripts/forecast.py

Reads extracted JSON from stdin. Outputs stock-out forecast and action items.
"""

import sys
import json
from datetime import datetime, timedelta

# Lead times (days)
SHIPPING = {"AUS": 30, "UK": 42, "CA": 45, "Nordic": 42}
EXPRESS_SHIPPING = {"AUS": 16, "UK": 42, "CA": 45, "Nordic": 42}
PRODUCTION_DAYS = 40
RAW_GOODS_DAYS = 70
LOCAL_FILL_DAYS = 28
TARGET_COVER = 17  # midpoint of 14-21d lean target


def main():
    data = json.load(sys.stdin)
    region = data["region"]
    pos = data["pos_model"]
    tpl = data["tpl"]
    shop = data["shopify"]
    config = data["config"]

    products = {p["sku"]: p for p in pos["products"]}
    sku_dsr = shop["sku_dsr"]
    sku_ded = tpl["sku_deductions"]
    shipments = pos["shipments"]
    today = datetime.now().date()

    ship_days = SHIPPING.get(region, 30)
    express_days = EXPRESS_SHIPPING.get(region, 16)

    print(f"STOCK-OUT FORECAST — {region} — {today.strftime('%d %b %Y')}")
    print(f"Lead times: {RAW_GOODS_DAYS + PRODUCTION_DAYS + ship_days}d (raw→delivery) | {PRODUCTION_DAYS + ship_days}d (fill→delivery) | {ship_days}d (shipping) | {LOCAL_FILL_DAYS}d (local fill)")
    print()

    # ---- Corrected days cover ----
    print("--- CORRECTED DAYS COVER ---")
    print(f"{'SKU':20s} {'Stock':>7s} {'Model DSR':>10s} {'Cover(M)':>9s} {'Actual DSR':>11s} {'Cover(A)':>9s} {'Flag':>10s}")

    critical = []
    warning = []
    watch = []
    safe_count = 0

    for p in pos["products"]:
        sku = p["sku"]
        stock = p["g3pl_on_hand"]
        model_rate = p["model_dsr"]
        if stock <= 0 and model_rate <= 0:
            continue

        # Actual DSR: prefer Shopify for sellable items, 3PL deduction for packaging/inserts
        actual_rate = 0
        if sku in config["packaging_skus"]:
            actual_rate = sku_ded.get(sku, {}).get("avg_deduction", 0)
        elif sku in config["kit_adjusted_items"]:
            # Kit-adjusted: standalone Shopify + kit consumption
            standalone = sku_dsr.get(sku, {}).get("14d", 0)
            kit_total = sum(sku_dsr.get(k, {}).get("14d", 0) for k in ["KIT-STA-2", "KIT-COM-4", "KIT-ULT-6"])
            actual_rate = standalone + kit_total
        else:
            actual_rate = sku_dsr.get(sku, {}).get("14d", 0)
            # For items with bundles, use 3PL deduction if significantly higher
            tpl_rate = sku_ded.get(sku, {}).get("avg_deduction", 0)
            if tpl_rate > actual_rate * 1.5 and tpl_rate > 5:
                actual_rate = tpl_rate  # Bundle effect — 3PL deduction is truer demand

        cover_model = stock / model_rate if model_rate > 0 else None
        cover_actual = stock / actual_rate if actual_rate > 0 else None

        flag = ""
        min_cover = min(c for c in [cover_model, cover_actual] if c is not None) if any(c is not None for c in [cover_model, cover_actual]) else None
        if min_cover is not None:
            if min_cover < 7:
                flag = "CRITICAL"
                critical.append((sku, p["name"], stock, model_rate, cover_model, actual_rate, cover_actual))
            elif min_cover < 14:
                flag = "CRITICAL"
                critical.append((sku, p["name"], stock, model_rate, cover_model, actual_rate, cover_actual))
            elif min_cover < 30:
                flag = "WARNING"
                warning.append((sku, p["name"], stock, model_rate, cover_model, actual_rate, cover_actual))
            elif min_cover < 45:
                flag = "WATCH"
                watch.append((sku, p["name"], stock, model_rate, cover_model, actual_rate, cover_actual))
            else:
                safe_count += 1
                continue  # Don't print safe items
        else:
            safe_count += 1
            continue

        cm_str = f"{cover_model:.0f}d" if cover_model else "—"
        ca_str = f"{cover_actual:.0f}d" if cover_actual else "—"
        print(f"{sku:20s} {stock:>7,} {model_rate:>10.1f} {cm_str:>9s} {actual_rate:>11.1f} {ca_str:>9s} {flag:>10s}")

    print(f"\n{safe_count} SKUs with 45+ days cover (safe) — not shown.")

    # ---- Stock-out forecast vs inbound ----
    print(f"\n--- STOCKOUT vs INBOUND ---")

    # Build shipment lookup: reference → est_arrival date
    ship_arrivals = {}
    for s in shipments:
        ref = s.get("reference", "")
        if not ref:
            continue
        arrival = s.get("est_arrival")
        if arrival:
            try:
                ship_arrivals[ref] = datetime.strptime(arrival, "%Y-%m-%d").date()
            except (ValueError, TypeError):
                pass

    stockout_before = []
    tight = []
    nothing_on_order = []

    for items in [critical, warning, watch]:
        for sku, name, stock, model_rate, cover_model, actual_rate, cover_actual in items:
            # Use actual rate for forecast (more conservative for planning)
            rate = actual_rate if actual_rate > 0 else model_rate
            if rate <= 0:
                continue
            days_to_stockout = stock / rate
            stockout_date = today + timedelta(days=int(days_to_stockout))

            # Find earliest inbound
            p = products.get(sku, {})
            inbound = p.get("inbound", {}) if isinstance(p, dict) else {}
            best_arrival = None
            best_ref = None
            best_qty = 0
            for ref, qty in inbound.items():
                arr = ship_arrivals.get(ref)
                if arr and (best_arrival is None or arr < best_arrival):
                    best_arrival = arr
                    best_ref = ref
                    best_qty = qty

            if best_arrival:
                days_to_arrival = (best_arrival - today).days
                gap = int(days_to_stockout) - days_to_arrival
                if gap < 0:
                    stockout_before.append((sku, name, stock, rate, stockout_date, best_ref, best_qty, best_arrival, gap))
                elif gap <= 7:
                    tight.append((sku, name, stock, rate, stockout_date, best_ref, best_qty, best_arrival, gap))
            else:
                # Nothing on order
                deadline = ""
                if days_to_stockout < 14:
                    deadline = "CRITICAL — express only"
                elif days_to_stockout < LOCAL_FILL_DAYS:
                    deadline = "Past local fill deadline"
                elif days_to_stockout < PRODUCTION_DAYS + ship_days:
                    deadline = "Past CN PO deadline"
                elif days_to_stockout < RAW_GOODS_DAYS + PRODUCTION_DAYS + ship_days:
                    deadline = "Raw goods PO deadline approaching"
                nothing_on_order.append((sku, name, stock, rate, stockout_date, days_to_stockout, deadline))

    if stockout_before:
        print(f"\nSTOCKOUT BEFORE ARRIVAL:")
        print(f"{'SKU':20s} {'Stock':>7s} {'DSR':>6s} {'Out':>11s} {'Inbound':>20s} {'Arrives':>11s} {'Gap':>6s}")
        for sku, name, stock, rate, out, ref, qty, arr, gap in stockout_before:
            print(f"{sku:20s} {stock:>7,} {rate:>6.1f} {out.strftime('%d %b'):>11s} {ref:>15s}+{qty:,} {arr.strftime('%d %b'):>11s} {gap:>+5d}d")

    if tight:
        print(f"\nTIGHT (0-7d margin):")
        print(f"{'SKU':20s} {'Stock':>7s} {'DSR':>6s} {'Out':>11s} {'Inbound':>20s} {'Arrives':>11s} {'Gap':>6s}")
        for sku, name, stock, rate, out, ref, qty, arr, gap in tight:
            print(f"{sku:20s} {stock:>7,} {rate:>6.1f} {out.strftime('%d %b'):>11s} {ref:>15s}+{qty:,} {arr.strftime('%d %b'):>11s} {gap:>+5d}d")

    if nothing_on_order:
        print(f"\nNOTHING ON ORDER:")
        print(f"{'SKU':20s} {'Stock':>7s} {'DSR':>6s} {'Out':>11s} {'Cover':>6s} {'Status'}")
        for sku, name, stock, rate, out, cover, deadline in nothing_on_order:
            print(f"{sku:20s} {stock:>7,} {rate:>6.1f} {out.strftime('%d %b'):>11s} {cover:>5.0f}d {deadline}")

    # ---- Action summary ----
    print(f"\n--- WHAT NEEDS ACTION ---")

    print(f"\nCRITICAL (act today):")
    for sku, name, stock, model_rate, cover_model, actual_rate, cover_actual in critical:
        cm = f"{cover_model:.0f}d" if cover_model else "—"
        ca = f"{cover_actual:.0f}d" if cover_actual else "—"
        print(f"  {sku} ({name}): {stock:,} units | Model: {cm} | Actual: {ca}")

    print(f"\nWARNING (act this week):")
    for sku, name, stock, model_rate, cover_model, actual_rate, cover_actual in warning:
        cm = f"{cover_model:.0f}d" if cover_model else "—"
        ca = f"{cover_actual:.0f}d" if cover_actual else "—"
        print(f"  {sku} ({name}): {stock:,} units | Model: {cm} | Actual: {ca}")

    print(f"\nWATCH:")
    for sku, name, stock, model_rate, cover_model, actual_rate, cover_actual in watch:
        cm = f"{cover_model:.0f}d" if cover_model else "—"
        ca = f"{cover_actual:.0f}d" if cover_actual else "—"
        print(f"  {sku} ({name}): {stock:,} units | Model: {cm} | Actual: {ca}")


if __name__ == "__main__":
    main()
