> **Context:** Get region info (which 3PL tab to use, inventory config) from `../Regions/[REGION].md`. Get kit-adjusted demand items from `../../Shared/Component Map.md`. Get deduction benchmarks from `../Context/Deduction Benchmarks.md`. Get lead times from `../Context/Lead Times.md`. After completing, update `../Context/Current Issues.md`.

# POS Model Check Skill

## Trigger
User asks for a stock position check, POS model check, check-in progress, double-count check, or packaging review. Also trigger on "what's actually available", "confirmed vs pending", "how much has been checked in", "is there double-counting", or when the user provides ShipHero PO CSV exports alongside an Order Schedule xlsx.

---

## Data Sources

### Order Schedule xlsx (from Google Drive)
**Always re-pull at the start of every POS Check.** Never reuse a prior extract, even from the same day — Greg updates POS MODEL daily (sometimes multiple times) and the 3PL tab updates independently. A "we already have the data" shortcut produces stale analysis.

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

### ShipHero PO CSVs (FALLBACK ONLY — not routine)
Don't prompt for these by default. The 3PL tab in the Order Schedule (AUS 3GPL, B360, etc.) is the live stock position. ShipHero CSVs are only useful when a container is **half checked-in** and we need to reconcile confirmed vs pending per SKU — a rare scenario. If the user explicitly provides CSVs or asks to reconcile a partial check-in, fall back to the Step 2/3 workflow for that specific container.

CSV columns, for reference:
- **Quantity** — expected on the PO
- **Quantity Received** — checked in so far
- **On Hand** — current total stock (warehouse-level)
- **Available** — on hand minus backorders/allocated

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
- **Bundle sales inflate 3PL deduction rates.** ACC-REM-BUN-1 (120ml + Bowl) and ACC-REM-BUN-2 (500ml + Bowl) sell as bundle SKUs on Shopify, but 3PL deducts the component SKUs individually. LIQ-SET (Liquids Set) deducts 1x of all 6 liquids per sale. If Greg sets POS MODEL DSR from 3PL deduction rates rather than Shopify sales, the model DSR for Remove 500ml, Remove Bowl, and liquids will be overstated. Always compare model DSR against Shopify standalone sales to detect this.
- **POS MODEL update timing vs same-day events.** The `UPDATED` cell (POS MODEL H9) shows when Greg last pasted data. If Katrina (G3PL) or a supplier confirms an event (PO check-in, stock adjustment) **after** that timestamp, the sheet won't show it. Always check the `UPDATED` time against known same-day Gmail/Slack events and apply **manual overrides** at the top of the analysis (e.g. "ACC-LAB = 18,344 on hand post Avi PO 11 check-in 16 Apr; sheet shows 3,397"). List every manual override up front so the reader sees the deltas.
- **Growth factor per container.** Different containers can be sized at different growth factors (e.g. AUS 07062026 Birthday Sale at 1.4x, standard at 1.3x). The per-container growth factor lives in each shipment block header (row 7, GROWTH FACTOR column). When projecting post-arrival cover, switch to the container's own growth factor for its landing window, not the global J9 value.

---

## Pre-built Scripts

Run `../Scripts/extract.py [REGION]` first to download the xlsx and parse all tabs into structured JSON. Then pipe into the analysis scripts:

```bash
uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py AUS > /tmp/aus.json
cat /tmp/aus.json | uv run --with pandas python3 Ops/Scripts/forecast.py
cat /tmp/aus.json | uv run --with pandas python3 Ops/Scripts/deductions.py
```

The scripts handle all data quirks (corrupted columns, last valid date detection, container arrival exclusion, benchmark comparison). Use their output as the data foundation, then interpret and write the narrative.

If the scripts are unavailable or need updating, fall back to the inline preprocessing below.

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

## Step 0a — Gmail & Slack Reconcile (do this BEFORE finalising any cover math)

The POS MODEL sheet is pasted by Greg once a day, often in the AM. Events that happen **after** Greg's paste — a 3PL check-in, a supplier confirmation, a stock adjustment — won't be in the sheet until tomorrow. If you run the POS Check straight off the xlsx, you will publish a stale view and potentially a false RED CRITICAL.

**Example that actually happened (16 Apr 2026):** POS MODEL said ACC-LAB = 3,397 units / 15d cover → flagged RED CRITICAL "chase Avi immediately". Same evening Katrina emailed confirming PO 11 (Avi) received = 18,344 on hand, ~75d cover. The critical flag was already resolved.

