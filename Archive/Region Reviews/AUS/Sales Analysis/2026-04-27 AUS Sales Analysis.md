# AUS Sales Data Analysis — 27 Apr 2026

## DATA FRESHNESS

- **Shopify:** through 26 Apr (1d lag, normal).
- **3PL (AUS 3GPL):** through 27 Apr (today).
- **Growth factor:** 1.3x (base 147/d → scaled 191.1/d). AUS 07062026 Birthday container 1.4x.

## SCOPE — STRESS TESTS

This analysis focuses on three questions raised in the POS Check:
1. W17 kit trajectory — post-Easter trough or step-change down?
2. STA mix-shift — did Daniel's W15/W16 +13.9% vs model hold, or revert?
3. Colour deduction anomaly status — did the ~1,000-unit single-day pattern continue past 16 Apr?

---

## DSR: MODEL vs REALITY

### Kits

| SKU | Model DSR | 7d | 14d | 30d | Gap vs Model (14d) |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 34.0 | 23.4 | 23.9 | 30.9 | **-30%** |
| KIT-COM-4 | 78.0 | 45.7 | 46.0 | 54.9 | **-41%** |
| KIT-ULT-6 | 35.0 | 17.3 | 17.5 | 21.9 | **-50%** |
| **Total** | **147** | **86.4** | **87.4** | **107.7** | **-41% vs base / -54% vs scaled** |

Actual growth factor: 87.4 / 147 = **0.59x** (vs 1.3x model). Recommended: **0.65x** (1.1× actual).
Holding 1.3x as projected target per user 27 Apr — flagged as health metric, not correction.

### Heal (kit-adjusted)

| SKU | Model DSR | Shop 7d | Shop 14d | 3PL 14d | Adj Cover @ 3PL |
|---|---:|---:|---:|---:|---:|
| LIQ-HEA-5 | 184.6 | 1.1 | 1.1 | 98.8 | 100d |

Model 184.6/d is the kit-adjusted projection. Actual 3PL deduction of 98.8/d aligns with kit consumption at ~0.65x scaled. Stock 9,919 → 100d cover. The OP fill of 11,500 (pending Chantelle) extends to ~210d post-arrival — comfortably bridges to AUS 08072026 (CN-in-kit).

### Liquids (standalone, pre-packed in kits from CN)

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | 3PL 14d | Comment |
|---|---:|---:|---:|---:|---:|---|
| LIQ-BAS-2 (Base) | 53.3 | 16.3 | 19.5 | 18.0 | 24.5 | 3PL > Shopify - bundle/kit leakage. Real run-rate ~24.5 |
| LIQ-SEN-2 (LO Base) | 9.1 | 4.9 | 4.9 | 2.3 | 5.5 | Aligned 3PL = Shopify = 5/d. Model overstates |
| LIQ-GLO-4 (Glow) | 26.0 | 6.3 | 6.9 | 10.7 | 9.5 | Model ~3x reality; 3PL dropping at ~9.5/d |
| LIQ-SEN-4 (LO Glow) | 7.8 | 2.7 | 2.9 | 1.4 | 4.0 | Real ~3-4/d |
| LIQ-SEA-3 (Seal) | 44.2 | 10.7 | 11.1 | 14.5 | 13.2 | Model ~3x reality |
| ACC-REM-500 (Remove 500ml) | 98.8 | 20.6 | 20.2 | 26.2 | 46.8 (post-fill, low confidence) | User-confirmed: trust sheet 98.8/d (~82d cover) |
| ACC-REM-BOW | 75.4 | 1.7 | 2.1 | 3.2 | 34.2 | **94% of 3PL deduction comes from bundles, not standalone** |

Bundle leakage clarification on ACC-REM-BOW: Shopify standalone 2.1/d vs 3PL 34.2/d. Difference (32.1/d) flows through ACC-REM-BUN-1 (with 120ml) and ACC-REM-BUN-2 (with 500ml). Cover at 36d should be trusted (3PL is reality), not the misleading 587d if you only used Shopify standalone.

---

## STRESS TEST 1 — W17 Kit Trajectory

