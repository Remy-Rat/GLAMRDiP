# Sales Data Analysis — CA — 10 Jun 2026

## Data Freshness
- Shopify latest date: **2026-06-09** (+1 day lag, normal)
- 3PL (B360) last valid: **2026-06-10**
- Growth factor: **2.0x** (kit base 69/d → scaled 138/d)
- Kit DSR base from POS MODEL: STA 9 / COM 47 / ULT 13 = 69

## DSR — Model vs Actual

### Kits
| SKU | Model DSR (2x) | Shop 7d | Shop 14d | Shop 30d | 3PL 14d/d | Gap vs Model |
|---|---|---|---|---|---|---|
| KIT-STA-2 | 18.0 | 7.6 | 8.9 | 11.8 | 9.2 | **-51% (30d)** |
| KIT-COM-4 | 94.0 | 59.0 | 64.6 | 78.3 | 64.8 | **-17% (30d)** |
| KIT-ULT-6 | 26.0 | 17.9 | 20.7 | 23.4 | 21.1 | **-10% (30d)** |
| **Total** | **138.0** | **84.5** | **94.2** | **113.5** | **95.1** | **-18% (30d), -32% (14d), -39% (7d)** |

**Growth factor health:** Actual 14d kit total / model base = 94.2 / 69 = **1.37x equivalent** (vs aspirational 2.0x). Gap **-32%** — sustained for 4+ weeks. Per [[growth-factor-framing]] hold 2x for sizing; flag overstock risk on future containers.

**Kit mix 14d:** STA 9% / COM 69% / ULT 22%. Model base mix: STA 13% / COM 68% / ULT 19%. Mix slightly under-indexes STA, slightly over-indexes ULT — consistent with prior reviews. No substitution issue.

### Heal (kit-adjusted)
| SKU | Model DSR | Shop 7d standalone | Shop 30d standalone | Kit-adj 14d (Shop+kits) | 3PL 14d/d |
|---|---|---|---|---|---|
| LIQ-HEA-5 | 142 | 0.4 | 0.7 | 95.0 | 97.2 |

3PL deduction 97.2/d matches kit-adj Shopify 95.0/d ±2 — kit-adjusted deduction working correctly. Model 142/d is the 2x scaled aspiration; reality 95-97/d. Stock 4,224 → cover **43d at actual**.

### Other liquids (standalone — pre-packed in kits from China)
| SKU | Model DSR (2x) | Shop 7d | Shop 14d | Shop 30d | Gap vs Model |
|---|---|---|---|---|---|
| LIQ-BAS-2 (Base) | 14 | 7.1 | 7.6 | 7.7 | -45% |
| LIQ-GLO-4 (Glow) | 8 | 4.7 | 3.8 | 3.7 | -54% |
| LIQ-SEA-3 (Seal) | 12 | 5.0 | 5.2 | 5.6 | -53% |
| LIQ-BON-1 (Bond) | 6 | 2.1 | 1.9 | 2.1 | -65% |
| LIQ-MAT-4 (Matte) | 6 | 2.7 | 2.6 | 2.9 | -52% |
| LIQ-SOA-6 (Soak) | 4 | 2.0 | 1.6 | 1.7 | -58% |
| LIQ-SEN-2 (Sens Base) | 8 | 3.4 | 2.9 | 3.5 | -56% |
| LIQ-SEN-4 (Sens Glow) | 6 | 2.1 | 1.9 | 2.3 | -62% |

All CA liquid POS MODEL DSRs are 45-65% above actual standalone selling. Per 4 Jun recap, Greg refresh outstanding. Operational impact low (cover at any rate is 75-300d) but model is misleading.

### Remove & accessories
| SKU | Model DSR | Shop 7d standalone | Shop 30d | Shop 7d bundle | Total demand 7d | 3PL 14d/d |
|---|---|---|---|---|---|---|
| ACC-REM-500 | 120 | 25.4 | 78.8 | 5.3 (BUN-2) | **30.7** | 60.1 |
| ACC-REM (120ml) | 10 | 2.1 | 2.1 | 36.7 (BUN-1) | **38.8** | 24.2 |
| ACC-REM-BOW | 30 | 3.0 | 2.5 | 41.0+ (BUN-1+2) | **44+** | 28.1 |

