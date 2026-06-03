# AUS POS Check — 18 May 2026

## DATA FRESHNESS

- **POS MODEL last updated:** 18 May 2026 (Greg AM paste). 3PL data through 18 May.
- **Growth factor:** 1.3x (191.1/d kit scaled vs 147/d base).
- **Kit DSR base:** STA 34, COM 78, ULT 35 → scaled STA 44.2 / COM 101.4 / ULT 45.5.

## MANUAL OVERRIDES (applied to all downstream calcs)

1. **LIQ-BAS-2: 0 → 648 units** (Katrina email 12:57 today: PO 14_AUS 05052026 received and checked in. Sheet shows 0 because paste was AM, check-in PM).
2. **LIQ-SEN-2: 0 → 216 units** (PO 14 contained 216).
3. **LIQ-SEN-4: 37 → 253 units** (PO 14 contained 216 added on top).
4. **AUS 09052026 manifest: pre-update.** Sheet does NOT reflect Daniel's 15 May additions (3k Coffin + 2.8k Almond + 1.7k Ballerina + 2.9k Square + 100 Stiletto + 300 kit boxes + 1k extra mailers; 744 Nail Drills NOT removed). Pending Sally acceptance. Treat sheet OL as floor; flag delta.
5. **Heal route — DEFERRED.** No LCL bridge this cycle (user 18 May). NDA proforma held. OP local fill waits for HEA-EMP/LID/BSH on AUS 07062026 (5 Jul). G3PL HEA-EMP stock = 0 today. Accept Heal OOS gap.
6. **ACC-NAI-MAT made in China** — supplier different from Avi. No local print option. Restock via CN container only.
7. **KIT-ULT-6 and ACC-REM-BOW OOS gaps accepted** (no express bridge planned).
8. **Free gift switched to ACC-NAI-MAT on Fri 15 May** (3 days of post-switch data: 16-18 May). Use 3-day post-switch rates for SKUs touched by the swap, not 14d.
9. **AUS 07062026 Birthday Sale deposit: PAID** (user-confirmed today).
10. **AUS 09052026 ship via Lily 20 May latest** (user-confirmed today, no express bridges alongside).

## SHIPMENT TIMELINE

| Container | Status | Est. Completion | Est. Arrival | Notes |
|---|---|---|---|---|
| AUS 05052026 (PO 14, express liquids) | ✅ DELIVERED 18 May | 6 May | 13 May | Katrina confirmed check-in today. 648 BAS + 216 SEN-2 + 216 SEN-4. |
| B360 PACKUP (PO 9) | Delivered with variances | — | 19 May (sheet) | 18 SKU variances unresolved 5+ weeks (-9,376 RE1-BOT, -911 REM-500, 11x -200 colours). |
| AUS 09052026 | In Production | 18 May | 17 Jun | User-override: ship 20 May via Lily. Manifest update pending Sally accept. |
| AUS 07062026 (Birthday Sale) | In Production, deposit paid | 5 Jun | 5 Jul | 1.4x growth factor sized container. |
| AUS 08072026 | Planned | 6 Jul | 5 Aug | Fill PO place date was 6 May — 12 days overdue. No PO email visible. |
| Container #5 (unnamed) | Planned | 5 Aug | 4 Sep | — |

---

## STOCK POSITION — DUAL DSR VIEW

Cover at projected (model × 1.3x) vs actual (14d 3PL deduction). For SKUs affected by 15 May free-gift swap, a third column shows post-switch 3-day rate (16-18 May) — operationally the relevant number.

### KITS

| SKU | Stock | Proj DSR | Cov @ Proj | 14d DSR | Cov @ 14d | 3d post-switch | Cov @ 3d |
|---|---:|---:|---:|---:|---:|---:|---:|
| KIT-STA-2 | 542 | 44.2 | 12d | 24.5 | 22d | 32 | 17d |
| KIT-COM-4 | 3,510 | 101.4 | 35d | 65.7 | 53d | 3 | 1,170d (offer pulled) |
| KIT-ULT-6 | 1,263 | 45.5 | 28d | 98.1 | 13d | **240** | **5d** 🔴 |

**Read:** Daniel's 14 May swap of free-gift attached SKU from Complete → Ultimate has redirected demand. COM idle, ULT surging. ULT cover at post-switch 3d rate = **5 days (~23 May OOS)**. AUS 09052026 brings 1,036 ULT, arrives 17 Jun → 25d gap. **Even with arrival, 1,263 + 1,036 = 2,299 units vs 240/d × 30d = 7,200 needed → undersupplied 4,900 units through arrival window.**

