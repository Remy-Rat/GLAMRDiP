# UK POS Model Check - 5 May 2026

## DATA FRESHNESS

- **POS MODEL last pasted:** 5 May 2026 (today, Greg AM paste).
- **3PL tab (B360):** last valid 5 May - **but represents frozen B360 Packup stock, NOT live Fulfillable.** Fulfillable on-hand is in POS MODEL col 7. No usable Fulfillable deduction feed yet.
- **Shopify last:** 4 May 2026 (+1 day lag, normal).
- **Growth factor:** 1.3x (unchanged).
- **Kit DSR base:** STA 13.0 + COM 41.6 + ULT 54.6 = 109.2/d at 1.3x (84/d base).
- **Actual 14d kit DSR:** 67.9/d → **effective 0.81x growth → -38% vs scaled target.**
- **Actual 7d kit DSR:** 71.7/d (0.85x). Slight WoW recovery off W17 floor.

### Manual overrides applied to sheet figures (Step 0a Gmail/Slack reconcile)

| SKU | Sheet says | Override | Source |
|---|---:|---:|---|
| LIQ-BAS-2 inbound on `UK Powder Room AND Chemence` | 8,000 | **7,568** | User confirmed 28/04: 432 redirected to Sweden via Fulfillable transhipment |
| LIQ-BAS-2 inbound on `UK Powder Room AND Chemence` status | "Completed, Est. Arrival 30 Apr" | **Landed at Fulfillable ~29 Apr** | Greg picking-list email to Ben 29/04; Daniel Slack 03/05 "Chemence liquids delivered in UK". Stock `g3pl_on_hand` may or may not yet reflect check-in - flagging as inbound until Fulfillable confirms |
| LIQ-GLO-4 inbound on same | 8,000 | 8,000 | No diversion |
| UK 03062026 ship-out | "complete, balance pending" | **Container production complete; balance unpaid as of today (28+ days open).** Sheet now shows Est. Completion 5 May / Est. Arrival 29 Jun (~55d transit) | User confirmation |
| Ben (Fulfillable) availability | sheet silent | **On paternity leave** (auto-reply 04/05). Escalations route through hello@fulfillable.co.uk + Roisin | Gmail auto-reply |

No Gmail/Slack stock events post Greg's paste this AM that would change hand counts.

---

## STOCK POSITION

Cover at projected (1.3x model) and actual (Shopify-derived; 14d unless noted) DSR side by side.

### Kits

| SKU | Stock | Projected DSR (1.3x) | Cover @ Projected | Actual 14d | Cover @ Actual |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 (Starter) | 137 | 13.0 | 11d | 11.6 | **12d 🔴** |
| KIT-COM-4 (Complete) | 3,968 | 41.6 | 95d | 24.2 | 164d |
| KIT-ULT-6 (Ultimate) | 3,852 | 54.6 | 71d | 32.1 | 120d |
| **All kits** | **7,957** | **109.2** | **73d** | **67.9** | **117d** |

**STA is critical.** Burned through ~86 units in 7 days (was 223 / 21d at 28/04). At 11.6/d actual, OOS by **~17 May**. UK 03062026 brings 448 STA but doesn't arrive until late Jun → ~6 weeks STA OOS unavoidable.

### Kit-Adjusted Liquids (Heal / Base / Glow at Fulfillable)

UK kit-adjusted demand = standalone Shopify + 1× kit-attach per kit sold. Using 14d kits 67.9/d.

| SKU | Stock | Standalone 14d | Kit-Adjusted Actual | Cover @ Kit-Adjusted | Notes |
|---|---:|---:|---:|---:|---|
| LIQ-HEA-5 (Heal) | 8,076 | 0.9 | 68.8 | **117d** | No fresh inbound |
| LIQ-BAS-2 (Base) | 7,164 | 19.8 | 87.7 | **82d** | + Chemence 7,568 inbound (override) ⇒ 168d post-checkin |
| LIQ-GLO-4 (Glow) | 7,875 | 8.8 | 76.7 | **103d** | + Chemence 8,000 inbound ⇒ 207d post-checkin |

**Read:** Once Fulfillable books in the Chemence 10-03-2026 fill (in-progress this week), Base/Glow cover jumps to 5-7 months. The single biggest cover risk this cycle is now neutralised.

### Standalone Liquids

