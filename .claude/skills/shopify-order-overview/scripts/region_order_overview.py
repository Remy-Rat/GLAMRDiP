#!/usr/bin/env python3
"""Region order overview -> Google Sheet (3 tabs: orders >48h, backordered SKUs, holds).

Usage: python3 region_order_overview.py <REGION>
Where <REGION> in (AUS, UK, CA).
"""
import json
import re
import sys
import time
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

URL = "https://public-api.shiphero.com/graphql"
TERMINAL = {"fulfilled", "canceled", "cancelled"}
HOLD_FIELDS = ["fraud_hold", "address_hold", "shipping_method_hold", "operator_hold", "payment_hold", "client_hold"]
ADC_PATH = "/Users/remy-m4/.config/gcloud/legacy_credentials/remy@glamrdip.com/adc.json"

FOLDER_ID = "1owM2WBXTsvQ0O9-eJsBR1SK9qOMPnUeJ"  # "Shopify Order Overview" Drive folder
HISTORY_DIR = Path.home() / ".claude/data/order-overview-history"

REGIONS = {
    "AUS": {
        "token": Path.home() / ".claude/skills/shiphero-public-api/token_aus.json",
        "inflight": ["pending", "GlamrDip", "GlamrDip - Starter Kit", "GlamrDip - Complete Kit",
                     "GlamrDip - Ultimate Kit", "GlamrDip Large"],
    },
    "UK": {
        "token": Path.home() / ".claude/skills/shiphero-public-api/token_uk.json",
        "inflight": ["pending", "GLAMRDIP D-PACK Ready"],
    },
    "CA": {
        "token": Path.home() / ".claude/skills/shiphero-public-api/token_ca.json",
        "inflight": ["pending", "GLAMRDiP"],
    },
}


def shiphero_token(region):
    return json.load(open(REGIONS[region]["token"]))["access_token"]


def gql(token, query, max_retries=5):
    """Run a GraphQL query. On rate-limit error (code 30), parse the `time_remaining`
    hint from ShipHero and sleep that long (plus 3s buffer) before retrying."""
    for _ in range(max_retries):
        req = urllib.request.Request(
            URL,
            data=json.dumps({"query": query}).encode(),
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            method="POST",
        )
        r = json.loads(urllib.request.urlopen(req).read())
        rate_errors = [e for e in (r.get("errors") or []) if e.get("code") == 30]
        if rate_errors:
            # Find longest wait suggested by ShipHero and sleep that long + buffer
            longest = 0
            for e in rate_errors:
                msg = e.get("message", "")
                m = re.search(r"In (\d+) seconds", msg)
                if m:
                    longest = max(longest, int(m.group(1)))
            time.sleep(max(longest, 5) + 3)
            continue
        return r
    return r


