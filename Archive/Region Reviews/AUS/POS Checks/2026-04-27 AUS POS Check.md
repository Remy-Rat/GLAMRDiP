# AUS POS Model Check — 27 Apr 2026

## DATA FRESHNESS

- **POS MODEL extracted:** 27 Apr 14:30 AEST (xlsx re-pulled fresh). Data dated 27 Apr.
- **3PL data last valid:** 27 Apr (today).
- **Shopify data through:** 26 Apr (+1 day lag, normal).
- **Growth factor:** 1.3x (base 147 kits/d → scaled 191.1/d).

## MANUAL OVERRIDES

Applied to all downstream calculations - the POS MODEL is already partially current but does not reflect these:

| Field | Sheet | Override | Source |
|---|---|---|---|
| AUS 09052026 Est. Completion | 30 Apr | **5 May** | Mark Slack 27 Apr (60k B114 jars completing 25 Apr, +10d Sally fill) |
| AUS 09052026 Est. Arrival | 30 May | **5 Jun** | Slip cascades from completion |
| ACC-REM-500 actual deduction rate | sheet 98.8/d | **no override** - use sheet 98.8/d (~82d cover) | User confirmed 27 Apr: "whatever is in the sheet now is truth, covered for ~82 days". Earlier 168/d figure no longer applies. |
| LIQ-HEA-5 future fills | OP local fill recurring | **CN-in-kit from AUS 08072026 onwards** (no further AUS local Heal fills) | User confirmed 27 Apr |
| 22-04-2026 OP Heal fill ETA | None set in sheet | **~13 Jun arrival** (assuming ~7 May ingredients arrive + 30d fill + 7d ship) | Inferred; depends on Chantelle reply |
| ACC-LAB on hand (post Avi PO 11) | sheet 16,787 | **same** - sheet caught up | 18,344 baseline 16 Apr - 11 days × 159.8/d ≈ 16,787 today; sheet now current |

---

## STOCK POSITION

### KITS

| SKU | Stock | Projected DSR (1.3x) | Cover @ Projected | Actual DSR (3PL 14d) | Cover @ Actual |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 1,026 | 44.2 | **23d** | 26.5 | 39d |
| KIT-COM-4 | 4,598 | 101.4 | 45d | 51.3 | 90d |
| KIT-ULT-6 | 2,762 | 45.5 | 61d | 19.2 | 144d |

Starter Kit is the kit pinch-point. AUS 09052026 (now arriving ~5 Jun) brings 2,016 STA. Stocks out ~5 Jun at 3PL rate - **margin = 0 days** vs revised arrival.

### LIQUIDS

| SKU (Name) | Stock | Model DSR | Cov @ Model | 3PL 14d DSR | Cov @ 3PL | Inbound |
|---|---:|---:|---:|---:|---:|---|
| LIQ-BAS-2 (Base) | 490 | 53.3 | **9d** | 24.5 | 20d | +648 AUS 05052026 (arr 6 May), +2,592 AUS 09052026 (5 Jun) |
| LIQ-SEN-2 (LO Base) | 63 | 9.1 | **7d** | 5.5 | 11d | +216 AUS 05052026 (6 May), +432 09052026 (5 Jun) |
| LIQ-GLO-4 (Glow) | 828 | 26.0 | 32d | 9.5 | 87d | +1,296 09052026 (5 Jun), +1,512 07062026 (15 Jun) |
| LIQ-SEN-4 (LO Glow) | 157 | 7.8 | 20d | 4.0 | 39d | +216 AUS 05052026 (6 May), +432 09052026 (5 Jun) |
| LIQ-SEA-3 (Seal) | 2,475 | 44.2 | 56d | 13.2 | 187d | +2,808 09052026 (5 Jun) |
| LIQ-HEA-5 (Heal) | 9,919 | 184.6 | 54d | 98.8 | 100d | +11,500 OP fill (~13 Jun pending New Directions) |
| ACC-REM-500 (Remove 500ml) | 8,058 | 98.8 | **82d** | 46.8 (post-fill, low confidence) | n/a use model | already-arrived B360 |
| ACC-REM-BOW (Remove Bowl) | 1,233 | 75.4 | 16d | 34.2 | 36d | +6,840 09052026 (5 Jun) |

### INSERTS / PACKAGING

| SKU | Stock | 3PL 14d DSR | Cover @ 3PL | Inbound |
|---|---:|---:|---:|---|
| ACC-LAB | 16,787 | 159.8 | 105d | **NONE** - no Avi PO in pipeline |
| ACC-THA | 31,177 | 162.4 | 192d | +30,800 09052026, +11,200 07062026 |
| ACC-INS | 18,498 | 96.8 | 191d | +5,280 each on 09052026 / 07062026 / 08072026 |

