> **Context:** Get region info (which 3PL tab to use) from `../Regions/[REGION].md`. Get component map and kit-adjusted demand formulas from `../../Shared/Component Map.md`. After completing, update `../Context/Current Issues.md`.

# Sales Data Analysis Skill

## Trigger
User asks for sales analysis, sell-through analysis, inventory trend check, stock discrepancy check, or DSR recalculation. Also trigger if user says "run the numbers", "what's actually selling", "check the sales data", "flag any discrepancies", or uploads an Order Schedule xlsx and asks about selling performance or stock movements.

---

## Data Sources (all from the Order Schedule xlsx)

### Tabs Used
- **SHOPIFY** — daily unit sales per SKU. Source of truth for customer demand.
- **B360** — daily inventory snapshots from the 3PL. Source of truth for stock on hand.
- **CNTR TRACKER** — container shipment records with delivery dates. Used to explain large inventory increases.
- **POS MODEL** — current DSR and growth factor settings (the plan).
- **DSR** — model DSR per SKU.

### Critical Data Quirks (learned from live runs)
- **B360 future columns are corrupted.** Greg sets up date columns ahead of time but doesn't paste data until that day. Unpasted columns show as `int64 min` (-9223372036854775808) or NaN. You MUST detect the last valid B360 date before doing any analysis.
- **Shopify data has a +1 day lag** — pasted the day after.
- **CNTR TRACKER is often stale** — ETAs and statuses may not be updated after delivery. Do NOT rely solely on tracker dates for container arrival matching. Detect arrivals from B360 data instead.
- **Packaging SKUs (STO-*, ACC-INS, ACC-THA) show 0 in Shopify** — they're consumed at warehouse level inside kits, not sold as Shopify line items. Exclude from Shopify DSR comparison. Only assess via B360 deduction rates.
- **Heal, Remove, and other liquids appear both as standalone Shopify sales AND inside kits.** Shopify DSR for these SKUs only captures standalone purchases. Real demand = standalone + kit consumption. Use the component map below.

---

## Component Map — Kit Contents

Each kit sold consumes these components at the 3PL. Use this to calculate total demand.

```
Every kit (STA/COM/ULT) consumes per unit:
  1x LIQ-HEA-5 (Heal)
  1x powder colour (from customer's selection)
  1x STO-BUB-BAG-L (Bubble Mailer) OR STO-MAI-BAG-S (Small Satchel)
  1x STO-MAI-2 (Small Box) — for non-mailer orders
  1x ACC-INS (Instructions Booklet)
  1x ACC-THA (Thank You Card)

KIT-STA-2 (Starter Kit) additionally:
  1x LIQ-BAS-2 (Base) OR LIQ-SEN-2 (Sensitive Base)
  1x LIQ-SEA-3 (Seal)
  
KIT-COM-4 (Complete Kit) additionally:
  1x LIQ-BAS-2, 1x LIQ-SEA-3, 1x LIQ-BON-1 (Bond), 1x LIQ-GLO-4 (Glow)
  1x ACC-REM (Remove 120ml)

KIT-ULT-6 (Ultimate Kit) additionally:
  All of Complete Kit plus: 1x ACC-REM-500 (Remove 500ml)
```

To calculate total demand for a liquid/component:
```
total_demand = shopify_standalone_sales + (kits_consuming_it × kits_sold_per_day)
```

Example for Heal: `total_heal_demand = shopify_heal + total_kits_sold` (all kits contain 1 Heal)
Example for Bond: `total_bond_demand = shopify_bond + complete_kits + ultimate_kits`

---

## Step 0 — Preprocessing (ALWAYS run first)

This step loads and cleans all data. Run this as a single code block before any analysis.

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

file_path = '/mnt/user-data/uploads/[FILENAME].xlsx'

# ---- SHOPIFY ----
shopify_raw = pd.read_excel(file_path, sheet_name='SHOPIFY', header=None)
# Find header row containing 'Date'
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

# ---- B360 ----
b360_raw = pd.read_excel(file_path, sheet_name='B360', header=None)
b360_skus = b360_raw.iloc[1:, 0].astype(str).str.strip().values
b360_dates = pd.to_datetime(b360_raw.iloc[0, 1:], errors='coerce')
valid_idx = ~b360_dates.isna()
b360_data = b360_raw.iloc[1:, 1:].loc[:, valid_idx.values]
b360_data.columns = b360_dates[valid_idx].values
b360_data.index = b360_skus
b360_data = b360_data.apply(pd.to_numeric, errors='coerce')

# CRITICAL: Remove corrupted future columns
# int64 min = -9223372036854775808, appears in unpasted cells
b360_data[b360_data < -1000] = np.nan

