# 🇦🇺 AUS POS Model Check — 1 Jun 2026

## DATA FRESHNESS
- **POS MODEL last paste:** 2026-06-01 (today, AM paste — Greg)
- **3PL data last valid:** 2026-06-01 (same as POS paste — fully aligned)
- **Shopify data last valid:** 2026-05-31 (1-day standard lag)
- **Growth factor (header):** 1.3x (191/d scaled total)
- **Active inbound shipments in POS MODEL:**
  - **AUS 09052026** (On the Way) — ETA G3PL **22 Jun** (21 days)
  - **AUS 07062026** (In Production) — completion 10 Jun, ETA **10 Jul** (39 days)
  - **AUS 05082026** (Ordering) — completion 6 Jul, ETA **5 Aug** (65 days) — **already in sheet at 1.3x sizing, despite Daniel's 27 May Slack note targeting 1.6x. Sheet manifest doesn't reflect the 1.6x intent yet.**
  - **AUS 04092026** (placeholder) — completion 5 Aug, ETA **4 Sep** (95 days)

## MANUAL OVERRIDES APPLIED

- **STO-BUB-BAG-L: sheet shows 969 on hand.** Katrina 26 May Gmail confirmed 600 physical pieces with "higher volume not deducted from system" — i.e. real consumables flow through that ShipHero doesn't capture. Greg may have applied a manual top-up (express PO inflation?) or the deduction model has been adjusted. **Treat headline cover as 600 actual / 969 sheet — both numbers below.**
- **KIT-ULT-6: sheet shows 0 stock + 0 backorder** — confirmed by G3PL Katrina 26 May ("only 54 Ultimate kits left, predict OOS by end of week"). **Per user 1 Jun: ULT orders are being fulfilled with COM substitution at warehouse.** ULT Shopify demand is being absorbed by COM stock. Treat ULT + COM as a single fulfillment pool for cover math.
- **OP balance: paid 27 May.** Heal fill commenced ~29 May. Expected G3PL delivery late Jun / early Jul.
- **AUS 07062026 has been upsized to 2x40HQ (V2)** per Daniel 25 May Slack — adding 560 ULT + 5,400 MAT + 17,228 REM-500 + 11,200 BUB + 25,000 CARE + Glass Slipper. Joel confirmed PO updated 28 May. **Sheet partially reflects the upsize (BUB at 22,000 matches; ULT still at 1,244 not 1,804).** Treat the sheet OL as imperfect until Greg refreshes.

## STOCK POSITION

Stock + actual DSR cover (3PL 7d/14d/30d), with model-scaled cover as the planning target.

### Kits

| SKU | Stock | Model DSR (1.3x) | 3PL 7d | Shop 7d | Cov @ Model | Cov @ 3PL7 |
|---|---|---|---|---|---|---|
| KIT-STA-2 | 215 | 44.2 | 21.0 | 21.9 | 5d | 10d |
| KIT-COM-4 | 2,463 | 101.4 | 148.4 | 145.1 | 24d | 17d |
| KIT-ULT-6 | **0** | 45.5 | 12.6 (depressed by OOS) | 12.4 | — | — |
| **Combined (STA+COM+ULT)** | **2,678** | **191.0** | **182.0** | **179.4** | **14d** | **15d** |

**Read:** Stock-out of ULT is being papered over by COM substitution. Combined kit pool has 14-15 days cover. At ETA 22 Jun (21 days), we run dry around **15 Jun — confirming the 7-day OOS gap pre-09052026 arrival.**

### Liquids (kit-adjusted via Sally pre-fill except Heal)

| SKU | Stock | Model DSR | 3PL 7d | Shop 7d | Cov @ Model | Cov @ 3PL7 |
|---|---|---|---|---|---|---|
| LIQ-BAS-2 | 174 | 69.3 | 21.9 (post-PO 14 catch-up) | 19.3 | 3d | 8d |
| LIQ-GLO-4 | 361 | 33.8 | 10.1 | 9.0 | 11d | 36d |
| LIQ-HEA-5 (kit-adj) | 4,122 | 240.0 | 181.7 | 2.0 standalone | 17d | 23d |
| LIQ-SEA-3 | 1,791 | 57.5 | 16.0 | — | 31d | 112d |
| LIQ-SEN-2 | 64 | 11.8 | 9.1 | 8.0 | 5d | 7d |
| LIQ-SEN-4 | 175 | 10.1 | 5.3 | 4.4 | 17d | 33d |
| LIQ-BON-1 | 1,048 | 22.0 | 7.3 | 6.1 | 48d | 143d |
| LIQ-SOA-6 | 447 | 16.9 | 4.0 | 3.3 | 26d | 111d |
| LIQ-MAT-2 | — (not in sheet) | — | — | — | — | — |

