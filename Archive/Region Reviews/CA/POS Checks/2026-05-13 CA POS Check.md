# POS Model Check — 🇨🇦 CA — 13 May 2026

> Source xlsx re-pulled 13 May 12:16 AEST. POS MODEL `UPDATED` cell = 13 May 2026 (today, fresh). 3PL tab last valid date = 13 May 2026 (today, fresh). Growth factor (J9) = 1.5x, kit base 80/d (STA 21 + COM 41 + ULT 18) → scaled 120/d.
>
> **User-confirmed inputs (13 May):**
> - CA 21062026 deposit **PAID**. Est completion **28 May**, est arrival **22 Jul** (sheet, ~55d transit). Container is 1.5x / 20GP, no kits.
> - Swift Heal + Remove 500ml fill **not placed - going very lean**. Watch sales past 7-10d closely (new site + new offer live since 6 May).
> - Mixam 1,300pcs ACC-LAB-CA reprint **in production** (7 May Mixam email MX2029340, user-confirmed on the way).
> - Univar acetone refund **CLOSED - all done** per user 13 May.
> - 3 at-risk colours (Blue Moon / Peony Puff / Glacier Glow) still in scope.
> - CA 25072026 PO place-date looks accurate; review what stocks out before it lands.

## Manual overrides applied
- ACC-LAB-CA inbound +1,300 from Mixam reprint (in production, ETA unconfirmed but assumed within 4-6 weeks).
- Sheet shows 22 Jul arrival for CA 21062026 — reconciled with user-confirmed 28 May completion + 55d sheet transit. Treating as 22 Jul for cover math.
- No Univar acetone refund line to action (closed).

---

## ⚡ HEADLINE — NEW STORE LIFT IS REAL

**7d kit DSR = 118.3/d vs scaled target 120/d (-1%, effectively at parity).** Up from 14d 82.7/d (-31%) and 30d 64.0/d (-47%). Effective growth factor:
- 7d: **1.48x** (matches 1.5x model)
- 14d: 1.03x
- 30d: 0.80x

This is the first time in 9 weeks CA has hit scaled target. The new store + offer launched 6 May; this is 7 days of post-launch data. **Don't recalibrate on it yet** — but the entire "lean / overstock" sizing logic from the 6 May review is now in question. Every downstream forecast in this report uses the **higher of 7d / 14d** rate as the operational risk number, not 30d.

By kit:
- KIT-STA-2: 7d 12.7/d (vs model 31.5, -60%) — STA underselling
- KIT-COM-4: 7d **80.9/d** (vs model 61.5, **+32%**) — COM driving the surge
- KIT-ULT-6: 7d **24.7/d** (vs model 27.0, -9%) — recovering

The lift is concentrated in COM-4. If this rate sustains, it pulls forward every COM-related forecast.

---

## STOCK POSITION — Two-rate cover view

Format: Stock | model DSR scaled @ 1.5x | actual rate (max of 7d/14d) | cover @ scaled | cover @ actual.
Heal and Instructions shown kit-adjusted (standalone + kit pulls).

### Kits

| SKU | Stock | Scaled DSR | Actual (max 7d/14d) | Cov @ scaled | Cov @ actual |
|---|---|---|---|---|---|
| KIT-STA-2 | 4,113 | 31.5/d | 12.7/d | 131d | **324d** |
| KIT-COM-4 | 7,501 | 92.3/d | **80.9/d** | 81d | **93d** ⚠️ |
| KIT-ULT-6 | 3,146 | 40.5/d | 24.7/d | 78d | **127d** |
| **Kits total** | 14,760 | 164/d | **118.3/d** | 90d | **125d** |

**Flag:** KIT-COM-4 cover at 7d rate (93d) is below the 109d gap to CA 25072026 arrival. 16d stockout risk if 7d rate sustains. At 14d rate (54.1/d) cover is 139d — safe. **Decision input.**

### Liquids (kit-adjusted for Heal)

