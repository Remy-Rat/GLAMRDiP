"""
extract.py — Download and parse Order Schedule xlsx into clean structured output.

Usage:
    uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py AUS
    uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py UK

Outputs JSON to stdout with all parsed data. Pipe to file or read directly.
"""

import sys
import json
import subprocess
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

# ---- Config ----

SHEET_IDS = {
    "AUS": "1fUitkQWryQmKdWLwvjyRG_C_-yh0v5lHjvQa3urBGr8",
    "CA": "1mCE2X25Fw67liKBgyvNMf3JGOwLM5ufQJTGPEJH1VEw",
    "UK": "1G7kzaGst8vyjgySiGJJC7BjdRf7eJiU-aHUsaE3PyXE",
    "Nordic": "1aBa7b5KZkOYYOfuBK3OHYENUQrFgrRtDwouL6fj2hTw",
}

TPL_TABS = {
    "AUS": "AUS 3GPL",
    "UK": "B360",
    "CA": "B360",
    "Nordic": "B360",
}

# Items filled locally and added at the 3PL per kit (kit-adjusted demand)
KIT_ADJUSTED = {
    "AUS": ["LIQ-HEA-5", "ACC-INS"],
    "CA": ["LIQ-HEA-5", "ACC-INS"],
    "UK": ["LIQ-HEA-5", "LIQ-BAS-2", "LIQ-GLO-4", "ACC-INS"],
    "Nordic": ["LIQ-HEA-5", "ACC-INS"],  # Until confirmed otherwise
}

# Items consumed on ALL orders (kit + standalone)
PER_ORDER = ["ACC-LAB", "ACC-THA"]

# Packaging SKUs — no Shopify sales, monitor via 3PL deductions only
PACKAGING_SKUS = [
    "STO-BUB-BAG-L", "STO-BUB-BAG-S", "STO-MAI-BAG-S", "STO-MAI-2",
    "ACC-INS", "ACC-THA", "ACC-LAB",
]

DEDUCTION_BENCHMARKS = {
    "KIT-STA-2": 100, "KIT-COM-4": 200, "KIT-ULT-6": 200,
    "LIQ-HEA-5": 435, "LIQ-BAS-2": 90, "LIQ-SEN-2": 18,
    "LIQ-SEA-3": 60, "LIQ-BON-1": 30, "LIQ-GLO-4": 45, "LIQ-SEN-4": 12,
    "LIQ-MAT-4": 18, "LIQ-SOA-6": 18,
    "ACC-REM": 100, "ACC-REM-500": 100, "ACC-REM-BOW": 100,
    "ACC-NAI-100/180": 90, "ACC-NAI-240": 90,
    "ACC-RE1-BOT": 100, "ACC-RE1-LID": 100, "ACC-RE1-INN": 100,
    "ACC-RE5-BOT": 100, "ACC-RE5-LID": 100, "ACC-RE5-INN": 100,
    "HEA-EMP": 435, "HEA-LID": 435, "HEA-BSH": 435,
    "STO-BUB-BAG-L": 435, "STO-MAI-BAG-S": 330, "STO-MAI-2": 330,
    "ACC-INS": 435, "ACC-THA": 735, "ACC-LAB": 735,
    "ACC-5PC-BAG": 24, "ACC-BRU": 9, "ACC-CUT-PRE": 15,
    "ACC-NAI-WIP": 15, "ACC-NAI-MAT": 15, "ACC-PRO-DRI": 12,
    "ACC-JAR": 21, "ACC-BOX": 3, "ACC-NAI-LIN": 24,
}
COLOUR_BENCHMARK = 35


def download_xlsx(region):
    sheet_id = SHEET_IDS[region]
    out_path = f"/tmp/{region.lower()}_order_schedule.xlsx"
    token = subprocess.check_output(
        ["/opt/homebrew/share/google-cloud-sdk/bin/gcloud", "auth", "print-access-token"],
        text=True,
    ).strip()
    subprocess.run(
        [
            "curl", "-s",
            "-H", f"Authorization: Bearer {token}",
            f"https://www.googleapis.com/drive/v3/files/{sheet_id}/export?mimeType=application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "-o", out_path,
        ],
        check=True,
    )
    return out_path


