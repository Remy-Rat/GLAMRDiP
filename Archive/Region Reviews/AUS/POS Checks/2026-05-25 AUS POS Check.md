# AUS POS Model Check - 25 May 2026

**Scope per user: stop at AUS 07062026 (arrival 5 Jul). AUS 08072026 sizing not in scope (Daniel placing today).**

---

## Manual overrides applied (user-confirmed today)

- **AUS 09052026 has SHIPPED** (Lily vessel away ~20 May). Sheet status: "On the Way", ETA G3PL 17 Jun confirmed.
- **PO 14 / AUS 05052026 express liquids fully checked in** (Katrina 18 May 02:57). LIQ-BAS-2 jumped from 0 → 529 on 19 May in 3PL data. Sheet reflects.
- **Avi 14-05-2026 PO (15k booklets) NOT yet dispatched** - awaiting Joel EFT. Treat as not in stock yet. User deprioritised the Avi gap math (OP paid first).
- **Mani Mat (ACC-NAI-MAT) offer per user "switched ~3 days ago" (~22 May)** but 3PL deduction data shows continued high pull (174-251/d, 22-25 May). Either offer still partially active or upsell pull persisting. Treat current rate ~190/d not zero.

---

## DATA FRESHNESS

- **POS MODEL UPDATED: 25 May 2026** (today - Greg has pasted)
- **3PL (AUS 3GPL) last valid date: 25 May 2026** (today)
- **Growth factor (global): 1.3x.** Birthday Sale 07062026 sized at 1.4x; all others 1.3x.
- **Kit DSR model (1.3x scaled): STA 44.2 + COM 101.4 + ULT 45.5 = 191.1/d total**
- **Kit DSR actual (7d avg from 3PL): STA 25.7 + COM 1.1 + ULT 167.9 = 194.7/d total** - **at target. Mix is inverted from model.**

---

## STOCK POSITION - 25 May

Two cover columns side by side: model (1.3x base × growth) and actual (7d 3PL deduction).

### Kits

| SKU | Stock | Model DSR | Cov @ Model | Actual 7d | Cov @ Actual |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 362 | 44.2 | 8d | 25.7 | 14d |
| KIT-COM-4 | 3,502 | 101.4 | 35d | 1.1 | 3,184d (idle) |
| KIT-ULT-6 | 88 | 45.5 | 2d | 167.9 | **<1d 🔴** |

### Liquids

| SKU | Stock | Model DSR | Cov @ Model | Actual 7d | Cov @ Actual |
|---|---:|---:|---:|---:|---:|
| LIQ-BAS-2 | 327 | 53.3 | 6d | 33.7 | 10d |
| LIQ-GLO-4 | 432 | 26.0 | 17d | 16.7 | 26d |
| LIQ-SEA-3 | 1,903 | 44.2 | 43d | 20.7 | 92d |
| LIQ-BON-1 | 1,099 | 16.9 | 65d | 7.1 | 154d |
| LIQ-MAT-4 | 1,829 | 10.4 | 176d | 4.9 | 377d |
| LIQ-SOA-6 | 475 | 13.0 | 36d | 6.9 | 69d |
| LIQ-SEN-2 | 128 | 9.1 | 14d | 9.5 | 13d |
| LIQ-SEN-4 | 212 | 7.8 | 27d | 5.8 | 36d |
| LIQ-HEA-5 | 5,394 | 186.0 | 29d | **197.4** | **27d 🔴** |

### Remove / Bowls

| SKU | Stock | Model DSR | Cov @ Model | Actual 7d | Cov @ Actual |
|---|---:|---:|---:|---:|---:|
| ACC-REM | 6,632 | 19.5 | 340d | 18.9 | 352d |
| ACC-REM-500 | 4,698 | 152.5 | 31d | **178.0** | **26d 🔴** |
| ACC-REM-BOW | 18 | 999+ | <1d | 35.0 | **<1d 🔴** |