### COLOURS WITH < 30D MODEL COVER

| SKU | Stock | Model DSR | Cov | Inbound |
|---|---:|---:|---:|---|
| POW-BOR-355 | 105 | 6.5 | 16d | +600 AUS 08072026 (15 Jul) |
| POW-HOT-568 | 111 | 6.5 | 17d | +600 AUS 08072026 |
| POW-RED-165 | 136 | 6.5 | 21d | +600 AUS 08072026 |
| POW-SPI-144 | 143 | 6.5 | 22d | +600 AUS 08072026 |
| POW-GAR-656 | 174 | 6.5 | 27d | +600 AUS 08072026 |

5 colours stocking out before AUS 08072026 (15 Jul arrival). All have inbound on that container - check whether AUS 05052026 (29 Apr completion / 6 May arrival) is the express colours fill that brings additional units of these. POS MODEL didn't show OL for these on 05052026.

---

## CHECK-IN PROGRESS

No active partial check-ins. B360 PACKUP delivered 16 Apr. OP Heal/Remove 500ml shown Delivered. PO 11 (Avi labels) delivered 16 Apr. Skipping ShipHero CSV reconciliation (not provided, AUS 3GPL tab is the live position).

---

## DOUBLE-COUNT DETECTION

OP Heal/Remove 500ml block is marked Delivered but POS MODEL still shows LIQ-HEA-5 +1,300 inbound and ACC-REM-500 +911 inbound under that block. **If the on-hand count already includes those units, projected ON HAND is overstated by 1,300 + 911 = 2,211 units.**

→ **Action: confirm with Greg whether those are still pending or already in 9,919 Heal / 8,058 Remove 500ml on-hand.** I've assumed they're already-arrived (matches the Delivered status) and not added them to cover calcs.

B360 PACKUP block (Delivered 16 Apr) - same logic. LIQ-GLO-4 +26, ACC-REM-500 +911. Treating as already in current stock counts.

---

## CONTAINER / ORDER STATUS

### AUS 05052026 (Express colours + small liquid bridge)
- POS MODEL: In Production, Est. Completion 29 Apr, Est. Arrival 6 May
- Slack: Daniel 22 Apr "small express order to push to fill asap and send"
- Reality (user-confirmed 27 Apr): **colours won't be at G3PL on 29 Apr** (longer transit); **liquids tentatively ~6 May** at G3PL - sheet date is roughly correct.
- Contains liquid bridge: LIQ-BAS-2 +648, LIQ-SEN-2 +216 (LO Base), LIQ-SEN-4 +216 (LO Glow). Plus colours.
- ACTION: Confirm exact G3PL date with Lily as it lands.

### Separate Base / LO Base / LO Glow express bridge order (NOT in POS MODEL)
- **Placed** (user-confirmed 27 Apr); payment status TBC, just happened.
- Estimated: completion ~30 Apr, then express ship (3-5 days transit) → G3PL ~3-5 May.
- ACTION: Greg to add to POS MODEL as separate Express Shipment block. Without it on the sheet, projected cover for Base/LOB/LOG is understated by an extra few hundred units of each.

### 22-04-2026 | Local Filling PO | Outsource Packaging (Heal 11,500)
- POS MODEL: In Production, no Est. Completion / Est. Arrival.
- Gmail: Peter replied 27 Apr - filling scheduled, awaiting raw material ETA from New Directions.
- Reality: blocked behind Chantelle (New Directions silent 4 days). Estimated ~13 Jun G3PL arrival assuming ~7 May ingredients + 30d fill + 7d ship.
- ACTION: Greg to add ETA once Chantelle confirms ingredients dispatch.

### B360 PACKUP (Delivered 16 Apr)
- Status complete. Confirm POS MODEL Express block reflects "Delivered" and stops contributing to projected ON HAND.

### AUS 09052026 (40HQ standard container)
- POS MODEL: In Production, Est. Completion 30 Apr, Est. Arrival 30 May.
- Reality: **completion ~5 May, arrival ~5 Jun** (Mark 27 Apr - B114 jars completing 25 Apr).
- 6-day slip cascades from jars to completion to arrival.
- ACTION: Greg to update POS MODEL Est. dates.

### AUS 07062026 (Birthday Sale)
- POS MODEL: In Production, Est. Completion 16 May, Est. Arrival 15 Jun. Deposit paid (user-confirmed).
- Growth factor for this container reportedly 1.4x - verify in shipment block. Use scaled DSRs for the spike window.

