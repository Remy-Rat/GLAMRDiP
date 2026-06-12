#!/usr/bin/env python3
"""PO Audit - compare Recommended POs vs the team's placed Purchase Orders.

Read-only. Never writes to any source sheet or Notion.

Input: JSON file of entries (Claude builds this from a Notion query - see
Ops/Skills/PO Audit.md for the query):
    [{"label": "UK 30082026", "rec": "<url>", "po": "<url or null>",
      "status": "Placed order (waiting payment)", "payment": "Waiting Deposit"}]

Usage:
    python3 po_audit.py entries.json                  # print comparison report
    python3 po_audit.py entries.json --sheet "TITLE"  # also build audit Google Sheet

Handles both PO families automatically:
  - CN Filling: 'Quantities' tab, SKU in col A, QTY column found by header
  - Raw Goods:  'TEMPLATE' (or first) tab, SKU in col B, Qty column by header
PO links that are Drive folders are resolved to the Google Sheet inside
(empty folder / no sheet => flagged as possibly not placed).
"""
import json, re, sys, warnings
warnings.filterwarnings('ignore')
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

CRED = '/Users/remy-m4/.config/gcloud/legacy_credentials/remy@glamrdip.com/adc.json'
creds = Credentials.from_authorized_user_file(CRED, scopes=['https://www.googleapis.com/auth/drive'])
creds.refresh(Request())
drive = build('drive', 'v3', credentials=creds, cache_discovery=False)
sheets = build('sheets', 'v4', credentials=creds, cache_discovery=False)


def to_num(v):
    try:
        return float(str(v).replace(',', '').replace('$', '').strip())
    except ValueError:
        return None


def file_id(url):
    m = re.search(r'/d/([A-Za-z0-9_-]{20,})', url or '') or re.search(r'id=([A-Za-z0-9_-]{20,})', url or '')
    return m.group(1) if m else None


def resolve(url):
    """Return (sheet_id, note). Folder links resolve to the sheet inside."""
    if not url:
        return None, 'no Purchase Order link'
    m = re.search(r'/folders/([A-Za-z0-9_-]{20,})', url)
    if not m:
        return file_id(url), ''
    files = drive.files().list(q=f"'{m.group(1)}' in parents and trashed=false",
                               fields='files(id,name,mimeType)', supportsAllDrives=True,
                               includeItemsFromAllDrives=True).execute().get('files', [])
    ss = [f for f in files if f['mimeType'] == 'application/vnd.google-apps.spreadsheet']
    if not ss:
        return None, ('PO folder is EMPTY' if not files
                      else 'no Google Sheet in folder: ' + ', '.join(f['name'] for f in files))
    if len(ss) > 1:
        po = [f for f in ss if 'PO' in f['name'].upper() or 'PURCHASE' in f['name'].upper()]
        ss = po or ss
    return ss[0]['id'], f"(from folder: {ss[0]['name'].strip()})"


def read_items(sid):
    """Return (title, {sku: qty}). Auto-detects CN Filling vs Raw Goods layout."""
    meta = sheets.spreadsheets().get(spreadsheetId=sid,
                                     fields='properties.title,sheets.properties').execute()
    title = meta['properties']['title'].strip()
    tabs = [s['properties']['title'] for s in meta['sheets']]
    qtab = next((t for t in tabs if t.strip().lower() == 'quantities'), None)
    if qtab:  # CN Filling: SKU in col A
        vals = sheets.spreadsheets().values().get(
            spreadsheetId=sid, range=f"'{qtab}'!A1:N1200").execute().get('values', [])
        hdr = next(i for i, r in enumerate(vals) if r and str(r[0]).strip() == 'SKU')
        qcol = next(j for j, c in enumerate(vals[hdr]) if str(c).strip().upper() == 'QTY')
        skucol = 0
    else:     # Raw Goods: SKU in col B on TEMPLATE / Recommended Purchase Order / first tab
        tab = next((t for t in tabs if 'TEMPLATE' in t.upper() or 'PURCHASE' in t.upper()), tabs[0])
        vals = sheets.spreadsheets().values().get(
            spreadsheetId=sid, range=f"'{tab}'!A1:N100").execute().get('values', [])
        hdr = next((i for i, r in enumerate(vals) if len(r) > 1 and str(r[1]).strip() == 'SKU'), None)
        if hdr is None:
            return title, None
        qcol = next(j for j, c in enumerate(vals[hdr]) if str(c).strip().lower() == 'qty')
        skucol = 1
    items = {}
    for r in vals[hdr + 1:]:
        sku = str(r[skucol]).strip() if len(r) > skucol else ''
        if not sku or sku == '-':
            continue
        items[sku] = to_num(r[qcol]) or 0 if len(r) > qcol else 0
    return title, items


