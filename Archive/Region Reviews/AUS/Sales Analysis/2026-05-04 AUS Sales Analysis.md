# AUS Sales Data Analysis — 4 May 2026

## DATA FRESHNESS

- **Shopify:** through 3 May (+1d lag, normal).
- **3PL (AUS 3GPL):** through 4 May (today).
- **Growth factor:** 1.3x (base 147/d → scaled 191.1/d). AUS 07062026 1.4x.

## SCOPE — STRESS TESTS

1. W18 kit trajectory — is 71.7/d a sustained step-down or distorted by a single weak day?
2. AUS 08072026 kit mix sizing - has the W18 softness moved the recommendation further down vs 27 Apr?
3. Cumulative colour deduction gap (POW-ENE-484 et al.) - did the 16 Apr cessation hold and the gap close?
4. Sensitive Base / Sensitive Glow demand spike confirmation - LIQ-SEN-2 went OOS today.
5. LIQ-BAS-2 7d Shopify surge - user notes typically repeat buyers, confirm benign.

---

## DSR: MODEL vs REALITY

### Kits

| SKU | Model DSR | 7d | 14d | 30d | Gap vs Model (14d) |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 34.0 | 20.7 | 22.1 | 27.9 | **-35%** |
| KIT-COM-4 | 78.0 | 32.6 | 39.1 | 49.7 | **-50%** |
| KIT-ULT-6 | 35.0 | 18.4 | 17.9 | 21.3 | **-49%** |
| **Total** | **147** | **71.7** | **79.1** | **98.9** | **-46% vs base / -59% vs scaled** |

Actual growth factor: 79.1 / 147 = **0.54x** (vs 1.3x model). Recommended (1.1× actual): **0.59x**. Holding 1.3x as projected target per `feedback_growth_factor_framing.md` - flagged as health metric, not correction.

### Heal (kit-adjusted)

| SKU | Model DSR | Shop 7d | Shop 14d | 3PL 14d | Adj Cover @ 3PL |
|---|---:|---:|---:|---:|---:|
| LIQ-HEA-5 | 184.6 | 3.1 | 2.1 | 82.2 | 114d |

Model 184.6/d kit-adjusted projection. Actual 3PL deduction 82.2/d aligns with 79.1/d kit consumption + standalone Shopify 2.1/d - **3PL ~3.0/d above pure kit-attached.** Slightly elevated vs prior reviews (98.8/d 27 Apr). Suggests fewer kits sold OR Heal-in-kit consumption rate gradually reducing - either way, current cover is healthier than 27 Apr's read.

### Liquids (standalone, pre-packed in kits from CN)

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | 3PL 14d | Comment |
|---|---:|---:|---:|---:|---:|---|
| LIQ-BAS-2 (Base) | 53.3 | **27.6** | 21.9 | 19.6 | 24.7 | **7d +41% vs 30d** - user-confirmed repeat-buyer surge. Not anomaly. |
| LIQ-SEN-2 (LO Base) | 9.1 | **8.1** | 6.5 | 4.2 | 7.3 | **7d +93% vs 30d.** Real demand growth. **OOS today.** |
| LIQ-GLO-4 (Glow) | 26.0 | 9.4 | 7.9 | 10.4 | 9.4 | Model overstates ~3x. |
| LIQ-SEN-4 (LO Glow) | 7.8 | **6.0** | 4.4 | 2.8 | 5.0 | **7d +114% vs 30d.** Real demand growth. |
| LIQ-SEA-3 (Seal) | 44.2 | 18.0 | 14.4 | 16.1 | 13.2 | Model overstates ~3x. |
| LIQ-BON-1 (Bond) | (nominal) | 5.7 | 4.8 | 5.9 | n/a | Steady. |
| LIQ-SOA-6 (Sensitive Glow) | n/a | 3.4 | 3.3 | 4.8 | n/a | Steady. |

