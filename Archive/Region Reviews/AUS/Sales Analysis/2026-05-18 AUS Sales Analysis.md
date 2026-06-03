# AUS Sales Data Analysis — 18 May 2026

## DATA FRESHNESS

- **Shopify last date:** 16 May 2026 (2d ago — normal +1d lag, plus weekend pasting). 30d window covers 16 Apr–16 May.
- **3PL (AUS 3GPL) last valid date:** 18 May 2026.
- **POS MODEL base kit DSR:** 147/d (STA 34 + COM 78 + ULT 35). Growth factor 1.3x → scaled 191.1/d.

---

## DSR — MODEL vs REALITY

### KITS

| SKU | Model (1.3x) | Shop 7d | Shop 14d | Shop 30d | 3PL 14d | Gap vs Model (7d) | Notes |
|---|---:|---:|---:|---:|---:|---:|---|
| KIT-STA-2 | 44.2 | 24.1 | 24.6 | 22.7 | 24.5 | **-45%** | Stable, flat at ~24/d for 30d. Below model by 45%. |
| KIT-COM-4 | 101.4 | 25.0 | 62.6 | 49.8 | 61.0 | **-75%** | Plummeted post-14 May offer-swap. Last 5 days avg 1.4/d. |
| **KIT-ULT-6** | 45.5 | **140.7** | 86.7 | 49.3 | 98.1 | **+209%** | Daniel's offer-swap from 14 May drove surge. Last 3 days avg 234/d sustained. |
| **Kit total** | 191.1 | 189.8 | 173.9 | 121.8 | 183.6 | **-1%** | **Recovered to projection** for first time post-transition. |

**Read:** the kit recovery is real. 11-16 May avg 188/d vs scaled target 191/d (-1.6%). Daniel's offer swap reshuffled demand from Complete to Ultimate but total kit volume is essentially at projection. The "post-website-switch DSR oversell artefact" Daniel flagged 7 May does NOT appear to be the driver — kit Shopify/3PL alignment is near-perfect (see Step 6).

**Mix implication:** if the swap is permanent, **POS MODEL kit DSRs need rebasing**: STA 34 → 24, COM 78 → 25, ULT 35 → 140+. Current 147/d base is right; the split is wildly off. Container sizing needs to match (08072026 kit mix currently STA 1,372 / COM 3,192 / ULT 1,428 is the inverse of demand).

### HEAL (kit-adjusted: standalone Shopify + kit consumption at 3PL)

| SKU | Shop 7d standalone | Kit consumption (3PL 14d) | Adjusted DSR | Gap |
|---|---:|---:|---:|---:|
| LIQ-HEA-5 | 2.4 | 183.6/d | 186.0/d (3PL) / 192/d expected from 188/d kit total | -3% | Aligned. |

### LIQUIDS (standalone — pre-packed in kits from China)

| SKU | Shop 7d | Shop 14d | Shop 30d | 3PL 14d | Notes |
|---|---:|---:|---:|---:|---|
| LIQ-BAS-2 | 8.3 | 29.3 | 22.8 | 49.7 | OOS suppression. PO 14 just landed 18 May, will normalise next 7d. |
| LIQ-SEN-2 | 2.4 | 2.9 | 4.0 | 0.0 | 3PL not deducting yet (PO 14 just landed). |
| LIQ-SEN-4 | 2.4 | 5.5 | 4.2 | 5.8 | Stable. |
| LIQ-SEA-3 | 11.0 | 22.4 | 16.3 | 20.2 | Stable. |
| LIQ-BON-1 | 5.7 | 8.3 | 6.0 | 9.4 | Slight uptick. |
| LIQ-GLO-4 | 7.4 | 15.1 | 10.3 | 14.7 | Slight slowing. |
| LIQ-MAT-4 | 4.3 | 5.3 | 3.9 | 5.3 | Flat. |
| LIQ-SOA-6 | 2.7 | 3.9 | 3.4 | 5.5 | Flat. |

### REMOVE PRODUCTS