def fetch_backordered_skus_via_products(token, valid_skus=None):
    """Enumerate products, keep those with backorder > 0. Source of truth that matches
    ShipHero's inventory view.

    If `valid_skus` is provided (set of SKUs that appear on at least one currently-
    backordered order), a SKU is kept when backorder > 0 AND either:
      - the SKU appears in `valid_skus` (direct line-item match), OR
      - the warehouse row is genuinely out of stock (available == 0 AND allocated > 0).
    The second clause catches kit-component backorders: when a bundle SKU
    (e.g. CA-$85-GIF) is on the order line but the actual short item is a component
    inside it, ShipHero flags the component as backordered with avail=0/alloc>0 even
    though it never appears on a line item itself. Without this rescue clause CA's
    real backorders (e.g. Mani Mat) get filtered out.
    Pass `valid_skus=None` to skip filtering."""
    rows = []
    cursor = None
    pages = 0
    while True:
        pages += 1
        after = f', after: "{cursor}"' if cursor else ""
        q = (
            f"{{ products {{ data(first: 50{after}) {{ pageInfo {{ hasNextPage endCursor }} "
            "edges { node { sku name warehouse_products { warehouse_id warehouse_identifier on_hand backorder allocated available } } } } } }"
        )
        r = gql(token, q)
        if r.get("errors"):
            print(f"  products ERR p{pages}: {r['errors']}")
            break
        d = r["data"]["products"]["data"]
        for e in d["edges"]:
            node = e["node"]
            sku = node["sku"]
            for wp in node["warehouse_products"]:
                bo = wp.get("backorder") or 0
                if bo <= 0:
                    continue
                allocated = wp.get("allocated") or 0
                available = wp.get("available") or 0
                if valid_skus is not None and sku not in valid_skus:
                    # Rescue clause: genuinely OOS (available=0 AND allocated>0) means real
                    # demand against zero stock -- keep even when SKU isn't on a line item.
                    if not (available == 0 and allocated > 0):
                        continue
                rows.append({
                    "SKU": sku,
                    "Product": node["name"],
                    "Warehouse": wp["warehouse_identifier"],
                    "On Hand": wp.get("on_hand") or 0,
                    "Backorder (pcs short)": bo,
                    "Allocated": allocated,
                    "Available": available,
                })
        if not d["pageInfo"]["hasNextPage"]:
            break
        cursor = d["pageInfo"]["endCursor"]
        if r["extensions"]["throttling"]["user_quota"]["credits_remaining"] < 800:
            time.sleep(8)
    rows.sort(key=lambda r: r["Backorder (pcs short)"], reverse=True)
    return rows, pages


def fetch_backordered_orders_with_lines(token):
    """Backordered orders + the SKUs in each that are on backorder.

    Includes ALL sources -- Shopify customer orders AND ShipHero manual (MO) orders
    created by customer support, since both represent real demand waiting on stock.
    `source` is captured so the reporting layer can label MO orders distinctly.

    Returns (order_numbers_set, long_form_rows) where long_form_rows is one row per
    (order, backordered_sku) pair -- tidy data for filter-driven views.
    """
    order_numbers = set()
    rows = []
    cursor = None
    pages = 0
    while True:
        pages += 1
        after = f', after: "{cursor}"' if cursor else ""
        q = (
            f"{{ orders(has_backorder: true) {{ data(first: 20{after}) "
            "{ pageInfo { hasNextPage endCursor } edges { node { order_number order_date source shop_name "
            "line_items { edges { node { sku product_name backorder_quantity } } } } } } } }"
        )
        r = gql(token, q)
        if r.get("errors"):
            print(f"  BO orders ERR p{pages}: {r['errors']}")
            break
        d = r["data"]["orders"]["data"]
        for e in d["edges"]:
            o = e["node"]
            order_numbers.add(o["order_number"])
            for li in (o.get("line_items") or {}).get("edges", []):
                n = li["node"]
                qty = n.get("backorder_quantity") or 0
                if qty <= 0:
                    continue
                rows.append({
                    "Order Number": o["order_number"],
                    "Order Date": o["order_date"],
                    "Source": o.get("source") or "",
                    "SKU": n["sku"],
                    "Product": n.get("product_name") or "",
                    "Backordered (pcs)": qty,
                })
        if not d["pageInfo"]["hasNextPage"]:
            break
        cursor = d["pageInfo"]["endCursor"]
        if r["extensions"]["throttling"]["user_quota"]["credits_remaining"] < 600:
            time.sleep(8)
    rows.sort(key=lambda r: (r["Order Date"], r["Order Number"], r["SKU"]))
    return order_numbers, rows


