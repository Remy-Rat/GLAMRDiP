# PO Audit — Recommended vs Placed

Read-only audit comparing our Recommended POs against the team's placed Purchase Orders in Notion. Flags quantity differences, missing/empty PO documents, and bookkeeping gaps. **Never edits any sheet or Notion entry.** First run 12 Jun 2026 (raw goods + CN filling).

## Constants (save the lookup)

- Notion database: **Master Financial Database**, data source `collection://2b8deea7-139d-81bb-891a-000bac531abe` (CN Filling Dashboard / Raw Goods Dashboard are views over it)
- `PO Type` values: `Raw Goods PO`, `CN Filling PO`, `Local Filling PO`, `Local Ingredients PO`, `Local Printing PO`
- Active statuses to audit: `Placed order (waiting payment)`, `In production` (add `Recommended` to catch unplaced)
- Script: `Ops/Scripts/po_audit.py` (uses remy@glamrdip.com legacy gcloud creds; read-only)

## Process

1. **Scope with Remy** — which PO type(s) and which entries (usually the active statuses above, or a screenshot of the dashboard view).
2. **Notion query** (via Notion MCP, one call):
   ```sql
   SELECT url, "PO Short Reference", "Status", "Payment Status",
          "Recommended PO", "Purchase Order"
   FROM "collection://2b8deea7-139d-81bb-891a-000bac531abe"
   WHERE "PO Type" = '<TYPE>' AND "Status" IN ('Placed order (waiting payment)', 'In production')
   ORDER BY "PO Short Reference"
   ```
3. **Build entries JSON** `[{label, rec, po, status, payment}]` and run:
   ```
   python3 Ops/Scripts/po_audit.py /tmp/entries.json --sheet "DD-MM-YYYY | <Type> PO Audit | Recommended vs Placed"
   ```
   The script resolves folder links to the sheet inside, auto-detects the sheet family (CN Filling = `Quantities` tab / SKU col A; Raw Goods = `TEMPLATE` tab / SKU col B), compares SKU-by-SKU, and builds a two-tab audit sheet (Audit Summary + Differences & Notes).
4. **Annotate** the generated sheet's Notes/Assessment columns — this is the judgement step (see triage below). Add an "Internal notes" section at the bottom of the Differences tab.
5. **Report to Remy**: lead with matches count, then real quantity flags, then housekeeping flags.

## Triage rules for differences (the judgement layer)

- **Before flagging, look for a V2/V3 recommendation file** in the same region/supplier Drive folder — Notion's Recommended PO link often points at a superseded version (e.g. AUS 07062026: placed PO matched "V2 AUS 07062026" exactly; V1 showed 10 false diffs). Flag the stale link, not the numbers.
- **SKU renames** — same qty appearing under a changed code is not a numbers flag (ACC-BRU-V2→ACC-BRU-NEW; typo fixes like ACCi-NAI-MAT-BOX→ACC-NAI-MAT-BOX).
- **Added lines may be absorbed cancellations** — check cancelled recommendations of the same date for matching quantities (e.g. cancelled Bubble Mailers 80,000 reappeared on the Cailang PO as 3-CUB-MAI).
- **Cross-supplier moves** — lines zeroed on one supplier and appearing on another at the same qty are a move, not two diffs (tips: Palin/Elephant → Cailang).
- **Split Notion entries** — two entries sharing the same rec+PO links with different totals = payment split (CA 21062026 + EXTRA); not a duplicate error.
- Everything left after triage is a genuine **CONFIRM with team** item (qty bumps, dropped lines, lines with no recommendation anywhere).

## Standing checks beyond quantities

- PO link missing, folder empty, or folder containing no sheet → "NOT PLACED?" flag
- Payment Status blank while status is "Placed order" → bookkeeping flag (whole CN Filling family was blank on first audit; raw goods normally carries "Waiting Deposit")
- Supplier name changes between recommendation and placed PO (Cuticle Presser: Yiwu Pinpin → Yangjiang Hongstars)
- Placed PO re-dated vs recommendation (team places later than rec date — informational only)

## Output naming

`DD-MM-YYYY | <Type> PO Audit | Recommended vs Placed`, lands in My Drive root (Remy moves it). Examples: 12-06-2026 raw goods `1ePEQl7CmVWjO8Jj1Mmvf91ib75hAMd6SAw14mSoSBIY`, CN filling `1h1IARjNJYYtFNcdrADBtRB2ryrRQHtNNkOKdTOubsbs`.
