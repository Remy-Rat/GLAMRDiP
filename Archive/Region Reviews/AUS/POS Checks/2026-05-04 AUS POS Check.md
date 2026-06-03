# AUS POS Model Check — 4 May 2026

## DATA FRESHNESS

- **POS MODEL extracted:** 4 May 11:30 AEST (xlsx re-pulled fresh today). `UPDATED` cell did not parse — assume Greg pasted same-day.
- **3PL data last valid:** 4 May (today).
- **Shopify data through:** 3 May (+1 day lag, normal).
- **Growth factor:** 1.3x (base 147 kits/d → scaled 191.1/d).

## MANUAL OVERRIDES (user-confirmed today)

| Field | Sheet | Override | Source |
|---|---|---|---|
| POW-CLE-193 (-203) and POW-SUN-SU015 (-123) deductions on 4 May | Both flagged as 3PL anomalies | **Expected, not anomalies** — these are part of the AUS-$85-GIF GWP campaign (launched 3 May). | User confirmed; Daniel/Katrina email thread 3 May. |
| AUS 08072026 Heal-in-kit qty | Sheet shows 0 LIQ-HEA-5 in 08072026 | **Will not be available** — YDM ingredients ~8 weeks from 1 May per Joel; Container #5 (14 Aug) is earliest plausible CN-Heal-in-kit window. Care/Heal bottle LCL to OP planned as bridge fill. | User-confirmed today. |
| AUS 05052026 (22-04-2026 Isay Express) | Sheet: completion 29 Apr / arrival 6 May | **Not shipped yet** — sheet ETA invalid. Treat as unknown until Sally despatches. | User-confirmed today. |
| 25-02-2026 OP Heal "1,300 short" | Open since 13 Apr | **Confirmed real, not a count error** — Katrina 1 May email: physical count + warehouse sweep confirms SH numbers accurate. 3PL tab shows +7,570 LIQ-HEA-5 inbound on 11 Apr (vs 9,000 ordered = 1,430 short, ~16% yield miss). No "secret" inbound exists. **Net effect: 1,300+ Heal units to be written off.** |
| LIQ-SEN-2 (LO Base) on hand | Sheet expected ~24 | **0 units as of 4 May** — fell to zero today (was 24 yesterday). Real OOS. | 3PL tab. |

---

## STOCK POSITION

### KITS

| SKU | Stock | Projected DSR (1.3x) | Cover @ Projected | Actual DSR (3PL 14d) | Cover @ Actual |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 885 | 44.2 | **20d** | 21.9 | 40d |
| KIT-COM-4 | 4,364 | 101.4 | 43d | 40.1 | 109d |
| KIT-ULT-6 | 2,636 | 45.5 | 58d | 17.5 | 151d |

Starter Kit drops below 21d projected cover. AUS 09052026 (per sheet now arriving 20 Jun, see Container Status) brings 2,016 STA → cover after = 12d gap at projected, +33d at actual. STA is the kit-side risk.

### LIQUIDS

| SKU (Name) | Stock | Model DSR | Cov @ Model | 3PL 14d | Cov @ 3PL | Inbound |
|---|---:|---:|---:|---:|---:|---|
| LIQ-BAS-2 (Base) | **298** | 53.3 | **6d** | 24.7 | 12d | +648 AUS 05052026 (NOT SHIPPED), +2,592 AUS 09052026 (20 Jun) |
| LIQ-SEN-2 (LO Base) | **0** | 9.1 | **OOS** | 7.3 | OOS | +216 AUS 05052026 (NOT SHIPPED), +432 AUS 09052026 (20 Jun) |
| LIQ-GLO-4 (Glow) | 755 | 26.0 | 29d | 9.4 | 80d | +1,296 AUS 09052026 (20 Jun), +1,512 AUS 07062026 (21 Jun) |
| LIQ-SEN-4 (LO Glow) | 113 | 7.8 | 14d | 5.0 | 23d | +216 AUS 05052026 (NOT SHIPPED), +432 AUS 09052026 (20 Jun) |
| LIQ-SEA-3 (Seal) | ~2,400 | 44.2 | 54d | ~13/d | ~185d | +2,808 AUS 09052026 (20 Jun) |
| LIQ-HEA-5 (Heal) | 9,390 | 184.6 | 51d | 82.2 | 114d | +11,500 OP fill 22-04-2026 (ETA contingent on Joel paying ND proforma) |
| ACC-REM-500 | 7,787 | 98.8 | 79d | (24 Apr inbound +4,795, post-fill rate ~70-100/d) | ~80d | covered through ~22 Jul; AUS 08072026 has 5,000 ACC-RE5-BOT/LID/INN for next OP fill |
| ACC-REM-BOW | 1,031 | 75.4 | 14d | 31.6 | 33d | +6,840 AUS 09052026 (20 Jun), +2,640 AUS 08072026 (15 Jul) |

