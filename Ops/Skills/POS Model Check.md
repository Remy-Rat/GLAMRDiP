> **Context:** Get region info (which 3PL tab to use, inventory config) from `../Regions/[REGION].md`. Get kit-adjusted demand items from `../../Shared/Component Map.md`. Get deduction benchmarks from `../Context/Deduction Benchmarks.md`. Get lead times from `../Context/Lead Times.md`. After completing, update `../Context/Current Issues.md`.

# POS Model Check Skill

## Trigger
User asks for a stock position check, POS model check, check-in progress, double-count check, or packaging review. Also trigger on "what's actually available", "confirmed vs pending", "how much has been checked in", "is there double-counting", or when the user provides ShipHero PO CSV exports alongside an Order Schedule xlsx.

---

## Data Sources

### Order Schedule xlsx (from Google Drive)
Fetch the latest via gcloud:
```bash
TOKEN=$(/opt/homebrew/share/google-cloud-sdk/bin/gcloud auth print-access-token)
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://www.googleapis.com/drive/v3/files/SHEET_ID/export?mimeType=application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" \
  -o /tmp/[region]_order_schedule.xlsx
```
Sheet IDs are stored in the memory file `reference_google_drive_sheets.md`.

### Tabs Used
- **POS MODEL** — source of truth for DSR, growth factor, stock, and shipment projections
  - Rows 0-9: Header with growth factor, kit DSRs, and per-shipment metadata blocks
  - Row ~10: Column headers (find by scanning for 'SKU' in col 1)
  - Rows 11+: Product data
  - Column groups per shipment block:
    - Cols 7-9: Current G3PL stock (ON HAND, DAYS COVER, RUN OUT)
    - Cols 12-15: Express Shipment #1 (OL, PL, projected ON HAND, DAYS COVER)
    - Cols 17-20: Express Shipment #2 (same structure)
    - Cols 24+: Additional container/shipment groups (repeating pattern)
  - Each shipment block header (rows 0-9) has: Our Reference, Est. Completion, Est. Arrival, Order Status, ASN
  - **OL** = Order Line quantity (what was ordered). **PL** = Packing List (what was actually packed)
  - Projected ON HAND = current stock + OL — **this is where double-counting occurs during partial check-in**
- **3PL tab** — daily inventory snapshots (tab name varies by region: AUS = `AUS 3GPL`, UK/CA/Nordic = `B360`)
- **PO TRACKER** — CN filling POs with status (Placed / In Production / Completed)
- **RECONCILIATION** — book-in data with discrepancies
- **CNTR TRACKER** — inactive, do not use. Shipment dates and statuses come from the POS MODEL header blocks (Est. Completion, Est. Arrival, Order Status per shipment column group).

### ShipHero PO CSVs (user exports on demand)
One CSV per active Purchase Order. Export from ShipHero > Purchase Orders > [PO] > Export CSV.
- **Quantity** — expected on the PO
- **Quantity Received** — checked in so far
- **On Hand** — current total stock (warehouse-level, same across all PO exports)
- **Available** — on hand minus backorders/allocated
- If user doesn't provide these, prompt: "To run the full POS Check, I need ShipHero PO exports for each active PO. Which POs are currently active?"

### External Sources
- **Slack** — regional inventory channel + 3PL channel for container/order context
- **Gmail** — supplier/filler emails for local fill status
- **Deduction Benchmarks** (`../Context/Deduction Benchmarks.md`) — red flag thresholds per SKU

### Critical Data Quirks
- **3PL future columns are corrupted.** Same int64 min / NaN issue as Sales Data Analysis. Detect last valid date before any analysis.
- **During container check-in (2-5 days at G3PL):** ON HAND partially includes inbound stock. POS MODEL Express Shipment columns assume inbound is separate → double-counting.
- **ShipHero PO status doesn't always flip** from Pending to Closed. Don't rely on status — use Quantity vs Quantity Received per SKU to determine completion.
- **Quarantined stock** shows in ShipHero On Hand but NOT in Available. The gap = quarantined + backorder allocated. Look for SKUs with "-QUARANTINED" suffix in PO exports.
- **Packaging SKUs (STO-\*, ACC-INS, ACC-LAB, ACC-THA) don't sell on Shopify.** Monitor only via 3PL deduction rates.

---

## Step 0 — Preprocessing

Run with: `uv run --with pandas,openpyxl python3 script.py`

### Block A: Order Schedule

