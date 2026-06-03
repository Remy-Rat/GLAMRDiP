# UK Sales Data Analysis - 28 Apr 2026

## DATA FRESHNESS

- **Shopify last:** 27 Apr 2026 (+1d lag, normal)
- **3PL tab (B360):** 28 Apr — but represents **frozen Packup stock**, not Fulfillable. No usable post-13 Apr deduction view from this tab.
- **POS MODEL:** updated 28 Apr (today). Growth factor 1.3x. Kit base 84/d → scaled 109.2/d.
- **Greg refresh confirmed:** Base + Glow DSR now kit-adjusted in POS MODEL (was standalone-only at 21 Apr). Heal already kit-adjusted previously.

**Caveat:** 3PL deduction integrity check is **blind on Fulfillable**. We have no Fulfillable deduction feed yet. All discrepancy work below is pre-13 Apr (B360) only. **Recommend Roisin export Fulfillable 14d deduction history.**

---

## DSR: MODEL vs REALITY

### Kits

| Kit | Model DSR (1.3x) | Shop 7d | Shop 14d | Shop 30d | Gap (14d vs 1.3x) |
|---|---:|---:|---:|---:|---:|
| Starter Kit (KIT-STA-2) | 13.0 | 11.0 | 10.7 | 13.3 | **-18%** |
| Complete Kit (KIT-COM-4) | 41.6 | 22.6 | 23.3 | 25.7 | **-44%** |
| Ultimate Kit (KIT-ULT-6) | 54.6 | 30.6 | 38.0 | 42.9 | **-30%** |
| **Total kits** | **109.2** | **64.2** | **72.0** | **81.9** | **-34%** |

**Effective actual growth: 0.86x.** Recommended (actual + 10%): 0.94x. Greg's 1.3x is now ~50% above the demand reality.

### Kit-Adjusted Liquids (Heal / Base / Glow)

| SKU | Model DSR (1.3x) | Standalone 14d | Kit-Adjusted 14d | Gap vs Model |
|---|---:|---:|---:|---:|
| Heal (LIQ-HEA-5) | 110.5 | 0.6 | 72.6 | -34% |
| Base (LIQ-BAS-2) | 135.2 | 23.4 | 95.4 | -29% |
| Glow (LIQ-GLO-4) | 122.2 | 7.4 | 79.4 | -35% |

The 14 Apr POS Check called out Base/Glow understatement (model 22 vs reality 90). Greg has now refreshed: model includes kit consumption. Use the kit-adjusted actual rates for cover calculations.

### Standalone Liquids (pre-packed in CN kits)

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap (14d) |
|---|---:|---:|---:|---:|---:|
| Seal (LIQ-SEA-3) | 15.6 | 9.4 | 9.5 | 9.0 | -39% |
| Bond (LIQ-BON-1) | 6.5 | 1.6 | 2.4 | 2.6 | -63% |
| Sensitive Glow (LIQ-SOA-6) | 6.5 | 1.6 | 1.4 | 1.7 | -78% |
| Liquids Matte (LIQ-MAT-4) | 7.8 | 1.9 | 2.3 | 3.0 | -71% |
| Sensitive Base (LIQ-SEN-2) | 0.0 | 0.0 | 0.0 | 0.0 | discontinued |
| Sensitive Liquid #4 (LIQ-SEN-4) | 0.0 | 0.0 | 0.0 | 0.0 | discontinued |

Sensitive line dormant. Bond + Sensitive Glow well below model — likely model is stale, not a sales problem.

### Remove Products

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap (14d) | Note |
|---|---:|---:|---:|---:|---:|---|
| Remove 120ml (ACC-REM) | 39.0 | 9.7 | 17.6 | 18.8 | -55% | Bundle effect (BUN-1) |
| Remove 500ml (ACC-REM-500) | 36.4 | 9.0 | 9.4 | 12.0 | -74% | Bundle effect (BUN-2) |
| Remove Bowl (ACC-REM-BOW) | 31.2 | 1.0 | 1.7 | 2.3 | **-95%** | Massive overstock — see flags |

### Top 10 Colours (14d)