### Free-gift / Tips

| SKU | Stock | Model DSR | Cov @ Model | Actual 7d | Cov @ Actual | Notes |
|---|---:|---:|---:|---:|---:|---|
| ACC-NAI-MAT | 985 | 164/d | 6d | **211.6** | **5d 🔴** | Offer per user switched ~22 May but rate stays 174-251/d |
| ACC-TIP-COF | 0 | - | OOS | 0 (depleted) | OOS | Already OOS since 18 May |
| ACC-TIP-SQU | 1,019 | 170/d | 6d | **198.7** | **5d 🔴** | **NEW: Square Tips became offer ~19 May (was 3-9/d, now 200+/d)** |
| ACC-TIP-ALM | 2,234 | 19.6 | 114d | 7.3 | 307d | Stable low |
| ACC-TIP-BAL | 1,051 | 5.2 | 202d | 3.0 | 350d | Stable low |
| ACC-TIP-STI | 647 | 2.6 | 248d | 2.3 | 283d | Stable low |
| ACC-TRA-BAG | 1,950 | - | - | 0.3 | 6,825d | Travel bag - idle |
| ACC-FRE-MANI | 0 | - | OOS | 0 (depleted) | OOS | Discontinued/replaced |

### Packaging / Inserts

| SKU           |  Stock | Model DSR |      Cov @ Model | Actual 7d | Cov @ Actual | Notes                                                |
| ------------- | -----: | --------: | ---------------: | --------: | -----------: | ---------------------------------------------------- |
| ACC-LAB       |  9,764 |     376/d |              26d | **311.0** |   **31d 🔴** | Avi 15k PO ready, awaiting Joel EFT                  |
| ACC-THA       | 24,158 |     366/d |              66d |     310.4 |          78d | OK                                                   |
| ACC-INS       | 14,073 |     195/d |              72d |     194.7 |          72d | OK                                                   |
| STO-BUB-BAG-S |  5,963 |     130/d | 79d (post-paste) |     284.1 |          21d | Check anomaly                                        |
| STO-BUB-BAG-L |  3,277 |     205/d |              16d | **365.7** |    **9d 🔴** | Way above 435 benchmark per [[deduction-benchmarks]] |
| STO-MAI-2     | 14,793 |     176/d |              84d |      93.4 |         158d | OK                                                   |
| STO-MAI-BAG-S | 17,354 |     176/d |              98d |      93.4 |         186d | OK                                                   |

---

## STOCK-OUT FORECAST

**Window 1: Today → AUS 09052026 arrival (17 Jun, 23 days)**

| SKU | Cov today (actual) | OOS date | 09052026 OL | Gap |
|---|---:|---|---:|---:|
| KIT-ULT-6 | <1d | OOS NOW | 1,036 | **22d gap** |
| ACC-REM-BOW | <1d | OOS NOW | 6,840 | **23d gap** |
| ACC-TIP-COF | 0d | OOS 18 May | **0 (not added)** | **41d gap (until 07062026)** |
| ACC-TIP-SQU | 5d | ~30 May | **0 (not added)** | **38d gap (until 07062026 - but 07062026 ALSO has 0)** |
| ACC-NAI-MAT | 5d | ~30 May | **0 (not added)** | **~18d gap minimum, dependent on offer-switch timing** |
| LIQ-BAS-2 | 10d | ~4 Jun | 2,592 | **13d gap** |
| STO-BUB-BAG-L | 9d | ~3 Jun | 5,000 | **14d gap** |
| LIQ-SEN-2 | 13d | ~7 Jun | 432 | **10d gap** |
| KIT-STA-2 | 14d | ~8 Jun | 2,016 | **9d gap** |
| LIQ-GLO-4 | 26d | ~20 Jun | 1,296 | **3d gap (tight)** |
| ACC-LAB | 31d | ~25 Jun | 0 (Avi-driven) | **8d gap pre-09052026 if Avi doesn't dispatch** |