```python
import pandas as pd
import numpy as np
from datetime import timedelta

file_path = '[PATH_TO_FILE].xlsx'
THREE_PL_TAB = '[REGION_3PL_TAB]'  # e.g. 'AUS 3GPL'

# ---- POS MODEL ----
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

# Kit DSRs from header
kit_dsr_model = {}
for r in range(1, 4):
    name = str(pos_raw.iloc[r, 0]).strip()
    dsr_val = pd.to_numeric(pos_raw.iloc[r, 1], errors='coerce')
    if 'Starter' in name: kit_dsr_model['KIT-STA-2'] = dsr_val
    elif 'Complete' in name: kit_dsr_model['KIT-COM-4'] = dsr_val
    elif 'Ultimate' in name: kit_dsr_model['KIT-ULT-6'] = dsr_val

model_kit_total = sum(kit_dsr_model.values())

# Per-SKU data from product table
pos_header_row = None
for r in range(len(pos_raw)):
    if str(pos_raw.iloc[r, 1]).strip() == 'SKU':
        pos_header_row = r; break

model_dsr = {}
model_stock = {}
if pos_header_row is not None:
    for r in range(pos_header_row + 1, len(pos_raw)):
        sku = str(pos_raw.iloc[r, 1]).strip()
        if sku == 'nan' or sku == '': continue
        stock = pd.to_numeric(pos_raw.iloc[r, 7], errors='coerce')
        days_cover = pd.to_numeric(pos_raw.iloc[r, 8], errors='coerce')
        if pd.notna(stock):
            model_stock[sku] = stock
        if pd.notna(stock) and pd.notna(days_cover) and days_cover > 0:
            model_dsr[sku] = stock / days_cover
model_dsr.update(kit_dsr_model)

# Shipment metadata from header (rows 0-9)
# Scan for blocks containing 'Our Reference' or 'Order Reference'
# Each block starts at a column where the reference label appears
# Extract: ref, eta, status, and OL quantities per SKU from the product rows

# ---- 3PL TAB ----
tpl_raw = pd.read_excel(file_path, sheet_name=THREE_PL_TAB, header=None)
tpl_skus = tpl_raw.iloc[1:, 0].astype(str).str.strip().values
tpl_dates = pd.to_datetime(tpl_raw.iloc[0, 1:], errors='coerce')
valid_idx = ~tpl_dates.isna()
tpl_data = tpl_raw.iloc[1:, 1:].loc[:, valid_idx.values]
tpl_data.columns = tpl_dates[valid_idx].values
tpl_data.index = tpl_skus
tpl_data = tpl_data.apply(pd.to_numeric, errors='coerce')
tpl_data[tpl_data < -1000] = np.nan
valid_counts = tpl_data.notna().sum()
threshold = len(tpl_data) * 0.3
valid_date_mask = valid_counts > threshold
last_valid_tpl = pd.Timestamp(max(tpl_data.columns[valid_date_mask]))
tpl = tpl_data.loc[:, tpl_data.columns <= last_valid_tpl]
```

### Block B: ShipHero PO CSVs

```python
import glob, os

shiphero_files = glob.glob('[PATH_TO_CSVS]/*.csv')
# Or user provides specific file paths

po_data = {}
for f in shiphero_files:
    # ShipHero CSVs have metadata rows before the header — skip rows until we find the header
    df_raw = pd.read_csv(f, header=None, nrows=15)
    header_row = None
    for i in range(len(df_raw)):
        if 'SKU' in str(df_raw.iloc[i].values):
            header_row = i; break
    
    if header_row is not None:
        df = pd.read_csv(f, header=header_row)
    else:
        df = pd.read_csv(f)
    
    df.columns = [c.strip() for c in df.columns]
    
    # Extract PO name from metadata rows
    po_name = df_raw.iloc[0, 1] if pd.notna(df_raw.iloc[0, 1]) else os.path.basename(f)
    
    po_data[str(po_name)] = {'file': f, 'skus': {}}
    for _, row in df.iterrows():
        sku = str(row.get('SKU', '')).strip()
        if not sku or sku == 'nan': continue
        po_data[str(po_name)]['skus'][sku] = {
            'expected': int(row.get('Quantity', 0)),
            'received': int(row.get('Quantity Received', 0)),
            'on_hand': int(row.get('On Hand', 0)),
            'available': int(row.get('Available', 0)),
        }
```

---

## Step 1 — Stock Position

The core deliverable. For every SKU, produce a three-way split:

- **Confirmed Available** = ShipHero `Available`. This is stock physically in the warehouse, not quarantined, not allocated. Use this for days cover.
- **Quarantined / Allocated** = ShipHero `On Hand` minus `Available`. Includes damaged goods, quality holds, backorder allocations. Flag if significant.
- **Pending Inbound** = `Quantity` minus `Quantity Received` across all active POs for this SKU. Stock at the 3PL but not yet scanned in, or still in transit.

Compare against POS MODEL ON HAND:
- **Delta** = (Available + Pending Inbound) minus POS MODEL ON HAND
- Negative delta = stock unaccounted for
- Positive delta = POS MODEL understated or check-in happened but model not updated

Output:
```
STOCK POSITION — [REGION] — [Date]

SKU              Available  Quarantined  Pending In  POS MODEL OH  Delta
KIT-STA-2          1,204            0        800          2,004       0
LIQ-HEA-5           568           42        500          1,068     -42
LIQ-BAS-2           135          864          0            568    +431 ← QUARANTINED explains gap
```

Show all SKUs with stock > 0 or model DSR > 0. Group by category: Kits, Liquids, Colours (top 15), Accessories, Packaging/Inserts.

---

## Step 2 — Check-In Progress

For each ShipHero PO CSV provided:

```
CHECK-IN PROGRESS

PO Name              Total SKUs  Fully In  Partial  Not Started  Overall %
B360 Packup               247       180       42          25         82%
OP Heal Fill                 3         3        0           0        100%
```

For POs with partial check-in, show the detail:
```
--- PARTIAL: B360 Packup ---
SKU              Expected  Received  Remaining  % Done
ACC-REM-500           911         0        911      0%
POW-SEN-217           250         0        250      0%
LIQ-GLO-4           1,052     1,026         26     98%
```

Only show SKUs that are not fully checked in. If a PO is 100% complete, just note it in the summary — no detail needed.

---

## Step 3 — Double-Count Detection

For each Express Shipment block in the POS MODEL header:

1. Identify the shipment reference and its OL quantities per SKU
2. Find the matching ShipHero PO (by reference name match)
3. For each SKU: double-counted = min(OL, Quantity Received)
4. If Quantity Received > 0 for any SKU, the projected ON HAND is overstated

```
DOUBLE-COUNT DETECTION

Express Shipment: OP Heal/Remove 500ml
  POS MODEL status: In Production
  ShipHero match: PO 10 (Outsource Packaging fill)
  Check-in: 100% complete

  SKU              POS OL  Already In  Double-Counted  Impact
  LIQ-HEA-5        9,000      9,000          9,000    Projected OH overstated by 9,000
  ACC-REM-500       3,500          0              0    Not yet checked in — no double-count

  TOTAL OVERSTATEMENT: 9,000 units (1 SKU)
```

If no Express Shipment blocks have matching ShipHero POs with any Quantity Received > 0:
```
DOUBLE-COUNT DETECTION: No active check-ins overlap with POS MODEL projections. No double-counting detected.
```

---

## Step 4 — Corrected Days Cover

Calculate days cover on **confirmed available stock only** (ShipHero Available), NOT POS MODEL projected ON HAND.

Use POS MODEL DSR as the rate. For kit-adjusted items (region-specific — check Component Map):
- AUS/CA: Heal and ACC-INS are kit-adjusted (standalone + kit consumption)
- UK: Heal, Base, Glow, and ACC-INS are kit-adjusted

```
CORRECTED DAYS COVER

SKU              Available  DSR      Confirmed Cover  POS MODEL Cover  Diff     Flag
KIT-STA-2          1,204    34.0          35d              42d         -7d
KIT-COM-4          2,891    78.0          37d              68d        -31d
LIQ-HEA-5           568   184.6           3d              61d        -58d      CRITICAL
LIQ-BAS-2           135    53.3           3d              11d         -8d      CRITICAL
ACC-LAB            3,800   364.0          10d              11d         -1d      CRITICAL

AFTER-ARRIVAL PROJECTION (pending inbound fully checked in)
SKU              Available  + Pending  = Total   Days Cover After
LIQ-HEA-5           568       500       1,068          6d         still CRITICAL
KIT-STA-2          1,204       800       2,004         59d         OK after arrival
```

Flags:
- **CRITICAL (<7d confirmed cover)** — needs immediate action, can't wait for check-in
- **WARNING (<14d confirmed cover)** — at risk if check-in stalls or next shipment delays
- **WATCH (<30d confirmed cover)** — monitor

---

## Step 5 — Packaging & Insert Monitoring