| Week | Dates | Kits/day | vs Model 191 | vs Base 147 | vs prev | Notes |
|---|---|---:|---:|---:|---:|---|
| W11 | 9-15 Mar | 105.3 | -45% | -28% | - | STA + ULT OOS, recovery starting |
| W12 | 16-22 Mar | 130.3 | -32% | -11% | +24% | Container arriving, BO clearing |
| W13 | 23-29 Mar | 128.4 | -33% | -13% | -1% | B360 BO clearing |
| W14 | 30 Mar-5 Apr | 105.4 | -45% | -28% | -18% | Easter dip (G3PL closed 3-7 Apr) |
| W15 | 6-12 Apr | 135.3 | -29% | -8% | +28% | **Best week post-transition** - Easter sale live |
| W16 | 13-19 Apr | 103.0 | -46% | -30% | -24% | Easter sale tail; G3PL re-open |
| W17 | 20-26 Apr | **86.4** | **-55%** | **-41%** | -16% | **Lowest weekly rate in 9 weeks** |

### Daily detail (last 14 days)

| Date | Total Kits | Notes |
|---|---:|---|
| 13 Apr | 110 | W16 starts, Easter sale active |
| 14 Apr | 89 | |
| 15 Apr | 104 | |
| 16 Apr | 113 | Last strong day |
| 17 Apr | 104 | **Easter sale ends ~here** |
| 19 Apr | 98 | (no 18 Apr data row) |
| 20 Apr | 87 | **Post-Easter step-down** |
| 21 Apr | 84 | |
| 22 Apr | 77 | |
| 23 Apr | 86 | |
| 24 Apr | 74 | Lowest day |
| 25 Apr | 95 | |
| 26 Apr | 102 | Partial recovery |

### Read

- **W17 is not just a trough — it's a post-promo step-down to a new baseline.** Pre-Easter W14 (the closest "no promo" week) ran 105/d. W17 is 86/d → **21% below pre-Easter baseline**.
- Days 20-24 Apr ran 74-87/d (avg 81/d). Days 25-26 ran 95-102/d - early signal of a partial recovery, but only 2 data points.
- The pre-Easter trough (W14) coincided with G3PL public holiday closure. W17 has no equivalent operational disruption - the rate IS the demand.
- **Implication for AUS 08072026 kit mix:** if W17 86/d holds for 1-2 more weeks, treat it as the operational baseline. If 25-26 Apr recovery is real, baseline is 95-105/d. Either way, model 191/d is now -50% to -55% off, and AUS 08072026 will overshoot if sized at 1.3x.

---

## STRESS TEST 2 — STA Mix-Shift Confirmation

| Week | STA/d | vs Model 34 | COM/d | vs 78 | ULT/d | vs 35 |
|---|---:|---:|---:|---:|---:|---:|
| W11 | 30.0 | -12% | 51.0 | -35% | 24.3 | -31% |
| W12 | 29.0 | -15% | 71.0 | -9% | 34.3 | -2% |
| W13 | 37.1 | +9% | 61.9 | -21% | 29.4 | -16% |
| W14 | 31.6 | -7% | 51.4 | -34% | 22.4 | -36% |
| W15 | **38.6** | **+14%** | 68.7 | -12% | 28.0 | -20% |
| W16 | 28.3 | -17% | 54.0 | -31% | 20.7 | -41% |
| W17 | **23.4** | **-31%** | 45.7 | -41% | 17.3 | -50% |

### Read

- **STA's W15 +14% was Easter-sale-driven, not a mix-shift.** W17 reverted to 23.4/d, which is *below* the W11-W14 pre-Easter average (~32/d).
- The W11-W14 pre-Easter STA average was 31.9/d - close to model 34. The W15/W16 +14% read came from Easter promo lift, not a sustained 39/d run rate.
- **All three kits dropped in W17** (-31% / -41% / -50%). STA dropped most in absolute terms vs its pre-Easter baseline; ULT-6 has the worst gap vs model.

### Implication for AUS 08072026 kit mix

The 21 Apr POS Check / Recap suggested "bump STA, cut COM/ULT". After this analysis:
- **STA: don't bump beyond the pre-Easter ~32/d baseline.** Sizing for the 39/d Easter peak overshoots. Recommended sizing: ~25-32/d × container window.
- **COM: cut.** Persistent -30% to -40% vs model across nearly every week. Sizing at 78/d is far too high.
- **ULT: cut hardest.** -36% to -50% vs model across most weeks. Sizing at 35/d → realistic at 17-22/d.

Use whichever is higher: pre-Easter average OR W17 (post-Easter baseline) - to give upside if marketing pulls demand back.

---

## STRESS TEST 3 — Colour Deduction Anomaly Status

### Single-day red flags (3PL deduction > benchmark, last 30 days)

The original 17 Apr investigation flagged 7 SKUs with single-day ~1,000-unit deductions: POW-ENE, POW-DRE, POW-ROY, POW-JUS, POW-GOL, POW-BRE, POW-CRE.

