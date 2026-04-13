> **Context:** Get region info from `../Regions/[REGION].md`. Get component map from `../../Shared/Component Map.md`. After completing, update `../Context/Current Issues.md`.

# Region POS Model Check Skill

## Trigger
User uploads an Order Schedule xlsx (e.g. `Canada_Order_Schedule.xlsx`, `UK_Order_Schedule.xlsx`) and asks for a region check, review, or recap. Also trigger if user says "check the model", "POS check", "validate against Slack", or any variation of cross-referencing inventory data with a region report.

---

## Region → Sheet Expectations
Each region's order schedule follows the same structure with these key tabs:
- **POS MODEL** — master tab with current stock levels, DSR, days cover, run-out dates, container/order status, growth factor
- **SALES** — configured date range showing DSR vs Shopify actual, status per SKU, Shopify daily rates
- **PO TRACKER** — all CN filling POs with status (Completed / In Production / Placed)
- **CNTR TRACKER** — all shipments with status (Delivered / In Transit / Organised)
- **B360** — daily inventory snapshots from the 3PL (columns = dates, rows = SKUs)
- **SHOPIFY** — daily sales data per SKU
- **RECONCILIATION** — per-order book-in data with discrepancies
- **DSR** — historical DSR snapshots
- **PASTE** — latest inventory paste from 3PL
- **B2G4 TRACK** — batch/lot tracking for kits and liquids

**Note:** AUS uses `AUS 3GPL` tab instead of `B360`. Check the Region file for which tab to use.

---

## Instructions

### Phase 1 — Read the POS Model (always do this first)

1. **Read the POS MODEL tab** — extract:
   - Growth factor (row 8, column near "GROWTH FACTOR")
   - Updated date (row 8, near "UPDATED")
   - Current DSR per kit type (rows 1-4: Starter, Complete, Ultimate, and the scale multiplier)
   - Per-SKU: product name, SKU, 3PL on hand qty, days cover, run-out date, status (In Stock / Out of Stock)
   - Container/order info embedded in the header area (order references, statuses, ETAs)
   - Any active local fill PO info (reference, status, est. completion)

2. **Read the SALES tab** — extract:
   - Date range (FROM / TO), days total, growth factor used
   - Per sold SKU: B360 on hand, status, DSR, projected demand, Shopify actual sales, Shopify daily rate, Shopify vs DSR %
   - Summary stats: how many in stock, how many OOS, avg Shopify vs DSR %

3. **Read the PO TRACKER** — extract:
   - Total orders, how many placed / in production / completed
   - For each non-completed order: reference, status, est. completion date, items included

4. **Read the CNTR TRACKER** — extract:
   - Total orders, how many in transit / delivered
   - For each in-transit or organised: reference, ASN, send date, ETA, shipment type

### Phase 2 — Read the Region Slack Channel (always do this)

5. **Read 30 days of the region's Slack channel** per the Region Recap skill instructions.
6. **Identify the most recent summary** and read its thread for any replies/resolutions.
7. **Capture all messages posted after the most recent summary.**

### Phase 3 — Cross-Reference & Validate

Run these checks and flag any discrepancies:

#### Stock Level Validation
- Compare OOS items in the SALES tab against what the Slack summary reported as OOS
- Flag any items the summary says are "in stock" but the model shows OOS (or vice versa)
- Flag any items with <14 days cover that weren't mentioned in the summary

#### DSR & Growth Factor Check
- Note the growth factor in the model vs what the summary states
- Calculate the actual Shopify vs DSR gap from the SALES tab
- If the gap is >40% below DSR consistently, flag this as "growth factor likely needs revision"
- State what the actual average daily kit sales were in the period vs what DSR forecasts

#### Container/Order Status Validation
- Cross-reference containers mentioned in the Slack summary against CNTR TRACKER
- Flag any containers the summary says are "on the way" but the tracker shows as "Delivered" (or vice versa)
- Flag any containers with ETAs that have passed but status hasn't been updated
- Check if any "In Production" POs in PO TRACKER have est. completion dates that have passed without status update

#### Days Cover Reality Check
- The POS model calculates days cover using the DSR (which includes the growth factor)
- Calculate a **realistic days cover** using actual Shopify daily sell rate from SALES tab instead
- Present both side by side for top-selling SKUs (kits, Heal, Remove, key accessories)
- This shows the difference between "days cover if we hit forecast" vs "days cover at actual selling rate"

#### Local Fill / Supplier Status
- Check if any local fill POs are mentioned in the model header area
- Cross-reference with Slack for the latest status updates
- Flag if a fill is listed as "In Production" in the model but Slack indicates it's completed or delayed

#### Batch Expiry Check (B2G4 TRACK)
- Scan the B2G4 tab for any batches with expiry dates within the next 60 days
- Flag any "Currently Used" batches approaching expiry

### Phase 4 — Compile the Report

Present the output in this structure:

---

#### 🇽🇽 [REGION] POS Model Check — [Today's Date]

**Model last updated:** [date from POS MODEL]
**Growth factor:** [X]x ([Y] kits/day)
**Sales period:** [FROM] to [TO] ([Z] days)

**📊 Forecast vs Reality**
- DSR forecast: [X] kits/day
- Actual Shopify: [Y] kits/day
- Gap: [Z]% below forecast
- Recommendation: [keep / revise down to Nx]

**🚨 Discrepancies Found**
List each discrepancy with:
- What the model/summary says vs what the data shows
- Impact (e.g. "summary didn't flag this OOS item with DSR of 100")
- Suggested action

**📦 Container/Order Status**
For each active order, show:
- Model status vs Slack status vs reality
- Flag any stale ETAs or unconfirmed arrivals

**📈 Days Cover: Forecast vs Actual**
Table showing top SKUs with:
| SKU | On Hand | DSR Days Cover | Actual Days Cover | Run-Out (DSR) | Run-Out (Actual) |

**⚠️ Items Approaching Risk**
- Items <14 days cover at DSR
- Items <30 days cover at actual (these matter if selling picks up)
- Any expiring batches

**✅ All Clear**
- Items/areas where model and Slack are aligned and no issues found

---

## Style Notes
- Be specific with numbers. Don't say "underselling significantly" — say "selling 68% below DSR"
- When flagging discrepancies, always state what the model says AND what reality shows
- Don't repeat the full Slack summary — focus on what doesn't match or what's missing
- If the model hasn't been updated recently (>3 days stale), flag this prominently at the top
- The audience is Remy, Daniel, and Joel — keep it operational

---

## Post-Task
Update `../Context/Current Issues.md` with any new discrepancies found.