### Procedure

1. **Read the POS MODEL `UPDATED` cell** (POS MODEL H9 for AUS; equivalent for other regions). Note the date AND time if available. That's your data-cutoff.

2. **Sweep Gmail for the period between `UPDATED` and now** — filter to:
   - 3PL operations contacts (Katrina, Jake, David for AUS; equivalents per region)
   - Local fillers (Peter/OP, Chemence, Swift, Oils4Life)
   - Local printers (Avi, Print Runner, Mixam)
   - Sally (Isay Nail), Lily (shipping agent)
   - Greg (stock reconciliation, ASN updates)
   
   Query template: `after:YYYY/MM/DD (from:katrina@... OR to:pjoseph@... OR subject:PO OR "received" OR "inbounded" OR "stocked in")`

3. **Sweep Slack** — regional inventory channel + 3PL channel since `UPDATED`. Look for messages from Katrina, David, Peter, Jake, Remy, Daniel, Joel that confirm actions.

4. **Identify manual overrides.** For each event since `UPDATED`, decide whether to override the sheet figure. Examples:
   - "Katrina: PO 11 Booklet received 16 Apr PM" → ACC-LAB overridden to user-confirmed figure (18,344)
   - "Greg 16 Apr: ACC-THA -11,200 discrepancy identified" → ACC-THA adjusted down pending Katrina confirmation
   - "Peter: Acetone received at OP 15 Apr" → OP Remove fill no longer ingredient-blocked

5. **List manual overrides at the top of the POS Check.** Format:
   ```
   Manual overrides applied to sheet figures:
   - ACC-LAB: 18,344 on hand (Avi PO 11 received 16 Apr; sheet shows 3,397 — Greg pasted AM, Katrina booked PM)
   - ACC-THA: 21,587 (32,787 less Greg-identified 11,200 B360 shortfall; pending Katrina reply Fri 18 Apr)
   ```

6. **Apply the overrides** to every downstream calculation (cover, windows, container gaps). Don't silently use the sheet value anywhere after this step.

7. **If the user confirmed a figure** (e.g. "18,344 on hand post-Avi"), prefer that figure. Ask before assuming.

This step is mandatory. A POS Check without a Gmail reconcile is a guess.

---

## Step 0b — Growth Factor Health Check

Compare the POS MODEL growth factor against actual 14d kit selling. This is a health check, not a correction — the growth factor is aspirational and tied to marketing/ad spend goals. We generally want to push for it, and would rather have slightly too much stock than not enough given container lead times.

```
actual_14d_kit_total = sum of 14d Shopify DSR for STA + COM + ULT
actual_growth = actual_14d_kit_total / model_kit_base_total
gap = (model_growth - actual_growth) / model_growth × 100
```

Report:
- Current growth factor vs actual
- Gap as a percentage (e.g. "selling 67% below scaled target")
- Whether the gap is narrowing, stable, or widening vs previous reviews
- Impact on stock cover: "At model rate: Xd cover. At actual rate: Yd cover."

**Flag if gap > 50% for 4+ consecutive weeks** — this means ordering decisions are significantly disconnected from demand. Don't recommend lowering the growth factor outright, but flag that stock levels will accumulate faster than expected and future container quantities should be reviewed.

Check the region file for any overstocking flags from previous reviews.

---

## Step 0c — Kit-Adjusted DSR Validation

Before proceeding, validate whether the POS MODEL DSR already includes kit consumption for each kit-adjusted item (check `../../Shared/Component Map.md` for the region).

For each kit-adjusted SKU:
```
kit_consumption = sum of scaled kit DSRs that consume this item
model_dsr = stock / days_cover from POS MODEL

if model_dsr >= kit_consumption * 0.8:
    # Model DSR already includes kit consumption (e.g. Heal, ACC-INS)
    kit_adjusted_dsr = model_dsr
else:
    # Model DSR is standalone only — ADD kit consumption
    kit_adjusted_dsr = model_dsr + kit_consumption
    # FLAG: "POS MODEL DSR understated for [SKU] — standalone {model_dsr}/day + kit {kit_consumption}/day = {kit_adjusted_dsr}/day"
```

**Why this matters:** When a region changes 3PL or changes its kit assembly process, items may become newly kit-adjusted (or stop being kit-adjusted). The POS MODEL may not be updated yet. Always verify against the Component Map and recent 3PL comms.

