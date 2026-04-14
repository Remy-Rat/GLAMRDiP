# SALES DATA ANALYSIS — AUS — 14 Apr 2026

## DATA FRESHNESS

- **Shopify:** 13 Apr 2026 (1d ago — standard +1 lag)
- **3PL (AUS 3GPL):** 14 Apr 2026 (today)
- **Growth factor:** 1.3x
- **POS MODEL base:** 147 kits/day → scaled: 191.1 kits/day

---

## DSR: MODEL vs REALITY

### Kits

| SKU | Product | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap vs Model (14d) |
|---|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | Starter | 44.2/d | 38.9 | 35.3 | 33.2 | **-20%** |
| KIT-COM-4 | Complete | 101.4/d | 68.1 | 60.5 | 63.3 | **-40%** |
| KIT-ULT-6 | Ultimate | 45.5/d | 25.3 | 25.6 | 28.4 | **-44%** |
| **TOTAL** | | **191.1/d** | **132.3** | **121.4** | **124.9** | **-36%** |

**Growth factor reality check:**
- Actual 14d kit DSR: 121.4/day
- Actual growth factor: **0.83x** (vs model 1.3x)
- Recommended growth factor (actual + 10% buffer): **0.91x**
- **Selling 36.5% below the 1.3x scaled target**

The model is overforecasting demand by ~70 kits/day. This has been the pattern since Feb — the 1.3x growth factor hasn't been justified by actual selling. At 0.83x actual, the base DSR (147/day) is more realistic than the scaled target (191/day).

### Kit Mix

| Kit | Model Base | Model % | Actual 14d | Actual % | Gap |
|---|---:|---:|---:|---:|---:|
| Starter | 34 | 23% | 35.3 | 29% | +4% (over-indexed) |
| Complete | 78 | 53% | 60.5 | 50% | -3% |
| Ultimate | 35 | 24% | 25.6 | 21% | -3% |

- Starter is the strongest performer relative to model — only -20% vs model scaled DSR, and slightly above model base (35.3 vs 34).
- Complete and Ultimate both selling ~40-44% below scaled model.

### Heal (Kit-Adjusted)

| SKU | Model DSR | Standalone 7d | Standalone 14d | Kit-Adj 7d | Kit-Adj 14d | Gap |
|---|---:|---:|---:|---:|---:|---:|
| LIQ-HEA-5 | 184.6/d | 2.7 | 2.7 | 135.0 | 124.1 | **-33%** |

- Kit-adjusted DSR tracks kit selling: 121.4 kits + 2.7 standalone = 124.1/day
- POS MODEL assumes 184.6/day — overstated by ~50 units/day
- **At 124.1/day actual, Heal has 90d cover (vs 61d at model rate)**

### Liquids (Standalone — Pre-packed in kits from CN)

| SKU | Product | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap (14d) |
|---|---|---:|---:|---:|---:|---:|
| LIQ-BAS-2 | Base | 53.3/d | 3.6 | 16.6 | 29.2 | **-69%** |
| LIQ-SEA-3 | Seal | 44.2/d | 12.4 | 18.3 | 24.4 | -59% |
| LIQ-GLO-4 | Glow | 26.0/d | 9.9 | 14.4 | 17.5 | -45% |
| LIQ-BON-1 | Bond | 16.9/d | 6.0 | 7.1 | 8.9 | -58% |
| LIQ-SEN-2 | Low Odour Base | 9.1/d | 1.0 | 0.5 | 2.0 | -95% |
| LIQ-SEN-4 | Low Odour Glow | 7.8/d | 0.9 | 0.4 | 2.6 | -95% |
| LIQ-MAT-4 | Matte | 10.4/d | 6.0 | 5.4 | 6.0 | -48% |
| LIQ-SOA-6 | Soak | 13.0/d | 6.9 | 6.1 | 6.1 | -53% |

Key observations:
- **Base 7d (3.6) dropped 88% from 30d (29.2).** Likely demand suppression from approaching OOS — only 784 units on hand. Customers may be seeing "low stock" or website may have pulled it.
- **All liquids are massively below model DSR.** The POS MODEL DSR is manually calculated from monthly sales — it appears to be based on a higher-demand period. Every liquid is 45-95% below model.
- **Sensitive Base and Sensitive Glow at near-zero 14d sales** (0.5/d and 0.4/d). Low Odour Glow was confirmed OOS by Katrina on 31 Mar.

