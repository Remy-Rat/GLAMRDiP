# Ops — CLAUDE.md

## When Starting Any Ops Task

1. Read `Context/Current Issues.md` — know what's live right now
2. Read `Regions/[REGION].md` — get contacts, channels, 3PL, suppliers
3. Read the relevant `Skills/` file for the task type
4. If calculating demand, read `../Shared/Component Map.md`
5. If emailing or escalating to a supplier, check the supplier section in the Region file

## Context Files (situational awareness)
- `Context/Current Issues.md` — active problems per region, updated after every review
- `Context/Upcoming Orders.md` — what's in production, planned, pending deposit
- `Context/Recent Decisions.md` — decisions from Joel/Daniel that affect ops

## Skills (task procedures)
- `Skills/Weekly Inventory Summary.md` — Monday morning routine, all 5 channels
- `Skills/Region Recap.md` — deep dive on one region (Slack + Gmail + synthesis)
- `Skills/POS Model Check.md` — stock position check using ShipHero PO data (confirmed vs pending vs quarantined, check-in progress, double-count detection, packaging monitoring)
- `Skills/Sales Data Analysis.md` — full xlsx analysis (DSR, days cover, discrepancies, trends)

## Key Operational Rules
- **AUS** uses `AUS 3GPL` tab in the order schedule xlsx (NOT `B360` — that's the old 3PL)
- **UK** is transitioning from Borderless 360 (B360) to Fulfillable (mid-April 2026)
- **Nordic** transitioned from Dippi brand to GLAMRDiP (completed late March 2026)
- **Kit-adjusted demand** for liquids = standalone Shopify sales + kit consumption. The model DSR often only captures standalone. ALWAYS calculate kit-adjusted. See `../Shared/Component Map.md` for formulas.
- **Growth factor** scales the sum of live kit DSRs from the POS MODEL tab. E.g. if kit DSRs total 147/day, then 1.3x = 191/day. POS MODEL is the source of truth for DSR — not the DSR tab.
- **B360 / G3PL future columns** are corrupted — Greg sets up date columns ahead of time but doesn't paste data until that day. Unpasted columns show as int64 min (-9223372036854775808) or NaN. Always detect the last valid date before analysis.
- **Shopify data has a +1 day lag** — pasted the day after.
- **Packaging SKUs** (STO-*, ACC-INS, ACC-THA) show 0 in Shopify — consumed at warehouse level inside kits. Exclude from Shopify DSR comparison.

## Post-Task: Always Update Context
After completing any review, recap, or analysis, update `Context/Current Issues.md` with the current state for the relevant region(s). Replace that region's section entirely — don't append. Keep it to the top 5-8 most important items. Include dates so staleness is visible.