# Find last valid B360 date (where >50% of SKUs have data)
valid_counts = b360_data.notna().sum()
threshold = len(b360_data) * 0.5
valid_date_mask = valid_counts > threshold
last_valid_b360 = pd.Timestamp(max(b360_data.columns[valid_date_mask]))
b360 = b360_data.loc[:, b360_data.columns <= last_valid_b360]

# ---- CNTR TRACKER ----
cntr_raw = pd.read_excel(file_path, sheet_name='CNTR TRACKER', header=None)
containers = []
for i in range(4, min(30, len(cntr_raw))):
    status = cntr_raw.iloc[i, 0]
    ref = cntr_raw.iloc[i, 1]
    eta = pd.to_datetime(cntr_raw.iloc[i, 5], errors='coerce') if pd.notna(cntr_raw.iloc[i, 5]) else pd.NaT
    stype = cntr_raw.iloc[i, 9] if pd.notna(cntr_raw.iloc[i, 9]) else ''
    if pd.notna(status) and str(status) not in ['NaN', 'Status']:
        containers.append({'status': str(status), 'ref': str(ref), 'eta': eta, 'type': str(stype)})

# ---- DSR (model) ----
dsr_raw = pd.read_excel(file_path, sheet_name='DSR', header=None)
model_dsr = {}
for i in range(3, len(dsr_raw)):
    sku = str(dsr_raw.iloc[i, 0]).strip()
    dsr_val = dsr_raw.iloc[i, 1]
    if pd.notna(dsr_val) and sku != 'nan':
        try: model_dsr[sku] = float(dsr_val)
        except: pass

# ---- POS MODEL (growth factor) ----
pos_raw = pd.read_excel(file_path, sheet_name='POS MODEL', header=None)
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

# ---- DATA FRESHNESS CHECK ----
shopify_age = (pd.Timestamp.now() - today).days
b360_age = (pd.Timestamp.now() - last_valid_b360).days
print(f"DATA FRESHNESS:")
print(f"  Shopify last date: {today.date()} ({'⚠️ STALE' if shopify_age > 2 else '✅'} — {shopify_age}d ago)")
print(f"  B360 last valid:   {last_valid_b360.date()} ({'⚠️ STALE' if b360_age > 2 else '✅'} — {b360_age}d ago)")
print(f"  Growth factor:     {growth_factor}x")
```

---

## Step 1 — DSR Comparison (Model vs Actual)

Calculate own DSR across 7d, 14d, 30d windows for all sold SKUs.

**SKU categories for this step:**
- **Kit SKUs** — KIT-STA-2, KIT-COM-4, KIT-ULT-6 (compare directly to model DSR)
- **Standalone liquids** — LIQ-HEA-5, ACC-REM, ACC-REM-500, LIQ-BON-1, LIQ-BAS-2, LIQ-SEN-2, LIQ-SEA-3, LIQ-GLO-4 (show both Shopify-only and kit-adjusted demand)
- **Colours (POW-*)** — top 15 by 14d volume
- **DO NOT include** packaging SKUs (STO-*, ACC-INS, ACC-THA) — they show 0 in Shopify

For each SKU:
```python
for window_days in [7, 14, 30]:
    start = today - timedelta(days=window_days)
    period_sales = shopify[(shopify['sku'] == sku) & (shopify['date'] > start)]['units'].sum()
    dsr = period_sales / window_days
```

**For liquids, calculate kit-adjusted demand:**
```python
kit_total_14d = sum of all kit DSRs (14d)
starter_14d = dsr for KIT-STA-2
complete_14d = dsr for KIT-COM-4
ultimate_14d = dsr for KIT-ULT-6

# Heal: all kits consume 1
heal_total = heal_standalone + kit_total_14d

# Bond: Complete + Ultimate consume 1
bond_total = bond_standalone + complete_14d + ultimate_14d

# Remove 120ml: Complete + Ultimate consume 1
rem120_total = rem120_standalone + complete_14d + ultimate_14d

# Remove 500ml: Ultimate consumes 1
rem500_total = rem500_standalone + ultimate_14d

# Base: Starter + Complete + Ultimate (assume ~70% choose Base over Sensitive)
base_total = base_standalone + kit_total_14d * 0.7

# Seal: Starter + Complete + Ultimate
seal_total = seal_standalone + kit_total_14d