| SKU | Model DSR | Shop 14d | Gap |
|---|---:|---:|---:|
| Cleo (POW-CLE-193) | 41.6 | 25.9 | -38% |
| Heart (POW-HEA-515) | 35.1 | 25.3 | -28% |
| Positive (POW-POS-184) | 36.4 | 21.0 | -42% |
| Pillow (POW-PIL-194) | 24.7 | 17.9 | -28% |
| Train-Wreck (POW-TRA-452) | 19.5 | 16.9 | -13% |
| Sweetheart (POW-SWE-001) | 22.1 | 16.2 | -27% |
| Bouquet (POW-BOU-222) | 24.7 | 15.6 | -37% |
| Harmony (POW-HAR-139) | 15.6 | 13.9 | -11% |
| Younger (POW-YOU-256) | 19.5 | 13.9 | -29% |
| Peachy (POW-PEA-068) | 15.6 | 13.3 | -15% |

Top sellers all -10% to -40%. Total colour DSR 14d: 613.7/d. Per-kit colour pick is averaging ~6 colours / kit (= 72 kits × 6 = 432/d expected from kits + ~180/d standalone = ~612/d — checks out).

---

## WEEKLY KIT TREND

| Week | Dates | Kits | Daily | vs Model (109.2/d) | Notable |
|---|---|---:|---:|---:|---|
| W10 | 02-08 Mar | 543 | 77.6 | **-29%** | Mailer shortage |
| W11 | 09-15 Mar | 585 | 83.6 | -23% | |
| W12 | 16-22 Mar | 473 | 67.6 | -38% | Complete Kit OOS at B360 |
| W13 | 23-29 Mar | 610 | 87.1 | -20% | |
| W14 | 30 Mar-05 Apr | 583 | 83.3 | -24% | Pre-transition |
| W15 | 06-12 Apr | **671** | **95.9** | **-12%** | Best week, transition imminent |
| W16 | 13-19 Apr | 585 | 83.6 | -23% | Fulfillable go-live mid-week |
| **W17** | **20-26 Apr** | **441** | **63.0** | **-42%** | **First clean Fulfillable week. Worst week in 8.** |
| W18 | 27 Apr (1d) | 70 | 70.0 | -36% | Mon (kits typically run hotter mid-week) |

**Read:** W17 is the single biggest concern in this analysis. Three possible drivers:
1. **Post-Easter normalisation** — late March / early April had Easter promo lift; W17 may be a return-to-baseline.
2. **Fulfillable transition friction** — colour OOS backorders (~50), bundle mis-picks, returns redirection. Customer-side disruption could have nudged conversions down.
3. **Macro slowdown** — same pattern showing in AUS (0.86x sustained) and CA (0.66x). UK held above the others until now.

Not enough data to attribute. Watch W18 closely. If W18 lands at 75-90/d, the W17 dip is normalisation. If W18 tracks W17 at <70/d, it's structural.

### Kit Mix (14d)

| Kit | Daily | Share | Model Share | Variance |
|---|---:|---:|---:|---|
| Starter Kit | 10.7 | 15% | 12% | +3pp |
| Complete Kit | 23.3 | 32% | 38% | -6pp |
| Ultimate Kit | 38.0 | 53% | 50% | +3pp |

Ultimate-heavy mix continues. The 21 Apr Recap had Ultimate at 52% — now 53%, holding. Implication: **Birthday Sale (UK 02072026) and UK 02082026 should weight Ultimate ahead of Complete** if mix sustains.

---

## REALISTIC DAYS COVER (Fulfillable only)

(See POS Check for full table. Summary of urgent items.)

| SKU | Stock | Actual DSR | Cover | Flag |
|---|---:|---:|---:|---|
| Base (LIQ-BAS-2) | 242 | 95.4/d | 3d | 🔴 saved by Chemence 30 Apr |
| Glow (LIQ-GLO-4) | 460 | 79.4/d | 6d | 🔴 saved by Chemence 30 Apr |
| Starter Kit (KIT-STA-2) | 223 | 10.7/d | 21d | 🟡 5-week gap to UK 03062026 |
| Just Friends (POW-JUS-449) | 31 | 8.4/d | 4d | 🔴 |
| Crush (POW-CRU-090) | 40 | 8.7/d | 5d | 🔴 |
| Over It (POW-OVE-487) | 60 | 7.4/d | 8d | 🔴 nothing on order |
| Bubbly (POW-BUB-516) | 79 | 6.3/d | 13d | 🔴 |
| Goddess (POW-GOD-017) | 79 | 6.6/d | 12d | 🔴 |
| Fairytale (POW-FAI-308) | 84 | 5.8/d | 14d | 🔴 nothing on order |
| Not 2day (POW-NOT-065) | 87 | 5.8/d | 15d | 🔴 nothing on order |
| Peachy (POW-PEA-068) | 141 | 13.3/d | 11d | 🔴 |

