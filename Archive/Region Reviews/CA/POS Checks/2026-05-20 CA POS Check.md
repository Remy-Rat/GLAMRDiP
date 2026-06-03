# POS MODEL CHECK — CA — 20 May 2026

> Source data: Order Schedule xlsx re-pulled 20 May 11:33 AEST. Shopify latest 19 May; 3PL latest 19 May. POS MODEL `UPDATED` cell not populated by Greg — data treated as 19 May AEST close.
>
> **Focus per user (20 May): Heal + Remove timing is the only thing that matters this cycle. Everything else is supporting context.**

## MANUAL OVERRIDES APPLIED
- **CA 21062026 contents** = reconfigured 14-15 May to 40HQ **with kits** (672 STA + 1,988 COM + 1,008 ULT + tips + Matte/Soak/Clear + 4,000 Remove Bowls + mailers/satchels). POS MODEL extract confirms reflected in sheet (kit OL columns match).
- **Swift `14-05-2026` Local Filling PO** = 6,500 LIQ-HEA-5 + 9,000 ACC-REM-500 + 1,000 ACC-REM (120ml). Status `Ordering`. Per user 20 May: ingredient POs in motion (New Directions Canada **Completed**, Amazon Canada **Completed**, Greenfield **Placed**). Outstanding gate: Joel pays Swift (prior balance + $13,064.63 advance) AND places 15-05-2026 Butuo Remove bottles raw goods PO.
- **PO 37 POW-COL-G16 247 check-in** = closed off ages ago per user 20 May. Drop from open threads.
- **ACC-LAB-CA B360 deduction rule** = still not firing (NaN per memory, not yet fixed by Greg). Model DSR 308/d used directly; no 3PL cross-check.

---

## DATA FRESHNESS
- POS MODEL last updated: ~19-20 May (UPDATED cell empty — Greg paste discipline carry)
- 3PL data last valid: 19 May (1d ago)
- Growth factor (global): **2.0x** (Kit base 80/d → scaled 160/d)
- Shopify latest: 19 May (+1d lag normal)

---

## STOCK POSITION — HEAL + REMOVE (THE LEAD WORRY)

| SKU         | Stock | Model DSR (2.0x kit-adj) | Cover @ Model | 3PL 14d avg | Cover @ 3PL | Combined 7d Shopify+bundle | Cover @ 7d |
| --- | ---:| ---:| ---:| ---:| ---:| ---:| ---:|
| **LIQ-HEA-5** | 6,487 | 170/d | 38d | 131.5/d | 49d | 136.2/d (135.2 kits + 1.0 standalone) | 48d |
| **ACC-REM-500** | 1,943 | 140/d | **14d** | 100.0/d | 19d | 108.9/d (101.0 std + 7.9 bun-2) | **18d** |
| ACC-REM (120ml) | 3,919 | 62/d | 63d | 12.5/d | 314d | 8.0/d (2.3 std + 5.7 bun-1) | 490d |
| ACC-REM-BOW | 5,334 | 80/d | 67d | 20.2/d | 264d | 4.4/d (1.9 std + 2.5 bun-2-shared) | n/a |
| LIQ-HEA-5 max-day | – | 177/d 3PL day | 37d | – | – | – | – |
| ACC-REM-500 max-day | – | 145/d 3PL day | 13d | – | – | – | – |

**Read:**
- **ACC-REM-500 is the headline.** 14-18d cover at any rate above model; 13-14d at the worst-case rates. Will OOS in **early-mid June**.
- **LIQ-HEA-5 has slack** at actual rate (48-49d cover) but the model rate (170/d) compresses cover to 38d — i.e. if the surge keeps climbing toward the scaled 160/d kit target, Heal cover closes fast.
- **ACC-REM (120ml) is massively overstocked** (314-490d cover). Bundle/upsell switch has shifted virtually all Remove demand to 500ml. Consider whether to even add 1,000 to Swift (currently in the PO).
- **ACC-REM-BOW** is steady — 67d at model, 264d at 3PL rate. Container CA 21062026 brings 8,000 more (1 Jul arrival). Will be overstocked post-arrival.

---

## CONTAINER GAP — WHAT THE CN BOX CAN'T FIX

