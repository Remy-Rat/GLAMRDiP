# Airtable Stock Tracking — Build Plan

## Goal
Replace per-PO spreadsheets (unscalable) and sit alongside Greg's portal (opaque) with a single Airtable base that tracks raw-good POs, CN POs, transfers, and allocations. Team-readable, no custom hosting, no Odoo dependency until that's set up.

## Why Airtable (not custom webapp)
- Transparent data model — team can read rollup formulas, not just trust output
- No hosting / no deploy pipeline
- Joel / Daniel / Greg can view without a custom dashboard being built
- Scales across all suppliers in one base (vs one workbook per PO)
- When something drifts from the portal, we have an auditable second source of truth

## Data model (Airtable tables)

| Table | Key fields |
|---|---|
| **Suppliers** | Name, Type (Raw goods / Filler / Buffer), Region |
| **SKUs** | SKU code, Name, Category, Default Supplier |
| **Raw Good POs** | PO Number, Supplier (link), PO Date, Status, Invoice, Lines (count), Total Ordered (rollup), Total Transferred (rollup), Remaining (formula) |
| **PO Lines** | Raw Good PO (link), SKU (link), Qty Ordered, Units Transferred (rollup), Remaining (formula) |
| **CN POs** | CN Filing Number, Region, Date, Total Allocated (rollup) |
| **Transfers** | Date, From (Supplier link), To (Supplier link), SKU (link), Units, PO Line (link → the specific PO+SKU line), CN PO (link, optional), Flow Type (formula), Status (Approved/Rejected) |

### Why a separate "PO Lines" table
Each PO has multiple SKUs with their own quantities. Transfers tie to a specific (PO × SKU) line, which gives per-line rollups for "remaining" without ambiguity.

## FIFO handling
- Transfer form: "PO Line" dropdown is filtered to `Supplier = selected, SKU = selected, Remaining > 0`, sorted **PO Date ascending** → oldest appears first.
- Overflow (transfer qty > PO Line remaining): user adds a second transfer row against the next-oldest PO Line. Same pattern as Greg's portal "+ Add Line".
- Optional: Airtable Script automation on transfer save to hard-enforce FIFO — flag if a newer PO is selected while an older one still has stock.

## Flow Type logic (formula on Transfer)
Same classification our reconciliation script uses:
- PO Line + CN PO set, To = Sally → `DIRECT_TO_CN`
- PO Line set, CN PO blank → `BUFFER_FEED` (source → intermediate)
- PO Line blank, CN PO set → `BUFFER_FORWARD` (intermediate → Sally)
- PO Line + CN PO set, To ≠ Sally → `BUFFER_FEED_TAGGED` (pre-tagged, e.g. Hether → Lily)
- CN PO = "CN-OPENING" → `OPENING_SEED`

## Pilot plan — start with Mark / JARs
Mark's catalogue is small and self-contained (4 SKUs on PO-28-03-26-MARK: `UK/EU-EMPTY-JAR`, `ACC-JAR-LIDS`, plus 2 others). Good pilot because:
- Simple supplier, no buffer intermediaries
- Direct-to-Sally flow only (no VIA_BUFFER complexity)
- Multiple active Mark POs exist → FIFO gets exercised immediately
- If accuracy matches Greg's portal for Mark for 2 weeks, extend pattern to the rest

**Pilot steps:**
1. Build base structure with all tables (empty)
2. Populate Suppliers, SKUs (Mark's 4 SKUs only), Raw Good POs, PO Lines for Mark's POs
3. Import Mark's historical transfers from today's reconciliation export
4. Verify rollups match portal's Remaining values
5. Build one Interface Designer page: "PO Detail" — shows Remaining + allocation breakdown
6. Run parallel for 2 weeks (new Mark transfers entered in both systems)

## Scale — 2000 SKUs
Fine for Airtable. Limits:
- Team plan: 50,000 records/base, $20/user/month
- 2000 SKUs × 1 record each = 4% of the limit
- Transfers grow ~1,000–1,500/year at current volumes → 5 years = 7,500 records. Plenty of headroom
- Do SKU import in CSV batches; don't hand-type

## Transfer input — start with option (a)
- **Keep Greg's portal for supplier transfer entry.** Suppliers don't re-learn anything.
- Greg publishes (or we export) the transfer log weekly into a Google Sheet
- Airtable Sync pulls that Sheet into the Transfers table
- Our rollups recompute Remaining continuously
- If portal and Airtable diverge, we investigate — Airtable is the independent audit

Later (if warranted): **option (b)** — replace portal with Airtable Forms per supplier + admin approval automation. Full consolidation, more work.

## Open items before build starts
- Confirm whether Greg's portal can export transfers to a Google Sheet on a schedule (enables option a cleanly)
- Decide: rebuild PO entry in Airtable (makes Airtable PO source of truth) or also sync POs from Greg's portal (mirror only, less work)
- Get a full SKU master export — ideally one CSV of all ~2000 SKUs with codes, names, default supplier
- Confirm Interface Designer viewer seats are free on Team plan for Joel / Daniel / Greg

## Known issues to watch (from 2026-04-17 reconciliation)
- 4 non-Sally PO variances in the portal (Bill +1,728; Kay +900; Palin -500, +480). Needs Greg to explain.
- 2 orphan forwards at Sally (TIP-ALM-BOX, TIP-SQU-BOX). Likely missed seed rows.
- Sally's raw-good POs under-reconcile by 500k+ units because fulfillment consumption isn't in the transfer export. Need Greg's shipment/fulfillment feed too if we want to close Sally's accounting.

## Re-runnable audit today
Until the base is built, `Ops/Scripts/po_reconciliation.py` produces the same reconciliation from a PO Lots CSV + Transfer History XLSX. Output: `Ops/Suppliers/PO_Reconciliation_YYYY-MM-DD.xlsx`.