**Sensitive product line is collectively up.** LIQ-SEN-2 + LIQ-SEN-4 + LIQ-SOA-6 7d sums to 17.5/d, vs 30d 11.8/d = +48%. Worth a marketing read - is something pushing sensitive variants?

### Remove products (standalone)

| SKU | Model DSR | Shop 7d | Shop 14d | 3PL 14d | Comment |
|---|---:|---:|---:|---:|---|
| ACC-REM (120ml) | n/a | 5.7 | 6.9 | 19.4 | Bundle leakage (ACC-REM-BUN-1). Real cover via 3PL. |
| ACC-REM-500 | 98.8 | 19.5 | 23.0 | (post-fill, low confidence) | Sheet 98.8/d trusted (user 27 Apr). Stock 7,787 = ~80d. |
| ACC-REM-BOW | 75.4 | 1.3 | 1.5 | 31.6 | **94% of 3PL deduction is bundle pulls.** 33d cover trustworthy. |

### Top 15 colours (14d total)

| SKU (Name) | 14d total | 14d/d | Notable |
|---|---:|---:|---|
| POW-CLE-193 (Clear) | 486 | 34.7 | **GWP campaign** SKU. 14d includes pre-launch + 3 May launch days. Stock 38,235 = healthy. |
| POW-POS-184 (Positive Pulse) | 349 | 24.9 | Strong seller. |
| POW-HEA-515 (Hearts on Fire) | 319 | 22.8 | Strong seller. |
| POW-PIL-194 (Pillow Talk) | 257 | 18.4 | |
| POW-BUB-516 (Bubbly) | 210 | 15.0 | |
| POW-OAK-283 | 184 | 13.1 | Stable. |
| POW-SWE-001 (Sweet Tooth) | 181 | 12.9 | **30d 18.3 → 7d 10.3 = -44%.** Cooling after Easter. |
| POW-GOD-017 (Goddess) | 178 | 12.7 | Recovered from 27 Apr "demand collapsed 59%" position. |
| POW-BLA-384 | 175 | 12.5 | |
| POW-MON-005 (Moon Magic) | 170 | 12.1 | |
| POW-CRE-217 (Creme Brulee) | 167 | 11.9 | One of the original "anomaly 7" (see Step 5B). |
| POW-DUS-346 | 161 | 11.5 | |
| POW-TRA-452 | 148 | 10.6 | |
| POW-BOU-222 | 140 | 10.0 | |
| POW-FAI-308 (Fairytale) | 138 | 9.9 | |

Total colour 14d = 8,726 = 623.3/d. Expected from kits (STA×3 + COM×6 + ULT×9 over 14d) = 461.8/d. **Excess 161.5/d is standalone colour sales (~26% of demand).**

---

## WEEKLY KIT TREND

| Week | Dates | Kits/day | vs 191 (1.3x) | vs 147 (base) | vs prev | Notes |
|---|---|---:|---:|---:|---:|---|
| W11 | 9-15 Mar | 105.3 | -45% | -28% | - | STA + ULT OOS, recovery starting |
| W12 | 16-22 Mar | 130.1 | -32% | -11% | +24% | Container arriving, BO clearing |
| W13 | 23-29 Mar | 128.4 | -33% | -13% | -1% | B360 BO clearing |
| W14 | 30 Mar-5 Apr | 105.4 | -45% | -28% | -18% | Easter dip (G3PL closed 3-7 Apr) |
| W15 | 6-12 Apr | 135.3 | -29% | -8% | +28% | **Best week post-transition** - Easter sale live |
| W16 | 13-19 Apr | 103.0 | -46% | -30% | -24% | Easter sale tail; G3PL re-open |
| W17 | 20-26 Apr | 86.4 | -55% | -41% | -16% | Lowest since transition |
| W18 | 27 Apr-3 May | **71.7** | **-62%** | **-51%** | **-17%** | **New low. Single 39-unit Tuesday distorts; ex-Tuesday avg ~76/d.** |

### Daily detail W17-W18

