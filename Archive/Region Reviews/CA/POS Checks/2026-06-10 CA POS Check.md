# POS Model Check — CA — 10 Jun 2026

## Data Freshness
- POS MODEL extracted 2026-06-10 11:11
- 3PL (B360) last valid date: 2026-06-10
- Shopify latest date: 2026-06-09 (+1 day lag)
- Growth factor: 2.0x (kit base 69/d → scaled 138/d)
- Kit DSR base: KIT-STA-2 = 9, KIT-COM-4 = 47, KIT-ULT-6 = 13

## Manual Overrides
- **CA 21062026 ETA:** sheet shows 9 Jul; user confirmed (4 Jun) Lily vessel lands 247 on 1 Jul. **Use 1 Jul** for all downstream cover math. Greg still owes sheet update (was 22 Jul on 4 Jun, partial fix to 9 Jul, real ETA 1 Jul).
- **Linda tip-fill items NOT making CA 21062026** (user 4 Jun). Treat ACC-TIP-COF 5,000 + ACC-TIP-SQU 1,500 + ACC-TIP-STI 200 + ACC-TIP-BAL 1,000 + ACC-TIP-ALM 1,000 + ACC-NAI-MAT 1,100 as **NOT INBOUND on 1 Jul.** Routing decision deferred per user 10 Jun.
- **Upsell switch Remove 500ml → 120ml + Bowl:** direction confirmed (user 10 Jun); operational flip not yet executed. Demand model below shows both pre-switch and post-switch outlooks.

## Stock Position — Key SKUs

Cover columns: **Cov(M) = stock / model_DSR × growth** | **Cov(A) = stock / 3PL 14d avg deduction**

### Kits
| SKU | Stock | Model DSR (2x) | Cov(M) | 3PL 14d/d | Cov(A) | Inbound (real) |
|---|---|---|---|---|---|---|
| KIT-STA-2 | 3,799 | 18.0 | 211d | 9.2 | 412d | +672 (21062026) |
| KIT-COM-4 | 5,580 | 94.0 | 59d | 64.8 | 86d | +1,988 (21062026) +4,256 (30082026) +2,800 (29092026) |
| KIT-ULT-6 | 2,500 | 26.0 | 96d | 21.1 | 119d | +1,008 (21062026) +784 (29092026) |
| **Kit total** | **11,879** | **138.0** | **86d** | **95.1** | **125d** | +3,668 (21062026) |

3PL and Shopify kit rates agree (Shopify 7d 84.5, 14d 94.2, 30d 113.5; 3PL 14d 95.1). No deduction-side anomaly. Cover well above target across the board.

### Liquids
| SKU | Stock | Model DSR (2x) | Cov(M) | 3PL 14d/d | Cov(A) | Inbound |
|---|---|---|---|---|---|---|
| LIQ-HEA-5 (Heal) | 4,224 | 142 (kit-adj) | 30d | 97.2 | **43d** | +6,500 Swift fill |
| LIQ-BAS-2 (Base) | 1,098 | 14 | 78d | 9.1 | 121d | +2,160 (21062026) |
| LIQ-GLO-4 (Glow) | 1,348 | 8 | 169d | 5.3 | 255d | +1,080 (21062026) |
| LIQ-SEA-3 (Seal) | 819 | 12 | 68d | 6.7 | 122d | +2,160 (21062026) +216 (29092026) |
| LIQ-BON-1 (Bond) | 896 | 6 | 149d | 2.9 | 306d | +1,080 (21062026) |
| LIQ-MAT-4 (Matte) | 1,136 | 6 | 189d | 2.7 | 419d | +2,808 (21062026) |
| LIQ-SOA-6 (Soak) | 813 | 4 | 203d | 2.7 | 300d | +4,104 (21062026) |
| LIQ-SEN-2 (Sens Base) | 613 | 8 | 77d | 3.6 | 172d | +216 +432 +216 |
| LIQ-SEN-4 (Sens Glow) | 515 | 6 | 86d | 3.0 | 172d | +216 +216 +216 |

