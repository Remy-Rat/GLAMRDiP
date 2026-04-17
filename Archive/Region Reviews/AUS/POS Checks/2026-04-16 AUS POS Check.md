# POS MODEL CHECK — AUS — 16 Apr 2026

## DATA FRESHNESS

- **POS MODEL last updated:** 16 Apr 2026
- **3PL data last valid:** 16 Apr 2026 (today)
- **Shopify data last valid:** 15 Apr 2026 (1-day lag)
- **ShipHero exports:** Not provided — running on POS MODEL + 3PL tab only. No confirmed/pending/quarantined split.
- **Growth factor:** 1.3x (147 base kit DSR → 191.1 scaled)
- **Kit DSRs (model):** STA 34 → 44.2 | COM 78 → 101.4 | ULT 35 → 45.5
- **Vessels:** 16 days express, 30 days standard

---

## GROWTH FACTOR HEALTH CHECK

| Metric | Value |
|---|---|
| Model growth factor | 1.3x |
| Model base kit DSR | 147.0/d (STA 34, COM 78, ULT 35) |
| Model scaled kit DSR | 191.1/d |
| **Actual 14d kit DSR** | **124.3/d** (STA 35.7, COM 61.9, ULT 26.7) |
| Actual 7d kit DSR | 124.6/d (STA 35.6, COM 63.3, ULT 25.7) |
| **Actual growth factor** | **0.85x** |
| Gap vs scaled target | **35.0% below** |

**vs previous (14 Apr):** was 0.83x / 36.5% below → now 0.85x / 35.0% below. Marginally narrowing.

**Weekly kit trend:**

| Week | Dates | Daily Rate | Trend |
|---|---|---:|---|
| W10 | 2-8 Mar | 95.1/d | |
| W11 | 9-15 Mar | 105.3/d | ↑ |
| W12 | 16-22 Mar | 130.3/d | ↑ |
| W13 | 23-29 Mar | 128.4/d | → |
| W14 | 30 Mar-5 Apr | 105.4/d | ↓ |
| W15 | 6-12 Apr | 135.3/d | ↑ |
| W16 | 13-15 Apr (3d) | 101.0/d | ↓ partial week |

- Kit selling volatile — ranges from 95 to 135/d. Not trending toward the 191 target.
- At model rate (191.1/d): every SKU cover is ~35% shorter than at actual rate. Ordering decisions based on inflated demand.
- Not recommending lowering the growth factor, but flagging: **current stock cover at actual selling gives ~35% more runway than the model suggests.** Future container quantities for COM and ULT should be reviewed given persistent oversupply.

---

## KIT-ADJUSTED DSR VALIDATION

### LIQ-HEA-5 (Heal) — kit-adjusted

| Metric | Rate |
|---|---|
| Shopify standalone | 2.7/d |
| Kit consumption (1 per kit × 124.3 kits/d) | 124.3/d |
| Kit-adjusted DSR | **127.0/d** |
| 3PL deduction rate | 146.4/d |
| POS MODEL DSR | 184.6/d |

- 3PL deduction (146.4/d) higher than calculated kit-adjusted (127.0/d) — includes some inventory adjustments or picks beyond standard formula.
- POS MODEL DSR (184.6/d) uses the 1.3x growth factor, overstating consumption.
- **Using 3PL deduction rate (146.4/d) for cover calculations** as it captures actual warehouse throughput.
- Stock: 10,998 → **75d at 3PL rate, 87d at kit-adjusted rate**

### ACC-INS (Instructions) — kit-adjusted

- Stock: 19,556 at 136.6/d 3PL deduction → **143d cover**. Healthy.

---

## STOCK POSITION

Running without ShipHero data. Using POS MODEL G3PL ON HAND. B360 Packup and PO 5/6 checked in 14 Apr — this is a clean snapshot.

### DSR Methodology
Showing both 14d and 30d Shopify rates. Where 30d is materially higher than 14d, the SKU likely had OOS days in the last 14 days depressing the average — flagged and 30d used for forecasting. 3PL deduction rate shown where it captures bundle/kit consumption not visible in Shopify.