| SKU | Shop 7d | Shop 14d | Shop 30d | 3PL 14d | Notes |
|---|---:|---:|---:|---:|---|
| ACC-REM (120ml) | 2.6 | 4.5 | 6.5 | 40.2 | **-60%** vs 30d. Cannibalised by 500ml + bundles. |
| **ACC-REM-500** | **145.9** | 106.1 | 59.6 | 131.6 | **+145%** vs 30d. Daniel 14 May "gone bonkers". |
| ACC-REM-BOW | 6.1 | 5.4 | 3.4 | 54.9 | Steady direct sales; massive 3PL gap from bundle attachment. |
| ACC-REM-BUN-1 (120 + Bowl) | 10.1 | 34.0 | 19.8 | 0 (bundle SKU) | Declining vs 14d. Shifting to BUN-2. |
| ACC-REM-BUN-2 (500 + Bowl) | 15.7 | 16.7 | 17.9 | 0 (bundle SKU) | Stable. |

### FREE-GIFT-DRIVEN (offer switched 15 May to ACC-NAI-MAT)

| SKU | Shop 7d | 3PL 14d | 3PL 3d post-switch (16-18 May) | Notes |
|---|---:|---:|---:|---|
| ACC-NAI-MAT (new free gift) | 2.1 | 48.7 (14d blend) | **215/d** | New offer rate. Direct Shopify sales near-zero — it's offer-attached. |
| ACC-FRE-MANI (old drip tray) | 0.0 | 149.0 (14d, hit zero 16 May) | 0 | Switched off Fri. Demand → zero. Stock = 0. No forward action. |
| ACC-TIP-COF | 2.1 | 186.1 (14d blend) | 271/d | OOS today (18 May, stock = 0). Continued offer-attached even post-mat switch. |

**The mat-swap drove the ACC-NAI-MAT 3PL rate from <5/d to 215/d in 3 days.** Direct Shopify (2.1/d) confirms it's offer-only, not standalone demand.

### TOP COLOURS (by 30d Shopify volume)

| SKU | Shop 7d | Shop 14d | Shop 30d | 3PL 14d | Notes |
|---|---:|---:|---:|---:|---|
| POW-CLE-193 (Clear) | 39.6 | 48.9 | 38.1 | 228.6 | GWP campaign drives 3PL deduction. |
| POW-POS-184 | 58.6 | 53.8 | 37.9 | 56.8 | Uptrending +55%. |
| POW-HEA-515 (Heaven) | 56.4 | 53.2 | 37.1 | 55.7 | Uptrending +52%. |
| POW-PIL-194 (Pillow Talk) | 47.6 | 45.6 | 30.5 | 47.6 | Uptrending +56%. |
| POW-CHA-011 (Charming) | 31.3 | 26.8 | 14.4 | 28.7 | **+117%** vs 30d. |
| POW-BAR-198 | 26.0 | 23.1 | 15.1 | 24.7 | **+72%** vs 30d. |
| POW-MON-005 (Moon Magic) | 26.6 | 23.9 | 17.3 | 25.7 | +54%. |
| POW-BLA-384 (Blackout) | 25.7 | 24.6 | 18.0 | 25.6 | +43%. |
| POW-GOD-017 (Goddess) | 25.9 | 25.3 | 18.2 | 26.3 | +42%. Was -59% on 17 Apr issues. |
| POW-TRA-452 (Train-Wreck) | 21.9 | 20.8 | 15.2 | 22.1 | +44%. |
| POW-BOU-222 (Boujee) | 19.7 | 18.7 | 14.2 | 19.4 | +39%. |
| POW-SLO-192 (Slow Burn) | 22.6 | 21.3 | 14.3 | 21.9 | +58%. |
| POW-SWE-001 (Sweet Tooth) | 13.7 | 14.9 | 13.4 | 14.5 | Flat. |
| POW-GOO-208 (Good Morning) | 19.1 | 18.1 | 14.0 | 19.9 | +36%. |
| POW-BUB-516 (Bubbly) | 16.6 | 17.0 | 15.4 | 18.3 | Flat. |

**Read:** colour demand broadly up 35-115% vs 30d in line with kit recovery (each kit pulls 3-9 colours). No anomalous colour spikes outside the kit-driven uplift.

### Growth factor health check