All liquids comfortable. Heal at 43d actual cover vs Swift fill arrival 23 Jun – 2 Jul (13-22d away) = **15-30d margin before OOS at 247**.

### Remove products
| SKU | Stock | Model DSR (2x) | Cov(M) | 3PL 14d/d | Cov(A) | Inbound |
|---|---|---|---|---|---|---|
| **ACC-REM-500** | **339** | **120** | **2.8d** | **60.1** | **6d** | **+9,000 Swift fill** |
| ACC-REM (120ml) | 3,510 | 10 | 351d | 24.2 | 145d | +1,000 Swift fill |
| ACC-REM-BOW (Bowl) | 4,831 | 30 | 161d | 28.1 | 172d | +8,000 (21062026) |

ACC-REM-500 is the binding constraint. 6d cover at actual; Swift fill earliest arrival 23 Jun = ~13d away.

### Tips & accessories (offer-driven)
| SKU | Stock | 3PL 14d/d | Cov(A) | Real Inbound | Notes |
|---|---|---|---|---|---|
| ACC-TIP-BAL (Ballerina) | 422 | 65.3 | **6d** | **0** (Linda not making 21062026) | Current offer tip per Daniel 27 May |
| ACC-TIP-ALM (Almond) | 2,157 | 31.1 | 69d | **0** (Linda not making) | Daniel 4 Jun: switch off early, replace with Travel Bag |
| ACC-TIP-COF (Coffin) | 134 | 122.0 | **1d** | **0** (Linda not making) | Was the offer tip pre-27 May swap; 122/d 14d avg reflects pre-swap rate |
| ACC-TIP-SQU (Square) | 177 | 1.9 | 94d | **0** (Linda not making) | Off the offer |
| ACC-TIP-STI (Stiletto) | 397 | 1.0 | 397d | **0** (Linda not making) | Off the offer |
| ACC-NAI-MAT (Mani Mat) | 0 | 0 (post-swap) | n/a | **0** (Linda not making) | OOS since ~27 May; offer swapped |
| ACC-TRA-BAG (Travel Bag) | 347 | 77.3 | **4d** | 0 | Already burning fast pre-offer-switch; if switched in, OOS in days |

### Inserts & packaging
| SKU | Stock | 3PL 14d/d | Cov(A) | Inbound |
|---|---|---|---|---|
| ACC-INS | 19,344 | 92.4 | 209d | +5,760 +4,080 |
| ACC-LAB-CA | 23,821 | (NaN — B360 rule) | 109d at model 218 | +20,000 Mixam (~14-18 Jun) +1,300 reprint |
| ACC-THA | 29,352 | 125.9 | 233d | +11,200 +2,800 +5,600 |
| STO-BUB-BAG-L | 5,204 | 95.7 | 54d | +30,000 Swift fill |
| STO-MAI-2 | 8,659 | 33.6 | 257d | +3,300 (21062026) |
| STO-MAI-BAG-S | 8,619 | 33.6 | 256d | +3,000 (21062026) |
| STO-BUB-BAG-S | 0 | 0 | n/a | n/a — 247 supplies; excluded |

ACC-LAB-CA B360 deduction rule still NaN (Greg owes fix). Cover comfortable through Aug.

## Container / Order Status

### CA 21062026 (Birthday Sale, 40HQ) — **ETA 1 Jul** (sheet says 9 Jul, ignore)
Status: On the Way (per sheet). Sally near completion + Lily vessel closed 1 Jun / sailed 5 Jun / ETA warehouse 1 Jul per user 4 Jun. Days to arrival: **21d**.
Real manifest landing: 672 STA + 1,988 COM + 1,008 ULT + 2,160 Matte + 4,104 Soak + 2,160 Base + 1,080 Glow + 2,160 Seal + 1,080 Bond + 8,000 Remove Bowls + 11,200 THA + colours + packaging.
**Stripped from manifest** (Linda): 5k Coffin + 1.5k Square + 200 Stiletto + 1k Ballerina + 1k Almond + 1.1k Mani Mat.