### AUS 08072026 (next standard, 15 Jul arrival)
- POS MODEL: status not set in sheet. Fill PO place date 29 Apr (2 days).
- **Heal must be CN-filled in kit on this container** (user-confirmed). Update spec before fill PO lodges.
- ACC-LAB and ACC-THA quantities to review (no ACC-LAB visible in inbound dict; ACC-THA has 0 here vs 11,200 in 07062026).

---

## LOCAL FILL STATUS

### Outsource Packaging - Heal 11,500 (ref: 22-04-2026)
- POS MODEL: In Production, no dates.
- Ingredients PO 22-04-2026 sent to Chantelle (New Directions) on 23 Apr by Joel - **no reply 4 days**.
- Peter (27 Apr): "Thanks for the new PO for Heal. I'll schedule the filling, please update on the raw material arrival." - filling scheduled, gated behind Chantelle.
- Lead time path: Chantelle confirms → ingredients ship + arrive (~5-10d) → Peter fills (~30d) → ship to G3PL (~7d) = **~50d from today if Chantelle replies tomorrow**.
- ACTION: **Chase Chantelle today** - phone follow-up if email silent. Drives the entire Heal landing date.

### Outsource Packaging - Remove 500ml (ref: 24-03-2026)
- POS MODEL: shows OP Heal/Remove 500ml as Delivered with 1,300 Heal + 911 Remove 500ml.
- Peter docket dispatched 22 Apr per email; should be at G3PL by now.
- **This was the last AUS Heal local fill before the 22-04-2026 PO.** Remove 500ml fill is OP's standalone product going forward unless replaced.

### No further AUS Heal local fills planned post-22-04-2026
- Heal moves to CN-in-kit from AUS 08072026 onwards. The 11,500 OP fill is the bridge.

---

## STOCK-OUT FORECAST

### STOCKOUT BEFORE ARRIVAL (gap < 0)

| SKU | Stock | DSR (rate) | Stocks Out | Next Inbound | Arrives | Gap |
|---|---:|---:|---|---|---|---:|
| LIQ-SEN-2 (LO Base) | 63 | 9.1 model / 5.5 actual | 4 May (model) / 8 May (actual) | AUS 05052026 +216 | ~3-6 May | -1d to +2d |
| LIQ-BAS-2 (Base) | 490 | 53.3 model / 24.5 actual | 6 May (model) / 17 May (actual) | AUS 05052026 +648 | ~3-6 May | -3d to +0d at model; +11d at actual |
| KIT-STA-2 (Starter) | 1,026 | 44.2 / 26.5 | 21 May (model) / 5 Jun (actual) | AUS 09052026 +2,016 | **5 Jun** (slipped) | -15d at model / **0d at actual** |

### TIGHT (gap 0-7d)

| SKU | Stock | DSR | Stocks Out | Next Inbound | Arrives | Gap |
|---|---:|---:|---|---|---|---:|
| LIQ-SEN-4 (LO Glow) | 157 | 7.8 / 4.0 | 17 May / 9 Jun | AUS 05052026 +216 | ~3-6 May | safe at actual; +11d at model |
| ACC-REM-BOW | 1,233 | 75.4 / 34.2 | 13 May / 2 Jun | AUS 09052026 +6,840 | 5 Jun (slipped) | **-23d at model** / +3d at actual |

### NOTHING ON ORDER

| SKU | Stock | DSR | Stocks Out | Deadline to Act |
|---|---:|---:|---|---|
| ACC-LAB | 16,787 | 159.8 (3PL) | ~10 Aug (105d) | Place Avi PO ~mid-May for 20,000 (10-21d Avi lead) |

### SAFE

Most kits, all liquids except those above, all packaging ACC-INS / ACC-THA, vast majority of colours. ~30+ days clear of any container.

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (act today)

- **Chase Chantelle (New Directions) - 22-04-2026 ingredients PO.** Silent 4 days. Every day = 1 day Heal landing slip. Phone if email silent by EOD.
- **LO Base (LIQ-SEN-2) at 7d cover.** Will hit zero ~4 May; AUS 05052026 lands ~6 May. **2-day OOS gap likely.** The newly-placed Base/LOB/LOG bridge express (~3-5 May at G3PL) should close it if it lands first - monitor.
- **Greg: update POS MODEL** - AUS 09052026 to 5 May completion / 5 Jun arrival; add 22-04-2026 OP fill ETA once Chantelle confirms; add separate Base/LOB/LOG bridge express PO; flip OP Heal/Remove 500ml + B360 PACKUP from "still inbound" to fully delivered (avoid double-count).

### 🟡 WARNING (act this week)