### Kits

| SKU | Product | G3PL OH | Shop 14d | Shop 30d | 3PL Ded/d | Best Rate | Cover | Δ vs 14 Apr |
|---|---|---:|---:|---:|---:|---:|---:|---|
| KIT-STA-2 | Starter Kit | 1,319 | 35.7/d | 33.0/d | 38.8/d | **38.8/d** | **34d** | -52 units |
| KIT-COM-4 | Complete Kit | 5,164 | 61.9/d | 62.5/d | 67.4/d | **67.4/d** | **77d** | -101 units |
| KIT-ULT-6 | Ultimate Kit | 2,964 | 26.7/d | 28.3/d | 25.5/d | **28.3/d** | **105d** | -48 units |

- STA still the constraint. 34d cover at 3PL rate, stocks out ~19 May.
- COM & ULT comfortable but overstocked vs 45-75d target.

### Liquids

| SKU | Product | G3PL OH | Shop 14d | Shop 30d | 3PL Ded/d | Best Rate | Cover | OOS Flag |
|---|---|---:|---:|---:|---:|---:|---:|---|
| LIQ-HEA-5 | Heal | 10,998 | 2.7/d | 3.8/d | 146.4/d | **146.4/d** | **75d** | Kit-adj (3PL) |
| LIQ-BAS-2 | Base | 725 | 17.6/d | 29.6/d | 23.8/d | **29.6/d** | **24d** | **14d depressed by OOS** |
| LIQ-SEN-2 | LO Base | 123 | 1.2/d | 2.0/d | 3.1/d | **3.1/d** | **40d** | 14d depressed |
| LIQ-GLO-4 | Glow | 930 | 14.1/d | 17.5/d | 22.5/d | **22.5/d** | **41d** | 3PL faster |
| LIQ-SEN-4 | LO Glow | 199 | 0.6/d | 2.5/d | 2.0/d | **2.5/d** | **80d** | 14d depressed |
| LIQ-SEA-3 | Seal | 2,622 | 18.3/d | 24.2/d | 24.5/d | **24.5/d** | **107d** | 14d depressed |
| LIQ-BON-1 | Bond | 1,387 | 7.3/d | 8.9/d | 8.5/d | **8.9/d** | **156d** | |
| LIQ-MAT-4 | Matte | 1,992 | 5.5/d | — | — | **5.5/d** | **362d** | |
| LIQ-SOA-6 | Soak | 667 | 6.4/d | 6.3/d | 11.7/d | **11.7/d** | **57d** | 3PL faster |

- **Base is worse than 14d alone suggests.** 30d Shopify rate is 29.6/d vs 14d of 17.6/d — Base was OOS or near-OOS during the 14d window. At 29.6/d, stocks out **10 May** (was reporting 16 May on 14d rate alone). 20-day gap before AUS 09052026.
- Heal comfortable at 75d but **no inbound on any future container** — new fill PO needs placing this week.
- Glow at 41d — stocks out ~27 May, 3d before AUS 09052026.
- Several liquids (LO Base, LO Glow, Seal) show 14d DSR depressed by recent OOS. 30d rates are more reliable for these.

### Accessories & Remove Products

| SKU | Product | G3PL OH | Shop 14d | Shop 30d | 3PL Ded/d | Best Rate | Cover | Δ vs 14 Apr |
|---|---|---:|---:|---:|---:|---:|---:|---|
| ACC-LAB | Labels Booklet | 3,563 | — | — | 241.8/d | **241.8/d** | **15d** | -333 units |
| ACC-REM-BOW | Remove Bowl | 1,617 | 75.4/d | 21d | 43.8/d | **37d** | -60 units |
| ACC-REM-500 | Remove 500ml | 3,731 | 98.8/d | 38d | 69.2/d | **54d** | -93 units |
| ACC-REM | Remove 120ml | 7,685 | 33.8/d | 227d | 25.7/d | **299d** | -37 units |
| ACC-NAI-WIP | Wipes | 263 | 6.5/d | 40d | 3.6/d | **73d** | -2 units |