### CA 30082026 — Ordering, completion 6 Jul, arrival 30 Aug
Placed 27 May (per Daniel). 40HQ at 2x DSR. Joel sign-off pending on free-gift qty (min 10k) + 6-12 new colour collections (status unknown per user). Sally 5-6w lead means new SKU window has closed; free-gift qty bump still possible.

### CA 29092026 — Ordering, completion 5 Aug, arrival 29 Sep
Status placeholder; numbers per Daniel earlier work.

### Swift Innovations 14-05-2026 (Local Fill)
Status: Ordering (POS MODEL). Real status: production day 7 of 14-21d window (started 4 Jun per user). Manifest: 6,500 LIQ-HEA-5 + 9,000 ACC-REM-500 + 1,000 ACC-REM + 30,000 STO-BUB-BAG-L. Earliest 247 receipt **23 Jun** (lead 14d + 5d transit), latest **2 Jul** (21d + 7d). Per [[swift-fill-lead-times]] 5-7d transit window confirmed.

### Mixam 14-05-2026 (Local Print)
Status: Ordering. Shipped 3 Jun (confirmed via Mixam email). ETA 247 **~14-18 Jun**. 20,000 ACC-LAB-CA. Cover safe through Aug.

## Local Fill Status

- **Swift 14-05-2026** — production day 7 of 14-21d. No update from Abhishek since 14 May invoice (27d silent). Worth a chase for confirmation production is running + target completion date.
- **No next Swift fill placed yet.** Post-fill cover math (Heal + Remove 500ml) in section 10a below — placement window likely mid-Aug.

## Stock-Out Forecast

### 🔴 Stockout before Swift fill arrives
| SKU | Stock | Rate (3PL 14d) | OOS in | Inbound arrives | Gap |
|---|---|---|---|---|---|
| ACC-REM-500 | 339 | 60.1/d | **6d** (16 Jun) | 23 Jun – 2 Jul | **-7 to -16d** |

Mitigation today: **execute the upsell switch** (user 10 Jun direction confirmed). Drops 500ml demand to Shopify standalone base (~25/d 7d, likely lower without upsell) → stock 339 / 15-20/d = **17-22d cover** = closes the gap on the earliest Swift arrival but stays tight against the latest.

### 🔴 Stockout already / imminent — Linda tips not inbound
| SKU | Stock | Rate (3PL 14d) | OOS in | Inbound (real) | Status |
|---|---|---|---|---|---|
| ACC-TIP-COF (Coffin) | 134 | 122/d (pre-swap) | <1d | 0 | Off-offer since 27 May; rate now near 0 — verify in Sales Analysis |
| ACC-TIP-BAL (Ballerina) | 422 | 65.3/d | **6d** | 0 | **CURRENT OFFER TIP** — needs route or rotation |
| ACC-TRA-BAG (Travel Bag) | 347 | 77.3/d | **4d** | 0 | Earmarked as next offer (Daniel 4 Jun) — already depleting fast |
| ACC-NAI-MAT (Mani Mat) | 0 | 0 (post-swap) | OOS | +1,100 (21062026 real — Linda not making) | Will arrive only via 30082026 (200 units) |

### 🟢 Safe
Everything else has 40d+ cover at actual rate with inbound where applicable.

## Cascading Arrival Projection (kit cover)

Using actual 3PL kit rate 95.1/d (14d avg).

