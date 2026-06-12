# 🇬🇧 UK POS Model Check — 9 Jun 2026

## Data Freshness

- POS MODEL last extracted: 2026-06-09 11:43 AEST (Greg paste timestamp not surfaced in extract; user-confirmed fresh today)
- 3PL data: Fulfillable deduction integrity still BLIND (`inventory_changes` 500-row cap unresolved — 5th cycle). All "actual DSR" figures use Shopify standalone + kit-adjusted estimates, not 3PL deductions.
- Shopify data latest: 2026-06-08 (Shopify +1d lag normal)
- Growth factor: 1.3x (89 base → 115.7 scaled)

## Manual Overrides Applied (post-paste events)

| SKU | Sheet | Override | Source |
|---|---|---|---|
| ACC-REM (120ml) | 458 + 0 inbound | 458 + 4,155 inbound (PO 11 Liquipak, ships Tue 10 Jun, lands ~16 Jun) | Joel paid 9 Jun per Remy |
| ACC-REM-500 | 2,718 + 571 packup | 2,718 + 400 inbound (PO 11 Liquipak) + 571 packup | PO 11 ShipHero pull 2 Jun |
| **ACC-LAB-UK** | **1,423** | **~11,423 (PO 17 received 10,000/10,000 per ShipHero, status "pending" unreliable per [[shiphero-status-unreliable]])** | **ShipHero PO 17 pull 9 Jun** |
| **5 free-gift bridge SKUs (PO 18)** | **Sheet shows in B360 PACKUP STOCK inbound** | **Booked in 6 Jun (PO 18 closed): ACC-NAI-MAT +386, ACC-TRA-BAG +751, ACC-FRE-MANI +1,529, POW-BLO-042 +2,700, POW-CRE-217 +5,686** | **ShipHero PO 18 pull 9 Jun** |
| LIQ-BAS-2 | 8,000 inbound (Chemence 22-04) status "Ordering" | Lands Fulfillable ~10 Jul (3 Jul completion verbal Vik 28 May + 5 biz days ship) | Vik Slack 28 May |
| UK 03062026 + UK 02072026 ETA | Sheet "On the Way" | Combined 40HQ, arrival ~22 Jul per Remy 3 Jun summary (Upcoming Orders said 15 Jul, summary is more recent) | Remy 3 Jun |
| B360 PACKUP STOCK (remainder) | "In Production" | 5 priority bridge SKUs released via PO 18. Rest still locked: 17 OOS colours + ACC-LAB legacy 7,349 + ACC-INS/ACC-THA packup. Joel £8,500 balance still unpaid + Abdul disposal quote dispute. | Daniel 4 Jun Slack + ShipHero PO 18 |

---

## Step 0c — Kit-Adjusted DSR Validation

Fulfillable picks per-kit automation rules (confirmed 13 Apr 2026):
- LIQ-BAS-2: 1 per kit + standalone
- LIQ-GLO-4: 1 per kit + standalone
- LIQ-HEA-5: 1 per kit + standalone
- ACC-INS: 1 per kit + standalone
- ACC-LAB-UK + ACC-THA: 1 per order + standalone

Scaled kit DSR = 115.7/d. So kit-adjusted base burn:
- Base: 115.7 + Shopify standalone (19.1/d 14d) = 134.8/d at scaled
- Glow: 115.7 + Shopify standalone (9.9/d 14d) = 125.6/d at scaled
- Heal: 115.7 + Shopify standalone (1.4/d 14d) = 117.1/d at scaled

POS MODEL DSRs for these (144.3, 128.7, 118.3) look broadly consistent with kit-adjusted scaled rates — model is already including kit consumption. **No double-add needed.** ✓

