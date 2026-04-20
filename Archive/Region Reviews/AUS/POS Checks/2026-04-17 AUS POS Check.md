# POS MODEL CHECK — AUS — 17 Apr 2026

## DATA FRESHNESS

- **POS MODEL updated:** 17 Apr 2026 (today) — confirmed in sheet H9
- **Growth factor:** 1.3x (J9) — base kit 147/d → scaled 191.1/d
- **3PL (AUS 3GPL) last valid:** 17 Apr 2026
- **Shopify last valid:** 16 Apr 2026 (1d lag)
- **Vessels:** 16 days express / 30 days standard
- **ShipHero exports:** Not available — no longer needed (all POs closed, minor B360 packup residual being chased)

### Manual overrides applied to sheet figures
- **ACC-LAB: 18,344 on hand** (Avi PO 11 received 16 Apr; Greg updated AM, Katrina booked in PM). Sheet shows 3,397.
- **ACC-THA: 21,587 on hand** (32,787 sheet less 11,200 Greg-identified B360 shortfall — pending Katrina response Fri 18 Apr).
- **Colour SKUs: POW-CHA-011 -200, POW-FRI-778 -200, POW-SIN-254 -400, POW-RUS-624 -200, POW-STE-001 -200** (B360 transfer shortfall).

---

## GROWTH FACTOR HEALTH CHECK

| Metric | Value |
|---|---|
| Model growth factor | 1.3x |
| Model base kit DSR | 147.0/d |
| Model scaled kit DSR | 191.1/d |
| Actual 14d kit DSR | 125.8/d |
| Actual 7d kit DSR | 122.0/d |
| Actual growth factor | **0.86x** |
| Gap vs scaled target | **34% below** |

**Weekly kit trend:**

| Week | Dates | Daily Rate | Trend |
|---|---|---:|---|
| W10 | 2-8 Mar | 95.1 | Trough |
| W11 | 9-15 Mar | 105.3 | ↑ |
| W12 | 16-22 Mar | 130.3 | ↑ |
| W13 | 23-29 Mar | 128.4 | → |
| W14 | 30 Mar-5 Apr | 105.4 | ↓ Easter |
| W15 | 6-12 Apr | 135.3 | ↑ Best since B360 transition |
| W16 | 13-16 Apr (4d) | 104.0 | ↓ Weakening |

**Note:** Easter 35% sale is live during W16. A 4-day rate of 104/d **with a 35% discount in market** is a concerning signal — the sale isn't lifting volume to anywhere near 1.3x scaled. Watch W17 closely.

Not recommending lowering growth factor (per your framing). Flagging only that ordering at 1.3x while running at 0.86x continues to accumulate overstock on COM, ULT, and several liquids.

---

## STOCK POSITION — DUAL-DSR VIEW

Shows projected cover at **1.3x model**, at **3PL actual deduction rate**, and at **Shopify 30d rate**. Where these diverge materially, both are flagged.

### Kits

| SKU | Stock | Model DSR (1.3x) | 3PL Ded/d | Shop 30d | Cov@Model | Cov@3PL | Cov@Shop | Flag |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| KIT-STA-2 | 1,296 | 44.2 | 39.0 | 33.8 | **29d** | 33d | 38d | ⚠️ tight at model |
| KIT-COM-4 | 5,099 | 101.4 | 69.2 | 63.0 | 50d | 74d | 81d | OK |
| KIT-ULT-6 | 2,949 | 45.5 | 25.4 | 28.1 | 65d | 116d | 105d | Overstock at actual |

### Liquids

