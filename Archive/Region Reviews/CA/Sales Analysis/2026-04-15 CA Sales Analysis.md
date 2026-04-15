# SALES DATA ANALYSIS — CA — 15 Apr 2026

## DATA FRESHNESS

- **Shopify:** 13 Apr 2026 (2d ago)
- **3PL:** 15 Apr 2026 (today)
- **Growth factor:** 2.0x
- **POS MODEL base:** 80/d → scaled: 160/d
- **Actual 14d kit total:** 52.6/d (0.66x)

---

## DSR: MODEL vs REALITY

### Kits

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap 14d |
|---|---|---|---|---|---|
| KIT-STA-2 | 42.0 | 14.7 | 14.8 | 15.2 | -65% |
| KIT-COM-4 | 82.0 | 28.4 | 27.4 | 29.2 | -67% |
| KIT-ULT-6 | 36.0 | 10.6 | 10.4 | 12.1 | -71% |
| **TOTAL** | **160.0** | **53.7** | **52.6** | **56.5** | **-67%** |

**Growth factor reality check:**
- Model: 2.0x (160/d scaled target)
- Actual: 0.66x (52.6/d)
- **Recommended: 0.72x** (actual + 10% buffer)
- CA is selling 67% below the scaled target. This has been consistent for 8+ weeks.

**Kit mix (14d):**
- Starter: 28% (14.8/d) — model expects 26%
- Complete: 52% (27.4/d) — model expects 51%
- Ultimate: 20% (10.4/d) — model expects 23%

Mix is broadly in line. ULT slightly underperforming its share.

### Heal (kit-adjusted)

| | Model DSR | Standalone 7d | Standalone 14d | Kit-adj 7d | Kit-adj 14d | Gap |
|---|---|---|---|---|---|---|
| LIQ-HEA-5 | 170.0 | 1.7 | 1.6 | 55.4 | 54.2 | -68% |

Heal model DSR (170/d) is based on 2.0x growth. At actual kit rates + standalone: 54.2/d. **Overstated by 3.1x.**

### Liquids (standalone — pre-packed in kits from CN)

| SKU | Name | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap 14d |
|---|---|---|---|---|---|---|
| LIQ-BAS-2 | Base | 34.0 | 13.6 | 11.7 | 12.3 | -66% |
| LIQ-SEA-3 | Seal | 24.0 | 10.4 | 8.6 | 9.3 | -64% |
| LIQ-GLO-4 | Glow | 20.0 | 7.4 | 6.3 | 6.7 | -68% |
| LIQ-BON-1 | Bond | 16.0 | 3.9 | 3.6 | 4.2 | -78% |
| LIQ-MAT-4 | Matte | 14.0 | 4.4 | 4.6 | 5.3 | -67% |
| LIQ-SOA-6 | Soak | 16.0 | 4.6 | 4.0 | 3.9 | -75% |
| LIQ-SEN-2 | Sensitive Base | 8.0 | 5.7 | 4.9 | 5.0 | -39% |
| LIQ-SEN-4 | Sensitive Glow | 6.0 | 4.0 | 3.4 | 3.6 | -43% |

All liquids 40-78% below model. Sensitive products closest to model (-39% to -43%), suggesting the niche customer base is less affected by whatever's suppressing main demand.

Bond is the weakest (-78%). Soak also weak (-75%). Both are lower-profile products.

### Remove Products

| SKU | Name | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap 14d |
|---|---|---|---|---|---|---|
| ACC-REM | Remove 120ml | 62.0 | 25.9 | 25.1 | 17.0 | -60% |
| ACC-REM-500 | Remove 500ml | 0.0 | 0.0 | 0.0 | 12.3 | OOS |
| ACC-REM-BOW | Remove Bowl | 80.0 | 4.7 | 4.9 | 4.0 | -94% |

**ACC-REM (120ml) is trending UP** — 7d (25.9) > 14d (25.1) > 30d (17.0). This may be substitution from Remove 500ml being OOS. Customers buying 120ml instead.