| Stage | Kit stock | Cov(A) |
|---|---|---|
| NOW (10 Jun) | 11,879 | 125d |
| Post-21062026 (1 Jul, +3,668 kits) | 13,548 (after 21d burn at 95/d, then +3,668) | **155d** ⚠️ |
| Post-30082026 (30 Aug, +4,256 kits) | 12,108 → 16,364 | **180d** ⚠️ |
| Post-29092026 (29 Sep, +3,584 kits) | 12,580 → 16,164 | **177d** ⚠️ |

⚠️ all post-arrival levels exceed 100d target band. Per [[growth-factor-framing]] this is an observation, not a downsize trigger; flag for future container sizing.

If model demand actually arrives (138/d at 2x), post-21062026 cover is 98d — closer to target. The overstock risk is **conditional on actual demand staying below model**.

## Container Gap Analysis

### CA 21062026 (arrives 1 Jul) — gaps vs reality
| SKU | OL in real manifest | OOS risk before 1 Jul | Action |
|---|---|---|---|
| ACC-REM-500 | 0 (Swift fill carries it) | Yes (Swift earliest 23 Jun) | Upsell switch today |
| ACC-TIP-BAL | 0 (Linda not making) | Yes (6d) | Linda dispatch decision deferred per user; offer rotates |
| ACC-NAI-MAT | 0 (Linda not making) | Already OOS | Offer rotated |
| ACC-TRA-BAG | 0 | 4d at current rate | Tighten before promoting to offer |

### CA 30082026 (arrives 30 Aug) — known gaps
- Joel sign-off pending on free-gift (min 10k Travel Bag/Tray/Mat) + new colour collections. Status unknown.
- Sally 5-6w lead = new SKU additions effectively closed; free-gift qty bump still feasible.

## Local Fill Forecast — Next Swift Fill

Current Swift fill carries 6,500 Heal + 9,000 Remove 500ml + 1,000 Remove 120ml. Lands 23 Jun – 2 Jul.

### Heal (LIQ-HEA-5)
At kit-adj actual 97.2/d:
- Stock at fill arrival (assume 27 Jun midpoint, 17d burn): 4,224 - 17×97.2 = **2,572 units**
- Post-fill: 2,572 + 6,500 = 9,072 → **93d cover** at 97.2/d. Safe.
- Next fill needs to be placed when cover hits ~17d. At 97.2/d that's after burning 9,072 - 1,652 = 7,420 units = 76 days from arrival = **place next Swift fill ~mid-Sep**.

### Remove 500ml (ACC-REM-500)
At actual 60.1/d (pre-upsell-switch; will drop after switch):
- Stock at arrival (assume 27 Jun, 17d burn from today): goes OOS ~16 Jun, stays OOS to 27 Jun → 0 units.
- Post-fill: 0 + 9,000 = 9,000 → 150d cover at 60.1/d, or 360d at standalone 25.4/d post-switch.
- If upsell stays switched to 120ml + Bowl: next 500ml fill required when stock hits 17d at the lower rate. Could be a year out.

### Remove 120ml (ACC-REM)
Post-switch demand becomes the binding rate. Current 3PL avg 24.2/d but this includes the BUN-1 attach (already 36.7/d 7d Shopify). Real post-switch demand:
- Base BUN-1 + standalone = ~38.8/d 7d. Add upsell channel volume (~25/d transferred from Remove 500ml standalone, assuming customer behaviour transfers).
- **Estimated post-switch ACC-REM demand: ~60-70/d.**
- Stock at fill arrival: 3,510 - 17×60 = **2,490 units**
- Post-fill: 2,490 + 1,000 = 3,490 → **50-58d cover at 60-70/d.**
- 1,000 units in Swift fill is light for the new demand level — flag for next fill sizing.

### Remove Bowl (ACC-REM-BOW)
Total demand (BUN-1 + BUN-2 + standalone) at 3PL = 28.1/d 14d. Stock 4,831 + 8,000 (21062026, 1 Jul) = post-arrival 12,300 → 437d. Comfortable.

