# Improvement Roadmap — last updated 17 Apr 2026

## Completed
- [x] **Google Drive connection** — gcloud CLI, read-only export of all 4 Order Schedules
- [x] **Slack + Gmail cross-referencing** — integrated into Region Recap and POS Check
- [x] **Per-region component maps** — inventory config in each Region file
- [x] **CNTR TRACKER retired** — arrivals detected from 3PL data, POS MODEL header for dates
- [x] **Deduction benchmarks** — per-SKU red flags from Greg's spreadsheet
- [x] **Sales spike/drop detection** — with CRO + sale-announcements channel cross-reference
- [x] **Stock-out forecasting** — with lead time framework (84/44/30d deadlines)
- [x] **PO recommendation logic** — in POS Check skill (Step 10)
- [x] **Actions-from-last-review tracker** — required section in Recap (17 Apr 2026) — surfaces stale/missed action items across reviews
- [x] **Red flag deduction investigation methodology** — classify each flag as Explained / Unexplained in Sales Analysis; added cumulative 3PL-vs-Shopify gap test
- [x] **Dual-DSR stock coverage view** — model (1.3x) / 3PL actual / Shopify 30d shown side-by-side in POS Check
- [x] **Container gap analysis** — explicit "what's missing from in-flight containers" step in POS Check
- [x] **Local fill sizing formula** — explicit lead-time + growth-factor math with lean/recommended/conservative options
- [x] **Manual override convention** — surface deltas between POS MODEL sheet and known same-day events (Gmail/Slack) at top of POS Check
- [x] **Step 0a Gmail reconcile in POS Check** — mandatory step before cover math (17 Apr 2026) — catches POS MODEL paste-time vs evening-event lag
- [x] **`/full-review` pause discipline** — mandatory pauses between phases with 3-finding + 4-question template (17 Apr 2026). Prevents stale data cascading downstream.
- [x] **"Always re-pull xlsx" rule** — explicit in POS Check + Sales Analysis data sources (17 Apr 2026)

## Priority 1 — Next up
- [ ] **Supplier scorecard** — track promised vs actual lead times per supplier (Avi, Peter/OP, Sally, Chemence, Mixam, Zakka). File at `Ops/Context/Supplier Scorecard.md`. Update each review. Gives leverage in conversations and catches chronic slippers.
- [ ] **CX health panel in weekly cycle** — pull orders >48hr, returns in progress, customs/tracking failures from #glamrdip-g3pl / #glamrdip-ca-247 / equivalent. Currently invisible in reports despite being real customer risk.
- [ ] **Standalone analysis script** — write `analysis.py` in this repo. Pre-generates POS Check + Sales Analysis data. Claude still reviews, interprets, and adds Slack/Gmail context on top.
- [ ] **Scheduled runs** — script runs on review schedule (Mon=AUS, Tue=UK, Wed=CA, Fri=Nordic). Data ready when Remy starts the review. Recap still done interactively.

## Priority 2 — When 3PL transitions settle (2-4 weeks)
- [ ] **Local filler packaging sheets** — Remy has Google Sheets tracking packaging held at each filler (Oils4Life, Chemence, Outsource Packaging, Swift, etc.). Connect these so POS Check can cross-reference: how many empty bottles/lids/brushes the filler has on hand → how many fills they can do before needing a packaging top-up from the 3PL or CN.
- [ ] **Shopify OOS check** — flag products marked OOS on the website that still have stock at the 3PL. Revenue leak detection.
- [ ] **DSR staleness detection** — flag when POS MODEL DSR drifts >30% from actual Shopify DSR for 3+ consecutive weeks. Prompt Greg to refresh.
- [ ] **Fulfillable PO data** — once UK stabilises, check if Fulfillable has equivalent PO export for check-in tracking (like ShipHero for AUS).

## Priority 3 — Medium-term (1-2 months)
- [ ] **Sally PO Tracker + Lily Shipment Tracker** — connect as Google Sheets. Enables live production/shipping data in forecasts instead of stale POS MODEL dates.
- [ ] **PO recommendation templates** — generate actual recommended PO with SKU quantities (not just "place by X date"). Feeds into Daniel's PO procedure workflow.
- [ ] **Cross-regional summary** — one-page view of all 4 regions side by side. Kit performance, critical items, upcoming deadlines. For Joel's Monday overview.
- [ ] **Historical trend tracking** — compare archived reviews week-over-week. "AUS kits up 13% this week" or "Base flagged critical for 3 consecutive weeks."

## Priority 4 — Longer-term (3+ months)
- [ ] **Marketing ↔ inventory feedback loop** — "500d of colour X idle → Gav run a campaign" or "stocking out of Y → pause ads." Bridge between Ops and Marketing.
- [ ] **Supplier performance tracking** — actual vs promised lead times over time (Chemence, G3PL, Sally). Better forecasting + leverage in conversations.
- [ ] **Cashflow-aware ordering** — factor payment schedules and deposit timelines into PO recommendations. "3 deposits due this month, recommend deferring Nordic fill by 2 weeks."
