# 🇬🇧 UK POS Check — 2 Jun 2026

## Data Freshness
- **POS MODEL last updated:** sheet pasted today; `UPDATED` cell wasn't readable, assume AM paste.
- **Shopify:** latest 2026-05-31 (+1 day lag standard).
- **3PL tab (B360):** last valid 2026-06-02 — but **5th consecutive cycle with zero deduction movement** (first_stock == latest_stock across the board). Fulfillable's ShipHero `inventory_changes` feed still capped at 500 edges per response, no cursor pagination implemented yet. Deduction-integrity remains BLIND. Operational DSR = Shopify 14d/30d + W21/W22 kit consumption math.
- **Growth factor:** 1.3x. Kit base 89/d → scaled 115.7/d.
- **Today's kit rate (W22 day-6, 25-31 May):** 99.3/d (-14% vs scaled).
- **Recent W21 (18-24 May):** 104.7/d (-10% vs scaled). **Kit recovery is at parity, not surging — softening into W22.**
- **ShipHero PO export:** pulled fresh — PO 10/11/14/17 (see Step 2).
- **Step 0a Gmail reconcile:** no manual overrides needed; nothing material since last Greg paste. See "ETA confirmations" below.

## Manual Overrides

| SKU | Sheet | Override | Source |
|---|---|---|---|
| (none) | — | — | Nothing post-paste in Gmail. |

## ETA Confirmations (this cycle)

- **Chemence PO 22-04-2026 completion: 3 Jul** (verbal only via Vik — Remy Slack 28 May URGENT). No formal email. **Remy still to chase Vik for written confirmation.**
- **Print Runner PO 17 labels: DPD-delivered to Joel 28 May 13:54-14:54 BST** (per his iCloud forward). **NOT forwarded to Fulfillable yet** — Daniel asked Greg/Remy for ASN 31 May, no resolution. PO 17 still shows 0% received in ShipHero.

## Open Supplier Silences

- **Liquipak (Simon Dickinson):** **~54 days silent** since 9 Apr payment receipt. Final fill PO 02-04-2026 (4,555 units) status unconfirmed via email. Last knowledge: goods ready, awaiting balance payment.
- **Chemence (Vik):** ~34 days silent on email (Slack 28 May has 3 Jul verbal ETA only).
- **Print Runner (Al):** 26 May email silent. DPD delivered 28 May but no formal "PO complete" from Al himself.
- **B360 Mihir/Mason/Chris:** 14+ days silent on packup SKU release.

---

## Step 1 — Stock Position

**Kits**

| SKU | Stock | Model DSR | Scaled (1.3x) | Cov @ Model | Cov @ W22 Shop |
|---|---|---|---|---|---|
| KIT-STA-2 | 12 | 6.5 | 8.5 | 1.8d 🔴 | 12d at 1.0/d |
| KIT-COM-4 | 2,260 | 68.9 | 89.6 | 33d | 39d at 58.4/d |
| KIT-ULT-6 | 2,852 | 40.3 | 52.4 | 71d | 111d at 25.7/d |

- **KIT-STA-2 effectively OOS today** at any meaningful rate. Shopify flow auto-substitutes STA→COM. No action needed unless substitution rate drops.
- **KIT-COM-4 is the workhorse.** 33d cover at model, 39d at actual. UK 03062026 brings +1,484. Comfortable.
- **KIT-ULT-6 has 71d model cover** but only 25.7/d actual selling — true cover ~111d. UK 03062026 brings +700, UK 02072026 +1,148, UK 30082026 +840. Sizing on these containers may be too high if W22 25.7/d holds.

**Liquids (kit-adjusted: Fulfillable picks 1 per kit + standalone Shopify)**

| SKU | Stock | + B360 packup | Total | Model DSR | Cov @ Model | Cov @ kit+std actual |
|---|---|---|---|---|---|---|
| LIQ-BAS-2 | 3,251 | 32 | 3,283 | 144.3 | 22.8d 🔴 | 27d at ~119/d (W22+std14d) |
| LIQ-GLO-4 | 4,744 | 596 | 5,340 | 128.7 | 41d | ~50d at ~108/d |
| LIQ-HEA-5 | 4,684 | 1,653 | 6,337 | 118.3 | 54d | ~64d at ~99/d |
| LIQ-SEA-3 | 2,451 | 369 | 2,820 | 15.6 | 181d | very long |
| LIQ-BON-1 | 458 | 194 | 652 | 6.5 | 100d | very long |
| LIQ-SOA-6 | 535 | 588 | 1,123 | 6.5 | 173d | very long |
| LIQ-MAT-4 | 728 | 469 | 1,197 | 7.8 | 154d | very long |