| SKU | Stock | Scaled DSR | Actual rate | Cov @ scaled | Cov @ actual |
|---|---|---|---|---|---|
| LIQ-HEA-5 | 7,385 | 191.3/d kit-adj | **119.6/d** kit-adj 7d | 39d | **62d** 🟡 |
| LIQ-BAS-2 | 1,356 | 38.3/d | 10.2/d 14d | 35d | 133d |
| LIQ-SEA-3 | 1,026 | 27.0/d | 7.1/d | 38d | 145d |
| LIQ-BON-1 | 990 | 18.0/d | 3.4/d | 55d | 291d |
| LIQ-GLO-4 | 1,492 | 22.5/d | 5.4/d | 66d | 276d |
| LIQ-MAT-4 | 1,220 | 15.8/d | 3.7/d | 77d | 330d |
| LIQ-SOA-6 | 897 | 18.0/d | 2.7/d | 50d | 332d |
| LIQ-SEN-2 | 721 | 9.0/d | 4.5/d | 80d | 160d |
| LIQ-SEN-4 | 595 | 6.8/d | 3.1/d | 88d | 192d |

**Flag:** LIQ-HEA-5 at 119.6/d kit-adjusted 7d = 62d cover. CA 21062026 (70d to arrival) brings ZERO Heal (filled locally). 25072026 also has zero. **OOS gap of ~8 days if 7d rate sustains, before Swift fill lands.** Lean-skip decision needs re-evaluation.

### Remove products

| SKU | Stock | Scaled DSR | Actual rate | Cov @ scaled | Cov @ actual |
|---|---|---|---|---|---|
| ACC-REM-500 | 2,647 | 112.5/d | **81.9/d** Shopify + **7.6 bundle** = **89.5/d** combined | 24d | **30d** 🔴 |
| ACC-REM | 3,976 | 69.8/d | 4.0/d 14d (standalone) + 11.6 bundle = 15.6/d | 57d | 255d |
| ACC-REM-BOW | 5,435 | 90.0/d | 2.4/d 14d + bundle | 60d | high |

**Cross-check:** 3PL deduction data 10-13 May = **109-145/d** on ACC-REM-500 (1.1-1.4x benchmark of 100). 4 consecutive days. At ~125/d 3PL rate, real cover is **21 days** — OOS ~3 Jun. **Both 21062026 and 25072026 carry zero ACC-REM-500.** Swift Remove 500ml fill is the ONLY restock path.

### Inserts & packaging (3PL deduction only, no Shopify)

| SKU | Stock | Model | 21062026 | 25072026 | Notes |
|---|---|---|---|---|---|
| ACC-LAB-CA | 6,643 | 231/d (model 1x) | 0 | 0 | At order-rate ~150/d, ~44d cover. Mixam +1,300 reprint = +8d. **Reorder by mid-Jun.** |
| ACC-THA | 33,464 | 231/d | 11,200 | 8,400 | Healthy, 97d at model |
| ACC-INS | 22,364 | 120/d kit-adj | 0 | 3,600 | Safe, 189d cover at 7d kit-adj 118.3 |
| STO-BUB-BAG-L | 8,304 | 120/d | 0 | 0 | 70d at model. Aligned with kit pace. |
| STO-MAI-BAG-S | 9,710 | 114/d | 10,000 | 6,000 | Healthy |
| STO-MAI-2 | 9,750 | 114/d | 10,450 | 5,280 | Healthy |
| STO-BUB-BAG-S | 0 | - | 0 | 0 | 247 supplies own, excluded |

### Colours at risk before CA 21062026 lands (70d to arrival)

All 6 of these are restocked on 21062026 — gap closes after arrival. Express bridge not in scope per recap (no Sally express, cash-tight).