**CA 21062026 brings ZERO LIQ-HEA-5, ZERO ACC-REM-500, only 1,000 ACC-REM (120ml).** These are locally filled at Swift — the next supply event for Heal + Remove 500ml is the 14-05-2026 Swift fill.

This means **the entire Heal/Remove timing arc is detached from container timing**. CA 21062026 arrival on 1 Jul does nothing for these two SKUs. The choke point is Swift production lead and Joel's payment gate.

---

## SWIFT FILL ETA — POST-PAYMENT TIMELINE

Per CA memory: Swift takes ~5-7 days fill completion → 247 restock. Per Abhishek 14 May email: he won't share production timeline until prior balance + advance ($13,064.63) clear. Ingredient feeders now in motion (NDA Completed, Amazon Completed, Greenfield Placed). Butuo Remove bottles PO drafted 15 May, **not yet placed by Joel**.

**Assumed lead-time stack post-Joel-payment** (each can compress if Swift prioritises):
- Butuo bottles transit to Swift: **5-7 days** (raw goods POs typically air or domestic CN→CA)
- Swift production (parallel with bottles transit once advance clears): **~14 days**
- Swift → 247 restock: **~5-7 days** (per `swift-lead-times` memory)
- **Total ≈ 25 days** post-payment to 247 shelf

| Joel pays | Swift fill at 247 ETA |
| --- | --- |
| 20 May (today) | ~14 Jun |
| 23 May (+3d) | ~17 Jun |
| 25 May (+5d) | ~19 Jun |
| 30 May (+10d) | ~24 Jun |

**Compression levers:** Swift can possibly fill from existing 120ml bottles inventory while Butuo bottles arrive. Confirm with Abhishek what's on hand at Swift right now.

---

## OOS GAP MATRIX — ACC-REM-500 (THE ONE THAT BREAKS)

Stock 1,943 today. Gap = days between OOS date and Swift restock arrival. **Positive gap = OOS days before fill lands.**

| Joel pays | Swift arrives | OOS @ 7d (108.9/d) | OOS @ 14d (99.1/d) | OOS @ model (140/d) | OOS @ 3PL-max (145/d) |
| --- | --- | --- | --- | --- | --- |
| **20 May (today)** | 14 Jun | 6 Jun (**+8d gap**) | 8 Jun (+6d) | 2 Jun (+12d) | 2 Jun (+12d) |
| 23 May | 17 Jun | 6 Jun (+11d) | 8 Jun (+9d) | 2 Jun (+15d) | 2 Jun (+15d) |
| 25 May | 19 Jun | 6 Jun (+13d) | 8 Jun (+11d) | 2 Jun (+17d) | 2 Jun (+17d) |
| 30 May | 24 Jun | 6 Jun (+18d) | 8 Jun (+16d) | 2 Jun (+22d) | 2 Jun (+22d) |

**Read:** OOS is **unavoidable** at every payment date and every rate. The cheapest scenario (Joel pays today, demand stays at 14d combined rate of 99/d) still has a **6-day OOS window**. The expensive scenario (Joel delays 10 days, model 140/d sustains) widens to **22 days**.

**Every additional day Joel delays = 1 additional day of OOS** — there is no slack in this stack.

---

## OOS GAP MATRIX — LIQ-HEA-5 (THE BUFFER)

Stock 6,487. Gap = days between OOS and Swift restock.

| Joel pays | Swift arrives | OOS @ 7d kits 136.2/d | OOS @ 14d kits 127.7/d | OOS @ model 170/d | OOS @ 3PL 131.5/d |
| --- | --- | --- | --- | --- | --- |
| **20 May (today)** | 14 Jun | 6 Jul (**-22d slack**) | 9 Jul (-25d) | 27 Jun (-13d) | 8 Jul (-24d) |
| 23 May | 17 Jun | 6 Jul (-19d) | 9 Jul (-22d) | 27 Jun (-10d) | 8 Jul (-21d) |
| 25 May | 19 Jun | 6 Jul (-17d) | 9 Jul (-20d) | 27 Jun (-8d) | 8 Jul (-19d) |
| 30 May | 24 Jun | 6 Jul (-12d) | 9 Jul (-15d) | 27 Jun (-3d) | 8 Jul (-14d) |