| SKU | Stock | Model DSR | Shop 14d | Cover @ Actual | Notes |
|---|---:|---:|---:|---:|---|
| LIQ-SEA-3 (Seal) | 2,860 | 15.6 | 11.4 | 251d | + 432 on UK 03062026 |
| LIQ-BON-1 (Bond) | 570 | 6.5 | 2.4 | 238d | + 216 on 03062026 |
| LIQ-SOA-6 (Soak) | 597 | 6.5 | 2.1 | 284d | Plenty |
| LIQ-MAT-4 (Matte) | 799 | 7.8 | 2.1 | 380d | Plenty |
| LIQ-SEN-2 (Low Odour Base) | 0 | 0 | 0 | n/a | **Discontinued in UK** - ignore |
| LIQ-SEN-4 (Low Odour Glow) | 0 | 0 | 0 | n/a | **Discontinued in UK** - ignore |

### Remove Products

| SKU | Stock | Model DSR | Shop 14d | Cover @ Actual | Notes |
|---|---:|---:|---:|---:|---|
| ACC-REM (120ml) | 1,735 | 39.0 | 9.4 | 184d | Healthy |
| ACC-REM-500 | 4,406 | 36.4 | 8.4 | 525d | Heavy overstock |
| ACC-REM-BOW | 5,123 | 31.2 | 0.9 | 5,692d | Dormant — was 80/d in model, 0.9/d real (recap flag carried) |

Liquipak final 800L PO covers ~160d Remove from 02-04-2026 placement = **OOS scenario early Sep 2026** if no replacement filler.

### Inserts / Packaging

| SKU | Stock | Model DSR | Cover @ Model | Notes |
|---|---:|---:|---:|---|
| ACC-INS (Instructions) | 8,903 | 106.6 | 84d | + 4,080 on UK 02082026, plus 7,349 in B360 packup (frozen) |
| ACC-LAB-UK (Labels Booklet) | 6,570 | 217.1 | **30d 🟡** | No CN inbound - local Print Runner only. **Place by ~10 May** |
| ACC-THA (Thank You) | 23,798 | 217.1 | 110d | + 5,600 on 03062026 |
| STO-BUB-BAG-L | 11,893 | 106.6 | 112d | + 2,300 on 03062026 |
| STO-MAI-2 | 8,284 | 110.5 | 75d | + 5,280 on 03062026 |
| STO-MAI-BAG-S | 10,604 | 110.5 | 96d | + 4,000 on 03062026 |

Note: ACC-LAB-UK 30d at projected, but at 76.0/d actual orders rate (per digest), real cover ≈ **86d** - more comfortable. Refresh Print Runner trigger against actual not model.

---

## DOUBLE-COUNT DETECTION

`UK Powder Room AND Chemence` (10-03-2026 Chemence fill) is the only shipment where check-in could be partial:

| SKU | POS OL (sheet) | Override | Fulfillable On-Hand | Already In? |
|---|---:|---:|---:|---|
| LIQ-BAS-2 | 8,000 | 7,568 | 7,164 | Likely **not yet checked in** (delivered ~29/04, normal Fulfillable check-in 3-7 days) |
| LIQ-GLO-4 | 8,000 | 8,000 | 7,875 | Likely **not yet checked in** |

The sheet's Projected ON HAND adds OL to current — overstated by **15,568 units** if Fulfillable checks in this week and Greg doesn't refresh col 7. Watch tomorrow's POS MODEL paste.

No other active check-ins.

---

## CONTAINER / ORDER STATUS

### UK 03062026 - **balance still unpaid (28+ days open)**
- POS MODEL: In Production, Est. Completion **5 May** (today), Est. Arrival 29 Jun. Note: 55-day transit baked into sheet (vs Lead Times.md 42d standard).
- Slack/Gmail: zero update in 21 days. Joel silent on Daniel's 28/04 ask.
- **Latest pay-date analysis: see dedicated section below.**

### UK 02072026 - Birthday Sale, in production
- Est. Completion 18 May, Est. Arrival 12 Jul. Deposit paid 14 Apr.
- Brings: 336 STA + 1,316 COM + 1,148 ULT + 5,600 ACC-THA + 200 Cotton Candy + 200 Crush + 200 Goddess + 400 Peachy + 400 Sincere + colours.

### UK 02082026 - planned, fill PO not yet placed
- Per sheet: Est. Completion 22 Jun, Est. Arrival 16 Aug.
- Last recap had user-pushed PO place date to ~13 May. **8 days from now.** No Daniel email visible in 21d Gmail - day-of placement assumed.

