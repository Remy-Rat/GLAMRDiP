# 🇨🇦 CA Sales Data Analysis — 4 Jun 2026

## DATA FRESHNESS

- **Shopify latest:** 2026-06-02 (+1d lag — 4 Jun analysis runs to W22 full + 2 days of W23)
- **3PL latest:** 2026-06-04
- **POS MODEL re-pulled:** 4 Jun 12:38 AEST
- **Manual overrides:** None affecting Sales Analysis (CA 21062026 ETA correction applies to POS Check only)

---

## HEADLINE

- **Kit DSR 14d: 108.4/d.** Actual growth 1.57x vs 2.0x model = **-21% gap**. Three consecutive declining weeks since W20 peak.
- **W20 was the outlier, not the trend.** W19 +58% WoW → W20 +97% WoW (peak 151.9/d, parity) → W21 -22% → W22 -13% → W23 (2 days) -5%. Settled rate ~100-108/d = ~1.5x equivalent.
- **W22 (25-31 May): 103.4/d, -25.1% vs 138/d 2x model.** First non-spike week post-recovery; this is the true post-offer baseline.
- **Kit mix stable.** COM 67% / ULT 22% / STA 11% — model 68/19/13. ULT slightly stronger than model (+0.8pp), STA slightly weaker (-1.7pp). No substitution signal like UK is showing.
- **Liquid-to-kit ratio 0.32** — normal kit-vs-repurchase ratio; standalone liquid demand is small.

Per [[growth-factor-framing]] — flag the 21% gap as health-check info, don't recommend cutting orders. Per [[forecast-dsr-planning-rate]] — actual rate is the operational planning rate, model rate is the aspiration we order against.

---

## WEEKLY KIT TREND

| Week | Dates | Daily | vs Model | WoW | 4w avg |
|---|---|---:|---:|---:|---:|
| W15 | 6-12 Apr | 55.4 | -60% | — | 55.4 |
| W16 | 13-19 Apr | 52.1 | -62% | -6% | 53.8 |
| W17 | 20-26 Apr | 46.1 | -67% | -12% | 51.2 |
| W18 | 27 Apr-3 May | 49.0 | -65% | +6% | 50.6 |
| W19 | 4-10 May | 77.3 | -44% | **+58%** | 56.1 |
| W20 | 11-17 May | 151.9 | **+10%** ⭐ | **+97%** | 81.1 |
| W21 | 18-24 May | 118.6 | -14% | -22% | 99.2 |
| W22 | 25-31 May | 103.4 | -25% | -13% | 112.8 |
| W23 (2d) | 1-2 Jun | 98.5 | -29% | -5% | 118.1 |

**Pattern:** W19-W20 was an offer/promo-driven spike (+171% above prior 4-wk avg at W20). Post-spike decline is now in its 3rd consecutive week. Look at it two ways:

1. **As recovery from a peak:** Settled ~100-108/d is dramatically better than the pre-recovery baseline (46-55/d in W15-W18). The improvement is real and structural.
2. **As distance from model:** -25% vs 138/d 2x target. Container sizing decisions made at 2x are exposed if the trend stays here.

The right read is probably "both true" — CA stepped up meaningfully but didn't fully reach the model's aspiration. Watch W23 full-week + W24 to see if 100-108/d is the new floor or if it continues to slide.

---

## KIT DSR vs MODEL

| SKU | Model DSR (scaled) | Shop 14d | Gap |
|---|---:|---:|---:|
| KIT-STA-2 | 18 | 11.9 | **-34%** |
| KIT-COM-4 | 94 | 73.1 | **-22%** |
| KIT-ULT-6 | 26 | 23.4 | -10% |
| **Total** | **138** | **108.4** | **-21%** |

ULT is performing closest to model. STA is the weakest. No emergent substitution pattern (unlike UK STA→COM). Per [[ca-offer-gift-card]] — CA upsell moved from physical-SKU attach to gift card on 27 May, which removed the kit-level boost the W20 spike was riding.

---

## LIQUIDS — STANDALONE (kit consumption stripped)

| SKU | Model DSR | Shop 14d | Gap | Note |
|---|---:|---:|---:|---|
| LIQ-BAS-2 (Base) | 14 | 9.3 | -34% | Repurchase only — kits come pre-packed from CN |
| LIQ-GLO-4 (Glow) | 8 | 3.6 | -55% | |
| LIQ-SEA-3 (Seal) | 12 | 7.4 | -38% | |
| LIQ-BON-1 (Bond) | 6 | 2.2 | -63% | |
| LIQ-MAT-4 (Matte) | 6 | 2.7 | -55% | |
| LIQ-SOA-6 (Soak) | 4 | 1.9 | -52% | |
| LIQ-SEN-2 (Sens. Base) | 8 | 3.6 | -55% | |
| LIQ-SEN-4 (Sens. Glow) | 6 | 2.6 | -57% | |
| LIQ-HEA-5 (Heal) standalone | n/a (kit-adj) | 0.9 | — | Real Heal demand is 108.3/d kit-adjusted |