def audit(entries):
    results = []
    for e in entries:
        out = {'label': e['label'], 'status': e.get('status', ''), 'payment': e.get('payment') or 'BLANK',
               'result': '', 'po_title': '', 'diffs': [], 'note': ''}
        results.append(out)
        pid, note = resolve(e.get('po'))
        if not pid:
            out['result'] = 'NOT PLACED?'
            out['note'] = note
            continue
        try:
            _, rec = read_items(file_id(e['rec']))
            out['po_title'], po = read_items(pid)
        except Exception as ex:
            out['result'] = 'READ ERROR'
            out['note'] = str(ex)[:140]
            continue
        if rec is None or po is None:
            out['result'] = 'NO SKU TABLE'
            continue
        for s in sorted(set(rec) | set(po)):
            rv, pv = rec.get(s, 0) or 0, po.get(s, 0) or 0
            if rv != pv:
                why = 'not on placed PO' if s not in po else ('not in recommended' if s not in rec else '')
                out['diffs'].append([s, rv, pv, why])
        out['result'] = 'Match' if not out['diffs'] else f"DIFFERENCES ({len(out['diffs'])})"
    return results


def build_sheet(title, results):
    ss = sheets.spreadsheets().create(body={
        'properties': {'title': title},
        'sheets': [{'properties': {'title': 'Audit Summary', 'gridProperties': {'rowCount': 60, 'columnCount': 8}}},
                   {'properties': {'title': 'Differences & Notes', 'gridProperties': {'rowCount': 80, 'columnCount': 7}}}]
    }).execute()
    sid = ss['spreadsheetId']
    ids = {s['properties']['title']: s['properties']['sheetId'] for s in ss['sheets']}
    summary = [[title, '', '', '', ''],
               ['Read-only audit. Notes column to be annotated after review.', '', '', '', ''], [],
               ['PO', 'Status', 'Payment Status', 'Numbers result', 'Notes']]
    for r in results:
        summary.append([r['label'], r['status'], r['payment'], r['result'], r['note']])
    detail = [['Quantity differences (recommended vs placed)', '', '', '', ''],
              ['PO', 'SKU', 'Recommended', 'Placed', 'Assessment']]
    for r in results:
        for d in r['diffs']:
            detail.append([r['label'], d[0], f'{d[1]:,.0f}', f'{d[2]:,.0f}', d[3]])
    detail += [[], ['Internal notes', '', '', '', '']]
    sheets.spreadsheets().values().batchUpdate(spreadsheetId=sid, body={
        'valueInputOption': 'RAW',
        'data': [{'range': "'Audit Summary'!A1", 'values': summary},
                 {'range': "'Differences & Notes'!A1", 'values': detail}]}).execute()
    B = {'style': 'SOLID', 'width': 1}
    bold = lambda sh, r1, r2: {'repeatCell': {
        'range': {'sheetId': sh, 'startRowIndex': r1, 'endRowIndex': r2,
                  'startColumnIndex': 0, 'endColumnIndex': 5},
        'cell': {'userEnteredFormat': {'textFormat': {'bold': True}}},
        'fields': 'userEnteredFormat.textFormat.bold'}}
    reqs = [bold(ids['Audit Summary'], 0, 1), bold(ids['Audit Summary'], 3, 4),
            bold(ids['Differences & Notes'], 0, 2),
            {'updateBorders': {'range': {'sheetId': ids['Audit Summary'], 'startRowIndex': 3,
                                         'endRowIndex': 4 + len(results), 'startColumnIndex': 0, 'endColumnIndex': 5},
                               'top': B, 'bottom': B, 'left': B, 'right': B, 'innerHorizontal': B, 'innerVertical': B}},
            {'updateDimensionProperties': {'range': {'sheetId': ids['Audit Summary'], 'dimension': 'COLUMNS',
                                                     'startIndex': 0, 'endIndex': 1},
                                           'properties': {'pixelSize': 300}, 'fields': 'pixelSize'}},
            {'updateDimensionProperties': {'range': {'sheetId': ids['Audit Summary'], 'dimension': 'COLUMNS',
                                                     'startIndex': 4, 'endIndex': 5},
                                           'properties': {'pixelSize': 560}, 'fields': 'pixelSize'}}]
    ndiff = sum(len(r['diffs']) for r in results)
    if ndiff:
        reqs.append({'updateBorders': {'range': {'sheetId': ids['Differences & Notes'], 'startRowIndex': 1,
                                                 'endRowIndex': 2 + ndiff, 'startColumnIndex': 0, 'endColumnIndex': 5},
                                       'top': B, 'bottom': B, 'left': B, 'right': B,
                                       'innerHorizontal': B, 'innerVertical': B}})
    sheets.spreadsheets().batchUpdate(spreadsheetId=sid, body={'requests': reqs}).execute()
    return ss['spreadsheetUrl']


if __name__ == '__main__':
    entries = json.load(open(sys.argv[1]))
    results = audit(entries)
    for r in results:
        print(f"{r['label']}: {r['result']} {r['note']}")
        for d in r['diffs']:
            print(f"    {d[0]:28s} rec={d[1]:>10,.0f}  po={d[2]:>10,.0f}  {d[3]}")
    if '--sheet' in sys.argv:
        title = sys.argv[sys.argv.index('--sheet') + 1]
        print('\nAudit sheet:', build_sheet(title, results))