def fetch_fulfillable_old(token, inflight_statuses, cutoff_iso, exclude_orders):
    """Old orders in an in-flight status that are genuinely unshipped and unblocked.

    `fulfillment_status` alone is unreliable for "needs picking" -- some 3PLs (e.g.
    Fulfillable in UK) leave orders in `pending` after shipping. We additionally
    require sum(line.quantity_shipped) == 0 to mean "nothing has physically gone out".
    Orders with any backorder line or any hold are also excluded.
    """
    rows = []
    seen = set()
    for status in inflight_statuses:
        cursor = None
        for _ in range(20):
            after = f', after: "{cursor}"' if cursor else ""
            q = (
                f'{{ orders(fulfillment_status: "{status}", order_date_to: "{cutoff_iso}") '
                f"{{ data(first: 20{after}) {{ pageInfo {{ hasNextPage endCursor }} "
                "edges { node { order_number order_date "
                "holds { fraud_hold address_hold shipping_method_hold operator_hold payment_hold client_hold } "
                "line_items { edges { node { quantity_shipped } } } "
                "} } } } }"
            )
            r = gql(token, q)
            if r.get("errors"):
                print(f"  ERR status={status!r}: {r['errors']}")
                break
            d = r["data"]["orders"]["data"]
            for e in d["edges"]:
                o = e["node"]
                num = o["order_number"]
                if num in seen:
                    continue
                seen.add(num)
                if num in exclude_orders:
                    continue
                h = o.get("holds") or {}
                if any(h.get(k) for k in HOLD_FIELDS):
                    continue
                # Drop anything where anything has shipped already (status is unreliable in some 3PL workflows)
                lines = [li["node"] for li in (o.get("line_items") or {}).get("edges", [])]
                if any((li.get("quantity_shipped") or 0) > 0 for li in lines):
                    continue
                rows.append({"Order Number": num, "Order Date": o["order_date"]})
            if not d["pageInfo"]["hasNextPage"]:
                break
            cursor = d["pageInfo"]["endCursor"]
            if r["extensions"]["throttling"]["user_quota"]["credits_remaining"] < 800:
                time.sleep(8)
    rows.sort(key=lambda r: r["Order Date"])
    return rows


def fetch_holds_via_statuses(token, inflight_statuses):
    """Lean hold sweep: only look at in-flight orders (much smaller than 30-day raw window)."""
    rows = []
    seen = set()
    for status in inflight_statuses:
        cursor = None
        for _ in range(20):
            after = f', after: "{cursor}"' if cursor else ""
            q = (
                f'{{ orders(fulfillment_status: "{status}") '
                f"{{ data(first: 100{after}) {{ pageInfo {{ hasNextPage endCursor }} "
                "edges { node { order_number order_date fulfillment_status "
                "holds { fraud_hold address_hold shipping_method_hold operator_hold payment_hold client_hold } "
                "} } } } }"
            )
            r = gql(token, q)
            if r.get("errors"):
                print(f"  Hold ERR status={status!r}: {r['errors']}")
                break
            d = r["data"]["orders"]["data"]
            for e in d["edges"]:
                o = e["node"]
                if o["order_number"] in seen:
                    continue
                seen.add(o["order_number"])
                h = o.get("holds") or {}
                reasons = [k.replace("_hold", "") for k in HOLD_FIELDS if h.get(k)]
                if not reasons:
                    continue
                rows.append({
                    "Order Number": o["order_number"],
                    "Order Date": o["order_date"],
                    "Status": o["fulfillment_status"] or "",
                    "Hold reasons": ", ".join(reasons),
                })
            if not d["pageInfo"]["hasNextPage"]:
                break
            cursor = d["pageInfo"]["endCursor"]
            if r["extensions"]["throttling"]["user_quota"]["credits_remaining"] < 800:
                time.sleep(8)
    rows.sort(key=lambda r: r["Order Date"])
    return rows


