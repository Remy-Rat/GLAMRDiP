#!/usr/bin/env python3
"""Order health report — backorders, stale orders, holds across ShipHero accounts.

Usage:
    uv run --with pandas,openpyxl python3 build_report.py [--test|--full]
                                                          [--regions AUS,UK,CA]
                                                          [--by-region]
                                                          [--out-dir PATH]
"""
import argparse
import json
import os
import time
import urllib.request
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

import pandas as pd

URL = "https://public-api.shiphero.com/graphql"
TOKEN_DIR = Path.home() / ".claude/skills/shiphero-public-api"
TERMINAL = {"fulfilled", "canceled", "cancelled"}
HOLD_FIELDS = ["fraud_hold", "address_hold", "shipping_method_hold", "operator_hold", "payment_hold", "client_hold"]

# Known in-flight statuses observed in practice per region. Used as a fallback when
# dynamic discovery misses rare custom statuses. Each 3PL configures their own workflow,
# sometimes dash-suffixed by kit type (e.g. "GlamrDip - Ultimate Kit"). Update this list
# when discovery surfaces a new status — keeps coverage robust even when traffic volume
# pushes rare statuses outside the discovery sample.
KNOWN_INFLIGHT_FALLBACKS = {
    "AUS": ["pending", "GlamrDip", "GlamrDip - Starter Kit", "GlamrDip - Complete Kit",
            "GlamrDip - Ultimate Kit", "GlamrDip Large"],
    "UK":  ["pending", "GLAMRDIP D-PACK Ready"],
    "CA":  ["pending", "GLAMRDiP"],
}


def n_business_days_ago(d, n):
    count = 0
    while count < n:
        d -= timedelta(days=1)
        if d.weekday() < 5:
            count += 1
    return d


def load_token(region):
    f = TOKEN_DIR / f"token_{region.lower()}.json"
    if not f.exists():
        raise FileNotFoundError(f"No ShipHero token for {region} at {f}. Run OAuth flow first.")
    return json.load(open(f))["access_token"]


def gql(token, query, max_retries=3):
    for _ in range(max_retries):
        req = urllib.request.Request(
            URL,
            data=json.dumps({"query": query}).encode(),
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            method="POST",
        )
        r = json.loads(urllib.request.urlopen(req).read())
        if r.get("errors") and any(e.get("code") == 30 for e in r["errors"]):
            time.sleep(10)
            continue
        return r
    return r


def fetch_backorders(token, full=False):
    """Backorders — all current. Pages of 20. Returns (rows, pages, order_numbers_set)."""
    rows = []
    order_numbers = set()
    cursor = None
    pages = 0
    page_cap = None if full else 6  # test cap: 6 pages = up to 120 backordered orders
    while True:
        pages += 1
        if page_cap is not None and pages > page_cap:
            break
        after = f', after: "{cursor}"' if cursor else ""
        q = (
            f"{{ orders(has_backorder: true) {{ data(first: 20{after}) "
            "{ pageInfo { hasNextPage endCursor } edges { node { order_number order_date "
            "line_items { edges { node { sku product_name quantity backorder_quantity } } } } } } } }"
        )
        r = gql(token, q)
        if r.get("errors"):
            print(f"  Backorder ERR: {r['errors']}")
            break
        data = r["data"]["orders"]["data"]
        for e in data["edges"]:
            o = e["node"]
            order_has_bo = False
            for li in o["line_items"]["edges"]:
                i = li["node"]
                if (i["backorder_quantity"] or 0) > 0:
                    order_has_bo = True
                    rows.append({
                        "Order Number": o["order_number"],
                        "Date": o["order_date"],
                        "SKU": i["sku"],
                        "Product": i["product_name"] or "",
                        "Backordered": i["backorder_quantity"],
                    })
            if order_has_bo:
                order_numbers.add(o["order_number"])
        if not data["pageInfo"]["hasNextPage"]:
            break
        cursor = data["pageInfo"]["endCursor"]
        if r["extensions"]["throttling"]["user_quota"]["credits_remaining"] < 600:
            time.sleep(8)
    return rows, pages, order_numbers