**Read:** Base (LIQ-BAS-2) is the only acute liquid — 8d cover at actual rate vs AUS 09052026 arrival in 21 days = **~13d gap**. Heal kit-adjusted rate has 23d cover, OP fill landing ~late Jun closes the gap. Glow is fine despite low headline model cover (under-consumed since 21 May based on 7d window).

### Accessories / Offer-attached

| SKU | Stock | 3PL 7d | Shop 7d | Cov @ 3PL7 | Status |
|---|---|---|---|---|---|
| ACC-NAI-MAT | **0** (BO 288) | 140.7 | 0.9 standalone | — | OOS, kit-attached via $85-gift |
| ACC-TIP-SQU | 543 | 68.0 | 3.1 | 8d | Will OOS ~9 Jun |
| ACC-TIP-COF | **0** (BO 2) | — (zero stock) | 0.0 | — | OOS since 18 May, **zero on any container** |
| ACC-TIP-ALM | 2,187 | 6.7 | 6.1 | 325d | Safe (overstocked) |
| ACC-TIP-BAL | 251 | 114.3 (anomaly) | 1.9 | 2d | Reads as crashing — check for bulk pull |
| ACC-TIP-STI | 640 | 1.0 | 0.9 | 640d | Safe |
| ACC-REM-BOW | **0** (BO 3) | 2.6 (residual) | 0.3 | — | OOS, 09052026 brings 6,840 (22 Jun) — **21d gap** |
| ACC-REM-500 | 3,588 | 158.6 | 152.3 | 23d | OP fill in motion + 17,228 in 07062026 |
| ACC-REM (120ml) | 6,575 | 8.1 | 4.3 | 807d | Massive overstock — selling collapsed to bundle channel |
| ACC-TRA-BAG | 1,950 | — (no flow yet) | 0.0 | — | **NEW OFFER CANDIDATE** — needs Shopify activation to test attach rate |
| ACC-FRE-MANI | **0** (BO 0 reported) | — | 0.0 | — | OOS — not on any container |

### Packaging / Inserts

| SKU | Stock | 3PL 7d | Cov @ 3PL7 | Benchmark | Status |
|---|---|---|---|---|---|
| **STO-BUB-BAG-L** | **969 sheet / 600 Katrina** | 329.7 | **3d sheet / 2d actual** | 435/d | 🔴 **CRITICAL — express PO placed 27 May, awaiting Joel pay** |
| STO-BUB-BAG-S | 19,800 | 224.6 | 88d | 130/d | Above benchmark — check |
| STO-MAI-2 | 14,449 | 49.1 | 294d | 330/d | Safe |
| STO-MAI-BAG-S | 17,010 | 49.1 | 346d | 330/d | Safe |
| ACC-LAB | 8,085 | 239.9 | 33d | 735/d | OK — Avi 15k landing ~early Jun closes any gap |
| ACC-INS | 12,823 | 178.6 | 71d | 435/d | Safe |
| ACC-THA | 22,475 | 240.4 | 93d | 735/d | Safe |

**Read:** Bubble mailer is the #1 packaging crisis. Even with 09052026 ETA 22 Jun bringing 6,000 BUB, the 3-day cover at current 330/d burn projects OOS ~4 Jun — **18 days before 09052026 arrival**. Express PO is essential.

## CHECK-IN PROGRESS
None active. PO 14 / AUS 05052026 (express liquids) fully received 18 May. Next inbound is AUS 09052026, not yet at G3PL.

## DOUBLE-COUNT DETECTION
No active mid-check-ins. AUS 09052026 still on the water. **No double-counting.**

## LOCAL FILL STATUS

### Outsource Packaging — Heal Fill (PO 22-04-2026)
- **Status:** In production. NDA ingredients delivered ~28 May.
- **Fill started:** 29 May per Peter.
- **Remaining ingredients:** Green Living (Calcium Chloride), Sydney Solvents (Acetone) — landing TBC.
- **Earliest G3PL delivery:** ~25 Jun (14d fill + 7d transit, assuming all ingredients land this week).
- **Action:** Daniel chase Green Living + Sydney Solvents on dispatch dates if not landed by 5 Jun.

### Outsource Packaging — Remove 500ml Fill (PO 25-05-2026)
- **Status:** Placed 25 May; Peter scheduled, bundled with Heal cycle.
- **Same ingredient gates** — Sydney Solvents IBC quote unresolved (40+ days idle).
- **Action:** Daniel decide acetone source (Sydney IBC vs alternate) THIS WEEK.

## STOCK-OUT FORECAST (window 1 Jun → 22 Jun, pre-09052026)