def write_tabs(sheets, sid, orders_rows, bo_sku_rows, bo_orderlines_rows, hold_rows, prior_notes=None):
    prior_notes = prior_notes or {}
    TAB1 = "Fulfillable Orders >48h"
    TAB2 = "Backordered SKUs"
    TAB3 = "Orders Affected by Backorder"
    TAB4 = "On Hold"
    meta = sheets.spreadsheets().get(spreadsheetId=sid).execute()
    existing = {s["properties"]["title"]: s["properties"]["sheetId"] for s in meta["sheets"]}

    requests = []
    first = meta["sheets"][0]["properties"]
    if first["title"] != TAB1:
        requests.append({"updateSheetProperties": {
            "properties": {"sheetId": first["sheetId"], "title": TAB1},
            "fields": "title",
        }})
        existing.pop(first["title"], None)
        existing[TAB1] = first["sheetId"]
    for t in (TAB2, TAB3, TAB4):
        if t not in existing:
            requests.append({"addSheet": {"properties": {"title": t}}})
    if requests:
        sheets.spreadsheets().batchUpdate(spreadsheetId=sid, body={"requests": requests}).execute()
        meta = sheets.spreadsheets().get(spreadsheetId=sid).execute()
        existing = {s["properties"]["title"]: s["properties"]["sheetId"] for s in meta["sheets"]}

    def _write_tab(title, gid, rows, headers, fmt_row, basic_filter=False, highlight_note_keys=None, key_col=None):
        # Clear contents AND remove any previous basic filter so we can re-set it cleanly
        sheets.spreadsheets().values().clear(spreadsheetId=sid, range=f"'{title}'").execute()
        try:
            sheets.spreadsheets().batchUpdate(spreadsheetId=sid, body={"requests": [
                {"clearBasicFilter": {"sheetId": gid}},
            ]}).execute()
        except Exception:
            pass
        if not rows:
            sheets.spreadsheets().values().update(
                spreadsheetId=sid, range=f"'{title}'!A1", valueInputOption="USER_ENTERED",
                body={"values": [[f"None for {title}."]]},
            ).execute()
            return
        values = [headers] + [fmt_row(r) for r in rows]
        sheets.spreadsheets().values().update(
            spreadsheetId=sid, range=f"'{title}'!A1", valueInputOption="USER_ENTERED",
            body={"values": values},
        ).execute()
        reqs = [
            {"updateSheetProperties": {
                "properties": {"sheetId": gid, "gridProperties": {"frozenRowCount": 1}},
                "fields": "gridProperties.frozenRowCount",
            }},
            {"repeatCell": {
                "range": {"sheetId": gid, "startRowIndex": 0, "endRowIndex": 1},
                "cell": {"userEnteredFormat": {"textFormat": {"bold": True}}},
                "fields": "userEnteredFormat.textFormat.bold",
            }},
            {"autoResizeDimensions": {
                "dimensions": {"sheetId": gid, "dimension": "COLUMNS", "startIndex": 0, "endIndex": len(headers)},
            }},
        ]
        if basic_filter:
            reqs.append({"setBasicFilter": {
                "filter": {
                    "range": {
                        "sheetId": gid,
                        "startRowIndex": 0,
                        "endRowIndex": len(values),
                        "startColumnIndex": 0,
                        "endColumnIndex": len(headers),
                    }
                }
            }})
        # Highlight Notes cell with light orange for rows whose note was carried forward from a prior sheet
        if highlight_note_keys and key_col and "Notes" in headers and key_col in headers:
            key_idx = headers.index(key_col)
            note_idx = headers.index("Notes")
            for row_pos, row_vals in enumerate(values[1:], start=1):  # start=1 because row 0 is header
                if len(row_vals) > key_idx and row_vals[key_idx] in highlight_note_keys:
                    reqs.append({"repeatCell": {
                        "range": {
                            "sheetId": gid,
                            "startRowIndex": row_pos,
                            "endRowIndex": row_pos + 1,
                            "startColumnIndex": note_idx,
                            "endColumnIndex": note_idx + 1,
                        },
                        "cell": {"userEnteredFormat": {
                            "backgroundColor": {"red": 0.988, "green": 0.898, "blue": 0.804},
                        }},
                        "fields": "userEnteredFormat.backgroundColor",
                    }})
        sheets.spreadsheets().batchUpdate(spreadsheetId=sid, body={"requests": reqs}).execute()

    def fmt_order(r):
        d = r["Order Date"]
        try:
            d = datetime.fromisoformat(d.replace("Z", "")).strftime("%Y-%m-%d %H:%M")
        except Exception:
            pass
        return [r["Order Number"], d]

    def fmt_hold(r):
        d = r["Order Date"]
        try:
            d = datetime.fromisoformat(d.replace("Z", "")).strftime("%Y-%m-%d %H:%M")
        except Exception:
            pass
        return [r["Order Number"], d, r["Status"], r["Hold reasons"]]

    # Aggregate long-form bo_orderlines_rows into one-row-per-order wide form
    from collections import defaultdict
    wide = defaultdict(lambda: {"date": "", "source": "", "skus": [], "total": 0})
    for r in bo_orderlines_rows:
        w = wide[r["Order Number"]]
        w["date"] = r["Order Date"]
        w["source"] = r.get("Source", "")
        w["skus"].append(f'{r["Product"]} -{r["Backordered (pcs)"]}')
        w["total"] += r["Backordered (pcs)"]
    wide_rows = [
        {"Order Number": k, "Order Date": v["date"], "Source": v["source"],
         "# Backordered SKUs": len(v["skus"]),
         "Total pcs short": v["total"],
         "Backordered SKUs": ", ".join(v["skus"])}
        for k, v in wide.items()
    ]
    wide_rows.sort(key=lambda r: r["Order Date"])

    def fmt_wide(r):
        d = r["Order Date"]
        try:
            d = datetime.fromisoformat(d.replace("Z", "")).strftime("%Y-%m-%d %H:%M")
        except Exception:
            pass
        return [r["Order Number"], d, r["Source"], r["# Backordered SKUs"], r["Total pcs short"], r["Backordered SKUs"]]

    notes_orders = prior_notes.get(TAB1, {})
    notes_bo_sku = prior_notes.get(TAB2, {})
    notes_orderbo = prior_notes.get(TAB3, {})
    notes_holds = prior_notes.get(TAB4, {})

    _write_tab(TAB1, existing[TAB1], orders_rows,
               ["Order Number", "Order Date", "Notes"],
               lambda r: fmt_order(r) + [notes_orders.get(r["Order Number"], "")],
               highlight_note_keys=set(notes_orders.keys()), key_col="Order Number")
    _write_tab(TAB2, existing[TAB2], bo_sku_rows,
               ["SKU", "Product", "Warehouse", "On Hand", "Backorder (pcs short)",
                "Delta vs prior", "Prior units short", "Allocated", "Available", "Notes"],
               lambda r: [r["SKU"], r["Product"], r["Warehouse"], r["On Hand"],
                          r["Backorder (pcs short)"],
                          r.get("Delta vs prior", ""), r.get("Prior units short", ""),
                          r["Allocated"], r["Available"], notes_bo_sku.get(r["SKU"], "")],
               basic_filter=True,
               highlight_note_keys=set(notes_bo_sku.keys()), key_col="SKU")
    _write_tab(TAB3, existing[TAB3], wide_rows,
               ["Order Number", "Order Date", "Source", "# Backordered SKUs", "Total pcs short", "Backordered SKUs", "Notes"],
               lambda r: fmt_wide(r) + [notes_orderbo.get(r["Order Number"], "")],
               highlight_note_keys=set(notes_orderbo.keys()), key_col="Order Number")
    _write_tab(TAB4, existing[TAB4], hold_rows,
               ["Order Number", "Order Date", "Status", "Hold reasons", "Notes"],
               lambda r: fmt_hold(r) + [notes_holds.get(r["Order Number"], "")],
               highlight_note_keys=set(notes_holds.keys()), key_col="Order Number")