- **ACC-LAB at 15d is compliance-critical.** Stocks out ~1 May. Avi Printing PO was placed 24 Mar — no delivery confirmation in 23 days. Must chase immediately.
- ACC-REM-BOW: Model DSR overstated (75.4 vs 43.8 3PL). Bundle effect inflates 3PL rate too (Shopify standalone only 4.1/d). Real consumption driven by ACC-REM-BUN-1 + ACC-REM-BUN-2 bundles.

### Colours — Critical (<45d model cover)

| SKU | Colour | G3PL OH | Model DSR | Cover (M) | Shopify 14d | Inbound |
|---|---|---:|---:|---:|---:|---|
| POW-BOR-355 | Bordeaux Nights | 105 | 6.5/d | 16d | 0/d | AUS 08072026 +600 (15 Jul) |
| POW-HOT-568 | Hot Gossip | 111 | 6.5/d | 17d | 0/d | AUS 08072026 +600 (15 Jul) |
| POW-RED-165 | Red Mischief | 136 | 6.5/d | 21d | 0/d | AUS 08072026 +600 (15 Jul) |
| POW-SPI-144 | Spicy Sangria | 143 | 6.5/d | 22d | 0/d | AUS 08072026 +600 (15 Jul) |
| POW-GAR-656 | Garnet Games | 176 | 6.5/d | 27d | 0/d | AUS 08072026 +600 (15 Jul) |
| POW-ALL-146 | All Eyes On Me | 230 | 6.5/d | 35d | 0/d | AUS 08072026 +600 (15 Jul) |
| POW-INF-506 | Inferno Hour | 238 | 6.5/d | 37d | 0/d | AUS 08072026 +600 (15 Jul) |
| POW-CRU-328 | Crushin Hard | 971 | 22.1/d | 44d | 17.4/d | AUS 09052026 +1,800 |
| POW-BLU-ZGD22 | Blue Moon | 514 | 11.7/d | 44d | 0.3/d | AUS 09052026 +1,200 |

- **7 Fire Collection colours: all show 0 Shopify sales in 14d.** Either these aren't live on the site yet, or they had a 14d dead period. Model assigns 6.5/d to each. If demand is real, they all stock out before AUS 08072026 (15 Jul) with 54-73d gaps. If demand is ~0, they're fine. **Need to verify listing status on Shopify.**
- Blue Moon: OOS on website but 514 units at G3PL (flagged last review). Still needs website action.
- Bubbly & Goddess: demand collapse noted last review — still monitoring.

### 24 colours with 0 Shopify sales (14d)
Includes Fire Collection, plus: Aurora, Dawning, Enigma, Euphoria, Glow Up, Gravity, Ignite, Luminance, Mecha, Mirage, Pulse, Solstice, The Queen, Tidal, and duplicate Blue Moon SKUs. Some may be delisted or awaiting launch.

---

## SHOPIFY vs 3PL ALIGNMENT

| SKU         | 3PL Ded/d | Shopify/d |    Gap | Status                                                 |
| ----------- | --------: | --------: | -----: | ------------------------------------------------------ |
| KIT-STA-2   |      38.8 |      35.7 |   +3.1 | ALIGNED                                                |
| KIT-COM-4   |      67.4 |      61.9 |   +5.5 | 3PL FASTER                                             |
| KIT-ULT-6   |      25.5 |      26.7 |   -1.2 | ALIGNED                                                |
| LIQ-HEA-5   |     146.4 |       2.7 | +143.7 | Expected — kit-adjusted (3PL includes kit consumption) |
| LIQ-BAS-2   |      23.8 |      17.6 |   +6.2 | 3PL FASTER                                             |
| LIQ-GLO-4   |      22.5 |      14.1 |   +8.4 | 3PL FASTER                                             |
| ACC-REM-500 |      69.2 |      33.9 |  +35.3 | Bundle effect (ACC-REM-BUN-2)                          |
| ACC-REM-BOW |      43.8 |       4.1 |  +39.7 | Bundle effect (both Remove bundles)                    |

