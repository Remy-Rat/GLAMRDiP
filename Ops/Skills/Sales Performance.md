> **Context:** Get region info from `../Regions/[REGION].md`. This skill is a commercial lens — it does NOT update `../Context/Current Issues.md` (that's the inventory skill's job).

# Sales Performance Skill

## Trigger
User asks for sales check, selling performance, kit trends, colour trends, growth check, commercial performance, or "how are we selling". Also trigger for "what's trending", "kit mix check", "colour intelligence", or "repurchase signal".

---

## Data Sources

### Order Schedule xlsx (from Google Drive)
- **SHOPIFY** — daily unit sales per SKU. Source of truth for all selling rates.
- **POS MODEL** — growth factor and kit DSR targets. Used as the commercial benchmark.

### External Context (optional enrichment)
- **#sale-announcements** (C091PEBAS65) — active promos, discount codes. Cross-reference when spikes detected.
- **#cro-team-meetings** (C098QGQ6NLS) — CRO experiments that may be influencing conversion rates.

### Not Used
- 3PL tab — that's inventory accountability, not sales performance
- CNTR TRACKER, RECONCILIATION — irrelevant to sales lens

---

## Pre-built Scripts

Run `../Scripts/extract.py [REGION]` first, then pipe into the sales performance script:

```bash
uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py UK > /tmp/uk.json
cat /tmp/uk.json | uv run --with pandas python3 Ops/Scripts/sales_performance.py
```