def n_business_days_ago(d, n):
    count = 0
    while count < n:
        d -= timedelta(days=1)
        if d.weekday() < 5:
            count += 1
    return d


def create_dated_sheet(drive, region, today):
    """Create a fresh Google Sheet in the folder, named 'AUS Order Overview - 2026-05-19',
    grant anyone-with-link writer permission so the team can leave comments inline,
    return (sheet_id, url)."""
    name = f"{region} Order Overview - {today}"
    res = drive.files().create(
        body={"name": name, "mimeType": "application/vnd.google-apps.spreadsheet", "parents": [FOLDER_ID]},
        fields="id,name,webViewLink",
    ).execute()
    drive.permissions().create(
        fileId=res["id"], body={"type": "anyone", "role": "writer"}, fields="id",
    ).execute()
    return res["id"], res["webViewLink"]


def find_prior_sheet(drive, region, today):
    """Find the most recent dated sheet for `region` before `today`. Returns sheet_id or None."""
    pattern = re.compile(rf"^{region} Order Overview - (\d{{4}}-\d{{2}}-\d{{2}})$")
    q = f"'{FOLDER_ID}' in parents and trashed = false and mimeType = 'application/vnd.google-apps.spreadsheet'"
    res = drive.files().list(q=q, fields="files(id,name)", pageSize=200).execute()
    best_date = None
    best_id = None
    for f in res.get("files", []):
        m = pattern.match(f["name"])
        if not m:
            continue
        try:
            d = date.fromisoformat(m.group(1))
        except ValueError:
            continue
        if d < today and (best_date is None or d > best_date):
            best_date = d
            best_id = f["id"]
    return best_id, best_date