**POS MODEL DSR is materially overstated on every CA liquid.** Greg refresh batch (Recap action item) needs to land for:
- LIQ-BAS-2: 14 → ~9
- LIQ-GLO-4: 8 → ~4
- LIQ-SEA-3: 12 → ~7
- LIQ-BON-1: 6 → ~2
- LIQ-MAT-4: 6 → ~3
- LIQ-SOA-6: 4 → ~2
- LIQ-SEN-2: 8 → ~4
- LIQ-SEN-4: 6 → ~3

Net impact: this is why all the liquid cover numbers look comically high (>100d). The actual cover is even higher than the POS Check shows — confirming the "liquids don't need restocking before next container" thesis from prior reviews. Doesn't affect CN container sizing (liquids are pre-packed in kits from Sally) but does affect the read on local-fill cadence (Swift 120ml — 449d cover sustainable).

---

## REMOVE / BUNDLE BREAKDOWN

| SKU | Model DSR | Shop 14d | 3PL ded/d | Notes |
|---|---:|---:|---:|---|
| ACC-REM-500 (standalone) | 120 | 86.9 | 90.0 | Model overstated 38%. 3PL ≈ Shopify (small bundle uplift) |
| ACC-REM (120ml standalone) | 10 | 2.1 | 8.4 | Bundle deductions inflate 3PL rate |
| ACC-REM-BOW | 30 | 2.3 | 12.7 | Bundle deductions inflate 3PL rate (ACC-REM-BUN-1 + BUN-2 pull) |
| ACC-REM-BUN-1 (120ml+Bowl) | n/a | 5.2 | — | Bundle SKU |
| ACC-REM-BUN-2 (500ml+Bowl) | n/a | 4.4 | — | Bundle SKU — **down -58% 7d vs 30d** (500ml supply depleting) |

**Key signals:**
- ACC-REM-500 actual burn ~90/d (3PL) ≈ ~87/d (Shopify) — close alignment, no significant bundle effect.
- ACC-REM-BUN-2 is dropping fast (4.4/d 14d → 2.7/d 7d → was 6.5/d 30d). Consistent with depleting Remove 500ml stock making the bundle harder to fulfil.
- POS MODEL DSR for ACC-REM-500 (120/d) overstates the demand. Even at actual 90/d, OOS is in 5 days — but cover math throughout this review uses the actual 90/d, which is correct.

---

## SHOPIFY vs 3PL ALIGNMENT (deduction integrity)

| SKU | Shopify 14d | 3PL ded/d | Gap | Status |
|---|---:|---:|---:|---|
| KIT-STA-2 | 11.9 | 11.4 | -0.5 | ✅ Aligned |
| KIT-COM-4 | 73.1 | 71.1 | -2.0 | ✅ Aligned |
| KIT-ULT-6 | 23.4 | 23.2 | -0.2 | ✅ Aligned |
| LIQ-HEA-5 | 0.9 | 108.3 | +107.4 | Kit-adjusted (expected) |
| LIQ-BAS-2 | 9.3 | 10.8 | +1.5 | ✅ Aligned (LIQ-SET bundle) |
| LIQ-GLO-4 | 3.6 | 5.4 | +1.8 | ✅ Aligned |
| LIQ-SEA-3 | 7.4 | 9.0 | +1.6 | ✅ Aligned |
| LIQ-BON-1 | 2.2 | 3.5 | +1.3 | ✅ Aligned |
| LIQ-SEN-2 | 3.6 | 4.2 | +0.6 | ✅ Aligned |
| LIQ-SEN-4 | 2.6 | 4.0 | +1.4 | ✅ Aligned |
| ACC-REM-500 | 86.9 | 90.0 | +3.1 | ✅ Aligned (bundle uplift) |
| ACC-REM | 2.1 | 8.4 | +6.3 | Bundle uplift (BUN-1) |
| ACC-REM-BOW | 2.3 | 12.7 | +10.4 | Bundle uplift (BUN-1 + BUN-2) |

**Deduction integrity is clean.** All kit gaps within ±2/d. Liquid gaps consistent with LIQ-SET (1.4/d) + bundle pulls. No anomalous over-deductions on this run. No "oversell post-theme-change" pattern.

---

## COLOUR INTELLIGENCE