---

## CONTAINER ARRIVALS DETECTED (3PL data — pre-transition only)

The B360 tab shows two "arrival-shaped" events post-cutover:
- **14 Apr** — 194 SKUs, +2,409 units. ACC-LAB +253, ACC-THA +253, STO-MAI-2 +156. **Likely a stocktake reconciliation or B360 transfer prep**, not a real container.
- **16 Apr** — 15 SKUs, +15 units. Marginal — noise.

No container arrivals at Fulfillable visible in this data. **3PL data here is not reflecting Fulfillable activity.**

---

## INVENTORY DISCREPANCIES (PRE-TRANSITION ONLY)

All single-day flag dates are 17 Mar - 6 Apr. These are pre-Fulfillable, at B360. The pattern matches the AUS-style "single-day spike" that needed Greg's reconciliation:

| Date | SKU | Deduction | Benchmark | Likely Explanation |
|---|---|---:|---:|---|
| 04 Apr | Slow Burn (POW-SLO-192) | 5,707 | 35 | Stock adjustment / count |
| 25 Mar | Creme Brulee (POW-CRE-217) | 5,694 | 35 | Stock adjustment / count |
| 16 Apr | STO-MAI-BAG-S | 3,565 | 330 | B360 Packup transfer prep |
| 25 Mar | Seal / Base / Glow | 1,663 / 1,657 / 1,657 | 60-90 | Same-day large adjustment |
| 17-22 Mar (multiple) | 13 colours +1,000 each | 1,003-1,104 | 35 | Same as AUS pattern — stock adjustments |
| 27 Mar - 06 Apr | 3 more colours +1,000 each | ~1,030 | 35 | Same |

**These are explained as B360-side stock adjustments / writeoffs / Packup prep.** Not unexplained shrinkage. Cumulative gap test isn't useful here because the SKUs are now part of the frozen 288,898 Packup units.

**Action:** Once Fulfillable deduction data is available, run the same flag analysis against post-13 Apr period. **Until then, integrity is unverified post-transition.**

---

## SELLING PERFORMANCE FLAGS

### Sales Spikes (7d > 30d by 50%+)

| SKU | 7d | 14d | 30d | Spike vs 30d | Note |
|---|---:|---:|---:|---:|---|
| POW-VEL-119 (Velvet) | 1.9 | 1.5 | 0.8 | **+137%** | Low base, possible launch / refresh |
| ACC-NAI-WIP (Nail Wipes) | 1.1 | 1.3 | 0.6 | +83% | Standalone uplift |
| POW-FRI-778 (Frisky) | 2.0 | 2.1 | 1.1 | +82% | Cross-region — also AUS top performer |
| **LIQ-BAS-2 (Base) standalone** | **20.3** | **23.4** | **11.6** | **+75%** | Notable — see below |
| POW-ICE-266 (Iced) | 4.0 | 4.5 | 2.6 | +54% | |