**Remove / Bowls**

| SKU | Stock | + B360 | Model DSR | Cov @ Model | Shop 30d | Shop 14d | Shop 7d |
|---|---|---|---|---|---|---|---|
| ACC-REM (120ml) | 519 | 43 | 59.8 | 9.4d 🔴 | 4.0 standalone | 2.5 | 1.6 |
| ACC-REM-500 | 3,248 | 571 | 36.4 | 105d | 24.6 standalone | 44.8 | 58.0 |
| ACC-REM-BOW | 3,696 | 1,280 | 66.3 | 75d | 0.6 standalone | 0.6 | 0.7 |
| ACC-REM-BUN-1 | (bundle) | — | — | — | 35.9 | 24.1 | 6.9 |
| ACC-REM-BUN-2 | (bundle) | — | — | — | 10.4 | 8.1 | 6.0 |

- **ACC-REM (120ml)** at 562 total available. Standalone Shopify trails (4/d 30d), but ACC-REM-BUN-1 + standalone = **combined 30d 39.9/d → 14d cover → OOS ~16 Jun.** PO 11 Liquipak final fill brings 4,155 units — pay-by analysis below.
- **ACC-REM-500** comfortable. Shopify spike from 26 May (+161% trend) holds — Bundle attaches and the offer driving demand.
- **ACC-REM-BOW** model 66.3/d is bundle-inflated; standalone 0.6/d. True burn is via ACC-REM-BUN-1 (Remove + Bowl bundle).

**Packaging / Labels / Inserts**

| SKU | Stock | + B360 | Model DSR | Cov @ Model |
|---|---|---|---|---|
| ACC-LAB-UK | 1,505 | 1,396 | 217.1 | **6.9d 🔴** |
| ACC-INS | 6,088 | 7,349 | 106.6 | 57d |
| ACC-THA | 18,959 | 5,246 | 217.1 | 87d |
| STO-BUB-BAG-L | 8,709 | 1,440 | 149.5 | 58d |
| STO-MAI-2 | 6,246 | 3,469 | 110.5 | 57d |
| STO-MAI-BAG-S | 8,582 | 3,555 | 110.5 | 78d |

- **ACC-LAB-UK at 6.9d cover.** PO 17 (Print Runner) brings 10,000 — but DPD delivered to Joel on 28 May, not Fulfillable. **If Joel hasn't forwarded, gap could open ~9 Jun.**

**Free-gift offer SKUs (Mat / Tray / Bag / Tips)**

| SKU | Stock | + B360 packup | If B360 released | Notes |
|---|---|---|---|---|
| ACC-NAI-MAT | 0 | 381 | 381 | Locked. Free-gift dry. |
| ACC-FRE-MANI | 0 | 1,524 | 1,524 | Locked. |
| ACC-TRA-BAG | 0 | 747 | 747 | Locked. |
| ACC-TIP-BAL (Ballerina) | 25 | 217 | 242 | Current offer SKU. **Effectively OOS today.** 4-5d burn at offer rate. |
| ACC-TIP-COF (Coffin) | 978 | 1,389 | 2,367 | Next offer SKU (Remy Asana task due today). |
| ACC-TIP-SQU (Square) | 449 | 717 | 1,166 | Was offer pre-Ballerina. Holds. |
| ACC-TIP-ALM (Almond) | 545 | 742 | 1,287 | Model 126.1/d looks stale (Shopify 3.0/d). |
| ACC-TIP-STI (Stiletto) | 179 | 356 | 535 | Not in active offer rotation. |

---

## Step 2 — ShipHero PO Status (PO 10 / 11 / 14 / 17)

**All 4 POs pending. 0% received across the board.**