### LIQUIDS

| SKU | Stock | Proj DSR | Cov @ Proj | 14d DSR | Cov @ 14d | 3d post-switch | Notes |
|---|---:|---:|---:|---:|---:|---:|---|
| LIQ-BAS-2 | 648* | 53.3 | 12d | 49.7 | 13d | — | *Post-PO14 override. AUS 09052026 brings 2,592 (17 Jun). Tight bridge. |
| LIQ-SEN-2 | 216* | 4.5 | 48d | n/a | — | — | Override. 09052026 brings 432. |
| LIQ-SEN-4 | 253* | 5.8 | 44d | 5.8 | 44d | — | Override. 09052026 brings 432. |
| LIQ-SEA-3 | 2,048 | 36.6 | 56d | 20.2 | 101d | — | Stable. 09052026 brings 2,808. |
| LIQ-BON-1 | 1,149 | 14.2 | 81d | 9.4 | 123d | — | Healthy. |
| LIQ-GLO-4 | 549 | 33.3 | 16d | 14.7 | 37d | — | 09052026 brings 1,296. |
| LIQ-MAT-4 | 1,863 | n/a | — | 5.3 | 351d | — | Overstocked. 07062026 brings 5,400 more. |
| LIQ-SOA-6 | 523 | n/a | — | 5.5 | 95d | — | OK. |
| **LIQ-HEA-5** | **6,776** | **184.6** | **37d** | **186.7** | **36d** | **278** | **24d 🔴 at post-switch — no fill in any container** |

**Heal critical — OOS GAP ACCEPTED.** Post-switch rate 278/d → 24d cover, stocks out ~11 Jun. **HEA-EMP/LID/BSH at G3PL = 0** (no empties on hand to fill from). AUS 07062026 brings 20k empties, arrives 5 Jul. OP fill 21d after empties land → next Heal at G3PL ~26 Jul. **Heal OOS ~11 Jun - ~26 Jul (~45 days).** Per user: defer LCL bridge, accept the gap.

### REMOVE PRODUCTS

| SKU | Stock | 14d DSR | Cov @ 14d | 3d rate | Notes |
|---|---:|---:|---:|---:|---|
| ACC-REM (120ml) | 6,764 | 40.2 | 168d | — | Healthy. |
| ACC-REM-500 | 5,944 | 131.6 | 45d | — | 09052026 brings 0. Local OP fill required. Stocks out ~3 Jul. |
| **ACC-REM-BOW** | **263** | **54.9** | **5d** 🔴 | 41 | **6d cover. AUS 09052026 brings 6,840 arrives 17 Jun → 24-day OOS gap.** No express bridge planned. |

### PACKAGING / INSERTS

| SKU | Stock | 14d ded/d | Cov @ 14d | 3d rate | Cov @ 3d | Benchmark | Anomalies |
|---|---:|---:|---:|---:|---:|---:|---|
| **STO-BUB-BAG-L** | **5,837** | 308 | 19d | **499** | **12d** 🔴 | 435 | 4 days above benchmark 15-18 May (399/447/556/495). Free-gift surge + kit recovery. |
| STO-MAI-BAG-S | (check) | n/a | — | — | — | 330 | — |
| STO-MAI-2 | (check) | n/a | — | — | — | 330 | — |
| ACC-INS | 15,436 | 183 | 84d | — | — | 435 | Healthy. |
| **ACC-LAB** | **11,941** | 275 | 43d | **346** | **35d** | 735 | Under benchmark. **Avi 15k inbound — see assessment below.** |
| ACC-THA | 26,331 | 275 | 96d | — | — | 735 | Healthy. |

**STO-BUB-BAG-L:** post-switch rate 499/d → 12d cover. 09052026 brings 5,000 (sheet) arrives 17 Jun → 30d × 499 = 14,970 needed. **Massively under-supplied at projected.** Daniel's 15 May +1,000 addition + "fill to brim" with mailers is critical and not reflected in POS MODEL. **If Sally accepts the +1k and fills extra space, 09052026 could land 6,000-10,000 mailers → comfortable. If only 5,000 lands, ~6-day OOS gap.**

### ACCESSORIES (Free-gift-driven SKUs)