- ACC-REM-500: model 120 over-states by 4x even at peak 3PL. Reality is the upsell channel pulling 60/d (dropping as OOS approaches; was 25.4/d Shopify 7d).
- ACC-REM: standalone almost nothing; bundle BUN-1 is the volume. 3PL 24/d aligns with bundle+std ≈ 39/d (some seasonal smoothing). Healthy.
- ACC-REM-BOW: model 30/d understates reality (~44/d via bundles). 3PL deduction 28/d aligned with model but bundle volume is real. Cover 172d at 3PL rate, 110d at total bundle math. Still safe with 8,000 inbound 21062026.

### Tips
| SKU | Model DSR | Shop 7d | Shop 30d | 3PL 14d/d | Notes |
|---|---|---|---|---|---|
| ACC-TIP-BAL (Ballerina) | 4 | 0.3 | 0.4 | 65.3 | **3PL ≫ Shopify** — current offer tip; deduction rate captures attach pull, Shopify only standalone |
| ACC-TIP-ALM (Almond) | 146 | 4.0 | 3.4 | 31.1 | Model 146 broken (per 4 Jun recap, should be ~5). 3PL captures historical kit-attach pre-Daniel 4 Jun switch-off plan |
| ACC-TIP-COF (Coffin) | 2 | 0.1 | 0.3 | 122.0 | Previous offer pre-27 May Ballerina swap. 14d avg captures pre-swap days; current rate should be near zero |
| ACC-TIP-SQU (Square) | 4 | 1.6 | 1.3 | 1.9 | Off-offer; aligned |
| ACC-TIP-STI (Stiletto) | 2 | 0.1 | 0.2 | 1.0 | Off-offer; aligned |
| ACC-NAI-MAT (Mani Mat) | 0 | 0.0 | 0.4 | 0 (post-swap) | OOS since ~27 May; offer rotated |
| ACC-TRA-BAG (Travel Bag) | 0.2 | 0.0 | 0.0 | 77.3 | **3PL pulling fast** — already attaching even though Shopify shows zero standalone. Future offer earmark |

## Weekly Kit Trend

| Week | Dates | Daily rate | vs Model (138/d) | Notes |
|---|---|---|---|---|
| W16 | 13-19 Apr | 52.1 | -62% | Pre-recovery |
| W17 | 20-26 Apr | 46.1 | -67% | Trough |
| W18 | 27 Apr-3 May | 49.0 | -64% | — |
| W19 | 4-10 May | 77.3 | -44% | Scale uplift |
| W20 | 11-17 May | **151.9** | **+10%** | Peak — promo/offer-driven |
| W21 | 18-24 May | 118.6 | -14% | Reversal |
| W22 | 25-31 May | 103.4 | -25% | Confirmed normalisation |
| W23 | 1-7 Jun | **91.6** | **-34%** | Continued slide |
| W24 (partial) | 8-9 Jun | 73.5 (2d) | -47% | Very recent, 2-day window |

**Trajectory:** Three consecutive weeks of decline post-W20 peak (-14%, -25%, -34%). W24 partial (2 days only) at -47% is noisy but consistent with the slide. **No promo spike, no campaign change in Slack to explain the drop** — looks like real demand softening.

**Kit mix stable:** W23 vs prior weeks: STA stays 8-10%, COM 67-70%, ULT 20-23%. Consistent throughout.

## Realistic Days Cover (key items only)

| SKU | Stock | Cov @ Model | Cov @ Actual | Action threshold |
|---|---|---|---|---|
| KIT-STA-2 | 3,799 | 211d | 412d | Monitor |
| KIT-COM-4 | 5,580 | 59d | 86d | Comfortable |
| KIT-ULT-6 | 2,500 | 96d | 119d | Comfortable |
| LIQ-HEA-5 | 4,224 | 30d | 43d (kit-adj) | Safe — Swift fill arrives 23 Jun – 2 Jul |
| **ACC-REM-500** | **339** | **3d** | **6d** | **CRITICAL — OOS 16 Jun without upsell switch** |
| ACC-REM | 3,510 | 351d | 145d (total demand) | Comfortable; rate increases on upsell switch |
| ACC-REM-BOW | 4,831 | 161d | 172d | Comfortable |
| ACC-TIP-BAL | 422 | 105d (broken) | 6d | CRITICAL — current offer tip |
| ACC-TRA-BAG | 347 | 1,735d (broken) | 4d | CRITICAL — already burning |
| ACC-INS | 19,344 | 140d | 209d | Comfortable |
| ACC-LAB-CA | 23,821 | 109d | n/a (NaN) | Mixam +20k inbound; safe through Aug |