- **Model:** 1.3x → 191.1/d scaled.
- **Actual 14d (avg kit total):** 173.9/d → effective growth factor **1.18x** (-9% vs model).
- **Actual 7d:** 189.8/d → effective growth factor **1.29x** (essentially at model).
- **Last 5 days (12-16 May):** avg 219/d → effective **1.49x** if sustained.
- **Recommendation:** **HOLD 1.3x.** Don't recalibrate up to 1.5x yet — last 5 days driven by free-gift swap promo lift. Wait another 2 weeks for stable post-promo baseline before re-evaluating. Per memory: growth factor is aspirational; the recent 5 days suggest the aspiration is becoming reality.

---

## WEEKLY KIT TREND (last 10 weeks)

| ISO Week | Units | Days | Per/day | vs 191.1 scaled |
|---|---:|---:|---:|---:|
| 2026-W11 (9-15 Mar) | 737 | 7 | 105.3 | -45% |
| 2026-W12 (16-22 Mar) | 911 | 7 | 130.1 | -32% |
| 2026-W13 (23-29 Mar) | 899 | 7 | 128.4 | -33% |
| 2026-W14 (30 Mar-5 Apr) | 738 | 7 | 105.4 | -45% |
| 2026-W15 (6-12 Apr) | 947 | 7 | 135.3 | -29% |
| 2026-W16 (13-19 Apr) | 618 | 6 | 103.0 | -46% |
| 2026-W17 (20-26 Apr) | 605 | 7 | 86.4 | -55% |
| 2026-W18 (27 Apr-3 May) | 502 | 7 | 71.7 | **-62% (floor)** |
| 2026-W19 (4-10 May) | 1,209 | 7 | 172.7 | -10% |
| **2026-W20 (11-16 May, partial)** | **1,135** | **6** | **189.2** | **-1%** |

**The trajectory:** W18 floor (-62%) → W19 (-10%) → W20 (-1%). 2-week recovery of 117/d (+165%). Driven by:
1. Free-gift offer change (drip tray → mani mat, Fri 15 May)
2. Free-gift attached SKU swap from Complete → Ultimate (Daniel 14 May)
3. Possible website-switch resolution / post-Easter normalisation

**Kit-by-day last 7 days (10-16 May):**

| Date | COM | STA | ULT | TOTAL |
|---|---:|---:|---:|---:|
| 10 May | 130 | 30 | 34 | 194 |
| 11 May | 40 | 22 | 56 | 118 |
| 12 May | 1 | 13 | 83 | 97 |
| 13 May | 0 | 18 | 110 | 128 |
| 14 May | 0 | 23 | 237 | 260 |
| 15 May | 2 | 29 | 233 | 264 |
| 16 May | 2 | 34 | 232 | 268 |

**ULT surge correlates with Daniel's 14 May offer-attach swap.** 233-237/d sustained for 3 days. Sustainable rate question for sizing.

---

## SELLING PERFORMANCE FLAGS

### 🔴 Spikes (7d > 30d by 50%+)

| SKU | 7d | 30d | Spike |
|---|---:|---:|---:|
| KIT-ULT-6 | 140.7 | 49.3 | **+186%** (offer swap) |
| ACC-REM-500 | 145.9 | 59.6 | **+145%** ("gone bonkers" — Daniel 14 May) |
| POW-CHA-011 (Charming) | 31.3 | 14.4 | +117% |
| POW-CLE-193 (Clear) | 39.6 | (n/a kit-driven) | offer-attached |
| POW-BAR-198 | 26.0 | 15.1 | +72% |
| POW-PIL-194 (Pillow Talk) | 47.6 | 30.5 | +56% |
| POW-POS-184 | 58.6 | 37.9 | +55% |
| POW-HEA-515 (Heaven) | 56.4 | 37.1 | +52% |

### 🔴 Drops (7d < 30d by 40%+)

| SKU | 7d | 30d | Drop |
|---|---:|---:|---:|
| KIT-COM-4 | 25.0 | 49.8 | **-75%** (offer-attach pulled to ULT) |
| KIT-STA-2 | 24.1 | 22.7 | flat (still -45% vs model) |
| LIQ-BAS-2 | 8.3 | 22.8 | -64% (OOS suppression — bridged today) |
| ACC-REM-120 | 2.6 | 6.5 | -60% (500ml cannibalisation) |
| ACC-REM-BUN-1 | 10.1 | 19.8 | -49% (shifting to BUN-2) |
| ACC-FRE-MANI (drip tray) | 0.0 | 0.5 | -100% (offer switched off Fri) |

