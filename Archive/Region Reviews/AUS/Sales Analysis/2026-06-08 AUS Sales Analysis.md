# 🇦🇺 AUS Sales Analysis - 8 Jun 2026

## DATA FRESHNESS
- Shopify last date: 2026-06-07 (1 day lag, expected).
- 3PL last valid date: 2026-06-08 (today).
- POS MODEL UPDATED: 2026-06-08 (today AM).
- Growth factor: 1.3x global. Kit base 147/d → scaled 191.1/d.

## DSR: MODEL vs REALITY

### KITS
| SKU | Model | Scaled | Shop 7d | Shop 14d | Shop 30d | Gap vs Scaled (14d) |
|---|---|---|---|---|---|---|
| KIT-STA-2 | 34.0 | 44.2 | 18.4 | 20.1 | 23.1 | -54% |
| KIT-COM-4 | 78.0 | 101.4 | **160.1** | 152.6 | 82.3 | **+51%** |
| KIT-ULT-6 | 35.0 | 45.5 | 0.0 | 6.2 | 83.4 | -86% |
| **Combined** | **147.0** | **191.1** | **178.5** | **178.9** | **188.8** | **-6%** |

**The combined kit rate is stable** at 178-191/d across the last 6 weeks. **Mix is fully distorted by substitution:**
- KIT-COM-4 7d 160/d vs 30d 82/d (+95%) - customers buying COM because ULT/STA are OOS.
- KIT-ULT-6 7d 0 because stock = 1 (literally OOS).
- KIT-STA-2 drifting down as stock runs thin (82 units / 20/d = 4d cover).

### Kit mix last 14d (actual % vs model %)
| Kit | Actual share | Model share | Delta |
|---|---|---|---|
| KIT-STA-2 | 11% | 23% | -12pp |
| KIT-COM-4 | **85%** | 53% | **+32pp** |
| KIT-ULT-6 | 3% | 24% | -21pp |

Substitution from ULT/STA into COM is the dominant flow. This matches memory note [[aus-kit-substitution]] - Ultimate kits manually fulfilled for Complete orders and vice versa.

### HEAL (kit-adjusted)
| Component | Rate |
|---|---|
| LIQ-HEA-5 standalone Shopify 14d | 3.4/d |
| All kits Shopify 14d (× 1 Heal per kit) | 179.0/d |
| **Kit-adjusted DSR** | **182.4/d** |
| POS MODEL DSR | 184.6/d |
| Variance | -1% (model accurate) |

Heal demand fully tracks the kit selling rate. 2,831 stock / 182/d = **15.5 days cover → OOS ~24 Jun**. OP local fill expected to land late this week + 7d transit = ~mid-late next week (per user: Peter finishing this week, email follow-up). Lands BEFORE container 22 Jun.

### LIQUIDS (standalone — pre-packed in kits from China)
| SKU | Model | Shop 7d | Shop 14d | Shop 30d | 3PL 14d | Note |
|---|---|---|---|---|---|---|
| LIQ-BAS-2 | 0 | 23.4 | 21.4 | 20.1 | 23.4 | Model says 0 (kit-internal) but real standalone 21-23/d |
| LIQ-SEN-2 | 0 | 8.4 | 8.2 | 6.5 | 9.1 | Sensitive standalone 8/d |
| LIQ-SEN-4 | 7.8 | 5.6 | 5.0 | 4.5 | 5.8 | Model OK |
| LIQ-GLO-4 | 26.0 | 18.4 | 13.7 | 12.3 | 14.9 | Model 90% overstated |
| LIQ-SEA-3 | 44.2 | **31.0** | 22.7 | 19.1 | 24.3 | **7d +62% vs 30d - spike** |
| LIQ-BON-1 | 16.9 | 9.1 | 7.6 | 6.8 | 8.4 | Model 100% overstated |
| LIQ-SOA-6 | 13.0 | 6.6 | 4.9 | 4.8 | 5.4 | Model 140% overstated |
| LIQ-MAT-4 | 10.4 | 5.3 | 3.9 | 4.2 | 3.9 | Model 165% overstated |