### UK Powder Room AND Chemence (10-03-2026) - landed
- POS MODEL: status Completed, Est. Arrival 30 Apr.
- Real status: **delivered to Fulfillable around 29 Apr** (Daniel 03/05). Check-in pending.

### 22-04-2026 Chemence (next fill) - blocked
- POS MODEL: Status Ordering, Est. Completion 17 Jun.
- Vik replied 28/04 asking for free-issue caps/brushes balance. Daniel sent tracker 29/04. **No reply from Vik in 6 days.**
- Owner: Daniel chase Vik this week. If silent through Thu 7 May, escalate.

### B360 PACKUP STOCK - frozen
- 288,898 units locked. £8,500 deposit "being paid slowly" (Daniel 04/05 digest thread). No Mason/Chris correspondence in 21d.
- Includes: 493 STA, 40 COM, 1,653 Heal, 7,349 ACC-INS, 19,445 STO-BUB-BAG-S (the only inbound on this SKU - Fulfillable currently 0), 1,396 ACC-LAB-UK, 5,246 ACC-THA, 45 OOS colour SKUs.
- **Treat as fully unavailable through end of June** at current £1k/week pace.

---

## UK 03062026 - LATEST BALANCE PAY DATE (key user ask)

**User cash-conservation question: latest pay date that still gets 03062026 in on time at actual DSR.**

### Inputs
- Production complete; balance unpaid; ship-out gated on payment + Lily booking (~1-2 day cycle).
- Vessel transit: sheet uses 55 days; Lead Times.md standard 42 days. Realistic median ~45-50 days for UK.
- Container brings: 448 STA + 1,484 COM + 700 ULT + 5 colour SKUs that are CURRENTLY OOS or <12d cover (Crush-090, Peachy, Bubbly, Goddess, Sincere) + 5,600 ACC-THA + replenishment STO/inserts.
- Next backstop: UK 02072026 arrives **12 Jul**.

### Pay-by → arrival map (using sheet's conservative 55d transit)

| Pay date | Ship +1d | Arrival 55d | Days before 02072026 (12 Jul) |
|---|---|---|---:|
| 5 May (today) | 7 May | **1 Jul** | 11 days |
| 12 May | 14 May | **8 Jul** | 4 days |
| 19 May | 21 May | **15 Jul** | -3 days (lands AFTER 02072026) |
| 26 May | 28 May | **22 Jul** | -10 days |

### Read

- **STA gap is unsavable.** STA stocks out ~17 May regardless. UK 03062026 cannot land in 12 days. Daniel's COM substitution plan (per 28/04 summary) is the only lever - **needs Joel sign-off this week.**
- **Top-seller colours that 03062026 saves** (Crush-090, Peachy, Bubbly, Goddess, Sincere) are all already OOS or <8d. They're going OOS regardless. Pay-date determines duration of OOS pain, not whether OOS happens.
- **Critical threshold: 12 May.** Pay any later than that and 03062026 lands within 4 days of 02072026 (12 Jul) - the two arrivals merge into a single replenishment cluster, killing 03062026's value as a distinct mid-cycle drop.

### Recommendation - REVISED after user clarification (5 May)

**User position:** colour OOS handled separately via express if needed; STA gap unsavable by any container. So colours + STA are off-table as pay-date drivers.

**Operational stock penalty of pay delay = effectively nil up to ~end of May.** Every non-colour SKU on UK 03062026 has 75d+ cover today, and UK 02072026 (12 Jul) + 02082026 (16 Aug) backstop everything before any non-colour SKU runs thin.

**Recommended pay window: 19-26 May 2026.**

| Pay date | Arrives | Role of 03062026 |
|---|---|---|
| 5-12 May | ~22 Jun-8 Jul | Pre-Birthday-Sale distinct top-up |
| **19-26 May** | ~5-22 Jul | Merges with or lands shortly after UK 02072026 (12 Jul); functional mid-cycle drop |
| Past mid-Jun | Mid-Jul to mid-Aug | Begins overlapping UK 02082026 placement; Sally relationship may strain |

**Soft constraints (not stock):**
- Sally relationship: 28+ days open, no email chase visible in 21d Gmail. Birthday Sale 02072026 deposit paid means she has skin in game. Realistic limit ~4-6 weeks before escalation = mid-Jun.
- Air-freight buffer: ~£1-2k per Sally express colour run. Cash benefit of 2 weeks pay-date push (~£2-5k retained) > 1 air-freight cost.