**Window 2: 17 Jun → AUS 07062026 arrival (5 Jul, 41 days total)**

SKUs that 09052026 does NOT restock (need 07062026 or local fill):

| SKU | Cov today | OOS date | 07062026 OL | Resolution path |
|---|---:|---|---:|---|
| LIQ-HEA-5 | 27d | ~21 Jun | **0** | Heal LCL bottle bridge → OP local fill, unplaced 7 days |
| ACC-REM-500 | 26d | ~20 Jun | **0** | OP local fill PO 22-04-2026, status Ordering, no movement |
| ACC-LAB | 31d | ~25 Jun | **0** | Avi 14-05-2026 15k PO ready to dispatch |
| ACC-NAI-MAT | 5d | ~30 May | **0** | **No restock route. CN-only SKU. 35+ day OOS gap to 07062026.** |
| ACC-TIP-SQU | 5d | ~30 May | **0** | **No restock route. 07062026 ALSO has 0. Sally needs Square added urgently.** |

---

## 🔴 CRITICAL FINDING #1: AUS 09052026 manifest in POS MODEL does NOT reflect Daniel's 15 May revision

The 18 May review documented Daniel's 15 May container revision sent to Sally: **+3k Coffin tips, +2.8k Almond, +1.7k Ballerina, +2.9k Square, +100 Stiletto, +300 kit boxes, +1k bubble mailers (brim-fill), -744 Nail Drills**.