def discover_inflight_statuses(token, region, today):
    """Discover non-terminal fulfillment_status values; union with known fallbacks.

    Uses `updated_from` filter (last 7 days) which catches currently-active orders
    by recent edit time. Paginates deeper than first:200 so rare custom statuses
    like 'GlamrDip Large' (1 order) get captured. Unions with KNOWN_INFLIGHT_FALLBACKS
    so we keep coverage even when traffic pushes a rare status outside the sample.
    """
    statuses = set(KNOWN_INFLIGHT_FALLBACKS.get(region, ["pending"]))
    updated_from = (today - timedelta(days=7)).strftime("%Y-%m-%d") + "T00:00:00"
    cursor = None
    for _ in range(15):  # up to 1,500 orders sampled
        after = f', after: "{cursor}"' if cursor else ""
        q = f'{{ orders(updated_from: "{updated_from}") {{ data(first: 100{after}) {{ pageInfo {{ hasNextPage endCursor }} edges {{ node {{ fulfillment_status }} }} }} }} }}'
        r = gql(token, q)
        if r.get("errors"):
            break
        data = r["data"]["orders"]["data"]
        for e in data["edges"]:
            s = e["node"]["fulfillment_status"]
            if s and s not in TERMINAL:
                statuses.add(s)
        if not data["pageInfo"]["hasNextPage"]:
            break
        cursor = data["pageInfo"]["endCursor"]
        if r["extensions"]["throttling"]["user_quota"]["credits_remaining"] < 1000:
            break
    return sorted(statuses)


def fetch_stale(token, region, today, stale_before_iso, exclude_orders=None, full=False):
    """Stale orders — orders in any in-flight status, placed before stale_before_iso.

    Dynamically discovers per-region in-flight statuses (each 3PL configures their own,
    including dash-suffixed variants like 'GlamrDip - Starter Kit'). Then queries each
    status independently with a date_to filter — small result sets, no need to paginate
    through fulfilled history.

    `exclude_orders` is a set of order numbers to skip (typically backordered orders —
    they're blocked on stock, not stale in the actionable sense).
    """
    exclude_orders = exclude_orders or set()
    statuses = discover_inflight_statuses(token, region, today)
    print(f"  In-flight statuses (discovered + fallbacks): {statuses}")
    rows = []
    seen = set()
    excluded_count = 0
    total_pages = 0
    for status in statuses:
        cursor = None
        page_cap = None if full else 5  # per-status page cap (each ~10-50 credits)
        pages_for_status = 0
        while True:
            pages_for_status += 1
            total_pages += 1
            if page_cap is not None and pages_for_status > page_cap:
                break
            after = f', after: "{cursor}"' if cursor else ""
            q = (
                f'{{ orders(fulfillment_status: "{status}", order_date_to: "{stale_before_iso}") '
                f"{{ data(first: 100{after}) {{ pageInfo {{ hasNextPage endCursor }} "
                "edges { node { order_number order_date fulfillment_status "
                "holds { fraud_hold address_hold shipping_method_hold operator_hold payment_hold client_hold } } } } } }"
            )
            r = gql(token, q)
            if r.get("errors"):
                # Status may not exist on this account — silently skip, log only if it's the only one
                print(f"  Stale (status={status!r}) ERR: {r['errors']}")
                break
            data = r["data"]["orders"]["data"]
            for e in data["edges"]:
                o = e["node"]
                if o["order_number"] in seen:
                    continue
                if o["order_number"] in exclude_orders:
                    excluded_count += 1
                    seen.add(o["order_number"])
                    continue
                seen.add(o["order_number"])
                age = (today - datetime.fromisoformat(o["order_date"].replace("Z", "")).date()).days
                h = o.get("holds") or {}
                reasons = [k.replace("_hold", "") for k in HOLD_FIELDS if h.get(k)]
                rows.append({
                    "Order Number": o["order_number"],
                    "Order Date": o["order_date"],
                    "Age (cal days)": age,
                    "Status": o["fulfillment_status"],
                    "On Hold": "Y" if reasons else "",
                    "Hold reasons": ", ".join(reasons),
                })
            if not data["pageInfo"]["hasNextPage"]:
                break
            cursor = data["pageInfo"]["endCursor"]
            if r["extensions"]["throttling"]["user_quota"]["credits_remaining"] < 800:
                time.sleep(8)
    if excluded_count:
        print(f"  (excluded {excluded_count} stale orders already counted as backorders)")
    return rows, total_pages