# Glow: Complete + Ultimate consume 1
glow_total = glow_standalone + complete_14d + ultimate_14d
```

**Output table format:**
```
SKU              Model DSR  Shop 7d  Shop 14d  Shop 30d  Kit-Adj 14d  Gap vs Model
KIT-STA-2             21.0    15.1     14.1      15.4         —          -33%
LIQ-HEA-5            85.0     1.4      1.4       1.7       52.1         -39%
```

At the bottom, state:
- Model growth factor vs actual kit performance as a multiplier (base 1x = 80 kits/day)
- Recommended growth factor (actual 14d + 10% buffer, minimum 1.0x)

---

## Step 2 — Weekly Kit Trend

Group Shopify kit sales into ISO weeks for the last 8 weeks.

```python
kit_sales = shopify[shopify['sku'].isin(kit_skus)].copy()
kit_sales['week_start'] = kit_sales['date'] - pd.to_timedelta(kit_sales['date'].dt.weekday, unit='d')
weekly = kit_sales.groupby('week_start').agg(
    total=('units', 'sum'),
    days=('date', 'nunique')
).reset_index()
weekly['daily'] = weekly['total'] / weekly['days']
```

Show week-over-week direction with arrows. Flag if:
- 3+ consecutive declining weeks
- Any week >30% above 4-week average (promo spike)
- Consistent >40% below model DSR

Also show kit mix percentages (Starter/Complete/Ultimate split) for the last 14 days — useful for validating model ratios.

---

## Step 3 — Realistic Days Cover

For each SKU with stock > 0, calculate days cover at **actual selling rate** vs **model DSR**.

**Use latest valid B360 stock** (from the last valid B360 date identified in preprocessing).

For liquids and components, use the **kit-adjusted demand** from Step 1 as the "actual" rate — not just Shopify standalone.

Output table:
```
SKU              Stock   Model DSR  Actual DSR  Model Cover  Actual Cover
KIT-ULT-6         887      18.0       10.7         49d          83d
LIQ-HEA-5        1760      85.0       52.1         21d          34d  ← kit-adjusted
```

Flag items:
- 🚨 OOS (stock = 0 and DSR > 0)
- ⚠️ <14 days cover at model DSR
- 📋 <30 days cover at actual rate (matters if selling picks up)

---

## Step 4 — Container Arrival Auto-Detection

**Do NOT rely on CNTR TRACKER dates** — they are often stale.

Instead, detect container arrivals directly from B360 data:

```python
# For each date in B360 (last 60 days), count how many SKUs had increases
cutoff = today - timedelta(days=60)
recent_cols = [c for c in b360.columns if pd.Timestamp(c) > cutoff]

for j in range(1, len(recent_cols)):
    date_col = recent_cols[j]
    prev_col = recent_cols[j-1]
    deltas = b360[date_col] - b360[prev_col]
    deltas = deltas.dropna()
    
    # A container check-in = many SKUs increasing simultaneously
    increases = deltas[deltas > 10]  # ignore tiny fluctuations
    if len(increases) >= 8:  # 8+ SKUs increasing on same day = container
        total_increase = increases.sum()
        # Try to match against CNTR TRACKER (±10 day window since tracker is stale)
        matched_ref = "no match in tracker"
        for c in containers:
            if pd.notna(c['eta']) and abs((pd.Timestamp(date_col) - c['eta']).days) <= 10:
                matched_ref = f"likely {c['ref']} (tracker ETA: {c['eta'].date()}, status: {c['status']})"
                break
```

After detection, flag:
- **Container detected in B360 but tracker still shows "In Transit"** → tracker needs updating
- **Tracker shows "Delivered" but no B360 increase detected** → possibly not checked in at 3PL
- **Container ETA passed >5 days ago, no B360 increase, tracker says "In Transit"** → delayed or lost

---

## Step 5 — Inventory Discrepancy Detection

Scan B360 for anomalous single-day movements over the last 45 days.

### Dynamic Thresholds
Calculate thresholds per SKU based on velocity:

```python
for sku in b360.index:
    sku_dsr = actual_dsr_14d.get(sku, 0)
    
    # Threshold = max(5x daily rate, minimum_floor)
    if sku.startswith(('KIT-', 'STO-')): floor = 500
    elif sku.startswith(('LIQ-', 'ACC-R')): floor = 200
    else: floor = 100
    
    threshold = max(sku_dsr * 5, floor)
```

### For each flagged movement:

**Large INCREASE (delta > threshold):**
1. Check if it aligns with a detected container arrival (from Step 4) → expected, label as such
2. If no container → flag as "unexplained increase" (possible stock correction, return, or data entry)

**Large DECREASE beyond sales (|delta| > threshold AND |delta| > 2× Shopify sales that day):**
1. Calculate: `unexplained_gap = |B360_decrease| - shopify_sales_that_day`
2. If gap > threshold → flag as "excess deduction"
3. If gap ≈ 0 → matches sales, not a discrepancy

**Component wipeouts (HEA-EMP, HEA-LID, HEA-BSH, ACC-RE1-BOT, ACC-RE1-LID, ACC-RE1-INN, ACC-RE5-BOT, ACC-RE5-LID, ACC-RE5-INN going to 0):**
These are expected when components are shipped to the local filler (Swift in CA, Outsource Packaging in AUS, etc). Note them but don't alarm — label as "component transfer to filler" and cross-reference with Slack for fill PO activity.

### Output format:
Group discrepancies by type, sort by absolute impact:
```
🚨 UNEXPLAINED (not aligned with container or sales):
  Date       | SKU              | Change   | Shopify | Gap      | Likely Cause
  2026-04-11 | POW-RAD-043      | -829     | 56      | -773     | Stock correction? Investigate with 3PL

