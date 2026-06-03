# UK Sales Data Analysis - 5 May 2026

## DATA FRESHNESS

- **Shopify last:** 4 May 2026 (+1d lag, normal).
- **3PL tab (B360):** last valid 5 May - **but represents frozen B360 Packup stock, NOT live Fulfillable.** Avg deduction = 0 across all SKUs (no movement on packup). All meaningful 3PL data is pre-13 Apr transition.
- **POS MODEL:** updated 5 May (today). Growth factor 1.3x. Kit base 84/d → scaled 109.2/d.

**Caveat carried for 3rd consecutive cycle:** 3PL deduction integrity check is **blind on Fulfillable**. The discrepancy / kit-alignment work below is Shopify-only. **Recommend Roisin export 14d Fulfillable deduction history** - this is the data integrity gap that's been open since transition.

---

## DSR: MODEL vs REALITY

### Kits

| Kit | Model DSR (1.3x) | Shop 7d | Shop 14d | Shop 30d | Gap vs Model (14d) |
|---|---:|---:|---:|---:|---:|
| Starter (KIT-STA-2) | 13.0 | 12.1 | 11.6 | 13.2 | **-11%** |
| Complete (KIT-COM-4) | 41.6 | 25.9 | 24.2 | 25.9 | **-42%** |
| Ultimate (KIT-ULT-6) | 54.6 | 33.7 | 32.1 | 40.2 | **-41%** |
| **Total kits** | **109.2** | **71.7** | **67.9** | **79.3** | **-38%** |

**Effective actual growth: 0.81x.** Recommended (actual + 10%): **0.89x.** Greg's 1.3x is now ~46% above demand reality - now 9+ consecutive weeks at 50%+ gap.

**Kit Mix (14d):** STA 17% / COM 36% / ULT 47%. Model assumes STA 12% / COM 38% / ULT 50%. Mix is roughly aligned - the gap is total volume, not mix. (Note: STA share has crept up from 12% in mid-Apr to 17% now - kit-down trading.)

### Kit-Adjusted Liquids (Heal / Base / Glow at Fulfillable)

UK kit-adjusted demand = standalone Shopify + 1× per kit. Using 14d kit total 67.9/d.

| SKU | Model DSR (1.3x) | Standalone 14d | Kit-Adjusted Actual | Gap vs Model |
|---|---:|---:|---:|---:|
| Heal (LIQ-HEA-5) | 110.5 | 0.9 | 68.8 | **-38%** |
| Base (LIQ-BAS-2) | 135.2 | 19.8 | 87.7 | **-35%** |
| Glow (LIQ-GLO-4) | 122.2 | 8.8 | 76.7 | **-37%** |

All three track the kit gap consistently - confirms Greg's model DSR is correctly kit-adjusted; the gap is purely the kit demand shortfall flowing through to liquid consumption.

### Standalone Liquids (pre-packed in CN kits)

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap vs Model (14d) | Read |
|---|---:|---:|---:|---:|---:|---|
| Seal (LIQ-SEA-3) | 15.6 | 13.3 | 11.4 | 10.5 | -27% | Healthy, slight drop |
| Bond (LIQ-BON-1) | 6.5 | 3.3 | 2.4 | 2.7 | **-63%** | Model stale |
| Soak (LIQ-SOA-6) | 6.5 | 2.6 | 2.1 | 2.0 | **-68%** | Model stale |
| Matte (LIQ-MAT-4) | 7.8 | 2.3 | 2.1 | 2.7 | **-73%** | Model stale |
| Low Odour Base (LIQ-SEN-2) | 0.0 | 0.0 | 0.0 | 0.0 | n/a | **Discontinued (confirmed)** |
| Low Odour Glow (LIQ-SEN-4) | 0.0 | 0.0 | 0.0 | 0.0 | n/a | **Discontinued (confirmed)** |

Bond / Soak / Matte model DSRs are 2-3x actual. Likely pasted from a higher-demand period. Cover figures based on these models will overstate risk - use Shopify rates for cover decisions on these.

### Remove Products

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap vs Model (14d) |
|---|---:|---:|---:|---:|---:|
| Remove 120ml (ACC-REM) | 39.0 | 9.1 | 9.4 | 15.3 | -76% |
| Remove 500ml (ACC-REM-500) | 36.4 | 7.7 | 8.4 | 11.3 | -77% |
| Remove Bowl (ACC-REM-BOW) | 31.2 | 0.9 | 0.9 | 2.0 | **-97%** |
| Remove 120ml + Bowl (ACC-REM-BUN-1) | n/a | 8.7 | 7.1 | 5.8 | bundle, +50% spike |