| SKU | Stock | Model (1.3x) | 3PL Ded/d | Shop 30d | Cov@Model | Cov@3PL | Cov@Shop | Flag |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| LIQ-BAS-2 | 702 | 53.3 | 24.9 | 30.2 | **13d** | 28d | 23d | 🔴 CRITICAL (all views) |
| LIQ-SEN-2 | 118 | 9.1 | 3.7 | 2.0 | **13d** | 32d | 59d | Model-critical only |
| LIQ-GLO-4 | 919 | 26.0 | 22.4 | 17.7 | **35d** | 41d | 52d | ⚠️ Warning |
| LIQ-SEN-4 | 193 | 7.8 | 2.8 | 2.6 | 25d | 69d | 74d | Model-critical only |
| LIQ-SEA-3 | 2,610 | 44.2 | 25.2 | 24.2 | 59d | 104d | 108d | OK |
| LIQ-BON-1 | 1,379 | 16.9 | 9.2 | 9.1 | 82d | 150d | 152d | OK |
| LIQ-SOA-6 | 660 | 13.0 | 12.1 | 6.5 | 51d | 55d | 102d | OK |
| LIQ-MAT-4 | 1,990 | 10.4 | 6.1 | 6.0 | 191d | 326d | 332d | Overstock |
| LIQ-HEA-5 | 10,893 | 184.6 | 148.5 | — | 59d | 73d | — | 🔴 **FILL PO OVERDUE** |

### Accessories

| SKU | Stock | Model (1.3x) | 3PL Ded/d | Shop 30d | Cov@Model | Cov@3PL | Cov@Shop | Flag |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| ACC-REM-500 | 3,691 | 98.8 | 167.9 | 35.2 | 37d | **22d** | 105d | 🔴 3PL faster than model |
| ACC-REM-BOW | 1,581 | 75.4 | 45.5 | 4.5 | **21d** | 35d | 351d | Warning |
| ACC-REM | 7,665 | 33.8 | 26.3 | 12.4 | 227d | 291d | 618d | Overstock |
| ACC-NAI-WIP | 262 | 6.5 | 4.3 | 3.6 | 40d | 61d | 73d | Warning |
| **ACC-LAB** ✳️ | **18,344** | 364.0 | 244.8 | 225.2 | **50d** | 75d | 81d | ⚠️ No restock plan |
| ACC-INS | 19,453 | 195.0 | 138.5 | — | 100d | 140d | — | OK |
| **ACC-THA** ✳️ | **21,587** | 364.0 | 245.1 | 225.2 | **59d** | 88d | 96d | ⚠️ See gap analysis |

### Packaging

| SKU | Stock | Model (1.3x) | 3PL Ded/d | Cov@Model | Cov@3PL | Benchmark | Flag |
|---|---:|---:|---:|---:|---:|---:|---|
| STO-BUB-BAG-L | 12,286 | 195.0 | 205.1 | 63d | 60d | 435 | OK |
| STO-BUB-BAG-S | 19,800 | — | 186.4 | — | 106d | 130 | OK |
| STO-MAI-BAG-S | 19,886 | 175.5 | 79.7 | 113d | 250d | 330 | Overstock |
| STO-MAI-2 | 17,325 | 175.5 | 82.5 | 99d | 210d | 330 | Overstock |

**Key divergences:**
- **ACC-REM-500 at 3PL 167.9/d vs model 98.8/d** — bundle consumption (ACC-REM-BUN-2, LIQ-SET). 3PL rate is reality; model is understating. Real cover: **22 days**, stocks out 9 May — exactly when OP fill arrives. Zero buffer.
- **Several liquids show model UP to 2x actual** — LIQ-SEN-2, LIQ-SEN-4, LIQ-MAT-4, ACC-REM. These are legitimate model overestimates; at actual rates they're fine. At 1.3x model they look critical.
- **ACC-LAB: model says 50d, Shopify 81d.** Divergence is because 3PL deduction captures per-order consumption (every order gets a label), not per-SKU. 3PL rate 245/d is closest to reality. At 245/d: 75d cover = stocks out ~1 Jul.

---

## CONTAINER STATUS

### Exp 2 — OP Remove 500ml (24-03-2026)
- **Sheet:** In Production. Est. completion 14 Apr / arrival 19 Apr — **STALE**
- **Reality:** All ingredients at OP. Peter fills end of this week (17-18 Apr). 14d fill + 7d ship → **completion ~1 May, arrival ~9 May**
- **Contents:** 5,000 ACC-REM-500
- **Greg: update Exp 2 dates in POS MODEL**

