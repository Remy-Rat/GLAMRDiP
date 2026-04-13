> **Context:** Get region info (which 3PL tab to use) from `../Regions/[REGION].md`. After completing, update `../Context/Current Issues.md`.

# Sales Data Analysis Skill

## Trigger
User asks for sales analysis, sell-through analysis, inventory trend check, stock discrepancy check, or DSR recalculation. Also trigger if user says "run the numbers", "what's actually selling", "check the sales data", "flag any discrepancies", or uploads an Order Schedule xlsx and asks about selling performance or stock movements.

---

## Data Sources (all from the Order Schedule xlsx)

### Tabs Used
- **SHOPIFY** — daily unit sales per SKU. Source of truth for customer demand.
- **3PL tab** — daily inventory snapshots. Tab name varies by region:
  - AUS: `AUS 3GPL` (do NOT use `B360` — that's the old 3PL)
  - UK: `B360` (transitioning to Fulfillable)
  - CA: `B360`
  - Nordic: `B360`
  - Check `../Regions/[REGION].md` for the correct tab.
- **CNTR TRACKER** — container shipment records. Often stale — detect arrivals from 3PL data instead.
- **POS MODEL** — **source of truth** for live DSR, growth factor, and stock on hand.
  - Kit DSRs: header rows (rows 1-3, col 1) — Starter, Complete, Ultimate
  - Per-SKU DSR: derived from G3PL ON HAND (col 7) ÷ DAYS COVER (col 8) in the product table
  - Growth factor: search for 'GROWTH FACTOR' label, value is adjacent cell
  - DSR is manually calculated from monthly sales and pasted periodically — it is NOT live. Monitor variance between model DSR and actual Shopify selling rates.

### Critical Data Quirks
- **3PL future columns are corrupted.** Greg sets up date columns ahead of time but doesn't paste data until that day. Unpasted columns show as `int64 min` (-9223372036854775808) or NaN. ALWAYS detect the last valid date before analysis.
- **Shopify data has a +1 day lag** — pasted the day after.
- **CNTR TRACKER is often stale** — detect arrivals from 3PL data instead.
- **Packaging SKUs (STO-*, ACC-INS, ACC-THA) show 0 in Shopify** — consumed at warehouse level inside kits. Exclude from Shopify DSR comparison.

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
- **Other liquids** — standalone Shopify DSR only (Base, Sensitive, Seal, Bond, Glow). These are pre-packed in kits from China.
- **Standalone items** — ACC-REM, ACC-REM-500 (not in kits, straight Shopify comparison)
- **Colours (POW-*)** — top 15 by 14d volume
- **DO NOT include** packaging SKUs (STO-*, ACC-INS, ACC-THA)

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

Detect from 3PL data (NOT CNTR TRACKER — it's often stale).

Look for days where 8+ SKUs increase simultaneously in the last 60 days. Try to match against CNTR TRACKER within ±10 day window. Flag:
- Detected in 3PL but tracker still shows "In Transit" → tracker needs updating
- Tracker shows "Delivered" but no 3PL increase → possibly not checked in
- Tracker ETA passed >5 days, no 3PL increase → delayed or lost

---

## Step 5 — Inventory Discrepancy Detection

Scan 3PL data for anomalous single-day movements over last 45 days.

Dynamic thresholds per SKU: `max(actual_dsr × 5, floor)` where floor = 500 (kits/packaging), 200 (liquids), 100 (colours).

Group output:
- **UNEXPLAINED** — not aligned with container or sales. Sort by absolute impact.
- **CONTAINER-ALIGNED** — expected, just count them.
- **COMPONENT TRANSFERS** — component SKUs (HEA-EMP, HEA-LID, HEA-BSH, ACC-RE1-*, ACC-RE5-*) going to 0 = shipped to local filler. Expected — don't alarm.

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
  [Unexplained, container-aligned, component transfers]

3PL DEDUCTION CHECK
  [Kit alignment, excluding container days]

SELLING PERFORMANCE FLAGS
  [Over/underperformers, dead stock, sensitive base signal]

KEY TAKEAWAYS
  [3-5 bullets: what needs action, what's FYI]
```

---

## Style Notes
- Lead with the growth factor reality check — it drives every ordering decision
- Present discrepancies sorted by impact (largest unexplained gap first)
- Don't alarm about container-aligned increases or component transfers — label as expected
- If 3PL data is stale (>2 days), flag prominently before any analysis
- When liquids show large variance vs model, note that POS MODEL DSR is manually updated from monthly sales — the model may be stale, not the selling rate wrong
- The audience is Remy and Daniel — they want what's real vs what the model assumes, and data integrity issues to raise with the 3PL