| SKU | Name | Stock | 7d | 14d | Cov | 21062026 | 25072026 | Gap |
|---|---|---|---|---|---|---|---|---|
| POW-GLA-CS02 | Glacier Glow | 7 | 3.9 | 3.1 | **2d** | 600 | 400 | -68d 🔴 |
| POW-BLU-ZGD22 | Blue Moon | 121 | 4.4 | 4.7 | 26d | 600 | 200 | -44d 🔴 |
| POW-PEO-SH07 | Peony Puff | 133 | 4.3 | 4.5 | 30d | 800 | 400 | -40d 🟡 |
| POW-LEM-ZGD01 | Lemonade | 151 | 3.0 | 2.9 | 50d | 600 | 200 | -20d 🟡 |
| POW-SAP-11933 | Sapphire Nights | 219 | 4.1 | 2.6 | 53d | 600 | 400 | -17d 🟡 |
| POW-SIL-11943 | Silent Eclipse | 173 | 2.9 | 2.4 | 60d | 800 | 200 | -10d 🟡 |

**Decision input:** Glacier Glow effectively OOS now (2d). User confirmed treating these as flagged. No express bridge — accept 40-68d OOS windows on the 3 worst.

### 3PL deduction anomalies (sustained, not single-day)

- **POW-CLE-193 (Clear): 4 consecutive days 99-208/d deducted** (3-6x benchmark of 35). Stock 14,001 → 70d cover at 200/d. **Shopify 7d only 29.3/d.** The gap suggests Clear is being auto-pulled at kit-component level (e.g. default colour for missing customer selection). Greg/Daniel to investigate.
- **POW-JUS-449 (Just Friends): 5 consecutive days 83-183/d deducted** (2-5x benchmark). Stock 10,704 → 63d cover at 170/d. Shopify 7d 6.1/d. Same anomaly pattern.
- **ACC-REM-500: 4 consecutive days 109-145/d** (1.1-1.4x). Confirms real demand 90-130/d range (matches 7d 81.9 + bundle 7.6 = 89.5).

---

## CONTAINER / ORDER STATUS

### CA 21062026 (Birthday Sale) — In Production
- **Est completion 28 May** (user-confirmed; sheet shows 28 May too)
- **Est arrival 22 Jul** (sheet, 55d transit)
- **Deposit PAID** (user-confirmed, was 15d overdue at 6 May review)
- **Manifest:** 0 kits | 8,640 liquids | 14,400 colours | 4,000 ACC-REM-BOW | 11,200 ACC-THA | 20,450 STO | 410 other ACC = **59,100 units total**, 20GP @ 1.5x
- **Slack/Gmail since 6 May:** No new operational chatter visible. Sally bottles and B115 jars status unclear from CA-channel - assumed running with the production timeline.

### CA 25072026 — Planned
- **Est completion 6 Jul** (sheet; user 13 May "PO place date looks accurate")
- **Est arrival 30 Aug** (sheet, 55d transit)
- **Manifest:** 5,404 kits (STA 1,400 + COM 2,800 + ULT 1,204) | 4,968 liquids | 46,200 colours | 2,700 ACC-REM-BOW | 3,600 ACC-INS | 8,400 ACC-THA | 11,280 STO | 3,760 other ACC = **86,312 units total**
- **Sizing concern:** at 7d kit rate (118.3/d), 5,404 kits = ~46 days post-arrival cover. The cycle to next container (planned 13 Aug arrival, completion 29 Jun) needs to bridge.

### 2 further planned shipments
- Unnamed, est completion 29 Jun → arrival 13 Aug
- Unnamed, est completion 15 Jul → arrival 29 Aug

These should be confirmed/named before placement; treat as planned only.

---

## LOCAL FILL STATUS

### Swift Innovations — Heal + Remove 500ml — DECISION POINT

**Current direction (user 13 May):** going very lean, no PO placed yet, watching sales 7-10d.

**Data 7 days into the new store / offer:**