**Read:** Heal is **safe under every actual-rate scenario.** Only the model 2.0x rate (170/d, the aspirational target) compresses cover enough to threaten — and only if Joel delays beyond 10 days does the model gap close to <3d. **Heal is OK.** Worry is concentrated entirely on ACC-REM-500.

---

## CHECK-IN PROGRESS

No active ShipHero CSVs provided. Last container landed (Powder Room) was checked in 4-5 May per prior recap. CA 21062026 is in production (est. completion 28 May). No double-count risk this cycle.

---

## PACKAGING & INSERTS

| SKU | 3PL stock | 14d avg ded | Days cover | Benchmark | Anomaly days last 14d |
| --- | ---:| ---:| ---:| ---:| ---:|
| ACC-LAB-CA | (model 6,878) | – B360 NaN | (model 22d at 308/d) | 735 | n/a (rule broken) |
| ACC-THA | 32,405 | 172.1 | 188d | 735 | 0 |
| ACC-INS | 21,505 | 126.8 | 170d | 435 | 0 |
| STO-BUB-BAG-L | 7,426 | 128.3 | 58d | 435 | 0 |
| STO-BUB-BAG-S | (247-supplied) | – | – | – | – |

**ACC-LAB-CA carries the only inserts/packaging risk** — Mixam 1,300pcs reprint in production (ETA early-mid Jun, MX2029340). 10k next reorder due by ~26 May - 2 Jun. Lead 30-33d + 7d buffer. Model says 22d cover at 308/d — that gets us to mid-Jun, broadly matching reprint arrival, BUT actual deduction rate is unknown due to B360 NaN. Recommend Remy places the 10k reorder this week regardless to keep the cycle on rhythm.

ACC-THA + ACC-INS + STO-BUB-BAG-L all comfortable. STO-BUB-BAG-L will lift further when CA 21062026 lands (1 Jul).

---

## STOCK-OUT FORECAST — THE BIG PICTURE

### 🔴 STOCKOUT BEFORE SWIFT FILL ARRIVES

| SKU | Stock | Rate | OOS | Swift arrives | Gap |
| --- | ---:| ---:| --- | --- | ---:|
| ACC-REM-500 | 1,943 | 99-145/d | 2-9 Jun | 14-24 Jun (depends on Joel pay date) | **+6 to +22 days OOS** |

### 🟡 TIGHT (Swift-dependent)
| SKU | Stock | Rate | OOS | Notes |
| --- | ---:| ---:| --- | --- |
| LIQ-HEA-5 | 6,487 | 127-170/d | 27 Jun - 9 Jul | Safe at actual rate; tight only if model 170/d sustains AND Joel delays >10 days |

### 🟢 SAFE
- All kits (76-316d cover; KIT-STA-2 oversupplied, KIT-COM-4 safest)
- All other liquids (137-248d cover; pre-21062026 levels strong)
- ACC-REM (120ml) — massive overstock, demand collapsed
- ACC-REM-BOW — 264d cover, container brings 8,000 more
- Packaging — all comfortable

### ⚫ MONITORED COLOURS (pre-1 Jul container)
- Blue Moon / Peony Puff / Glacier Glow: prior review at -23/-19/-47d gaps. Container restocks 600/600/800 on 1 Jul. Accept the gap per 13 May Joel decision (Sally arrears + cash-tight blocks express). Daily monitor.
- POW-CLE-193 + POW-JUS-449: high 3PL deductions are offer-attached pull (per 13 May review), not data issue. Stocks 14,001 / 10,704 → 70d / 63d cover at current burn.

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (act today/this week)
1. **Joel pay Swift Innovations** — prior balance + $13,064.63 advance. **Every day = +1 day of ACC-REM-500 OOS.** Ingredients sequenced (NDA Completed / Amazon Completed / Greenfield Placed); payment is the only remaining gate to start Swift production.
2. **Joel place 15-05-2026 Butuo Remove bottles raw goods PO.** 5 days unplaced. Required to feed Swift 500ml production. PO already drafted by Remy 15 May.
3. **Daniel/Remy confirm with Abhishek** what 500ml bottle inventory Swift has on hand right now — if any, Swift can start without waiting for Butuo, compressing the lead.
4. **CX prep for ACC-REM-500 OOS window** (~6-12 days minimum, possibly 18-22d if payment slips). Gav rollout + theme switch to alternate offer. The Remove 500ml stockout will hit during the active $85-gift offer window — material CX risk.