### AUS Powder Room (24-03-2026)
- **Status:** At risk — B114 jars delay with Mark. Sally has powder + stickers; jars at G3PL pending dispatch to local filler.
- **Joel decision pending:** fill all 400 units each locally, or partial.

### Container #3 — AUS 09052026 (JS21-20260303-1)
- **Sheet:** Est. completion 30 Apr / arrival 30 May. In Production.
- **Reality:** B114 jars finishing 20 Apr → 30 Apr completion tracking. Standard 30d vessel.
- **Key contents:** 2,016 STA / 3,052 COM / 1,036 ULT / 2,592 Base / 1,296 Glow / 432 LO Base / 432 LO Glow / 2,808 Seal / 1,080 Bond / 1,080 Soak / 6,840 Remove Bowl / 30,800 ACC-THA / 5,280 ACC-INS / 1,100 Cuticle Presser / 176 Wipes
- **NOT in this container:** LIQ-HEA-5 (no ready Heal), ACC-LAB, ACC-REM-500

### Container #4 — AUS 07062026 (Birthday Sale, JS21-20260326-1)
- **Sheet:** Est. completion 16 May / arrival 15 Jun. Deposit paid. In Production. 1.4x growth factor for this order.
- **Key contents:** 1,260 STA / 3,164 COM / 1,244 ULT / 2,376 Base / 1,512 Glow / 11,200 ACC-THA / 6,720 ACC-INS / 2,000 Remove Bowl
- **NOT in this container:** LIQ-HEA-5, ACC-LAB, ACC-REM-500

### Container #5 — AUS 08072026 (Planned)
- **Sheet:** Est. completion 15 Jun / arrival 15 Jul. Not yet ordered. **Fill PO place date 29 Apr (12 days away).**
- **Key contents:** 1,372 STA / 3,192 COM / 1,428 ULT / Empty Heal bottles (HEA-EMP/LID/BSH 20k each) + Remove 500ml bottle components / 1,944 Base / 864 Glow / 5,280 ACC-INS / 2,640 Remove Bowl + ~80 colour SKUs (Fire Collection restock)
- **NOT in this container:** LIQ-HEA-5 (ready), **ACC-LAB**, **ACC-THA** (none at all), ACC-REM-500 (only bottles for future fill)

---

## STOCK-OUT FORECAST BY WINDOW (at 1.3x model + actual cross-check)

### Window 0: NOW → OP Remove 500ml fill (~9 May) — 22 days

Items stocking out in this window:

| SKU | Stock | Best Rate Used | Stocks Out | Window | Notes |
|---|---:|---:|---|---|---|
| LIQ-BAS-2 | 702 | 30.2/d (Shop 30d) | ~10 May | At window end | 14d Shopify depressed by approaching OOS |
| LIQ-SEN-2 | 118 | 3.7/d (3PL) | ~20 May | Post window | Model (9.1/d) says 30 Apr — model overstates |
| ACC-REM-BOW | 1,581 | 45.5/d (3PL) | ~22 May | Post window | Model (75.4) says 8 May |
| ACC-REM-500 | 3,691 | 167.9/d (3PL) | **~9 May** | At window end | Race with fill arrival. Zero buffer. |

**At 1.3x model only, also these stock out in Window 0:**
- LIQ-SEN-2 at 9.1/d → 13d → ~30 Apr
- ACC-REM-BOW at 75.4/d → 21d → ~8 May

Actual data doesn't back this — both are OOS dates closer to 20-22 May per 3PL rate. Model DSRs are stale for these SKUs (Greg to correct).

### Window 1: OP Fill (~9 May) → AUS 09052026 (~30 May) — 21 days

The OP fill only brings +5,000 Remove 500ml. Nothing else arrives.