### Top 10 sellers (14d volume)
| # | SKU | 14d/d | % of colour total |
|---|---|---:|---:|
| 1 | POW-HEA-515 | 36.6 | 5.7% |
| 2 | POW-PIL-194 | 28.2 | 4.4% |
| 3 | POW-CLE-193 | 24.8 | 3.9% |
| 4 | POW-POS-184 | 23.6 | 3.7% |
| 5 | POW-TRA-452 | 19.4 | 3.0% |
| 6 | POW-CHA-011 | 16.6 | 2.6% |
| 7 | POW-MON-005 | 16.6 | 2.6% |
| 8 | POW-BAR-198 | 14.1 | 2.2% |
| 9 | POW-PEA-068 | 13.6 | 2.1% |
| 10 | POW-BLA-384 | 13.4 | 2.1% |

Top 10 = 32.4% of colour demand. Healthy long-tail.

### Sustained risers (7d vs 30d, min 2/d, accel >5%)
| SKU | 7d | 14d | 30d | Accel |
|---|---:|---:|---:|---:|
| **POW-DRE-D08** | 2.9 | 5.1 | 2.4 | **+21%** ⭐ |
| **POW-BLO-D07** | 2.9 | 5.2 | 2.5 | **+16%** ⭐ |
| POW-MYS-318 | 3.4 | 3.2 | 3.0 | +13% |
| POW-SUG-545 | 2.7 | 2.4 | 2.4 | +13% |
| POW-KIN-642 | 4.0 | 4.0 | 3.6 | +11% |
| POW-JET-206 | 2.9 | 3.3 | 2.7 | +7% |
| POW-BUB-516 | 12.0 | 11.9 | 11.3 | +6% |
| POW-NOT-065 | 6.3 | 6.5 | 6.0 | +5% |
| POW-HEL-387 | 6.3 | 6.2 | 6.0 | +5% |

**POW-DRE-D08 + POW-BLO-D07 are emerging breakout colours.** D-suffix per [[dippi-prefix-convention]] is a legit region-native code, not Nordic. Both went from 2.4-2.5/d in 30d to 5.1-5.2/d in 14d — doubled. Worth flagging as restock candidates for the next CN PO. Currently:
- POW-DRE-D08: not in 21062026 manifest, not in 30082026 manifest → **no inbound, only 7d data above projection**. Greg needs to add the model DSR.
- POW-BLO-D07: not in 21062026 manifest, not in 30082026 manifest → same.

**POW-CLE-193 ongoing high 3PL pull:** Shopify 14d = 24.8/d, but 3PL deducting 126.4/d (16d streak of 4-9x benchmark of 35). Per [[ca-offer-gift-card]] — this is the offer-attached colour pool, deducted at the warehouse when shipped as part of offer bundles. **Model DSR 172 is overstated** (set when offer attached at higher rate); real Shopify demand 25/d + offer pull ~100/d = 125/d combined. Stock 10,940 + 10,000 (21062026) + 10,600 (30082026) = comfortably resourced.

**POW-SUG-545 (Sugar Rush) sustained signal:** also flagged in UK as sustained overseller. Restock candidate — only 400 units in 30082026 (likely undersized given +13% accel).

### Sales drops (7d < 30d by 40%+)
| SKU | 7d | 30d | Drop |
|---|---:|---:|---:|
| POW-GLA-CS02 (Glacier Glow) | 0 | 1.3 | -100% |
| CA-POW-LIP-570 | 0 | 2.0 | -100% |
| CA-POW-ROS-522 | 0 | 2.0 | -100% |
| CA-POW-COB-G17 | 0 | 2.0 | -100% |
| CA-POW-BAL-521 | 0.1 | 3.0 | -97% |
| CA-POW-SEC-G15 | 0.1 | 2.9 | -97% |
| CA-POW-VAN-F01 | 0.1 | 2.8 | -96% |
| CA-POW-LIM-G13 | 0.1 | 1.6 | -94% |
| CA-POW-MAP-564 | 0.1 | 1.4 | -93% |
| CA-POW-POW-F17 | 0.3 | 4.0 | -92% |
| CA-POW-GOL-565 | 0.1 | 1.3 | -92% |
| CA-POW-AMB-572 | 0.4 | 1.7 | -76% |

**Pattern:** the CA-prefix SKUs are fading hard. These are the AU-prefix-style legacy SKUs from the early CA assortment. Same fade pattern observed in AUS (POW-COB-G17, POW-VAN-F01, POW-ROS-522, etc.). **Gav listing audit candidates** — likely de-list / merge with current naming.

POW-GLA-CS02 (Glacier Glow) is the one non-CA-prefix drop — but it was already flagged as OOS in the 20 May recap. Restocked on CA 21062026 (600 units). Expect rate to return post-arrival.