**Sensitive Base signal:** LIQ-SEN-2 / LIQ-BAS-2 ratio = 8.2 / 21.4 = 38% of standalone Base. Stable.

### REMOVE / TIPS / MAT
| SKU | Model | Shop 7d | Shop 14d | Shop 30d | 3PL 14d | Note |
|---|---|---|---|---|---|---|
| ACC-REM | 19.5 | 5.6 | 4.9 | 4.0 | 7.8 | Massively oversupplied (6,523 stock) |
| ACC-REM-500 | 149.5 | 165.3 | 158.8 | 159.2 | 163.1 | Model accurate; 14d cover |
| ACC-REM-BOW | 0 | 0.3 | 0.3 | 3.9 | 1.3 | Bundle-attached; standalone almost dead |
| ACC-NAI-MAT | 0 | 0.3 | 0.6 | **1.6** | **76.0** | **3PL >> Shopify - $85-gift offer attach decoded** |
| ACC-TIP-BAL | 0 | 0.9 | 1.4 | 2.0 | **75.1** | **Same offer-attach pattern** |
| ACC-TIP-SQU | 14.3 | 6.9 | 5.0 | 4.8 | 37.4 | Square Tips offer attach decayed since 19 May |
| ACC-TIP-STI | 2.6 | 0.6 | 0.7 | 1.1 | 0.8 | Dead - 245d cover |
| ACC-TIP-COF | 0 | 0.0 | 0.0 | 0.6 | 0.1 | Dead |
| ACC-TIP-ALM | 19.5 | 11.0 | 8.6 | 8.0 | 8.9 | Below model |

### BUNDLES (Shopify-only deductions)
| SKU | 7d | 14d | 30d | Note |
|---|---|---|---|---|
| ACC-REM-BUN-1 (120ml+Bowl) | 0.0 | 0.6 | 5.5 | Collapsed - ACC-REM-BOW OOS |
| ACC-REM-BUN-2 (500ml+Bowl) | 0.6 | 1.0 | 9.3 | Cooling - bowl OOS again |
| LIQ-SET (6-liquid set) | 0.1 | 0.5 | 0.5 | Steady |

### TOP 15 COLOURS by 14d Shopify
| SKU | 14d/d | 7d/d | 30d/d | 3PL 14d | Note |
|---|---|---|---|---|---|
| POW-CLE-193 (Clear) | 208.4 | 223.3 | 226.4 | 227.6 | $85-gift offer-pool [[aus-85-gift-offer-attaches]] |
| POW-HEA-515 | 57.3 | 57.0 | 58.9 | 57.0 | Healthy |
| POW-POS-184 | 51.1 | 52.7 | 55.3 | 51.5 | Healthy |
| POW-PIL-194 | 44.9 | 41.3 | 48.0 | 44.9 | Healthy |
| POW-BAR-198 | 27.1 | 26.1 | 27.5 | 26.9 | Healthy |
| POW-GOD-017 | 25.6 | 28.1 | 26.6 | 25.4 | Healthy |
| POW-CHA-011 | 24.6 | 25.6 | 29.1 | 25.0 | Healthy |
| POW-MON-005 | 24.4 | 26.1 | 25.6 | 24.6 | Healthy |
| POW-BLA-384 | 22.4 | 22.9 | 24.6 | 22.5 | Healthy |
| POW-TRA-452 | 22.0 | 23.6 | 22.7 | 22.1 | Healthy |
| POW-SLO-192 | 21.1 | 21.7 | 22.1 | 21.1 | Healthy |
| POW-GOO-208 | 20.6 | 22.3 | 21.0 | 20.6 | Healthy |
| POW-EMB-602 | 20.4 | 19.6 | 21.5 | 20.4 | Healthy |
| POW-BUB-516 | 20.1 | 19.9 | 20.5 | 20.3 | Healthy |
| POW-BOU-222 | 19.9 | 21.4 | 20.8 | 19.6 | Healthy |

POW-CLE-193 + POW-TRE010 / POW-SUN-SU015 / POW-CAN-D103 remain the $85-gift offer-attach pool per memory.

