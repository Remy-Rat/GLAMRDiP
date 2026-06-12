# 🇦🇺 AUS POS Check - 8 Jun 2026

## DATA FRESHNESS

- **POS MODEL UPDATED:** 2026-06-08 (today AM paste, Greg). Public holiday Monday so no G3PL check-in / movement events today; Tue 9 Jun is the first operational day with mailers landed.
- **AUS 3GPL tab last valid date:** 2026-06-08 (same paste).
- **ShipHero:** not pulled this run - sheet is current and the operative window (Tue 9 Jun post-holiday) hasn't started yet.
- **Growth factor:** 1.3x global (191.1 kits/d scaled). AUS 07062026 carries its own 1.4x; AUS 05082026 + AUS 04092026 carry 1.6x.

## MANUAL OVERRIDES (Gmail/Slack vs sheet)

- **STO-BUB-BAG-L:** sheet shows 1,096 on hand 8 Jun. PO 17 (AUK Logistics bubble mailers) physically delivered Fri 5 Jun; stock jumped from 0 to 1,949 on 6 Jun in the 3PL tab. G3PL has burned through 853 units (~430/d) in the 3 days since landing. PO 17 brought ~3,000 units (approx, from prior recap context). No further override - sheet is current.
- **ACC-LAB:** sheet shows 6,147 on hand. 15,000-unit Avi PO sitting at Avi awaiting Joel payment (12 days stalled). Treat as 6,147 confirmed; +15,000 contingent on Joel paying.
- **Sydney Solvents acetone:** Joel paid pending receipt confirmation. Not at OP per Peter 4 Jun. Heal fill at OP partial-state (NDA/Coconut/Vit E/Calcium in, acetone out).
- **AUS 05082026 deposit:** NOT paid. Container is in "Ordering" status with 1.6x growth assumption; effectively a draft until deposit lands.

## STOCK POSITION - CRITICAL SKUs (Projected @ 1.3x vs Actual 14d)

| SKU | Stock | Proj DSR | Cov @ Proj | Actual DSR (14d/7d) | Cov @ Actual | Flag |
|---|---|---|---|---|---|---|
| **KIT-STA-2** | 82 | 57.5 | 1.4d | 20.0 / 19.0 | **4.1d** | 🔴 OOS this week |
| **KIT-COM-4** | 1,335 | 131.8 | 10.1d | 154.8 / 161.1 | **8.3d** | 🔴 OOS pre-09052026 |
| **KIT-ULT-6** | 1 | 59.2 | 0.02d | 6.8 / 0.0 | **OOS NOW** | 🔴 marked SELL OOS, substitution active |
| **LIQ-HEA-5** (kit-adj) | 2,831 | 191.1 | 14.8d | 183.1 / 184.4 | **15.4d** | 🔴 OOS ~23 Jun (drives kit fulfilment after KIT-COM lands) |
| **LIQ-BAS-2** standalone | 0 | n/a | n/a | 23.4 / 24.9 | OOS NOW | 🔴 14d gap pre-22 Jun |
| **LIQ-SEN-2** | 0 | n/a | n/a | 9.1 / 9.1 | OOS NOW | 🔴 14d gap |
| **LIQ-GLO-4** | 223 | n/a | n/a | 14.9 / 19.7 | **11.3d** | 🟡 3d gap |
| **LIQ-SEN-4** | 131 | n/a | n/a | 5.8 / 6.3 | 20.8d | 🟢 safe to 22 Jun |
| **LIQ-SEA-3** | 1,563 | n/a | n/a | 24.3 / 32.6 | 48d | 🟢 |
| **LIQ-BON-1** | 982 | n/a | n/a | 8.4 / 9.4 | 104d | 🟢 |
| **LIQ-SOA-6** | 399 | n/a | n/a | 5.4 / 6.9 | 57d | 🟢 |
| **LIQ-MAT-4** | 1,774 | n/a | n/a | 3.9 / 5.4 | 329d | 🟢 |
| **ACC-REM** (120ml) | 6,523 | n/a | n/a | 7.8 / 7.4 | 881d | 🟢 oversupplied |
| **ACC-REM-500** | 2,414 | n/a | n/a | 163.1 / 167.7 | **14.4d** | 🔴 OOS ~23 Jun, fill TBD today |
| **ACC-REM-BOW** | 0 | n/a | n/a | 1.3 / 0.0 | OOS NOW | 🟡 small DSR, 6,840 in 22 Jun |
| **ACC-INS** (kit-adj) | 11,567 | 191.1 | 60.5d | 179.0 / 179.4 | 64.5d | 🟢 |
| **ACC-LAB** (all orders) | 6,147 | n/a | n/a | 258.4 / 276.9 | **22.2d** | 🟡 gated on Joel paying Avi |
| **ACC-NAI-MAT** | 0 | n/a | n/a | 76.0 / 0.4 | OOS NOW | 🟢 offer pivoted, demand collapsed |
| **ACC-TIP-BAL** (current offer) | 0 | n/a | n/a | 75.1 / 35.9 | OOS NOW | 🔴 active offer SKU, must rotate |
| **ACC-TIP-SQU** | 495 | n/a | n/a | 37.4 / 6.9 | 71.7d | 🟢 |
| **ACC-TIP-STI** | 636 | n/a | n/a | 0.8 / 0.6 | 1,060d | 🟢 oversupplied |
| **ACC-TIP-COF** | 0 | n/a | n/a | 0.1 / 0.0 | dead | 🟢 |
| **ACC-TIP-ALM** | 2,109 | n/a | n/a | 8.9 / 11.1 | 190d | 🟢 |
| **STO-BUB-BAG-L** | 1,096 | n/a | n/a | 317.7 / 319.4 | **3.4d** | 🔴 cleared PO 17 burn, container in 14d |
| **STO-BUB-BAG-S** | 2,215 | n/a | n/a | 267.7 / 310.9 | **7.1d** | 🟡 |
| **STO-MAI-2** | 13,912 | n/a | n/a | 62.9 / 76.7 | 181d | 🟢 |
| **STO-MAI-BAG-S** | 16,473 | n/a | n/a | 62.9 / 76.7 | 215d | 🟢 |