---

## DEAD-STOCK COUNTER

- **W22 active colours by velocity:**
  - 42 colours >5/d (high)
  - 74 colours >2/d (moderate)
  - 102 colours >1/d (active)
  - 167 colours >0/d (any sales)
  - **14 colours at zero** (14d trailing)
- 14d-zero count comparable to prior reviews (20 May: 21 dead SKUs). Slight improvement.
- The 14 zero-SKUs likely overlap with the CA-prefix legacy assortment (Gav audit).

---

## OFFER POOL — DEDUCTION SIGNATURES

Single-day 3PL deductions over benchmark in last 14d:

| Date | SKU | Deduction | Benchmark | Ratio |
|---|---|---:|---:|---:|
| 25 May | POW-CLE-193 | 212 | 35 | 6.1x |
| 13 May | POW-CLE-193 | 208 | 35 | 5.9x |
| 16 May | POW-CLE-193 | 203 | 35 | 5.8x |
| 16 May | ACC-NAI-MAT | 199 | 15 | 13.3x |
| 10 May | POW-CLE-193 | 194 | 35 | 5.5x |
| 12 May | POW-CLE-193 | 193 | 35 | 5.5x |
| 19 May | POW-CLE-193 | 192 | 35 | 5.5x |
| 13 May | POW-JUS-449 | 183 | 35 | 5.2x |
| 16 May | POW-JUS-449 | 177 | 35 | 5.1x |
| 14 May | POW-CLE-193 | 175 | 35 | 5.0x |
| 25 May | POW-JUS-449 | 172 | 35 | 4.9x |
| ... (more POW-CLE-193 / POW-JUS-449 days) | | | | |
| 19 May | ACC-NAI-MAT | 151 | 15 | 10.1x |

**Two clear offer-attached patterns:**
1. **POW-CLE-193 + POW-JUS-449** (Clear + Just Friends) — sustained 5-6x benchmark since 10 May. Both are core offer colours per Daniel 27 May summary ("Current Website Offer: Square tips, Gift Card, Clear, Just Friends"). 16-day streak above benchmark.
2. **ACC-NAI-MAT** (Mani Mat) — was 10-13x benchmark mid-May, now 0 (depleted, swapped out 27 May).

Per [[ca-offer-gift-card]] — physical-SKU attach has collapsed (the Mani Mat / Travel Bag / Tip allocations went to gift card on 27 May). But the COLOUR pool (Clear + Just Friends) is still pulling — that part of the offer is intact.

---

## WHAT NEEDS ACTION (Sales-driven)

### 🟡 This week

1. **Greg: POS MODEL DSR refresh batch.** Liquids overstated 30-60%; ACC-REM-500 overstated 38%; ACC-REM overstated 5x; ACC-REM-BOW overstated 13x. Also: ACC-TIP-ALM model 148/d is broken (real ~5/d). Doesn't change current operational decisions (the POS Check uses actual rates) but the sheet will keep showing misleading single-line cover figures until refreshed.
2. **Greg/Daniel: add POW-DRE-D08 + POW-BLO-D07 to model.** Both sustained risers +16-21% accel, doubled from 30d to 14d. Currently no POS MODEL DSR set. Restock candidates for next CN container.
3. **Gav/Remy: CA-prefix listing audit.** 7+ CA-POW-* SKUs at -90%+ vs 30d. Likely de-list candidates. Aligns with same fade pattern seen in AUS (per [[current-issues]] AU-prefix list).

### 🟢 Monitor

4. **Watch W23 full-week kit rate.** W22 -25% is the post-spike baseline; if W23 closes near 95-100/d we have a clean settled rate to size against. If it slides below 90/d, container sizing thesis (2x) needs revisiting.
5. **POW-SUG-545 (Sugar Rush) emerging globally.** Restock candidate flagged in both CA and UK reviews this cycle.
6. **POW-CLE-193 offer-pool depletion math.** At current 126/d 3PL combined rate, 10,940 stock = 87d cover. With CA 21062026 (+10,000 on 1 Jul), post-arrival cover ~150d at current rate — safe through Q3.

---

## NOTES FOR NEXT CYCLE

- W22 is the first clean post-spike data week. W23-W24 will tell us whether the CA recovery floor is 95/d or 110/d.
- The W20 single-week parity-level performance now looks unambiguously like a spike, not a sustained trend. Per [[growth-factor-framing]] still hold 2.0x model for ordering, but treat 105/d as the planning rate for 30-60 day operational decisions (cover math, fill sizing, etc).
- Heal kit-adjusted rate at 108.3/d cleanly matches kit total 108.4/d — so the kit-adjustment math is working as expected. Same should hold next cycle.