## GROWTH FACTOR REALITY CHECK
- Model base: 147/d (STA 34 + COM 78 + ULT 35)
- Scaled @ 1.3x: 191.1/d
- Actual 14d kit total: 178.9/d
- Actual growth: 178.9 / 147 = **1.22x**
- **Gap: 6% below scaled target** (W23/W24 sit at -6 to -7% vs scaled)
- Recommended growth (actual × 1.1): 1.34x → still defensible to hold 1.3x.

Per [[growth-factor-framing]] and [[forecast-dsr-planning-rate]]: hold 1.3x as planning rate. Trend is mostly stable, not deteriorating - W22 -6%, W23 -7%, W24 (in flight) -7%. Three weeks at ~178-180/d is the current floor. Will become a risk only if W25 dips below 170/d.

## WEEKLY KIT TREND (last 8 weeks)
| Week | Total | Per day | vs Scaled (1.3x) | Notes |
|---|---|---|---|---|
| Apr 13-19 (W16) | 618 | 88.3 | -54% | Pre $85-gift offer |
| Apr 20-26 (W17) | 605 | 86.4 | -55% | Floor |
| Apr 27 - May 3 (W18) | 502 | 71.7 | -62% | Floor |
| May 4-10 (W19) | 1,209 | 172.7 | -10% | $85-gift offer kicks in |
| May 11-17 (W20) | 1,388 | 198.3 | **+4%** | At target |
| May 18-24 (W21) | 1,343 | 191.9 | 0% | At target (peak) |
| May 25-31 (W22) | 1,256 | 179.4 | -6% | First step back |
| **Jun 1-7 (W23)** | **1,250** | **178.6** | **-7%** | Stabilising at ~179/d, mailer drag visible |

**Three weeks at 179-192/d is the new structural rate.** $85-gift offer drove the recovery and is sustaining demand. Below-target gap is small enough to ignore (within model noise per [[growth-factor-framing]]).

## REALISTIC DAYS COVER (model vs actual)
| SKU | Stock | Model DSR | Cov(M) | Actual DSR | Cov(A) | Flag |
|---|---|---|---|---|---|---|
| KIT-STA-2 | 82 | 34 | 2d | 20.1 | 4d | 🔴 |
| KIT-COM-4 | 1,335 | 78 | 13d | 152.6 | 9d | 🔴 |
| KIT-ULT-6 | 1 | 35 | 0d | 6.2 (suppressed) | 0d | 🔴 OOS |
| LIQ-HEA-5 | 2,831 | 184.6 | 15d | 182.4 | 16d | 🔴 |
| LIQ-BAS-2 | 0 | — | — | 21.4 | OOS | 🔴 |
| LIQ-SEN-2 | 0 | — | — | 8.2 | OOS | 🔴 |
| LIQ-SEA-3 | 1,563 | 44.2 | 35d | 22.7 | 69d | 🟢 (7d spike to 31/d worth watching) |
| LIQ-GLO-4 | 223 | 26 | 9d | 13.7 | 16d | 🟡 OOS ~24 Jun |
| LIQ-MAT-4 | 1,774 | 10.4 | 171d | 3.9 | 452d | 🟢 oversupplied |
| ACC-REM-500 | 2,414 | 149.5 | 16d | 158.8 | 15d | 🔴 |
| ACC-LAB | 6,147 | 364 | 17d | 258.4 | 24d | 🟡 gated on Joel paying Avi |
| ACC-INS | 11,567 | 195 | 59d | 179.0 | 65d | 🟢 |

## CONTAINER ARRIVALS DETECTED

Last 60 days: no major check-ins from CN containers. The 9-14 Apr cluster was the B360 PACKUP arrival series (Feb-Apr transition). Since then:
- 18 May: PO 14 / AUS 05052026 express liquids landed (per [[Current Issues]]).
- 5 Jun: PO 17 (AUK Logistics bubble mailers) - confirmed via 6 Jun STO-BUB-BAG-L jump from 0 to 1,949.