## Container Arrival Auto-Detection

Last 60d in 3PL data — no 8+ SKU simultaneous jumps detected for CA. Powder Room (24-03-2026) arrival was last container, checked in 25-26 Apr per previous reviews. Next arrival expected:
- Mixam 14-05-2026 ACC-LAB-CA reprint ~14-18 Jun
- Swift 14-05-2026 fill 23 Jun – 2 Jul
- CA 21062026 Lily vessel 1 Jul (sheet says 9 Jul — incorrect)

## Inventory Discrepancy Detection

### Red flags (last 14d)
30 total events. Top SKUs by frequency: POW-CLE-193 (16), POW-JUS-449 (9), ACC-NAI-MAT (3), ACC-REM-500 (2).

**No red flags in last 7 days** — POW-CLE-193 / POW-JUS-449 offer-pull period appears to have tapered post-W20. Last big spike POW-CLE-193 147/d on 2 Jun (vs 35 benchmark = 4.2x). Cooling but still elevated. ACC-NAI-MAT spikes all pre-27 May offer swap (explained).

### Cumulative gap test (3PL > Shopify by 30d)
- KIT-STA-2: 3PL 14d 9.2/d × 30 = 276 vs Shopify 30d × 30 = 354. Gap **-78** (3PL under-deducting, likely returns or paste lag). Within tolerance.
- KIT-COM-4: 3PL 64.8 × 30 = 1,944 vs Shopify 78.3 × 30 = 2,349. Gap **-405** (Shopify > 3PL). Same pattern — likely Shopify 30d window catching post-W20 peak the 3PL 14d doesn't.
- KIT-ULT-6: 3PL 21.1 × 30 = 633 vs Shopify 23.4 × 30 = 702. Gap **-69**. Tight.

3PL deductions are running *slower* than Shopify 30d sales — consistent with the kit decline trend (recent days lighter than 30d avg). Data integrity clean.

### Stock gains / component transfers
- No component drops to zero (HEA-EMP, ACC-RE5-BOT etc) — Swift fill cycle hasn't pulled fresh components yet.
- POS MODEL shows Swift fill `Ordering` status — production runs from local Swift stock, not a fresh transfer this cycle.

## 3PL Deduction Check (kit alignment)

| SKU | Shop 7d/d | 3PL 14d/d | Gap | Status |
|---|---|---|---|---|
| KIT-STA-2 | 7.6 | 9.2 | +1.6 | aligned |
| KIT-COM-4 | 59.0 | 64.8 | +5.8 | aligned (3PL slightly faster, normal) |
| KIT-ULT-6 | 17.9 | 21.1 | +3.2 | aligned |

Kit deduction integrity clean. Within ±5/d per kit. No 3PL data anomalies.

## Selling Performance Flags

### Sales drops (7d significantly below 30d)
| SKU | 7d | 14d | 30d | Drop vs 30d | Notes |
|---|---|---|---|---|---|
| ACC-REM-500 | 25.4 | 53.7 | 78.8 | **-68%** | Going OOS — demand suppressed by stock-out |
| POW-DRE-D08 (Dreamer) | 0.9 | 1.9 | 2.6 | -65% | Was breakout 4 Jun (+16-21% accel) — cooling |
| POW-BLO-D07 (Blowout) | 0.7 | 1.8 | 2.6 | -73% | Same cohort cooling |
| POW-ANG-D09 (Angel) | 1.4 | 2.2 | 3.5 | -60% | Same cohort cooling |
| POW-DOM-657 | 2.0 | 2.9 | 4.4 | -55% | Watch |

The three D-suffix breakouts (Dreamer / Blowout / Angel Energy) flagged in last review have all reversed — back to pre-W20 baseline. Consistent with broader kit slowdown.

