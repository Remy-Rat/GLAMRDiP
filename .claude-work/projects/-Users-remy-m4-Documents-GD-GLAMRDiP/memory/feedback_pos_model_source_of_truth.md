---
name: POS MODEL is source of truth for DSR
description: Always use POS MODEL tab (not DSR tab) for model DSR values and growth factor calculations
type: feedback
---

POS MODEL tab in the Order Schedule xlsx is the source of truth for live DSR and growth factor — NOT the DSR tab.

**Why:** The DSR tab contains historical cross-checked values that lag behind the live forecast. Growth factor scales the sum of live kit DSRs (e.g. 34+78+35=147, at 1.3x = 191/day), not a fixed 80 kits/day base.

**How to apply:** When running any sales analysis or inventory calculation, pull model DSR from POS MODEL. Kit DSRs are in the header rows (rows 1-3). Per-SKU DSR is derived from G3PL ON HAND ÷ DAYS COVER in the product table. The Component Map should only show kit composition and example calculations, not be treated as a source of truth for growth factor numbers.