### Remove Products (Standalone)

| SKU | Product | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap (14d) |
|---|---|---:|---:|---:|---:|---:|
| ACC-REM | Remove 120ml | 33.8/d | 13.4 | 13.1 | 12.1 | -61% |
| ACC-REM-500 | Remove 500ml | 98.8/d | 30.4 | 32.0 | 35.2 | -68% |
| ACC-REM-BOW | Remove Bowl | 75.4/d | 4.0 | 4.1 | 4.8 | -95% |

- **ACC-REM-500 model DSR (98.8/d) is wildly overstated.** Shopify shows 32/day. The model DSR is derived from G3PL stock / days cover — but 3PL deductions include bundle consumption (ACC-REM-BUN-2 triggers a 500ml + Bowl deduction). The model is reading 3PL deductions, not Shopify demand.
- **ACC-REM-BOW same issue** — model shows 75.4/d but Shopify only 4.1/d. Most Bowl consumption comes via bundles (ACC-REM-BUN-1 and ACC-REM-BUN-2), not standalone sales.

### Top 20 Colours (by 14d Shopify volume)

| SKU | Colour | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap (14d) |
|---|---|---:|---:|---:|---:|---:|
| POW-CLE-193 | Clear | 65.0/d | 51.6 | 54.1 | 53.0 | -17% |
| POW-HEA-515 | Heaven | 57.2/d | 43.6 | 40.4 | 42.7 | -29% |
| POW-PIL-194 | Pillow Talk | 40.3/d | 37.7 | 37.1 | 38.4 | -8% |
| POW-POS-184 | Positivi-Tea | 44.2/d | 24.7 | 30.1 | 37.1 | -32% |
| POW-SWE-001 | Sweet Tooth | 31.2/d | 30.4 | 26.9 | 25.9 | -14% |
| POW-MON-005 | Moon Magic | 28.6/d | 25.4 | 23.8 | 23.5 | -17% |
| POW-OAK-283 | Oak | 18.2/d | 24.0 | 20.9 | 19.8 | **+15%** |
| POW-BLA-384 | Blackout | 28.6/d | 21.9 | 20.4 | 22.2 | -29% |
| POW-CRE-217 | Creme Brulee | 23.4/d | 22.0 | 20.3 | 19.3 | -13% |
| POW-BOU-222 | Boujee | 23.4/d | 21.6 | 19.6 | 19.4 | -16% |
| POW-DUS-346 | Dusk | 22.1/d | 20.1 | 18.1 | 18.8 | -18% |
| POW-TRA-452 | Train-Wreck | 24.7/d | 18.6 | 17.4 | 18.0 | -29% |
| POW-CRU-328 | Crushin Hard | 22.1/d | 21.9 | 16.5 | 16.0 | -25% |
| POW-SLO-192 | Slow Burn | 23.4/d | 17.1 | 16.1 | 15.3 | -31% |
| POW-OUR-772 | Our Secret | 22.1/d | 14.3 | 16.0 | 16.0 | -28% |
| POW-BAR-198 | Bare Necessity | 24.7/d | 14.0 | 15.3 | 15.8 | -38% |
| POW-FAI-308 | Fairytale | 22.1/d | 15.1 | 15.3 | 15.2 | -31% |
| POW-FAL-431 | Fall | 19.5/d | 15.6 | 15.3 | 15.8 | -22% |
| POW-GOO-208 | Good Morning | 26.0/d | 16.0 | 15.1 | 16.9 | -42% |
| POW-YOU-256 | Yours Truly | 22.1/d | 16.0 | 14.9 | 14.3 | -32% |

- **Clear (54.1/day)** firmly #1. Now fully stocked at 39,068 after PO 5/6 closure. 
- **Pillow Talk (37.1/day)** is the closest to model at -8%. Consistent performer.
- **Oak (20.9/day) overperforming** model at +15%. 7d trending up to 24.0.
- Total colour DSR: 1,041/day (14d). Top 20 colours account for ~47% of total colour demand.