Current POS MODEL inbound on AUS 09052026:
- ACC-TIP-COF: **0** (expected +3,000)
- ACC-TIP-ALM: **0** (expected +2,800)
- ACC-TIP-BAL: **0** (expected +1,700)
- ACC-TIP-SQU: **0** (expected +2,900)
- ACC-TIP-STI: **0** (expected +100)
- ACC-NAI-MAT: **0** (Daniel 18 May said "we'd now be pushing it to get any item produced in time" - mani mat not in 09052026)
- STO-BUB-BAG-L: **5,000** (sheet had 4,300; reduced to 171 per Greg's 22 May comment; revision was +1,000 brim-fill - net unclear)

**Three possibilities:**
- (a) Sally rejected the revision (no Slack/Gmail evidence either way - all comms via WeChat per Daniel)
- (b) Greg hasn't pasted the revision yet (despite POS MODEL UPDATED 25 May)
- (c) Daniel's 18 May 18:24 reply ("we'd now be pushing it to get any item produced in time") implies the revision was conceded as too late

**Impact if not on 09052026:**
- ACC-TIP-COF: 41-day OOS gap (today → 5 Jul) instead of 23-day
- ACC-TIP-SQU: same 41-day gap (and 07062026 has 0 Square too)
- ACC-TIP-ALM: low rate (7/d) so not yet critical
- Bubble mailer brim-fill loss: -1,000 reduces 09052026 to 5,000 - 14d cover at 365/d, was 18d cover with the brim-fill

**Action: Daniel/Remy confirm with Sally/Lily in writing - was the revision shipped or not?** This determines whether tips OOS gaps are 23d or 41d. The diff is severe.

---

## 🔴 CRITICAL FINDING #2: Square Tips (ACC-TIP-SQU) is the new offer tip, not visible in 18 May review

3PL daily deductions show a step-change on 19 May:

| Date | ACC-TIP-COF | ACC-TIP-SQU |
|---|---:|---:|
| 12-18 May | 100-300/d (offer) | 3-9/d (idle) |
| 19-25 May | 0 (OOS) | **116-268/d (new offer)** |

When Coffin Tips depleted (18 May), the website-attached free-gift tip switched to Square. **This was not flagged in the 18 May review.**

- Stock today: 1,019 / 199/d 7d avg = **5d cover** → OOS ~30 May
- No 09052026 inbound, no 07062026 inbound, no 08072026 inbound
- **Gap: ~36-41 days before next restock unless Sally adds Square to 07062026**

Action: Daniel push Sally for +5,000 ACC-TIP-SQU on 07062026 (still in production, est completion 5 Jun).

---

## 🔴 CRITICAL FINDING #3: Mani Mat offer "switched" per user but rate hasn't normalised

User flagged today that the Mani Mat offer was "switched ~3 days ago" (~22 May). Daily 3PL deductions for ACC-NAI-MAT:

| Date | Deduction |
|---|---:|
| 12-13 May | 0 |
| 14 May | 3 |
| 15 May (offer ON, drip tray retired) | 4 |
| 16 May | 70 |
| 17 May | 302 |
| 18 May | 275 |
| 19 May | 363 |
| 20 May | 227 |
| 21 May | 115 |
| **22 May (offer per user OFF)** | **174** |
| 23 May | 161 |
| 24 May | 190 |
| **25 May** | **251** |

**Post-22-May average: 194/d.** Not zero, not normalised. Either (a) offer still active in some flow, (b) upsell/bundle pulling, or (c) some lagged Shopify→3PL lead time. **Treat current rate as 190/d planning, not zero.**

Stock 985 / 190 = **5d cover** → OOS ~30 May. **No restock on any container.** 35-41 day OOS gap to 07062026.

Action: Joel/Daniel confirm exact offer state today. If offer is in fact off and rate hasn't dropped, investigate the residual demand source.

---

## 🔴 CRITICAL FINDING #4: KIT-ULT-6 will run out in days

Stock fell from 2,357 (12 May) → 88 (25 May). Sustained 100-266/d post-15-May offer-attach swap (Complete → Ultimate). 7d avg 168/d.

- Today: 88 / 168 = **<1 day** (effectively OOS)
- 09052026 brings 1,036 ULT (arrival 17 Jun = 23 days away)
- 23 days × 168/d = **3,864 units of demand vs 88 + 1,036 = 1,124 supply = 2,740 unit shortfall**
- 07062026 brings 1,244 ULT (arrival 5 Jul = 18 days later)
- Combined supply through 5 Jul: 88 + 1,036 + 1,244 = 2,368 vs 41d × 168 = 6,888 demand. **~4,500 unit shortfall by 5 Jul.**

**No bridge available.** Per 18 May review: "No bridge - accepted". This was flagged. Now compounded: even with both 09052026 and 07062026 landing on time, ULT stays in OOS condition until **08072026 (5 Aug) at earliest**, IF Daniel sizes 08072026 ULT properly (today's draft per user).

**Implication for KIT-COM-4:** Idle at 1.1/d (vs 101.4 model). 3,502 in stock = 3,184 days cover at current rate. **Massively overstocked at the kit mix level.** 09052026 brings 3,052 more, 07062026 another 3,164. Without a Shopify flow auto-substitution like UK has (STA → COM), Complete is dead inventory until offer rebalances.

Recommendation (carry to 08072026 sizing): match container kit mix to actual rate, not model. STA 26 + COM 1 + ULT 168 = 195/d. ULT should be ~85% of kit volume, not 24%.

---

## 🟡 LIQ-HEA-5 (Heal) - 27d cover, no restock on any container

- Stock 5,394 / 197.4/d 7d avg = **27d cover** → OOS ~21 Jun
- 09052026: 0 (kits ship without Heal - filled locally at OP)
- 07062026: 0
- 08072026: 0 (Daniel drafting today - **NO Heal in fill PO per 18 May intent**)
- **Heal LCL bottle bridge unplaced 7 days.** Per 18 May: bottle LCL to OP + local ingredient sourcing. ~28d total lead.
- If placed this week → G3PL ~22 Jun (1 day after OOS).
- If placed next week → G3PL ~29 Jun (8 days into OOS).

**Action: Daniel scope this week. Joel approve.**

---

## 🟡 ACC-REM-500 - 26d cover, no restock on any container

- Stock 4,698 / 178/d 7d avg = **26d cover** → OOS ~20 Jun
- OP local fill PO 22-04-2026 status Ordering. Empty bottles at G3PL, ingredient supply unresolved (acetone via Sydney Solvents 33 days idle).
- Same OP cycle as Heal LCL bridge - **bundle the placement.**

**Action: Daniel scope concurrent with Heal LCL placement. Acetone source needs decision (Sydney Solvents IBC quote idle 33 days, or alternate).**

---

## 🟡 STO-BUB-BAG-L - 9d cover at 365/d (above benchmark)

Large bubble mailer rate is running 360-556/d in last 10 days (vs 435 benchmark - 4 anomaly days). Driven by Mani Mat / Square tip offer triggering larger-parcel orders.

- Stock 3,277 / 365 = **9d cover** → OOS ~3 Jun
- 09052026 brings 5,000 (was 4,300, then per Greg 22 May comment reduced to "171" then revised brim-fill = unclear final qty; sheet shows 5,000 OL)
- 07062026 brings 10,800

**If 5,000 is true:** post-09052026 = 5,000 + (3,277 - 23×365) = OOS before 09052026 lands. ~14-day gap.

**If true brim-fill 1,000+ added to 09052026 made it through:** total 6,000 → still 17d cover at 365/d = OOS 4 Jul = 1d gap before 07062026.

**Action: confirm with Greg/Daniel what the final 09052026 STO-BUB-BAG-L OL is post-revision. The 22 May "less mailer bags" Greg comment is ambiguous - reduced to 171 (4,129 cut) is one read; reduced from 5,300 to 4,300 (and now showing 5,000) is another.**

---

## 🟢 ACC-LAB - 31d cover, Avi 15k PO ready

- Stock 9,764 / 311/d 7d avg (climbing: 245→282→311) = **31d cover** → OOS ~25 Jun
- Avi 14-05-2026 PO: 15,000 booklets ready to dispatch, awaiting Joel EFT
- 09052026: 0 (Avi-supplied)
- 07062026: 0
- User flagged: deprioritise Avi gap math. OP gets paid first.

**Scenarios:**
- Joel pays Mon-Tue, Avi dispatches Wed, lands G3PL +3-5d road freight Vic→Vic = ~3-5 Jun. New stock 9,764 - 9×311 + 15,000 = 21,963 → 70d cover from arrival → covers through ~13 Aug. Safe past 07062026.
- Joel pays Fri, Avi dispatches Mon, lands ~9-11 Jun. New stock 9,764 - 16×311 + 15,000 = 19,788 → 64d from arrival = comfortable.
- Joel pays in 2 weeks: pre-Avi OOS gap opens 25 Jun → ~7-13 Jul (cuts into 07062026 arrival window 5 Jul).

**Action: Avi can wait per user, but every week of slip eats the 07062026-window buffer. Monitor.**

---

## CONTAINER / ORDER STATUS

| Ref | Status | Est. Completion | Est. Arrival | Growth | Notes |
|---|---|---|---|---|---|
| B360 PACKUP (PO 9) | Delivered | - | 19 May 2026 | 1.3x | 172 colours, 45d cover target. Transferred. |
| **AUS 09052026 (PO 16)** | **On the Way** | 18 May | **17 Jun** | 1.3x | **SHIPPED via Lily (user-confirmed today). 168 colours, 45d cover target.** |
| AUS 07062026 (Birthday Sale) | In Production | 5 Jun | 5 Jul | **1.4x** | Deposit PAID (18 May). 167 colours, 45d cover target. |
| AUS 08072026 | (no status) | 6 Jul | 5 Aug | 1.3x | Per user: Daniel drafting today. Out of scope for this review. |
| Container #5 | (no status) | 5 Aug | 4 Sep | 1.3x | Out of scope. |

**Container-status flags:**
- AUS 09052026 ETA hasn't shifted from 17 Jun. Lily fast vessel only path to a tighter date.
- AUS 07062026 still 5 Jun completion / 5 Jul arrival. No further Slack/Sally updates since 18 May.

---

## LOCAL FILL STATUS

### Outsource Packaging (OP) - Heal + Remove 500ml
- **Heal LCL bottle bridge:** UNPLACED 7 days since 18 May direction set. Bottles to ship from CN/local supply → OP fills locally → ship to G3PL. ~28d total lead.
- **Remove 500ml fill (22-04-2026):** Status Ordering. Empty bottles at G3PL, acetone unresolved.
- **OP relationship status:** Peter 23 May email threatened 1 Jun finance charges on overdue Joel payments. **Pay overdue balance before placing new fill.**

### Avi Printing - Local Labels
- **14-05-2026 PO:** 15,000 booklets in production complete, awaiting Joel EFT before dispatch.
- **Next Avi top-up:** Out of scope (08072026 territory).

### Sydney Solvents - Acetone (for OP Remove 500ml ingredient)
- IBC quote idle 33 days our side.
- Less urgent now Heal LCL is bottle-led, but Remove 500ml still needs acetone for next OP fill cycle.

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (today / this week)

1. **Joel pay Peter / OP overdue balance** before 1 Jun finance-charge ultimatum. Heal LCL placement waits on this.
2. **Daniel scope Heal LCL bottle bridge** (qty / bottle source / local ingredients / freight). Place this week to land ~22 Jun before 21 Jun OOS. **7 days lost.**
3. **Daniel/Remy confirm in writing with Sally:** was Daniel's 15 May 09052026 revision (tips + mailers) accepted and shipped? POS MODEL still shows 0 tip inbound on 09052026. The COF/SQU/MAT OOS gaps swing 18 days on this answer.
4. **Daniel push Sally for +5,000 ACC-TIP-SQU on 07062026** (still in production, completion 5 Jun). **New finding** - Square Tips is now the offer tip, 199/d, OOS ~30 May, no restock anywhere.
5. **Joel/Daniel confirm Mani Mat offer state** - per user "switched ~3 days ago" but 3PL deduction unchanged at 190+/d. Either offer still semi-active, upsell pull, or data lag. Investigate and recalibrate cover math.
6. **Daniel place AUS 08072026 fill PO today** (per user). Key sizing inputs (out of detailed scope for this review but worth carrying):
   - Kit mix: ULT 168/d, STA 26/d, COM 1/d. Size ULT up substantially, COM down.
   - ACC-NAI-MAT: 10-15k if offer continues.
   - ACC-TIP-SQU: 5-8k.
   - ACC-LAB: 0 (Avi covers).

### 🟡 WARNING (this week)

7. **Daniel scope OP Remove 500ml fill** concurrent with Heal LCL. Resolve acetone source (Sydney Solvents IBC vs alternate).
8. **STO-BUB-BAG-L 09052026 OL** - Greg/Daniel confirm final number post-revision. Sheet shows 5,000 but Greg's 22 May "less mailer bags" comment is unclear (171? 4,129 cut? +1k brim-fill?).
9. **POW-CLE-193** sustained 5-6x benchmark deduction (10+ consecutive days at 250-360/d, benchmark 35/d). Offer-attached pull confirmed CA-side; verify AUS context. Stock unknown - check if listing is correctly priced/displayed.
10. **POW-TRE010** at 299/d on 17-18 May (benchmark 35/d). Investigate.

### 🟢 MONITOR

11. **AUS 09052026 vessel tracking** - any Lily WeChat updates on ETA tightening.
12. **AUS 07062026 (Birthday Sale)** completion ETA - 5 Jun on sheet. No updates from Sally/Lily since 18 May.
13. **Kit DSR rebase** - POS MODEL needs reset to current mix (STA 25, COM 1, ULT 168) once Daniel/Joel deem the offer-swap permanent. Greg backlog item.

---

## OVERSTOCK FLAGS (post-arrival cover > 100d, target 45-75d)

At actual 7d rates, post-09052026 cover:

| SKU | Stock post-09 | Cover post-09 | Excess vs 75d target |
|---|---:|---:|---:|
| KIT-COM-4 | 6,485 | **5,895d** at 1.1/d | +6,400 units idle by 5 Jul |
| LIQ-MAT-4 | 7,229 | 1,476d | +6,862 units |
| LIQ-BON-1 | 2,179 | 307d | +1,646 units |
| LIQ-SEA-3 | 4,711 | 227d | +3,160 units |
| LIQ-SOA-6 | 1,555 | 225d | +1,038 units |
| ACC-REM | 6,632 | 352d | +5,387 units |
| ACC-TIP-BAL | 1,051 | 350d | +826 units |
| ACC-TIP-STI | 647 | 283d | +475 units |
| ACC-TIP-ALM | 2,234 | 307d | +1,687 units |
| ACC-TRA-BAG | 1,950 | 6,825d | +1,927 units |
| STO-MAI-2 | 21,283 | 228d | +14,000 units |

**Read:** Mix imbalance is concentrated. COM kits + Mat liquid + Bond liquid + Sea liquid + ALM/BAL/STI tips all overstocking. ULT + new-offer SKUs (NAI-MAT, SQU tips) all severely undersized.

**08072026 sizing review needs to use actual mix, not model.** Surface to Daniel today.

---

## DUAL-DSR DIVERGENCE FLAGS

Where model vs 7d rate diverges materially:

| SKU | Model DSR | 7d Actual | Direction | Read |
|---|---:|---:|---|---|
| KIT-COM-4 | 101.4 | 1.1 | **Model 92x actual** | Offer-swap killed Complete kit demand |
| KIT-ULT-6 | 45.5 | 167.9 | **Actual 3.7x model** | Offer-swap surged Ultimate, model way under-states risk |
| ACC-NAI-MAT | ~164 | 211.6 | Actual 1.3x model | Within tolerance but cover already <5d |
| ACC-TIP-SQU | ~170 | 198.7 | Actual 1.2x model | But model previously had 0 for SQU (was idle) - **new offer pattern** |
| ACC-TIP-COF | ~170 | 0 | Model way over | OOS - rate is artificially 0 |
| STO-BUB-BAG-L | 205 | 365.7 | **Actual 1.8x model** | Larger-parcel pattern from new offer mix |
| ACC-LAB | 376 | 311 | Model 1.2x actual | Within tolerance, model slightly conservative |

---

## FOLLOW-UP ITEMS

### Immediate (today/Monday)
- [ ] Joel: pay Peter / OP overdue balance (1 Jun finance-charge ultimatum)
- [ ] Daniel: scope Heal LCL bottle bridge (7 days lost)
- [ ] Daniel/Remy: confirm Sally accepted 09052026 revision in writing
- [ ] Daniel: push Sally +5,000 ACC-TIP-SQU on 07062026 (still in production)
- [ ] Joel/Daniel: confirm Mani Mat offer state - is it still active, what's pulling 190+/d?
- [ ] Daniel: place 08072026 fill PO with rebalanced mix (ULT up, COM down, NAI-MAT 10-15k, SQU 5-8k)

### This week
- [ ] Daniel: scope OP Remove 500ml fill concurrent with Heal LCL
- [ ] Daniel/Sydney Solvents: acetone source decision
- [ ] Remy: chase Greg on final 09052026 STO-BUB-BAG-L OL after 22 May revision
- [ ] Remy: chase Jake on PO 9 B360 PACKUP count + Heal 1,300 sweep (6+ weeks)

### Ongoing
- [ ] Greg: POS MODEL kit DSR rebase (STA 25, COM 1, ULT 168) once offer-swap deemed permanent
- [ ] Daniel: investigate POW-CLE-193 + POW-TRE010 offer-attach pattern (multi-week 5-9x benchmark)