**ACC-REM-500 has been OOS** — 30d shows 12.3/d (pre-OOS) but 7d and 14d are 0. Demand will bounce back once restocked (~18-20 Apr). Pre-OOS, this was a strong seller.

**ACC-REM-BOW model DSR (80/d) is wrong.** Actual 3PL deduction is 18.5/d (driven by both bundle SKUs: ACC-REM-BUN-1 = 120ml+Bowl, ACC-REM-BUN-2 = 500ml+Bowl). Shopify shows 4.9/d because Shopify only records the bundle SKU. Greg should set model DSR to ~20/d.

### Bundle Demand

| SKU | Name | 7d | 14d | 30d | Note |
|---|---|---|---|---|---|
| ACC-REM-BUN-1 | 120ml + Bowl | 11.7 | 12.1 | 7.5 | Trending UP (substitution from 500ml OOS?) |
| ACC-REM-BUN-2 | 500ml + Bowl | 0.0 | 0.0 | 7.5 | Dropped to 0 — Remove 500ml OOS |
| LIQ-SET | Liquids Set | 2.0 | 1.7 | 1.8 | Stable. Each sale deducts 1x of all 6 liquids at 3PL |

ACC-REM-BUN-1 spiking because customers can't buy the 500ml bundle. Once 500ml restocks, expect BUN-2 to resume at ~7.5/d and BUN-1 to drop back.

### Sensitive Base Signal

- Base (LIQ-BAS-2): 11.7/d (70%)
- Sensitive (LIQ-SEN-2): 4.9/d (30%)
- Total: 16.6/d
- Split matches the expected 70/30 model.

---

## WEEKLY KIT TREND

| Week | Dates | Days | Total | Daily Rate | vs Model (160/d) |
|---|---|---|---|---|---|
| W8 | 16-22 Feb | 7 | 535 | 76.4 | -52% |
| W9 | 23 Feb-1 Mar | 7 | 416 | 59.4 | -63% |
| W10 | 3-8 Mar | 6 | 366 | 61.0 | -62% |
| W11 | 9-15 Mar | 7 | 496 | 70.9 | -56% |
| W12 | 16-22 Mar | 7 | 459 | 65.6 | -59% |
| W13 | 23-29 Mar | 7 | 369 | 52.7 | -67% |
| W14 | 30 Mar-5 Apr | 7 | 333 | 47.6 | -70% |
| W15 | 6-12 Apr | 7 | 388 | 55.4 | -65% |
| W16 | 13 Apr | 1 | 61 | 61.0 | -62% |

**Trajectory:** Declining from W8 (76/d) to W14 (47.6/d), with a slight recovery in W15 (55.4/d). The W15 uptick aligns with the Easter Sale (4-12 Apr, all regions). W11 peak (70.9/d) coincides with the AfterPay Day Sale (19-22 Mar, AU+CA).

**Pattern:** Promo weeks bump by ~15-20/d, then demand drops back. Baseline without promos appears to be ~50-55/d and slowly declining. Joel's NCROAS testing (tighter ad targets, running since mid-Feb) is the most likely driver — demand dropped from ~76/d to ~50/d over the test period.

**No sustained improvement in 8 weeks.** The 160/d target is disconnected from reality.

---

## TOP 20 COLOURS (by 14d Shopify volume)