| SKU | Spike Date | Spike Units | New since 17 Apr? |
|---|---|---:|---|
| POW-MIL-193 | 19 Mar | 1,020 | No - pre-existing |
| POW-FRO-001 | 29 Mar | 1,014 | No - pre-existing |
| **POW-STA-033** | **1 Apr** | **1,579** | **YES - missed in 17 Apr investigation** |
| POW-DRE-771 | 8 Apr | 1,113 | Pre-existing |
| POW-JUS-449 | 8 Apr | 1,006 | Pre-existing |
| POW-ROY-304 | 11 Apr | 1,013 | Pre-existing |
| POW-BRE-109 | 12 Apr | 1,007 | Pre-existing |
| POW-GOL-597 | 13 Apr | 1,108 | Pre-existing |
| POW-CRE-217 | 13 Apr | 1,030 | Pre-existing |
| POW-ENE-484 | 16 Apr | 1,001 | Pre-existing (most recent) |

**Pattern stopped after 16 Apr.** No new ~1,000-unit single-day deductions in the 11 days since. **Positive signal.**

**New finding:** POW-STA-033 -1,579 on 1 Apr was not in the 17 Apr investigation list. Add to the Katrina escalation.

### Cumulative gap test (3PL 30d avg deduction × 30 vs Shopify 30d sum)

| SKU | 3PL Avg/d | 3PL 30d | Shopify 30d | Gap | Notes |
|---|---:|---:|---:|---:|---|
| POW-ENE-484 | 251.0 | 7,530 | 18 | **+7,512** | Most extreme. Avg masked by 16 Apr +1,001 + earlier spikes. |
| POW-MIL-193 | 9.8 | 294 | 135 | +159 | Modest |
| POW-CRI-762 | 1.0 | 30 | 27 | +3 | Aligned |
| POW-DRE-771 | 6.3 | 189 | 249 | -60 | Shopify > 3PL (selling caught up) |
| POW-ROY-304 | 6.5 | 195 | 255 | -60 | Aligned / catching up |
| POW-JUS-449 | 4.6 | 138 | 183 | -45 | Aligned |
| POW-GOL-597 | 7.2 | 216 | 231 | -15 | Aligned |
| POW-BRE-109 | 2.7 | 81 | 87 | -6 | Aligned |
| POW-CRE-217 | 15.1 | 453 | 519 | -66 | Aligned |
| POW-STA-033 | 7.0 | 210 | 315 | -105 | Shopify > 3PL |
| POW-FRO-001 | 3.4 | 102 | 135 | -33 | Aligned |
| POW-HEA-641 | 3.5 | 105 | 123 | -18 | Aligned |
| **TOTAL** | | | | **+7,266** | |

### Read

- **POW-ENE-484 dominates the residual.** 7,512 unit cumulative gap = effectively all the unexplained 3PL pull. Most of this stems from spikes prior to + including 16 Apr.
- The other 6 originally flagged SKUs (POW-DRE / POW-ROY / POW-JUS / POW-GOL / POW-BRE / POW-CRE) now have small or negative cumulative gaps - Shopify selling has caught up over 30 days. This means the original spikes were one-off events that "pre-deducted" stock, not ongoing leakage.
- **POW-STA-033 (-1,579 on 1 Apr) is a new addition** with similar pattern - Shopify 30d 315 / 3PL 30d 210 means Shopify > 3PL now (the spike "pre-deducted" units that have since been sold).
- **No active leakage post-16 Apr.** Pattern was a 4-week cluster (19 Mar - 16 Apr) of one-off spikes. Either an inventory adjustment process, write-offs, or a system event with limited duration.

### Bundle vs standalone breakdown — ACC-REM-BOW (sanity check on 36d cover)

| Source | Units/day | % of total |
|---|---:|---:|
| Standalone Shopify (Shop 14d) | 2.1 | 6% |
| ACC-REM-BUN-1 + ACC-REM-BUN-2 (kit-adjusted via bundle) | ~32.1 | 94% |
| **3PL deduction total** | **34.2** | **100%** |

The 3PL 36d cover number is correct. Don't be fooled by the Shopify-only 587d figure - bundle pulls are real demand.

---

## REALISTIC DAYS COVER (key items, model vs actual)