Notes:
- Actual DSR uses 3PL deduction rates (14d, ex-arrival days). Where 7d collapses to 0 (KIT-ULT-6, ACC-TIP-COF, ACC-TIP-BAL, ACC-REM-BOW), the SKU is OOS-suppressed not demand-collapsed (no stock → no deductions).
- Kit total combined burn rate (STA + COM + ULT): **184.7/d 14d** (close to 1.3x model 191.1). Substitution flows ULT → COM still in play.

## KIT OOS WINDOW BEFORE AUS 09052026 - HEADLINE NUMBER

This is the question Remy flagged.

**Today (8 Jun):** total kit stock = 82 + 1,335 + 1 = **1,418 kits**  
**Combined burn rate:** 184.7/d (14d 3PL, ex-arrivals)  
**Days until total-kit OOS:** 1,418 / 184.7 = **7.7 days → OOS ~16 Jun**

**AUS 09052026 arrival:** 22 Jun  
**Kit OOS gap pre-arrival: 6 days (16-21 Jun inclusive).**

But kits cannot ship without **Heal** (LIQ-HEA-5 is added at 3PL per [[Component Map]]).

**Heal OOS ~23 Jun** (2,831 / 184/d = 15.4d). 09052026 container brings 0 Heal - it's not a kit-component in CN containers, OP local fill is the only path.

**OP Heal fill status today (8 Jun):**
- Started 29 May at OP per Peter 28 May email.
- NDA / Calcium / Coconut Oil / Vit E received at OP 4 Jun.
- **Acetone NOT received** (Sydney Solvents - Joel paid pending receipt confirmation, James silent since 26 May invoice send).
- Lead time once all ingredients in: ~21d (14 fill + 7 transit) per [[Lead Times]].
- **Best case Heal landing G3PL: ~22-25 Jun** (if acetone arrives by mid-week and fill catches up). 
- **Worst case: 28 Jun - 3 Jul** if acetone slips a week and fill is paused.

**Combined kit-fulfilment OOS window:**
- **Best case:** 16-22 Jun (6 days). Kit container lands 22 Jun, Heal also lands ~22 Jun, fulfilment resumes immediately.
- **Likely case:** 16-25 Jun (9-10 days). Heal slips 2-3 days post-container.
- **Worst case:** 16 Jun - 3 Jul (~17 days). Acetone slip cascades into mid-container fulfilment void.

The critical lever is Joel chasing Sydney Solvents acetone confirmation this week.

## WHAT ELSE IS AT RISK (the user-asked question)

Adjacent gaps over the 8-22 Jun window:

| SKU | Stock | DSR | OOS Date | Container Brings | Net Position |
|---|---|---|---|---|---|
| LIQ-BAS-2 standalone | 0 | 25/d | NOW | 2,592 on 22 Jun | 14d gap, then 100d cover |
| LIQ-SEN-2 | 0 | 9/d | NOW | 432 on 22 Jun | 14d gap, then 48d cover |
| LIQ-GLO-4 std | 223 | 19.7/d | ~19 Jun | 1,296 on 22 Jun | 3d gap |
| ACC-REM-500 | 2,414 | 167.7/d | ~23 Jun | 0 in 22 Jun; depends on Peter (gasket today) or Swift rush | **CRITICAL - no CN inbound** |
| ACC-REM-BOW | 0 | 1.3/d | NOW | 6,840 on 22 Jun | 14d gap, low DSR so visible only as bundle unfulfilled |
| ACC-TIP-BAL | 0 | 36/d | NOW | 0 on 22 Jun | **CRITICAL - offer must rotate now** |
| STO-BUB-BAG-L | 1,096 | 319/d | ~12 Jun (3-4d) | 6,000 on 22 Jun | 10d gap - second mailer crisis incoming |
| STO-BUB-BAG-S | 2,215 | 311/d | ~16 Jun | 0 on 22 Jun | **CRITICAL - no inbound, check supplier** |
| ACC-LAB | 6,147 | 259/d | ~2 Jul | 0 ex-Avi PO | gated on Joel payment to Avi |
| ACC-NAI-MAT | 0 | 0.4/d 7d | NOW | 200 on 4 Sep | offer pivoted - watch attach rate |

**The four risks that aren't kit-OOS:**
1. **STO-BUB-BAG-L second crisis (3-4 day cover)** - 22 Jun container has 6k vs 319/d burn = 18-day cover. Tight. Watch G3PL processing rate.
2. **STO-BUB-BAG-S OOS ~16 Jun, ZERO container inbound** - the smaller bubble pocket. Daniel needs to verify what container, if any, restocks this.
3. **ACC-REM-500 OOS 23 Jun, no CN container inbound** - depends entirely on Peter (gasket sample today) or Swift cross-region rush-fill. **Joel/Daniel decision today.**
4. **ACC-TIP-BAL OOS now, currently active offer** - offer must rotate today before 22 Jun container.

## CHECK-IN PROGRESS

No active ShipHero CSV exports for this run. PO 17 (bubble mailers) delivered 5 Jun; stock movement in the 3PL tab confirms receipt (0 → 1,949 on 6 Jun then burned down to 1,096 by 8 Jun). No partial check-in to reconcile.

## DOUBLE-COUNT DETECTION

No active in-flight container check-ins. Next container (AUS 09052026) is "On the Way" with est. arrival 22 Jun - no overlap with current G3PL stock projection. **No double-count detected.**

## CONTAINER / ORDER STATUS

| Ref | Status | Est. Completion | Est. Arrival | Growth |
|---|---|---|---|---|
| **B360 PACKUP** | Delivered | - | 25 May 2026 | 1.3x |
| **AUS 09052026** | On the Way | 18 May | 22 Jun 2026 | 1.3x |
| **AUS 07062026 v2** | In Production | **10 Jun** | **10 Jul 2026** | 1.4x |
| **AUS 05082026** | Ordering (no deposit) | 6 Jul | 5 Aug 2026 | 1.6x |
| **AUS 04092026** | (placeholder) | 5 Aug | 4 Sep 2026 | 1.6x |

**Notable:**
- **AUS 07062026 arrival slipped 5 days** (1 Jun recap noted 5 Jul → now 10 Jul). Need Daniel to verify with Sally; may simply be a sheet-side adjustment to factor the v2 upsize.
- **AUS 05082026 deposit not paid** - sheet shows "Ordering" but per user this container is a draft until Joel commits. Free gift + colour sign-offs also outstanding.
- **AUS 04092026 placeholder** - 1.6x growth, no reference number yet. Need to align with Daniel's next-PO cadence.

## LOCAL FILL STATUS

**Outsource Packaging - Heal + Remove 500ml (ref 22-04-2026 + 25-05-2026)**
- Status: In Production (Heal fill started 29 May per Peter)
- Ingredients in hand at OP: NDA ✅ / Calcium ✅ / Coconut ✅ / Vit E ✅ / **Acetone ❌**
- Acetone: Joel paid Sydney Solvents pending James receipt confirmation. James silent since 26 May invoice. **Daniel/Joel chase James for production-start ETA.**
- Induction Sealer arrives at OP today (8 Jun) - gasket samples for Remove 500ml fill, decision today on Peter local vs Swift cross-region rush.
- Earliest Heal landing G3PL: ~22-25 Jun (if acetone arrives mid-week). Worst case 3 Jul.
- Earliest Remove 500ml landing: TBD pending gasket result + ingredient + fill cycle (~21 days from go).