| SKU         | Name            | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap 14d |
| ----------- | --------------- | --------- | ------- | -------- | -------- | ------- |
| POW-CLE-193 | Clear           | 60.0      | 31.1    | 30.7     | 32.2     | -49%    |
| POW-HEA-515 | Heaven          | 46.0      | 17.9    | 17.0     | 17.9     | -63%    |
| POW-PIL-194 | Pillow Talk     | 40.0      | 17.3    | 17.0     | 18.3     | -57%    |
| POW-POS-184 | Positivi-Tea    | 50.0      | 15.6    | 16.3     | 18.3     | -67%    |
| POW-TRA-452 | Treasure        | 28.0      | 13.3    | 12.6     | 13.4     | -55%    |
| POW-MON-005 | Moon Magic      | 34.0      | 14.0    | 12.4     | 13.5     | -64%    |
| POW-BLA-384 | Blackberry      | 28.0      | 12.1    | 11.8     | 12.2     | -58%    |
| POW-PEA-068 | Peaches n Cream | 20.0      | 10.7    | 10.8     | 11.8     | -46%    |
| POW-GOD-017 | Goddess         | 22.0      | 11.3    | 10.1     | 9.8      | -54%    |
| POW-FAL-431 | Fall            | 28.0      | 10.4    | 9.8      | 10.0     | -65%    |
| POW-BOU-222 | Boujee          | 28.0      | 10.1    | 9.6      | 10.6     | -66%    |
| POW-HAR-139 | Harmony         | 20.0      | 8.3     | 9.1      | 9.3      | -55%    |
| POW-YOU-256 | Yours Truly     | 22.0      | 8.3     | 9.1      | 9.4      | -59%    |
| POW-BAR-198 | Bare Necessity  | 24.0      | 9.3     | 9.0      | 9.7      | -62%    |
| POW-CHA-011 | Champagne Toast | 26.0      | 8.9     | 8.4      | 9.3      | -68%    |
| POW-SWE-001 | Sweet Tooth     | 24.0      | 7.6     | 8.2      | 9.2      | -66%    |
| POW-CRE-217 | Creme Brulee    | 22.0      | 8.0     | 8.1      | 8.7      | -63%    |
| POW-FAI-308 | Fairytale       | 16.0      | 8.0     | 7.8      | 8.6      | -51%    |
| POW-EMB-602 | Embers          | 16.0      | 7.1     | 7.6      | 8.3      | -52%    |
| POW-GOO-208 | Good Morning    | 20.0      | 7.1     | 7.5      | 8.9      | -62%    |

Total colour DSR: 7d = 623/d, 14d = 563/d. All colours underperforming model by 46-68%.

Clear is #1 by a wide margin (30.7/d) and closest to model (-49%). Everything else is -50% or worse.

---

## SALES SPIKES (7d > 30d by 50%+)

| SKU         | Name      | 7d   | 14d | 30d | Spike | Likely Cause                                |
| ----------- | --------- | ---- | --- | --- | ----- | ------------------------------------------- |
| POW-COR-045 | Coral     | 7.9  | 3.9 | 1.8 | +339% | **New collection launch**                   |
| POW-OPA-040 | Opal      | 7.9  | 3.9 | 1.8 | +339% | New collection launch                       |
| POW-SER-039 | Serenity  | 10.0 | 5.0 | 2.3 | +335% | New collection launch                       |
| POW-BLO-042 | Blossom   | 10.4 | 5.2 | 2.4 | +333% | New collection launch                       |
| POW-CHA-047 | Champagne | 6.0  | 3.0 | 1.4 | +329% | New collection launch                       |
| POW-ORC-038 | Orchid    | 12.4 | 6.2 | 2.9 | +328% | New collection launch                       |
| POW-RAD-043 | Radiant   | 14.0 | 7.0 | 3.3 | +324% | New collection launch (SKU issue 10-14 Apr) |
| POW-CHE-044 | Cherry    | 8.0  | 4.0 | 1.9 | +321% | New collection launch                       |

**All 8 spiking colours are from the same new collection** launched by Gav (identified 22 Mar, 25 colours ready for CA). Combined 7d demand: 76.6/d across 8 SKUs. This is genuine launch demand, not an anomaly.

**Stock risk:** These colours have limited stock (700-750 units each) and nothing on order until CA 25072026 (Aug). At current 7d rates, Orchid (57d), Blossom (70d), Opal (94d) stock out well before August. Already flagged in POS Check.

No active promo found in `#sale-announcements` or `#cro-team-meetings` driving these specifically — it's organic launch demand.

---

## SALES DROPS (7d < 30d by 40%+)

