---
name: Regional SKU quirks for inventory analysis
description: SKU names and packaging rules that vary by region — must check per region before analysis
type: feedback
---

**ACC-LAB (Labels Booklet) is region-suffixed:**
- AUS: `ACC-LAB`
- CA: `ACC-LAB-CA`
- UK: `ACC-LAB-UK`
- Nordic: TBD — check when running

**Why:** Each region has region-specific compliance booklets with different content. The SKU suffix identifies the region.

**STO-BUB-BAG-S (Bubble Wrap Liquid Pocket):**
- AUS: tracked in G3PL, deducted from stock
- CA: 247 Fulfilment supplies their own — does NOT appear in B360 data. Not a stock concern.
- UK/Nordic: TBD

**How to apply:** When running POS Check or Sales Analysis, check region-specific SKU names for labels. If a packaging SKU shows 0 in 3PL data, check if the 3PL supplies it themselves before flagging as OOS.