| SKU | Stock | 14d ded/d | 3d rate | Cov @ 3d | Notes |
|---|---:|---:|---:|---:|---|
| **ACC-TIP-COF** | **0** | 186 | 271 | **OOS NOW** 🔴 | Stocked out today (18 May). 09052026 brings 0. 07062026 brings 5,000 (arrives 5 Jul = 48d). **48-day OOS unless added to 09052026 (Daniel 15 May request: +3,000 pending Sally accept).** |
| ACC-TIP-ALM | 2,285 | 8.5 | 16 max | — | 269d at 14d. Free-gift swap will likely pull demand. 07062026 brings 600, 08072026 brings 800. |
| ACC-TIP-BAL | 1,072 | 2.6 | 5 max | — | 415d. 09052026 has 0; Daniel asked +1,700 pending Sally accept. |
| ACC-TIP-SQU | 2,410 | 5.1 | 9 max | — | 475d. 09052026 has 0; Daniel asked +2,900. |
| ACC-TIP-STI | 663 | 1.6 | 3 max | — | 414d. 09052026 has 0; Daniel asked +100. |
| **ACC-NAI-MAT** | **2,466** | 62 | **215** | **11d** 🔴 | New free-gift SKU from 15 May. Post-switch rate 70 → 302 → 275 day-on-day. Stocks out ~29 May. **No inbound on any container.** |
| **ACC-FRE-MANI** | **0** | 149 | 0 | OOS | Old free-gift (drip tray). Switched off Friday. Zero forward demand. Not an action item. |

---

## CONTAINER GAP ANALYSIS

### AUS 09052026 (arrives 17 Jun, 30 days) — pending Sally accept of Daniel's 15 May rev

**SHEET CONTENT vs DANIEL'S 15 MAY REQUEST:**

| Item | Sheet OL | Daniel 15 May | Delta |
|---|---:|---:|---|
| ACC-TIP-COF | 0 | +3,000 | +3,000 needed |
| ACC-TIP-ALM | 0 | +2,800 | +2,800 needed |
| ACC-TIP-BAL | 0 | +1,700 | +1,700 needed |
| ACC-TIP-SQU | 0 | +2,900 | +2,900 needed |
| ACC-TIP-STI | 0 | +100 | +100 needed |
| ACC-BOX (kit boxes) | 180 | +300 | Daniel's 300 may be on top → 480 total |
| STO-BUB-BAG-L | 5,000 | +1,000 (and fill brim) | At least 6,000; could be 8-10k if brim |
| ACC-PRO-DRI | 744 | REMOVE | Sheet still has 744 |

**Critical: this revision must be accepted by Sally and reflected in POS MODEL before shipping 20 May.** Remy to confirm with Lily/Sally in writing.

### AUS 09052026 stockout gaps (against current sheet, 30d to arrival)

| SKU | Stock | Rate | Days to OOS | Inbound on 09052026 | Post-arrival cover |
|---|---:|---:|---:|---:|---|
| KIT-ULT-6 | 1,263 | 240 | 5d | 1,036 | **GAP 25d; -4,900 units even at arrival** |
| KIT-STA-2 | 542 | 32 | 17d | 2,016 | OK |
| LIQ-HEA-5 | 6,776 | 278 | 24d | 0 (Heal local) | Depends on LCL fill |
| ACC-REM-BOW | 263 | 41 | 6d | 6,840 | OK after arrival, 24d OOS gap before |
| STO-BUB-BAG-L | 5,837 | 499 | 12d | 5,000 | OK after arrival if Sally accepts +brim |
| LIQ-BAS-2 | 648* | 50 | 13d | 2,592 | OK; PO 14 bridges |
| ACC-TIP-COF | 0 | 271 | OOS NOW | 0 (per sheet) | **48d OOS unless Sally accepts +3k** |
| ACC-NAI-MAT | 2,466 | 215 | 11d | 0 | **30d+ OOS — needs local restock or Sally addition** |

### AUS 08072026 (arrives 5 Aug, 79 days) — fill PO not yet placed

**Missing from manifest:**
- ACC-LAB: 0 → Avi 14-05-2026 PO covers (15k arriving ~late May / early Jun)
- ACC-THA: 0 → ACC-THA still healthy through 08072026 (96d cover stretches)
- LIQ-HEA-5: 0 (correct — local fill)
- ACC-REM-500: 0 filled (5k empties brought for local fill)
- ACC-NAI-MAT: 0 — **gap risk** if new free-gift rate sustains and 09052026 doesn't supply