| SKU | Stock | 7d demand | 14d demand | Cover @ 7d | Cover @ 14d | Next inbound | Gap to next CN |
|---|---|---|---|---|---|---|---|
| LIQ-HEA-5 | 7,385 | 119.6/d kit-adj | 84.0/d kit-adj | 62d (OOS ~14 Jul) | 88d (OOS ~9 Aug) | none on CN | n/a — local fill only |
| ACC-REM-500 | 2,647 | 89.5/d combined (Shopify+bundle) / 125/d at 3PL | 60.1/d combined | 30d (OOS ~12 Jun) | 44d (OOS ~26 Jun) | none on CN (zero on 21062026 + 25072026) | n/a — local fill only |

**Lead time:** Swift fill ~5-7d from fill completion to 247 restock (per memory). Add filling + ingredient lead = realistically ~3-4 weeks total if ingredients on hand.

**Risk if skip-fill decision holds:**
- LIQ-HEA-5: at 7d rate, OOS 14 Jul (12d before 21062026 lands but 21062026 brings ZERO Heal). At 14d rate, OOS 9 Aug. Either way no CN bridge - Swift is the only mechanism.
- ACC-REM-500: at 7d combined rate, OOS 12 Jun. At 3PL rate (125/d), OOS 3 Jun. At 14d rate, OOS 26 Jun. **Nothing in any pipeline.** Could be a 6-10 week OOS gap if waited until 25072026 (zero ACC-REM-500 there either).

**Recommendation:** Don't skip. Place a lean fill THIS WEEK to bridge. Sizing options:

**Heal** (lead 21-28d Swift):
- Lean 5,000 → +42d at 119.6/d 7d (or +60d at 14d 84/d)
- Recommended 7,500 → +63d at 7d / +89d at 14d
- Conservative 10,000 → +84d / +119d

**Remove 500ml** (lead 21-28d Swift):
- Lean 3,000 → +33d at 89.5/d (or +50d at 60.1/d 14d)
- Recommended 5,000 → +56d / +83d
- Conservative 7,500 → +83d / +125d

User's stated lean preference + the 7d-might-not-sustain caveat → **Recommended Heal 7,500 + Remove 500ml 5,000**. Heavy enough to bridge to ~31 Aug at 7d rate, ~early Sep at 14d. If 7d rate fades back to 14d/30d levels, becomes overstock by ~30d only — manageable.

This contradicts the user's "no action yet" decision; flag explicitly. The decision was made on the 6 May numbers; 7 days of new-store data has changed the math.

### Mixam Canada — ACC-LAB-CA reprint
- 1,300pcs in production (order MX2029340, in production 7 May)
- ETA not given. Assume 4-6 weeks from 7 May = ~early-mid Jun delivery.
- Stock-on-hand 6,643 + 1,300 reprint = 7,943. At ~150/d order rate = ~53d cover from today.
- **Reorder needed by mid-Jun** (1-2 weeks before reprint arrives to maintain continuity). Recommend Daniel/Remy place a 10,000pc Mixam reorder this week given ~14-21d local print lead.

---

## STOCK-OUT FORECAST

### Stockout before next inbound arrives (gap < 0)

| SKU | Stock | Rate | OOS in | Next inbound | Arrives | Gap |
|---|---|---|---|---|---|---|
| POW-GLA-CS02 | 7 | 3.9/d | now | CA 21062026 (600) | 22 Jul | -68d 🔴 |
| LIQ-HEA-5 | 7,385 | 119.6/d kit-adj | 62d | Swift fill (TBD) | TBD | TBD - **fill not placed** |
| ACC-REM-500 | 2,647 | 89.5/d combined | 30d | Swift fill (TBD) | TBD | TBD - **fill not placed** |
| POW-BLU-ZGD22 | 121 | 4.7/d | 26d | CA 21062026 (600) | 22 Jul | -44d 🔴 |
| POW-PEO-SH07 | 133 | 4.5/d | 30d | CA 21062026 (800) | 22 Jul | -40d 🟡 |
| POW-LEM-ZGD01 | 151 | 3.0/d | 50d | CA 21062026 (600) | 22 Jul | -20d 🟡 |
| POW-SAP-11933 | 219 | 4.1/d | 53d | CA 21062026 (600) | 22 Jul | -17d 🟡 |
| POW-SIL-11943 | 173 | 2.9/d | 60d | CA 21062026 (800) | 22 Jul | -10d 🟡 |
| ACC-LAB-CA | 6,643 | 150/d est | 44d | Mixam reprint 1,300 + reorder TBD | early-mid Jun | tight - reorder this week |
| KIT-COM-4 | 7,501 | 80.9/d 7d | 93d | CA 25072026 (2,800) | 30 Aug | -16d at 7d, +85d at 14d (54.1) |