| Date | Total Kits | Day | Notes |
|---|---:|---|---|
| 20 Apr | 87 | Mon | W17 starts |
| 21 Apr | 84 | Tue | |
| 22 Apr | 77 | Wed | |
| 23 Apr | 86 | Thu | |
| 24 Apr | 74 | Fri | |
| 25 Apr | 95 | Sat | |
| 26 Apr | 102 | Sun | |
| 27 Apr | 73 | Mon | W18 starts |
| 28 Apr | **39** | Tue | **Lowest day in dataset** - 47% below same-day-of-week W17 |
| 29 Apr | 64 | Wed | |
| 30 Apr | 80 | Thu | |
| 1 May | 83 | Fri | |
| 2 May | 71 | Sat | |
| 3 May | 92 | Sun | |

**Read:**
- 28 Apr 39 kits = a single anomalous day, not a pattern signal. Without it, W18 partial is 76.4/d (still down from W17 86.4 but in line with the broader trend).
- 30 Apr-3 May ran 80/83/71/92 = 81.5/d avg. **Closer to a stable W18 baseline than 71/d suggests.**
- The 4-week trajectory W15→W18: 135 → 103 → 86 → 71. **-9% per week step-down.** Easter ad spend wind-down + post-promo normalisation.

### Kit mix (14d)

| SKU | 14d total | 14d/d | Model | Gap | Mix Share |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 309 | 22.1 | 34.0 | -35% | 28% |
| KIT-COM-4 | 548 | 39.1 | 78.0 | -50% | 49% |
| KIT-ULT-6 | 250 | 17.9 | 35.0 | -49% | 23% |

**Mix unchanged from last review.** Complete remains the workhorse at ~50% of kit volume. STA continues at 28% (vs model 23% expected). ULT at 23% steady.

---

## REALISTIC DAYS COVER (key items)

| SKU | Stock | Cover @ Model | Cover @ Actual | Flag |
|---|---:|---:|---:|---|
| KIT-STA-2 | 885 | 20d | 40d | **<14d at Shopify 7d 20.7/d → 43d** OK at actual; tight at projected |
| KIT-COM-4 | 4,364 | 43d | 109d | Healthy |
| KIT-ULT-6 | 2,636 | 58d | 151d | Overstocked at actual rate |
| LIQ-BAS-2 | 298 | 6d | 12d | **CRITICAL** |
| LIQ-SEN-2 | 0 | OOS | OOS | **OOS - listing decision needed** |
| LIQ-GLO-4 | 755 | 29d | 80d | OK |
| LIQ-SEN-4 | 113 | 14d | 23d | **WARNING** |
| LIQ-HEA-5 | 9,390 | 51d | 114d | OK; +11,500 OP fill pending |
| ACC-REM-500 | 7,787 | 79d | n/a (sheet trusted) | OK |
| ACC-REM-BOW | 1,031 | 14d | 33d | **WATCH at model rate** |
| ACC-LAB | 15,788 | 46d | 108d | OK; mid-May Avi PO |

---

## CONTAINER ARRIVALS DETECTED (last 30 days, from 3PL)

| Date | SKU Count | Total Units | Top SKUs |
|---|---:|---:|---|
| 14 Apr | ~150+ | ~190,000 | B360 PACKUP delivery (large mixed inbound) |
| 18 Apr | 1 | +14,808 | ACC-LAB (Avi PO 11) |
| 24 Apr | 1 | +4,795 | ACC-REM-500 (24-03-2026 OP fill) |

No CN container arrivals since 14 Apr. AUS Powder Room (24-03-2026) FedEx-delivered today per Remy email - awaiting G3PL check-in.

---

## INVENTORY DISCREPANCY DETECTION

### 5A — Single-day flags (last 7 days)