Starting from Window 0 consumption, what stocks out:

| SKU | Stock at 9 May | Best Rate | Stocks Out | Days Before 09052026 |
|---|---:|---:|---|---:|
| LIQ-BAS-2 | -37 (OOS) | 30.2/d | 10 May | **-20d OOS** |
| KIT-STA-2 | ~438 | 39.0/d | ~22 May | **-8d OOS** |
| LIQ-GLO-4 | ~427 | 22.4/d | ~28 May | **-2d OOS** |
| ACC-REM-BOW | ~580 | 45.5/d | ~22 May | **-8d OOS** |
| ACC-NAI-WIP | ~168 | 4.3/d | ~25 Jun | Safe |

**AT 1.3x MODEL (stress-test):**
- KIT-STA-2 stocks out ~16 May (14d gap)
- LIQ-GLO-4 stocks out ~22 May (8d gap)
- ACC-REM-BOW stocks out ~8 May (22d gap)
- LIQ-SEN-2 stocks out ~30 Apr (30d gap)

Either way, **Base is the top critical** — OOS 10-20 days before restock. STA and Remove Bowl also tight.

### Window 2: AUS 09052026 (~30 May) → AUS 07062026 (~15 Jun) — 16 days

09052026 refreshes all kits + most liquids + bowls. No Heal, no Labels, no Remove 500ml.

Post-09052026 snapshot (1.3x):

| SKU | Post-Arrival Stock | Cov@Model | Cov@3PL | At risk before 15 Jun? |
|---|---:|---:|---:|---|
| KIT-STA-2 | ~2,016 | 46d | 52d | No |
| KIT-COM-4 | ~4,922 | 49d | 71d | No |
| KIT-ULT-6 | ~2,227 | 49d | 88d | No |
| LIQ-BAS-2 | ~2,592 | 49d | 104d | No (just refilled after 20d OOS) |
| LIQ-GLO-4 | ~731 | 28d | 33d | **⚠️ No — tight** |
| LIQ-HEA-5 | ~2,036 | 11d | 14d | **🔴 YES — OOS ~10-14 Jun** (before 07062026) |
| ACC-REM-500 | ~5,139 | 52d | 31d | No |
| ACC-REM-BOW | ~7,420 | 98d | 163d | Overstock |
| **ACC-LAB** | **~3,248** | **9d** | **13d** | **🔴 YES — OOS before 07062026** |
| ACC-THA | ~4,987 | 14d | 20d | **🔴 YES — if Greg's shortfall real** |

**Window 2 critical risks:**
- **LIQ-HEA-5 OOS ~10-14 Jun** at 1.3x. Only fixed by OP Heal fill — which hasn't been placed.
- **ACC-LAB OOS before 07062026** — need another Avi PO placed by mid-May for late-May delivery.
- **ACC-THA tight** if Greg's 11,200 shortfall confirmed. At 3PL rate still ~20d cover, marginal.

### Window 3: AUS 07062026 (~15 Jun) → AUS 08072026 (~15 Jul) — 30 days

07062026 brings +11,200 ACC-THA, kits, some liquids. Still **no Heal, no Labels, no Remove 500ml**.

Post-07062026 snapshot (1.3x):

| SKU | Post-Arrival Stock | Cov@Model | Cov@3PL | At risk before 15 Jul? |
|---|---:|---:|---:|---|
| KIT-STA-2 | ~2,538 | 57d | 65d | No |
| KIT-COM-4 | ~7,158 | 71d | 103d | Overstock |
| LIQ-HEA-5 | depends on fill | — | — | 🔴 if no fill |
| LIQ-BAS-2 | ~3,361 | 63d | 135d | No |
| LIQ-GLO-4 | ~1,488 | 57d | 66d | Healthy |
| ACC-REM-500 | depends on 2nd fill | — | — | ⚠️ need 2nd fill placed |
| ACC-REM-BOW | ~7,060 | 94d | 155d | Overstock |
| **ACC-LAB** | **~0 or negative** | **—** | **—** | **🔴 YES — OOS** |
| ACC-THA | ~9,832 | 27d | 40d | **⚠️ 08072026 has no THA** |