### PO 10_UK 03062026 — pending — Primary warehouse
- po_date: 2026-06-13 | 59 line items | 84,425 units
- Contents: 1,484 COM + 700 ULT + 448 STA + 8,000 BAS empties + 8,000 GLO empties + 10k×3 empty glass parts (lid/brush/inner) + 5,600 ACC-THA + 5,280 STO-MAI-2 + 4,000 STO-MAI-BAG-S + 2,300 STO-BUB-BAG-L + 432 LIQ-SEA-3 + 216 LIQ-BON-1 + ~21,400 colours
- **Cross-reference:** Slack says UK 03062026 + UK 02072026 consolidated as a single 40HQ, arrival 15 Jul. The ShipHero PO is the 03062026 half.
- **No received movement.** Container is in production, vessel TBD. Sheet shows 21 May completion / 15 Jul arrival — consistent.

### PO 11_02-04-2026_Liquipack — pending — Primary warehouse
- po_date: 2026-04-23 | 2 line items | 4,555 units | subtotal £3,973.30
- Contents: **4,155 ACC-REM (120ml) + 400 ACC-REM-500**
- **Critical: this is the Liquipak final fill.** Goods ready per 27 May Daniel; balance £3,973.30 awaiting Joel payment.
- **No received movement.** Confirms goods haven't shipped yet.

### PO 14_UK02072026 — pending — Primary warehouse
- po_date: 2026-07-14 | 67 line items | 280,311 units (largest of the 4)
- Contents: 1,316 COM + 1,148 ULT + 336 STA + **massive component load (60k×3 empty glass parts + 30k×2 Base/Glow bottles for Chemence next cycle)** + 5,600 ACC-THA + 4,950 ACC-GLA-FIL + 3,000 STO-MAI-BAG-S + 2,640 STO-MAI-2 + 1,680 ACC-INS + 1,400 STO-BUB-BAG-L + 1,080 LIQ-SEA-3 + 648 LIQ-MAT-4 + 216 LIQ-BON-1 + 216 LIQ-SOA-6 + 1 ACC-TIP-BAL + ~10k colours
- **This is the 02072026 half of the consolidated 40HQ.** Combined PO 10 + PO 14 lands at Fulfillable 15 Jul per Slack.

### PO 17 - 14-05-2026 | Print Runner — pending — Primary warehouse
- po_date: 2026-05-30 | 1 line item | 10,000 ACC-LAB-UK
- **No received movement** despite DPD delivery 28 May.
- **The 10k labels physically arrived in UK on 28 May but went to Joel's address per his iCloud forward** — not Fulfillable. PO 17 will only flip from pending to received once Joel forwards (or once ShipHero ASN is created with Fulfillable as receiver).

### Practice-run takeaway

For UK, the ShipHero PO ID maps to the `PO N_` prefix in `po_number`, not the API's `legacy_id` (which is a 7-digit internal). Use the PO number prefix to pin a specific PO. **What this view adds vs the POS MODEL sheet:**
- Confirms whether anything has been physically checked in (PO 17 not yet at Fulfillable despite DPD delivery date)
- Confirms what's actually on the PO (PO 11 shows 4,155+400 Liquipak units, matches Slack)
- Gives 0% / partial / 100% visibility per SKU at the moment of pull
- **Worth running each cycle** alongside the POS MODEL to catch ASN gaps like PO 17.

---

## Step 4 — Corrected Days Cover (confirmed available, no double-counting)

Confirmed available = POS MODEL `g3pl_on_hand` (Fulfillable live stock). B360 packup excluded — locked behind Joel balance.

| SKU | Confirmed | Operating DSR | Confirmed Cover | Flag |
|---|---|---|---|---|
| KIT-STA-2 | 12 | 6.5 model / 1.0 Shop 7d | 1.8d / 12d | 🔴 OK if substitution holds |
| ACC-LAB-UK | 1,505 | 217.1 | **6.9d** | 🔴 PO 17 not yet at Fulfillable |
| ACC-REM | 519 | 39.9 combined 30d | **13d** | 🔴 Liquipak fill due — pay-by below |
| LIQ-BAS-2 | 3,251 | 144.3 model / ~119 actual | 22.8d / 27d | 🔴 Chemence 3 Jul gap |
| ACC-TIP-BAL | 25 | offer-attach rate | <1d | 🔴 Already burning |
| ACC-NAI-MAT / FRE-MANI / TRA-BAG | 0 | n/a | OOS | 🔴 Locked in B360 |