def fetch_holds(token, today, full=False):
    """On-hold orders — last 30 days, any *_hold flag true."""
    rows = []
    cursor = None
    pages = 0
    page_cap = None if full else 2  # test cap: 2 pages = 200 orders
    window_start = (today - timedelta(days=30)).strftime("%Y-%m-%d")
    while True:
        pages += 1
        if page_cap is not None and pages > page_cap:
            break
        after = f', after: "{cursor}"' if cursor else ""
        q = (
            f'{{ orders(order_date_from: "{window_start}") '
            f"{{ data(first: 100{after}) {{ pageInfo {{ hasNextPage endCursor }} "
            "edges { node { order_number order_date fulfillment_status "
            "holds { fraud_hold address_hold shipping_method_hold operator_hold payment_hold client_hold } } } } } }"
        )
        r = gql(token, q)
        if r.get("errors"):
            print(f"  Hold ERR p{pages}: {r['errors']}")
            break
        data = r["data"]["orders"]["data"]
        for e in data["edges"]:
            o = e["node"]
            h = o.get("holds") or {}
            reasons = [k.replace("_hold", "") for k in HOLD_FIELDS if h.get(k)]
            if reasons:
                rows.append({
                    "Order Number": o["order_number"],
                    "Order Date": o["order_date"],
                    "Status": o["fulfillment_status"],
                    "Hold reasons": ", ".join(reasons),
                })
        if not data["pageInfo"]["hasNextPage"]:
            break
        cursor = data["pageInfo"]["endCursor"]
        if r["extensions"]["throttling"]["user_quota"]["credits_remaining"] < 800:
            time.sleep(8)
    return rows, pages


def write_xlsx(path, today, stale_cutoff, by_region_data, mode_note):
    """Write the combined report with Summary + per-region category tabs.

    Tab structure: one Summary, then for each region: BO by SKU, Backorders, Stale, On Hold.
    """
    summary = []
    for region, d in by_region_data.items():
        summary.append({
            "Region": region,
            "BO line items": len(d["bo"]),
            f"Stale (placed before {stale_cutoff}, not fulfilled)": len(d["stale"]),
            "On hold (any flag)": len(d["holds"]),
            "Mode": mode_note,
        })
    summary.append({
        "Region": "TOTAL",
        "BO line items": sum(len(d["bo"]) for d in by_region_data.values()),
        f"Stale (placed before {stale_cutoff}, not fulfilled)": sum(len(d["stale"]) for d in by_region_data.values()),
        "On hold (any flag)": sum(len(d["holds"]) for d in by_region_data.values()),
        "Mode": mode_note,
    })

    def _fmt_date(df, col):
        df = df.copy()
        df[col] = pd.to_datetime(df[col], errors="coerce").dt.strftime("%m/%d/%Y %I:%M %p")
        return df

    with pd.ExcelWriter(path, engine="openpyxl") as w:
        pd.DataFrame(summary).to_excel(w, sheet_name="Summary", index=False)
        for region, d in by_region_data.items():
            # BO by SKU
            if d["bo"]:
                bo_df = pd.DataFrame(d["bo"])
                sku_summary = (
                    bo_df.groupby(["SKU", "Product"], dropna=False)
                    .agg(**{
                        "Orders affected": ("Order Number", "nunique"),
                        "Total qty backordered": ("Backordered", "sum"),
                    })
                    .reset_index()
                    .sort_values("Orders affected", ascending=False)
                    .reset_index(drop=True)
                )
                sku_summary.to_excel(w, sheet_name=f"{region} BO by SKU", index=False)
                _fmt_date(bo_df, "Date").sort_values("Date").to_excel(w, sheet_name=f"{region} Backorders", index=False)
            else:
                pd.DataFrame(columns=["SKU", "Product", "Orders affected", "Total qty backordered"]).to_excel(w, sheet_name=f"{region} BO by SKU", index=False)
                pd.DataFrame(columns=["Order Number", "Date", "SKU", "Product", "Backordered"]).to_excel(w, sheet_name=f"{region} Backorders", index=False)
            # Stale
            if d["stale"]:
                _fmt_date(pd.DataFrame(d["stale"]), "Order Date").sort_values("Order Date").to_excel(w, sheet_name=f"{region} Stale Orders", index=False)
            else:
                pd.DataFrame(columns=["Order Number", "Order Date", "Age (cal days)", "Status", "On Hold", "Hold reasons"]).to_excel(w, sheet_name=f"{region} Stale Orders", index=False)
            # On Hold
            if d["holds"]:
                _fmt_date(pd.DataFrame(d["holds"]), "Order Date").sort_values("Order Date").to_excel(w, sheet_name=f"{region} On Hold", index=False)
            else:
                pd.DataFrame(columns=["Order Number", "Order Date", "Status", "Hold reasons"]).to_excel(w, sheet_name=f"{region} On Hold", index=False)