---

## WEEKLY KIT TREND (8 weeks)

| Week | Dates | Daily Rate | vs Model (191.1/d) | Trend |
|---|---|---:|---:|---|
| W8 | 16-22 Feb | 114.1/d | -40% | Mid-transition chaos |
| W9 | 23 Feb-1 Mar | 106.8/d | -44% | Trough approaching |
| W10 | 2-8 Mar | 95.1/d | **-50%** | Trough (STA+ULT OOS) |
| W11 | 9-15 Mar | 105.3/d | -45% | STA OOS, slight recovery |
| W12 | 16-22 Mar | 130.1/d | -32% | STA restocked, container arriving |
| W13 | 23-29 Mar | 128.4/d | -33% | Steady |
| W14 | 30 Mar-5 Apr | 105.4/d | -45% | Easter break (G3PL closed 3-7 Apr) |
| W15 | 6-12 Apr | 135.3/d | **-29%** | Best week — PO 5/6 stock clearing |

**Trajectory:** Clear V-shaped recovery from the W10 trough. W15 (135.3/day) is the best since before the B360 transition. Easter (W14) dipped but bounced back immediately. The pattern is: performance improves when stock is available. The -29% gap is structural (demand vs model), not a fulfilment issue.

**3 consecutive declining weeks?** No — W14 dipped but recovered in W15. No sustained decline.

**>30% above 4-week average (promo spike)?** No. Selling is flat-to-recovering.

---

## SHOPIFY vs 3PL DEDUCTION CHECK

Container arrival days excluded: 10 Apr, 14 Apr.

### Kits — ALIGNED

| SKU | 3PL Ded/d | Shopify/d | Gap | Status |
|---|---:|---:|---:|---|
| KIT-STA-2 | 38.2 | 35.3 | +2.9 | ALIGNED |
| KIT-COM-4 | 65.0 | 60.5 | +4.5 | ALIGNED |
| KIT-ULT-6 | 26.0 | 25.6 | +0.4 | ALIGNED |

Kit deduction logic is working correctly at G3PL. Small positive gaps (~3-5 units) are normal — Shopify data has a 1-day lag.

### Liquids — Bundle Effect

| SKU | 3PL Ded/d | Shopify/d | Gap | Explanation |
|---|---:|---:|---:|---|
| LIQ-HEA-5 | 141.5 | 2.7 | +138.8 | Expected — kit-adjusted (1 Heal per kit) |
| ACC-REM-500 | 64.9 | 32.0 | +32.9 | Bundle effect (ACC-REM-BUN-2) |
| ACC-REM | 25.3 | 13.1 | +12.2 | Bundle effect (ACC-REM-BUN-1) |
| LIQ-GLO-4 | 22.5 | 14.4 | +8.1 | LIQ-SET bundle (~4/d) + minor gap |
| LIQ-SEA-3 | 24.4 | 18.3 | +6.1 | LIQ-SET bundle (~4/d) |
| LIQ-BAS-2 | 21.6 | 16.6 | +5.1 | LIQ-SET bundle (~4/d) |
| LIQ-BON-1 | 8.2 | 7.1 | +1.2 | ALIGNED |

**Key finding:** The Remove 500ml and Remove Bowl "overdeduction" is explained by **ACC-REM-BUN-2 bundle sales** (~33/day on Shopify as bundles). When a customer buys the bundle, 3PL deducts both ACC-REM-500 and ACC-REM-BOW individually. Same logic for 120ml bundles. This means:
- **ACC-REM-500 model DSR of 98.8/day is wrong** — it's based on 3PL deductions (including bundles), not standalone demand. Actual Shopify demand is ~32/day standalone + ~33/day in bundles = ~65/day total demand on 500ml stock.
- **ACC-REM-BOW model DSR of 75.4/day is wrong** — actual standalone is 4.1/day + ~33/day in bundles = ~37/day total demand.

**LIQ-SET (Liquids Set)** selling 4.2/day on Shopify (7d: 6.3, spiking). Each set deducts 1x of all 6 liquids. This accounts for ~4 units/day of the Base, Glow, Seal, Bond, Soak gaps.