Packaging SKUs and inserts don't sell on Shopify. Monitor via 3PL deduction rates.

1. Calculate average daily deduction from 3PL tab over last 14 days (exclude days where stock increased — container arrivals)
2. Days cover at that deduction rate using ShipHero Available stock
3. Compare daily deductions to benchmarks from `../Context/Deduction Benchmarks.md`
4. Flag any day in the last 14 where deduction exceeded the benchmark

```
PACKAGING & INSERTS

SKU              Available  Deduction/day  Days Cover  Benchmark  Anomaly Days
STO-BUB-BAG-L      8,420          177         48d        435           0
STO-MAI-BAG-S      2,100           71         30d        330           0
STO-MAI-2          5,100           73         70d        330           0
STO-BUB-BAG-S      3,200          159         20d        130           1 ← see below
ACC-INS             4,200          120         35d        435           0
ACC-LAB             3,800          211         18d        735           0
ACC-THA             5,100          211         24d        735           0

ANOMALIES:
  09 Apr — STO-BUB-BAG-S: 168 deducted (benchmark: 130) — check for bulk liquid orders
```

---

## Step 6 — Container / Order Status Cross-Reference

For each active shipment found in the POS MODEL header area (each column group has Our Reference, Est. Completion, Est. Arrival, Order Status):

1. Extract dates and status from the POS MODEL header block — this is the closest source of truth for timelines
2. Match against PO TRACKER by reference
3. Match against ShipHero PO CSV (if provided)
4. Search Slack regional + 3PL channel for the reference (last 14 days)
5. Search Gmail for the reference (last 21 days)

```
CONTAINER / ORDER STATUS

Ref: AUS 09052026
  POS MODEL:     In Production, Est. Completion 15 Apr, Est. Arrival not set
  PO TRACKER:    In Production
  ShipHero:      No PO found (not yet shipped)
  Slack:         Daniel: "100% delayed" (8 Apr). Joel: "worst case B113" (9 Apr)
  Gmail:         Joel emailed Mark re B114, no reply (5 days)
  REALITY:       Delayed to mid-May. B113 fallback discussed but no decision.
  ACTION:        Joel to confirm B113 vs wait for B114. Update POS MODEL Est. Completion.
```

Flag stale POS MODEL dates: if Est. Completion or Est. Arrival has passed and the shipment block still shows the old date, note it — the model needs updating.

---

## Step 7 — Local Fill Status

Check POS MODEL header for active fill PO references (look for "Local Filling PO" or "Outsource Packaging" or region-specific filler names from the Region file).

Cross-reference:
- Slack for latest filler updates
- Gmail for ingredient supplier correspondence
- ShipHero for any matching PO (fill deliveries get a PO when they arrive at the 3PL)

```
LOCAL FILL STATUS

Outsource Packaging — Heal + Remove 500ml (ref: 25-02-2026)
  POS MODEL:     In Production
  Ingredients:   Calcium Chloride ✅ | Coconut Oil + Vitamin E ✅ | Acetone ❌ (paid 9 Apr, no delivery)
  Lead time:     ~28 days from all ingredients at OP
  Earliest G3PL delivery: mid-May (if acetone arrives this week)
  ACTION:        Chase Sydney Solvents for acetone delivery date.

Outsource Packaging — Remove 500ml (ref: 24-03-2026)
  POS MODEL:     Ordering
  Status:        Not yet placed. Awaiting ingredients.
  ACTION:        Dependent on first fill completing.
```

If no active local fills: `No active local fills for this region.`

---

## Step 8 — Stock-Out Forecast

The core forward-looking analysis. For each SKU, project when it stocks out and whether inbound arrives in time.

Reference lead times from `../Context/Lead Times.md`:
- **84 days** = minimum to place a raw goods PO and receive via standard CN production + vessel
- **44 days** = minimum to place a filling PO and receive (production + shipping, raw goods already at Sally)
- **30 days** = shipping only (production complete, waiting to ship)
- **28 days** = local fill lead time (AUS, ingredients already at filler)

### For each SKU with confirmed stock and DSR > 0:

```
days_until_stockout = confirmed_stock / actual_DSR
```

### Cross-reference against each inbound shipment:

For each POS MODEL shipment block that includes this SKU (OL > 0):
```
days_until_arrival = est_arrival - today
gap = days_until_stockout - days_until_arrival

gap > 7   → safe, stock lasts well past arrival
gap 0-7   → tight, no margin for delay
gap < 0   → STOCKOUT |gap| days before arrival
```