**Window 3 critical risks:**
- **ACC-LAB completely OOS** before 15 Jul with zero inbound. **MUST place another Avi PO by ~end of May.**
- **ACC-THA runs into 08072026 gap** — 08072026 has no THA. At 1.3x model (364/d), OOS ~12 Jul. At 3PL rate (245/d), OOS ~25 Jul → 10d OOS.
- **LIQ-HEA-5** still depends on fill.
- **ACC-REM-500** needs a 2nd fill (OP) placed around mid-May for delivery before mid-Jun.

### Post-08072026 (15 Jul) Final Position

| SKU | Post-All Stock | Cov@Model (1.3x) | Cov@Actual (0.86x) | Overstock flag |
|---|---:|---:|---:|---|
| KIT-STA-2 | ~3,910 | 88d | 132d | OK |
| KIT-COM-4 | ~10,350 | **102d** ⚠️ | **155d** ⚠️ | Excess ~3,400 units |
| KIT-ULT-6 | ~4,483 | **99d** ⚠️ | **180d** ⚠️ | Excess ~2,400 units |
| LIQ-BAS-2 | ~5,305 | 100d | 177d | Excess ~2,500 |
| LIQ-GLO-4 | ~2,352 | 91d | 140d | Excess ~800 |
| ACC-REM-BOW | ~9,700 | 129d | 229d | Excess ~6,000 |
| ACC-LAB | 0 | — | — | **Ongoing gap** |
| ACC-THA | 0 | — | — | **Ongoing gap** |
| LIQ-HEA-5 | fill-dependent | — | — | — |

**Overstock theme:** Running at 0.86x but ordering at 1.3x = ~50% more stock than actual demand supports. Acting on this is the user's call (growth factor is aspirational) but the excess is material:
- COM: ~3,400 units excess (~$60k+ tied up at cost)
- ULT: ~2,400 units excess
- Base: ~2,500 excess
- Remove Bowl: ~6,000 excess

---

## CONTAINER GAP FLAGS — THINGS TO ADD TO IN-PROGRESS / PLANNED ORDERS

This is the "are we missing something that should be on one of these containers" analysis.

### 🔴 AUS 08072026 — CRITICAL GAPS (Fill PO due 29 Apr, 12 days away)

**Missing / insufficient on 08072026:**

| Item | 08072026 Qty | Risk | Recommendation |
|---|---:|---|---|
| **ACC-LAB** | 0 | OOS ~1 Jul, no Avi PO in pipeline | Place **Avi PO for ~50,000 units** by mid-May (Avi lead ~15-20d). Not on any container. |
| **ACC-THA** | 0 | Potential OOS early Jul at model rate | Add ~20,000 to 08072026 OR print locally |
| **LIQ-HEA-5 (ready)** | 0 | Covered by local fill | OP fill only — **place now** |
| **LIQ-GLO-4** | 864 | Only 864 units, post-arrival 91d at model | Probably adequate if fill cycle holds |

**Kit quantity review for 08072026 (at 0.86x actual selling):**
- Current planned: STA 1,372 / COM 3,192 / ULT 1,428
- At actual consumption through July, excess will be most pronounced in COM and ULT
- **Recommendation:** reduce COM by ~1,000-1,500 and ULT by ~500-800, reallocate capacity to STA +500 or additional colours

### ⚠️ AUS 07062026 — Secondary Gaps (Birthday Sale, already in production)

**Already loaded with correct 1.4x sizing for Birthday.** No critical gaps, but worth noting:
- **No Heal, no Labels, no Remove 500ml** — all must be sourced locally (OP fills, Avi)
- **Powder Room colours:** 07062026 is light on new colour launches — Birthday-specific mix. OK for Birthday SKU strategy.

### ⚠️ AUS 09052026 — Already locked