def load_prior_notes(sheets, prior_sheet_id, tab_title, key_col):
    """Read a tab from a prior sheet and return {key: notes}. Empty notes excluded."""
    if not prior_sheet_id:
        return {}
    try:
        res = sheets.spreadsheets().values().get(
            spreadsheetId=prior_sheet_id, range=f"'{tab_title}'!A:Z",
        ).execute()
    except Exception:
        return {}
    rows = res.get("values", [])
    if len(rows) < 2:
        return {}
    headers = rows[0]
    if "Notes" not in headers or key_col not in headers:
        return {}
    key_idx = headers.index(key_col)
    note_idx = headers.index("Notes")
    out = {}
    for r in rows[1:]:
        if len(r) <= max(key_idx, note_idx):
            continue
        k = r[key_idx]
        n = r[note_idx]
        if k and n and n.strip():
            out[k] = n
    return out


def load_prior_snapshot(region, today):
    """Find the most recent prior history snapshot for `region` before `today`.
    Returns dict of {sku: units_short} or None if no prior exists."""
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    pattern = re.compile(rf"^(\d{{4}}-\d{{2}}-\d{{2}})_{region}\.json$")
    best_date = None
    best_path = None
    for p in HISTORY_DIR.glob(f"*_{region}.json"):
        m = pattern.match(p.name)
        if not m:
            continue
        try:
            d = date.fromisoformat(m.group(1))
        except ValueError:
            continue
        if d < today and (best_date is None or d > best_date):
            best_date = d
            best_path = p
    if not best_path:
        return None, None
    data = json.loads(best_path.read_text())
    return best_date, {row["SKU"]: row["Backorder (pcs short)"] for row in data}


def save_snapshot(region, today, bo_sku_rows):
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    out = HISTORY_DIR / f"{today}_{region}.json"
    out.write_text(json.dumps(bo_sku_rows, indent=2))


def prune_history(today, keep_days=14):
    """Trash history files older than `keep_days`."""
    if not HISTORY_DIR.exists():
        return []
    cutoff = today - timedelta(days=keep_days)
    pattern = re.compile(r"^(\d{4}-\d{2}-\d{2})_[A-Z]+\.json$")
    pruned = []
    for p in HISTORY_DIR.iterdir():
        m = pattern.match(p.name)
        if not m:
            continue
        try:
            d = date.fromisoformat(m.group(1))
        except ValueError:
            continue
        if d < cutoff:
            p.unlink()
            pruned.append(p.name)
    return pruned