### 🟡 WARNING (act this week)
5. **Sally accept revised CA 21062026 40HQ PO additions** (sent 15 May). Container est. completion 28 May = 8 days. Sally raw goods + $150k arrears are the gating risks. **Daniel monitor.**
6. **Mixam ACC-LAB-CA 10k reorder by ~26 May - 2 Jun.** Remy place. Don't wait for 1,300 reprint arrival — Mixam lead 30-33d.
7. **Daniel schedule Linda tip filling** for CA 21062026 (Mani Mat 1,100 + Square 1,500 + Stiletto 200 + Ballerina 1,000 + Almond 1,000 + Coffin 5,000).
8. **CA 25072026 sizing review** by 27 May (place date). At surge rate (~135-160/d kits sustained), the 5,404 kit allocation may be tight on arrival — re-check after 1 more week of post-surge data.

### 🟢 MONITOR
9. **Greg POS MODEL refresh** — ACC-REM-500 model 140 vs actual 100 (overstated); ACC-REM (120ml) 62 vs 12.5 (5x overstated); LIQ-HEA-5 170 vs 131.5 (slightly high but kit-adjusted basis defensible).
10. **Greg ACC-LAB-CA B360 deduction rule fix.** Still NaN, prevents actual cover calc.
11. **Greg update CA 21062026 ETA** in sheet from 22 Jul → 1 Jul (Lily vessel confirmation from 13 May review — not yet refreshed).
12. **Gav booklet-missing CX email rollout** — list with him since 11 May, 9 days no reply.
13. **Daniel + Joel kit DSR rebase decision** after 2 more weeks of post-surge data. Don't lower 2.0x yet per [[growth-factor-framing]].

---

## LOCAL FILL FORECAST

**Swift Innovations** — Heal + Remove 500ml (ref: 14-05-2026, status `Ordering`)
- Heal in PO: **6,500 pcs**. Post-fill stock at Swift arrival (~14 Jun if Joel pays today):
  - At actual 131.5/d: stock at arrival ~6,487 - (25d × 131.5) = ~3,200 → post-fill 9,700 → 74d cover. Good.
  - At model 170/d: stock at arrival ~6,487 - (25d × 170) = ~2,237 → post-fill 8,737 → 51d cover. Acceptable.
- Remove 500ml in PO: **9,000 pcs**. Post-fill stock at arrival:
  - At actual 99/d: 0 + 9,000 = 9,000 → 91d cover from arrival (only after the 6+d OOS).
  - At model 140/d: 0 + 9,000 = 9,000 → 64d cover from arrival.
- Remove 120ml in PO: **1,000 pcs**. **Kept intentionally** as fallback supply: if ACC-REM-500 OOS during the upcoming gap window, the website upsell flips back from Remove 500ml → 120ml — we need 120ml to cover that bridge until next Swift fill. Current 120ml cover 314d standalone, but bridge scenario will drain it fast under switched-upsell traffic.

**Next Swift fill placement (after this one lands):**
- At kit-adjusted 130/d Heal burn + scaled target ramp: post-fill cover 74d → next fill needs to **arrive** ~Aug-end. Place by ~mid-Jul (allowing 25d lead).
- Remove 500ml: 9,000 / 99/d (current 14d rate) = 91d post-fill. If surge keeps lifting, drop to 60d. Place next Remove 500ml fill ~mid-Aug.

---

## PO RECOMMENDATIONS

Standard target: maintain 14-21d kit cover. Lead times: 84d (raw goods → delivery), 44d (filling), 30d (shipping), 5-7d (Swift restock).

### Kits — no action needed
KIT-STA-2 / KIT-COM-4 / KIT-ULT-6 all 76-316d cover; CA 21062026 brings 672 + 1,988 + 1,008 (1 Jul) + CA 25072026 1,400 + 2,800 + 1,204 (25 Aug). Cover comfortable through Sep at surge rate.