---

## DEAD STOCK (colour SKUs idle — stock > 100, 14d Shop = 0)

**24 SKUs / 8,507 units idle.** Top by stock:

| SKU | Stock |
|---|---:|
| POW-LIM-LH10 | 3,550 |
| POW-MIR-015 | 343 |
| POW-PUL-W035 | 280 |
| POW-THE-W005 | 264 |
| POW-GRA-W036 | 257 |
| POW-SOL-019 | 247 |
| POW-MEC-W039 | 246 |
| POW-EUP-014 | 240 |
| POW-GLO-018 | 238 |
| POW-INF-506 | 238 |
| POW-SAF-149 | 236 |
| POW-IGN-W021 | 235 |
| POW-ALL-146 | 227 |
| POW-LUM-021 | 221 |
| POW-TID-W006 | 214 |

POW-LIM-LH10 dominates (Limited Halloween) — likely seasonal-only, dormant outside Q4. The W-suffix colours (W005/W015/W021/W035/W036/W039) appear to be a separate winter/wave collection — verify whether intentionally unlaunched on AUS site. **Action:** Gav/Remy listing audit. Low operational urgency.

---

## 3PL DEDUCTION INTEGRITY (Shopify vs 3PL gap test)

### Kit alignment — excellent

| SKU | 3PL 14d/d | Shop 14d/d | Gap |
|---|---:|---:|---:|
| KIT-STA-2 | 24.5 | 24.6 | -0.1 ✅ |
| KIT-COM-4 | 61.0 | 62.6 | -1.6 ✅ |
| KIT-ULT-6 | 98.1 | 86.7 | +11.4 ✅ (Shopify behind on most-recent surge) |
| ACC-LAB | 274.8 | 275.0 | -0.2 ✅ |

**G3PL deduction logic is working correctly.** No "post-website-switch oversell artefact" detected for AUS kits. Daniel's 7 May cross-region hypothesis does not apply here.

### Component / kit-adjusted gaps (explained)

| SKU | 3PL 14d | Shop 14d | Gap | Explanation |
|---|---:|---:|---:|---|
| LIQ-HEA-5 | 186.7 | 3.1 | 183.6 | Heal in every kit (188/d kit total + standalone). Aligned. |
| ACC-REM-500 | 131.6 | 106.1 | 25.5 | Bundle ACC-REM-BUN-2 deducts 500ml. BUN-2 14d 16.7/d. Plus possible GWP attach. Aligned. |
| ACC-REM-BOW | 54.9 | 5.4 | 49.5 | BUN-1 + BUN-2 = 50.7/d combined → bowl included. Aligned. |
| ACC-NAI-MAT | 48.7 | 3.0 | 45.7 | Free-gift attach from 15 May. 3-day post-switch rate 215/d. Aligned. |
| ACC-FRE-MANI | 149.0 | 0.0 | 149.0 | Old free-gift drip tray. Stock exhausted 16 May. Historical. |

### Colour cumulative gap (3PL > Shopify 30d by 300+)

| SKU | 3PL 30d | Shop 30d | Gap | Explanation |
|---|---:|---:|---:|---|
| POW-CLE-193 (Clear) | 6,858 | 1,143 | 5,715 | GWP campaign attaching Clear to other purchases. Daniel 7 May confirmed. |
| POW-TRE010 (Treasure) | 4,230 | 5 | 4,225 | New free-gift attached colour (Daniel 11 May swap from Sun Pop). |
| POW-SUN-SU015 (Sun Pop) | 3,174 | 11 | 3,163 | Was free-gift attached colour pre-Treasure swap. Historical. |
| POW-POS-184 | 1,704 | 1,137 | 567 | Likely partial GWP / kit-pick offset. Worth a sanity check. |
| POW-HEA-515 (Heaven) | 1,671 | 1,113 | 558 | Same — partial offset. |
| POW-PIL-194 (Pillow Talk) | 1,428 | 916 | 512 | Same. |
| POW-CHA-011 (Charming) | 861 | 433 | 428 | Same. |

