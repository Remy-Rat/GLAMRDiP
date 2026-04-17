> **Context:** Get region info (which 3PL tab to use) from `../Regions/[REGION].md`. After completing, update `../Context/Current Issues.md`.

# Sales Data Analysis Skill

## Trigger
User asks for sales analysis, sell-through analysis, inventory trend check, stock discrepancy check, or DSR recalculation. Also trigger if user says "run the numbers", "what's actually selling", "check the sales data", "flag any discrepancies", or uploads an Order Schedule xlsx and asks about selling performance or stock movements.

---

## Data Sources (all from the Order Schedule xlsx)

**Always re-pull the xlsx at the start of every Sales Analysis.** Never reuse a prior extract, even from the same day — the SHOPIFY tab updates on +1d lag, the 3PL tab updates daily, and POS MODEL may be re-pasted. Using stale data silently degrades the analysis.

### Important: Data Source for DSR Calculations
All DSR calculations use the **SHOPIFY tab raw data** directly (7d/14d/30d windows from the most recent date). Do NOT use the SALES tab — its date range is manually set and may be stale or set to a non-standard period. The SALES tab is ignored for this analysis.

3PL deduction checks use the **3PL tab raw data** directly (daily stock snapshots, excluding container arrival days).

### Tabs Used
- **SHOPIFY** — daily unit sales per SKU. Source of truth for customer demand. Calculate DSR from raw data.
- **3PL tab** — daily inventory snapshots. Tab name varies by region:
  - AUS: `AUS 3GPL` (do NOT use `B360` — that's the old 3PL)
  - UK: `B360` (transitioning to Fulfillable)
  - CA: `B360`
  - Nordic: `B360`
  - Check `../Regions/[REGION].md` for the correct tab.
- **CNTR TRACKER** — inactive tab. Do not use. Detect container arrivals from 3PL data instead (look for days where 8+ SKUs increase simultaneously).
- **POS MODEL** — **source of truth** for live DSR, growth factor, and stock on hand.
  - Kit DSRs: header rows (rows 1-3, col 1) — Starter, Complete, Ultimate
  - Per-SKU DSR: derived from G3PL ON HAND (col 7) ÷ DAYS COVER (col 8) in the product table
  - Growth factor: search for 'GROWTH FACTOR' label, value is adjacent cell
  - DSR is manually calculated from monthly sales and pasted periodically — it is NOT live. Monitor variance between model DSR and actual Shopify selling rates.

### Critical Data Quirks
- **3PL future columns are corrupted.** Greg sets up date columns ahead of time but doesn't paste data until that day. Unpasted columns show as `int64 min` (-9223372036854775808) or NaN. ALWAYS detect the last valid date before analysis.
- **Shopify data has a +1 day lag** — pasted the day after.
- **CNTR TRACKER is inactive** — detect arrivals from 3PL data instead (8+ SKUs increasing on the same day = container check-in).
- **Packaging SKUs (STO-*, ACC-INS, ACC-THA) show 0 in Shopify** — consumed at warehouse level inside kits. Exclude from Shopify DSR comparison.
- **Bundle sales inflate 3PL deduction rates.** ACC-REM-BUN-1 (120ml + Bowl) and ACC-REM-BUN-2 (500ml + Bowl) sell as bundle SKUs on Shopify, but 3PL deducts the component SKUs individually. LIQ-SET (Liquids Set) deducts 1x of all 6 liquids per sale. If Greg sets POS MODEL DSR from 3PL deduction rates rather than Shopify sales, the model DSR for Remove 500ml, Remove Bowl, and liquids will be overstated. Always compare model DSR against Shopify standalone sales to detect this.

---

## Pre-built Scripts

Run `../Scripts/extract.py [REGION]` first to download the xlsx and parse all tabs into structured JSON. Then pipe into the analysis scripts:

```bash
uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py AUS > /tmp/aus.json
cat /tmp/aus.json | uv run --with pandas python3 Ops/Scripts/dsr.py
cat /tmp/aus.json | uv run --with pandas python3 Ops/Scripts/deductions.py
```

The scripts handle all data quirks (corrupted columns, last valid date detection, Shopify +1 day lag, container arrival exclusion). Use their output as the data foundation, then interpret and write the narrative.

If the scripts are unavailable or need updating, fall back to the inline preprocessing below.

---

## Kit-Adjusted Demand — Region-Specific

**Kits arrive pre-assembled from China.** Most liquids are already packed inside the kit. Only locally-filled items are picked separately at the 3PL and consumed per kit sale.

### AUS
- **Heal (LIQ-HEA-5)** — filled locally by Outsource Packaging, added to kits at G3PL. Kit-adjusted demand = standalone Shopify + kit sales. POS MODEL DSR already includes this.
- **All other liquids** (Base, Sensitive, Seal, Bond, Glow) — pre-packed in kits from China. G3PL stock only depletes from standalone Shopify sales. Compare standalone Shopify DSR to POS MODEL DSR.
- **Remove 120ml, Remove 500ml** — standalone items, NOT included in kits. Compare standalone Shopify DSR to POS MODEL DSR.

### Other Regions
Component map varies by region. Check `../Regions/[REGION].md` and confirm with the user which items are filled locally vs pre-packed from China before applying kit-adjusted demand. When in doubt, use standalone Shopify DSR.

---

## Growth Factor

The growth factor scales the sum of the live kit DSRs from the POS MODEL header.

```
base_total = STA_DSR + COM_DSR + ULT_DSR   (from POS MODEL rows 1-3)
scaled_total = base_total × growth_factor

Example: 34 + 78 + 35 = 147/day base → at 1.3x = 191/day
```

To calculate recommended growth factor from actual sales:
```
actual_growth = actual_14d_kit_total / base_total
recommended = actual_growth × 1.1   (10% buffer)
```

---

## Step 0 — Preprocessing (ALWAYS run first)

Run with: `uv run --with pandas,openpyxl python3 script.py`

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

file_path = '[PATH_TO_FILE].xlsx'
THREE_PL_TAB = '[REGION_3PL_TAB]'  # e.g. 'AUS 3GPL', 'B360'

# ---- SHOPIFY ----
shopify_raw = pd.read_excel(file_path, sheet_name='SHOPIFY', header=None)
header_idx = None
for i in range(10):
    if 'Date' in shopify_raw.iloc[i].astype(str).tolist():
        header_idx = i; break
shopify = shopify_raw.iloc[header_idx+1:].copy()
shopify.columns = ['date', 'sku', 'units']
shopify['date'] = pd.to_datetime(shopify['date'], errors='coerce')
shopify['units'] = pd.to_numeric(shopify['units'], errors='coerce').fillna(0)
shopify = shopify.dropna(subset=['date'])
shopify['sku'] = shopify['sku'].astype(str).str.strip()
today = shopify['date'].max()

# ---- 3PL TAB ----
tpl_raw = pd.read_excel(file_path, sheet_name=THREE_PL_TAB, header=None)
tpl_skus = tpl_raw.iloc[1:, 0].astype(str).str.strip().values
tpl_dates = pd.to_datetime(tpl_raw.iloc[0, 1:], errors='coerce')
valid_idx = ~tpl_dates.isna()
tpl_data = tpl_raw.iloc[1:, 1:].loc[:, valid_idx.values]
tpl_data.columns = tpl_dates[valid_idx].values
tpl_data.index = tpl_skus
tpl_data = tpl_data.apply(pd.to_numeric, errors='coerce')

# CRITICAL: Remove corrupted future columns
tpl_data[tpl_data < -1000] = np.nan
valid_counts = tpl_data.notna().sum()
threshold = len(tpl_data) * 0.3
valid_date_mask = valid_counts > threshold
last_valid_tpl = pd.Timestamp(max(tpl_data.columns[valid_date_mask]))
tpl = tpl_data.loc[:, tpl_data.columns <= last_valid_tpl]

# ---- POS MODEL (source of truth for DSR + growth factor) ----
pos_raw = pd.read_excel(file_path, sheet_name='POS MODEL', header=None)

# Growth factor
growth_factor = None
for r in range(12):
    for c in range(15):
        val = pos_raw.iloc[r, c]
        if str(val).strip() == 'GROWTH FACTOR':
            for offset_r, offset_c in [(1, 0), (0, 1), (0, -1)]:
                candidate = pos_raw.iloc[r + offset_r, c + offset_c]
                if pd.notna(candidate):
                    try: growth_factor = float(candidate); break
                    except: pass
            break

# Kit DSRs from header (rows 1-3, col 1)
kit_dsr_model = {}
for r in range(1, 4):
    name = str(pos_raw.iloc[r, 0]).strip()
    dsr_val = pd.to_numeric(pos_raw.iloc[r, 1], errors='coerce')
    if 'Starter' in name: kit_dsr_model['KIT-STA-2'] = dsr_val
    elif 'Complete' in name: kit_dsr_model['KIT-COM-4'] = dsr_val
    elif 'Ultimate' in name: kit_dsr_model['KIT-ULT-6'] = dsr_val

# Per-SKU DSR from product table
model_dsr = {}
pos_header_row = None
for r in range(len(pos_raw)):
    if str(pos_raw.iloc[r, 1]).strip() == 'SKU':
        pos_header_row = r; break
if pos_header_row is not None:
    for r in range(pos_header_row + 1, len(pos_raw)):
        sku = str(pos_raw.iloc[r, 1]).strip()
        if sku == 'nan' or sku == '': continue
        stock = pd.to_numeric(pos_raw.iloc[r, 7], errors='coerce')
        days_cover = pd.to_numeric(pos_raw.iloc[r, 8], errors='coerce')
        if pd.notna(stock) and pd.notna(days_cover) and days_cover > 0:
            model_dsr[sku] = stock / days_cover
model_dsr.update(kit_dsr_model)

model_kit_total = sum(kit_dsr_model.values())
model_scaled_total = model_kit_total * growth_factor

# ---- CNTR TRACKER ----
cntr_raw = pd.read_excel(file_path, sheet_name='CNTR TRACKER', header=None)
containers = []
for i in range(4, min(50, len(cntr_raw))):
    status = cntr_raw.iloc[i, 0]
    ref = cntr_raw.iloc[i, 1]
    eta = pd.to_datetime(cntr_raw.iloc[i, 5], errors='coerce') if pd.notna(cntr_raw.iloc[i, 5]) else pd.NaT
    stype = cntr_raw.iloc[i, 9] if len(cntr_raw.columns) > 9 and pd.notna(cntr_raw.iloc[i, 9]) else ''
    if pd.notna(status) and str(status) not in ['NaN', 'Status']:
        containers.append({'status': str(status), 'ref': str(ref), 'eta': eta, 'type': str(stype)})

# ---- DATA FRESHNESS ----
shopify_age = (pd.Timestamp.now() - today).days
tpl_age = (pd.Timestamp.now() - last_valid_tpl).days
```

---

## Step 1 — DSR Comparison (Model vs Actual)

Calculate Shopify DSR across 7d, 14d, 30d windows. Compare to POS MODEL DSR.

**SKU categories:**
- **Kits** — KIT-STA-2, KIT-COM-4, KIT-ULT-6 (compare Shopify DSR directly to POS MODEL)
- **Heal** — kit-adjusted (standalone + kit sales). POS MODEL already includes kit consumption. Show both standalone and adjusted.
- **Inserts** — ACC-INS (kit-adjusted: per kit), ACC-LAB and ACC-THA (per order). These show 0 or low in Shopify but are consumed at 3PL level. Track for days cover.
- **Other liquids** — standalone Shopify DSR only (Base, Sensitive, Seal, Bond, Glow, Sensitive Glow). These are pre-packed in kits from China.
- **Standalone items** — ACC-REM, ACC-REM-500 (not in kits, straight Shopify comparison)
- **Colours (POW-*)** — top 15 by 14d volume. Shopify captures kit picks directly (STA×3, COM×6, ULT×9). Include colour demand sanity check: total colour DSR vs expected from kits vs standalone.
- **DO NOT include** packaging SKUs (STO-*) — these belong in the POS Model Check skill, not sales analysis

**Output table format:**
```
--- KITS ---
SKU              Model DSR  Shop 7d  Shop 14d  Shop 30d  Gap vs Model
KIT-STA-2             34.0    38.6     35.1      33.3          +3%

--- HEAL (kit-adjusted: standalone + kit consumption at 3PL) ---
SKU              Model DSR  Shop 7d  Shop 14d  Shop 30d  Adj 14d  Gap vs Model
LIQ-HEA-5           184.6     2.9      2.7       3.9    123.1        -33%

--- LIQUIDS (standalone — pre-packed in kits from China) ---
SKU              Model DSR  Shop 7d  Shop 14d  Shop 30d  Gap vs Model
LIQ-BAS-2            53.3     0.0     15.6      29.4        -71%
```

At the bottom:
- POS MODEL growth factor vs actual: `actual_14d_kit_total / model_kit_base_total`
- % below/above scaled target
- Recommended growth factor (actual × 1.1)

---

## Step 2 — Weekly Kit Trend

Group Shopify kit sales into ISO weeks for the last 8 weeks. Show a `vs Model` column comparing daily rate to the scaled target.

Flag if:
- 3+ consecutive declining weeks
- Any week >30% above 4-week average (promo spike)
- Consistent >40% below model scaled target

Show kit mix (Starter/Complete/Ultimate split) for 14d with model comparison.

---

## Step 3 — Realistic Days Cover

For each SKU with stock > 0, calculate days cover at **POS MODEL DSR** and **actual Shopify DSR**.

Use latest valid 3PL stock. For Heal, use kit-adjusted actual DSR. For all other liquids, use standalone Shopify DSR.

Flag items:
- **OOS** — stock = 0 and DSR > 0
- **<14d CRITICAL** — either model or actual cover below 14 days
- **<30d WARNING** — either model or actual cover below 30 days

---

## Step 4 — Container Arrival Auto-Detection

Detect from 3PL data directly. CNTR TRACKER is inactive — do not use.

Look for days where 8+ SKUs increase simultaneously in the last 60 days. These are container check-in events. Try to match against POS MODEL shipment blocks by comparing detected arrival dates to Est. Arrival dates (±10 day window).

For each detected arrival, show: date, SKU count, total units, top 5 SKUs, and whether it matches a known POS MODEL shipment.

---

## Step 5 — Inventory Discrepancy Detection (Red Flag Investigation)

This is the accountability step — "Shopify says we sold X, 3PL deducted Y, where's the gap?" Don't just **list** red flags — **investigate and classify each**. A flagged deduction is a hypothesis, not a finding.

### 5A — Single-day flag investigation

For every red flag the extract produces (single-day deduction > benchmark from `../Context/Deduction Benchmarks.md`):

1. **Pull same-day Shopify sales** for that SKU. If ~0 and 3PL is 1,000+, it's not a sales event.
2. **Pull 15-day window Shopify sales** around the date — establish the normal rate. A 1,000-unit 3PL spike with 5-10/d Shopify either side = a one-off event, not a trend.
3. **Classify** each flag into one of these buckets:

| Class | Pattern | Action |
|---|---|---|
| **Explained — OP fill transfer** | SKU is `ACC-RE5-*`, `ACC-RE1-*`, `HEA-EMP/LID/BSH`, and a local fill PO was active on or near that date | Note and suppress from escalation. Cross-check that the OP delivery came back (close the loop). |
| **Explained — bundle event** | SKU moves with a same-day spike in LIQ-SET / ACC-REM-BUN-1 / ACC-REM-BUN-2 | Check bundle volume — explains gaps of ~4-30/d, not 1,000+/d |
| **Explained — kit swap / backorder clearing** | KIT-* deductions spike by 2-3x benchmark on a known backorder-clearing day (check Slack for that date) | Note and contextualise |
| **Explained — reconciliation** | RECONCILIATION tab shows entry on that date for that SKU, OR known transition shortfall (e.g. Greg's B360 packup investigation) | Note and cross-reference Greg's email thread |
| **⚠️ Unexplained** | Shopify near-zero, no bundle pairing, no OP transfer, no reconciliation entry — just a single big spike | **Escalate to G3PL** with date + SKU + quantity |

### 5B — Cumulative gap test (the high-value integrity check)

Run this independently from the single-day flag test. For every SKU (focus on colours since they have no bundle/kit leakage):

```
tpl_30d = avg_daily_deduction × 30
shop_30d = sum(Shopify units, last 30 days)
gap = tpl_30d - shop_30d

Flag if gap > 300 units for colours, or > 500 for kits/liquids
```

A single-day flag with 14 days of normal activity either side might still *look* suspicious but not actually represent missing stock. The **cumulative** view tells you whether the SKU's inventory account is actually short.

Typical output shape:

```
COLOUR SKU — UNEXPLAINED CUMULATIVE GAPS (3PL > Shopify by 30d)

SKU              3PL 30d   Shop 30d    Gap     Spike Date    Spike Units
POW-ENE-484        3,798        23   3,775    16 Apr          1,001
POW-DRE-771        3,657       318   3,339    08 Apr          1,113
...
TOTAL                                22,090 units unexplained

  → Each SKU's gap traces to ONE single-day spike while normal days show 5-10/d
  → Pattern suggests stock adjustments or write-offs, not sales
  → Action: request G3PL explanation for each spike
```

### 5C — Stock Gains (likely reconciliation or check-in)

3PL stock **increased** outside a detected container arrival:
- **Reconciliation** — 3PL found stock during a count (cross-check RECONCILIATION tab)
- **Ongoing check-in** — container still being processed across multiple days
- **Returns** — customer returns checked back in

Note likely cause; don't alarm — these are usually positive.

### 5D — Component Transfers (expected, don't alarm)

Component SKUs going to 0 or big single-day drops when a local fill PO is active:
- **ACC-RE5-BOT / INN / LID** → OP for Remove 500ml fill
- **ACC-RE1-BOT / INN / LID** → OP for Remove 120ml fill
- **HEA-EMP / LID / BSH** → OP for Heal fill

These are transfers to the filler, not lost stock. The component reappears ~28-35 days later as the finished SKU (LIQ-HEA-5, ACC-REM-500, ACC-REM).

---

## Step 6 — Shopify vs 3PL Deduction Check

For kit SKUs, compare daily Shopify sales to 3PL stock deductions over last 14 days.

**IMPORTANT: Exclude days where 3PL stock increased** (container arrivals) — these skew the averages. Only count sell-through days.

```
gap = avg_3PL_deduction_per_day - avg_Shopify_sales_per_day
If gap < 5: aligned
If gap > 5: 3PL dropping faster than Shopify explains
If gap < -5: 3PL dropping slower (returns, paste lag, or data issue)
```

This is the cleanest data integrity check. If kits are aligned, 3PL deduction logic is working correctly.

---

## Step 7 — Selling Performance Flags

### Sales Spikes (7d DSR > 30d DSR by 50%+)
Flag any SKU where the 7d selling rate is 50%+ above the 30d average. This could indicate:
- A promo or campaign driving demand
- A CRO change (upsell, bundle, layout change)
- A TikTok/social media moment
- Seasonal surge
- A pricing error on the website

**Cross-reference context:** When spikes are detected, check `#sale-announcements` (C091PEBAS65) for active promos and `#cro-team-meetings` (C098QGQ6NLS) for recent CRO changes that could explain the spike. This turns "X spiked" into "X spiked — likely driven by [specific change]."

Show the 7d, 14d, 30d DSRs so the trend is visible. These items may stock out faster than expected.

```
SALES SPIKES (7d significantly above 30d):
  SKU              7d DSR  14d DSR  30d DSR  Spike vs 30d
  POW-OAK-283       24.6     20.9     13.8       +78%    ← trending up fast
  KIT-STA-2         38.6     35.1     33.3       +16%    (below 50% threshold — not flagged)
```

### Sales Drops (7d DSR < 30d DSR by 40%+)
Flag any SKU where the 7d selling rate has dropped 40%+ below the 30d average. This could indicate:
- OOS on the website (check Shopify store)
- Product removed from active listings
- Marketing/CRO pulled back (check `#cro-team-meetings`)
- Post-promo normalisation (check `#sale-announcements` for recent sale end dates)
- Seasonal decline

```
SALES DROPS (7d significantly below 30d):
  SKU              7d DSR  14d DSR  30d DSR  Drop vs 30d
  LIQ-BAS-2          0.0     15.6     29.4       -100%   ← check if OOS on website
  POW-XXX-123        5.0      8.2     12.1        -59%
```

### Overperformers (>20% above model DSR)
May stock out faster than POS MODEL predicts.

### Underperformers (>40% below model DSR)
Model DSR may need refresh. Flag that DSR is manually updated from monthly sales — if recent weeks are consistently lower, the model is stale.

### Dead stock (in stock, 0 Shopify sales in 14d)
For colour SKUs (POW-*): count and total units sitting idle. Likely unlaunched colours.

### Sensitive Base signal
Compare LIQ-SEN-2 vs LIQ-BAS-2 standalone performance. Model assumes 70/30 kit split.

---

## Output Structure

```
SALES DATA ANALYSIS — [REGION] — [Date]

DATA FRESHNESS
  Shopify: [date] ([X]d ago)
  3PL: [date] ([X]d ago)
  Growth factor: [X]x
  POS MODEL base: [X]/day → scaled: [X]/day

DSR: MODEL vs REALITY
  [Kits, Heal (kit-adjusted), liquids (standalone), top colours]
  Growth factor comparison and recommendation

WEEKLY KIT TREND
  [8-week trend with vs Model column]
  [Kit mix with model comparison]

REALISTIC DAYS COVER
  [Model vs actual cover]

CONTAINER ARRIVALS DETECTED
  [From 3PL data, with tracker cross-ref]

INVENTORY DISCREPANCIES
  [Stock losses (raise with 3PL), stock gains (reconciliation/check-in), container-aligned, component transfers]

3PL DEDUCTION CHECK
  [Kit alignment, excluding container days]

SELLING PERFORMANCE FLAGS
  [Sales spikes, sales drops, over/underperformers, dead stock, sensitive base signal]

KEY TAKEAWAYS
  [3-5 bullets: what needs action, what's FYI]
```

---

## Style Notes
- Lead with the growth factor reality check — it drives every ordering decision
- Split discrepancies into **stock losses** (raise with 3PL) and **stock gains** (reconciliation/check-in). Losses sorted by impact — this is the actionable list
- Don't alarm about container-aligned increases, component transfers, or stock gains — label as expected/positive
- If 3PL data is stale (>2 days), flag prominently before any analysis
- When liquids show large variance vs model, note that POS MODEL DSR is manually updated from monthly sales — the model may be stale, not the selling rate wrong
- The audience is Remy and Daniel — they want what's real vs what the model assumes, and data integrity issues to raise with the 3PL