### After CA 21062026 lands (22 Jul) — anything still at risk before CA 25072026 lands (30 Aug)?

**None** — all colours flagged above are restocked sufficiently by 21062026 to bridge to 25072026. ACC-REM-500 / Heal still no inbound (Swift only). KIT-COM-4 only at risk if 7d rate sustains 109+ days.

---

## CASCADING ARRIVAL PROJECTION

Target cover 45-75 days. Actual rate = max(7d, 14d).

| SKU | NOW Stock | NOW Cover | After 21062026 (22 Jul) Stock | Cover | After 25072026 (30 Aug) Stock | Cover |
|---|---|---|---|---|---|---|
| KIT-STA-2 | 4,113 | 324d | 4,113 (none on 21) | ~213d | 5,513 | ~334d ⚠️ |
| KIT-COM-4 | 7,501 | 93d 7d / 139d 14d | 7,501 (none on 21) | 23d at 7d / 69d at 14d | 10,301 | 46d at 7d / 112d at 14d |
| KIT-ULT-6 | 3,146 | 127d | 3,146 (none on 21) | 57d at 7d | 4,350 | 80d ⚠️ |
| LIQ-HEA-5 | 7,385 | 62d | OOS - Swift only | - | OOS - Swift only | - |
| LIQ-BAS-2 | 1,356 | 133d | 2,802 | 256d ⚠️ | 3,666 | 332d ⚠️ |
| ACC-REM-500 | 2,647 | 30d | 0 - Swift only | - | 0 - Swift only | - |
| ACC-REM-BOW | 5,435 | high | 9,435 (+4,000) | high | 12,135 (+2,700) | high |
| ACC-INS | 22,364 | 189d | same | 80d at 7d kit-adj | 25,964 | 92d at 7d ⚠️ |
| ACC-LAB-CA | 6,643 | 44d | + reprint + reorders | depends | depends | depends |