| SKU | Stock | Cover @ Model | Cover @ Actual (3PL or 14d Shopify) | Flag |
|---|---:|---:|---:|---|
| KIT-STA-2 | 1,026 | 23d (44.2/d scaled) | **39d** (3PL 26.5/d) | OK (W17 actual ~23/d → 44d) |
| KIT-COM-4 | 4,598 | 45d | 90d | Healthy |
| KIT-ULT-6 | 2,762 | 61d | 144d | Healthy / overstocked |
| LIQ-BAS-2 | 490 | 9d | 20d | **<14d at model** WARNING |
| LIQ-SEN-2 | 63 | 7d | 11d | **CRITICAL** |
| LIQ-GLO-4 | 828 | 32d | 87d | OK |
| LIQ-SEN-4 | 157 | 20d | 39d | WATCH |
| LIQ-HEA-5 | 9,919 | 54d | 100d | OK; OP fill pending |
| ACC-REM-500 | 8,058 | **82d** (sheet) | n/a (sheet trusted) | OK |
| ACC-REM-BOW | 1,233 | 16d | 36d | WATCH |
| ACC-LAB | 16,787 | 46d | 105d | OK; needs Avi PO mid-May |

---

## CONTAINER ARRIVALS DETECTED (last 30 days, from 3PL)

| Date | SKU Count | Total Units | Top 5 |
|---|---:|---:|---|
| 27 Mar | 96 | 69,623 | ACC-THA, STO-MAI-BAG-S, POW-BAR-198, POW-SHH-013, ACC-NAI-100/180 |
| 28 Mar | 95 | 84,008 | ACC-INS, ACC-5PC-BAG, ACC-RE1-LID, ACC-REM, STO-MAI-BAG-S |
| 10 Apr | 118 | 128,553 | ACC-THA, ACC-INS, STO-MAI-BAG-S, STO-MAI-2, ACC-RE5-BOT |
| 14 Apr | 197 | 194,695 | POW-CLE-193, ACC-STI-45885, POW-BOU-222, ACC-REM, POW-HEA-515 |

14 Apr is the B360 PACKUP delivery (197 SKUs is very large, consistent with packup transfer). 10 Apr likely is part of AUS 07032026 final check-in continuation.

---

## SELLING PERFORMANCE FLAGS

### Sales drops (7d well below 30d, post-Easter)

All three kits dropped post-Easter. Driver = end of Easter sale 17 Apr; ad spend / promo lift removed.

| SKU | 7d | 14d | 30d | 7d vs 30d |
|---|---:|---:|---:|---:|
| KIT-STA-2 | 23.4 | 23.9 | 30.9 | -24% |
| KIT-COM-4 | 45.7 | 46.0 | 54.9 | -17% |
| KIT-ULT-6 | 17.3 | 17.5 | 21.9 | -21% |

### Standalone liquid drops

| SKU | 7d | 14d | 30d | Notable |
|---|---:|---:|---:|---|
| LIQ-BAS-2 | 16.3 | 19.5 | 18.0 | 7d slightly below 14d but stable |
| LIQ-SEN-2 (LO Base) | 4.9 | 4.9 | 2.3 | 7d above 30d - standalone interest growing |
| LIQ-SEN-4 (LO Glow) | 2.7 | 2.9 | 1.4 | Same trend |

### Underperformers (kits >40% below model 14d)

- KIT-COM-4 -41%
- KIT-ULT-6 -50%

### Dead stock (not in scope here - would be Step 7 on full run; flag separately if needed)

---

## KEY TAKEAWAYS

1. **W17 is a post-Easter step-down to ~86/d, not a trough.** Pre-Easter baseline (W14) was 105/d. Even if the 25-26 Apr partial recovery sustains, baseline is ~95-105/d. Sizing AUS 08072026 at scaled 191/d will overshoot by ~50%.
2. **STA mix-shift didn't happen.** W15 +14% was Easter sale, not a structural change. Pre-Easter STA averaged 32/d and W17 is 23/d - below baseline, not above. **Don't bump STA on AUS 08072026 beyond ~32/d sizing.**
3. **Colour deduction anomaly stopped 16 Apr.** No new ~1,000-unit spikes in 11 days. The 7-SKU pattern was a 4-week cluster (19 Mar - 16 Apr), likely write-offs or stock adjustments. **POW-STA-033 (1 Apr -1,579) is a new addition** that wasn't in the 17 Apr list - add to Katrina escalation.
4. **POW-ENE-484 holds the residual cumulative gap of 7,512 units.** All other 6 originally flagged SKUs have caught up (Shopify ≥ 3PL on 30d basis). Push Katrina specifically on POW-ENE-484.
5. **AUS 08072026 kit-mix call** (due 29 Apr) should reflect: STA ~25-32/d (pre-Easter baseline, not Easter peak); COM ~50/d (10 weeks under 78); ULT ~17-22/d (50% off model consistently). Plus add Heal-in-kit, ACC-LAB ~20k, ACC-THA top-up (per POS Check).