**Bottom line: pay anywhere 19-26 May. Buys 2-3 weeks cash retention with no operational stock penalty given express-colour fallback.**

---

## STOCK-OUT FORECAST

### 🔴 STOCKOUT BEFORE ARRIVAL (gap < 0)

| SKU | Stock | Actual DSR | Stocks out | Next inbound | Arrives | Gap |
|---|---:|---:|---|---|---|---:|
| KIT-STA-2 | 137 | 11.6 | **17 May** | UK 03062026 (448) | ~22 Jun-8 Jul | **-36 to -52d** |
| POW-COT-030 (Cotton Candy) | 0 | 1.7 (30d) | already OOS | UK 02072026 (200) | 12 Jul | -68d (already gone day 7) |
| POW-CRU-090 (Crush) | 0 | 6.8 | already OOS | UK 03062026 (200) | ~22 Jun | -48d already |
| POW-JUS-449 (Just Friends) | 0 | 5.4 | already OOS | nothing pipeline | n/a | indefinite |
| POW-OVE-487 (Over It) | 3 | 7.5 | now | nothing pipeline | n/a | indefinite |
| POW-PEA-068 (Peachy) | 47 | 12.5 | ~9 May | UK 03062026 (1,200) | ~22 Jun | -45d |
| POW-SEA-450 (Seaside) | 37 | 6.1 | ~11 May | nothing on 03062026/02072026 | n/a | indefinite |
| POW-FAI-308 (Fairytale) | 46 | 5.4 | ~14 May | nothing | n/a | indefinite |
| POW-NOT-065 (Not 2day) | 49 | 5.7 | ~14 May | nothing | n/a | indefinite |
| POW-GOD-017 (Goddess) | 48 | 4.9 | ~15 May | UK 03062026 (400) | ~22 Jun | -38d |
| POW-BUB-516 (Bubbly) | 51 | 5.3 | ~15 May | UK 03062026 (400) | ~22 Jun | -38d |
| POW-SIN-254 (Sincere) | 141 | 8.9 | ~21 May | UK 03062026 (800) | ~22 Jun | -32d |

### 🟡 TIGHT (0-7d margin or near-OOS)
- POW-TRA-452 (Train-Wreck): 163 / 16.1 = 10d. UK 03062026 brings 800 - saved with ~6 weeks gap.
- POW-BAR-198: 279 / 10.7 = 21d. UK 03062026 brings 1,600. Likely lands in time.

### 🔴 NOTHING ON ORDER (no inbound for SKU)
- **Just Friends (POW-JUS-449)** - 0 stock, 5.4/d, **nothing on 03062026, 02072026, or 02082026.** Past CN PO deadline (84d). Express only or accept indefinite OOS.
- **Over It (POW-OVE-487)** - 3 units, 7.5/d, same. **(Carried from last 3 recaps.)**
- **Seaside (POW-SEA-450)** - 37 units, 6.1/d, same.
- **Fairytale (POW-FAI-308)** - 46 units, 5.4/d, same.
- **Not 2day (POW-NOT-065)** - 49 units, 5.7/d, same.

These 5 SKUs have **structurally fallen out of the pipeline.** Either Daniel adds to UK 02082026 (fill PO place ~13 May - 8 days), or they're written off until rebuild.

---

## CONTAINER GAP ANALYSIS

### UK 02082026 (fill PO due ~13 May) - critical gap items

Pull what's NOT in the container vs SKUs running thin:

- **ACC-LAB-UK: 0 units (correct - local Print Runner only).** Place Print Runner PO this week.
- **5 OOS colours with nothing in pipeline** (Just Friends, Over It, Seaside, Fairytale, Not 2day). **Daniel: confirm whether to add to UK 02082026.** Each at 5-8/d × 84d shipping cycle = 420-672 units to bridge until next-next container.
- **STA quantity (560 on 02082026)**: at 11.6/d actual, that's 48d cover post-arrival. If kit demand recovers to 1.3x (109/d total → STA ~13/d), 43d cover. Tight but workable IF 03062026 arrives on time first.

### Cross-cutting: B360 packup gaps if it stays frozen
- **STO-BUB-BAG-S: 0 in Fulfillable, 19,445 in B360 packup.** If packup stays frozen and a kit-adjacent product spikes, this is the first packaging to gap.
- **ACC-LAB-UK: 1,396 in packup (offset by Print Runner local print).** Bigger lever is Print Runner PO.
- **STA: 493 in packup**. Could close the STA gap if released by mid-May. Worth pushing the £8,500 conversation.