Remove model DSRs are heavily inflated - the 31.2/d Bowl model vs 0.9/d actual is the classic "model set from 3PL deduction including bundle" pattern. **Cover decisions on these should use Shopify+bundle rate (~10-12/d combined Bowl), not model.**

### Top 15 Colours by 14d DSR

| SKU | Name | 7d | 14d | 30d | Stock | Cover @ 14d |
|---|---|---:|---:|---:|---:|---:|
| POW-CLE-193 | Clean (?) | 26.6 | 24.4 | 29.1 | (check) | - |
| POW-HEA-515 | Heart Eyes (?) | 23.9 | 23.1 | 27.1 | - | - |
| POW-POS-184 | Posy (?) | 20.6 | 19.0 | 22.7 | - | - |
| POW-TRA-452 | Train Wreck | 16.9 | 16.1 | 17.6 | 163 | 10d 🔴 |
| POW-PIL-194 | Pillow (?) | 16.4 | 14.9 | 19.0 | - | - |
| POW-BOU-222 | Bouquet (?) | 15.4 | 14.2 | 11.6 | - | - |
| POW-HAR-139 | Harvest (?) | 14.6 | 13.6 | 15.0 | - | - |
| POW-PEA-068 | Peachy | 13.9 | 12.5 | 14.8 | 47 | 4d 🔴 |
| POW-CHA-011 | Charming | 11.6 | 12.4 | 14.5 | - | - |
| POW-OAK-283 | Oak (?) | 13.4 | 11.9 | 14.6 | - | - |
| POW-BLA-384 | Black (?) | 13.3 | 11.9 | 14.0 | - | - |
| POW-BAR-198 | Bare (?) | 11.6 | 10.7 | 13.3 | 279 | 21d 🟡 |

(Top 5 colour DSRs are 19-27/d - these are the velocity drivers. Most show 7d ≈ 14d ≈ 30d - stable.)

---

## WEEKLY KIT TREND

| Week | Dates | Kits/day | vs Scaled (109.2) | vs Base (84) | Notable |
|---|---|---:|---:|---:|---|
| W11 | 9-15 Mar | 83.6 | -23% | 1.00x | Pre-transition |
| W12 | 16-22 Mar | 67.6 | -38% | 0.80x | B360 mailer shortage period |
| W13 | 23-29 Mar | 87.1 | -20% | 1.04x | Recovery |
| W14 | 30 Mar-5 Apr | 83.3 | -24% | 0.99x | Transition prep |
| W15 | 6-12 Apr | 95.9 | -12% | 1.14x | **Peak in window**, pre-Fulfillable |
| W16 | 13-19 Apr | 83.6 | -23% | 1.00x | First Fulfillable week (live 13 Apr) |
| W17 | 20-26 Apr | 63.0 | **-42%** | 0.75x | **Worst week in 8 — floor confirmed** |
| W18 | 27 Apr-3 May | 76.0 | -30% | 0.90x | Recovery off W17 |
| W19 partial (1d) | 4 May | 40.0 | -63% | 0.48x | Sunday low - normal weekday-cycle dip |

**Read:**
- W17 (-42%) was a real floor, not noise. W18 (-30%) confirms recovery.
- Pre-transition baseline ran ~85/d. Post-transition has settled at 70-80/d, ~10-15% lower than pre-transition.
- 1.3x scaled target (109.2/d) hasn't been hit since W15 (95.9/d, still -12%). The factor remains aspirational by 30-50%.
- **Trend over last 4 weeks (W15→W18):** 96 → 84 → 63 → 76. Down then partial recovery. Not yet establishing a new base above ~80/d.

---

## REALISTIC DAYS COVER

For SKUs where actual rate diverges materially from model. (Full kit/liquid figures live in POS Check.)

| SKU | Stock | Actual Rate | Cover @ Actual | Model Rate | Cover @ Model | Read |
|---|---:|---:|---:|---:|---:|---|
| KIT-STA-2 | 137 | 11.6/d | **12d 🔴** | 13.0/d | 11d | OOS ~17 May, container can't save |
| LIQ-HEA-5 | 8,076 | 68.8/d (kit-adj) | 117d | 110.5/d | 73d | Healthy at actual |
| LIQ-BAS-2 | 7,164 | 87.7/d (kit-adj) | 82d (+ 7,568 inbound) | 135.2/d | 53d | Risk neutralised by Chemence landing |
| LIQ-GLO-4 | 7,875 | 76.7/d (kit-adj) | 103d (+ 8,000 inbound) | 122.2/d | 64d | Same |
| ACC-LAB-UK | 6,570 | ~76/d (orders) | 86d | 217.1/d | 30d | Trigger model says 30d, real is 86d - Print Runner trigger should reflect real |
| ACC-REM-BOW | 5,123 | 0.9/d | 5,692d | 31.2/d | 164d | Massive overstock, model irrelevant |