### INSERTS / PACKAGING

| SKU | Stock | 3PL 14d | Cover @ 3PL | Inbound |
|---|---:|---:|---:|---|
| ACC-LAB | 15,788 | 145.9 | 108d | **NONE - not in 09052026, 07062026, 08072026.** Avi PO needed mid-May. |
| ACC-THA | 30,178 | 145.9 | 207d | +30,800 AUS 09052026 (20 Jun), +11,200 AUS 07062026 (21 Jun). **NOT in 08072026.** |
| ACC-INS | 17,998 | 79.3 | 227d | +5,280 each on 09052026 / 07062026 / 08072026 |

### COLOURS WORTH FLAGGING

- **POW-SIN-254 (Sincere):** 1,902 units / 9.6 14d DSR = 198d. Top seller. PO 9 reconciliation flagged 200 under-received, still pending Jake's Friday count. AUS 08072026 brings +600.
- **POW-COR-481:** 490 units / 0.5/d = 980d. Massive overstock, 200 inbound on 08072026 — review.
- **5 colours under 30d cover** (POW-BOR-355, POW-HOT-568, POW-RED-165, POW-SPI-144, POW-GAR-656) — all on AUS 08072026 (+600 each). Same as 27 Apr - no movement, all dependent on 15 Jul arrival landing on time.

---

## CHECK-IN PROGRESS