### Next Swift Fill Sizing Preview
Targeting Sep place / mid-Oct arrival:
| Scenario | Heal | Remove 500ml | Remove 120ml |
|---|---|---|---|
| Lean (~60d post-fill) | 6,000 | 4,000 (low if upsell off) | 4,000 |
| Recommended (~90d) | 9,000 | 6,000 | 6,000 |
| Conservative (~120d) | 12,000 | 8,000 | 8,000 |

Defer firm sizing decision until upsell switch behaviour clarifies.

## PO Recommendations / Place-By Dates

| Category | Place By | Notes |
|---|---|---|
| Swift fill #2 (Heal, Remove) | ~Mid-Aug (place) / Mid-Sep (lands) | Depends on next Butuo Remove bottles raw goods PO being placed by Joel |
| Butuo Remove bottles (raw goods for Swift fill #2) | Within 2-3 weeks | Daniel posted recommended PO 20 May; status unknown |
| ACC-LAB-CA next Mixam | Aug | 109d current + 20k inbound = ~190d post-arrival; no urgency |
| Next CN container | CA 29092026 placeholder placed; no new container needed | Kit cover >150d post-Aug arrival |

## What Needs Action

🔴 **CRITICAL (act today)**
- **Execute Shopify upsell switch Remove 500ml → 120ml + Bowl.** Direction confirmed by user; operational flip outstanding. 6d cover at current rate vs 13-22d to Swift fill arrival = OOS gap if switch doesn't happen. Without switch: stock out Tue 16 Jun.
- **ACC-TIP-BAL (Ballerina) offer tip — 6d cover, no real inbound on 21062026.** Plan per Daniel 4 Jun: rotate to Travel Bag. But ACC-TRA-BAG has 4d cover too. Need decision on what the offer is after Ballerina runs out.

🟡 **WARNING (act this week)**
- **Chase Abhishek (Swift)** for production confirmation + target completion date (27d silent since 14 May invoice). Don't wait for it to arrive without communication.
- **Joel sign-off on CA 30082026** free-gift qty / colour collections — Sally window has effectively closed for new SKUs; free-gift bump still feasible.
- **Greg housekeeping:** update CA 21062026 sheet ETA to 1 Jul (currently 9 Jul, was 22 Jul); fix ACC-LAB-CA B360 deduction NaN; refresh stale CA liquid DSRs (all 30-60% overstated per 4 Jun).
- **247 invoice 305815 query** (Remy 4 Jun) — chase Zaid (6d silent).

🟢 **MONITOR**
- Mixam ACC-LAB-CA arrival ~14-18 Jun.
- Kit overstock projection: post-30082026 = 180d cover. Per [[growth-factor-framing]] flag for future container sizing, not a downsize trigger.
- POW-CLE-193 + POW-JUS-449 sustained offer-pull continues (red flags 140-212/d through late May; tapering early Jun). Stock comfortable.

## Follow-Up Items

- [ ] Remy/Joel/Daniel: Execute Shopify upsell switch 500ml → 120ml + Bowl today
- [ ] Daniel: decision on offer tip after Ballerina runs out (Travel Bag too at 4d cover) — defer per user but operationally tight
- [ ] Remy: chase Abhishek (Swift) for production status + ETA
- [ ] Joel: sign off CA 30082026 free-gift qty + colour collections
- [ ] Joel/Vanessa: pay Zakka balance by ~17 Jun (7 days)
- [ ] Remy: chase Zaid on 247 invoice 305815 insert-rate query
- [ ] Daniel: chase Zaid on 247 SOP audit reply (8d silent)
- [ ] Greg: update CA 21062026 ETA to 1 Jul
- [ ] Greg: fix ACC-LAB-CA B360 deduction NaN
- [ ] Greg: refresh stale CA liquid DSRs (all 30-60% overstated)
- [ ] Remy: acknowledge 247 Apr rate sheet (22d stale)
- [ ] Gav: booklet-missing CX email rollout (30d stale)