---

## CONTAINER ARRIVALS DETECTED

| Date      | SKUs Increased | Total Units | Likely Source                                      |
| --------- | -------------: | ----------: | -------------------------------------------------- |
| 25 Feb    |            164 |     +51,112 | AUS 21022026 (3PL transition container)            |
| 26 Feb    |            185 |      +2,385 | Continued check-in from above                      |
| 5 Mar     |             26 |     +16,810 | Small shipment (Mani Mats, stickers, misc)         |
| 27-28 Mar |          98+95 |    +164,229 | AUS 07032026 (major container) — 2-day check-in    |
| 10 Apr    |            118 |    +128,553 | B360 Packup + OP fill delivery (PO 10)             |
| 14 Apr    |            198 |    +192,196 | PO 5 & 6 closure — final B360 + remaining check-in |

The 14 Apr event is the largest — 192k units across 198 SKUs. This is the PO 5 & 6 closure that we've been waiting for since the B360 transition.

---

## INVENTORY DISCREPANCY DETECTION

### Red Flag Deductions (single day exceeding benchmark)

Most red flags cluster around two periods:
1. **20-26 Mar** — heavy fulfilment catch-up after AUS 07032026 container arrival and kit swap activity (Remy swapped 60+ Ultimate orders to Complete on 27 Mar)
2. **6 Apr** — Easter weekend catch-up (G3PL closed 3-7 Apr, Sunday batch processing)

| Date | SKU | Deduction | Benchmark | Likely Cause |
|---|---|---:|---:|---|
| 26 Mar | KIT-COM-4 | 336 | 200 | Kit swap (ULT→COM) + backorder clearing |
| 25 Mar | KIT-COM-4 | 325 | 200 | Same — high-volume COM fulfilment |
| 6 Apr | ACC-REM-500 | 182 | 100 | Easter catch-up batch |
| 23 Mar | ACC-REM-500 | 170 | 100 | Post-container clearing |
| 23 Mar | LIQ-BAS-2 | 169 | 90 | Post-container clearing |
| 21 Mar | LIQ-BAS-2 | 151 | 90 | Post-container clearing |

**POW-BRA-337 (Brain Freeze): 288 on 26 Mar** — far above the 35 colour benchmark. Also 80 on 25 Mar. Total of 368 in 2 days. This looks like a stock adjustment or reconciliation rather than genuine sales. Worth confirming with G3PL.

**POW-CLE-193 (Clear):** Multiple high days (117-190) through Mar and into Apr. At 54.1/day actual DSR, Clear is legitimately the highest-velocity colour. The 190 on 6 Apr (Easter catch-up) is 3.5x daily rate — elevated but plausible for a multi-day batch.

### Dead Stock (colours with stock > 0, zero Shopify sales in 14d)

- **25 colours, 6,180 total units**
- Mostly thermal/colour-change (W-prefix: Thermo, Pulse, Gradient, Mercurial, Tidal Turn), seasonal (Yule Gold, Star Pine), and recently unlaunched
- **POW-RUS-624 (Rustle, 827 units):** Has a model DSR (3.9/d) but 0 Shopify sales. May be unlisted or OOS on website despite having 3PL stock.
- **POW-BLU-ZGD22 (Blue Moon, 519 units):** Confirmed OOS in 7 Apr summary. Now has stock at G3PL (from B360 packup?) but may not be relisted on Shopify yet.

---

## SELLING PERFORMANCE FLAGS

### Sales Spikes (7d > 30d by 50%+)

| SKU | Product | 7d DSR | 14d DSR | 30d DSR | Spike |
|---|---|---:|---:|---:|---:|
| LIQ-SET | Liquids Set | 6.3 | 4.2 | 3.4 | +83% |
| POW-DAY-025 | Daydream | 12.3 | 10.4 | 7.6 | +62% |
| POW-SUG-545 | Sugar Rush | 2.6 | 2.1 | 1.6 | +61% |
| POW-MAR-009 | Marshmallow | 10.3 | 8.4 | 6.8 | +52% |