---

## Step 5 — Packaging Anomalies

- **No 3PL deduction movement detected** in B360 tab — 5th consecutive cycle BLIND. Cannot surface anomalies.
- Cross-check: Fulfillable receives + ships independently; current data only captures B360 packup snapshot.

---

## Step 6 — Container / Order Status Cross-Reference

| Ref | Sheet Status | Sheet Date | ShipHero | Reality |
|---|---|---|---|---|
| UK Powder Room | Landed 13-14 May | — | PO 13 closed | ✅ Booked in 19 May. |
| Chemence PO 12 (10-03-2026) | Landed | — | PO 12 closed | ✅ Done. |
| Chemence PO 22-04-2026 | In Production, completion 17 Jun | 17 Jun | (no separate PO yet) | **🔴 Sheet stale.** Vik verbal 28 May: completion 3 Jul. |
| UK 03062026 + UK 02072026 | In Production, arrival 15 Jul | 15 Jul | PO 10 + PO 14 pending | Consolidated 40HQ. Sheet matches Slack. |
| UK 30082026 | (newly added) | place 27 May, arrive 30 Aug | not yet in ShipHero | **🔴 Sheet may not reflect Daniel's 27 May PO yet** — user confirmed placed. |
| UK 29092026 | Planned | 29 Sep | — | After 30082026. |
| Liquipak PO 02-04-2026 | Ordering | — | PO 11 pending | Awaiting balance payment. |
| Print Runner PO 14-05-2026 | placed | — | PO 17 pending | **DPD delivered to Joel 28 May, not Fulfillable.** |

---

## Step 7 — Local Fill Status

**Chemence (PO 22-04-2026) — Base 8,000 + Glow 6,000**
- Status: Ordering. Vik silent on email 34 days; verbal completion ETA 3 Jul (Slack 28 May, not in writing).
- **At 5 business days ship-to-Fulfillable = 10 Jul arrival.**
- LIQ-BAS-2 OOS at 24-29 Jun (model 144.3/d to actual ~119/d range) → **gap 11-16 days.**

**Liquipak (PO 02-04-2026) — 4,155 ACC-REM + 400 ACC-REM-500**
- Status: Ordering / goods ready / awaiting balance payment £3,973.30.
- Lead = Joel pays → goods ship → ~5 business days transit (≈ 7 calendar days) to Fulfillable.
- See pay-by analysis below.

**Oils4Life — Heal**
- No active PO. Stock 4,684 / 39.6d cover. Dale silent 21d+ from 26 May Recap; no new chase visible this week. Plan next fill in next cycle.

---

## Step 8 — Stock-Out Forecast

### 🔴 STOCKOUT BEFORE ARRIVAL (gap < 0)

| SKU | Stock | DSR | Stocks Out | Next Inbound | Arrival | Gap |
|---|---|---|---|---|---|---|
| LIQ-BAS-2 | 3,251 | 144.3 / ~119 actual | 24-29 Jun | PO 22-04-2026 (Chemence) | ~10 Jul | **-11 to -16d** |
| ACC-REM | 519 | 39.9 combined | ~16 Jun | PO 11 (Liquipak) | depends on Joel pay | varies |
| ACC-TIP-BAL | 25 | offer-driven | NOW | none active | — | already OOS |
| ACC-NAI-MAT | 0 | offer-driven | OOS | B360 release | depends on Joel balance | varies |
| ACC-FRE-MANI | 0 | — | OOS (offer dry) | B360 release | depends | — |
| ACC-TRA-BAG | 0 | — | OOS (offer dry) | B360 release | depends | — |

### 🟡 TIGHT (gap 0-7 days)

| SKU | Stock | DSR | Cover | Next Inbound | Gap |
|---|---|---|---|---|---|
| ACC-LAB-UK | 1,505 | 217.1 | 6.9d | PO 17 (Print Runner) | Tight — Joel must forward labels to Fulfillable this week |

### 🟢 SAFE

All others (kits, GLO/HEA, packaging, ACC-REM-500 etc.) have 30+ days cover at actual rate.

---

## Step 8a — Liquipak Pay-By Calculation (user's specific question)