No active partial check-ins. PO 9 B360 PACKUP delivered (variances under Jake's Friday count, still outstanding). PO 10 25-02-2026 OP fill closed at 7,570 (vs 9,000 ordered) - 1,300+ shortfall now confirmed via Katrina's 1 May warehouse sweep. PO 11 (Avi) check-in shown on 18 Apr at +14,808 ACC-LAB.

---

## DOUBLE-COUNT DETECTION

POS MODEL still shows **OP Heal/Remove 500ml** block with Heal +1,300 inbound and ACC-REM-500 +911 inbound. Status:
- **LIQ-HEA-5: the 1,300 is fictitious** — original PO 10 (25-02-2026) shipped 9,000 OL but only 7,570 booked at G3PL on 11 Apr. The 1,300 short is the gap, not pending inbound. Greg should remove this from POS MODEL projection or the model overstates Heal cover by 1,300.
- **ACC-REM-500: 911 inbound also fictitious** — was the matching PO 9 B360 PACKUP variance line. PO 9 already booked.
- **Action:** Greg to flatten the OP Heal/Remove 500ml block to "Delivered, no inbound" so projected ON HAND is correct.

---

## CONTAINER / ORDER STATUS

### AUS 05052026 (22-04-2026 Isay Express, small bridge)
- POS MODEL: completion 29 Apr / arrival 6 May / status In Production
- **Reality (user 4 May):** **NOT SHIPPED YET**. Sally hasn't despatched. The 648 LIQ-BAS-2 cost-transfer from CA 15012026 (per Daniel 22 Apr Slack) is in-hand at Sally but not en route.
- Cargo: 648 LIQ-BAS-2, 216 LIQ-SEN-2, 216 LIQ-SEN-4 + Powder Room express colours.
- ACTION: **Daniel/Lily WeChat Sally TODAY for shipping date.** Each day of delay = LIQ-BAS-2 / LIQ-SEN-2 OOS extends. Sheet ETA invalid - update.

### AUS 09052026 (40HQ standard container)
- POS MODEL: **completion 21 May / arrival 20 Jun** (sheet revised since last review).
- 27 Apr position: completion 5 May, arrival 5 Jun. Sheet now shows a **further 16-day slip** vs Mark's 27 Apr update.
- No Mark / Sally / Lily comms in 9 days to validate the new dates.
- ACTION: Confirm with Mark whether 21 May is realistic or another fallback. If real, kit cover gap widens.

### AUS 07062026 (Birthday Sale, 1.4x growth factor)
- POS MODEL: completion 22 May / arrival 21 Jun.
- Deposit paid (user-confirmed 27 Apr).
- Liquids landing 21 Jun close behind 09052026 (20 Jun).

### AUS 08072026 (next standard, 15 Jul arrival)
- POS MODEL: completion 15 Jun / arrival 15 Jul. Fill PO place date **6 May (2 days).**
- **CRITICAL GAPS in current draft:**
  - **NO ACC-LAB.** 27 Apr POS Check flagged - still no movement. Add ~20,000 to container.
  - **NO ACC-THA.** Same. Add 15-20,000.
  - **NO LIQ-HEA-5 (kit-Heal).** Per user today: Heal-in-kit not realistic on this container due to YDM ingredients ~8 weeks out from 1 May. **Treat as committed: 08072026 ships without kit-Heal. Bridge via Care/Heal LCL → OP fill.**
- Heal components in container: 20,000 each HEA-EMP / HEA-LID / HEA-BSH (for next OP fill, NOT finished Heal).
- ACTION: Daniel to draft revision **today** (place 6 May).

### Container #5 (unnamed - completion 15 Jul / arrival 14 Aug)
- POS MODEL header: ref blank.
- **This is the earliest plausible CN-Heal-in-kit container** if YDM ingredients land end-Jun and YDM fill takes 30-40 days.
- ACTION: Daniel + Joel to confirm Container #5 raw goods PO timing - this is the container that closes the Heal gap.

### B360 PACKUP (Delivered 16 Apr)
- Sheet status correct.
- 23-SKU variance investigation ongoing (Jake's Friday count overdue).

---

## LOCAL FILL STATUS

### Outsource Packaging — Heal 11,500 (ref: 22-04-2026)
- POS MODEL: In Production, no Est. Completion / Est. Arrival.
- Gmail: Chantelle (ND) sent proforma invoice 28 Apr. **Awaiting Joel payment 6 days.**
- Peter (27 Apr): "filling scheduled, awaiting raw material arrival."
- Lead time path from Joel payment day (D0): D+5 ingredients ship → D+7 ingredients at Peter → +30d fill → +7d ship to G3PL = **D+47 to D+50** at G3PL.
  - Pay Tue 5 May → ETA G3PL ~21 Jun
  - Pay Fri 8 May → ETA G3PL ~24 Jun
  - Pay Mon 12 May → ETA G3PL ~28 Jun
- ACTION: Joel pay ND proforma this week. Greg to add ETA to POS MODEL once paid.

### Care/Heal Bottle LCL to OP (NEW - per Daniel 1 May Slack)
- Not yet placed. User-confirmed today: "we need to work something out here."
- Purpose: bridge AUS Heal demand from ~Jul through to Container #5 CN-Heal-in-kit arrival (~mid-Aug minimum).
- Sizing scenario: 184.6/d × 60-90d bridge = ~11,000-16,000 units finished Heal needed.
- Bottle/component cost: HEA-EMP/LID/BSH already in 08072026 container at 20,000 each (lands 15 Jul) - sufficient stock for 1-2 follow-up OP fills.
- Lead time: LCL bottle send + OP fill cycle = ~6-8 weeks total if Daniel pulls Heal bottles forward (LCL transit ~3-4 weeks + 30d fill + 7d ship).
- ACTION: Daniel to size and source. Joel to approve LCL freight cost.

### Outsource Packaging — Remove 500ml (ref: 24-03-2026)
- DELIVERED 24 Apr 2026 (confirmed via 3PL +4,795 jump). Stock 7,787.
- Closed.

---

## STOCK-OUT FORECAST

### STOCKOUT NOW / IMMINENT

| SKU | Stock | DSR | Status | Inbound | Gap |
|---|---:|---:|---|---|---:|
| **LIQ-SEN-2 (LO Base)** | **0** | 7.3 | **OOS today** | AUS 05052026 +216 (NOT SHIPPED) | indeterminate - depends on Sally despatch |
| **LIQ-BAS-2 (Base)** | 298 | 24.7 | OOS in ~12d (16 May) | AUS 05052026 +648 (NOT SHIPPED), then AUS 09052026 +2,592 (20 Jun) | If Sally despatches this week, safe; otherwise potential OOS 16-22 May |

### TIGHT (gap < 10 days at projected)

| SKU | Stock | DSR | Stocks Out | Next Inbound | Gap |
|---|---:|---:|---|---|---:|
| LIQ-SEN-4 (LO Glow) | 113 | 7.8 model / 5.0 actual | 17 May / 27 May | AUS 05052026 +216 (NOT SHIPPED) → AUS 09052026 +432 (20 Jun) | bridge dependent on Sally despatch |
| KIT-STA-2 | 885 | 44.2 model / 21.9 actual | 24 May / 14 Jun | AUS 09052026 +2,016 (20 Jun) | -27d at model / -6d at actual |
| ACC-REM-BOW | 1,031 | 75.4 model / 31.6 actual | 19 May / 6 Jun | AUS 09052026 +6,840 (20 Jun), +2,640 AUS 08072026 (15 Jul) | -32d at model / -14d at actual |

### NOTHING ON ORDER

| SKU | Stock | DSR | Stocks Out | Deadline to Act |
|---|---:|---:|---|---|
| ACC-LAB | 15,788 | 145.9 (3PL) | ~19 Aug (108d) | Place Avi PO ~mid-May for 20,000 (10-21d Avi lead) |
| LIQ-HEA-5 (post-22-04-2026 fill) | 9,390 + 11,500 (~21 Jun) | 184.6 model / 82.2 actual | OOS at projected ~26 Aug if no further fill / OOS at actual ~mid-Jan 2027 | **Care/Heal LCL bridge fill needs to be in flight by ~late May** to land before any projected-rate OOS scenario |

### SAFE

LIQ-GLO-4, LIQ-SEA-3, all other liquids, ACC-INS, ACC-THA, vast majority of colours.

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (act today)

- **LIQ-SEN-2 OOS now.** Listing handling decision needed (mark OOS, accept gap, or attempt express via Sally with Lily). AUS 05052026 has 216 inbound but not despatched.
- **LIQ-BAS-2 12d cover.** Without AUS 05052026 shipping by ~10-12 May, OOS by 16 May. Sally has 648 in hand from CA cost transfer per Daniel 22 Apr — express via Lily becomes the bridge.
- **Daniel: AUS 08072026 fill PO drafting. Place 6 May (2 days).**
  - Add ACC-LAB ~20,000.
  - Add ACC-THA ~15-20,000.
  - **Confirm: no LIQ-HEA-5 in kit (per today's Heal call).** Heal components (HEA-EMP/LID/BSH 20,000 each) already in - keep.
  - Cut COM/ULT to actual run-rate (40/d / 17/d) - 27 Apr Sales Analysis recommended ~50/d COM, 17-22/d ULT.
- **Joel: pay New Directions proforma.** Each day = 1 day OP Heal fill slip. Pay this week to keep 21 Jun ETA.
- **Greg: clean POS MODEL.**
  - Remove the 1,300 LIQ-HEA-5 + 911 ACC-REM-500 phantom inbound from "OP Heal/Remove 500ml" block (already delivered, the gap is a write-off not pending stock).
  - Update AUS 05052026 status to reflect "not yet despatched" - currently sheet shows arrival 6 May.
  - Update AUS 09052026 sheet completion 21 May / arrival 20 Jun was a Greg-revision; verify with Mark before locking.

### 🟡 WARNING (act this week)

- **Sally / Lily: confirm AUS 05052026 ship-out date.** Daniel/Remy WeChat. Sheet says arrival 6 May - reality is unknown.
- **Mark: confirm AUS 09052026 timeline.** B114 jars target was 25 Apr (~9 days ago). No update. Sheet now shows 21 May completion; need validation.
- **Avi PO for ACC-LAB.** 108d cover. Place by ~mid-May for 20,000 units (compliance-critical).
- **Care/Heal LCL bottle send sizing.** Daniel to spec quantity (recommend 11,000-16,000 finished Heal target post-fill) + LCL freight cost approval from Joel.
- **PO 9 B360 PACKUP Friday count.** Remy following up. 23-SKU variances pending (-200 each on 11 colour SKUs incl. Sincere top seller, plus 9,376 ACC-RE1-BOT under, 911 ACC-REM-500 under).
- **Mid-cycle check on LIQ-BAS-2 daily depletion.** 7d Shopify DSR jumped to 27.6 (vs 16.3/d 7d two weeks ago). If sustained, the bridge is even tighter.

### 🟢 MONITOR

- **GWP campaign deductions.** POW-CLE-193 already 38,235 at G3PL (massive cover) - 1,944/d at GWP rate would still take weeks. POW-SUN-SU015 at 1,706 is the constraint - 123/d × 14d = 1,722 = ~2 weeks cover. Watch.
- **Greg POS MODEL OP block doublecount cleanup** (above).
- **Container #5 (unnamed) raw goods PO timing.** This is the kit-Heal-in-kit successor. Daniel to confirm.
- **Sincere POW-SIN-254 cover post-PO 9 -200 variance** when Jake's count returns.

---

## LOCAL FILL FORECAST

### OP Heal — 22-04-2026 fill (in production, gated on payment)
- Current 9,390 → expected post-fill (assuming ~21 Jun arrival): 9,390 - (47 × 184.6 projected) = ~712 → +11,500 fill = **12,212 (66d at projected) / +5,527 + 11,500 = 17,027 (207d at actual 82.2/d)**.
- **Yield risk:** prior 25-02-2026 fill was 9,000 OL but yielded 7,570 (84%). Apply same yield to 11,500 → ~9,660 actual. Post-fill becomes 712 + 9,660 = 10,372 (56d projected) / 5,527 + 9,660 = 15,187 (185d actual).
- ACTION: Pay ND. Confirm fill quantity discipline with Peter.

### Care/Heal LCL bridge fill (proposed)
- Sizing options (D = arrival at G3PL):
  - **Lean (60d cover post-fill at projected):** ~11,000 units. LCL bottles ~3-4wk transit + 30d fill + 7d ship = D+~9-10wk from LCL despatch.
  - **Recommended (90d cover post-fill at projected):** ~16,500 units.
  - **Conservative (120d cover at projected):** ~22,000 units.
- ACTION: Daniel to choose sizing this week. Joel to approve LCL cost. Lily/Sally to coordinate Heal bottle send (likely from Sally's existing HEA-EMP stock OR pull from AUS 08072026 inbound 20,000 buffer).

### Next OP Remove 500ml fill (AUS 08072026 brings 5,000 each component)
- Current 7,787 stock; ~80d cover at sheet 98.8/d. Stocks out ~22 Jul (mid-AUS 08072026 arrival window 15 Jul).
- AUS 08072026 brings 5,000 ACC-RE5-BOT/LID/INN — components for next OP fill, not finished Remove 500ml.
- ACTION: Plan next OP fill placement ~early Jun for ~6,000-8,000 units fill.

---

## PO RECOMMENDATIONS

| Item | Stock | Cover | Recommendation | Place By |
|---|---:|---:|---|---|
| Avi PO (ACC-LAB) | 15,788 | 108d (3PL) | 20,000 units, Avi standard 10-21d | **~mid-May** |
| AUS 08072026 fill PO | - | - | Add ACC-LAB ~20k, ACC-THA ~15-20k. NO LIQ-HEA-5 (per Heal-late call). Cut COM/ULT to actual run-rate. Hold STA at pre-Easter ~32/d. | **6 May (2 days)** |
| Care/Heal LCL bottle send | - | - | Lean 11,000 or Recommended 16,500 unit fill target (post-OP fill cover). Bottles via LCL pull-forward from Sally OR AUS 08072026 buffer. | **Daniel scope this week** |
| Next OP Remove 500ml fill | 7,787 | 80d (sheet) | ~6,000-8,000 units. Components on AUS 08072026. | **Place ~early Jun** |
| LIQ-BAS-2 / LIQ-SEN-2 / LIQ-SEN-4 express bridge | as above | OOS - 14d | **Sally despatch existing 648 Base + 216 LO Base + 216 LO Glow ASAP via Lily express.** | **THIS WEEK** |

---

## CASCADING ARRIVAL PROJECTION

Target: 45-75d cover. Actual kit DSR: 79.5/d (sum 14d 3PL: 21.9 + 40.1 + 17.5).

| | NOW | After AUS 05052026 (assume +7d slip → ~13 May) | After AUS 09052026 (20 Jun) | After AUS 07062026 (21 Jun) | After AUS 08072026 (15 Jul) |
|---|---:|---:|---:|---:|---:|
| Days from today | 0 | +9 | +47 | +48 | +72 |
| KIT-STA-2 stock | 885 | 688 (no kit OL) | 688 - 38d×21.9 = -144 ⚠️ +2,016 = **1,872 (85d)** | +1,260 = 3,132 (143d) ⚠️ | +1,372 = 4,021 (184d) ⚠️ |
| KIT-COM-4 stock | 4,364 | 4,003 (no kit OL) | 2,479 +3,052 = 5,531 (138d) ⚠️ | +3,164 = 8,415 ⚠️ | +3,192 = 10,668 ⚠️ |
| KIT-ULT-6 stock | 2,636 | 2,478 (no kit OL) | 1,812 +1,036 = 2,848 (163d) ⚠️ | +1,244 = 3,943 ⚠️ | +1,428 = 5,043 ⚠️ |
| LIQ-HEA-5 | 9,390 | 8,651 | post-OP fill (assume ~21 Jun ~5,400) +11,500 OR +9,660 yield-adjusted = 15,060 (183d at actual / 82d at projected) | ditto | ditto |

**STA flag:** zero cover for **6 days** between projected stock-out (14 Jun at actual 21.9/d) and AUS 09052026 arrival (20 Jun). Bridge options: pull Complete kits as substitute (Joel 17 Apr precedent), or express STA via Sally if she has finished kit on hand.

---

## OVERSTOCK FLAGS (post-arrival cover > 100d, 45-75d target)

- **KIT-COM-4: post-09052026 = 138d (currently 109d at actual 40.1/d, model 101.4/d).** Persistent overstock pattern.
- **KIT-ULT-6: post-09052026 = 163d.** AUS 08072026 adds another 1,428.
- **LIQ-SEA-3: 185d cover today** at actual ~13/d. AUS 09052026 brings +2,808 → 400+ days. Cut from 09052026 if possible (kit-attached, hard).
- **POW-COR-481: 980d cover** at 0.5/d. 200 inbound on 08072026 unnecessary - cut.

---

## FOLLOW-UP ITEMS

### Immediate (today / tomorrow)
- [ ] **Joel: pay New Directions proforma** for 22-04-2026 ingredients.
- [ ] **Daniel: draft AUS 08072026 fill PO** with ACC-LAB ~20k, ACC-THA ~15-20k, NO finished Heal, kit mix at actual run-rate. Place 6 May.
- [ ] **Daniel/Lily WeChat Sally:** confirm AUS 05052026 ship date + express the 648 Base / 216 LO Base / 216 LO Glow.
- [ ] **Remy: chase Jake on PO 9 Friday count.**
- [ ] **Greg: flatten OP Heal/Remove 500ml block** in POS MODEL (remove 1,300 + 911 phantom inbound).

### By end of week
- [ ] **Daniel: scope Care/Heal LCL bridge fill** — qty (lean 11,000 or recommended 16,500), bottle source, LCL freight cost for Joel approval.
- [ ] **Mark: confirm AUS 09052026 21 May completion** is realistic.
- [ ] **Listing decision on LIQ-SEN-2** (mark OOS or accept) until inbound lands.

### Ongoing
- [ ] Place Avi ACC-LAB PO ~mid-May (20,000 units).
- [ ] Plan next OP Remove 500ml fill ~early Jun (6-8,000 units).
- [ ] Confirm Container #5 raw goods PO timing (CN-Heal-in-kit successor).
- [ ] Daniel/Jake: ShipHero name sync resolution (now 18 days stalled).
- [ ] Re-list Blue Moon (POW-BLU-ZGD22), verify Fire Collection listings (still flagged 21+ days).