## STOCK-OUT FORECAST

### STOCKOUT BEFORE NEXT ARRIVAL (gap < 0)

| SKU | Stock | DSR | Stocks Out | Next Inbound | Arrives | Gap |
|---|---|---|---|---|---|---|
| KIT-ULT-6 | 1 | (substituted) | OOS now | AUS 09052026 +1,036 | 22 Jun | -14d (substitution covers) |
| KIT-STA-2 | 82 | 20.0 | 12 Jun | AUS 09052026 +2,016 | 22 Jun | -10d |
| KIT-COM-4 | 1,335 | 161.1 | 16 Jun | AUS 09052026 +3,052 | 22 Jun | -6d |
| LIQ-HEA-5 | 2,831 | 184.4 | 23 Jun | OP Heal fill | ~22-25 Jun | 0 to -2d (or -10d worst case) |
| LIQ-BAS-2 | 0 | 24.9 | NOW | AUS 09052026 +2,592 | 22 Jun | -14d |
| LIQ-SEN-2 | 0 | 9.1 | NOW | AUS 09052026 +432 | 22 Jun | -14d |
| LIQ-GLO-4 | 223 | 19.7 | 19 Jun | AUS 09052026 +1,296 | 22 Jun | -3d |
| ACC-REM-500 | 2,414 | 167.7 | 23 Jun | OP fill or Swift rush | TBD | depends on today's decision |
| ACC-REM-BOW | 0 | 1.3 | NOW | AUS 09052026 +6,840 | 22 Jun | -14d |
| ACC-TIP-BAL | 0 | 36.0 | NOW | none | n/a | needs offer rotation |
| STO-BUB-BAG-L | 1,096 | 319.4 | ~12 Jun | AUS 09052026 +6,000 | 22 Jun | -10d (second bubble crisis) |
| STO-BUB-BAG-S | 2,215 | 310.9 | ~16 Jun | none | n/a | **no inbound** |

### NOTHING ON ORDER

- **STO-BUB-BAG-S** - 2,215 stock, 310/d burn, OOS ~16 Jun, no CN inbound. Daniel: check if this needs adding to AUS 07062026 v2 or a separate express PO.
- **ACC-TIP-BAL** - 0 stock, was the current offer tip. Either rotate offer or place express tips PO (Linda lead time).
- **ACC-LAB** - 6,147 stock, gated on Joel paying Avi for 15k PO ready to ship.

## WHAT NEEDS ACTION

### 🔴 CRITICAL (act today)

- **Sydney Solvents acetone receipt confirmation** - Joel/Daniel chase James for ETA. Heal fill blocked until acetone lands; every day of slip pushes Heal landing past 22 Jun and extends kit OOS gap.
- **Joel/Daniel Remove 500ml decision** - Induction Sealer + gasket samples land at Peter today. Peter local fill (28d) or Swift cross-region rush. Without a decision today, 4-5d cover on 500ml at 167/d burn means OOS by 13 Jun.
- **Offer rotation Ballerina → Travel Bag + gift card** - Joel sign-off requested 1 Jun summary. Travel Bag 1,950 pcs = 10d cover at $85-gift attach. Without rotation today the offer goes blind on Tuesday.
- **G3PL Tue 9 Jun fulfilment plan** - 900-order backlog post-public-holiday. STO-BUB-BAG-L at 3-day cover and burning hard. Confirm overtime / priority sequencing with Katrina.
- **STO-BUB-BAG-S OOS in 8 days, no inbound** - identify supply route (add to 07062026 v2? express order?).
- **Joel pay Avi** - ACC-LAB at 22d cover, 15k booklets sitting at Avi. Cuts margin tight given container lands 22 Jun with no Avi PO.

### 🟡 WARNING (act this week)

- **Joel pay AUS 05082026 deposit** - container is draft otherwise. Sally completion window 6 Jul means deposit needed within ~7 days.
- **Joel sign-off AUS 05082026 free gift (10k+) + 6-12 colour collections** - 12 days stale.
- **Daniel verify AUS 07062026 v2 completion** - sheet now shows 10 Jul arrival vs 5 Jul in 1 Jun recap. Confirm with Sally; ULT + MAT invoice + Glass Slipper qty still open.
- **Jake (G3PL):** owes auto-attached packaging SKU pick-fee exclusion reply + PO 9 PACKUP physical count + alt-mailer images. All 12-14 days silent.