def compute_deltas(bo_sku_rows, prior_map):
    """Annotate each SKU row with delta vs prior snapshot. Mutates rows in place.

    prior_map: {sku: units_short} from previous run, or None if no prior data."""
    for r in bo_sku_rows:
        if prior_map is None:
            r["Delta vs prior"] = ""
            r["Prior units short"] = ""
            continue
        sku = r["SKU"]
        prior = prior_map.get(sku)
        cur = r["Backorder (pcs short)"]
        if prior is None:
            r["Delta vs prior"] = "new"
            r["Prior units short"] = 0
        else:
            d = cur - prior
            r["Delta vs prior"] = f"{d:+d}" if d != 0 else "0"
            r["Prior units short"] = prior


def archive_old_sheets(drive, today, keep_days=14):
    """Trash dated overview sheets in the folder older than `keep_days`.
    Recognises names of the form '<REGION> Order Overview - YYYY-MM-DD'."""
    cutoff = today - timedelta(days=keep_days)
    pattern = re.compile(r" Order Overview - (\d{4}-\d{2}-\d{2})$")
    q = f"'{FOLDER_ID}' in parents and trashed = false and mimeType = 'application/vnd.google-apps.spreadsheet'"
    res = drive.files().list(q=q, fields="files(id,name)", pageSize=200).execute()
    trashed = []
    for f in res.get("files", []):
        m = pattern.search(f["name"])
        if not m:
            continue
        try:
            file_date = date.fromisoformat(m.group(1))
        except ValueError:
            continue
        if file_date < cutoff:
            drive.files().update(fileId=f["id"], body={"trashed": True}).execute()
            trashed.append(f["name"])
    return trashed