- Base and Glow showing 3PL consuming faster than Shopify standalone — these are inside every kit from China (1x each), so the 3PL deduction includes kit picks. This is expected but means Base is depleting at ~24/d, not the 17.6/d Shopify rate.
- Remove products heavily inflated by bundle picks at 3PL.

---

## PACKAGING & INSERTS

| SKU | Product | Stock | Ded/d | Cover | Benchmark | Max Day | Flag |
|---|---|---:|---:|---:|---:|---:|---|
| STO-BUB-BAG-L | Bubble Mailer | 12,428 | 202.8/d | **61d** | 435 | 449 | 1 red flag (6 Apr) |
| STO-BUB-BAG-S | Bubble Liquid Pocket | 13,529 | 183.0/d | **74d** | 130 | 569 | Spikes but high stock |
| STO-MAI-BAG-S | Small Satchel | 19,938 | 78.1/d | **255d** | 330 | 237 | Safe |
| STO-MAI-2 | Small Box | 17,377 | 80.7/d | **215d** | 330 | 236 | Safe |
| ACC-INS | Instructions | 19,556 | 136.6/d | **143d** | 435 | 283 | Safe |
| ACC-THA | Thank You Card | 32,954 | 242.0/d | **136d** | 735 | 615 | Safe |
| ACC-LAB | Labels Booklet | 3,563 | 241.8/d | **15d** | 735 | 615 | **CRITICAL** |

- **ACC-LAB at 15d is the only packaging concern.** Everything else has 60+ days.
- STO-BUB-BAG-L had one red flag day (449 vs 435 benchmark on 6 Apr) — likely a high-kit-order day. Not systemic.

---

## CONTAINER / ORDER STATUS

### OP Remove 500ml (24-03-2026) — Local Fill
- **POS MODEL:** In Production, Est Completion 14 Apr, Est Arrival 19 Apr
- **Gmail (15 Apr):** Peter at OP confirmed acetone received. Will plan fill by end of this week (17-18 Apr).
- **REALITY:** All ingredients now at OP. Fill planning starts ~17 Apr. 14d filling + 7d delivery → **delivery to G3PL ~8-9 May.** POS MODEL dates are STALE — update completion to ~1 May, arrival to ~9 May.
- **Quantity:** 5,000 Remove 500ml
- **Impact:** Remove 500ml at 54d cover (69.2/d) — stocks out ~8 Jun. Fill arrives ~9 May. Comfortable margin.

### AUS 09052026 — CN Container
- **POS MODEL:** In Production, Est Completion 30 Apr, Est Arrival 30 May
- **Slack (13 Apr):** "Jars to be finished on the 20th for B114, likely completion date 30th April (Sally needs 10 days to fill and pack)"
- **REALITY:** B114 jars finishing ~20 Apr → Sally completion ~30 Apr → arrival ~30 May (30d standard) or ~16 May (16d express). Dates align with POS MODEL.
- **Key contents:** 2,016 STA, 3,052 COM, 1,036 ULT, 2,592 Base, 1,296 Glow, 6,840 Remove Bowls
- **Risk:** STA stocks out 22 May — 8d gap before arrival. Base stocks out ~16-27 May — 3-14d gap.

### AUS 07062026 (Birthday Sale) — CN Container
- **POS MODEL:** In Production, Est Completion 8 May, Est Arrival 7 Jun
- **Slack (13 Apr):** Deposit now paid. Growth factor 1.4x.
- **REALITY:** On track. Deposit confirmed paid (was stalled 2+ weeks — now resolved).
- **Key contents:** 1,260 STA, 3,164 COM, 1,244 ULT, 2,376 Base, 1,512 Glow

### AUS 08072026 — Planned
- **POS MODEL:** Est Completion 15 Jun, Est Arrival 15 Jul
- **Status:** Not yet ordered. Fill PO place date 29 Apr.
- **Key contents:** Fire Collection restocks (600 each), 1,372 STA, 3,192 COM, 1,428 ULT
- **Risk:** If fill PO not placed by 29 Apr, this pushes back and Fire Collection colours have no restock.