If a shipment has no Est. Arrival set, use Est. Completion + 30 days shipping as a proxy.

### For SKUs with NO inbound on order:

```
if days_until_stockout < 14   → CRITICAL: express shipment or local fill only option
if days_until_stockout < 44   → too late for new CN PO, need express or local fill
if days_until_stockout < 84   → raw goods PO deadline approaching — flag for PO recommendation
if days_until_stockout >= 84  → OK for now, standard PO timeline available
```

### Output:

```
STOCK-OUT FORECAST

--- STOCKOUT BEFORE ARRIVAL (gap < 0) ---
SKU              Stock   DSR    Stocks Out   Next Inbound        Arrives    Gap
LIQ-BAS-2         777   53.3   in 15d       CA 03022026         Apr 25*   -10d stockout
                                             * delayed — duties unpaid. Original ETA Apr 2.
ACC-LAB-CA           0    —     NOW OOS      PO 35 Labels        TBD       no ETA set
                                             8,700 already at 247 but investigating.

--- TIGHT (gap 0-7 days) ---
SKU              Stock   DSR    Stocks Out   Next Inbound        Arrives    Gap
LIQ-SOA-6         338   16.0   in 21d       Swift Fill           TBD       no ETA — monitor

--- NOTHING ON ORDER (no inbound for this SKU) ---
SKU              Stock   DSR    Stocks Out   Deadline to Act
POW-XXX-123      450    25.0    in 18d       ⚠️ Past CN PO deadline (need 84d). Express only.
ACC-REM-BOW     1,435   80.0    in 18d       ⚠️ Past CN PO deadline. Check if on next planned order.

--- SAFE (gap > 7 days or 84+ days cover with no inbound needed) ---
[Count]: X SKUs with 30+ days cover and inbound arriving in time or not needed.
```

### Key signals to surface:
- **Stockout before arrival** — the most critical finding. Show the exact gap in days.
- **No inbound, under 84d** — missed the ordering window. Can only fix with express or local fill.
- **No inbound, under 44d** — even a rush PO won't arrive in time. Express shipment required.
- **Delayed containers** — use user-provided context (e.g. "duties unpaid") to adjust ETAs. Don't just use the POS MODEL date if it's known to be stale.
- **Local fills as a safety net** — if a liquid is stocking out and there's a local filler for it (check Region Inventory Config), flag this as an option with the ~28d lead time.

---

## Step 9 — What Needs Action

Three tiers. The stock-out forecast drives the critical tier — if something stocks out before its inbound arrives, that's the #1 priority.

```
WHAT NEEDS ACTION

🔴 CRITICAL (act today)
  - LIQ-BAS-2: 777 units, stocks out in 15d. CA 03022026 delayed (duties unpaid). 10d stockout gap.
  - ACC-LAB-CA: OOS now. 8,700 at 247 but under investigation. No confirmed available.
  - POS MODEL overstated by 2,873 units (OP Heal fill double-counted).
  - CA 03022026: 12d past arrival, duties need paying. 56 SKUs, 35k units blocked.

🟡 WARNING (act this week)
  - LIQ-SOA-6: 338 units, 21d cover. Inbound from Swift fill but no ETA set.
  - POW-XXX: under 84d cover with nothing on order — past raw goods PO deadline.
  - Acetone delivery unconfirmed — blocks Remove 500ml fill timeline.

🟢 MONITOR (FYI)
  - PO 9 check-in at 97%. 10k units remaining.
  - STO-BUB-BAG-S deduction rate 24% above benchmark — check with 3PL.
```

---

## Step 10 — Recommended Next PO Place Date

Using the lead time framework from `../Context/Lead Times.md`, calculate when the next PO needs to be placed to maintain 14-21 days of kit cover.

### Logic

For each key SKU category (kits, kit-adjusted liquids, high-velocity colours):

```
target_cover = 17 days  (midpoint of 14-21d lean target)

# When will stock hit the target cover level?
days_until_target = (confirmed_stock / actual_DSR) - target_cover

# Work backwards from that date:
restock_needed_by    = today + days_until_target
est_completion_by    = restock_needed_by - 30 days (shipping)
filling_po_place_by  = est_completion_by - 40 days (production)
raw_goods_po_by      = est_completion_by - 70 days (raw goods lead)
```

If there's already inbound stock (container on the way or in production), account for it:
```
# After inbound arrives, stock jumps. Recalculate from post-arrival stock level.
post_arrival_stock = confirmed_stock + inbound_OL
days_until_target_post = (post_arrival_stock / actual_DSR) - target_cover
```