### 🟢 MONITOR

- LIQ-MAT-4 5.4/d 7d - confirm whether Matte demand has dropped permanently (offer-attached previously).
- ACC-NAI-MAT 0.4/d 7d - confirms Mani Mat offer pivot. Watch attach rate when Travel Bag becomes the offer.
- KIT-STA-2 stock at 4d cover - substitution to KIT-COM-4 may absorb but track customer-facing impact.

## CASCADING ARRIVAL PROJECTION (KITS)

Kit-only burn 184.7/d (combined 14d 3PL). Target post-arrival cover: 45-75d.

| Stage | Days from today | Total Kit Stock | Cover @ 184.7/d |
|---|---|---|---|
| NOW (8 Jun) | 0 | 1,418 | 7.7d |
| **OOS (16 Jun)** | 8 | 0 | 0 |
| Pre-09052026 arrival (22 Jun) | 14 | 0 (carried zero 6 days) | 0 |
| Post-09052026 (22 Jun) | 14 | +6,104 = 6,104 | 33d |
| Pre-07062026 arrival (10 Jul) | 32 | 6,104 - 18×184.7 = 2,779 | 15d |
| Post-07062026 (10 Jul) | 32 | +5,668 = 8,447 | 46d ✅ |
| Pre-05082026 arrival (5 Aug) | 58 | 8,447 - 26×184.7 = 3,645 | 20d |
| Post-05082026 (5 Aug) | 58 | +8,344 = 11,989 | 65d ✅ |

**Cover slack only opens up after the 07062026 v2 container lands 10 Jul.** Until then we're running at 15-30d cover.

### IF AUS 09052026 ARRIVAL SLIPS (e.g. customs)

5-day slip → 0 kits 16-26 Jun = 10-day total OOS gap (vs 6-day baseline). Adding ~5 days to Heal landing dependency too. Compounds to 12-15 day kit fulfilment void.

10-day slip → 0 kits 16-31 Jun = 15-day OOS gap. **Material revenue impact.** Express bridge would normally apply here but per memory there's no bridge for kits and the 07062026 v2 isn't completing until ~10 Jun.

## PO RECOMMENDATIONS

Target 14-21d kit cover post-arrival. Lead times per [[Lead Times]].

| Action | When | Why |
|---|---|---|
| Sydney Solvents acetone follow-up | Today | Heal fill landing within OP cycle |
| Remove 500ml fill route decision | Today | 4-5d cover at 167/d |
| Avi payment | This week | ACC-LAB 22d cover |
| AUS 05082026 deposit + sign-offs | This week | Sally completion 6 Jul window closing |
| STO-BUB-BAG-S supply review | This week | OOS 16 Jun, no inbound |
| Verify AUS 07062026 v2 completion | This week | 5-day arrival slip to confirm |
| Avi labels next PO size review | Mid-Jun | After current 15k lands, plan next |
| Plan AUS 04092026 reference number | End of Jun | Currently placeholder, growth 1.6x |

## LOCAL FILL FORECAST

**OP Heal cycle:**
- Current fill (started 29 May): est. landing G3PL 22-25 Jun (acetone permitting), qty per 22-04-2026 PO + topup from 25-05-2026 PO.
- Next OP Heal placement: assume ~14d after current fill lands = early Jul. Daniel to align with the post-22 Jun stock recovery curve.

**OP Remove 500ml:**
- Currently blocked on gasket samples (today 8 Jun decision).
- If Peter local: ~28d from go = late Jun / early Jul.
- If Swift cross-region: timing TBD per [[swift-fill-lead-times]] - confirmed CA workflow but cross-region rush is non-standard.

---

**FOLLOW-UP for Sales Analysis to check:**
- Confirm kit DSR isn't being suppressed by G3PL OOS (Shopify orders received vs G3PL ships out gap during the mailer/kit shortage week).
- Confirm whether KIT-ULT-6 7d=0 is genuinely OOS-suppressed (no stock to ship) and Shopify standalone demand is healthy.
- Track ACC-TIP-BAL standalone Shopify burn (vs attach via offer) to confirm offer-pivot timing.
- Travel Bag standalone DSR + projected attach rate post-pivot.