Cross-reference with B360/3PL deduction data where available — if the 3PL was deducting a liquid at ~1/day but the Component Map says it's kit-adjusted at 90/day, the 3PL process may have recently changed. Check Slack/Gmail for 3PL setup changes.

---

## Step 1 — Stock Position

The core deliverable. For every SKU with stock > 0 or model DSR > 0, show stock and TWO cover numbers side by side:

- **Projected DSR** = POS MODEL SKU DSR × growth factor (the aspirational rate we order against)
- **Actual DSR** = 3PL 14d deduction rate (excludes container arrival days). This captures true demand including bundles + kit consumption.
  - Fall back to **Shopify DSR** for SKUs where the 3PL rate is corrupted by a known anomaly (mystery deduction spikes, stock adjustments). Mark these with a caret (^) or similar.
  - Use the actual-DSR cover as the operational number — projected is the ambition target.

Output:
```
STOCK POSITION — [REGION] — [Date]

SKU              Stock   Projected DSR  Cover @ Projected  Actual DSR  Cover @ Actual
KIT-STA-2        1,165        44.2            26d             30.8         38d
LIQ-BAS-2          604        53.3            11d             20.7         29d
LIQ-HEA-5       10,449       184.6            57d            123.7         84d
```

Group by category: Kits, Liquids, Remove products, Inserts / packaging, Colours (only flag the ones with anomaly-driven divergence or critical cover). Don't dump 150+ colour rows — call out exceptions.

**Don't include a third column for model-alone or Shopify-alone rates** — keep to the two-cover format. If a rate substitution is needed (e.g. 3PL corrupted), annotate inline, don't add a column.

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

## Step 8.5 — Dual-DSR Stock Coverage View

Show cover simultaneously at three rates to expose model vs reality divergence. This is the most important single artefact a reader takes away.

For each critical SKU, compute:

```
cov_model   = stock / (SKU model DSR × growth factor)
cov_3pl     = stock / 3PL avg deduction per day (last 14d, excluding arrivals)
cov_shop30  = stock / Shopify 30d DSR   (where SKU sells standalone)
```

Present as a single table with all three covers side by side. Call out the divergences explicitly:
- **All three agree (within 20%)** → trust the number.
- **Model > 3PL > Shopify** (typical) → model is inflated; 3PL captures reality including bundles/kit consumption.
- **3PL > Model > Shopify** → the SKU is consumed faster than the model thinks (e.g. ACC-REM-500 at 168/d 3PL vs 99/d model). Real cover is the 3PL view. The model UNDER-states risk on these.
- **Shopify > 3PL** → typically data lag or a kit/bundle not accounted for. Investigate before acting.

Whichever rate is **fastest** is the cover number that matters operationally. Call it out in the headline cover column.

---

## Step 8.6 — Container Gap Analysis

This is the "what's missing from an in-flight container that we need to flag" step. A container can land on time and still leave you OOS on something that wasn't on it.

For each in-production / planned container, pull its SKU contents from the POS MODEL shipment block (OL > 0). Then for every SKU with a flagged cover gap, ask:

1. **Is this SKU in the next landing container?** If no — and it stocks out in that window — it's a gap.
2. **Is the OL quantity sufficient** for actual selling through the window *to* the following container? If the container replenishes to 20d cover but the next container is 45 days away, it's a partial gap.
3. **Where does the SKU come from?** Some SKUs are never in CN containers (ACC-LAB = Avi local print; LIQ-HEA-5 = OP local fill). A "gap" for these means **a local PO needs placing**, not a container change.

Output a per-container gap list:

```
AUS 08072026 — CRITICAL GAPS (Fill PO due 29 Apr)
  - ACC-LAB: 0 units. Current 18,344, OOS ~1 Jul, no Avi PO in pipeline.
    → Place Avi PO ~mid-May for 20,000 units.
  - ACC-THA: 0 units in container. Post-07062026 cover 20-27d at actual/model rate. Gap of 10d before 08072026.
    → Add 20,000 ACC-THA to 08072026 OR place a standalone print order.
  - LIQ-HEA-5: 0 units ready. Entirely dependent on OP fills.
    → Fill PO must be continuous.
```

Common SKUs to check specifically: **ACC-LAB, ACC-THA, LIQ-HEA-5, ACC-REM-500**. These have recurring container-gap patterns because they are locally sourced or kit-adjusted.

---

## Step 8.7 — Container Pushback Sensitivity