| Date | SKU | Deduction | Benchmark | Class |
|---|---|---:|---:|---|
| 4 May | POW-CLE-193 | 203 | 35 | **Explained** - GWP AUS-$85-GIF launch (3 May), 1× POW-CLE-193 per qualifying kit order. 59 orders queued at launch + new 4 May orders = ~200 expected. |
| 4 May | POW-SUN-SU015 | 123 | 35 | **Explained** - same GWP. POW-SUN-SU015 cover at 1,706 / 123/d = 14d if GWP rate sustained - flag for monitoring (Shopify 7d standalone 8.9/d, GWP rate likely tapering as queue clears). |
| 4 May | LIQ-BAS-2 | 79 | 90 | **Below benchmark** but +3x normal. User-confirmed: repeat-buyer surge, not anomaly. |
| 4 May | LIQ-SEN-2 | 24 | 18 | **Above benchmark** - last LO Base units cleared. Real OOS event. |

No unexplained single-day flags.

### 5B — Cumulative gap test (3PL 30d vs Shopify 30d)

The originally-flagged 7 colours from 17 Apr (POW-ENE-484, POW-DRE-771, POW-ROY-304, POW-JUS-449, POW-GOL-597, POW-BRE-109, POW-CRE-217) plus the 27 Apr addition (POW-STA-033):

| SKU | 3PL avg/d | 3PL 30d | Shopify 30d | Gap | Comment |
|---|---:|---:|---:|---:|---|
| POW-ENE-484 | 32.8 | 984 | 18 | **+966** | 27 Apr was +7,512. **Reduced ~85%.** Either spike rolled out of window or reconciliation captured. |
| POW-DRE-771 | 42.1 | 1,262 | 223 | +1,039 | 27 Apr was -60. Jumped back up. **Investigate.** |
| POW-ROY-304 | 39.6 | 1,188 | 274 | +914 | 27 Apr was -60. Jumped back up. **Investigate.** |
| POW-JUS-449 | 37.6 | 1,127 | 174 | +953 | 27 Apr was -45. Jumped back up. **Investigate.** |
| POW-GOL-597 | 42.3 | 1,269 | 221 | +1,048 | 27 Apr was -15. Jumped back up. **Investigate.** |
| POW-BRE-109 | 35.3 | 1,060 | 96 | +964 | 27 Apr was -6. Jumped back up. **Investigate.** |
| POW-CRE-217 | 47.3 | 1,418 | 495 | +923 | 27 Apr was -66. Jumped back up. **Investigate.** |
| POW-STA-033 | 8.5 | 254 | 292 | -38 | Aligned. |
| POW-MIL-193 | 6.1 | 182 | 180 | +2 | Aligned. |
| POW-FRO-001 | 3.5 | 106 | 121 | -15 | Aligned. |

**Significant finding:** the 6 colours (POW-DRE / POW-ROY / POW-JUS / POW-GOL / POW-BRE / POW-CRE) that 27 Apr showed had "caught up" (gap near zero) **now show ~900-1,050 unit gaps each**. **+5,841 units of new excess 3PL deduction across these 6 SKUs since 27 Apr** (compared to ~200 expected at average rates).

Possible explanations:
- The B360 PACKUP -200/-250 variances (Remy's 28 Apr email to Jake) for several of these SKUs (CRE-217 -250, FRO-001 not in list, ROY-304 not in list, BRE-109 not in list) may have manifested as 3PL deductions when reconciled into Greg's tracker.
- Greg may have done a reconciliation adjustment that pulled these down.
- A new spike pattern starting late April.

**Action:** cross-reference with Greg's 27 Apr+ stock tracker updates and the PO 9 B360 PACKUP variance list (Jake's Friday count, still pending). If these are legitimate write-offs from PO 9, expect them to net to the variance figures (~200-250 each). The gap of ~1,000 each is roughly 4x the PO 9 variance per SKU - suggests a separate event.

POW-ENE-484 the original outlier dropped from +7,512 to +966 - likely the 16 Apr spike rolling out. **Net AUS colour gap exposure today:** ~7,000+ units across 7 SKUs (vs ~7,500 last review on 1 SKU dominated by POW-ENE).

### 5C — Stock gains