- **No Heal** (locally filled)
- **No Labels** (locally printed)
- **Remove Bowl 6,840** — at actual 45.5/d consumption, post-arrival = 156d cover = excess ~3,000+ units. Can't change now.

---

## PUSHBACK SENSITIVITY — AUS 09052026 +14 day slip

B114 jars are the identified bottleneck. Sally completion is tracking 30 Apr at current pace — BUT if Mark slips another 2 weeks (tracked to 4 May finish → Sally 14 May → arrival ~13 Jun), the risks multiply.

**If 09052026 arrives 13 Jun instead of 30 May (+14d):**

| SKU | New OOS Gap | Additional Days OOS |
|---|---|---:|
| LIQ-BAS-2 | 10 May → 13 Jun | **+14d** (34d total) |
| KIT-STA-2 | 22 May → 13 Jun | **+14d** (22d total) |
| LIQ-GLO-4 | 28 May → 13 Jun | **+14d** (16d total) |
| ACC-REM-BOW | 22 May → 13 Jun | **+14d** (22d total) |
| LIQ-SEN-2 (model) | 30 Apr → 13 Jun | +14d (44d total) |

**At actual 0.86x selling** — same calculation but starting runway is longer, so gaps are slightly shorter (Base goes from ~10 May → 13 Jun OOS; STA from ~26 May → 13 Jun = still ~18d).

**What can bridge a +14d slip on 09052026?**
- **Base:** Only Sally express. Lily WeChat contact to split/express part of 09052026.
- **STA:** Swap to COM kits (already precedented 27 Mar). COM stock is ample.
- **Remove Bowl:** Redirect from bundle deductions? No easy fix — needs express.
- **Glow:** Sally express, or OP Chemence... no, OP doesn't fill Glow. Sally only.

**Recommendation:** Lily WeChat check-in this week to confirm jar timing. If any doubt about 20 Apr finish, begin Base + STA + Bowl express conversation now.

---

## LOCAL FILL RECOMMENDATIONS

### Heal (LIQ-HEA-5) — OVERDUE, PLACE TODAY

**Lead time (your input):** 21d ingredient + 30d fill + 7d ship = **58d**

**Projected consumption (1.3x):** 184.6/d (from DSR 142 × 1.3)

| Scenario        |   Quantity | Post-fill cover @ 1.3x | Post-fill cover @ actual 0.86x |
| --------------- | ---------: | ---------------------: | -----------------------------: |
| Lean            |     12,000 |                    66d |                            96d |
| **Recommended** | **15,000** |                **83d** |                       **121d** |
| Conservative    |     18,000 |                    99d |                           144d |

**Math (at 15,000 recommended):**
- Current stock: 10,893
- Consumption during 58d lead at 184.6/d: 10,707
- Stock at fill arrival: 186 (essentially zero — **1-day buffer**)
- Post-fill: 15,186 → 83d at 1.3x or 121d at 0.86x actual

**Why 15,000 is the sweet spot:**
- 58d fill cycle means we need another fill placed ~same time as this one lands (mid-Jun) to keep Heal continuous
- At 15,000 units and actual 0.86x rate, we have 121d cover = plenty of runway for next fill
- At 1.3x, we have 83d — still comfortable, with ~25d buffer if next fill slips
- Avoids going to 18k+ which compounds overstock if selling stays at 0.86x

**Place today** — every day of delay tightens the 1-day arrival buffer toward OOS.

### Remove 500ml (ACC-REM-500) — NEXT FILL NEEDED AFTER CURRENT

Current OP fill (24-03-2026) brings 5,000 units ~9 May. Post-fill stock 3,691 + 5,000 = 8,691. At 3PL rate 167.9/d (the real rate due to bundles), that's **52d cover → stocks out ~30 Jun.**

08072026 bottle components arrive 15 Jul for a future fill — no ready-to-use stock.