def run_region(region, drive, sheets, today, cutoff_iso):
    cfg = REGIONS[region]
    print(f"\n=== {region} ===")
    token = shiphero_token(region)

    bo_orders, bo_orderlines = fetch_backordered_orders_with_lines(token)
    print(f"  Backordered orders: {len(bo_orders)} | order-SKU rows: {len(bo_orderlines)}")

    # Cross-validate against real orders: only SKUs that appear on an actual backordered order count.
    # Drops phantom inventory state (SKUs ShipHero reports as backordered with no customer commitment behind it).
    valid_skus = {row["SKU"] for row in bo_orderlines}
    bo_sku_rows, p = fetch_backordered_skus_via_products(token, valid_skus=valid_skus)
    prior_date, prior_map = load_prior_snapshot(region, today)
    compute_deltas(bo_sku_rows, prior_map)
    print(f"  Backordered SKUs: {len(bo_sku_rows)} (paged {p}x){' | prior: ' + str(prior_date) if prior_date else ' | no prior'}")
    for r in bo_sku_rows[:15]:
        delta = r.get("Delta vs prior") or ""
        delta_str = f" [{delta}]" if delta and delta != "0" else ""
        print(f"    {r['Product']} ({r['SKU']}): -{r['Backorder (pcs short)']} pcs{delta_str}")

    orders_rows = fetch_fulfillable_old(token, cfg["inflight"], cutoff_iso, bo_orders)
    print(f"  Fulfillable orders >48h: {len(orders_rows)}")

    hold_rows = fetch_holds_via_statuses(token, cfg["inflight"])
    print(f"  Orders on hold: {len(hold_rows)}")
    for r in hold_rows[:10]:
        print(f"    {r['Order Number']} ({r['Order Date'][:10]}): {r['Hold reasons']}")

    prior_sid, prior_date = find_prior_sheet(drive, region, today)
    prior_notes = {}
    if prior_sid:
        print(f"  Prior sheet: {prior_date} -> {prior_sid}")
        prior_notes = {
            "Fulfillable Orders >48h": load_prior_notes(sheets, prior_sid, "Fulfillable Orders >48h", "Order Number"),
            "Backordered SKUs": load_prior_notes(sheets, prior_sid, "Backordered SKUs", "SKU"),
            "Orders Affected by Backorder": load_prior_notes(sheets, prior_sid, "Orders Affected by Backorder", "Order Number"),
            "On Hold": load_prior_notes(sheets, prior_sid, "On Hold", "Order Number"),
        }
        total_notes = sum(len(v) for v in prior_notes.values())
        print(f"  Carried-forward notes: {total_notes}")

    sid, url = create_dated_sheet(drive, region, today)
    write_tabs(sheets, sid, orders_rows, bo_sku_rows, bo_orderlines, hold_rows, prior_notes=prior_notes)
    save_snapshot(region, today, bo_sku_rows)
    print(f"  Sheet: {url}")

    return {
        "region": region, "sheet_id": sid, "url": url,
        "fulfillable_count": len(orders_rows),
        "bo_skus": bo_sku_rows, "holds": len(hold_rows),
        "prior_snapshot_date": str(prior_date) if prior_date else None,
    }


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: region_order_overview.py <AUS|UK|CA|ALL>")
    target = sys.argv[1].upper()
    if target != "ALL" and target not in REGIONS:
        sys.exit(f"Unknown region {target!r}. Choose from AUS, UK, CA, ALL.")
    regions = list(REGIONS.keys()) if target == "ALL" else [target]

    today = date.today()
    cutoff = n_business_days_ago(today, 2)
    cutoff_iso = (cutoff + timedelta(days=1)).strftime("%Y-%m-%d") + "T00:00:00"
    print(f"Today: {today} | cutoff: orders dated <= {cutoff}")

    creds = Credentials.from_authorized_user_file(ADC_PATH, scopes=["https://www.googleapis.com/auth/drive"])
    creds.refresh(Request())
    drive = build("drive", "v3", credentials=creds, cache_discovery=False)
    sheets = build("sheets", "v4", credentials=creds, cache_discovery=False)

    results = [run_region(r, drive, sheets, today, cutoff_iso) for r in regions]

    print("\n=== Archiving older than 14 days ===")
    trashed = archive_old_sheets(drive, today, keep_days=14)
    if trashed:
        for name in trashed:
            print(f"  trashed: {name}")
    else:
        print("  (nothing to trash)")
    pruned_history = prune_history(today, keep_days=14)
    if pruned_history:
        print(f"  pruned history snapshots: {len(pruned_history)}")

    print("\n=== Summary ===")
    for r in results:
        print(f"  {r['region']:4s} fulfillable>48h={r['fulfillable_count']:>4d}  BO SKUs={len(r['bo_skus']):>3d}  holds={r['holds']}  -> {r['url']}")

    # Emit structured JSON for the calling skill (or other downstream automation)
    out_path = Path("/tmp/order_overview_last_run.json")
    payload = {
        "date": str(today),
        "regions": [
            {
                "region": r["region"],
                "url": r["url"],
                "sheet_id": r["sheet_id"],
                "fulfillable_count": r["fulfillable_count"],
                "holds": r["holds"],
                "prior_snapshot_date": r.get("prior_snapshot_date"),
                "bo_skus": [
                    {
                        "sku": s["SKU"],
                        "product": s["Product"],
                        "units_short": s["Backorder (pcs short)"],
                        "delta_vs_prior": s.get("Delta vs prior", ""),
                        "prior_units_short": s.get("Prior units short", ""),
                    }
                    for s in r["bo_skus"]
                ],
            }
            for r in results
        ],
        "archived": trashed,
    }
    out_path.write_text(json.dumps(payload, indent=2))
    print(f"\nJSON: {out_path}")


if __name__ == "__main__":
    main()