Next expected:
- 22 Jun: AUS 09052026 container (kits + colours + liquids + 6,840 ACC-REM-BOW + 6k STO-BUB-BAG-L)
- 10 Jul: AUS 07062026 v2 (+5,668 kits, +5,400 LIQ-MAT-4, +17,228 ACC-REM-500, +22k STO-BUB-BAG-L, +25k CARE, +5,400 MAT)

## INVENTORY DISCREPANCIES (30d cumulative 3PL > Shopify)
| SKU | 3PL 30d (est) | Shopify 30d | Gap | Cause |
|---|---|---|---|---|
| ACC-NAI-MAT | 2,280 | 48 | +2,232 | **Explained — $85-gift offer attach** ([[aus-85-gift-offer-attaches]]) ~79% attach rate. Decoded. Now collapsing post-pivot. |
| ACC-TIP-BAL | 2,252 | 59 | +2,193 | **Explained — current offer tip from late May.** Same kit-attach mechanism. Will fully collapse once Travel Bag pivot lands. |
| KIT-COM-4 | 4,644 | 2,470 | +2,174 | **Explained — substitution.** Customers ordering ULT/STA fulfilled with COM at G3PL. Burns COM stock without matching Shopify SKU. |
| ACC-TIP-SQU | 1,123 | 145 | +978 | **Explained — Square Tips offer attach decay** (52% attach from 19 May, decaying through Jun). |

All four cumulative gaps are explained by either substitution or offer-attach mechanics. **No unexplained discrepancies this week** — data integrity is clean.

## 3PL DEDUCTION CHECK (Shopify vs 3PL alignment)
Excluding container arrival days, kit aggregate:
- Shopify 14d kit total: 179/d
- 3PL 14d combined kit deductions: ~179/d (per extract output)
- **Gap: <2/d, aligned**

3PL deduction process working correctly on kits. The COM-specific gap is substitution-driven (kit-line type swap at picking).

## SELLING PERFORMANCE FLAGS

### Sales Spikes (7d > 30d × 1.5)
| SKU | 7d | 14d | 30d | Spike |
|---|---|---|---|---|
| KIT-COM-4 | 160.1 | 152.6 | 82.3 | **+95%** (substitution-driven, not real demand spike) |
| ACC-PRO-DRI (Pro Drill) | 5.3 | n/a | 2.7 | +93% |
| LIQ-HEA-5 std | 4.9 | 2.7 | 2.8 | +73% (low base, possibly noise) |
| ACC-NAI-LIN | 5.4 | n/a | 3.2 | +70% |
| ACC-BRU | 3.7 | n/a | 2.3 | +64% |
| **LIQ-SEA-3 (Seal)** | **31.0** | 22.7 | 19.1 | **+62%** — worth watching, stock 1,563 / 31 = 50d still safe |
| POW-SOR-113 | 3.9 | n/a | 2.5 | +52% |

KIT-COM-4 spike is **artefact** of ULT/STA substitution, not a real campaign effect.

### Sales Drops (7d < 30d × 0.6)
| SKU | 7d | 30d | Drop |
|---|---|---|---|
| KIT-ULT-6 | 0.0 | 83.4 | -100% (OOS-suppressed, not demand drop) |
| ACC-REM-BUN-1 | 0.0 | 5.5 | -100% (bowl OOS) |
| AUS-$85-GIF | 0.0 | 6.2 | -100% (offer SKU - rotating?) |
| AU-POW-VAN-F01 | 0.3 | 7.0 | -96% — legacy AU-prefix colour fading |
| AU-POW-BAL-521 | 0.6 | 10.0 | -94% — legacy |
| AU-POW-POW-F17 | 0.7 | 10.8 | -93% — legacy |
| AU-POW-LIP-570 | 0.6 | 8.2 | -93% — legacy |
| AU-POW-SEC-G15 | 0.7 | 9.6 | -93% — legacy |
| AU-POW-ROS-522 | 0.6 | 7.4 | -92% — legacy |
| AU-POW-COB-G17 | 1.9 | 8.0 | -77% — legacy |
| ACC-REM-BOW | 0.3 | 3.9 | -93% (OOS-suppressed) |