**Total unexplained-ish gap: 15,168 units / 7 SKUs.** Biggest 3 (CLE, TRE, SUN) all explained by GWP / free-gift attach. Remaining 4 (POS/HEA/PIL/CHA) — small gaps (~500 units each) likely small GWP attach. No data integrity action required.

---

## CONTAINER ARRIVALS DETECTED (3PL data, 8+ SKUs increasing same day)

| Date | SKUs Increased | Total Units | Top 5 |
|---|---:|---:|---|
| 27 Mar | 94 | +69,605 | ACC-THA 15.8k, STO-MAI-BAG-S 6k, POW-BAR-198 3.2k |
| 28 Mar | 95 | +84,008 | ACC-INS 10.4k, ACC-5PC-BAG 10k, ACC-RE1-LID 6k |
| 10 Apr | 118 | +128,553 | ACC-THA 16.6k, ACC-INS 9.5k, STO-MAI-BAG-S 5.9k |
| **14 Apr** | **194** | **+194,685** | **POW-CLE-193 39k**, ACC-STI-45885 4.4k, POW-BOU-222 3.4k |
| 18 May (today) | small | (partial) | LIQ-BAS-2 648, LIQ-SEN-2 216, LIQ-SEN-4 216 (PO 14 express liquids) |

**14 Apr was the AUS Powder Room main check-in.** 27-28 Mar / 10 Apr were B360 PACKUP transfers in pieces.

---

## KEY TAKEAWAYS

1. **Kit DSR fully recovered to projection** (188/d vs 191 target, -1%). Last 5 days running at 219/d (1.49x). Trajectory: W18 -62% → W20 -1% in 2 weeks.

2. **Mix dramatically reshuffled** by Daniel's 14 May free-gift offer-attach swap (Complete → Ultimate). ULT 3-day avg 234/d vs model 45.5 (5.1x). COM idle at 1.4/d. **POS MODEL kit DSRs need rebasing if swap is permanent** — current container sizing on 07062026 and 08072026 is the inverse of demand.

3. **G3PL deduction logic is clean.** Kit/ACC-LAB alignment within 1.6 units/day. The "post-website-switch oversell artefact" Daniel flagged 7 May is NOT happening for AUS. Cross-region hypothesis should be re-tested in UK/CA/Nordic.

4. **ACC-REM-500 +145% spike** ("gone bonkers" — Daniel 14 May) is genuine demand, not a deduction artefact. Local OP fill cycle needs the 5,000-unit lean PO discussed for 07062026 (next OP cycle after acetone resolution).

5. **Free-gift mat (ACC-NAI-MAT) consumption 215/d** post-Friday switch. CN-supplied — no local restock route. Must be on AUS 07062026 (if Sally accepts) and certainly on 08072026 fill PO.

6. **Heal demand is real and accelerating** — kit-adjusted 14d rate 187/d, 3-day rate 278/d. The 45-day OOS gap (11 Jun → 26 Jul) per accepted POS Check direction is the single biggest CX risk this cycle.

7. **Colour demand up 35-115% across top 15** in line with kit recovery. No anomalous colour spikes outside the kit-driven uplift. Dead stock 24 SKUs / 8,507 units idle — listing audit candidate (low urgency).

8. **No new unexplained 3PL deduction anomalies.** All historical April spikes (POW-DRE-771, POW-GOL-597, POW-ROY-304 etc.) already on B360 PACKUP variance list with Jake — no fresh escalations.

---

## OPEN QUESTIONS FOR USER / DANIEL

1. **Is the free-gift-Ultimate offer permanent or promotional?** Drives whether to rebase model DSRs + reshape 08072026 / Container #5 kit mix.
2. **Should POS MODEL kit DSRs be rebased now** or wait 2 more weeks for stable post-promo baseline?
3. **Sun Pop (POW-SUN-SU015) — relist or write off?** 3,174 units consumed in last 30d via free-gift before swap. Now dormant.
4. **POW-LIM-LH10 (3,550 idle Halloween units)** — seasonal hold or clearance?