### Stale POS MODEL data:
- **Exp 1 (OP Heal/Remove 500ml):** Status "Delivered" ✅
- **Exp 2 (OP Remove 500ml):** Shows completion 14 Apr / arrival 19 Apr — STALE. Should be completion ~1 May / arrival ~9 May.
- **B360 PACKUP:** Status "Delivered" ✅

---

## LOCAL FILL STATUS

### OP Remove 500ml Fill (24-03-2026)
- **Ingredients:** Calcium Chloride ✅ | Coconut Oil + Vitamin E ✅ (13 Apr) | Acetone ✅ (received 15 Apr)
- **All ingredients confirmed at OP as of 15 Apr.**
- Peter will plan fill by end of this week (17-18 Apr).
- Lead time: 14d filling + 7d delivery to G3PL
- **Earliest G3PL delivery: ~8-9 May**
- Quantity: 5,000 Remove 500ml

### Heal Fill — Needs Placing
- **Flagged 13 Apr:** "We need to place a Heal fill this week — recommended PO to come."
- Current Heal stock: 10,998 at 146.4/d → 75d (stocks out ~30 Jun)
- At 28d OP lead time, if placed this week (16-18 Apr): delivery ~14-16 May. Well before stockout.
- **Action: Place Heal fill PO with Outsource Packaging this week.**

### Avi Printing — Labels Booklet
- PO placed 24 Mar. No delivery confirmation in 23 days.
- **ACC-LAB stocks out ~1 May. Must chase Avi immediately.**

---

## STOCK-OUT FORECAST — BY CONTAINER WINDOW

### Window 0: NOW → OP Remove 500ml Fill (~9 May) — 23 days

| SKU | Stock | Best Rate | Stocks Out | Notes |
|---|---:|---:|---|---|
| ACC-LAB | 3,563 | 241.8/d | **30 Apr** | NO INBOUND. Stocks out before anything arrives. |
| LIQ-BAS-2 | 725 | 29.6/d | **10 May** | 14d DSR (17.6) depressed by OOS — 30d rate (29.6) is true demand. Worse than last review reported. |

- **ACC-LAB is the first thing to go.** 14 days from now. Nothing can fix this except Avi Printing delivery.
- **Base stocks out 10 May** at the 30d Shopify rate — 6 days sooner than the 14d rate predicted. No local fill, no interim shipment.

### Window 1: OP Fill (~9 May) → AUS 09052026 (~30 May) — 21 days

The OP fill brings +5,000 Remove 500ml. Nothing else arrives in this window.

**Stocks out during this window (before AUS 09052026):**

| SKU | Stock | Best Rate | Stocks Out | Days Before 09052026 | 09052026 Brings |
|---|---:|---:|---|---:|---|
| LIQ-BAS-2 | 725 | 29.6/d | **10 May** | **-20d** | +2,592 |
| KIT-STA-2 | 1,319 | 38.8/d | **19 May** | **-10d** | +2,016 |
| ACC-REM-BOW | 1,617 | 43.8/d | **22 May** | **-7d** | +6,840 |
| LIQ-SEN-2 | 123 | 3.1/d | **25 May** | **-4d** | +432 |
| LIQ-GLO-4 | 930 | 22.5/d | **27 May** | **-3d** | +1,296 |
| ACC-LAB | 3,563 | 241.8/d | **30 Apr** | **-30d** | Nothing |

- **6 SKUs stock out before AUS 09052026.** Base is the worst at 20 days OOS. Labels booklet already OOS by this point.
- ACC-REM-500 safe: 3,731 + 5,000 fill = 7,139 post-fill (103d at 69.2/d). Comfortable through to Aug.

**Safe through this window:**

| SKU | Stock | Best Rate | Cover | Status |
|---|---:|---:|---:|---|
| KIT-COM-4 | 5,164 | 67.4/d | 77d | Arrives with 2,220 remaining |
| KIT-ULT-6 | 2,964 | 28.3/d | 105d | Arrives with 1,719 remaining |
| LIQ-HEA-5 | 10,998 | 146.4/d | 75d | Safe but no inbound — fill needed |
| LIQ-SEA-3 | 2,622 | 24.5/d | 107d | |
| LIQ-BON-1 | 1,387 | 8.9/d | 156d | |
| LIQ-SOA-6 | 667 | 11.7/d | 57d | |