⚠️ = cover exceeds 100d post-arrival (overstock vs 45-75d target IF 7d rate doesn't sustain). At 7d rate KIT-COM-4 is on target; at 14d rate it overstocks.

### If CA 21062026 is delayed
- ACC-REM-BOW: 5,435 at low rate → safe well past Aug 30 anyway.
- LIQ-BAS-2: 1,356 at 10.2/d (14d) → 133d cover, safe past 25072026.
- Colours: the 6 flagged would push OOS gaps even wider (already -68 to -10d). Tolerable per user direction.

### Overstock flags (post-arrival cover > 100d at 7d rate)
- LIQ-BAS-2 at 256d post-21062026 — but liquid demand at 7d is structurally low for CA, hard to reduce without affecting kit assembly mix.
- All other "non-COM-4" kit components remain on the high side post-25072026 if 7d rate is a spike not a baseline.
- **Honest read:** if 7d rate is a one-week spike, CA still has the 6 May overstock problem. If 7d rate sustains, CA is near right-sized. Need 2-3 more weeks of post-launch data before recalibrating.

---

## PO RECOMMENDATIONS

| SKU / Action | Owner | By when | Reason |
|---|---|---|---|
| **Swift fill: Heal 7,500 + Remove 500ml 5,000** | Daniel | This week (place 13-16 May) | OOS gap at 7d rate: Heal 12d before 21062026 (which carries no Heal), Remove 500ml 30d-now-OOS with nothing in any container. Lean sizing, easy to recover if rate fades. |
| **Mixam ACC-LAB-CA reorder 10,000pc** | Remy | This week | Stock 6,643 + 1,300 reprint = 7,943 at ~150/d order rate = ~53d. Local print lead 14-21d. |
| **CA 25072026 manifest review** | Daniel/Remy | When confirming 6 Jul PO placement | At 7d rate, 5,404 kits = 46d post-arrival cover, tight. At 14d rate, plenty. Decision depends on whether 7d rate sustains over next 2-3 weeks. |
| **Investigate POW-CLE-193 + POW-JUS-449 deduction anomaly** | Greg/Daniel | This week | 5-6x benchmark sustained 4+ days each, far above Shopify rates. Could be kit-component auto-pull or deduction error. |
| **CA 21062026 production check-in** | Remy | Within 7 days | Confirm Sally on track for 28 May completion. Bottles + B115 jars status unknown from CA Slack since 6 May. |

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (act today/tomorrow)
- **POW-GLA-CS02 (Glacier Glow): 7 units, OOS now.** 600 on 21062026 (70d away). Accept gap per user direction.
- **ACC-REM-500: 30 days cover at 7d combined / 21 days at 3PL rate.** Nothing in any container. **Place Swift Remove 500ml fill this week (5,000pcs recommended).**
- **LIQ-HEA-5: 62 days cover at 7d kit-adj rate.** Stocks out before 21062026 lands (21062026 carries zero Heal anyway — Swift only). **Place Swift Heal fill this week (7,500pcs recommended).**
- **Confirm 5-6x deduction spike on POW-CLE-193 / POW-JUS-449** isn't a system error before it becomes a 14,001-unit / 10,704-unit hole.

### 🟡 WARNING (act this week)
- **ACC-LAB-CA: 44d cover** even with 1,300 Mixam reprint inbound. Reorder ~10,000pc from Mixam now.
- **POW-BLU-ZGD22, POW-PEO-SH07, POW-LEM-ZGD01, POW-SAP-11933, POW-SIL-11943** all stocking out before 21062026 (gaps -10 to -44d). All restocked on 21062026 - tolerable per user.
- **CA 25072026 sizing** — defer decision until 2-3 weeks of post-launch sales data is in (i.e. by 20-27 May review).
- **Sally / 21062026 production** — confirm bottle + jar status; no Slack update since 6 May.

### 🟢 MONITOR
- KIT-COM-4 7d burn rate. If 80.9/d sustains for 2+ weeks, escalate to 25072026 sizing.
- ACC-REM-BUN-1, ACC-REM-BUN-2 selling well (~12/d and ~10/d combined) — accelerates component consumption.
- Booklet-missing CX email rollout (Gav has the list from 11 May).
- 14d zero-sale list growing (27 in-stock colours, mostly L-/D-suffix limited series). Listing audit candidate.

---

## FOLLOW-UP ITEMS

### Immediate (this week)
- [ ] Daniel: Place Swift Heal 7,500 + Remove 500ml 5,000 fill (recommended sizing - revisit if 7d rate fades)
- [ ] Remy: Place Mixam ACC-LAB-CA reorder ~10,000pc
- [ ] Greg/Daniel: Investigate POW-CLE-193 + POW-JUS-449 deduction anomaly (5-6x benchmark, sustained)
- [ ] Remy: Chase 247 status on 21062026 production (Sally bottles + B115 jars unclear since 6 May)

### By end of month
- [ ] Daniel/Remy: Review CA 25072026 manifest with 2-3 weeks of post-launch sales data (target ~27 May)
- [ ] Greg: Refresh POS MODEL DSR for Base/Glow + ACC-REM-BOW + ACC-LAB-CA (stale per 6 May review)
- [ ] Greg: ACC-LAB-CA B360 deduction rule fix (NaN row issue)

### Ongoing
- [ ] Gav: Booklet-missing CX email rollout
- [ ] Gav/Remy: Dead-stock listing audit (38 SKUs, low urgency)