Use whichever gives the later (more relaxed) deadline — you don't need to order again until the inbound is consumed.

### Output

```
PO RECOMMENDATIONS

Target: maintain 14-21d kit cover (lean). Lead times: 84d (raw goods → delivery), 44d (filling PO → delivery), 30d (shipping only).

--- KITS ---
SKU           Stock   DSR    Cover   Inbound           After Inbound   Next PO Place By     Raw Goods By
KIT-STA-2     2,491   14.1   176d    CA 03022026 +800  233d            no PO needed yet     no PO needed yet
KIT-ULT-6       859   10.6    81d    CA 03022026 +500  128d            no PO needed yet     no PO needed yet

--- KIT-ADJUSTED (Heal, ACC-INS) ---
LIQ-HEA-5    1,601   53.0    30d    Swift +7,500       172d            no PO needed yet     no PO needed yet

--- FLAGGED (approaching PO deadlines) ---
SKU           Stock   DSR    Cover   Next PO Place By    Raw Goods By     Status
LIQ-SOA-6      338    4.1    83d     ~May 28 (filling)   ~Apr 18 (raw)    ⚠️ raw goods deadline this week
ACC-REM-BOW  1,435   80.0    18d     PAST                PAST             🔴 express only
```

### Key rules:
- Only show SKUs where a PO deadline is within 30 days, or where it's already past
- If a SKU has inbound arriving, recalculate the deadline from post-arrival stock
- If a deadline is past, state what the only remaining options are (express shipment, local fill, or accept the stockout)
- For kits: the PO drives all kit contents from China. Flag the earliest kit deadline as the container PO deadline.
- For locally-filled items (Heal, Remove): use local fill lead time (~28d) instead of CN lead time
- Always specify the date, not just "in X days" — dates are actionable, relative days are forgettable

---

## Graceful Degradation

**If no ShipHero CSVs provided:**
- Skip Steps 2-3 (check-in progress and double-count detection)
- Step 1 uses POS MODEL ON HAND instead of ShipHero Available (no confirmed/pending split)
- Step 4 uses POS MODEL ON HAND for days cover
- Flag prominently: "Running without ShipHero data — stock position is based on POS MODEL only. Confirmed vs pending split not available."

**If region doesn't use ShipHero:**
- Same degradation as above
- Note which 3PL system the region uses and whether equivalent PO data is available

---

## Output Structure

```
POS MODEL CHECK — [REGION] — [Date]

DATA FRESHNESS
  POS MODEL last updated: [date]
  3PL data last valid: [date] ([X]d ago)
  ShipHero exports: [list of PO names]
  Growth factor: [X]x ([Y] base → [Z] scaled)

STOCK POSITION
  [Step 1]

CHECK-IN PROGRESS
  [Step 2]

DOUBLE-COUNT DETECTION
  [Step 3]

CORRECTED DAYS COVER
  [Step 4 — confirmed only + after-arrival projection]

PACKAGING & INSERTS
  [Step 5 — deduction rates, days cover, anomalies]

CONTAINER / ORDER STATUS
  [Step 6 — per-shipment cross-reference]

LOCAL FILL STATUS
  [Step 7]

STOCK-OUT FORECAST
  [Step 8 — stockout before arrival, tight, nothing on order, safe]

WHAT NEEDS ACTION
  [Step 9 — 🔴 / 🟡 / 🟢 tiers, driven by forecast]

PO RECOMMENDATIONS
  [Step 10 — next PO place dates, raw goods deadlines, flagged items]
```

---

## Style Notes
- Lead with DATA FRESHNESS — if ShipHero exports are >24h old, flag prominently. The whole skill depends on current data.
- STOCK POSITION is the anchor section. Everything else supports it.
- When showing days cover, always specify the rate: "3d at 184.6/day kit-adjusted DSR" — never ambiguous.
- Make double-count math explicit: "POS MODEL says X. ShipHero says Y already checked in. Therefore Z is double-counted."
- Numbers are always specific: "568 units, 3 days cover" — never "low stock".
- This skill does NOT cover: DSR comparison, weekly trends, selling performance flags, Shopify vs 3PL deduction alignment, stock loss/gain detection. Those belong in Sales Data Analysis.
- Packaging monitoring belongs HERE, not in Sales Data Analysis.
- The audience is Remy, Daniel, and Joel. Operational and sharp. Dot points over paragraphs.

---

## Post-Task
Update `../Context/Current Issues.md` with stock position findings for the region. Replace that region's section entirely.