### Window 2: AUS 09052026 (~30 May) → AUS 07062026 (~7 Jun) — 8 days

AUS 09052026 resolves the May stockouts (except Labels). This is a short 8-day gap to the Birthday Sale container.

**Post-09052026 snapshot (what it resolves + what's still at risk):**

| SKU | Post-Arrival Stock | Cover | At Risk Before 07062026? |
|---|---:|---:|---|
| KIT-STA-2 | 2,016 (was OOS 10d) | **52d** | No — safe for 8d |
| KIT-COM-4 | 5,272 | **78d** | No |
| KIT-ULT-6 | 2,755 | **97d** | No |
| LIQ-BAS-2 | 2,592 (was OOS 20d) | **88d** | No — but was OOS for 20 days |
| LIQ-GLO-4 | 1,296 (was OOS 3d) | **58d** | No |
| LIQ-SEN-2 | 432 (was OOS 4d) | **139d** | No |
| ACC-REM-BOW | 6,840 (was OOS 7d) | **156d** ⚠️ | No — massively overstocked |
| LIQ-HEA-5 | 4,560 | **31d** | Short window, safe |
| ACC-LAB | **STILL OOS** | — | Not on 09052026 or 07062026 |

- AUS 09052026 clears all stockouts except **ACC-LAB which remains OOS indefinitely** until Avi Printing delivers.
- ACC-REM-BOW jumps from OOS to 156d — the 6,840 units were ordered against model DSR (75.4/d). Actual 3PL is 43.8/d (Shopify standalone only 4.1/d). ~5,400 excess units.

### Window 3: AUS 07062026 (~7 Jun) → AUS 08072026 (~15 Jul) — 38 days

Birthday Sale container lands. 1.4x growth factor for this order.

**Post-07062026 snapshot:**

| SKU | Post-Arrival Stock | Cover | Notes |
|---|---:|---:|---|
| KIT-STA-2 | 2,966 | **76d** | Healthy |
| KIT-COM-4 | 7,875 | **117d** ⚠️ | Overstocked |
| KIT-ULT-6 | 3,772 | **133d** ⚠️ | Overstocked |
| LIQ-BAS-2 | 4,731 | **160d** ⚠️ | Heavy overstock — was OOS 20d in May, now 5mo+ excess |
| LIQ-GLO-4 | 2,628 | **117d** ⚠️ | Overstock |
| LIQ-HEA-5 | 3,385 | **23d** | **At risk before 08072026** — stocks out ~30 Jun. Fill PO this week extends this. |
| ACC-REM-500 | 5,133 | **74d** | Healthy |
| ACC-REM-BOW | 8,490 | **194d** ⚠️ | Heavy overstock |
| ACC-LAB | **STILL OOS** | — | Still no inbound from any container |

**At risk before AUS 08072026 (15 Jul):**
- **LIQ-HEA-5 without new fill: stocks out ~30 Jun** (15d before 08072026). If Heal fill placed this week (+10,000, delivery ~16 May): extends to ~143d post-fill. No issue.
- **Fire Collection colours** (if selling at model 6.5/d): all 7 stock out May-Jun. AUS 08072026 brings +600 each on 15 Jul.
- **ACC-LAB: still OOS.** Must be resolved via Avi Printing, not containers.

### Post AUS 08072026 (15 Jul) — Final Position

| SKU | Post-All Stock | Cover | vs 75d Target |
|---|---:|---:|---|
| KIT-STA-2 | 3,006 | **77d** | On target |
| KIT-COM-4 | 9,001 | **134d** ⚠️ | +59d over / ~3,900 excess units / 2.0mo |
| KIT-ULT-6 | 4,269 | **151d** ⚠️ | +76d over / ~2,100 excess units / 2.7mo |
| LIQ-BAS-2 | 5,817 | **196d** ⚠️ | +121d over / ~3,600 excess units / 5.1mo |
| LIQ-GLO-4 | 2,637 | **117d** ⚠️ | +42d over / ~950 excess units / 1.4mo |
| ACC-REM-BOW | 9,465 | **216d** ⚠️ | +141d over / ~6,200 excess units / 4.7mo |
| LIQ-HEA-5 | depends on fill | — | Fill-dependent |

**Overstock pattern:** Model assumes 191/d kit selling. Actual is 124/d. Every container ordered at 1.3x inflates stock further. COM, ULT, Base, Glow, and Remove Bowls are all heavily overstocked after all 3 containers land. If demand doesn't scale to target, this represents months of excess inventory and tied-up cash. **Review AUS 08072026 quantities — reduce COM/ULT, increase STA.**

### IF AUS 09052026 IS DELAYED (worst case)

If 09052026 doesn't arrive by 30 May, 5 SKUs are OOS with no cover until AUS 07062026 on 7 Jun:

| SKU | Stocks Out | Days OOS Before 07062026 |
|---|---|---:|
| LIQ-BAS-2 | 10 May | **28d OOS** |
| KIT-STA-2 | 19 May | **19d OOS** |
| ACC-REM-BOW | 22 May | **16d OOS** |
| LIQ-SEN-2 | 25 May | **13d OOS** |
| LIQ-GLO-4 | 27 May | **11d OOS** |

COM (77d) and ULT (105d) survive comfortably. The constraint is entirely on STA, Base, and Glow.

---

## LOCAL FILL FORECAST

### Outsource Packaging — Remove 500ml (ACC-REM-500) — DSR: 69.2/d (3PL, bundle-adjusted)
- Current: 3,731 units (54d)
- Fill arriving: ~9 May (+5,000) → ~7,139 post-fill (103d)
- Next fill place by: not urgent — 103d post-fill cover
- If Birthday Sale (1.4x late Jun): still comfortable with 100+ days

### Outsource Packaging — Heal (LIQ-HEA-5) — DSR: 146.4/d (3PL, kit-adjusted)
- Current: 10,998 units (75d) — stocks out ~30 Jun
- **No fill in pipeline.** Flagged 13 Apr for placement this week.
- If placed 18 Apr: delivery ~16 May. Post-fill cover depends on quantity.
- **Recommended: 10,000 units → 68d additional cover. Total ~143d post-fill → comfortable through Birthday Sale.**
- Place by: **18 Apr** (this week)

---

## PO RECOMMENDATIONS

Target: 14-21d kit cover (lean). Lead times: 84d (raw→delivery), 44d (fill→delivery), 30d (shipping), 28d (local fill).

### Flagged — Approaching or Past Deadlines

| SKU | Stock | Best Rate | Cover | Next PO Place By | Status |
|---|---:|---:|---:|---|---|
| ACC-LAB | 3,563 | 241.8/d | 15d | **PAST — chase Avi Printing immediately** | PO placed 24 Mar, no delivery confirmation |
| LIQ-HEA-5 | 10,998 | 146.4/d | 75d | **18 Apr (this week)** — local fill PO to OP | No fill in pipeline, no container inbound |
| KIT-STA-2 | 1,319 | 38.8/d | 34d | AUS 09052026 covers (if on time) | 10d OOS gap — monitor for delay |
| LIQ-BAS-2 | 725 | 29.6/d | 24d | AUS 09052026 covers (if on time) | **20d OOS gap** — express only if container delays |

### No PO Needed Yet
- KIT-COM-4: 77d + 3 inbound containers → 134d post-all. Already overstocked — reduce 08072026 qty.
- KIT-ULT-6: 105d + 3 inbound → 151d. Already overstocked — reduce 08072026 qty.
- ACC-REM-500: 54d + OP fill 9 May → 103d. Comfortable.

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (act today)

- **ACC-LAB (Labels Booklet): 3,563 units, 15d cover, stocks out ~30 Apr. NO INBOUND on any container.** Compliance-critical — can't ship without them. Avi Printing PO placed 24 Mar with no delivery confirmation. Chase Avi immediately + confirm delivery ETA.
- **LIQ-BAS-2 (Base): 725 units, stocks out ~10 May (30d rate: 29.6/d — 14d rate of 17.6 was depressed by OOS).** AUS 09052026 arriving ~30 May → **20d stockout gap.** No local fill option. Express from Sally or redirect from another region only options.
- **KIT-STA-2 (Starter): 1,319 units, 34d at 3PL rate, stocks out ~19 May.** AUS 09052026 arriving ~30 May → 10d gap. Swap to COM/ULT if STA runs out (used before 27 Mar).
- **POS MODEL Exp 2 dates stale:** OP Remove 500ml shows completion 14 Apr / arrival 19 Apr. Reality: completion ~1 May / arrival ~9 May. Greg to update.

### 🟡 WARNING (act this week)

- **Heal fill PO: place with Outsource Packaging this week.** 10,998 units / 75d. No inbound from any container. Without fill, stocks out ~30 Jun — 15d before AUS 08072026. Recommended 10,000 units.
- **LIQ-GLO-4 (Glow): 930 units, 41d (3PL rate).** Stocks out ~27 May, 3d before AUS 09052026. Tight but shorter gap than Base/STA.
- **ACC-REM-BOW (Remove Bowl): 1,617 units, 37d cover.** Stocks out ~22 May, 7d before AUS 09052026. Post-arrival swings to 156d overstock — review 09052026 quantity (6,840 is excessive at actual rates).
- **AUS 08072026 fill PO place date: 29 Apr.** If not placed on time, Fire Collection restocks are at risk.
- **Fire Collection colours (7 SKUs): verify Shopify listing status.** All showing 0 sales in 14d. If listed and selling at model rate (6.5/d each), they stock out May-Jun with no restock until 15 Jul.
- **Blue Moon (POW-BLU-ZGD22): 514 units at G3PL, OOS on website.** Re-enable listing.
- **Review AUS 08072026 kit quantities.** COM and ULT heavily overstocked — reduce and reallocate to STA.

### 🟢 MONITOR (FYI)

- **Growth factor gap narrowing slightly** (35% below vs 36.5% last review) but still well off 1.3x target. Kit selling averaging 124/d, volatile week-to-week (95-135 range). COM and ULT accumulating excess stock.
- **AUS 07062026 deposit confirmed paid** — no longer a blocker.
- **OP Remove 500ml fill on track.** All ingredients at OP, fill planning this week, delivery ~9 May.
- **STO-BUB-BAG-L**: 1 red flag day (6 Apr, 449 vs 435 benchmark). Not systemic.
- **24 colours with 0 Shopify sales** — some may be delisted, some awaiting launch. Low urgency but worth a periodic listing audit.
- **Multiple liquid DSRs depressed by recent OOS** (Base, LO Base, LO Glow, Seal). 30d rates used where 14d was understated.

---

## FOLLOW-UP ITEMS

### Immediate
- [ ] Chase Avi Printing for ACC-LAB delivery ETA (PO 24-03-2026)
- [ ] Place Heal fill PO with Outsource Packaging (~10,000 units)
- [ ] Greg: Update POS MODEL Exp 2 dates (OP Remove 500ml: completion ~1 May, arrival ~9 May)
- [ ] Verify Fire Collection colour listing status on Shopify
- [ ] Re-enable Blue Moon on Shopify

### By End of Month
- [ ] Confirm AUS 09052026 on track for 30 Apr completion (B114 jars finishing ~20 Apr)
- [ ] Place AUS 08072026 fill PO by 29 Apr
- [ ] Review AUS 08072026 kit quantities — reduce COM/ULT, increase STA
- [ ] Review ACC-REM-BOW quantity on AUS 09052026 (6,840 is ~5,400 excess vs 75d target at 3PL rate)

### Ongoing
- [ ] Monitor Base (LIQ-BAS-2) weekly — 30d cover, stocks out mid-May if no express
- [ ] Monitor STA weekly — 37d cover, stocks out late May
- [ ] Track growth factor trend — sustained at 0.85x vs 1.3x model
- [ ] Verify stock sync working at G3PL (enabled 13 Apr)