### Sales spikes (7d significantly above 30d)
**None at 50%+ threshold.** Even POW-SUG-545 (Sugar Rush — flagged in UK + CA last cycle) is stable: 7d 3.0 / 14d 2.9 / 30d 2.7. Not running.

### Overperformers vs model (>20% above model DSR)
- ACC-TRA-BAG: 3PL 77.3/d vs model 0.2/d. Currently attached to orders despite zero Shopify. Confirms it's the planned next offer (Daniel 4 Jun) — needs sizing decision.
- POW-CLE-193 + POW-JUS-449: model 35 benchmark; 3PL 14d avg ~120-140/d. Sustained 16+ day offer pull. Cooling but still elevated.

### Underperformers vs model (>40% below model DSR)
- All 8 standalone liquids (Base/Glow/Seal/Bond/Matte/Soak/Sens-2/Sens-4): 45-65% below model.
- LIQ-HEA-5 model 142 vs kit-adj actual 95 (-33%).
- KIT-STA-2 model 18 vs actual 9.2/d (-51%).
- ACC-TIP-ALM model 146 vs 3PL 31/d (-79%) — broken DSR per 4 Jun recap.
- ACC-NAI-MAT model 0 (post-swap reset already done).

**Greg refresh batch still owing:** all CA liquids 30-60% overstated, ACC-REM-500 120 → ~80, ACC-REM 10 → 2, ACC-REM-BOW 30 → 3 (standalone), ACC-TIP-ALM 146 → 5.

### Dead stock (colour POW-*, 14d zero Shopify)
22 SKUs with zero 14d Shopify sales:
- 11 CA legacy: POW-LIP-570, ROS-522, COB-G17, BAL-521, SEC-G15, VAN-F01, LIM-G13, MAP-564, POW-F17, GOL-565, AMB-572 (mostly UK/EU- variants or CA-POW- prefixed)
- 11 broader idle: POW-BEY-825, FES-006, HOL-022, REI-008, MIR-015, THE-W005, TID-W006, PUL-W035, JUB-L11, GLA-CS02, SUN-SU015, JUI-SU020, ALL-146, RED-165, GAR-656, BOR-355, SPI-144, SAF-149, INF-506, HOT-568

Listing audit candidates for Gav. Same cohort pattern as AUS/UK fade lists.

## Key Takeaways

1. **W23 confirms three-week kit slide post-W20 peak.** -14% → -25% → -34%. Even W24 partial (2 days) sits at -47%. No campaign change visible in #ca-inventory; this is genuine demand softening. Per [[growth-factor-framing]] hold 2x for ordering; treat ~95/d as operational reality. **Flag for next cycle: if W24 closes below 90/d, container sizing thesis on CA 30082026 (2x = 138/d, 40HQ) is exposed.**

2. **The three D-suffix breakouts flagged on 4 Jun have all reversed.** POW-DRE-D08 / POW-BLO-D07 / POW-ANG-D09 down 60-73% 7d vs 30d. Drop the "add to POS MODEL" recommendation from last cycle — the signal was a W20-era spike, not sustained.

3. **ACC-REM-500 demand collapsing as OOS approaches.** Shopify 7d 25.4 vs 30d 78.8 (-68%) — site is suppressing sales (likely "low stock" or auto out-of-stock). Pre-empts the upsell switch in a way. Validates that switching to 120ml + Bowl won't lose meaningful volume.

4. **ACC-TRA-BAG already burning 77/d at 3PL despite zero Shopify standalone.** It's being attached to orders right now — possibly via the gift card / Almond tip / colour offer mix. If Daniel formally switches it to the offer, demand jumps further. **Stock 347 / 4d cover, no inbound — size next CN PO accordingly.**

5. **Kit deduction integrity clean** (Shopify 7d total 84.5 vs 3PL 14d 95.1, gap explained by 30d trailing data). No 3PL anomalies. POW-CLE-193 + POW-JUS-449 offer-pull cooled; no red flags in last 7 days.

6. **Greg POS MODEL refresh outstanding** — 8 liquids 45-65% overstated, ACC-TIP-ALM at 146 needs reset to ~5, ACC-LAB-CA B360 deduction rule still NaN. Operational impact low (cover safe at any rate); model misleads daily-digest readers.