### B360 PACKUP (sheet status "Delivered" 19 May)
- 18 SKU variances totalling ~20,000 units short (-9,376 ACC-RE1-BOT dominates; 11x -200 colours; -911 ACC-REM-500).
- 5+ weeks unresolved. Katrina 11 May email asked "how did warehouse sweep go" — implies still open. Treat OL values as discrepancy magnitudes, not pending stock.

---

## LOCAL FILL STATUS & FORECAST

### Outsource Packaging — Heal (DEFERRED)

- **POS MODEL Express #2 (22-04-2026 OP Fill):** No OL populated. Old fill never started (NDA payment held).
- **User direction 18 May:** No LCL bottle bridge this cycle. Accept Heal OOS gap.
- **HEA-EMP / HEA-LID / HEA-BSH at G3PL = 0.** No empties on hand to fill from locally.
- **Earliest OP local Heal fill:** post AUS 07062026 arrival (5 Jul brings 20k of each empty) + 21d OP fill cycle = G3PL delivery ~26 Jul.
- **OOS WINDOW:** ~11 Jun (Heal runs out at 278/d post-switch rate) → ~26 Jul (next local fill lands) = **~45 days.** Will dent kit fulfilment — Heal is in every kit.
- **Open question for Daniel:** is HEA-EMP available cross-region (e.g. UK/CA G3PL stock) to bridge with smaller air-freight if the 45-day window proves intolerable? Out of scope per today's direction but worth flagging.

### Outsource Packaging — Remove 500ml
- **Sheet has 22-04-2026 PO blocked on raw materials.** Peter chasing 5 May.
- ACC-REM-500 cover 45d at 14d rate — adequate through next fill cycle if placed by mid-June.
- AUS 07062026 brings 20k 500ml empties (5 Jul). AUS 08072026 brings 5k 500ml empties (5 Aug). Next OP fill can use those empties; CN ingredients not required.
- **Action:** Daniel scope Remove 500ml fill timing once Heal LCL placed.

### Avi Printing — ACC-LAB
- **14-05-2026 PO: 15,000 units. Status Ordering.** Lead time ~14-21d local print.
- ETA ~28 May - 4 Jun.

---

## AVI 15K SUFFICIENCY ASSESSMENT (user query)

| Scenario | Pre-Avi cover | Post-Avi cover | Gap to 08072026 (5 Aug) |
|---|---:|---:|---|
| At 14d rate (275/d) | 43d (29 Jun OOS) | 11,941 + 15,000 = 26,941 / 275 = 98d (after Avi land ~1 Jun) | **OK** (next OOS ~7 Sep) |
| At 3d post-switch (346/d) | 35d (22 Jun OOS) | 26,941 / 346 = 78d (after Avi land ~1 Jun) | **TIGHT** — OOS ~18 Aug, 2 weeks past 08072026 |
| At 400/d (further surge) | 30d (17 Jun OOS) | 26,941 / 400 = 67d (after Avi land ~1 Jun) | **GAP** — OOS ~7 Aug, 2 days post 08072026 |

**Verdict:** 15k is sufficient at current 14d rate but **tight at post-switch rate**. Risk: if kit recovery sustains and free-gift mat drives high order count, the 346/d rate could grow further (more orders × 1 label-per-order). 

**Recommendation:** Place a **5-7k Avi top-up PO** by 1 Jun, lead time 14-21d → arrives 15-22 Jun → ensures cover through 08072026 even at 400/d. Total Avi pipeline 20-22k = the original 20k recommendation. Cost-effective insurance vs OOS.

---

## STOCK-OUT FORECAST

### 🔴 STOCKOUT BEFORE ARRIVAL (acute gap) — many ACCEPTED per user direction

| SKU | Stock | Rate | Stocks Out | Next Inbound | Arrives | Gap | Action |
|---|---:|---:|---|---|---|---|---|
| ACC-TIP-COF | 0 | 271/d | NOW | 07062026 (5k) OR 09052026 (+3k if Sally accepts) | 17 Jun / 5 Jul | **48d at min** | Push Sally on 09052026 manifest accept (Daniel 15 May rev) |
| **KIT-ULT-6** | 1,263 | 240/d | 23 May | 09052026 (1,036) | 17 Jun | 25d + undersupplied at arrival | **ACCEPTED** (no bridge available) |
| **ACC-REM-BOW** | 263 | 41/d | 24 May | 09052026 (6,840) | 17 Jun | 24d | **ACCEPTED** (no bridge) |
| **LIQ-HEA-5** | 6,776 | 278/d | 11 Jun | 07062026 empties → OP local fill | ~26 Jul | **~45 days** | **ACCEPTED** (no LCL this cycle) |
| STO-BUB-BAG-L | 5,837 | 499/d | 30 May | 09052026 (5,000+) | 17 Jun | 18d if only 5k sheet OL / closes if Sally fills brim | Confirm Sally accepts brim-fill |
| **ACC-NAI-MAT** | 2,466 | 215/d | 29 May | — CN supplier, none on container | — | **OOS open-ended** until added to 07062026 (in production) or 08072026 (not yet placed) | Add to 07062026 if Sally still flexible; certain on 08072026 fill PO |