Sense check at W23 actual ~106.9/d (today's digest):
- Base: 106.9 + 19.1 = 126.0/d
- Glow: 106.9 + 9.9 = 116.8/d
- Heal: 106.9 + 1.4 = 108.3/d

---

## Step 0b — Growth Factor Health Check

- Model growth: 1.3x (89 base → 115.7/d)
- Actual W22-W23 selling: ~99-107/d kits
- Gap to scaled: -7% to -14% (improved from W22's -26%)

Gap is narrowing — W23 -8% (today's digest 106.9/d) is the smallest in 3 weeks. Hold 1.3x for ordering per [[growth-factor-framing]]; not over the 50%/4-week trigger. Overstock risk on KIT-COM-4 / KIT-ULT-6 still present (see Cascading Arrival Projection below).

---

## Step 1 — Stock Position (Dual DSR)

### Kits

| SKU | Stock | Projected DSR (1.3x) | Cover @ Projected | Actual DSR | Cover @ Actual |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 11 | 6.5 | 2d | 0.6 | 18d |
| KIT-COM-4 | 1,657 | 68.9 | 24d | 73.9 | 22d |
| KIT-ULT-6 | 2,770 | 40.3 | 69d | 21.6 (est) | 128d |

**KIT-STA-2 effectively OOS** — substitution to KIT-COM-4 carries the load (78.6% of kit demand). COM dominant; STA + ULT remaining shares ~10% each per Sales Analysis 26 May.

### Liquids

| SKU | Stock | Projected DSR | Cover @ Projected | Actual DSR (kit-adj) | Cover @ Actual |
|---|---:|---:|---:|---:|---:|
| LIQ-BAS-2 | 1,395 | 144.3 | 10d | 115-135/d | **10-12d** 🔴 |
| LIQ-GLO-4 | 2,547 | 128.7 | 20d | 106-117/d | 22-24d 🟡 |
| LIQ-HEA-5 | 2,908 | 118.3 | 25d | 108-117/d | 25-27d 🟡 |
| LIQ-SEA-3 | 2,366 | 15.6 | 152d | 10.6 | 224d |
| LIQ-BON-1 | 439 | 6.5 | 68d | 3.1 | 142d |
| LIQ-SEN-2 | 0 | 0 | n/a | 0 | discontinued |
| LIQ-SEN-4 | 0 | 0 | n/a | 0 | discontinued |

### Remove products

| SKU | Stock | Projected DSR | Cover @ Projected | Actual DSR | Cover @ Actual | Notes |
|---|---:|---:|---:|---:|---:|---|
| ACC-REM (120ml) | 458 | 59.8 | 8d | 39.9 (combined w/ bundle) | 11d | PO 11 +4,155 lands ~16 Jun |
| ACC-REM-500 | 2,718 | 36.4 | 75d | 66.5 | 41d | PO 11 +400 lands ~16 Jun |
| ACC-REM-BOW | 3,596 | 66.3 | 54d | 0.9 standalone (bundle eats) | bundle-driven | UK 29092026 +7,500 |

### Inserts / Free-gift bridge tips

| SKU | Stock | Projected DSR | Cover | Note |
|---|---:|---:|---:|---|
| ACC-TIP-COF | 68 | 117.0 | 0.6d 🔴 | Current offer; 1,389 in B360 packup |
| ACC-TIP-BAL | 16 | 3.9 | 4d 🔴 | Previous offer (now ~0 standalone) |
| ACC-NAI-MAT | 382 | 3.9 | 98d | OK as bridge; 2,652 packup locked |
| ACC-LAB-UK | 1,423 | ~110 (kit+std) | 13d 🔴 | PO 17 +10,000 awaiting Fulfillable book-in |
| ACC-INS | 5,401 | 106.6 | 51d | 7,349 packup |
| ACC-THA | 17,852 | 217.1 | 82d | 5,246 packup |

### Colours (CRITICAL flagged, full list in forecast)

19 colours flagged CRITICAL (<7d cover or stockout-before-arrival). High-velocity at risk:
- **POW-HEA-515** (Heaven): 962 / 44.7 = 22d, UK 03062026 +800 arrives 22 Jul = **-22d gap**
- **POW-CHA-011** (Charming): 421 / 31.1 = 14d, UK 03062026 +800 = **-30d gap**
- **POW-PIL-194** (Pillow Talk): 366 / 30.1 = 12d, UK 03062026 +1,600 = **-31d gap**
- **POW-FLO-024** (Flower Child): 194 / 20.0 = 10d, UK 03062026 +600 = **-34d gap**
- **POW-SWE-001** (Sweet Tooth): 547 / 16.3 = 34d, UK 03062026 +1,400 = **-10d gap**
- **POW-HAR-139** (Hard to Get): 544 / 21.4 = 25d, UK 03062026 +200 = **-18d gap**

These 6 alone = a packup-locked free-gift colour shortage problem if Joel doesn't clear B360 balance. The packup carries the bridge.

**Sustained sellers without inbound (overshooting model):**
- POW-SUG-545 (Sugar Rush): 30d 4.8/d, 7d 5.0/d — model 1.3, **3.8x model**, day 6+ sustained. Listing/promo audit candidate per Sales Analysis next phase.

---

## Step 2 — Check-In Progress (Active ShipHero POs)

**Source of truth: ShipHero quantity_received (status field unreliable for Fulfillable per [[shiphero-status-unreliable]]).**

| PO | Description | Status | quantity_received |
|---|---|---|---|
| PO 11 | Liquipak (4,155 ACC-REM + 400 ACC-REM-500) | pending — ships Tue 10 Jun | 0 / 4,555 (Joel paid 9 Jun, ships Tue) |
| **PO 17** | **Print Runner (10,000 ACC-LAB-UK)** | **pending (unreliable) — RECEIVED** | **10,000 / 10,000 (100%)** ✓ |
| **PO 18** | **B360 → Fulfillable transfer (5 priority free-gift SKUs)** | **closed 6 Jun** | **100% (Mat 386, Travel Bag 751, Tray 1,529, BLO-042 2,700, CRE-217 5,686)** ✓ |
| PO 10 | UK 03062026 (Sally CN) | pending — in production | 0 / 7,000+ |
| PO 14 | UK 02072026 (Sally CN) | pending — in production | 0 / 2,200+ |

**PO 17 and PO 18 are effectively booked in.** ACC-LAB-UK at ~104d cover after PO 17. 5 free-gift bridge SKUs available at Fulfillable from PO 18. No daily Roisin chase needed.

---

## Step 3 — Double-Count Detection

PO 11 (Liquipak fill) hasn't shipped yet — no Quantity Received. No double-counting on the active POs.

The shipment block `22-04-2026 | Local Filling PO | Chemence` shows status "Ordering" with OL 8,000 BAS + 6,000 GLO. ShipHero PO not yet created (goods still at Chemence). No double-count.

PO 17 + PO 18 status pending book-in. Will need a re-run once Roisin books them in — both have 0 Quantity Received today.

---

## Step 4 — Confirmed Days Cover (post-Liquipak)

Treating B360 packup as **0 confirmed** until Joel pays balance:

| SKU | Available | DSR (kit-adj) | Confirmed Cover | After PO 11 lands 16 Jun |
|---|---:|---:|---:|---|
| LIQ-BAS-2 | 1,395 | 130/d | 11d | unchanged |
| ACC-REM | 458 | 39.9 | 11d | +4,155 → 4,613 / 39.9 = **116d cover** ✓ |
| ACC-REM-500 | 2,718 | 66.5 | 41d | +400 → 3,118 / 66.5 = 47d |
| ACC-LAB-UK | 1,423 | ~110 | 13d | +10,000 PO 17 book-in → ~104d ✓ |
| ACC-TIP-COF | 68 | 117 | 0.6d | unchanged (lives in packup) |
| ACC-TIP-BAL | 16 | 3.9 | 4d | unchanged (lives in packup) |
| KIT-STA-2 | 11 | 0.6 (Shopify only) | 18d | UK 03062026 +448 → 22 Jul |

**Critical reads:**
- **LIQ-BAS-2 11d cover with no inbound until ~10 Jul = OOS 19-22 Jun → 10 Jul = ~18-21 day OOS gap.** Worse than last week's 11-16 day projection because actual rate has stayed at scaled kit-adjusted ~130/d.
- ACC-REM (120ml) resolves once PO 11 lands ~16 Jun. 0-2 day OOS gap if shipping holds Tue.
- ACC-LAB-UK depends entirely on Roisin booking PO 17 in within next ~10 days.

---

## Step 5 — Packaging & Inserts

Fulfillable 3PL deduction blind (5th cycle). No anomaly detection possible — flagged for visibility only.

Estimated rates at scaled kit DSR (115.7/d):
- ACC-INS 1 per kit = 115.7 + std 106.6 = **mostly kit-driven**. 5,401 / 110 = ~49d (matches POS MODEL 50.7d).
- ACC-LAB-UK 1 per order = ~110/d. 1,423 / 110 = 13d. Critical without PO 17 book-in.
- ACC-THA 1 per order. 17,852 / 217 (model) = 82d. Adequate.
- STO-BUB-BAG-L 1,453 stock, no measured ded — assume safe with PO 18 + container inflows.
- STO-BUB-BAG-S 19,445 stock — comfortable.
- STO-MAI-BAG-S 3,569 stock.
- STO-MAI-2 3,483 stock.

**Until cursor pagination fix lands, packaging anomaly detection is unavailable for UK.** Treat all packaging as "trust model + visual sanity check" only.

---

## Step 6 — Container / Order Status

### B360 PACKUP STOCK
- POS MODEL: In Production
- Reality: **288,898 units stranded.** £8,500 balance unpaid (Joel). $5kAUD disposal quote (Abdul) flagged by Daniel 4 Jun as suspicious.
- Holds: 17 OOS colours + 5 free-gift SKUs (Mat 381, Tray 1,524, Travel Bag 747, CRE-217, BLO-042) + tip bridge SKUs.
- Action: Joel pay balance; Remy negotiate disposal-quote pushback.

### 22-04-2026 Chemence (Base + Glow fill)
- POS MODEL: Ordering
- Reality: In production at Chemence. **Verbal 3 Jul completion (Vik via Remy Slack 28 May).** No formal email confirmation; 42d silent on email.
- Goods land Fulfillable ~10 Jul (5 biz days ship).
- Action: Joel chase Vik for compression/express options + formal email.

### 02-06-2026 Chemence (next UK PO)
- Joel placed via email 5 Jun (next fill: 9,000 BAS + 8,000 GLO).
- Vik no reply yet (4d).
- Brief target completion: ~15 Aug. Land Fulfillable ~22 Aug.
- Plus NORDIC + EU Chemence POs also placed 5-8 Jun (Joel sent 3 POs to Vik in 3 days).

### UK 03062026 + UK 02072026 (single 40HQ)
- POS MODEL: "On the Way"
- Reality: ETA 22 Jul (per Remy 3 Jun summary; Upcoming Orders had 15 Jul — go with summary).
- Combined manifest includes 784 STA + 2,800 COM + 1,848 ULT + 432 BAS + ~21,400 colours + STO + 90k empty-bottle components.
- **Misses early access (18 Jul / 21 Jul)** per Remy 3 Jun.

### UK 30082026
- POS MODEL: Ordering
- Daniel posted recommended PO 27 May. Joel sign-off pending (free-gift qty min 7k + 6-12 new colour collections).
- Sally lead 5-6 weeks; window closes within days.

### UK 29092026
- POS MODEL: Ordering (placeholder).

---

## Step 7 — Local Fill Status

### Chemence (Base + Glow)
- **22-04-2026 PO** — In production. 3 Jul verbal completion. Lands Fulfillable ~10 Jul. **Critical for Base OOS gap.**
- **02-06-2026 PO** — Placed 5 Jun. Vik silent. Expected completion ~15 Aug.
- Place PO-after-this in first week Aug to maintain 8-10 week cycle.

### Oils4Life (Heal)
- **No active PO.** Heal cover 25-27d at kit-adjusted rate. Dale silent 21d+.
- Lead time ~14d ingredients + 30d fill + 7d transit = ~51d. **Need to place by ~14 Jun** to land before stockout (~6 Jul at actual). Remy outbound urgent.

### Liquipak (Remove — exiting)
- **PO 11** — Joel paid 9 Jun. Ships Tue 10 Jun. Lands Fulfillable ~16 Jun. 4,155 ACC-REM + 400 ACC-REM-500.
- **This is the last Liquipak fill ever.**
- Replacement filler: outreach to Leading Solvents drafted today (Remy). 2-3 week window to lock alternative or accept ACC-REM 120ml runs out post this fill.

### Print Runner (ACC-LAB-UK)
- **PO 17** — 10,000 units delivered to Fulfillable. Awaiting Roisin book-in.

---

## Step 8 — Stock-Out Forecast (Adjusted)

### Stockout BEFORE arrival (gap < 0)

| SKU | Stock | DSR | OOS Date | Next Inbound | Arrives | Gap |
|---|---:|---:|---|---|---|---:|
| **LIQ-BAS-2** | 1,395 | 130/d | **20 Jun** | Chemence 22-04 +8,000 | ~10 Jul | **-20d** 🔴 |
| ACC-TIP-COF | 68 | 117 | 10 Jun | B360 packup +1,389 OR UK 03062026 | 22 Jul | -42d if packup stays locked |
| ACC-TIP-BAL | 16 | 0.8 | 29 Jun | UK 02072026 +100 | 22 Jul | -23d |
| 6+ colours | per above | per above | 18 Jun-4 Jul | UK 03062026 / 02072026 | 22 Jul | -10 to -34d |
| ACC-LAB-UK | 1,423 | 110 | 22 Jun | PO 17 book-in | this week | 0d if booked, -10d+ if slips |

### Tight (0-7d margin)

- LIQ-GLO-4: 2,547 / 116/d = 22d cover. Chemence 22-04 +6,000 lands 10 Jul → exactly at OOS. **Same gap as Base, less critical because GLO consumes slightly slower.**
- LIQ-HEA-5: 2,908 / 108/d = 27d cover. No fill PO placed → projected OOS 6 Jul. **Place Oils4Life fill PO this week.**

### Nothing on order

- ACC-REM-500: 2,718 / 66.5 = 41d → 19 Jul. No CN-style replenishment beyond PO 11's 400 units. UK 30082026 has 5k Remove 120ml; **does not address Remove 500ml gap.**
- LIQ-SEN-2/-4: 0 stock. Discontinued per [[uk-discontinued-liquids]]. No action.

---

## Step 8.5 — Liquipak Replacement Filler Timeline

ACC-REM (120ml) ends at Liquipak forever after PO 11:

```
ACC-REM after PO 11 lands: 4,613 / 39.9 = 116d cover (to ~10 Oct)
ACC-REM-500 after PO 11 lands: 3,118 / 66.5 = 47d cover (to ~26 Jul)
```

**ACC-REM-500 is the urgent one.** 47d cover means stockout late Jul unless either:
1. A new filler is engaged for Remove production by mid-Jun (decision + onboard + first fill within 6-8 weeks).
2. We pull from CN container (UK 30082026 brings 5,000 Remove 120ml, lands 30 Aug — too late).
3. We accept ~30-45d Remove 500ml OOS.

Outreach to Leading Solvents drafted. Recommend Remy + Daniel decide:
- Send out 3-4 outreach emails this week (Leading Solvents + 2-3 others).
- If no UK option viable by 23 Jun → switch Remove products to CN-fill on a future container (rebalance UK 30082026 if window still open).

---

## Step 8.6 — Container Gap Analysis

### UK 03062026 + UK 02072026 (40HQ, arrival 22 Jul)

| Gap | Detail | Mitigation |
|---|---|---|
| ACC-LAB-UK | 0 in container (locally printed). Cover 13d → 22 Jul = need PO 17 booked + likely a top-up | Roisin book-in PO 17. Avi-equivalent next PO ~end Jun. |
| LIQ-BAS-2 | 432 only (Sweden bridge bottle). Doesn't address UK Base. Chemence 22-04 separate. | Chemence dependency only. |
| LIQ-HEA-5 | 0 in container (Oils4Life local fill). | Oils4Life PO this week. |
| ACC-REM / ACC-REM-500 | 0 (Liquipak local fill). | PO 11 today + replacement filler decision. |
| ACC-TIP-BAL | 100 only. With 4d cover → 22 Jul still **gap**. | Either pull from packup, accept tip rotation, or add to UK 30082026 if Joel signs off. |

### UK 30082026 (40HQ, arrival 30 Aug)

| Gap | Detail | Mitigation |
|---|---|---|
| Free-gift quantity | Joel sign-off pending. Min 7k Mat/Tray/Travel Bag. | Joel must sign off this week. |
| New colour collections | Min 6-12 SKUs. | Joel sign-off. |
| Care liquid | Not in this container or the one after | Daniel monitor Oct/Nov cover gap. |
| LIQ-BAS-2 / LIQ-GLO-4 | Empty bottles for UK + Nordic + EU only (not filled). | Chemence dependency. |
| LIQ-HEA-5 | 0 | Oils4Life dependency. |

---

## Step 9 — What Needs Action

### 🔴 CRITICAL (act today / this week)

1. **LIQ-BAS-2 ~20 Jun OOS, fill lands ~10 Jul = -20 day gap.** Joel must email Vik this week for compression options on 22-04-2026 OR Daniel commits to a kit-throttle / attach reduction plan. **No mitigation in Slack as of today.**
2. **B360 packup balance £8,500 + disposal-quote pushback.** 5 priority free-gift SKUs released via PO 18 (closed 6 Jun) ✓. **17 OOS colours + ACC-LAB legacy 7,349 + ACC-INS/THA packup still locked.** Joel pay balance; Remy negotiate Abdul on disposal.
3. **Oils4Life Heal fill PO.** Place this week. Heal OOS ~6 Jul at actual rate. Lead time 51d.
4. **Liquipak replacement filler outreach.** Leading Solvents draft ready. Send 3-4 emails this week.
5. **UK 30082026 Joel sign-off.** Free-gift qty + new colour collections. Sally window closes within days.

### 🟡 WARNING (act this week)

7. **POW-SUG-545 sustained 3.8x model 6+ days.** Sales Analysis to confirm; permanent model reset candidate.
8. **W23 kit recovery confirmation.** Today's -8% the best in 3 weeks. Verify via Sales Analysis.
9. **Fulfillable returns SOP** (Roisin reply outstanding 9d).
10. **G3PL / Fulfillable / 247 Packing SOP updates** (Daniel 2 Jun email; Ben/Seby silent 7d).
11. **B360 stock-out balance** (parallel to disposal quote). Mihir/Mason silent 25d+.
12. **Ireland IOSS shipping mapping** (Remy).

### 🟢 MONITOR / FYI

- Fulfillable deduction blind (5th cycle). ShipHero `inventory_changes` cursor pagination still overdue.
- ACC-TIP rotation chain (Coffin running now, next is what?).
- UK 03062026 + UK 02072026 misses 18/21 Jul early access — CX comms plan.
- B360 deposit return ($30k AUD) — Abdul "today" 8 Jun, expected this week.

---

## Step 10a — Local Fill Forecast

### Chemence — Base + Glow

```
22-04-2026 PO: 8,000 BAS + 6,000 GLO
  Completion: 3 Jul (verbal)
  Lands Fulfillable: ~10 Jul

Base at landing: 1,395 - (30d × 130/d) = -2,505 (OOS for ~19 days before fill lands)
Post-fill: 8,000 - 2,505 = 5,495 / 130/d = 42d cover → next stockout ~21 Aug

Glow at landing: 2,547 - (30d × 116/d) = -933 (OOS for ~7 days)
Post-fill: 6,000 - 933 = 5,067 / 116/d = 44d → ~23 Aug

02-06-2026 PO: 9,000 BAS + 8,000 GLO
  Completion: ~15 Aug
  Lands Fulfillable: ~22 Aug

Base at 22 Aug: 5,495 - (43d × 130/d) = -85 → small stockout 21-22 Aug
Glow at 22 Aug: 5,067 - (43d × 116/d) = 79 → tight but holds

Post-fill (22 Aug): Base 9,000 / 130 = 69d, Glow ~8k / 116 = 69d
```

**Two fill cycles cover through ~30 Oct.** Place 3rd Chemence PO ~mid-Aug for late-Oct stockout protection.

### Oils4Life — Heal

```
No active PO. Heal cover 25-27d at 108-117/d kit-adj.

Lead: ~51d. Place by 14 Jun to land before stockout 6 Jul.

Sizing options (target 80-120d post-fill cover):
  6,000 units → 51d cover (lean, leaves gap if next fill slips)
  8,000 units → 68d cover (recommended)
  10,000 units → 86d cover (conservative, matches Chemence cycle)
```

Recommend 8,000 units.

### Liquipak — Remove (EXITING)

PO 11 is final. Post-arrival cover: ACC-REM 116d, ACC-REM-500 47d.

ACC-REM-500 is the binding constraint at 47d. **A replacement filler must be onboarded + first fill placed by ~mid-Jul to land before ACC-REM-500 OOS ~26 Jul.** Realistic given 6-8 week onboarding + fill cycles — only if outreach sends this week.

### Print Runner — ACC-LAB-UK

PO 17 (10,000 units) at Fulfillable awaiting book-in. Post-book-in: 1,423 + 10,000 = 11,423 / 110/d = 104d. Adequate through mid-Sep. Next PO place by ~mid-Aug.

---

## Step 10b — PO Recommendations

| Action | Owner | Deadline | Status |
|---|---|---|---|
| Place Oils4Life Heal fill PO (8,000 units) | Remy / Daniel | 14 Jun | Not placed; Dale silent |
| Send Liquipak replacement outreach (3-4 candidates) | Remy | This week | Leading Solvents drafted |
| Joel sign off UK 30082026 free-gift + colours | Joel | This week | 13d overdue |
| Joel email Vik for 22-04 compression | Joel | Today/tomorrow | Not done |
| Joel pay B360 £8,500 balance | Joel | This week | Stalled |
| 3rd Chemence PO (UK Base+Glow) | Daniel/Remy | Mid-Aug | Plan now |

---

## Step 10c — Cascading Arrival Projection (Kits + Liquids)

Target cover band: 45-75d post-arrival.

### Kits

|  | NOW (9 Jun) | After UK 03/02062026 (22 Jul) | After UK 30082026 (30 Aug) | After UK 29092026 (29 Sep) |
|---|---|---|---|---|
| KIT-STA-2 | 11 / 18d | +448+336 → ~795 / 1.3d ↓ | +0 → consumed | +616 → 51d (post-Sep) |
| KIT-COM-4 | 1,657 / 22d | -consumed +1,484+1,316 → ~ -700 +2,800 = ~2,100 / 28d | +3,584 → 78d ✓ | +1,008 → similar |
| KIT-ULT-6 | 2,770 / 128d | +700+1,148 → still ample | +840 → ✓ | +3,220 ⚠️ overstock candidate |

KIT-COM-4 still tight at 22 Jul arrival point — substitution flow keeps it lean. Sales Analysis to verify W23 actual.

### Base / Glow / Heal

|  | NOW | After Chemence 22-04 (10 Jul) | After UK 03/02062026 (22 Jul) | After Chemence 02-06 (22 Aug) | After UK 30082026 (30 Aug) |
|---|---|---|---|---|---|
| LIQ-BAS-2 | 1,395 / 11d | +8,000 → 42d | +432 only (empty bottles continue Sweden bridge) | +9,000 → 69d | empty bottles UK+Nordic+EU |
| LIQ-GLO-4 | 2,547 / 22d | +6,000 → 44d | empty bottles | +8,000 → 69d | empty bottles |
| LIQ-HEA-5 | 2,908 / 27d | OILS4LIFE PO needed by 14 Jun | (depends on Oils4Life fill) | | |

### Delay scenario

**If Chemence 22-04 slips by 2 weeks:** Base stockout extends from -20 days to -34 days. Glow joins Base in OOS (currently borderline). Kit fulfilment paused or kit-throttled.

**If PO 17 book-in slips past 16 Jun:** ACC-LAB-UK OOS ~22 Jun. Every order needs a label; this halts fulfilment until book-in completes.

### Overstock flags

- KIT-ULT-6 at 29 Sep arrival projects to **300+ days cover** at actual rate. Daniel to consider trimming UK 29092026 ULT qty if W23 actual doesn't recover above 25/d.
- ACC-REM-BOW at 29 Sep: 3,596 + 7,500 = 11,096 standalone, bundle-driven. Hard to model standalone cover; flag for Sales Analysis.

---

## Follow-Up Items

### Immediate (this week)
- [ ] Joel email Vik for 22-04-2026 Chemence compression/express options
- [ ] Joel pay B360 £8,500 stock-out balance
- [ ] Joel sign off UK 30082026 free-gift qty + new colour collections
- [ ] Joel approve LCL Remove Bowls bridge (12d unanswered)
- [ ] Remy chase Roisin daily on PO 17 + PO 18 book-in
- [ ] Remy + Daniel send Liquipak replacement outreach (Leading Solvents + 2-3 others)
- [ ] Remy place Oils4Life Heal fill PO (8,000 units, by 14 Jun)
- [ ] Daniel/Joel commit to LIQ-BAS-2 gap mitigation plan (express, throttle, attach reduction)

### By end of month
- [ ] Remy negotiate Abdul on B360 disposal quote ($5kAUD)
- [ ] Greg POS MODEL DSR refresh batch (LIQ-SEN to 0, per-kit DSR, ACC-NAI variants etc.)
- [ ] Implement ShipHero `inventory_changes` cursor pagination (5-cycle blind continues)
- [ ] Print Runner next ACC-LAB-UK top-up PO (~mid-Aug)

### Ongoing
- [ ] Watch W23 kit recovery (Sales Analysis next phase)
- [ ] Care liquid Oct/Nov gap (not in UK 30082026 or next)
- [ ] B360 deposit return ($30k AUD) — Abdul committed "today" 8 Jun
- [ ] Sweden re-ship UK2NOEXPRES (Roisin engaged 4 Jun, Daniel asked for DHL Express)
- [ ] Ireland IOSS shipping mapping (Remy)
