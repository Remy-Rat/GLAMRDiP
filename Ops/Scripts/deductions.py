"""
deductions.py — 3PL deduction rates, anomalies, Shopify vs 3PL alignment.

Usage:
    uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py AUS | \
    uv run --with pandas python3 Ops/Scripts/deductions.py

Reads extracted JSON from stdin. Outputs deduction analysis tables.
"""

import sys
import json


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

    print(f"DEDUCTION ANALYSIS — {region} — extracted {data['extracted_at']}")
    print(f"3PL last valid: {tpl['last_valid_date']}")
    print(f"Arrival days excluded: {tpl['arrival_dates']}")
    print()

    # ---- Container arrivals ----
    print("--- CONTAINER ARRIVALS DETECTED ---")
    for a in tpl["arrivals"]:
        print(f"  {a['date']}: {a['sku_count']} SKUs, +{a['total_units']:,} units")
        for sku, units in list(a["top5"].items())[:3]:
            print(f"    {sku}: +{units:,}")

    # ---- Shopify vs 3PL alignment (kits) ----
    print(f"\n--- SHOPIFY vs 3PL ALIGNMENT (kits, 14d) ---")
    print(f"{'SKU':15s} {'3PL Ded/d':>10s} {'Shop/d':>8s} {'Gap':>7s} {'Status':>10s}")
    for sku in ["KIT-STA-2", "KIT-COM-4", "KIT-ULT-6"]:
        d = sku_ded.get(sku, {})
        s = sku_dsr.get(sku, {})
        avg_3pl = d.get("avg_deduction", 0)
        avg_shop = s.get("14d", 0)
        gap = avg_3pl - avg_shop
        status = "ALIGNED" if abs(gap) < 5 else ("3PL FASTER" if gap > 5 else "3PL SLOWER")
        print(f"{sku:15s} {avg_3pl:>10.1f} {avg_shop:>8.1f} {gap:>+7.1f} {status:>10s}")

    # ---- Shopify vs 3PL alignment (liquids + remove) ----
    print(f"\n--- SHOPIFY vs 3PL ALIGNMENT (liquids & remove, 14d) ---")
    print(f"{'SKU':15s} {'3PL Ded/d':>10s} {'Shop/d':>8s} {'Gap':>7s} {'Status':>10s} {'Note':s}")
    for sku in ["LIQ-HEA-5", "LIQ-BAS-2", "LIQ-GLO-4", "LIQ-SEA-3", "LIQ-BON-1", "LIQ-SEN-2", "LIQ-SEN-4", "ACC-REM-500", "ACC-REM", "ACC-REM-BOW"]:
        d = sku_ded.get(sku, {})
        s = sku_dsr.get(sku, {})
        avg_3pl = d.get("avg_deduction", 0)
        avg_shop = s.get("14d", 0)
        gap = avg_3pl - avg_shop
        status = "ALIGNED" if abs(gap) < 5 else ("3PL FASTER" if gap > 5 else "3PL SLOWER")
        note = ""
        if sku in config["kit_adjusted_items"]:
            note = "kit-adj (3PL includes kit consumption)"
        elif sku in ["ACC-REM-500", "ACC-REM-BOW"]:
            note = "bundle effect (ACC-REM-BUN-2)"
        elif sku == "ACC-REM":
            note = "bundle effect (ACC-REM-BUN-1)"
        print(f"{sku:15s} {avg_3pl:>10.1f} {avg_shop:>8.1f} {gap:>+7.1f} {status:>10s} {note}")

    # ---- Packaging deduction rates ----
    print(f"\n--- PACKAGING & INSERTS ---")
    print(f"{'SKU':20s} {'Stock':>8s} {'Ded/d':>7s} {'Cover':>7s} {'Max/d':>7s}")
    for sku in config["packaging_skus"]:
        d = sku_ded.get(sku, {})
        stock = d.get("latest_stock", 0)
        avg = d.get("avg_deduction", 0)
        cover = d.get("days_cover_actual")
        max_d = d.get("max_deduction", 0)
        cover_str = f"{cover:.0f}d" if cover else "—"
        print(f"{sku:20s} {stock:>8,.0f} {avg:>7.1f} {cover_str:>7s} {max_d:>7.0f}")

    # ---- Red flag deductions ----
    print(f"\n--- RED FLAG DEDUCTIONS (single day > benchmark) ---")
    print(f"{'Date':>12s} {'SKU':>20s} {'Deduction':>10s} {'Benchmark':>10s}")
    for rf in tpl["red_flags"][:20]:
        print(f"{rf['date']:>12s} {rf['sku']:>20s} {rf['deduction']:>10,} {rf['benchmark']:>10,}")

    # ---- Key SKU 14d deduction summary ----
    print(f"\n--- KEY SKU DEDUCTION SUMMARY (14d, excl arrival days) ---")
    print(f"{'SKU':20s} {'Start':>8s} {'Latest':>8s} {'Avg Ded':>8s} {'Cover':>7s}")
    key_skus = [
        "KIT-STA-2", "KIT-COM-4", "KIT-ULT-6",
        "LIQ-HEA-5", "LIQ-BAS-2", "LIQ-SEN-2", "LIQ-GLO-4", "LIQ-SEN-4",
        "LIQ-SEA-3", "LIQ-BON-1", "ACC-REM-500", "ACC-REM", "ACC-REM-BOW",
        "ACC-LAB", "POW-CLE-193",
    ]
    for sku in key_skus:
        d = sku_ded.get(sku, {})
        if not d:
            continue
        cover = d.get("days_cover_actual")
        cover_str = f"{cover:.0f}d" if cover else "—"
        print(f"{sku:20s} {d['first_stock']:>8,.0f} {d['latest_stock']:>8,.0f} {d['avg_deduction']:>8.1f} {cover_str:>7s}")


if __name__ == "__main__":
    main()