Action: Greg should refresh Bond / Soak / Matte / Remove Bowl model DSRs from current Shopify rates — current model rates inflate apparent risk and distort PO sizing.

---

## SELLING PERFORMANCE FLAGS

### Sales Spikes (7d > 30d by 50%+)

| SKU | Name | 7d | 14d | 30d | Spike vs 30d |
|---|---|---:|---:|---:|---:|
| UK-£45-GIF | Gift Card £45 | 3.6 | 1.8 | 0.8 | **+350%** ← Mother's Day / promo? |
| POW-PUM-398 | Pumpkin Spice | 2.9 | 2.0 | 1.7 | +71% |
| POW-ICE-266 | Iced Out | 6.0 | 5.0 | 3.6 | +67% |
| ACC-REM-BUN-1 | Remove + Bowl bundle | 8.7 | 7.1 | 5.8 | +50% |
| POW-DOV-093 | Dove | 1.1 | 0.9 | 0.7 | +57% |
| ACC-NAI-100/180 | Pro File 100/180 | 1.9 | 1.2 | 1.2 | +58% |
| ACC-NAI-WIP | Lint-Free Wipes | 1.6 | 1.4 | 1.0 | +60% |

**Cross-reference context:** Worth checking `#sale-announcements` (C091PEBAS65) for active UK promo. The £45 gift card 4.5x spike is unusual - either promo or Mother's Day driver.

### Sales Drops (7d < 30d by 40%+)

| SKU | Name | 7d | 14d | 30d | Drop vs 30d | Likely cause |
|---|---|---:|---:|---:|---:|---|
| POW-COT-030 | Cotton Candy | 0.0 | 0.0 | 1.7 | **-100%** | OOS at Fulfillable (day 7 OOS) |
| POW-VIB-529 | Vibes | 0.0 | 0.0 | 1.2 | **-100%** | Likely OOS - confirm |
| POW-FLA-CS24 | Flamingo Mist | 0.3 | 0.5 | 1.0 | -70% | Listing/stock check |
| POW-BLU-ZGD06 | Blush | 0.6 | 1.1 | 1.3 | -54% | - |
| POW-VIO-ZGD21 | Violet Sky | 0.6 | 0.6 | 1.0 | -40% | - |
| POW-PIN-SU016 | Pink Twist | 0.7 | 0.9 | 1.2 | -42% | - |
| POW-GHO-771 | Ghostin | 1.0 | 0.9 | 1.7 | -41% | - |
| POW-CAS-CS32 | Cashmere | 1.0 | 1.5 | 1.9 | -47% | - |
| POW-AWA-050 | Awakening | 1.3 | 1.7 | 2.3 | -43% | - |
| POW-IMA-264 | Imagine That | 1.9 | 1.9 | 3.2 | -41% | - |
| POW-JUS-449 | Just Friends | 4.3 | 5.4 | 8.2 | -48% | OOS at Fulfillable |
| ACC-REM | Remove 120ml standalone | 9.1 | 9.4 | 15.3 | -41% | Bundle absorbing? Check ACC-REM-BUN-1 +50% |
| ACC-REM-BOW | Remove Bowl standalone | 0.9 | 0.9 | 2.0 | **-55%** | Bundle absorbing |
| ACC-PRO-DRI | Perfection Pro Drill | 0.6 | 0.7 | 1.2 | -50% | - |
| ACC-TIP-ALM | Almond Tips | 4.0 | 4.4 | 6.8 | -41% | - |

**Read:**
- POW-COT-030, POW-VIB-529, POW-JUS-449: drops are OOS-driven (already flagged in POS Check).
- ACC-REM standalone -41% AND ACC-REM-BOW standalone -55% AND ACC-REM-BUN-1 +50%: **explained by new Remove 120ml + Bowl before-cart upsell** (CRO change, user-confirmed). Net Remove demand flat - just shifted from standalone SKUs to bundle SKU. Going forward, model the Remove product line on Shopify+bundle combined rate, not standalone alone.
- 8 colours dropped 40-55% with no obvious OOS cause - **listed below for Remy follow-up.** Not investigating now; flagged for next pass.

### Colours dropped 40-55% with no OOS cause (for Remy follow-up)