- **LIQ-SET spike (+83%)** — this explains the extra liquid deductions at 3PL. At 6.3/day, each sale deducts 1x of all 6 liquids. Monitor — if sustained, increases liquid cover consumption by ~6/day per SKU.
- Daydream and Marshmallow trending up — check if marketing is pushing these.

### Sales Drops (7d < 30d by 40%+)

| SKU | Product | 7d DSR | 14d DSR | 30d DSR | Drop | Likely Cause |
|---|---|---:|---:|---:|---:|---|
| POW-BLU-ZGD22 | Blue Moon | 0.0 | 0.0 | 3.4 | -100% | OOS on website |
| POW-VIO-11932 | Violet Flush | 0.1 | 1.9 | 4.0 | -96% | Low stock (589 units) |
| POW-BUB-516 | Bubbly | 0.7 | 0.8 | 7.0 | -90% | Possible delisting? |
| LIQ-BAS-2 | Base | 3.6 | 16.6 | 29.2 | -88% | Approaching OOS (784 units) |
| POW-GOD-017 | Goddess | 2.6 | 6.9 | 19.6 | -87% | Possible OOS/delist |
| LIQ-SEN-4 | Low Odour Glow | 0.9 | 0.4 | 2.6 | -67% | OOS confirmed 31 Mar |
| LIQ-SEN-2 | Low Odour Base | 1.0 | 0.5 | 2.0 | -49% | Low stock (135 units) |
| LIQ-SEA-3 | Seal | 12.4 | 18.3 | 24.4 | -49% | Moderating from spike |

- **Base (-88%)** — demand crashing as stock approaches zero. This confirms the POS Check finding: Base will stock out ~late April.
- **Goddess (-87%)** — went from 19.6/day (30d) to 2.6/day (7d). Large colour with 3,495 units on hand. Not a stock issue — check if it's been removed from listings or marketing shifted.
- **Bubbly (-90%)** — 2,952 units on hand but selling collapsed. Same question — delisted?
- **Blue Moon (-100%)** — confirmed OOS on website. Has stock at G3PL post PO 5/6. Needs relisting.

### Sensitive Base Signal

| Product | 14d DSR | Share |
|---|---:|---:|
| Base (standalone) | 16.6/d | 97% |
| Sensitive Base | 0.5/d | 3% |
| **Total** | **17.1/d** | |

Model assumes ~70/30 split. Reality is 97/3. Sensitive Base is either:
- Extremely niche (genuine low demand)
- OOS on website (only 135 units at G3PL)
- Under-marketed relative to standard Base

At 0.5/day actual, the 135 units = 270d cover. Not a stock risk — just a demand observation.

---

## KEY TAKEAWAYS

1. **Growth factor needs recalibrating.** 1.3x model predicts 191/day but actual is 121/day (0.83x). Recommended: 0.91x (actual + 10% buffer). Every ordering decision is currently based on demand that's 36% higher than reality. This inflates stock-out urgency and could lead to over-ordering.

2. **Kit performance improving.** W15 (135.3/day) is the best week since before the B360 transition. Starter closest to model at -20%. Recovery tracks stock availability — when kits are in stock, they sell.

3. **Base demand collapsing as OOS approaches.** 7d DSR (3.6) is 88% below 30d (29.2). This is a demand suppression signal — customers seeing "low stock" or "sold out" and not purchasing. POS Check confirms stockout ~late April with no local fill option.

4. **LIQ-SET bundle driving 3PL deduction gaps.** Spiking at 6.3/day. Each sale deducts all 6 liquids. This inflates the model DSR for liquids if Greg is using 3PL deductions to set POS MODEL rates. Model DSR for Remove 500ml (98.8) and Remove Bowl (75.4) are clearly overstated — actual demand is 32/d and 4.1/d respectively.

5. **3 colours need website attention:** Blue Moon (OOS but has stock), Goddess (demand collapsed 87% — delist or marketing?), Bubbly (demand collapsed 90%).

6. **POW-BRA-337 (Brain Freeze) needs investigation.** 368 units deducted on 25-26 Mar — 10x the daily benchmark. Stock adjustment or genuine? Confirm with G3PL.