**Assumptions:**
- ACC-REM stock today: 519 at Fulfillable + 43 in B360 packup (treat the 43 as bonus, not in cover base) → **operating stock 519**.
- 5 business days transport (Liquipak ships → arrives Fulfillable) ≈ **7 calendar days**.
- Goods land in pending status, need ~1-2 days to book in. Build a 2-day buffer.

**At three plausible burn rates:**

| Rate basis | DSR/d | Days cover | OOS date | Pay-by (OOS - 9d incl. buffer) |
|---|---|---|---|---|
| Model 59.8/d (bundle-inflated) | 59.8 | 8.7d | **~11 Jun** | **~2 Jun (today)** |
| Combined 30d (BUN-1 35.9 + std 4.0) | 39.9 | 13.0d | **~15 Jun** | **~6 Jun (Fri)** |
| Combined 14d (BUN-1 24.1 + std 2.5) | 26.6 | 19.5d | **~21 Jun** | **~12 Jun** |

**Recommendation:** **Pay Monday 9 Jun.**
- A Friday 6 Jun payment doesn't gain much real ship-time: Liquipak processes through the weekend at best Monday morning, so a Fri-evening payment effectively ships Mon-Tue same as a Mon payment.
- Pay Mon 9 Jun → ships Tue 10 Jun → 5 biz days transit → arrive Fulfillable Mon 16 Jun → book-in Tue-Wed 17-18 Jun.
- At combined 30d rate 39.9/d: stock runs ~15 Jun. Arrival 16 Jun + 1-2d book-in = **0-3 day OOS gap**. Acceptable buffer.
- If model rate 59.8/d proves correct (bundle-inflated, unlikely but possible): OOS 11 Jun → 5-7 day OOS gap regardless of pay date. Express ship from Liquipak would be only option.

This is a **this-week** item — paying anywhere from today through Mon 9 Jun gives the same approximate Fulfillable arrival. Don't slip past Monday.

---

## Step 8b — Chemence Base Gap Mitigation Options

LIQ-BAS-2 14-day OOS gap (29 Jun OOS at actual rate → 10 Jul Chemence arrival).

| Option | Feasibility | Notes |
|---|---|---|
| Push Vik to compress to ~20 Jun completion | Low | 35 days silent on email; verbal commitment only at 3 Jul. Would need Joel direct intervention. |
| Pull empty Base bottles to Chemence early | Medium | PO 10 (UK 03062026) has 5k empty Base bottles already on container — but it's not landing until 15 Jul, too late. Need to source from elsewhere or air-freight. |
| Cross-region Base pull (AUS/CA) | Low | AUS has its own Base tight at 09052026 arrival; CA Swift fills Heal/Remove only. No spare Base in either region. |
| Kit-throttle (slow kit dispatches in 22-29 Jun window) | Medium | Operationally messy. Backorder rate would spike. Would buy ~3-5 days. |
| Free-issue acceleration to Chemence | Medium | Daniel had a tracker 29 Apr; needs Vik to confirm what's outstanding. |
| Accept the OOS gap | Default | Customer-visible. Kits cannot be assembled without Base. |

**Recommendation:** Joel to email Vik immediately requesting (a) written 3 Jul confirmation, (b) options for express dispatch of completed batch + later top-up, (c) compressed timeline cost. Daniel/Remy to model kit-throttle as backstop.

---

## Step 9 — What Needs Action