def write_region_xlsx(path, region, data, today, stale_cutoff, mode_note):
    """Single-region xlsx for VA hand-off."""
    summary = [{
        "Region": region,
        "BO line items": len(data["bo"]),
        f"Stale (placed before {stale_cutoff}, not fulfilled)": len(data["stale"]),
        "On hold (any flag)": len(data["holds"]),
        "Mode": mode_note,
    }]

    def _fmt_date(df, col):
        df = df.copy()
        df[col] = pd.to_datetime(df[col], errors="coerce").dt.strftime("%m/%d/%Y %I:%M %p")
        return df

    with pd.ExcelWriter(path, engine="openpyxl") as w:
        pd.DataFrame(summary).to_excel(w, sheet_name="Summary", index=False)
        if data["bo"]:
            bo_df = pd.DataFrame(data["bo"])
            sku_summary = (
                bo_df.groupby(["SKU", "Product"], dropna=False)
                .agg(**{
                    "Orders affected": ("Order Number", "nunique"),
                    "Total qty backordered": ("Backordered", "sum"),
                })
                .reset_index()
                .sort_values("Orders affected", ascending=False)
                .reset_index(drop=True)
            )
            sku_summary.to_excel(w, sheet_name="Backorders by SKU", index=False)
            _fmt_date(bo_df, "Date").sort_values("Date").to_excel(w, sheet_name="Backorders", index=False)
        else:
            pd.DataFrame(columns=["SKU", "Product", "Orders affected", "Total qty backordered"]).to_excel(w, sheet_name="Backorders by SKU", index=False)
            pd.DataFrame(columns=["Order Number", "Date", "SKU", "Product", "Backordered"]).to_excel(w, sheet_name="Backorders", index=False)
        if data["stale"]:
            _fmt_date(pd.DataFrame(data["stale"]), "Order Date").sort_values("Order Date").to_excel(w, sheet_name="Stale Orders", index=False)
        else:
            pd.DataFrame(columns=["Order Number", "Order Date", "Age (cal days)", "Status", "On Hold", "Hold reasons"]).to_excel(w, sheet_name="Stale Orders", index=False)
        if data["holds"]:
            _fmt_date(pd.DataFrame(data["holds"]), "Order Date").sort_values("Order Date").to_excel(w, sheet_name="On Hold", index=False)
        else:
            pd.DataFrame(columns=["Order Number", "Order Date", "Status", "Hold reasons"]).to_excel(w, sheet_name="On Hold", index=False)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--full", action="store_true", help="Paginate everything (slower, higher credit cost).")
    p.add_argument("--regions", default="AUS,UK,CA", help="Comma-separated regions. Default: AUS,UK,CA")
    p.add_argument("--by-region", action="store_true", help="Also write per-region xlsx files for VA hand-off.")
    p.add_argument("--out-dir", default=str(Path.home() / "Downloads"))
    args = p.parse_args()

    today = date.today()
    if today.weekday() >= 5:
        print(f"WARNING: today is {today.strftime('%A')} — orders typically aren't fulfilled on weekends. Report may be misleading.")

    stale_cutoff = n_business_days_ago(today, 2)
    stale_before_iso = (stale_cutoff + timedelta(days=1)).strftime("%Y-%m-%d") + "T00:00:00"
    mode_note = "FULL" if args.full else "TEST (capped pagination)"
    print(f"Today: {today} | stale cutoff: orders placed before {stale_cutoff} | mode: {mode_note}")

    regions = [r.strip().upper() for r in args.regions.split(",") if r.strip()]
    by_region_data = {}
    for region in regions:
        print(f"\n=== {region} ===")
        try:
            token = load_token(region)
        except FileNotFoundError as e:
            print(f"  SKIP: {e}")
            continue
        bo, bo_pages, bo_order_numbers = fetch_backorders(token, full=args.full)
        print(f"  Backorders: {len(bo)} line items across {len(bo_order_numbers)} orders ({bo_pages} pages)")
        stale, st_pages = fetch_stale(token, region, today, stale_before_iso, exclude_orders=bo_order_numbers, full=args.full)
        print(f"  Stale orders (excluding backordered): {len(stale)} ({st_pages} pages)")
        holds, h_pages = fetch_holds(token, today, full=args.full)
        print(f"  Holds: {len(holds)} ({h_pages} pages)")
        by_region_data[region] = {"bo": bo, "stale": stale, "holds": holds}

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    combined = out_dir / f"order_health_{today}.xlsx"
    write_xlsx(combined, today, stale_cutoff, by_region_data, mode_note)
    print(f"\nCombined report: {combined}")

    if args.by_region:
        for region, data in by_region_data.items():
            path = out_dir / f"order_health_{region}_{today}.xlsx"
            write_region_xlsx(path, region, data, today, stale_cutoff, mode_note)
            print(f"  {region} region file: {path}")

    # Print short summary
    print("\n=== Summary ===")
    for region, data in by_region_data.items():
        print(f"  {region:5s} BO={len(data['bo']):>4d}  Stale={len(data['stale']):>3d}  Holds={len(data['holds']):>3d}")


if __name__ == "__main__":
    main()