def parse_pos_model(file_path):
    pos_raw = pd.read_excel(file_path, sheet_name="POS MODEL", header=None)

    # Growth factor
    growth_factor = None
    for r in range(12):
        for c in range(15):
            val = pos_raw.iloc[r, c]
            if str(val).strip() == "GROWTH FACTOR":
                for dr, dc in [(1, 0), (0, 1), (0, -1)]:
                    cand = pos_raw.iloc[r + dr, c + dc]
                    if pd.notna(cand):
                        try:
                            growth_factor = float(cand)
                            break
                        except (ValueError, TypeError):
                            pass
                break

    # Kit DSRs from header (rows 1-5)
    kit_dsr = {}
    for r in range(1, 6):
        name = str(pos_raw.iloc[r, 0]).strip()
        val = pd.to_numeric(pos_raw.iloc[r, 1], errors="coerce")
        if "Starter" in name:
            kit_dsr["KIT-STA-2"] = float(val) if pd.notna(val) else 0
        elif "Complete" in name:
            kit_dsr["KIT-COM-4"] = float(val) if pd.notna(val) else 0
        elif "Ultimate" in name:
            kit_dsr["KIT-ULT-6"] = float(val) if pd.notna(val) else 0

    kit_base_total = sum(kit_dsr.values())

    # Updated date
    updated = None
    for r in range(10):
        for c in range(10):
            if str(pos_raw.iloc[r, c]).strip() == "UPDATED":
                cand = pos_raw.iloc[r, c + 1] if c + 1 < len(pos_raw.columns) else None
                if cand is None:
                    cand = pos_raw.iloc[r + 1, c]
                if pd.notna(cand):
                    try:
                        updated = pd.Timestamp(cand).strftime("%Y-%m-%d")
                    except Exception:
                        pass

    # Product table header row
    pos_header_row = None
    for r in range(len(pos_raw)):
        if str(pos_raw.iloc[r, 1]).strip() == "SKU":
            pos_header_row = r
            break

    # Shipment blocks — scan header rows for "Our Reference" labels
    shipments = []
    if pos_header_row:
        for c in range(12, len(pos_raw.columns)):
            label = str(pos_raw.iloc[5, c]).strip() if pd.notna(pos_raw.iloc[5, c]) else ""
            if "Our Reference" in label or "reference" in label.lower():
                ref_val = pos_raw.iloc[5, c + 1] if c + 1 < len(pos_raw.columns) and pd.notna(pos_raw.iloc[5, c + 1]) else ""
                # Scan surrounding rows for metadata
                ship = {"col": c, "reference": str(ref_val).strip()}
                for r in range(10):
                    for cc in [c, c + 1]:
                        if cc < len(pos_raw.columns):
                            lbl = str(pos_raw.iloc[r, c]).strip() if pd.notna(pos_raw.iloc[r, c]) else ""
                            val = pos_raw.iloc[r, c + 1] if c + 1 < len(pos_raw.columns) else None
                            if "Est. Completion" in lbl and pd.notna(val):
                                try:
                                    ship["est_completion"] = pd.Timestamp(val).strftime("%Y-%m-%d")
                                except Exception:
                                    pass
                            if "Est. Arrival" in lbl and pd.notna(val):
                                try:
                                    ship["est_arrival"] = pd.Timestamp(val).strftime("%Y-%m-%d")
                                except Exception:
                                    pass
                            if "Order Status" in lbl and pd.notna(val):
                                ship["status"] = str(val).strip()
                            if "GROWTH FACTOR" in lbl and pd.notna(val):
                                try:
                                    ship["growth_factor"] = float(val)
                                except Exception:
                                    pass
                shipments.append(ship)

    # Per-SKU data
    products = []
    if pos_header_row:
        # Map column indices for shipment OL values
        for r in range(pos_header_row + 1, len(pos_raw)):
            sku = str(pos_raw.iloc[r, 1]).strip()
            if sku == "nan" or sku == "":
                continue
            name = str(pos_raw.iloc[r, 0]).strip()
            stock = pd.to_numeric(pos_raw.iloc[r, 7], errors="coerce")
            days_cover = pd.to_numeric(pos_raw.iloc[r, 8], errors="coerce")
            backorder = pd.to_numeric(pos_raw.iloc[r, 10], errors="coerce")
            model_rate = float(stock / days_cover) if pd.notna(stock) and pd.notna(days_cover) and days_cover > 0 else 0

            # For kits, use scaled DSR
            if sku in kit_dsr and growth_factor:
                model_rate = kit_dsr[sku] * growth_factor

            # Collect OL per shipment block
            ol_by_shipment = {}
            for ship in shipments:
                col = ship["col"]
                # OL is at the shipment column itself in the product row
                ol_val = pd.to_numeric(pos_raw.iloc[r, col], errors="coerce")
                if pd.notna(ol_val) and ol_val != 0:
                    ol_by_shipment[ship["reference"]] = int(ol_val)

            prod = {
                "sku": sku,
                "name": name,
                "g3pl_on_hand": int(stock) if pd.notna(stock) else 0,
                "days_cover_model": round(float(days_cover), 1) if pd.notna(days_cover) else None,
                "model_dsr": round(model_rate, 1),
                "backorder": int(backorder) if pd.notna(backorder) and backorder != 0 else 0,
                "inbound": ol_by_shipment,
            }
            products.append(prod)

    return {
        "growth_factor": growth_factor,
        "kit_dsr_base": kit_dsr,
        "kit_base_total": kit_base_total,
        "kit_scaled_total": kit_base_total * growth_factor if growth_factor else None,
        "updated": updated,
        "shipments": shipments,
        "products": products,
    }