Only run when there's **evidence of a specific delay** (Slack/Gmail flag, e.g. B114 jars slipping, customs held). Don't stress-test every container blindly.

When a delay is identified:
1. Model the pushback at the **evidence-based duration** (e.g. "Mark says ~20 days B114" → +14d arrival).
2. Recompute stockout gaps for every SKU that depends on that container.
3. Show at **both 1.3x model and actual 0.86x rates** — the user cares about both.
4. Explicitly list the bridging options: Sally express via Lily, kit swap (STA↔COM precedent), cross-regional redirect (only if user confirms region is in scope), local fill alternative.

---

## Step 9.5 — Local Fill Sizing

When recommending a fill PO quantity (Heal, Remove, etc.), use explicit lead times + projected DSR. Don't hand-wave a round number.

### Inputs
- **Lead time components** — ask the user or check `../Context/Lead Times.md`. For AUS OP Heal fills: ~21d ingredients + 30d filling + 7d shipping = **58d**. For OP Remove 500ml: shorter (~14d fill + 7d ship if ingredients on hand). Confirm with Peter if uncertain.
- **Projected DSR** — the POS MODEL growth factor (J9 on POS MODEL tab for AUS). E.g. 1.3x × 147 base kits + standalone Shopify for Heal = **184.6/d**.
- **Current stock** at the filler SKU.
- **Next container bringing this SKU** (is any? — for Heal on AUS, usually none).

### Formula

```
consumption_during_lead = lead_days × projected_DSR
stock_at_delivery       = current_stock - consumption_during_lead
target_post_fill_cover  = desired_cover_days × projected_DSR
fill_qty                = target_post_fill_cover - stock_at_delivery
```

Pick `desired_cover_days` based on the fill cycle:
- If next fill will be placed ~lead_days after this one lands, aim for `1.5 × lead_days` post-fill cover (buffer for cycle slip).
- If you want `2 × lead_days` cover (conservative) — rounds up.
- If user prefers lean (common), aim for `1.2 × lead_days`.

### Output format

Always show 3 scenarios (lean / recommended / conservative) and both 1.3x projected + actual-rate cover. Let the user decide based on overstock appetite:

```
Heal fill sizing:
  Lead: 58d | Projected 184.6/d | Current 10,893 | Stock at delivery: ~186

  Qty        Cov @ 1.3x        Cov @ actual 0.86x
  12,000         66d                96d        (lean)
  15,000         83d               121d        (recommended)
  18,000         99d               144d        (conservative)
```

Flag if stock at delivery is negative — that means there will be an OOS gap before the fill lands; quote it in days.

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

## Step 10a — Local Fill Forecast

For regions with active local fillers (Chemence, Oils4Life, Swift, Outsource Packaging), forecast when the next fill needs to be placed. This is often more urgent than CN container timing.

### For each locally-filled liquid:

```
# Current fill in pipeline
fill_arriving = dispatch_date + transit_days
stock_at_arrival = current_stock - (days_to_arrival * kit_adjusted_dsr)
stock_after_fill = stock_at_arrival + fill_qty

# When does post-fill stock hit target cover?
days_to_target = (stock_after_fill / kit_adjusted_dsr) - target_cover
restock_needed_by = fill_arriving + days_to_target
place_next_by = restock_needed_by - filler_lead_time
```

### Demand spike adjustment

If a known demand spike is approaching (Birthday Sale, Black Friday, seasonal):
- Check the growth factor in the relevant container header block (e.g. 1.4x for Birthday Sale)
- For the spike period (~2-4 weeks), use scaled DSR instead of baseline
- This pulls the "place by" date forward — show both dates (baseline vs spike-adjusted)

### Output

```
LOCAL FILL FORECAST

Chemence — Base (LIQ-BAS-2) — DSR: 89.6/day kit-adjusted
  Current: 1,629 units (18d)
  Fill arriving: 29 Apr (+8,000) → 8,317 post-fill (93d)
  Next fill place by: ~12 May (at 8-week lead)
  If Birthday Sale (1.4x late Jul): place by ~5 May
```

Only show locally-filled items. If no local fills active: "No active local fills for this region."

---

## Step 10b — Recommended Next PO Place Date

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

## Step 10c — Cascading Arrival Projection

The key forward-looking view. For each active shipment in sequence, show what the stock position looks like as each one arrives — accounting for consumption between arrivals. This answers: "where are we now, where are we after the next container, and where are we after the one after that?"

### Logic

Order all inbound shipments chronologically by Est. Arrival. For each stage:

```
Stage 0 (NOW): current confirmed stock → cover at actual DSR
Stage 1 (after Shipment A arrives):
    stock_consumed = actual_DSR × days_until_A_arrives
    remaining = current_stock - stock_consumed
    post_arrival = remaining + Shipment_A_OL
    cover = post_arrival / actual_DSR
Stage 2 (after Shipment B arrives):
    stock_consumed = actual_DSR × days_between_A_and_B
    remaining = post_A_stock - stock_consumed
    post_arrival = remaining + Shipment_B_OL
    cover = post_arrival / actual_DSR
...continue for each shipment
```

### Output

```
CASCADING ARRIVAL PROJECTION

Target cover: 45-75 days | Actual kit DSR: [X]/d

--- KITS ---
                     NOW           After [Ref A]       After [Ref B]       After [Ref C]
                     Stock  Cover   Stock  Cover        Stock  Cover        Stock  Cover
KIT-STA-2            2,477  167d    4,465  301d  ⚠️     5,199  328d  ⚠️     ...
KIT-COM-4            3,779  138d    8,567  312d  ⚠️     ...
KIT-ULT-6              852   82d    3,512  337d  ⚠️     ...
ALL KITS             7,108  135d   16,544  314d  ⚠️    20,940  370d  ⚠️

--- LIQUIDS / REMOVE / KEY ITEMS ---
[Same cascading format for items that have inbound]

⚠️ = cover exceeds 100d (potential overstock vs 45-75d target)
```

### Delay scenario

After the projection table, answer: **"If [next shipment] is delayed, what stocks out?"**

For each SKU, calculate how long current stock (without the next shipment) lasts at actual DSR. If anything stocks out before the shipment after it arrives, flag it:

```
IF [Ref A] IS DELAYED:
  KIT-ULT-6: current 852 at 10.4/d → stocks out 82d (5 Jul). [Ref B] arrives 5 Jul — cuts it close.
  LIQ-SOA-6: current 338 at 4.0/d → stocks out 85d (9 Jul). [Ref B] arrives 5 Jul — OK.
  All other SKUs: safe until [Ref B].
```

### Overstock flag

If any SKU exceeds 100d cover after a shipment arrival, flag it with the excess vs target:

```
OVERSTOCK FLAGS (post-arrival cover > 100d, target 45-75d):
  KIT-COM-4: 312d cover, +252d over target, +6,923 excess units
  ACC-REM-BOW: 462d cover, +402d over target, +7,450 excess units
  → Review future container quantities for these SKUs
```

This is especially important when the growth factor is aspirational (higher than current actual). Flag the gap: "Model assumes [X]/d. Actual is [Y]/d. If demand doesn't scale to target, these quantities represent [Z] months of excess inventory."

---

## Partial Check-In Mode (ShipHero CSVs)

Only relevant when a container is actively mid-check-in and we need to reconcile confirmed vs pending per SKU. In this mode only:
- User provides ShipHero CSV exports per active PO
- Run Steps 2 and 3 (check-in progress + double-count detection)
- Show confirmed / pending / quarantined split in Step 1

Outside of that scenario, use the 3PL tab as the stock position and skip Steps 2 and 3.

**If region is mid-3PL transition:**
- Two 3PLs may be active. Stock at old 3PL = pending transfer, not sellable until physically moved.
- The POS MODEL may have a "Packup" or transfer block in Express Shipment columns — treat this as a stock transfer, not a CN shipment. It has no Est. Completion/Arrival dates from Sally.
- 3PL process changes (e.g. new 3PL picks different items per kit) may change which items are kit-adjusted. Verify against recent emails to the new 3PL.
- Don't assume quarantined stock at the old 3PL is usable — it may include components, returns, or work-order inventory that isn't finished product. Cross-check with stocktake data.
- Check whether the stock-out/offboarding process has been initiated: deposit paid, work orders submitted, stocktake timeline confirmed.

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

LOCAL FILL FORECAST
  [Step 10a — per locally-filled liquid: current fill ETA, post-fill cover, next placement date, spike adjustment]

PO RECOMMENDATIONS
  [Step 10b — next PO place dates, raw goods deadlines, flagged items]

CASCADING ARRIVAL PROJECTION
  [Step 10c — stage-by-stage cover as each shipment arrives, delay scenarios, overstock flags]

FOLLOW-UP ITEMS
  Immediate / By end of month / Ongoing — with checkboxes
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