- ACC-LAB +14,808 on 18 Apr - Avi PO 11 (expected).
- ACC-REM-500 +4,795 on 24 Apr - 24-03-2026 OP Remove fill (expected).
- B360 PACKUP +large mixed delivery 14 Apr - already absorbed.

### 5D — Component transfers (expected, monitor)

- HEA-EMP, HEA-LID, HEA-BSH at G3PL: not separately tracked here. The 22-04-2026 OP Heal fill (11,500) requires components - Peter receives these as needed. AUS 08072026 brings 20,000 of each (15 Jul) for next-cycle fills. Care/Heal LCL (per POS Check) would pull components forward.
- ACC-RE5-BOT/LID/INN: not separately tracked. AUS 08072026 brings 5,000 each for next OP Remove 500ml fill.

---

## 3PL DEDUCTION CHECK (Kit alignment, last 14d)

(Excluding container arrival days)

| Kit | 3PL avg deduction/d | Shopify avg sales/d | Gap | Aligned? |
|---|---:|---:|---:|---|
| KIT-STA-2 | 21.9 | 22.1 | -0.2 | ✅ |
| KIT-COM-4 | 40.1 | 39.1 | +1.0 | ✅ |
| KIT-ULT-6 | 17.5 | 17.9 | -0.4 | ✅ |

**Kit deductions perfectly aligned with Shopify sales.** 3PL deduction logic working correctly. Stock sync didn't introduce kit-side issues.

---

## SELLING PERFORMANCE FLAGS

### Sales Spikes (7d > 30d by 50%, 30d ≥ 2/d)

| SKU | 7d | 14d | 30d | Spike vs 30d | Likely Cause |
|---|---:|---:|---:|---:|---|
| AUS-$85-GIF | 10.1 | 5.1 | 2.4 | +330% | GWP campaign launched 3 May (SKU is the GWP parent). |
| LIQ-SEN-4 (LO Glow) | 6.0 | 4.4 | 2.8 | +114% | Sensitive product line growth. Cover at 23d 3PL rate - **monitor**. |
| LIQ-SEN-2 (LO Base) | 8.1 | 6.5 | 4.2 | +93% | Sensitive product line growth. **OOS today.** |

LIQ-BAS-2 (Base) at 7d 27.6 / 30d 19.6 = +41% (under threshold). Per user: repeat buyers, benign.

### Sales Drops (7d < 30d by 40%, 30d ≥ 2/d)

| SKU | 7d | 14d | 30d | Drop | Notes |
|---|---:|---:|---:|---:|---|
| POW-AWA-050 | 0.7 | 1.2 | 2.7 | -73% | Long-tail colour cooling. |
| POW-NOT-065 (Not 2day) | 2.4 | 4.1 | 6.2 | -61% | |
| LIQ-SET (Liquids Set) | 1.0 | 0.6 | 2.4 | -58% | Bundle - independent of LO Base OOS (different liquids). Real demand drop. |
| POW-COT-CS11 | 1.0 | 1.6 | 2.3 | -57% | |
| POW-VIB-529 (Vibes) | 4.1 | 5.5 | 8.7 | -53% | |
| POW-PER-229 | 2.1 | 3.0 | 4.5 | -53% | |
| POW-DAY-025 | 3.1 | 3.7 | 6.6 | -53% | |
| POW-SWE-001 (Sweet Tooth) | 10.3 | 12.9 | 18.3 | -44% | Top seller cooling. |
| POW-MAR-009 | 3.1 | 3.1 | 5.4 | -43% | |

**Pattern:** the colour tail is softening in step with kit demand. ~10 colours in -40% range. Consistent with the W17→W18 -17% kit step-down. **Not a listing problem; demand softness.**

### Overperformers (>20% above model DSR)

LIQ-SEN-2 (Shopify 8.1/d vs model 9.1/d = -11%). LIQ-SEN-4 (6.0/d vs 7.8/d = -23%). Neither overperforms model in 7d/14d windows - but vs 30d trend they've doubled. Model itself is the relevant benchmark.

No kit overperforms model.