| SKU           | Name                | 7d  | 14d | 30d  | Drop  | Cause                             |
| ------------- | ------------------- | --- | --- | ---- | ----- | --------------------------------- |
| ACC-REM-500   | Remove 500ml        | 0.0 | 0.0 | 12.3 | -100% | OOS — restock arriving ~18-20 Apr |
| ACC-REM-BUN-2 | 500ml + Bowl bundle | 0.0 | 0.0 | 7.5  | -100% | OOS (Remove 500ml component)      |
| POW-BLU-ZGD22 | Blue Crystal        | 0.0 | 0.0 | 1.7  | -100% | Likely OOS or delisted            |
| POW-GHO-771   | Ghost               | 0.6 | 1.0 | 1.5  | -60%  | Low volume, could be noise        |
| POW-LEM-ZGD01 | Lemonade            | 2.0 | 3.2 | 4.1  | -51%  | Declining — monitor               |
| POW-SEA-450   | Seashell            | 2.0 | 2.2 | 3.4  | -41%  | Declining — monitor               |

The Remove 500ml / BUN-2 drops are entirely OOS-driven — demand will return once restocked. ACC-REM-BUN-1 (120ml bundle) spiking from 7.5/d to 12.1/d confirms customers are substituting.

---

## CONTAINER ARRIVALS DETECTED (from 3PL data)

| Date | SKUs | Units | Likely Cause |
|---|---|---|---|
| 4 Mar | 8 | +2,255 | Reconciliation — top SKUs (POW-JUS-449 +796, POW-MON-005 +590) match Feb cycle count corrections from 247 |
| 3 Apr | 9 | +14 | Returns or minor corrections |

**No large container arrival detected.** CA 03022026 + CA 07042026 (94,268 units) have NOT been checked in — confirmed held at customs.

---

## INVENTORY DISCREPANCIES

### Stock Losses (raise with 3PL)

Kit alignment is CLEAN — 3PL deductions match Shopify within 3 units/day for all 3 kit SKUs. This is good data integrity.

Liquid alignment is also clean when accounting for kit-adjusted demand (Heal) and bundle effects (Remove, Bowl).

No material unexplained stock losses in the last 14 days.

### Red Flags

| Date | SKU | Deduction | Benchmark | Note |
|---|---|---|---|---|
| 2 Mar | ACC-RE5-INN | 9,999 | 100 | Component transfer to Swift — EXPECTED |
| 11 Apr | POW-RAD-043 | 829 | 35 | SKU went inactive (Gav rename) — NOT real. Reactivated 14 Apr |
| Multiple | POW-CLE-193 | 38-84/d | 35 | Clear is #1 colour. Genuinely high demand. Consider raising benchmark to 60 |

### Component Transfers

ACC-RE5-INN (Remove 500ml inner), ACC-RE5-BOT, ACC-RE5-LID, ACC-RE1-BOT, ACC-RE1-LID, ACC-RE1-INN, HEA-EMP, HEA-LID, HEA-BSH — all went to 0 in late Feb/early Mar. This is the Swift fill component transfer. Expected.

---

## 3PL DEDUCTION CHECK

### Kits — ALIGNED

| SKU | 3PL Ded/d | Shopify/d | Gap | Status |
|---|---|---|---|---|
| KIT-STA-2 | 15.3 | 14.8 | +0.5 | ALIGNED |
| KIT-COM-4 | 30.6 | 27.4 | +3.2 | ALIGNED |
| KIT-ULT-6 | 11.5 | 10.4 | +1.1 | ALIGNED |

Clean. 3PL deduction logic is working correctly.

### Liquids — explained gaps