def parse_3pl(file_path, tab_name, lookback_days=45):
    tpl_raw = pd.read_excel(file_path, sheet_name=tab_name, header=None)
    tpl_skus = tpl_raw.iloc[1:, 0].astype(str).str.strip().values
    tpl_dates = pd.to_datetime(tpl_raw.iloc[0, 1:], errors="coerce")
    valid_idx = ~tpl_dates.isna()
    tpl_data = tpl_raw.iloc[1:, 1:].loc[:, valid_idx.values]
    tpl_data.columns = tpl_dates[valid_idx].values
    tpl_data.index = tpl_skus
    tpl_data = tpl_data.apply(pd.to_numeric, errors="coerce")
    tpl_data[tpl_data < -1000] = np.nan

    valid_counts = tpl_data.notna().sum()
    threshold = len(tpl_data) * 0.3
    valid_date_mask = valid_counts > threshold
    last_valid = pd.Timestamp(max(tpl_data.columns[valid_date_mask]))
    tpl = tpl_data.loc[:, tpl_data.columns <= last_valid]

    today = pd.Timestamp.now().normalize()
    cutoff = today - timedelta(days=lookback_days)
    recent_cols = [c for c in tpl.columns if c >= cutoff]

    # Container arrival detection (8+ SKUs increasing)
    diffs = tpl[recent_cols].diff(axis=1) if len(recent_cols) > 1 else pd.DataFrame()
    arrivals = []
    arrival_dates = set()
    for col in diffs.columns[1:]:
        increases = diffs[col][diffs[col] > 0]
        if len(increases) >= 8:
            arrival_dates.add(col)
            top5 = increases.nlargest(5)
            arrivals.append({
                "date": col.strftime("%Y-%m-%d"),
                "sku_count": int(len(increases)),
                "total_units": int(increases.sum()),
                "top5": {str(k): int(v) for k, v in top5.items()},
            })

    # Per-SKU deduction analysis (last 14 days, excluding arrival days)
    fourteen_ago = today - timedelta(days=14)
    recent_14 = [c for c in tpl.columns if c >= fourteen_ago and c <= last_valid]
    sku_deductions = {}
    for sku in tpl.index:
        if not isinstance(sku, str) or sku == "nan":
            continue
        row = tpl.loc[sku, recent_14].dropna()
        if len(row) < 2:
            continue
        daily_diffs = row.diff()
        sell_days = [c for c in daily_diffs.index[1:] if c not in arrival_dates]
        if not sell_days:
            continue
        deductions = daily_diffs[sell_days]
        deds_only = deductions[deductions < 0].abs()
        avg_ded = float(deds_only.mean()) if len(deds_only) > 0 else 0
        max_ded = float(deds_only.max()) if len(deds_only) > 0 else 0
        latest_stock = float(row.iloc[-1])
        first_stock = float(row.iloc[0])
        sku_deductions[sku] = {
            "latest_stock": latest_stock,
            "first_stock": first_stock,
            "avg_deduction": round(avg_ded, 1),
            "max_deduction": round(max_ded, 0),
            "days_cover_actual": round(latest_stock / avg_ded, 0) if avg_ded > 0 else None,
        }

    # Red flag deductions (full lookback period)
    red_flags = []
    full_diffs = tpl[recent_cols].diff(axis=1) if len(recent_cols) > 1 else pd.DataFrame()
    for sku in tpl.index:
        if not isinstance(sku, str):
            continue
        benchmark = DEDUCTION_BENCHMARKS.get(sku, COLOUR_BENCHMARK if sku.startswith("POW-") or sku.startswith("ACC-STI-") else None)
        if benchmark is None:
            continue
        for col in full_diffs.columns[1:]:
            val = full_diffs.loc[sku, col]
            if pd.notna(val) and val < 0 and abs(val) > benchmark:
                red_flags.append({
                    "date": col.strftime("%Y-%m-%d"),
                    "sku": sku,
                    "deduction": int(abs(val)),
                    "benchmark": benchmark,
                })
    red_flags.sort(key=lambda x: x["deduction"], reverse=True)

    return {
        "last_valid_date": last_valid.strftime("%Y-%m-%d"),
        "arrivals": arrivals,
        "arrival_dates": [d.strftime("%Y-%m-%d") for d in sorted(arrival_dates)],
        "sku_deductions": sku_deductions,
        "red_flags": red_flags[:30],
    }