- **Avi PO for ACC-LAB.** 105d cover at 3PL rate (vs 47d sheet). Stocks out ~10 Aug. **Place ~mid-May for 20,000 units** (10-21d lead). Not on any CN container.
- **AUS 08072026 fill PO place date is 29 Apr (2 days).** Daniel needs to draft kit-mix revision: cut COM/ULT to 0.86x actual, bump STA, add ACC-LAB (~20,000) + ACC-THA top-up, and **switch Heal to CN-in-kit** (no LIQ-HEA-5 standalone OL).
- **KIT-STA-2 zero margin** to AUS 09052026 arrival at 3PL rate (39d cover, 39 days to 5 Jun). Any further slip on jars or fill = stockout. Bridge options: send next express batch or pull Complete kits per Joel's 17 Apr fallback.
- **ACC-REM-BOW at 36d cover** (3PL rate). Stocks out ~2 Jun, AUS 09052026 lands 5 Jun. 3-day gap. Only 1,233 on hand.
- **ACC-REM-500 next fill direction.** No standalone OP Remove 500ml fill in pipeline post-24-03-2026. **Sheet shows 82d cover at 98.8/d - safe through ~18 Jul** (mid-AUS 08072026 arrival window). Confirm AUS 08072026 OL contains adequate ACC-REM-500 OR plan next OP Remove fill ~early Jun.
- **Chase Katrina** on PO 10 Heal recount + B360 transfer discrepancies + ShipHero name sync (11 days silent across all three).

### 🟢 MONITOR

- B114 jars completing ~25 Apr (Mark). Confirm via Lily WeChat once finished; any further slip cascades to AUS 09052026.
- 5 colours under 30d cover - all on AUS 08072026. If 08072026 slips, these flip to express territory.
- POS MODEL OP Heal/Remove 500ml block - confirm with Greg the inbound numbers aren't double-counted into on-hand.
- Growth factor health: 7d kit selling 86.4/d, 14d 87.4/d, 30d 107.7/d. **-54% vs scaled** (191.1), **-41% vs base** (147). Sustained 9-10 weeks. Don't lower; flag for 08072026 / future container quantity review.

---

## LOCAL FILL FORECAST

### Outsource Packaging - Heal (LIQ-HEA-5) - 184.6/d projected, 98.8/d 3PL
- Current: 9,919 (54d projected / 100d 3PL).
- Fill in pipeline: +11,500, ETA ~13 Jun (gated on Chantelle reply).
- At 13 Jun: stock = 9,919 + 11,500 - (47d × 184.6) = ~12,743 → **69d projected cover / 129d at 3PL**.
- **No further OP Heal fills planned** - AUS 08072026 onwards Heal is CN-in-kit.
- AUS 08072026 arrives 15 Jul, brings Heal-in-kit. From 13 Jun to 15 Jul = 32d. At projected rate, 12,743 - 32×184.6 = 6,837 = 37d remaining cover when 08072026 lands. **Tight; if 08072026 slips, OOS gap.**
- ACTION: 08072026 fill PO must include explicit Heal-in-kit qty when Daniel drafts 29 Apr.