**Recommendation:** Place a 2nd OP Remove 500ml fill by **~10 May** (just as first arrives) for delivery late May / early Jun. Quantity: ~5,000-6,000 units to extend cover to ~3 months.

### Avi Printing (ACC-LAB) — PLACE NEW PO BY MID-MAY

Current 18,344. At 3PL 244.8/d, OOS ~1 Jul. No container ACC-LAB. Avi lead ~15-20d.

**Recommendation:** Place next Avi PO by **~15 May** for late-May/early-Jun delivery. Qty to target 60-75d post-delivery cover at projected rate (~18,000-22,000 units).

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (today)

- **Place OP Heal fill PO — 15,000 units.** 4 days overdue. Every day of delay erodes the 1-day buffer at arrival.
- **Confirm Avi PO 11 actually reflects 18,344 at G3PL.** If POS MODEL paste hasn't caught up by tomorrow, reconcile with Katrina.
- **Base (LIQ-BAS-2): 702 units, 28d cover (3PL) / 23d (Shop 30d).** Stocks out 10-15 May. AUS 09052026 arrives 30 May → **15-20d OOS gap.** No local fill option — express via Sally only path.
- **ACC-REM-500: 22d cover at 3PL rate (not 37d model).** Stocks out 9 May, exactly when OP fill arrives. Zero buffer. If Peter's fill slips by 2+ days, brief OOS.

### 🟡 WARNING (this week)

- **AUS 08072026: No ACC-LAB, no ACC-THA.** Fill PO due 29 Apr. Add THA (~20,000) to the order, and plan a separate Avi ACC-LAB PO for mid-May.
- **AUS 09052026 pushback sensitivity.** Confirm B114 jar finish 20 Apr (Remy WeChat Lily this week). If slip, begin express conversations for Base/STA/Bowl now.
- **Heal at 59d model cover / 73d 3PL.** Container 07062026 + 08072026 bring zero ready Heal. Fill-placement this week covers 07062026 arrival; need 3rd fill scheduled for mid-Jun to cover 08072026 window.
- **ACC-REM-500: place 2nd OP fill by 10 May.**
- **Review AUS 08072026 kit quantities.** At 0.86x actual, COM/ULT overstock building. Recommend trim ~1,500 COM + ~600 ULT.

### 🟢 MONITOR

- **Growth factor gap sustained at 0.86x for 8+ weeks.** W15 recovered (135/d), W16 softening (104/d in 4d with 35% Easter sale live). Not a decision trigger yet but worth watching.
- **LIQ-SEN-2 / LIQ-SEN-4 / LIQ-MAT-4 model DSR stale.** At actual rates all are fine — model shows critical. Greg to update.
- **ACC-REM-BOW model DSR 75.4 vs actual 45.5.** 66% overstate. Drives ordering inflation. Greg to reduce to ~45/d.

---

## FOLLOW-UP ITEMS

### Immediate (today / Monday)
- [ ] Draft Heal fill PO (15,000 units to OP) — Daniel/Remy
- [ ] Confirm Avi PO 11 ACC-LAB quantity in POS MODEL once synced (should be ~15k units in, total 18,344)
- [ ] Confirm jar finish timing with Lily (WeChat)
- [ ] Peter: confirm Remove 500ml fill start date

### By 29 Apr
- [ ] AUS 08072026 Fill PO placement — add ACC-THA 20,000, review kit qty (trim COM/ULT)
- [ ] Greg: update POS MODEL Exp 2 dates (OP Remove 500ml completion ~1 May, arrival ~9 May)
- [ ] Katrina: response on Greg's 11,200 ACC-THA shortfall + colour shortfalls

### By mid-May
- [ ] Place 2nd OP Remove 500ml fill PO (~5,500 units)
- [ ] Place Avi ACC-LAB PO (~20,000 units)

### Monitoring
- [ ] W17 selling rate (is W16 soft start a trend or noise during sale?)
- [ ] ShipHero product name sync resolution (Daniel + Jake)
- [ ] B360 packup residual discrepancies (Greg tracking)