---

## LOCAL FILL STATUS

### Chemence (Base, Glow, Seal)
- **10-03-2026 fill: landed at Fulfillable ~29 Apr.** 7,568 BAS + 8,000 GLO. Awaiting Fulfillable check-in confirmation. Stock will jump 5-7 months cover once booked in.
- **22-04-2026 fill: BLOCKED.** Vik 28/04 asked for free-issue caps/brushes balance. Daniel sent tracker 29/04. 6 days silent. Required for 60-day completion (~22 Jun target).
- **432 BAS-2 to Sweden:** Remy emailed Ben for air-freight quote 04/05. Ben on pat leave - escalate via hello@fulfillable.co.uk.

### Oils4Life (Heal)
- No active PO. Heal at 117d cover at kit-adjusted 14d rate.
- Last comms 21d+ silent.
- **Recommended: outbound chase Dale this week.** Heal lead time TBD - confirm ~28d from order so we can plan next placement at ~70-80d cover (mid-late May).

### Liquipak (Remove 120ml/500ml) - exiting
- Final 800L fill placed 02-04-2026. Lead time TBD from Simon (silent since 09/04).
- Coverage post-fill: ~160d Remove. **OOS scenario early Sep.**
- **8+ weeks no replacement filler found** (search ongoing - no fillers willing at <20% uplift). Realistic options:
  1. Accept ~20% cost uplift with one of the contacted alt-fillers (none confirmed yet but it's the price implied by their initial responses).
  2. Continue cold-outreach; accept early-Sep OOS risk if no luck.
  3. Substitute: ship Remove from a sister region (CA Swift overstock), accepting freight cost.

---

## PACKAGING & INSERTS MONITORING

3PL deduction monitoring is **blind on Fulfillable** - B360 tab represents frozen packup, not the live 3PL. No usable post-13 Apr deduction view.

**Action:** Roisin export 14d Fulfillable deduction history (open since last 2 recaps).

Static stock view (POS MODEL only):
- ACC-LAB-UK 30d (model rate) - **trigger Print Runner PO this week.**
- ACC-INS 84d - healthy.
- ACC-THA 110d - healthy.
- STO-BUB-BAG-L 112d - healthy.
- STO-BUB-BAG-S **0 in Fulfillable** (19,445 in B360 packup, frozen). At ~liquid-only-order rate, runway is unclear without deduction data. Watch.

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (act today / this week)

1. **Joel: confirm decision on UK 03062026 balance.** Pay window **19-26 May** (revised from 12 May after user clarified colours/STA off-table). Buys 2-3 weeks cash retention; no operational stock penalty.
2. **Joel: approve Daniel's COM-substitution plan for STA gap.** STA OOS by 17 May, container can't save it. Decision needed before 17 May - 12 days.
3. **Daniel: chase Vik (Chemence) on free-issue caps/brushes balance** sent 29/04. 6 days silent. Blocks 22-04-2026 ETA.
4. **Daniel: place UK 02082026 fill PO by 13 May.** 8 days. Add Just Friends + Over It + Seaside + Fairytale + Not 2day quantities (420-672 each) if we want to rebuild those SKUs.
5. **Remy: place Print Runner ACC-LAB-UK PO this week.** 30d cover at model rate; trigger window is now.

### 🟡 WARNING (act within 14 days)

6. **Daniel: Liquipak replacement decision.** 8+ weeks open. Practical paths:
   - **Path A:** Re-engage the contacted alt-fillers, accept their ~20% higher price quotes formally. Locks in continuity.
   - **Path B:** Continue cold-outreach, accept Sep OOS risk if no luck.
   - **Path C:** Cross-region: ship Remove from CA Swift overstock to UK. Adds freight cost but uses existing supply chain.
7. **Joel: £8,500 B360 deposit pace.** £1k/week = 8.5 weeks to fund. STO-BUB-BAG-S, STA bridging stock, and 7,349 ACC-INS sit behind this. Worth Joel-Daniel call on whether to accelerate.
8. **Remy: chase Dale (Oils4Life)** - 21d+ silent. Pre-empt next Heal fill timing.
9. **Remy: Roisin export 14d Fulfillable deduction history.** Carried 2 cycles - first time we'll see Fulfillable deduction integrity.
10. **Remy: chase Ben/hello@ for 432 BAS-2 air-freight quote to Sweden** - Ben on pat leave.

### 🟢 MONITOR (FYI)

- POW-COT-030 (Cotton Candy) OOS day 7. UK 02072026 brings 200 (12 Jul). 9-week OOS. No save.
- 5 OOS colours with no pipeline (Just Friends, Over It, Seaside, Fairytale, Not 2day). Decision lever = UK 02082026 (action #4).
- Heal cover 117d at actual - comfortable. Next Oils4Life PO ~mid-late May.
- ACC-REM-BOW 5,123 at 0.9/d - 5,692d cover. Dormant. Carry forward as overstock signal.

---

## CASCADING ARRIVAL PROJECTION

At actual 14d kit DSR (67.9/d) and assuming UK 03062026 pay 12 May → ship 14 May → arrive ~5 Jul.

| | NOW | After Chemence book-in (~7 May) | After UK 03062026 (~5 Jul) | After UK 02072026 (~12 Jul) | After UK 02082026 (~16 Aug) |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 137 (12d) | 137 (12d) | OOS days 18-61 | post-arrival 484 (42d) | post-arrival 1,044 (90d) |
| KIT-COM-4 | 3,968 (164d) | 3,968 (164d) | 2,469 + 1,484 = 3,953 (163d) | + 1,316 = 5,269 (218d) | + 1,148 = 6,417 (265d) |
| KIT-ULT-6 | 3,852 (120d) | 3,852 (120d) | 1,856 + 700 = 2,556 (80d) | + 1,148 = 3,704 (115d) | + 840 = 4,544 (142d) |
| LIQ-BAS-2 | 7,164 (82d) | 14,300 (163d) | likely refilled (Chemence cycle) | - | - |
| LIQ-GLO-4 | 7,875 (103d) | 15,875 (207d) | likely refilled | - | - |
| LIQ-HEA-5 | 8,076 (117d) | 8,076 (117d) | post-Oils4Life fill expected | - | - |

### Overstock flags (post-arrival cover > 100d, target 45-75d)
- KIT-COM-4: 218d after 02072026 at actual 0.81x rate, ~93d at projected 1.3x. **At projected: within target band.** Health-check signal only.
- KIT-ULT-6: 142d after 02082026 at actual; ~70d at projected. Within target.
- LIQ-BAS-2 / LIQ-GLO-4: at projected 1.3x, post-Chemence book-in is ~3.6 months Base / 4.3 months Glow; after 22-04-2026 lands ~22 Jun, sits at ~4 months cover both. **Healthy 60-90d target buffer. 22-04-2026 quantities fine as ordered.**

Per `feedback_growth_factor_framing.md`: growth factor is aspirational, sizing decisions stay at projected. Actual rates are health-check signals, not order-revision triggers.

### IF UK 03062026 SLIPS PAST 19 MAY (becomes 02072026-cluster)
- All cover figures above hold; net effect = single big arrival ~12 Jul instead of two distinct drops.
- STA gap extends from 36-52d to 56+ days. COM substitution becomes the structural plan, not a bridge.
- Top-seller colour OOS pain extends from ~6 weeks to ~8 weeks.

---

## FOLLOW-UP ITEMS

**Immediate (this week)**
- [ ] Joel: confirm UK 03062026 balance pay date - pay window 19-26 May (cash-tight friendly, no stock penalty)
- [ ] Joel: approve COM-substitute-for-STA plan
- [ ] Daniel: chase Vik on free-issue stock + 22-04-2026 ETA
- [ ] Daniel: decide whether to add 5 OOS colours to UK 02082026
- [ ] Remy: place Print Runner ACC-LAB-UK PO (~10,000 units)
- [ ] Remy: outbound Dale (Oils4Life) for next Heal fill timing

**By 13 May**
- [ ] Daniel: place UK 02082026 fill PO
- [ ] Daniel: Liquipak replacement decision (Path A/B/C above)

**Ongoing / Watch**
- [ ] Roisin Fulfillable deduction export (data integrity)
- [ ] Ben/hello@ Sweden air-freight quote (Ben on pat leave)
- [ ] Greg: refresh POS MODEL post Fulfillable Chemence check-in (avoid double-count)
- [ ] Greg: review COM/ULT/BAS/GLO quantities on UK 02082026 + 22-04-2026 Chemence vs 0.81x actual demand