| SKU | Stock | Burn rate | OOS by | 09052026 brings | Gap |
|---|---|---|---|---|---|
| KIT-ULT-6 (combined w COM) | 2,678 | 182/d (3PL 7d) | ~15 Jun | 6,104 kits (STA+COM+ULT) | -7d |
| LIQ-BAS-2 | 174 | 22/d | ~8 Jun | 2,592 | -14d |
| LIQ-SEN-2 | 64 | 9/d | ~8 Jun | 432 | -14d |
| LIQ-SEA-3 | 1,791 | 16/d | ~14 Aug | 2,808 | safe |
| LIQ-GLO-4 | 361 | 10/d | ~6 Jul | 1,296 | safe but lean |
| LIQ-HEA-5 (kit) | 4,122 | 182/d | ~23 Jun | 0 (OP fill not container) | OP fill 25 Jun ≈ same window — TIGHT |
| ACC-NAI-MAT | 0 | 141/d | now | 0 (not on container) | offer pivot pending |
| ACC-TIP-SQU | 543 | 68/d | ~9 Jun | 0 (not on container) | ongoing OOS |
| ACC-TIP-COF | 0 | n/a | already OOS | 0 | ongoing OOS |
| ACC-TIP-BAL | 251 | 114/d | ~3 Jun | 0 | OOS this week |
| ACC-REM-BOW | 0 | 3/d residual | already OOS | 6,840 | restocks 22 Jun (21d gap) |
| ACC-FRE-MANI | 0 | n/a | already OOS | 0 | ongoing OOS |
| STO-BUB-BAG-L | 600-969 | 330/d | **~4 Jun** | 6,000 | -18d **CRITICAL** |
| ACC-LAB | 8,085 | 240/d | ~5 Jul | 0 (Avi covers) | Avi 15k landing closes |

## CASCADING ARRIVAL PROJECTION (post-arrival cover at 3PL 7d rate)

| SKU | Now | After 09052026 (22 Jun) | After 07062026 (10 Jul) | After 05082026 (5 Aug) | After 04092026 (4 Sep) |
|---|---|---|---|---|---|
| KIT combined | 2,678 (15d) | OOS 7d, then +6,104 = 6,104 (33d post-arrival) | +5,668 = ~8,500 (47d) | +8,344 = ~14,000 (77d) | +5,880 = ~16,000 (88d) |
| LIQ-BAS-2 | 174 (8d) | OOS 14d, +2,592 = 2,138 | +2,376 = ~4,000 (180d) | +1,944 | +1,728 |
| LIQ-HEA-5 (kit) | 4,122 (23d) | -3,822 = 300, then +OP fill ~25 Jun (TBC qty) | continues OP-fed | OP-fed | OP-fed |
| ACC-REM-BOW | 0 (OOS) | +6,840 = 6,840 (2,600d at residual rate) | +2,000 | +5,000 | +1,080 |
| ACC-REM-500 | 3,588 (23d) | -3,250 = 338, then OP fill timing | +17,228 (07062026 OL increased) | +0 | +0 |
| STO-BUB-BAG-L | 969 (3d) | OOS 18d, +6,000 = 6,000 (18d) | +22,000 = 28,000 (85d) | +30,000 | +15,000 |

**The 22 Jun arrival is the crunch — everything depends on it landing on time.** Lily vessel is confirmed away ~20 May (5 weeks transit). No buffer.

## DELAY SCENARIO: IF AUS 09052026 SLIPS 3-5 DAYS
- Kit OOS gap: from -7d → -10 to -12d.
- BUB OOS gap: -21 to -23d (already 18d).
- BAS OOS gap: from -14d → -17 to -19d.
- HEA: cover may already be running out by 22 Jun — slip turns it into 5-7d OOS.