### Underperformers (>40% below model DSR)

All three kits: STA -35%, COM -50%, ULT -49%. **Persistent for 9-10 weeks.** Model is structurally above run-rate.

### Dead stock (in stock, 0 Shopify 14d)

Per 27 Apr Sales Analysis, Fire Collection (7 colours zero-sell 14d) was flagged - listing state still unverified. POW-COR-481 at 490 units, 0.5/d 14d 3PL deduction = 980d cover - effectively dead. Worth a Shopify-side audit.

### Sensitive variant signal

| | Shop 7d | Shop 14d | Shop 30d | Trend |
|---|---:|---:|---:|---|
| LIQ-SEN-2 (LO Base) | 8.1 | 6.5 | 4.2 | **+93% vs 30d** |
| LIQ-SEN-4 (LO Glow) | 6.0 | 4.4 | 2.8 | **+114% vs 30d** |
| LIQ-SOA-6 (Sensitive Glow) | 3.4 | 3.3 | 4.8 | -29% (mild drop) |
| LIQ-BAS-2 (Base) | 27.6 | 21.9 | 19.6 | +41% |

Sensitive Base + LO Glow growing. Base also up. **Possible driver:** seasonal nail-care shift, repeat buyers stocking up, or a CRO/listing change. Worth `#sale-announcements` / `#cro-team-meetings` cross-reference (out of scope for this run).

LIQ-SEN-2 + LIQ-SEN-4 combined growth **right as LO Base goes OOS** is an unfortunate timing intersection - express bridge via Sally is the only option short of accepting customer disappointment.

---

## KEY TAKEAWAYS

1. **W18 71.7/d is partly a single-day artefact** (28 Apr only 39 kits). Ex-Tuesday W18 = 76.4/d. Either way W18 < W17 86.4/d - the multi-week step-down (135→103→86→72) is real and post-Easter normalisation. **AUS 08072026 sizing should reflect ~75/d kit baseline**, not 191/d.

2. **Kit deductions perfectly track Shopify sales** (3PL avg ~14d ±0.5 of Shopify avg). 3PL deduction logic is working - data integrity is sound on the kit side.

3. **LIQ-SEN-2 OOS today + LIQ-SEN-4 7d +114%** = sensitive variants are the standout demand story. Express bridge from Sally (216 + 216 already in 22-04-2026 PO awaiting ship) is critical. If sustained, AUS 08072026 sizing should bump LO Base / LO Glow above current 432 each.

4. **AUS 08072026 kit-mix recommendation (no signal change vs 27 Apr):**
   - STA ~32/d × container window (sized to ~25-32/d)
   - COM ~50/d (currently 39/d 14d, 49.7/d 30d - mid-point)
   - ULT ~17-22/d (currently 17.9/d 14d - hold to 17.9/d size)
   - Plus ACC-LAB ~20k, ACC-THA ~15-20k, NO LIQ-HEA-5 (per Heal call), HEA-EMP/LID/BSH 20k each (already in).

5. **Cumulative colour gap reactivated.** The 6 colours that had caught up by 27 Apr (POW-DRE, POW-ROY, POW-JUS, POW-GOL, POW-BRE, POW-CRE) now show **~900-1,050 unit excess 3PL deductions each** - +5,841 units of new exposure across 6 SKUs since 27 Apr. POW-CRE-217 partly explained by PO 9 B360 PACKUP -250 variance. Cross-reference Greg's tracker + PO 9 Jake count when it arrives. **Likely a single reconciliation event or write-off pass**, but worth confirming.

6. **POW-ENE-484 cumulative gap dropped from +7,512 (27 Apr) to +966 (today)** - either a reconciliation captured the missing units, or the 16 Apr spike rolled toward the edge of the 30d window. Net positive.

7. **GWP AUS-$85-GIF accounts for today's 3PL spikes on POW-CLE-193 (203) and POW-SUN-SU015 (123).** Sustained at this rate, Sun Pop (1,706 stock) hits 14d cover. Watch.