### 🟡 TIGHT (gap < 14d)

| SKU | Stock | Rate | Stocks Out | Next Inbound | Notes |
|---|---:|---:|---|---|---|
| LIQ-BAS-2 | 648 | 50/d | 1 Jul | 09052026 (2,592) 17 Jun | OK with PO 14 bridge. |
| ACC-LAB | 11,941 | 346/d | 22 Jun | Avi 15k ~late May | OK with Avi. Top-up recommended. |
| LIQ-GLO-4 | 549 | 15/d | 24 Jun | 09052026 (1,296) | OK. |

### 🟢 SAFE
All other liquids, colours, kits (COM, STA) at 30+ days cover with inbound aligned.

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (today / this week)

1. **Confirm Sally accepted Daniel's 15 May AUS 09052026 manifest revision.** Remy WeChat Lily / email Sally. The +10,500 tips + 1,000 mailers + 300 kit boxes + Nail Drill removal must be confirmed in writing before 20 May ship. **Critical because:** if Sally rejects, ACC-TIP-COF OOS extends to 5 Jul (07062026 arrival).

2. **Daniel place AUS 08072026 fill PO** (12 days overdue, no draft visible). Hold at projected (1.3x), don't lean-cut — kit DSR confirmed recovered. Critical adds:
   - **ACC-NAI-MAT: add 10-15k** (new free-gift SKU, CN supplied, 215/d new rate — no other route)
   - **KIT-ULT-6: increase from 1,428** — at post-switch 240/d, current 1,428 = 6d cover. Suggest re-size to 8-10k assuming new rate sustains.
   - **KIT-COM-4: cut from 3,192** — Complete idle at 3/d post-switch. Reduce or zero out.
   - ACC-LAB: ZERO is correct if Avi cycle stays on (top-up by 1 Jun)

3. **Add ACC-NAI-MAT to AUS 07062026 (in production)** if Sally still accepts revisions to Birthday Sale container. Bridge the 29 May OOS → 5 Jul arrival gap.

### ACCEPTED PER USER (no action — flag for next review)

- **KIT-ULT-6 OOS 23 May → 17 Jun.** 25-day gap, no bridge.
- **ACC-REM-BOW OOS 24 May → 17 Jun.** 24-day gap, no bridge.
- **LIQ-HEA-5 OOS ~11 Jun → ~26 Jul.** 45-day gap, no LCL bridge this cycle. **CX impact — Heal in every kit.**

### 🟡 WARNING (this week)

4. **STO-BUB-BAG-L** — confirm Sally filling 09052026 to brim with mailers (Daniel 14 May request). Without this, 18d OOS gap before arrival.

5. **Sydney Solvents IBC acetone decision** — 28 days idle. Decision needed for Remove 500ml local fill cycle (still needs acetone).

6. **Place 5-7k Avi top-up PO by 1 Jun** to insulate ACC-LAB against post-switch rate sustaining.

7. **Confirm POS MODEL 09052026 manifest updated** by Greg after Sally accept (otherwise downstream container modelling drifts).

8. **Heal CX preparation** — 45-day Heal OOS will affect every kit. Marketing/Joel may need a customer-facing comms plan (substitute, partial-shipment, or transparency comms) before 11 Jun.

### 🟢 MONITOR

11. **B360 PACKUP 18 SKU variances** — Heal 1,300 + ACC-RE1-BOT 9,376 + 911 ACC-REM-500 + 11x colours -200 each. 5+ weeks unresolved. Remy chase Jake; treat OL as discrepancies not pending stock.

12. **AUS 07062026 (Birthday Sale) timeline** — deposit paid, but completion 5 Jun → arrival 5 Jul means container-to-sale lead window is now thin.