**LIQ-BAS-2 standalone +75%** is the most interesting signal. Base standalone Shopify demand has nearly doubled vs 30d average. Hypotheses:
- Customers reordering Base (refill cycle hit) → consistent with Base being the most-used liquid
- Promotional pricing on standalone Base (worth checking #sale-announcements)
- Genuine velocity increase from existing customer base

Check `#sale-announcements` and `#cro-team-meetings` for any Base-specific change in last 7-10 days.

### Sales Drops (7d < 30d by 40%+)

| SKU | 7d | 14d | 30d | Drop | Note |
|---|---:|---:|---:|---:|---|
| Brewing (POW-BRE-109) | 0.0 | 0.0 | 1.3 | **-100%** | Check listing — likely OOS or delisted |
| Cotton (POW-COT-030) | 0.0 | 0.0 | 3.1 | **-100%** | Likely OOS / removed |
| Vibrant (POW-VIB-529) | 0.0 | 0.0 | 1.9 | **-100%** | Likely OOS / removed |
| Eve (POW-EVE-019) | 0.1 | 0.8 | 1.1 | -91% | |
| Radiant (POW-RAD-043) | 0.1 | 0.6 | 1.1 | -91% | |
| Scarlet (POW-SCA-155) | 0.4 | 0.7 | 1.2 | -67% | |
| Jelly (POW-JEL-SU018) | 0.4 | 0.8 | 1.2 | -67% | |
| Cottoncandy (POW-COT-CS11) | 0.4 | 0.7 | 1.1 | -64% | |
| Ghost (POW-GHO-771) | 0.7 | 1.1 | 1.9 | -63% | |
| Square Tips (ACC-TIP-SQU) | 2.3 | 4.1 | 5.6 | -59% | |
| **Remove Bowl (ACC-REM-BOW)** | 1.0 | 1.7 | 2.3 | -57% | Overstock issue compounds |
| Imagine That (POW-IMA-264) | 2.0 | 2.6 | 4.1 | -51% | |
| **Remove 120ml (ACC-REM)** | 9.7 | 17.6 | 18.8 | -48% | Significant — see below |
| Sugar (POW-SUG-545) | 0.9 | 1.4 | 1.7 | -47% | |
| Lace (POW-LAC-196) | 1.7 | 2.4 | 3.2 | -47% | |

**Remove 120ml dropped 48% in 7d.** That's notable — Remove 120ml is a kit-adjacent essential. Possible drivers:
- Customers shifted to Remove 500ml (better value)
- Bundle ACC-REM-BUN-1 promotion ended
- Site listing issue
- Liquipak out-of-stock messaging on the website?

Worth a 5-minute Shopify check to confirm Remove 120ml is live and not OOS-flagged.

### Dead Stock (in stock, 0 Shopify 14d)

| SKU | Units | Likely Explanation |
|---|---:|---|
| POW-HOL-022 (Holly) | 200 | Christmas — dormant |
| POW-YUL-007 (Yule) | 200 | Christmas — dormant |
| POW-CAN-016 (Candle) | 199 | Christmas — dormant |
| POW-CAN-D103 (Candle D) | 199 | Christmas — dormant |
| POW-CHA-047 (Charcoal) | 198 | possibly seasonal |
| POW-REI-008 (Reindeer) | 198 | Christmas — dormant |

Total: 1,194 units, 6 SKUs. All look like 2024/Christmas colours not currently in active rotation. Confirm with Marketing whether to clear via discount or hold for Q4 relaunch.

### Liquids Set (LIQ-SET) Bundle

7d: 0.1 / 14d: 0.1 / 30d: 0.2. Effectively zero. Negligible drag on individual liquid stock.

### Sensitive Base Signal

LIQ-BAS-2 (Base): 23.4/d (100%). LIQ-SEN-2 (Sensitive Base): 0/d. Sensitive line is fully dormant — confirmed discontinued.

---

## KEY TAKEAWAYS

1. **W17 -42% is the single biggest signal.** First clean post-transition week. Worst kit week in 8 weeks. Watch W18 - if <70/d, this is structural, not normalisation.
2. **Greg has refreshed Base + Glow DSR to kit-adjusted in POS MODEL.** The 22 vs 90 understatement that's been live for 4 weeks is fixed. Use the new kit-adjusted figures going forward.
3. **Effective growth factor 0.86x — POS MODEL set at 1.3x.** 50% disconnect. Future container quantities should be sized against reality (or accept building overstock buffer).
4. **Base standalone +75% in 7d** — interesting signal. Worth checking sale / CRO context. Could explain part of the 75/d kit-adj rate vs lower expectation.
5. **Remove 120ml -48% in 7d** — material drop, check Shopify listing health.
6. **3 colours at -100% (Brewing / Cotton / Vibrant)** — likely OOS or delisted on the site. Verify and either restock-flag or accept removal.
7. **Top-seller colours stocking out before UK 03062026:** Peachy (8 May), Goddess (9 May), Bubbly (10 May), Train-Wreck (14 May), Sincere (18 May). Tied to the kit-mix concentration — every Ultimate kit picks 9 colours.
8. **Remove Bowl: 5,278 units, 1.7/d. Overstock at >3,000d.** Don't add to any future container until 2027. Past flag, now confirmed.
9. **Dead stock 1,194 units** in 6 Christmas colours — Marketing decision: discount or hold.
10. **Fulfillable deduction integrity remains unverified** — request 14d export from Roisin to enable proper data integrity check next review.