### Locally-filled — Swift cycle is the only active loop
- **Heal**: 14-05-2026 PO covers next ~70d. Next placement ~mid-Jul.
- **Remove 500ml**: 14-05-2026 PO covers next ~60-90d depending on rate. Next placement ~mid-Aug.
- **Remove 120ml**: 314d cover, no action.

### Local printing — Mixam
- 1,300pcs reprint in production (MX2029340, ETA early-mid Jun).
- **10k reorder due by 26 May - 2 Jun.** Remy to place this week.

### Raw goods (CN-supplied)
- **Butuo Remove bottles raw goods PO (15-05-2026 draft)** — Joel to place. Feeds Swift 500ml cycle. 5 days unplaced.
- No other raw goods POs due in window.

---

## CASCADING ARRIVAL PROJECTION — KEY SKUs

Target cover: 45-75 days at the new (post-surge) actual rate. Stage = post-arrival cover at actual 14d rate.

| SKU | NOW stock | After Swift fill (~14-24 Jun) | After CA 21062026 (1 Jul) | After CA 25072026 (~25 Aug) |
| --- | ---:| ---:| ---:| ---:|
| **LIQ-HEA-5** | 6,487 (49d) | ~9,700 (74d) | 9,700 (74d) — container brings 0 | 9,700 minus burn ~5,200 (40d) |
| **ACC-REM-500** | 1,943 (19d) | OOS for 6-22d, then ~9,000 (91d) | 9,000 (91d) — container brings 0 | 9,000 minus burn ~3,400 (34d) |
| **KIT-COM-4** | 6,868 (76d 3PL) | 6,868 (76d) | 8,856 (98d) ⚠️ | 11,656 (129d) ⚠️ |
| **KIT-ULT-6** | 2,978 (116d 3PL) | 2,978 (116d) | 3,986 (155d) ⚠️ | 5,190 (202d) ⚠️ |
| **KIT-STA-2** | 4,033 (316d 3PL) | 4,033 (316d) ⚠️ | 4,705 (368d) ⚠️ | 6,105 (478d) ⚠️ |

⚠️ = over 100d cover. **KIT-STA-2 is structurally over-ordered against the new offer mix** — STA is selling 13/d (7d) vs the COM 96/d and ULT 26/d. The CA 21062026 + CA 25072026 add another 2,072 STA units on top of an already 316d cover.

**Sales Analysis hypothesis: same Shopify flow STA→COM substitution we saw in UK** — verify and quantify before sizing CA 25072026.

### IF SWIFT FILL IS DELAYED (Joel pays slips)
- ACC-REM-500: every additional day of payment delay = +1 day of OOS. At +10d delay, 22-day OOS during active offer window.
- LIQ-HEA-5: still safe under all actual-rate scenarios up to +10d delay. Only at model 170/d rate does the gap close to <3d (a +10d delay scenario).

---

## FOLLOW-UP ITEMS

**Immediate (today)**
- [ ] Joel: pay Swift (prior balance + $13,064.63 advance)
- [ ] Joel: place 15-05-2026 Butuo Remove bottles PO
- [ ] Remy/Daniel: confirm Swift 500ml bottle inventory on hand to compress lead time
- [ ] Remy/Gav: CX prep for ACC-REM-500 OOS window (theme switch / alternate offer)

**This week**
- [ ] Sally: accept revised CA 21062026 40HQ PO additions (Daniel monitor)
- [ ] Remy: Mixam ACC-LAB-CA 10k reorder by 26 May - 2 Jun
- [ ] Daniel: Linda tip filling schedule for CA 21062026
- [ ] Daniel/Remy: CA 25072026 sizing review by 27 May (place date)

**Ongoing**
- [ ] Greg: POS MODEL DSR refresh (ACC-REM-500 140→100, ACC-REM 62→12.5, LIQ-HEA-5 170→130)
- [ ] Greg: ACC-LAB-CA B360 deduction rule fix
- [ ] Greg: update CA 21062026 ETA 22 Jul → 1 Jul in sheet
- [ ] Gav: booklet-missing CX email rollout
- [ ] Daniel + Joel: kit DSR rebase decision after 2 more weeks of post-surge data