def parse_shopify(file_path):
    shopify_raw = pd.read_excel(file_path, sheet_name="SHOPIFY", header=None)
    header_idx = None
    for i in range(10):
        row_vals = shopify_raw.iloc[i].astype(str).tolist()
        if any("Date" in str(v) for v in row_vals):
            header_idx = i
            break

    shopify = shopify_raw.iloc[header_idx + 1 :].copy()
    shopify.columns = ["date", "sku", "units"]
    shopify["date"] = pd.to_datetime(shopify["date"], errors="coerce")
    shopify["units"] = pd.to_numeric(shopify["units"], errors="coerce").fillna(0)
    shopify = shopify.dropna(subset=["date"])
    shopify["sku"] = shopify["sku"].astype(str).str.strip()
    shopify = shopify[shopify["sku"] != "nan"]

    latest = shopify["date"].max()

    def dsr(sku, days):
        start = latest - timedelta(days=days - 1)
        subset = shopify[(shopify["sku"] == sku) & (shopify["date"] >= start) & (shopify["date"] <= latest)]
        return round(subset["units"].sum() / days, 1)

    all_skus = [s for s in shopify["sku"].unique() if isinstance(s, str)]

    sku_dsr = {}
    for sku in all_skus:
        sku_dsr[sku] = {"7d": dsr(sku, 7), "14d": dsr(sku, 14), "30d": dsr(sku, 30)}

    # Weekly kit trend (last 9 weeks)
    kit_skus = ["KIT-STA-2", "KIT-COM-4", "KIT-ULT-6"]
    kit_data = shopify[shopify["sku"].isin(kit_skus)].copy()
    kit_data["week"] = kit_data["date"].dt.isocalendar().week.astype(int)
    kit_data["year"] = kit_data["date"].dt.isocalendar().year.astype(int)

    weeks = (
        kit_data.groupby(["year", "week"])
        .agg(total=("units", "sum"), days=("date", "nunique"), min_date=("date", "min"), max_date=("date", "max"))
        .reset_index()
        .sort_values(["year", "week"])
        .tail(9)
    )

    weekly_trend = []
    for _, row in weeks.iterrows():
        daily = round(row["total"] / row["days"], 1) if row["days"] > 0 else 0
        weekly_trend.append({
            "week": int(row["week"]),
            "dates": f"{row['min_date'].strftime('%d %b')}-{row['max_date'].strftime('%d %b')}",
            "days": int(row["days"]),
            "total": int(row["total"]),
            "daily_rate": daily,
        })

    # Dead stock (colours with stock — needs cross-ref with POS MODEL, done by caller)
    colours_14d_zero = [s for s in all_skus if s.startswith("POW-") and sku_dsr.get(s, {}).get("14d", 0) == 0]

    return {
        "latest_date": latest.strftime("%Y-%m-%d"),
        "sku_dsr": sku_dsr,
        "weekly_kit_trend": weekly_trend,
        "colours_14d_zero": colours_14d_zero,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 extract.py <REGION>", file=sys.stderr)
        print("Regions: AUS, UK, CA, Nordic", file=sys.stderr)
        sys.exit(1)

    region = sys.argv[1].upper()
    if region not in SHEET_IDS:
        print(f"Unknown region: {region}. Use AUS, UK, CA, or Nordic.", file=sys.stderr)
        sys.exit(1)

    print(f"Downloading {region} order schedule...", file=sys.stderr)
    file_path = download_xlsx(region)
    print(f"Downloaded to {file_path}", file=sys.stderr)

    print("Parsing POS MODEL...", file=sys.stderr)
    pos = parse_pos_model(file_path)

    print(f"Parsing 3PL tab ({TPL_TABS[region]})...", file=sys.stderr)
    tpl = parse_3pl(file_path, TPL_TABS[region])

    print("Parsing SHOPIFY...", file=sys.stderr)
    shop = parse_shopify(file_path)

    output = {
        "region": region,
        "extracted_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "file_path": file_path,
        "config": {
            "kit_adjusted_items": KIT_ADJUSTED[region],
            "per_order_items": PER_ORDER,
            "packaging_skus": PACKAGING_SKUS,
            "tpl_tab": TPL_TABS[region],
        },
        "pos_model": pos,
        "tpl": tpl,
        "shopify": shop,
    }

    print(json.dumps(output, indent=2, default=str))


if __name__ == "__main__":
    main()