13. **Liquids cover** — Base/Glow recovered via PO 14 + 09052026. Watch for any further Joel sample-approval delays on Low Odour Base (not relevant if PO 14 SEN-2 already in stock).

---

## PO RECOMMENDATIONS

| Item | Action | Qty | Place By | Lead | Arrives | Rationale |
|---|---|---:|---|---|---|---|
| Avi ACC-LAB top-up | Place | 5-7k | 1 Jun | ~14-21d | 15-22 Jun | Insulate against post-switch demand. Brings total Avi pipeline to 20-22k. |
| AUS 08072026 fill PO | Place (Daniel) | per draft | 18-22 May (12d overdue) | 70d production | 5 Aug arrival | Hold at projected 1.3x. Critical adds: **+ACC-NAI-MAT 10-15k**, **+KIT-ULT-6 8-10k** (size up from 1,428), **-KIT-COM-4** (size down or zero, idle post-swap). |
| AUS 07062026 addition request | Push Sally | +ACC-NAI-MAT ~5k if accepted | This week | container | 5 Jul | Bridge ACC-NAI-MAT gap if Sally still flexible (in production). |
| Remove 500ml local fill | Scope timing | 5-10k | Once OP empties usable | ~28d | mid-Jun / early-Jul | ACC-REM-500 OOS ~3 Jul. Buffer with OP cycle once acetone resolved. |

---

## CASCADING ARRIVAL PROJECTION (kits, post-switch rate)

| Stage | Date | KIT-STA-2 | KIT-COM-4 | KIT-ULT-6 |
|---|---|---:|---:|---:|
| NOW (18 May) | — | 542 (17d) | 3,510 (1,170d at 3/d) | 1,263 (5d) 🔴 |
| Post 09052026 (17 Jun, 30d) | +2,016 / +3,052 / +1,036 | 542 + 2,016 - (32 × 30) = 1,598 (50d) | 3,510 + 3,052 - 90 = 6,472 (2,157d) | 1,263 + 1,036 - 7,200 = **-4,901** ❌ |
| Post 07062026 (5 Jul, 48d) | +1,260 / +3,164 / +1,244 | (1,598 - 18×32) + 1,260 = 2,282 (71d) | (6,472 - 54) + 3,164 = 9,582 (3,194d) | already OOS; +1,244 lands into OOS gap ~5 Jul |
| Post 08072026 (5 Aug, 79d) | +1,372 / +3,192 / +1,428 | continues OK | continues OK | depends on rate stabilising |

**OVERSTOCK FLAG:** KIT-COM-4 at 3/d post-switch (Daniel's offer-pull) sits at 3,510 + inbound 9,408 across 3 containers = **12,918 units against current 3/d = 4,300d cover**. Either the offer attached to Complete returns (reverting demand) or these incoming COM orders are overstocked. **Daniel: review whether to cut COM from upcoming containers** if the free-gift-Ultimate offer becomes permanent.

**KIT-ULT-6:** Diametrically opposed — 240/d post-switch is unsustainable with current container sizing. 09052026's 1,036 ULT is 4.3d at new rate. **Daniel: size ULT up significantly in 07062026 (currently 1,244) and 08072026 (currently 1,428)**.

---

## FOLLOW-UP ITEMS

**Immediate (today / Monday):**
- [ ] Remy: confirm with Sally/Lily in writing that 09052026 manifest 15 May rev is accepted + 20 May ship + brim-fill with mailers
- [ ] Remy: push Sally for ACC-NAI-MAT addition to AUS 07062026 (still in production)
- [ ] Daniel: place AUS 08072026 fill PO (12d overdue) — re-size ULT up, COM down, add ACC-NAI-MAT 10-15k
- [ ] Joel/Daniel: CX comms plan for Heal OOS 11 Jun - 26 Jul (45-day window in every kit)

**By end of week:**
- [ ] Daniel: scope Remove 500ml next OP fill timing (post-acetone resolution)
- [ ] Daniel: Sydney Solvents IBC acetone decision (28d idle)

**By 1 Jun:**
- [ ] Remy: place 5-7k Avi ACC-LAB top-up PO

**Ongoing:**
- [ ] B360 PACKUP 18-SKU variance resolution with Jake (5+ weeks)
- [ ] Greg refresh POS MODEL post-Sally manifest accept + post-PO 14 check-in
- [ ] ShipHero name-sync (32 days stalled)
- [ ] Monitor: KIT-ULT-6 / ACC-REM-BOW / LIQ-HEA-5 OOS impacts on CX + revenue