✅ CONTAINER-ALIGNED (expected):
  2026-03-04 | Multiple SKUs    | +5,200   | —       | —        | Container CA 15012026 check-in

📋 COMPONENT TRANSFERS (expected — local fill):
  2026-02-27 | HEA-EMP          | -34,200  | 0       | -34,200  | Shipped to Swift for fill PO
```

---

## Step 6 — Shopify vs B360 Deduction Check

For kit SKUs (the most reliable 1:1 comparison), compare daily over last 14 days:

```python
for sku in ['KIT-STA-2', 'KIT-COM-4', 'KIT-ULT-6']:
    # Get B360 values for last 14 days
    recent_b360 = b360.loc[sku].dropna()
    recent_dates = [d for d in recent_b360.index if pd.Timestamp(d) > today - timedelta(days=14)]
    
    total_b360_change = 0
    total_shopify = 0
    days_counted = 0
    for j in range(1, len(recent_dates)):
        b360_delta = float(recent_b360[recent_dates[j]]) - float(recent_b360[recent_dates[j-1]])
        shop_day = shopify[(shopify['sku'] == sku) & 
                           (shopify['date'].dt.date == pd.Timestamp(recent_dates[j]).date())]['units'].sum()
        total_b360_change += b360_delta
        total_shopify += shop_day
        days_counted += 1
    
    avg_b360 = total_b360_change / days_counted  # should be negative
    avg_shop = total_shopify / days_counted
    gap = abs(avg_b360) - avg_shop
    
    # If gap > 5/day: B360 dropping faster than Shopify explains → possible issue
    # If gap < -5/day: B360 dropping slower → returns or paste lag
    # If gap ≈ 0: aligned ✅
```

This is the cleanest data integrity check. If kits are aligned, 3PL deduction logic is working correctly.

---

## Step 7 — Selling Performance Flags

### Overperformers (selling >20% above model DSR)
List any SKU where actual 14d DSR > model DSR × 1.2. These may stock out faster than predicted.

### Underperformers (selling >40% below model DSR)
List any SKU where actual 14d DSR < model DSR × 0.6. Capital tied up unnecessarily.

### Dead stock (in stock, 0 Shopify sales in 14d)
For colour SKUs (POW-*): list all with B360 stock > 0 but zero Shopify sales in 14 days. 
Count them and total the units sitting idle. Note if these have been flagged in Slack previously (likely unlaunched colours).

### Sensitive Base signal
Compare LIQ-SEN-2 vs LIQ-BAS-2 performance against model. If Sensitive is overperforming while Base underperforms, the 70/30 kit split assumption may need adjusting.

---

## Output Structure

Present the full analysis in this order:

```
📊 Sales Data Analysis — [REGION] — [Date]

⚠️ DATA FRESHNESS
  Shopify: [date] ([X]d ago)
  B360: [date] ([X]d ago)
  [Flag if either is >2 days stale]

🎯 DSR: MODEL vs REALITY
  [Table from Step 1 — kits, kit-adjusted liquids, top colours]
  Model: Xx (Y kits/day) → Actual: Zx (W kits/day)
  Recommended growth factor: [X]x

📈 WEEKLY KIT TREND
  [8-week trend from Step 2]

📦 REALISTIC DAYS COVER
  [Table from Step 3 — model vs actual cover, using kit-adjusted rates for liquids]

🚢 CONTAINER ARRIVALS DETECTED
  [Auto-detected from B360 in Step 4, with tracker cross-ref and staleness flags]

🚨 INVENTORY DISCREPANCIES
  [Grouped output from Step 5 — unexplained, container-aligned, component transfers]

✅ 3PL DEDUCTION CHECK
  [Kit Shopify vs B360 alignment from Step 6]

🔍 SELLING PERFORMANCE FLAGS
  [Overperformers, underperformers, dead stock from Step 7]

🔑 KEY TAKEAWAYS
  [3-5 bullets: what needs action, what's FYI]
```

---

## Style Notes
- Lead with the growth factor reality check — it drives every ordering decision
- Present discrepancies sorted by impact (largest unexplained gap first)
- Don't alarm about container-aligned increases — confirm and label as expected
- Don't alarm about component transfers to filler — label as expected  
- If B360 data is stale (>2 days), flag this prominently before any analysis
- For dead stock colours, explicitly note whether they've been flagged in Slack previously
- The audience is Remy and Daniel — they want what's real vs what the model assumes, and data integrity issues to raise with the 3PL
