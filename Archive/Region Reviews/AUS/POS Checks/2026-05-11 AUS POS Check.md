# AUS POS Model Check — 11 May 2026

## DATA FRESHNESS

- **POS MODEL extracted:** 11 May 12:01 AEST (xlsx re-pulled fresh today). `UPDATED` cell not filled by Greg — assume today's paste.
- **3PL data last valid:** 11 May (today).
- **Shopify data through:** 10 May (+1 day lag, normal).
- **Growth factor:** 1.3x (147 base → 191.1 scaled).
- **14d kit actual:** 22.7 + 72.4 + 26.1 = **121.2/d (effective 0.82x)** — but trajectory is steepening (today's daily digest 158/d, 7d).

## MANUAL OVERRIDES (user-confirmed today)

| Field | Sheet | Override | Source |
|---|---|---|---|
| AUS 09052026 completion | 21 May / arrival 20 Jun | **Sally claim only, no email/WeChat paper trail.** Sally waiting on jars from Mark; Remy pushing for written confirmation. Treat 21 May as supplier claim, not locked — model a +7d slip scenario in cover math. | Slack 7 May Remy summary; user 11 May. |
| AUS 08072026 fill PO | Place date was 6 May | **Deliberate hold, place window 18-25 May.** Not overdue. | User-confirmed today. |
| LIQ-BAS-2 / LIQ-SEN-2 / LIQ-SEN-4 bridge | AUS 05052026 (sheet comp 6 May / arr 13 May) | **Sheet dates stale — container not shipped.** Sally finished express liquid bottles post-CN holiday (7 May); LO Base + Glow ready, Base awaiting Joel sample sign-off. | Slack 7 May. |
| Care/Heal LCL bridge concept | 4 May POS Check sized LCL options | **DROPPED — 11,500 OP Heal fill IS the local Care fill, not separate.** Next OP fill (~8,500) will be the follow-up cycle, also local. | User-confirmed today. |
| LIQ-HEA-5 phantom inbound | OP Heal/Remove 500ml block shows +1,300 inbound | **Fictitious** — 25-02-2026 PO 10 yield gap, not pending. Greg still has not flattened. Projected ON HAND overstated by 1,300. | Katrina 1 May / 4 May POS Check. |
| ACC-REM-500 phantom inbound | B360 PACKUP block shows +911 inbound | **Fictitious** — already booked at G3PL. Same flattening required. | 4 May POS Check. |
| Selling rate basis for 08072026 sizing | Was assumed -55% to -62% (W17-W18) | **Today's daily digest 158/d (-17%)** — recovery in progress, real in 3PL deductions (KIT-COM-4 dropped 780 units in 7 days, peak day 174). Sales Analysis to confirm sustainability. Treat 158/d as live, retain 1.3x projected for sizing buffer. | User-confirmed today. |

---

## STEP 0a — GMAIL / SLACK RECONCILE (events since last paste)

- **G3PL PO 12 Powder Room received in full** (Katrina email 4 May) — already in sheet.
- **GWP AUS-$85-GIF** orders firing (Katrina 3 May confirmation). POW-CLE-193 / POW-SUN-SU015 deduction spikes are this campaign — benign.
- **Daniel 5 May:** NDA ingredient dispatch ETA "within fortnight" (~19 May) — contingent on Joel paying proforma.
- **Daniel 7 May:** firm deadline 23 May for NDA payment.
- **Sally finished express bottles** (Remy 7 May) — LO Base + LO Glow ready, Base awaiting Joel sign-off.
- **Daniel 8 May:** kit offer changed to reduce double-consignment (Remove Bowl bundles) — explains uptick in ACC-REM-BOW consumption pre-change.
- **No Mark / Sally / Lily** email or WeChat in 21 days documenting AUS 09052026 21 May completion claim.

---

## STOCK POSITION

### KITS

| SKU | Stock | Projected DSR (1.3x) | Cover @ Projected | Actual DSR (3PL 14d) | Cover @ Actual |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 708 | 44.2 | **16d** | 22.7 | 31d |
| KIT-COM-4 | 3,584 | 101.4 | 35d | 72.4 | 49d |
| KIT-ULT-6 | 2,397 | 45.5 | 53d | 26.1 | 92d |

**STA is the kit-side risk.** 7-day stock decline: STA -177, COM -780 (peak day 174 deduction), ULT -239. KIT-COM-4 momentum stands out — 72.4/d 14d avg masks accelerating recent deductions.

**Selling-recovery scenario (if 158/d total kit holds):**
- STA mix ~24% → ~38/d → STA cover compresses to **19d**.
- COM mix ~60% → ~95/d → COM cover compresses to **38d**.
- ULT mix ~16% → ~25/d → ULT cover **96d**.

### LIQUIDS

| SKU (Name) | Stock | Model DSR | Cov @ Model | 3PL 14d | Cov @ 3PL | Inbound |
|---|---:|---:|---:|---:|---:|---|
| LIQ-BAS-2 (Base) | **0** | 53.3 | **OOS today** | 37.7 | OOS | +648 AUS 05052026 (NOT SHIPPED), +2,592 AUS 09052026 (20 Jun), +2,376 AUS 07062026 (12 Jul), +1,944 AUS 08072026 (5 Aug) |
| LIQ-SEN-2 (LO Base) | **0** | 9.1 | **OOS today** | 9.0 | OOS | +216 AUS 05052026 (NOT SHIPPED), +432 AUS 09052026 |
| LIQ-SEN-4 (LO Glow) | 56 | 7.8 | **7d** | 7.2 | 8d | +216 AUS 05052026 (NOT SHIPPED), +432 AUS 09052026 |
| LIQ-GLO-4 (Glow) | 606 | 26.0 | 23d | 15.9 | 38d | +26 B360 PACKUP (phantom?), +1,296 AUS 09052026, +1,512 AUS 07062026 |
| LIQ-SEA-3 (Seal) | 2,136 | 44.2 | 48d | 24.2 | 88d | +2,808 AUS 09052026 |
| LIQ-BON-1 (Bond) | 1,199 | 16.9 | 71d | 9.2 | 130d | +1,080 AUS 09052026 |
| LIQ-SOA-6 (Sensitive Glow) | 544 | 13.0 | 42d | 5.8 | 93d | +1,080 AUS 09052026 |
| LIQ-HEA-5 (Heal) | 8,165 | 184.6 | 44d | 125.3 | 65d | +1,300 OP fill (PHANTOM), +11,500 22-04-2026 OP fill (gated on NDA payment) |

### REMOVE / ACCESSORIES

| SKU | Stock | Model DSR | Cov @ Model | 3PL 14d | Cov @ 3PL | Inbound |
|---|---:|---:|---:|---:|---:|---|
| ACC-REM (120ml) | 6,865 | 33.8 | 203d | 42.2 | 163d | none |
| ACC-REM-500 | 7,106 | 98.8 | 72d | 68.0 | 104d | +911 B360 PACKUP (PHANTOM) |
| **ACC-REM-BOW** | **480** | 75.4 | **6d** | 53.8 | **9d** ⚠️ | +6,840 AUS 09052026 (20 Jun), +2,000 AUS 07062026, +2,640 AUS 08072026 |

### INSERTS / PACKAGING

| SKU | Stock | 14d 3PL avg | Cover | Benchmark | Inbound |
|---|---:|---:|---:|---:|---|
| ACC-LAB | 13,719 | 219.1 | **63d** | 735 | **NONE — Avi PO needed.** |
| ACC-THA | 28,109 | 219.1 | 128d | 735 | +30,800 AUS 09052026, +11,200 AUS 07062026. NOT in 08072026. |
| ACC-INS | 16,805 | 120.9 | 139d | 435 | +5,280 each in 09052026 / 07062026 / 08072026 |

### COLOURS WORTH FLAGGING

- **POW-CLE-193:** 334 / 266 deducted (10 / 11 May) at 9.5x / 7.6x benchmark — GWP firing, benign.
- **POW-SUN-SU015:** GWP component, low remaining stock — monitor.
- **POW-SIN-254 (Sincere):** stock check needed against PO 9 -200 variance (still pending Jake count).

---

## CHECK-IN PROGRESS

No active partial check-ins.
- **AUS Powder Room (24-03-2026)** — PO 12 received full at G3PL 4 May (Katrina confirmation).
- **B360 PACKUP** — Delivered (sheet says 7 May; PO 9 23-SKU variances still pending Jake's overdue count — 14 days past 1 May deadline).
- **OP Remove 500ml fill (24-03-2026)** — Delivered 24 Apr (closed).

---

## DOUBLE-COUNT DETECTION

POS MODEL still shows two phantom inbound lines from delivered local fills:

| Block | SKU | Phantom OL | Status |
|---|---|---:|---|
| OP Heal/Remove 500ml (Delivered 30 Mar) | LIQ-HEA-5 | +1,300 | **PHANTOM** — 25-02-2026 PO 10 yield gap, not pending stock |
| B360 PACKUP (Delivered 7 May) | ACC-REM-500 | +911 | **PHANTOM** — already booked at G3PL |
| B360 PACKUP | LIQ-GLO-4 | +26 | likely correct micro-variance, low impact |

**Combined overstatement of projected ON HAND: 2,211 units.** Heal cover overstated by ~7 days at projected DSR.

**ACTION:** Greg to flatten both blocks (carry-over from 4 May POS Check, still open).

---

## CONTAINER / ORDER STATUS

### AUS 05052026 (Isay Express bridge)
- **Sheet:** comp 6 May / arr 13 May, In Production.
- **Reality:** Not shipped yet per 4 May confirmation + 7 May Slack. Sally has finished express liquid bottles post-CN holiday. **LO Base + LO Glow ready; Base awaiting Joel sample sign-off.**
- Cargo: 648 LIQ-BAS-2 + 216 LIQ-SEN-2 + 216 LIQ-SEN-4 + Powder Room express colours.
- **ACTION:** Joel approve Base sample TODAY → Sally despatch via Lily air-freight this week. Every day of delay extends LIQ-BAS-2 / LIQ-SEN-2 OOS window.

### AUS 09052026 (40HQ standard)
- **Sheet:** comp 21 May / arr 20 Jun, In Production.
- **Reality:** 21 May completion is Sally-claim via WeChat being chased for written confirmation. **No email/WeChat trail in 21 days.**
- 40 days to arrival from today.
- Container brings the critical replenishment for: KIT-STA-2 (+2,016), KIT-COM-4 (+3,052), KIT-ULT-6 (+1,036), all liquids, ACC-REM-BOW (+6,840), ACC-THA (+30,800), ACC-INS (+5,280).
- **ACTION:** Remy to surface written confirmation of 21 May from Sally / Mark this week. Run +7d slip scenario as default until confirmed.

### AUS 07062026 (Birthday Sale, 1.4x growth assumption)
- **Sheet:** comp 12 Jun / arr 12 Jul, In Production. **Slipped from 22 May / 21 Jun (4 May position) — 27-day arrival slip.**
- 62 days to arrival. Birthday Sale arrival timing tightens.
- **ACTION:** Joel to confirm deposit status; Daniel to chase Lily-Sally ETA pressure.

### AUS 08072026 (next standard)
- **Sheet:** comp 6 Jul / arr 5 Aug. Status: not yet placed. **Place window 18-25 May (deliberate hold per user).**
- 86 days to arrival.
- 4 May POS Check criteria still apply, modulated by recovery signal:
  - Add ACC-LAB ~20,000
  - Add ACC-THA ~15-20,000
  - NO LIQ-HEA-5 in kit (per YDM 8-week ingredient lead from 1 May, container can't carry)
  - Kit mix: **revisit cuts.** If 158/d total holds, don't cut COM/ULT below 30/35d targets — sheet 3,192 COM / 1,428 ULT roughly aligns.

### Container #5 (unnamed)
- **Sheet:** comp 5 Aug / arr 4 Sep. Status null. **Slipped from 15 Jul / 14 Aug — 21-day slip.**
- 116 days to arrival.
- **Earliest plausible CN-Heal-in-kit container** (YDM 8-week ingredient timer from 1 May → ~26 Jun YDM-ready → fill cycle → ship → ~late Aug at best).
- **ACTION:** Daniel + Joel to confirm Container #5 raw goods PO timing; this is the kit-Heal-in-kit successor.

### B360 PACKUP (Delivered 7 May per sheet)
- 23-SKU variance count overdue **14 days** (Jake committed Fri 1 May).
- LIQ-BAS-2-QUARANTINED disposal certificate also outstanding.

---

## LOCAL FILL STATUS

### Outsource Packaging — Heal 11,500 (ref: 22-04-2026)
- **POS MODEL:** In Production, no Est. Completion / Est. Arrival.
- **Gmail (Daniel 5 May):** NDA ingredient dispatch ~19 May (within fortnight) — contingent on Joel paying proforma.
- **NDA payment deadline 23 May** (Daniel 7 May firm).
- **Lead time path from Joel payment day (D0):** D+5 ingredients ship → D+7 at Peter → +30d fill → +7d ship to G3PL.

| Pay date | Heal at G3PL ETA |
|---|---|
| Tue 13 May | ~30 Jun |
| Mon 19 May | ~6 Jul |
| Fri 23 May (deadline) | **~10 Jul** |
| Mon 26 May (slip) | ~13 Jul |

- **Yield risk:** prior 25-02-2026 fill 9,000 OL → 7,570 received (84% yield). Apply to 11,500 → ~9,660 actual.
- **ACTION:** Joel pays this week. Greg to add ETA to POS MODEL once paid.

### Next OP Heal fill (~8,500 units — Remy 7 May floated)
- Components: HEA-EMP/LID/BSH already at G3PL (per 4 May, 20,000+ each).
- Not yet placed. Trigger window: place ~mid-Jun for delivery ~late Jul → covers gap to Container #5 (4 Sep CN-Heal-in-kit).
- **ACTION:** Place fill PO mid-Jun targeting ~8,500 units; sizing confirmed by Heal cover math (below).

### Outsource Packaging — Remove 500ml (next cycle)
- ACC-RE5-BOT/LID/INN on AUS 08072026 (+5,000 each).
- Current Remove 500ml: 7,106, 104d cover at actual.
- **ACTION:** Plan next OP fill placement ~early Jul for ~6,000-8,000 units.

### Avi Printing — ACC-LAB
- Current 13,719 / 63d cover at actual 219/d.
- **ACTION:** Place 20,000-unit PO this week (Avi lead 10-21d → land ~1 Jun) to keep buffer ahead of 13 Jul projected OOS.

---

## STOCK-OUT FORECAST

### STOCKOUT NOW

| SKU | Stock | DSR | Status | Next Inbound | Gap |
|---|---:|---:|---|---|---:|
| **LIQ-BAS-2 (Base)** | 0 | 37.7 | **OOS today** | AUS 05052026 +648 (NOT SHIPPED) | indeterminate |
| **LIQ-SEN-2 (LO Base)** | 0 | 9.0 | **OOS today** | AUS 05052026 +216 (NOT SHIPPED) | indeterminate |

### IMMINENT (<14 days)

| SKU | Stock | DSR | Stocks Out | Next Inbound | Gap |
|---|---:|---:|---|---|---:|
| **ACC-REM-BOW** | 480 | 53.8 actual | **~20 May (9d)** | AUS 09052026 (+6,840, 20 Jun) | **-31d OOS** |
| **LIQ-SEN-4 (LO Glow)** | 56 | 7.2 actual | ~19 May (8d) | AUS 05052026 +216 (NOT SHIPPED) → AUS 09052026 +432 | bridge dependent |

### TIGHT (<30 days at actual)

| SKU | Stock | DSR | Stocks Out | Next Inbound | Gap |
|---|---:|---:|---|---|---:|
| KIT-STA-2 | 708 | 22.7 / ~38 if recovery holds | 12 Jun / 25 May | AUS 09052026 (20 Jun) | -8d at actual / **-26d if 158/d total kit holds** |
| LIQ-GLO-4 | 606 | 15.9 / could lift | 11 Jun | AUS 09052026 (20 Jun) | -9d at actual |

### TIGHT (30-60d at actual)

| SKU | Stock | DSR | Cover | Next Inbound | Status |
|---|---:|---:|---:|---|---|
| **ACC-LAB** | 13,719 | 219.1 | 63d (OOS ~13 Jul) | NONE — Avi PO needed | Trigger window NOW |
| KIT-COM-4 | 3,584 | 72.4 / ~95 if recovery holds | 49d / **38d** | AUS 09052026 (20 Jun) | Tightening fast |
| LIQ-HEA-5 | 8,165 | 125.3 actual / 184.6 model | 65d / 44d | 22-04-2026 OP fill (~10 Jul if NDA pays 23 May) | Gated on Joel payment |

### SAFE

KIT-ULT-6, LIQ-SEA-3, LIQ-BON-1, LIQ-SOA-6, ACC-REM, ACC-REM-500, ACC-INS, ACC-THA, most colours.

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (act today)

1. **LIQ-BAS-2 + LIQ-SEN-2 OOS now.** Listing decision required. AUS 05052026 has 648 + 216 inbound but Sally hasn't despatched. **Joel: approve Low Odour Base sample → Sally air-freight via Lily this week.**
2. **ACC-REM-BOW 9d cover.** OOS ~20 May. Container 31 days late (20 Jun). **Express bridge: 1,000-2,000 units from Sally via Lily, OR cross-region from CA Swift overstock (CA had 439d cover per 4 May).** Daniel + Joel decision today.
3. **Joel: pay NDA 22-04-2026 proforma.** Deadline 23 May (12 days). Every day past extends Heal G3PL ETA by 1 day. At deadline payment, Heal lands ~10 Jul — already 14 days after AUS 08072026's previous projected arrival, now aligned with new 5 Aug AUS 08072026 arrival.
4. **Avi ACC-LAB PO this week** (20,000 units, 10-21d lead → land ~1 Jun) to keep buffer ahead of 13 Jul projected OOS.
5. **Greg: clean POS MODEL** — flatten OP Heal/Remove 500ml (+1,300 LIQ-HEA-5) and B360 PACKUP (+911 ACC-REM-500) phantom inbound. Update AUS 05052026 to "not despatched" or remove arrival date.

### 🟡 WARNING (act this week)

1. **Remy: get written confirmation of AUS 09052026 21 May completion from Sally / Mark.** Verbal only currently. Model +7d slip until confirmed — STA gap widens to ~13d at actual / ~25d if recovery holds.
2. **Daniel: AUS 08072026 fill PO scope** (place 18-25 May per user). Add ACC-LAB ~20,000, ACC-THA ~15-20,000, NO LIQ-HEA-5 in kit. Kit mix: reconsider COM/ULT cuts given selling recovery signal.
3. **Remy: chase Jake on PO 9 B360 PACKUP Friday count** (14 days past deadline). Escalate via channel + email.
4. **Remy: pull Jake's "Heal history" email** Daniel referenced 3 May — surface and resolve the 1,300pcs missing Heal.
5. **LIQ-SEN-4** decision: 56 units, 8d cover. Mark OOS or accept gap to AUS 05052026.
6. **Daniel: confirm with Sally next OP Heal fill (~8,500 units)** mid-Jun placement to cover gap to Container #5 (4 Sep).

### 🟢 MONITOR

1. **Selling-recovery trajectory.** If 158/d total kit holds through this week, STA gap math compresses to ~26d OOS vs 09052026 arrival. Sales Analysis will validate sustainability.
2. **GWP campaign deductions** (POW-CLE-193 / POW-SUN-SU015) — still benign, don't reflag.
3. **ShipHero name-sync issue** (25 days stalled, Daniel/Jake decision needed).
4. **Listings: Blue Moon relist, Fire Collection verification, Goddess** — no movement in 4+ weeks.
5. **Container #5 raw goods PO timing** — kit-Heal-in-kit successor, needs Daniel + Joel confirmation.

---

## CASCADING ARRIVAL PROJECTION

Target: 45-75d cover. Using actual kit DSR 121.2/d (14d 3PL) as baseline scenario.

| | NOW | After AUS 05052026 (assume +14d slip → 25 May, ~Sally express) | After AUS 09052026 (20 Jun) | After AUS 07062026 (12 Jul) | After AUS 08072026 (5 Aug) |
|---|---:|---:|---:|---:|---:|
| Days from today | 0 | +14 | +40 | +62 | +86 |
| **KIT-STA-2** | 708 (31d) | 708 - 14×22.7 = **390** | 390 - 26×22.7 = **-200 OOS** → +2,016 = **1,816** (80d) | -198, +1,260 = 2,878 (127d) | -499, +1,372 = 3,751 (165d) |
| **KIT-COM-4** | 3,584 (49d) | 3,584 - 14×72.4 = **2,570** | 2,570 - 26×72.4 = **688** (10d) → +3,052 = **3,740** (52d) | -1,591, +3,164 = 5,313 (73d) | -1,679, +3,192 = 6,826 (94d) |
| **KIT-ULT-6** | 2,397 (92d) | 2,397 - 14×26.1 = 2,032 | 2,032 - 26×26.1 = 1,353 (52d) → +1,036 = 2,389 (92d) | -574, +1,244 = 3,059 (117d) ⚠️ | -601, +1,428 = 3,886 (149d) ⚠️ |
| **ACC-REM-BOW** | 480 (9d) | -753, **already OOS** | OOS until 20 Jun. -1,400+ in gap. +6,840 = ~6,000+ (110d) ⚠️ | +2,000 = ~8,000 ⚠️ | +2,640 ⚠️ |
| **LIQ-HEA-5** | 8,165 (65d) | -1,754 = 6,411 (51d) | -3,258 = 3,153 (25d) | Post 22-04-2026 OP fill (~10 Jul) +11,500 yield-adj ~9,660: see below | |
| **ACC-LAB** | 13,719 (63d) | -3,067 = 10,652 (49d) | -5,696 = 4,956 (23d) Avi PO ~+20,000 by ~1 Jun = 24,956 (114d) | -7,769 = 17,187 (78d) | -7,769 = ~9,400 (43d) Avi PO #2 needed |

**STA red flag:** at 14d 3PL rate 22.7/d, current 708 stocks out **31 days from now (~11 Jun)**, vs AUS 09052026 arrival in 40 days. **9-day OOS gap.** If 158/d total kit holds and STA mix ~24% → 38/d → STA stocks out in 19 days (~30 May), **22-day OOS gap.** Bridge options:
- **Sally express via Lily** (precedent: 4 May call for express liquid bottles).
- **Pull Complete kits as substitute** (Joel 17 Apr precedent; STA→COM upgrade).
- **Don't cut STA share on AUS 08072026** — current 1,372 OL is right-sized given recovery.

**ACC-REM-BOW already in OOS trajectory.** No internal AUS bridge until 20 Jun. **CA Swift overstock cross-region (~439d cover) is the cleanest bridge** — needs Daniel + Joel call.

---

## HEAL COVER SCENARIO (anchored on NDA payment 23 May)

| Stage | Date | Heal Stock | Cover | Notes |
|---|---|---:|---:|---|
| Now | 11 May | 8,165 | 44d @ 184.6/d projected | 65d @ 125.3/d actual |
| Pre-NDA-pay | 23 May | 8,165 - 12×184.6 = **5,950** | 32d projected | |
| OP Heal lands | ~10 Jul | 5,950 - 48×184.6 = **-2,910 OOS by ~8 Jul!** at projected | | At actual 125.3/d: -65 OOS by ~9 Jul. **Either rate: ~2 days OOS pre-fill.** |
| Post 22-04-2026 OP fill (yield-adj) | ~10 Jul | +9,660 = **9,660** | 52d projected / 77d actual | Yield 84% on 11,500 |
| Pre next OP fill | ~mid-Aug at projected / ~early Sep at actual | depends on next fill placement | | Next OP fill placement ~mid-Jun for ~late Jul delivery |
| Container #5 CN-Heal-in-kit | ~4 Sep | TBC | | Earliest plausible date contingent on YDM ingredients arriving end-Jun |

**CRITICAL FLAG:** at projected DSR, current Heal stocks out ~8 Jul — 2 days before 22-04-2026 OP fill lands (at 23 May payment). At actual DSR, OOS ~9 Jul — same window. **Either way the gap is real but small (~2 days).**

**Mitigation:** either (a) Joel pays NDA proforma **mid-week** (13-14 May) rather than at deadline to pull Heal lands forward to ~30 Jun, closing the 2-day gap; or (b) accept the brief gap if Daniel/Lily confirm Sally has any finished Heal in CN to express bridge.

**Next OP fill placement timing:** if 11,500 lands ~10 Jul and we want continuous cover to Container #5 (4 Sep, 56 days later):
- Heal demand 56 days × 184.6/d projected = 10,338 units needed
- Heal demand 56 days × 125.3/d actual = 7,017 units needed
- Recommended sizing: **8,500-10,500 units** (Remy's 7 May floated 8,500 aligns with actual rate).
- Place mid-Jun for delivery ~late Jul → 11 days OOS gap mid-Aug at projected rate. **Either size to 10,500 OR pull placement to early Jun.**

---

## CONTAINER GAP ANALYSIS

### AUS 08072026 — CRITICAL GAPS (place 18-25 May)
- **ACC-LAB: 0 units.** OOS projected ~13 Jul, container arrives 5 Aug → **23-day gap**. Need Avi PO this week (closes the gap).
- **ACC-THA: 0 units.** Current 128d cover; post-AUS 09052026 +30,800 / post-AUS 07062026 +11,200 = will run ~80-120d depending on consumption. **Add 15-20,000 to 08072026** to maintain cover post-5 Aug.
- **LIQ-HEA-5: 0 units in kit.** Confirmed not in this container (YDM-late). Heal bridge via 22-04-2026 OP fill + next OP fill (~8,500).
- **Kit mix at recovered rate:** if 158/d holds → STA mix 38/d × 86 days = 3,268 expected demand vs 2,628 inbound across 09052026 + 07062026; sheet 08072026 STA OL = 1,372. **Hold STA, don't cut.**

### Container #5 — CN-Heal-in-kit successor
- Sheet: 5 Aug completion / 4 Sep arrival. Status null.
- **Earliest plausible CN-Heal-in-kit container.** YDM ingredient timer (~26 Jun YDM-ready) + ~30d fill + shipping = late Aug minimum. 4 Sep arrival realistic.
- **ACTION:** Daniel + Joel to confirm raw goods PO timing and whether kit-Heal is actually loaded.

---

## OVERSTOCK FLAGS (post-arrival cover > 100d)

- **KIT-ULT-6:** 117d post-AUS 07062026, 149d post-AUS 08072026 at actual 26.1/d. If recovery holds at ~25/d ULT, still 150d post-AUS 08072026. **Consider trimming ULT on 08072026 fill PO by 30-40%.**
- **LIQ-SEA-3:** 88d cover today at 24.2/d actual. +2,808 on AUS 09052026 → **~200d post-arrival.** Persistent overstock — flag but kit-attached so hard to cut.
- **LIQ-BON-1:** 130d cover today. +1,080 on AUS 09052026 → 240d+. **Cut from 09052026 if possible** (low priority).
- **LIQ-SOA-6:** 93d cover today. +1,080 on AUS 09052026. Will exceed 200d. **Cut.**
- **ACC-INS:** 139d cover at actual 121/d. +5,280 each on 09052026 / 07062026 / 08072026 — will accumulate to 300d+. **Reduce 08072026 OL.**

---

## PACKAGING & INSERTS BENCHMARKS (3PL deductions last 14d)

| SKU | 14d avg | Benchmark | Anomaly days |
|---|---:|---:|---:|
| STO-BUB-BAG-L | ~219/d | 435 | 0 (but yesterday's 494 → benign at 1.1x) |
| ACC-INS | 120.9 | 435 | 0 |
| ACC-LAB | 219.1 | 735 | 0 |
| ACC-THA | 219.1 | 735 | 0 |

No anomalies in last 14 days beyond GWP campaign on colours.

---

## PO RECOMMENDATIONS

| Item | Stock | Cover | Recommendation | Place By |
|---|---:|---:|---|---|
| Avi PO (ACC-LAB) | 13,719 | 63d actual | 20,000 units, Avi standard 10-21d | **This week (target land ~1 Jun)** |
| AUS 08072026 fill PO | - | - | Add ACC-LAB ~20k, ACC-THA ~15-20k. NO LIQ-HEA-5. Hold STA, modest COM trim (3,000-3,200 vs sheet 3,192 OK), cut ULT 30-40% to ~1,000. | **18-25 May (deliberate hold)** |
| Next OP Heal fill | 8,165 + 11,500 fill | gap mid-Aug | ~8,500-10,500 units (size for 56d cover to Container #5) | **mid-Jun for ~late Jul delivery** |
| Next OP Remove 500ml fill | 7,106 | 104d actual | ~6,000-8,000 units. Components on AUS 08072026 (5 Aug). | **Place ~early Jul** |
| Express bridge — LIQ-BAS-2 / LIQ-SEN-2 / LIQ-SEN-4 | OOS / 8d | OOS | **Joel: approve Base sample. Sally despatch 648 + 216 + 216 via Lily air-freight this week.** | **This week** |
| Express bridge — ACC-REM-BOW | 480 | 9d | **Cross-region from CA Swift overstock (1,000-2,000) OR Sally express.** | **This week** |

---

## FOLLOW-UP ITEMS

### Immediate (today / tomorrow)
- [ ] **Joel: pay New Directions proforma** by mid-week to pull Heal G3PL ETA forward to ~30 Jun (closes the projected 2-day OOS gap).
- [ ] **Joel: approve LO Base sample** → Sally despatch express liquids via Lily.
- [ ] **Daniel/Joel: ACC-REM-BOW bridge decision** — cross-region from CA OR Sally express.
- [ ] **Remy: write to Sally + Mark** for written confirmation of AUS 09052026 21 May completion.
- [ ] **Remy: place Avi PO** for ACC-LAB ~20,000 units.
- [ ] **Greg: clean POS MODEL** — flatten OP Heal/Remove 500ml + B360 PACKUP phantom inbound.

### By end of week
- [ ] **Remy: chase Jake** on PO 9 Friday count + Heal history email (14+ days overdue).
- [ ] **Daniel: AUS 08072026 fill PO draft** with reviewed kit-mix (hold STA, trim ULT, no kit-Heal).
- [ ] **Daniel: confirm next OP Heal fill (~10,500 units) for mid-Jun placement.**
- [ ] **Listing call** on LIQ-SEN-2 (mark OOS or accept gap).

### Ongoing
- [ ] **Daniel + Joel: confirm Container #5 raw goods PO timing** (CN-Heal-in-kit successor).
- [ ] **Daniel/Jake: ShipHero name sync resolution** (25 days stalled).
- [ ] **Listings: Blue Moon relist, Fire Collection verification, Goddess** (4+ weeks open).
- [ ] **Joel: AUS 07062026 deposit status confirmation** post-27-day slip.
- [ ] **Plan next OP Remove 500ml fill** for early Jul placement (6-8,000 units).