### 🔴 CRITICAL (act today)
1. **Joel: pay Liquipak balance £3,973.30 by Mon 9 Jun.** PO 11 has 4,155 Remove 120ml + 400 Remove 500ml. Final fill ever; cannot slip past Monday (weekend doesn't gain ship-time, so Fri vs Mon are functionally equivalent).
2. **Joel: chase Vik for written 3 Jul completion confirmation + express dispatch options.** LIQ-BAS-2 14-16 day OOS gap (29 Jun → 10 Jul) is the single biggest risk.
3. **Joel: forward Print Runner ACC-LAB-UK 10k delivery to Fulfillable** (DPD landed at his address 28 May). ACC-LAB-UK at 6.9d cover.
4. **Joel: pay B360 stock-out balance** to unlock the free-gift bridge (Mat 381 + Tray 1,524 + Travel Bag 747 + Coffin Tips 1,389 + Ballerina 217). Ballerina effectively OOS today.
5. **Remy: execute Asana "Change UK free gift back to Coffin Tips"** — due today. Coffin has 978 standalone + 1,389 in B360 packup.

### 🟡 WARNING (act this week)
1. **Daniel/Joel: decide Chemence gap mitigation.** Kit-throttle, express request to Vik, or accept OOS.
2. **Joel: sign off UK 30082026 free-gift qty (min 7k) + 6-12 new colour collections.** PO already placed (per user), but downstream content depends on Joel sign-off.
3. **Joel: pay Fulfillable £10k remaining balance** (committed 28 May "next week").
4. **Daniel: Liquipak replacement Path A/B/C decision.** 20 days silent. Without a replacement filler, ACC-REM 120ml has no fill cycle beyond PO 11.
5. **Remy: chase Vik for formal email** confirming 3 Jul completion (verbal-only is fragile).
6. **Remy: Ireland IOSS shipping mapping** (per Roisin 1 Jun).

### 🟢 MONITOR
- ACC-REM-500 +161% trend from 26 May still holds (58/d 7d). Watch for sustained demand vs landed fill.
- W22 softening to 99/d kit — early-week noise or trend? Sales Analysis to confirm.
- POS MODEL DSR refresh outstanding (tips look most stale: ACC-TIP-ALM 126.1 vs Shop 3.0).
- ShipHero `inventory_changes` cursor pagination — still blocked, 5th cycle without deduction-integrity visibility.

---

## Step 10a — Local Fill Forecast

**Chemence Base/Glow next cycle (post-PO 22-04-2026):**

User intends to place next Chemence PO at **~8,000 BAS + ~6,500 GLO** (per 2 Jun conversation). Target: land with **14-21 days cover remaining** of prior fill.

Working back from the 22-04-2026 PO landing ~10 Jul (treating any pre-arrival OOS gap as zero-stock):

| Rate basis | Burn/day | Post-arrival days cover | Next OOS | Next fill **land by** | **Vik complete by** (7d ship) |
|---|---|---|---|---|---|
| W22 actual (99.3 kit + 19.4 Shop 14d) | 119/d | 67d | ~15 Sep | 25 Aug (21d) — 1 Sep (14d) | **18-25 Aug** |
| Scaled aspirational (115.7 + 20.8) | 136.5/d | 59d | ~6 Sep | 16-23 Aug | **9-16 Aug** |
| POS MODEL (144.3, already kit-incl) | 144.3/d | 55d | ~3 Sep | 13-20 Aug | **6-13 Aug** |

GLOW math runs ~3 days earlier than BASE because of slightly faster relative burn (4,744 g3pl + 596 B360 packup vs 6,000 incoming fill is tighter).

**Recommendation for Vik brief:**
- **Base 8,000 + Glow 6,500 — completion required at Chemence by Friday 15 Aug** (mid-range across the three rate scenarios; matches GLOW 17 Aug at 21d-buffer end of W22 actual rate, and tracks aspirational ~16 Aug at 14d buffer).
- Goods at Fulfillable by ~22 Aug (5 biz days ship).
- **If kit demand recovers to scaled rate (115.7/d): pull complete-by forward to Friday 8 Aug.**
- Place the PO this week. Vik historically took ~9 weeks on PO 22-04-2026 (placed late Apr, completing 3 Jul) — a 15 Aug completion from a 5 Jun placement = ~10 weeks. **No slack for Vik to slip.**

**Hedge:** if Vik signals she can't hit 15 Aug, the fallback is to size the PO larger (e.g. 10,000 BAS / 8,500 GLO) so the post-22-04-2026 stock-fill cycle extends further into Sep and gives Vik more runway. Trade-off is higher Fulfillable holding qty.

**Liquipak next cycle: N/A.** PO 11 is the last Liquipak fill ever per region notes. Replacement filler decision still stalled.

**Oils4Life Heal next cycle:**
- Heal cover post-Chemence (no change at this PO) = 4,684 / 99/d actual = 47d → OOS late July.
- Remy to outbound Dale (Oils4Life) this week for next fill timing.

---

## Step 10c — Cascading Arrival Projection

Operating at W22 kit rate 99.3/d (-14% vs scaled 115.7). Each kit consumes 1 BAS + 1 GLO + 1 HEA + 1 INS + 1 LAB + 1 THA.

| | NOW (2 Jun) | After Chemence ~10 Jul | After PO 10+14 (15 Jul) | After UK 30082026 (30 Aug) |
|---|---|---|---|---|
| KIT-STA-2 | 12 | -85 (substitution-fed) | 783 | 783 |
| KIT-COM-4 | 2,260 | -1,260 (40d burn @ 58.4 Shop 7d) | -1,944 + 1,316 = -628 | -628 + 3,584 = 2,956 |
| KIT-ULT-6 | 2,852 | 1,860 (40d burn @ 25.7 Shop 7d) | 1,860 + 1,148 = 3,008 | 3,008 + 840 = 3,848 |
| **LIQ-BAS-2** | **3,283** | **(OOS gap 29 Jun → 10 Jul) → 8,000 post-fill = 7,000** | **+0 = 7,000** | **+0 (no Base in CN containers)** |
| LIQ-GLO-4 | 5,340 | -370 + 6,000 = 5,630 | +0 = 5,630 | +0 = 5,630 |
| LIQ-HEA-5 | 6,337 | 2,377 (40d burn @ 99/d) | +0 = 2,377 | +0 = 2,377 (Oils4Life next cycle needed) |
| ACC-REM (120ml) | 519 | -1,077 + 4,155 (Liquipak) + post-burn 30d at 39.9/d = ~2,400 | ~2,000 | ~500 (PO 11 last fill ever) |
| ACC-LAB-UK | 1,505 | -8,180 + 10,000 (PR 17) at ~99/d kit = ~3,500 (if Joel forwards) | +0 = ~3,500 | +0 = ~0 |

**⚠️ Watch items at this trajectory:**
- **LIQ-BAS-2** 14-16 day OOS gap is non-negotiable without intervention.
- **KIT-COM-4** dips negative ~7-10 Jul before PO 10/14 lands 15 Jul. Sub-1d gap.
- **ACC-LAB-UK** depletes again ~Aug if no second Print Runner PO placed.
- **LIQ-HEA-5** drops to 24d cover by mid-Aug if no Oils4Life fill placed by then.

---

## Step 10b — PO Recommendations

| Item | Recommended action | Latest place date |
|---|---|---|
| Liquipak balance | Pay this week | **Mon 9 Jun** (weekend doesn't gain ship-time) |
| Print Runner forward | Joel to forward DPD shipment to Fulfillable | This week |
| B360 stock-out balance | Joel to clear | This week (free-gift bridge) |
| Vik written confirmation + express | Joel email today | Today |
| Oils4Life next Heal fill | Remy outbound to Dale | This week |
| Next Print Runner ACC-LAB-UK PO | Place ~late Jul (after PO 17 books in) | ~22 Jul |
| Next Chemence fill (8k BAS + 6.5k GLO) | Place THIS WEEK; brief Vik "complete by 15 Aug" (8 Aug if surge) | Place by ~5 Jun for ~10wk lead |

---

## Follow-Up Items

**Immediate:**
- [ ] Joel: pay Liquipak by Mon 9 Jun (£3,973.30)
- [ ] Remy/Daniel: place next Chemence PO this week (8k BAS + 6.5k GLO; brief Vik "complete by 15 Aug")
- [ ] Joel: forward Print Runner labels to Fulfillable
- [ ] Joel: chase Vik for 3 Jul written + express
- [ ] Joel: pay B360 balance
- [ ] Remy: execute Coffin Tips offer swap (Asana due today)
- [ ] Remy: chase Vik for formal email

**By end of week:**
- [ ] Daniel: Chemence gap mitigation decision
- [ ] Daniel: Liquipak replacement Path A/B/C
- [ ] Joel: pay Fulfillable £10k remaining
- [ ] Joel: UK 30082026 sign-off (free-gift + colours)
- [ ] Remy: Ireland IOSS mapping

**Ongoing:**
- [ ] ShipHero `inventory_changes` cursor pagination work (5th cycle blind)
- [ ] Greg: POS MODEL DSR refresh (tips most stale; ACC-TIP-ALM 126→3, kit mix STA/COM/ULT shift)
- [ ] Pull ShipHero PO data each POS Check cycle (PO 10/11/14/17 practice run worked — fold into standard procedure)