| SKU | 3PL Ded/d | Shopify/d | Gap | Note |
|---|---|---|---|---|
| LIQ-HEA-5 | 61.1 | 1.6 | +59.5 | Kit-adjusted (3PL includes kit consumption). Expected. |
| LIQ-BAS-2 | 15.1 | 11.7 | +3.4 | ALIGNED. ~2/d from LIQ-SET bundle. |
| LIQ-GLO-4 | 8.9 | 6.3 | +2.6 | ALIGNED. ~2/d from LIQ-SET. |
| LIQ-SEA-3 | 11.3 | 8.6 | +2.7 | ALIGNED. ~2/d from LIQ-SET. |
| LIQ-BON-1 | 6.2 | 3.6 | +2.6 | ALIGNED. ~2/d from LIQ-SET. |
| ACC-REM | 41.1 | 25.1 | +16.0 | Bundle effect (ACC-REM-BUN-1 = 12.1/d). 25.1 + 12.1 = 37.2 ≈ 41.1. |
| ACC-REM-BOW | 18.5 | 4.9 | +13.6 | Both bundles (BUN-1 12.1 + BUN-2 0 currently). Shopify 4.9 = standalone bowl sales. |

All gaps are explained by kit consumption, LIQ-SET, or bundle effects. **No data integrity issues.**

---

## DEAD STOCK (colours in stock, 0 Shopify sales in 14d)

**15 colours, 7,330 total units.**

| SKU | Name | Stock | Note |
|---|---|---|---|
| POW-JUB-L11 | Jubilee | 1,025 | |
| POW-ANG-D09 | Angel | 994 | Unlaunched |
| POW-DRE-D08 | Dream | 809 | Unlaunched |
| POW-SAT-D10 | Satin | 799 | Unlaunched |
| POW-ROS-D14 | Rose | 798 | Unlaunched |
| POW-VEL-D13 | Velvet | 797 | Unlaunched |
| POW-BLO-D07 | Bloom | 790 | Unlaunched |
| POW-STA-009 | Starlight | 723 | |
| POW-UND-056 | Under | 453 | |
| POW-SAF-149 | Saffron Blaze | 50 | Fire Collection — needs launch |
| POW-ALL-146 | All Eyes On Me | 39 | Fire Collection |
| POW-RED-165 | Red Mischief | 1 | Fire Collection — essentially OOS |
| POW-INF-506 | Inferno Hour | 42 | Fire Collection |
| POW-GAR-656 | Garnet Games | 9 | Fire Collection |
| POW-BOR-355 | Bordeaux Nights | 1 | Fire Collection — essentially OOS |

**Two groups:**
1. **Unlaunched colours (5,987 units):** POW-ANG-D09, DRE-D08, SAT-D10, ROS-D14, VEL-D13, BLO-D07. Likely part of the 34 colours Daniel flagged on 18 Mar as sitting at 247 but not on the CA website. Check if these are in Gav's rollout plan (22 Mar he identified 25 ready to launch).
2. **Fire Collection (141 units across 5 SKUs):** SAF-149, ALL-146, RED-165, INF-506, GAR-656. 3 of 5 are at 0-1 units (effectively OOS). Need launching on the CA site if planned, otherwise dead inventory.

---

## KEY TAKEAWAYS

1. **Growth factor 2.0x → 0.72x.** Selling 67% below scaled target for 8 consecutive weeks. Joel's NCROAS testing is the likely driver. Every model DSR and days cover is ~3x overstated. Greg must update to stop misleading ordering decisions.

2. **New colour collection is the one bright spot.** 8 colours launched, combined 77/d demand. Orchid and Blossom are the standouts (10-12/d each). But stock is limited (700-750 units each) with no restock until Aug. Consider adding to CA 21062026 or accept stockout.

3. **Remove 500ml OOS is causing substitution.** ACC-REM-BUN-1 (120ml bundle) jumped from 7.5/d to 12.1/d. ACC-REM (120ml standalone) also trending up (17→25.9/d). Once 500ml restocks (~18-20 Apr), expect 120ml demand to normalise back down.

4. **Data integrity is clean.** Kit alignment within 3 units/day. All liquid and remove gaps explained by kit consumption, LIQ-SET, and bundle effects. No unexplained stock losses.

5. **7,330 units of dead stock across 15 colours.** Mostly unlaunched D-suffix colours (5,987 units) and Fire Collection (141 units, 3 effectively OOS). Gav/Joel to confirm whether these are planned for launch or should be cleared.