### Outsource Packaging - Remove 500ml (ACC-REM-500) - 98.8/d model / 168/d 3PL override
- Current: 8,058. Last fill (24-03-2026) delivered.
- At sheet 98.8/d: **82d cover → out ~18 Jul** (per sheet, user-confirmed).
- AUS 08072026 lands 15 Jul - close timing. Verify AUS 08072026 OL contains ACC-REM-500 (didn't show in extracted inbound dict).
- ACTION: confirm AUS 08072026 includes ACC-REM-500 top-up; otherwise plan next OP fill for ~early Jun placement.

---

## PO RECOMMENDATIONS

| Item | Stock | Cover | Recommendation | Place By |
|---|---:|---:|---|---|
| ACC-LAB (Avi local print) | 16,787 | 105d (3PL) | 20,000 units, Avi standard lead 10-21d | **~mid-May** to maintain >50d cover through 08072026 lead |
| AUS 08072026 fill PO | - | - | Cut COM/ULT to 0.86x actual; bump STA; **add Heal-in-kit per kit qty**; add ACC-LAB ~20k, ACC-THA top-up | **29 Apr (2 days)** |
| Next OP Remove 500ml fill | 8,058 | 82d (sheet, user-confirmed) | Verify AUS 08072026 OL has ACC-REM-500; otherwise plan OP fill | Decide ~early Jun |

---

## CASCADING ARRIVAL PROJECTION

Target cover: 45-75 days. Actual kit DSR (3PL avg): **97/d** (sum STA 26.5 + COM 51.3 + ULT 19.2).

| | NOW | After AUS 05052026 (~6 May) | After Bridge (Base/LOB/LOG) (~5 May) | After AUS 09052026 (5 Jun) | After AUS 07062026 (15 Jun) | After AUS 08072026 (15 Jul) |
|---|---:|---:|---:|---:|---:|---:|
| Days from today | 0 | 9 | 8 | 39 | 49 | 79 |
| KIT-STA-2 stock | 1,026 | (no kit OL) | (no kit OL) | +2,016 → 2,144 | +1,260 → 2,142 | +1,372 → 2,747 |
| KIT-COM-4 stock | 4,598 | (no kit OL) | (no kit OL) | +3,052 → 5,649 | +3,164 → 7,148 | +3,192 → 8,711 |
| KIT-ULT-6 stock | 2,762 | (no kit OL) | (no kit OL) | +1,036 → 3,049 | +1,244 → 3,728 | +1,428 → 4,581 |
| Kit cover (97/d) | 88d | 79d | 79d | **108d ⚠️** | 137d ⚠️ | 165d ⚠️ |

⚠️ Cover exceeds 100d post-each-arrival - given the -41% vs base / -54% vs scaled gap, kit quantities on each container will land soft. **Not a critical flag** (lead times mean we order conservatively), but the AUS 08072026 kit mix should reflect actual run-rate.

### IF AUS 09052026 SLIPS A FURTHER 7 DAYS (worst case: Sally jars beyond 25 Apr or any production slip)

- KIT-STA-2: 1,026 / 26.5 = 39d → out ~5 Jun (current revised arrival). +7d slip = 7-day OOS gap. **Need bridge plan.**
- LIQ-BAS-2: at 24.5/d, 490 = 20d. AUS 05052026 brings 648 → cover after = ~46d → out ~22 Jun. Safe.
- LIQ-SEN-2: 63 → out ~12d (8 May). AUS 05052026 brings 216 → +40d cover. Safe assuming AUS 05052026 lands.
- ACC-REM-BOW: 1,233 / 34.2 = 36d → out 2 Jun. AUS 09052026 +7d slip = 9-day OOS gap.

→ STA + ACC-REM-BOW are the slip-sensitive items. Watch jars completion daily.

---

## OVERSTOCK FLAGS (post-arrival cover > 100d, target 45-75d)

- **KIT-COM-4: post-09052026 cover = 5,649 / 51.3 = 110d.** Post-08072026 = 8,711 / 51.3 = 170d. ~6-9 weeks of excess at actual rate.
- **KIT-ULT-6: post-09052026 cover = 3,049 / 19.2 = 159d.** Wildly over 75d target. Consider cutting ULT on AUS 08072026.
- **LIQ-SEA-3: 187d cover at 13.2/d.** Already over. AUS 09052026 brings another 2,808 → 400+ days. Cut from 09052026 if possible.
- **LIQ-GLO-4: 87d cover.** AUS 09052026 +1,296 → 224d. Cut.

These reinforce the broader 0.86x-actual-vs-1.3x-target message: container quantities are calibrated to growth-factor, but kit/liquid run-rate is base or below.

---

## FOLLOW-UP ITEMS

### Immediate (today / tomorrow)
- [ ] Chase Chantelle (New Directions) on 22-04-2026 ingredients PO. Phone call if email silent by EOD 27 Apr.
- [ ] Confirm AUS 05052026 G3PL arrival date with Lily / Daniel.
- [ ] Greg: update POS MODEL with overrides listed at top.
- [ ] Daniel: draft AUS 08072026 fill PO for 29 Apr (Heal CN-in-kit, kit-mix revision, add ACC-LAB / ACC-THA).
- [ ] Lily WeChat - confirm B114 jars finished 25 Apr and Sally fill window started.

### By end of week
- [ ] Chase Katrina on PO 10 Heal recount + B360 transfer + ShipHero name sync.
- [ ] Decide ACC-REM-500 next replenishment route (08072026 OL vs OP fill).
- [ ] Confirm separate Base/LOB/LOG bridge express timing - Daniel.

### Ongoing
- [ ] Place Avi PO for ACC-LAB (~20k) ~mid-May.
- [ ] Monitor LO Base (LIQ-SEN-2) day-by-day for OOS - 7d cover, narrow window even with AUS 05052026.
- [ ] Re-verify the 22,090-unit colour deduction anomaly from 17 Apr POS Check (POW-ENE, POW-DRE, POW-ROY, POW-JUS, POW-GOL, POW-BRE, POW-CRE) once Katrina replies.