**There is no express bridge available** for kits (Sally still completing 07062026 in production; can't fast-track new container).

## OVERSTOCK FLAGS (post-arrival cover >100d)

| SKU | Current Cover | Post-09052026 Cover | Concern |
|---|---|---|---|
| LIQ-SEA-3 | 112d | post-09052026 ~135d | trim future containers |
| LIQ-BON-1 | 143d | post-09052026 ~180d | trim |
| LIQ-SOA-6 | 111d | post-09052026 ~150d | trim |
| ACC-REM (120ml) | 807d | unchanged | already known — bundle channel only |
| ACC-TIP-ALM | 325d | unchanged | already known |
| ACC-TIP-STI | 640d | unchanged | already known |

These are not actions for next week but should inform AUS 05082026 sizing decisions before Sally invoices.

## WHAT NEEDS ACTION

### 🔴 CRITICAL (act today)

1. **STO-BUB-BAG-L: 3d cover, OOS ~4 Jun.** Express PO placed 27 May, awaiting Joel pay. Also chase Jake on alt-mailer image + cost (Daniel asked 27 May, no reply 5 days). **Without this, all order fulfillment stalls in ~3 days.**
2. **Kit pool OOS ~15 Jun, 7 days before 09052026 arrives.** No bridge. Accept the OOS window or place customer-comms / website-throttling plan now.
3. **AUS 05082026 sized at 1.3x but Daniel's plan is 1.6x.** Sheet manifest needs Greg refresh to reflect: ULT 2,352 → ~3,500-4,500, more colours, free-gift item (10k+). Joel still owes 2 decisions (free gift product + new colours) before Sally invoices.
4. **ACC-TIP-BAL: 2 day cover at 114/d, no inbound.** Either error in 3PL reading (spike from a single bulk order?) or genuine pull through some attach. **Verify and decide if it needs to be added to the offer-pool.**

### 🟡 WARNING (act this week)

1. **LIQ-BAS-2: 8d cover, 14d gap before 22 Jun.** No bridge possible. Will run on backorder. Make sure CX comms reflects.
2. **LIQ-SEN-2: 7d cover.** Similar — 14d backorder gap.
3. **LIQ-HEA-5: 23d cover.** OP fill must land by ~25 Jun; if Green Living / Sydney Solvents delay ingredients, fill slips and Heal goes OOS. Daniel chase.
4. **ACC-TIP-SQU: 8d cover, no container restock.** Offer pivot away from Square Tips needed before 9 Jun.
5. **ACC-NAI-MAT: OOS now, residual deductions still happening.** 288-unit backorder. Offer already pivoting to Travel Bag — make sure Shopify SKU is fully turned off.
6. **AUS 07062026 V2 sheet not fully reflecting Daniel's 25 May upsize.** Get Greg to update so we're not flying blind on what Sally is actually producing.
7. **STO-BUB-BAG-S: 88d cover headline but burn 224/d vs benchmark 130/d — 73% above benchmark.** Either a wrong benchmark or an attach pattern shifting. Investigate.

### 🟢 MONITOR

- ACC-LAB: 33d cover, Avi 15k delivery 29 May per "Your Printers" notification — Greg confirm ASN at G3PL.
- ACC-FRE-MANI: OOS, 0 demand on Shopify, no backorder reported — may be safely retired.
- ACC-TRA-BAG: 1,950 on hand, becoming the new offer SKU. Burn rate unknown until offer goes live.

## PO RECOMMENDATIONS

| SKU | Current cover | Action |
|---|---|---|
| Kit container (CN) | 14d combined | AUS 05082026 already placed at 1.3x — needs Greg to update to 1.6x manifest |
| ACC-NAI-MAT | 0 / OOS | Drop from offer permanently OR add to AUS 05082026 if Daniel/Joel want offer continuity |
| ACC-TIP-SQU | 8d | Add to AUS 05082026 if intending to keep in offer mix |
| ACC-TIP-COF | 0 / OOS | Add to AUS 05082026 (zero in current pipeline) |
| LIQ-HEA-5 | OP fill in motion | Daniel to forecast next OP fill cycle after this one lands |
| STO-BUB-BAG-L | 3d | Express PO placed 27 May. Plan a future LCL for sustained supply if G3PL alt-mailer isn't viable. |

## FOLLOW-UP ITEMS

### Immediate (today)
- [ ] Joel: pay express bubble mailer PO
- [ ] Joel: decide free gift product + new colour collections for AUS 05082026
- [ ] Daniel: chase Green Living + Sydney Solvents on ingredient ETA
- [ ] Greg: refresh sheet to reflect AUS 07062026 V2 + AUS 05082026 1.6x sizing
- [ ] Daniel/Remy: confirm Shopify offer cutover from Mani Mat to Travel Bag is live

### By end of week
- [ ] Greg: refresh stale POS MODEL DSRs noted in Recap (LIQ-BAS-2, LIQ-SEA-3, LIQ-BON-1, LIQ-SOA-6, ACC-REM-BOW, KIT-COM-4)
- [ ] Daniel: decide acetone source for next Remove 500ml fill cycle
- [ ] Remy: chase Jake on B360 PACKUP variance (7 weeks stalled) + alt-mailer cost
- [ ] Joel: confirm Avi paid + ASN'd at G3PL

### Ongoing
- [ ] CX comms plan for 15 Jun - 22 Jun kit OOS window
- [ ] CX comms plan for 4 Jun bubble mailer OOS (or fulfillment alt-mailer rollout)
- [ ] Monitor weekly DSR — if kit drops below 175/d the 05082026 1.6x sizing may be overshoot