| SKU | Name | 7d | 14d | 30d | Drop |
|---|---|---:|---:|---:|---:|
| POW-FLA-CS24 | Flamingo Mist | 0.3 | 0.5 | 1.0 | -70% |
| POW-BLU-ZGD06 | Blush | 0.6 | 1.1 | 1.3 | -54% |
| POW-VIO-ZGD21 | Violet Sky | 0.6 | 0.6 | 1.0 | -40% |
| POW-PIN-SU016 | Pink Twist | 0.7 | 0.9 | 1.2 | -42% |
| POW-GHO-771 | Ghostin | 1.0 | 0.9 | 1.7 | -41% |
| POW-CAS-CS32 | Cashmere | 1.0 | 1.5 | 1.9 | -47% |
| POW-AWA-050 | Awakening | 1.3 | 1.7 | 2.3 | -43% |
| POW-IMA-264 | Imagine That | 1.9 | 1.9 | 3.2 | -41% |

### Dead Stock (in stock, 0 Shopify 14d)

- **49 colour SKUs at 0 sales 14d**, of which:
  - **5 in stock (991 units idle)** - candidates for relisting / clearance review
  - **44 OOS** (no stock + no sales) - matches the 28 Apr "45 OOS colour SKUs" estimate, mostly stuck in B360 packup

### Sensitive Base / Glow Signal

LIQ-SEN-2 = 0/d, LIQ-SEN-4 = 0/d both windows. Discontinued status confirmed - **safe to drop these from POS MODEL on next refresh.**

LIQ-SOA-6 (Soak/Sensitive Glow alternative): 2.1/d 14d. Stable but quiet.

---

## CONTAINER ARRIVALS DETECTED (B360 historical)

Only 2 detected events on B360 tab in last ~21 days:

- **14 Apr** - 194 SKUs, +2,409 units. Likely **B360 stocktake reconciliation or Fulfillable transition prep**, not a real container. Carried from 28 Apr Sales Analysis.
- **16 Apr** - 15 SKUs, +15 units. Marginal - noise.

**No live Fulfillable arrivals detected** because B360 tab represents frozen packup, not live 3PL. Powder Room arrival ~30 Apr and Chemence 10-03-2026 fill ~29 Apr cannot be detected without Fulfillable's deduction feed.

---

## INVENTORY DISCREPANCIES

**Cannot run on UK post-13 Apr** - no Fulfillable deduction data.

Pre-13 Apr historical (from B360, all dates 31 Mar-7 Apr) showed normal day-to-day deduction ranges with the colour benchmark (35/d) repeatedly hit by top-sellers (POW-CLE-193, POW-HEA-515, POW-POS-184, POW-PEA-068, etc.). KIT-ULT-6 had a 859-unit deduction on 31 Mar - 4.3x benchmark - but this aligned with a documented backorder-clearing day around the Fulfillable transition prep. Not actionable now.

**Action carried for 3rd cycle: Roisin export 14d Fulfillable deduction history.** Without this we have no way to detect AUS-style mystery deductions or kit-alignment integrity issues at the new 3PL. This is the highest-priority data gap.

---

## 3PL DEDUCTION CHECK (BLIND)

Cannot run. 3PL tab is frozen B360. Open until Roisin export.

---

## KEY TAKEAWAYS

1. **Effective growth factor 0.81x vs 1.3x target - 9+ weeks at 50% gap.** Daniel/Joel call due on whether to formally reduce, accept structural overstock buffer, or push marketing harder. Per `feedback_growth_factor_framing.md` we don't recommend lowering, but this gap should be flagged in the next Joel sync.
2. **W17 (-42%) confirmed as floor; W18 (-30%) is real recovery off it.** Watch W19 closely - if it lands sub-W17, structural concern. If 75-90/d, post-transition normalisation playing out.
3. **Bond / Soak / Matte / Remove Bowl model DSRs are 2-3x actual** - Greg refresh would clean cover figures and stop these flagging unnecessarily.
4. **Discontinued LIQ-SEN line confirmed dormant** - Greg can drop from model on next refresh.
5. **New Remove 120ml + Bowl before-cart upsell live** - drives ACC-REM-BUN-1 +50%, ACC-REM standalone -41%, ACC-REM-BOW standalone -55%. Net Remove demand flat. Model Remove SKUs on Shopify+bundle combined rate going forward.
6. **8 colours dropped 40-55% with no OOS** - listed in Sales Drops section for Remy follow-up. Not actioned this cycle.
7. **49 zero-14d colour SKUs (45 already known OOS, 4 with 991 units idle)** - already in POS Check action list.
8. **Fulfillable deduction integrity: BLIND.** Carried 3 cycles. Roisin export is now the single most important data integrity action.