The script handles all calculations. Use its output as the data foundation, then layer on commercial context from Slack channels (#sale-announcements, #cro-team-meetings) to explain the "why" behind the numbers.

---

## Step 1 — Growth Headline

The opening frame. Is the region growing, shrinking, or flat?

- Kit total DSR: 7d / 14d / 30d windows
- Momentum — compare windows to classify the trend:
  - **Accelerating**: 7d > 14d > 30d
  - **Decelerating**: 7d < 14d < 30d
  - **Peaking**: 7d < 14d > 30d (came up, now pulling back)
  - **Recovering**: 7d > 14d < 30d (was down, now coming back)
  - **Flat**: <5% variance across all windows
- Growth factor check: actual vs model target. Frame as a commercial health check — don't recommend lowering the growth factor; flag the gap as insight into whether the target is realistic or aspirational.
- One-line summary: e.g. "UK kits are accelerating — 93.7/d (7d) vs 83.5/d (30d), +12% momentum"

---

## Step 2 — Category Performance

Break sales into four categories. Show each category's size and direction.

### Kits (the core business)
- Total DSR: 7d / 14d / 30d
- Per-kit breakdown: STA, COM, ULT with DSR and % of total
- Kit mix interpretation: ULT-heavy = higher AOV, STA-heavy = more entry-level / ad-driven
- Flag any kit type with >20% gap between 7d and 30d DSR

### Liquids (repurchase signal)
- Standalone liquid DSR only (not kit-adjusted — this is about repeat purchase behaviour)
- Total standalone liquid DSR: 7d / 14d / 30d
- Per-SKU table for all liquids
- Liquid-to-kit ratio: total standalone liquid DSR / total kit DSR. Higher = more returning customers.
- Flag any liquid with >30% change between 7d and 30d

### Accessories (upsell & repeat)
- Remove 120ml, Remove 500ml, Remove Bowl: standalone Shopify DSR
- Bundle DSR: BUN-1, BUN-2, LIQ-SET (shows bundle attach rate)
- Other accessories: Manicure Kit, Pro File Set, etc.
- Flag any with >30% change between 7d and 30d

### Colours (catalogue breadth)
- Total colour DSR: 7d / 14d / 30d
- Active colours (selling >1/day): count
- Colours per kit: total colour DSR / total kit DSR (should approximate weighted avg of 3/6/9 based on kit mix)
- Flag if colour-to-kit ratio deviates from expected

---

## Step 3 — Weekly Kit Trend

8-week minimum. Show trajectory, not just snapshots.

- Weekly total kit sales, daily rate, vs model target
- 4-week rolling average for smoothing
- Week-over-week % change
- Flag: 3+ consecutive declining weeks, promo spikes (>30% above 4-week avg), post-promo hangover

Cross-reference #sale-announcements for promo timing if spikes/dips detected.

---

## Step 4 — Kit Mix Analysis

How the STA/COM/ULT balance is shifting.

- 14d mix vs 30d mix — direction of change
- Model mix (from POS MODEL base DSRs) vs actual mix
- Interpretation guide:
  - ULT share rising: customers choosing premium, AOV increasing
  - STA share rising: more first-timers or price-sensitive, could be ad-driven
  - COM declining: middle option losing appeal, could be CRO/pricing gap
- Note any CRO experiments from #cro-team-meetings that could affect mix

---

## Step 5 — Colour Intelligence

### Top 10 by Volume (14d)
The bestsellers. Show DSR and % of total colour volume.

### Top 10 Risers (7d vs 30d acceleration)
Colours with the biggest positive momentum. Only include colours selling >2/d (14d) to filter noise. These are genuinely trending — could be social, seasonal, or CRO-related.

### Top 10 Fallers (7d vs 30d deceleration)
Colours losing momentum. Only include colours selling >2/d (30d). Could be OOS on website, seasonal fade, or post-promo normalisation.

### Catalogue Efficiency
- How many colours drive 50%, 80%, 90% of total colour volume?
- Counts: selling >5/d, >2/d, >1/d, >0/d, zero
- Tells you if the catalogue is healthy (broad demand) or concentrated (few winners carrying everything)

---

## Step 6 — Repurchase Signals

Use standalone product sales as a proxy for customer retention.

### Liquid Repurchase
- Total standalone liquid DSR / total kit DSR = liquid repurchase ratio
- Higher ratio = more returning customers buying refills
- Compare 7d ratio vs 30d ratio for direction

### Remove Product Sales
- Remove products are almost always repurchase
- Total remove DSR as another retention proxy

### Bundle Performance
- LIQ-SET, ACC-REM-BUN-1, ACC-REM-BUN-2: DSR
- Bundle : standalone ratio

---

## Step 7 — Selling Flags

### Breakout Performers (sustained growth: 7d > 14d > 30d, all windows >2/d)
Genuinely trending, not just spiking. Sort by total momentum (7d/30d ratio).

### Fading Performers (sustained decline: 7d < 14d < 30d, 30d >2/d)
All windows declining. Losing momentum — not a one-off dip.

### Spikes (7d > 30d by 50%+, 30d >1/d)
Sharp recent increase. Note to cross-reference promos and CRO.

### Drops (7d < 30d by 40%+, 30d >2/d)
Sharp recent decline. Note to check OOS status, listing changes, post-promo normalisation.

---

## Output Structure

```
SALES PERFORMANCE — [REGION] — [Date]

GROWTH HEADLINE
  Kit total: 7d=[X] | 14d=[X] | 30d=[X]
  Growth factor: [X] model | [X] actual | vs target: [X]%
  Momentum: [classification]
  [one-line summary]

CATEGORY PERFORMANCE
  Kits: [X]/d | Liquids: [X]/d | Accessories: [X]/d | Colours: [X]/d
  [per-category detail]

WEEKLY KIT TREND
  [8-week table with rolling avg and WoW %]

KIT MIX ANALYSIS
  [STA/COM/ULT: 14d vs 30d, direction, model comparison]

COLOUR INTELLIGENCE
  [top sellers, risers, fallers, catalogue efficiency]

REPURCHASE SIGNALS
  [liquid ratio, remove rate, bundle performance]

SELLING FLAGS
  [breakout, fading, spikes, drops]

COMMERCIAL SUMMARY
  [3-5 bullets: what the data says about the business, not what to order]
```

---

## Style Notes
- **Commercial lens only.** Do not discuss stock levels, days cover, 3PL issues, or container arrivals. Those belong in Sales Data Analysis and POS Model Check.
- Lead with the growth headline — it's the single most important commercial metric.
- Frame everything as "what does this mean for the business?" not "what do we need to order?"
- Use % changes and directional language (accelerating, trending, fading) over absolute numbers where the trend matters more than the snapshot.
- When flagging underperformance, frame as "the data shows X — here's what might be driving it" not "this SKU is bad."
- Cross-reference promos and CRO context to turn data points into commercial insights.
- The audience is Remy, Daniel, and Joel — they want to know if the marketing is working and where to focus commercial attention.