10+ AU-prefix legacy colours fading 70-95%. This is the listing-audit candidate set already known to Gav (per prior recap), now showing in the data. **Pure listing artefact, not real demand drop.**

### Overperformers (>20% above model DSR)
- KIT-COM-4 +95% (substitution)
- LIQ-SEA-3 +50% above scaled model (31/d vs scaled 57.5/d) - wait that's below model. Actually the 7d spike +62% vs 30d but still below model.

### Underperformers (>40% below model DSR)
- KIT-STA-2 -55% vs scaled (substitution-affected)
- KIT-ULT-6 -86% (OOS)
- LIQ-GLO-4 -47%
- LIQ-BON-1 -50%
- LIQ-SOA-6 -62%
- LIQ-MAT-4 -62%

These all match the known [[pos-check-dsr-labels]] pattern - model DSRs were last manually refreshed pre-W19 recovery and don't reflect current customer mix.

### Dead stock (in-stock SKUs with 0 Shopify 14d)
ACC-TIP-COF (0 stock, dead anyway), ACC-TIP-STI (636 stock, 0.7/d - 890d cover), LIQ-MAT-4 (1,774 / 3.9 = 452d).

## MATTE DEEP DIVE (user-flagged "might not have enough")

### LIQ-MAT-4 (Matte liquid)
- Stock: 1,774
- Shopify 7d/14d/30d: 5.3 / 3.9 / 4.2 per day
- 3PL 14d deduction: 3.9/d
- **At current rate: 452 days cover. Massively safe.**
- Inbound: AUS 07062026 +5,400 (arrival 10 Jul). Post-arrival: 7,000+ units = 5+ years cover at current rate.

**The current-rate read is: we have heaps.**

### ACC-NAI-MAT (Mani Mat)
- Stock: 0
- Shopify 7d: 0.3/d (collapsed post offer pivot)
- 3PL 14d: 76/d (residual offer-attach burn)
- Inbound: only 200 on AUS 04092026 (4 Sep)

**However:** if Matte (LIQ-MAT-4) becomes the next offer-attach SKU (replacing Mani Mat / Ballerina via the $85-gift mechanic), demand will jump 10-20x:
- Mani Mat at peak attach: 211/d 7d → 1,774 stock = 8d cover
- If Matte becomes the offer tip/attach at 50-100/d burn: 1,774 / 75 = ~24d → OOS ~2 Jul (8 days before 07062026 lands)
- Post-07062026 (10 Jul) +5,400: 5,400 / 75 = 72d cover, fine.

**If the offer pivot becomes Matte, the pre-arrival window is the risk window** - 8 days OOS gap between ~2 Jul stockout and 10 Jul container.

If Matte is NOT becoming the next offer, current inbound is overkill (5 years cover).

Flag this for Daniel to clarify intended offer-attach SKU for the post-Ballerina period.

## KEY TAKEAWAYS

1. **Kit selling structurally stable at 178-192/d** (1.21-1.31x), well above $85-gift launch floor of 86/d. Hold 1.3x growth.
2. **KIT-COM-4 +95% spike is substitution, not demand** - real combined kit DSR is 179/d, not 192/d. Don't over-react to the COM number.
3. **No unexplained inventory discrepancies this week.** All cumulative gaps explained by substitution or offer-attach.
4. **AU-prefix legacy colours fading hard** (10+ at -75 to -95%). Listing audit needed - already with Gav.
5. **LIQ-SEA-3 (Seal) 7d spike +62%** — small in absolute terms (31/d vs 19/d) but worth watching for trend. Stock 1,563 = 50d safe regardless.
6. **Matte (LIQ-MAT-4) stock vs demand is the question for Daniel:** if it becomes the next offer-attach SKU, current 1,774 + 5,400 (10 Jul) = ~30 days at offer-pace 75/d burn before further restock needed. If staying as a standalone colour, we have 5+ years cover.
7. **POS MODEL DSRs for non-kit liquids are stale** (40-160% overstated). Greg refresh outstanding.
