# POS MODEL Check - UK - 12 May 2026

## DATA FRESHNESS & MANUAL OVERRIDES

- **POS MODEL extracted:** 2026-05-12 13:38 (re-pulled fresh for this check; user confirmed today's paste)
- **3PL tab (B360):** last valid date 2026-05-12 — **but B360 is frozen Packup snapshot, all 14d deduction values = 0.** Live Fulfillable deduction history not in this sheet (deferred to next cycle per user direction).
- **Growth factor:** 1.3x (global). Per-container blocks all use 1.3x except UK 02072026 which is Birthday Sale.
- **Kit DSRs in model (Greg's refresh applied):** STA 13.0, COM 41.6, ULT 54.6 → base 109.2/d → scaled 1.3x = 142.0/d.
- **Actual 14d kit DSR (Shopify):** STA 8.9, COM 35.0, ULT 34.2 → total **78.1/d → effective growth 0.72x.**

**Manual overrides:**
- **Container merge assumed:** UK 03062026 + UK 02072026 ship as one 40HQ (Joel "highly likely will combine"). Both shown in sheet with arrival 15 Jul - consistent with merge.
- **Complete-kit substitution active:** STA gap absorbed by COM (user-confirmed). Combined STA+COM stock + DSR used for cover math.
- **ACC-LAB-UK actual rate:** sheet model 217.1/d; per user direction use actual 14d order rate. Shopify ACC-LAB shop_30d = 141.2/d but shop_14d = 0 (post-transition Fulfillable tracks ACC-LAB-UK, not generic ACC-LAB). Best proxy = 14d kit DSR + standalone-order DSR. **Working figure: ~100/d order rate** (78.1 kits + ~22/d non-kit orders, conservative on the high side).
- **22-04-2026 Chemence est. completion 17 Jun is stale** - sheet shows 60d from 23/04 placement, but Vik silent 14 days on free-issue caps/brushes. Treat as **at-risk; realistic completion +14d → ~1 Jul.**

---

## STOCK POSITION

### Kits (combined STA+COM under substitution)

| SKU | Stock | Inbound (B360 / 03062026 / 02072026 / 02082026) | Model DSR | Cover @ Model 1.3x | Shopify 14d DSR | Cover @ Actual |
|---|---:|---|---:|---:|---:|---:|
| KIT-STA-2 | 99 | 493 / 448 / 336 / 560 | 13.0 (×1.3 = 16.9) | 6d | 8.9 | 11d |
| KIT-COM-4 | 3,632 | 40 / 1,484 / 1,316 / 1,148 | 41.6 (×1.3 = 54.1) | 67d | 35.0 | 104d |
| KIT-ULT-6 | 3,608 | 0 / 700 / 1,148 / 840 | 54.6 (×1.3 = 71.0) | 51d | 34.2 | 105d |
| **STA+COM (sub)** | **3,731** | **(combined)** | **70.8** | **53d** | **43.9** | **85d** |

**STA gap removed via substitution** — STA standalone would stock out 23 May; combined with COM, 85d cover at Shopify rate covers through to mid-Aug, well past UK 03062026/02072026 merged arrival 15 Jul.

### Kit-Adjusted Liquids (kit demand + standalone)

| SKU | Stock | Inbound | Standalone Shop 14d | Kit Demand (78.1/d) | Combined DSR | Cover @ Actual |
|---|---:|---|---:|---:|---:|---:|
| LIQ-BAS-2 (Base) | 5,938 | 8,000 (22-04 Chemence) | 23.6 | 78.1 | 101.7 | **58d** |
| LIQ-GLO-4 (Glow) | 7,200 | 6,000 (22-04 Chemence) | 10.8 | 78.1 | 88.9 | **81d** |
| LIQ-HEA-5 (Heal) | 6,958 | 1,653 (B360 Packup) | 2.0 | 78.1 | 80.1 | **87d** |
| ACC-INS | 8,318 | 7,349 / 1,680 / 4,080 | 0.0 | 78.1 | 78.1 | **107d** |

All four healthy. Base + Glow + Heal all run through the 22-04-2026 Chemence completion window (sheet says 17 Jun → realistic 1 Jul ~50d out). Oils4Life Heal fill cycle: next Heal fill needs placing ~mid-late May to land in time, but with 87d cover that's safe through ~7 Aug.

### Non-Kit Liquids

| SKU | Stock | Inbound | Shop 30d | Cover (Shop) | Cover (Model) |
|---|---:|---|---:|---:|---:|
| LIQ-SEA-3 (Seal) | 2,724 | 369 / 432 / 1,080 / 864 | 12.7 | 215d | 175d |
| LIQ-BON-1 (Bond) | 540 | 194 / 216 / 216 / 432 | 3.1 | 174d | 83d |
| LIQ-SOA-6 (Soak) | 579 | 588 / 0 / 216 / 216 | 1.9 | 305d | 89d |
| LIQ-MAT-4 (Matte) | 781 | 469 / 0 / 648 / 216 | 2.4 | 326d | 100d |
| LIQ-SEN-2 (Sensitive Base) | 0 | 0 | 0.0 | **DISCONTINUED** | — |
| LIQ-SEN-4 (Sensitive Glow) | 0 | 0 | 0.0 | **DISCONTINUED** | — |

Per memory `reference_uk_discontinued_liquids.md`, LIQ-SEN-2/4 confirmed dormant in UK. Drop from model. Bond/Soak/Matte all overstocked vs Shopify reality (5+ months) — model DSR 2-3x actual.

### Remove Range (bundles inflate real demand)

| SKU | Stock | Inbound | Shop 30d (standalone) | + Bundle Share | Real DSR | Cover |
|---|---:|---|---:|---:|---:|---:|
| ACC-REM (120ml) | 1,389 | 43 (B360) | 11.3 | +15.0 (BUN-1) | 26.3 | **53d** |
| ACC-REM-500 | 4,264 | 571 (B360) | 9.7 | +10.8 (BUN-2) | 20.5 | **208d** |
| ACC-REM-BOW | 4,718 | 1,280 (B360) | 1.3 | +25.8 (both BUN) | 27.1 | **174d** |

ACC-REM (120ml) the tightest at 53d. Liquipak final 800L PO (paused replacement search) covers ~160d → OOS scenario early Sep crystallising.

### Inserts & Labels

| SKU | Stock | Inbound | Order Rate (proxy) | Cover @ Actual | Notes |
|---|---:|---|---:|---:|---|
| ACC-LAB-UK | 5,309 | 1,396 (B360 locked) | ~100/d | **53d** | Print Runner PO needed within ~2 weeks. 14-21d local lead. |
| ACC-THA | 22,538 | 5,246 / 5,600 / 5,600 / 11,200 | ~141/d (shop ACC-THA) | 160d | Healthy. UK 02082026 adds 11,200. |
| ACC-INS | 8,318 | (above, kit-adj) | 78.1/d | 107d | Healthy. |

**ACC-LAB-UK trigger:** at order rate ~100/d → 53d cover today. With 14-21d Print Runner lead, place by **~21-26 May** to keep landing above 14d cover. Sooner if order rate trends up.

---

## CONTAINER / ORDER STATUS

| Reference | POS MODEL Status | Est. Completion | Est. Arrival | Reality |
|---|---|---|---|---|
| **B360 PACKUP STOCK** | In Production | — | — | ~288,898 units locked. £8,500 deposit "paid slowly" (Daniel 4 May). Treat fully unavailable through end-June. Mason silent 28d. |
| **UK Powder Room AND Chemence** | Completed | — | 30 Apr | Landed ~29 Apr per Greg picking list. 7,568 Base + 8,000 Glow + colours in stock. |
| **22-04-2026 \| Chemence Fill** | Ordering | 17 Jun (sheet) | — | **Blocked 14 days on Vik free-issue reply.** Realistic completion +14d → ~1 Jul. 8,000 Base + 6,000 Glow. |
| **UK 03062026** | In Production | 21 May | 15 Jul | Balance NOT paid (35+ days). Ship-out 4 May lapsed. Container merge with 02072026 confirmed (Joel "highly likely"). |
| **UK 02072026** | In Production | 21 May | 15 Jul | Birthday Sale. Awaits jar payment. Merge with 03062026 into single 40HQ. |
| **UK 02082026** | (no status) | 13 Jul | 6 Sep | **Fill PO place date 13 May (TOMORROW).** No PO email visible in 21d. |
| (4 unnamed) | (no status) | 12 Aug → 18 Sep | 6 Oct → 12 Nov | Future placeholders. Not surfaced for action. |

---

## STOCK-OUT FORECAST

### CRITICAL (act today)

| SKU | Stock | DSR | Stocks Out | Next Inbound | Arrives | Gap | Bridge |
|---|---:|---:|---|---|---|---:|---|
| **POW-BUB-516** (Bubbly) | 3 | 5.4 | **12 May (today)** | UK 03062026 +400 | 15 Jul | -64d | Express via Sally |
| **POW-DAY-025** (Daydream) | 12 | 5.9 | 14 May | UK 02082026 +200 | 6 Sep | -115d | Add to 02082026 fill OR express |
| **POW-TRA-452** (Train-Wreck) | 49 | 16.2 | 15 May | UK 03062026 +800 | 15 Jul | -61d | Express via Sally |
| **POW-NOT-065** (Not 2day) | 23 | 4.6 | 17 May | **NOTHING** (B360 118 locked) | — | — | Add to UK 02082026 + B360 release |
| **POW-SEA-450** (Seaside) | 27 | 4.4 | 18 May | UK 02082026 +200 (B360 1,659 locked) | 6 Sep | -111d | Add to 02082026 + B360 release |
| **POW-SIN-254** (Sincere) | 87 | 7.8 | 23 May | UK 03062026 +800 | 15 Jul | -53d | Express via Sally |
| **KIT-STA-2** | 99 | 8.9 | 23 May (standalone) | UK 03062026 +448 | 15 Jul | -53d | **Resolved via Complete-kit substitution (user-confirmed)** |
| **POW-BAR-198** (Bare Necessity) | 189 | 12.4 | 27 May | UK 03062026 +1,600 | 15 Jul | -49d | Express via Sally |
| **POW-SLO-192** (Slow Burn) | 227 | 11.9 | 31 May | **NOTHING** | — | — | Add to UK 02082026 fill PO |

### WARNING (act this week)

| SKU | Stock | DSR | Stocks Out | Action |
|---|---:|---:|---|---|
| POW-JUS-449 | 0 | 5.8 | already OOS | B360 1,152 locked + UK 02082026 +200 (36d post-arrival cover - inadequate). **Bump 02082026 quantity** |
| POW-OVE-487 | 0 | 5.9 | already OOS | B360 1,610 locked + zero CN inbound. **Add to UK 02082026** |
| POW-FAI-308 | 0 | 5.9 | already OOS | B360 1,636 locked + zero CN inbound. **Add to UK 02082026** |
| POW-PEA-068 (Peachy) | 0 | 11.8 | already OOS | UK 03062026 +1,200 = 102d post-arrival. OK after merge lands |
| POW-GOD-017 (Goddess) | 0 | 6.3 | already OOS | UK 03062026 +400 = 63d post-arrival. OK |
| POW-CRU-090 (Crush) | 0 | 5.9 | already OOS | UK 03062026 +200 = 33d post-arrival. **Under-restocked, top up 02072026 or 02082026** |
| ACC-LAB-UK | 5,309 | ~100 | ~21 Jun | Print Runner PO ~21-26 May. 14-21d lead |
| ACC-REM (120ml) | 1,389 | 26.3 | ~5 Jul | Liquipak final 800L cover through ~early Sep. Decision needed on replacement filler |
| POW-RID-661, POW-MON-005, POW-BUT-098, POW-JET-206, POW-SWE-258 | ~100-230 | 3-6/d | 9-19 Jun | UK 03062026/02072026 inbound 200-400 each. Inadequate restock. Top up in 02082026 |

---

## CONTAINER GAP ANALYSIS

### UK 02082026 (fill PO place date 13 May, tomorrow)

Sheet contents: 560 STA + 1,148 COM + 840 ULT + 4,080 ACC-INS + 11,200 ACC-THA + colours.

**Recommended additions:**

| SKU | Current Stock | DSR | Recommended Add | Reason |
|---|---:|---:|---:|---|
| POW-OVE-487 | 0 | 5.9 | **800-1,000** | No CN inbound at all; B360 locked |
| POW-FAI-308 | 0 | 5.9 | **800-1,000** | No CN inbound at all; B360 locked |
| POW-JUS-449 | 0 | 5.8 | **+500 (bump from 200)** | 200 already in 02082026 = 36d only |
| POW-SEA-450 | 27 | 4.4 | **+400 (bump from 200)** | 200 already; bumps to ~135d |
| POW-NOT-065 | 23 | 5.2 | **600-800 (new add)** | Nothing in CN pipeline; B360 only 118 |
| POW-SLO-192 | 227 | 11.9 | **800** | Nothing on order at all; 11.9/d sustains |
| POW-CRU-090 | 0 | 5.9 | **+400** | 200 in 03062026 is too thin |
| POW-DAY-025 | 12 | 5.9 | **400** | Only 200 in 02082026 |

Total recommended add: ~5,300-6,300 units of colours. Sales Analysis will refine quantities; this POS Check confirms the gaps exist.

**Recommended UK 02082026 place date:** **13 May (tomorrow) - hold to schedule.** If slips to 14-15 May still keeps arrival 6 Sep. Past 16 May arrival slips into late-Aug/early-Sep window when Liquipak Remove OOS risk crystallises — compounds rather than offsets.

### UK 03062026 + 02072026 (merged, arriving 15 Jul)

Combined contents inbound for STA + COM + ULT (784 + 2,800 + 1,848). At combined STA+COM substitution rate (43.9/d Shopify), 3,584 kits = 82d post-arrival cover. Healthy.

ACC-THA from merged container: 11,200 + already 22,538 on hand minus consumption through 15 Jul = comfortably covered.

**No additions needed** — container is locked, just needs balance + jar payment to ship together.

---

## LOCAL FILL STATUS

| Filler | Liquid | Status | Last Update | Next Action |
|---|---|---|---|---|
| **Chemence** | Base + Glow | 22-04-2026 PO blocked on Vik free-issue | Vik silent 14d (since 28/04) | Daniel/Remy escalate to Vik + cc Ldrury@chemence.com |
| **Oils4Life** | Heal | No active PO | Dale silent 21d+ | Remy outbound Dale - next Heal fill ~mid-late May for ~7 Aug landing |
| **Liquipak** | Remove 120ml/500ml | Final 800L PO landed earlier; replacement search paused | Daniel 7 May: search paused | Decision required by end-May |
| **Print Runner** | ACC-LAB-UK | No active PO | — | Remy place ~21-26 May at ~10,000 units |

---

## PO RECOMMENDATIONS

**Target: maintain 14-21d kit cover; trigger filling POs 60-80d before stockout.**

| SKU | Stock | DSR | Cover | Next Inbound | Action | Place By |
|---|---:|---:|---:|---|---|---|
| UK 02082026 (fill PO) | — | — | — | (none after) | **PLACE 13-15 MAY** (tomorrow). Add 5 OOS no-pipeline + 3 deep-stockout colours | **13 May** |
| ACC-LAB-UK | 5,309 | ~100 | 53d | 1,396 (B360 locked) | Print Runner PO ~10,000 units | **~21-26 May** |
| Heal fill (Oils4Life) | 6,958 | 80.1 | 87d | (none) | Outbound Dale to scope next fill | **This week** (lead-time enquiry only; not place yet) |
| Chemence 22-04-2026 ETA | — | — | — | 8,000 BAS + 6,000 GLO | Unblock Vik on free-issue | **This week** |

---

## STOCK SCENARIOS - DELAY MODELS

### Scenario A: UK 03062026/02072026 merged ships on time (15 Jul arrival)
- Kits: STA+COM substitution carries through to mid-Aug. ULT to mid-Aug.
- Colours: top sellers (Peachy/Sincere/Goddess/Bubbly) bridged via Sally express (user accepts). 5 no-pipeline colours unresolved until UK 02082026 (6 Sep) - 7-week colour-OOS window for these 5 specific SKUs.

### Scenario B: Balance/jar payment slips to end-May → arrival late-Jul / early-Aug
- Kits: still OK (STA+COM combined 85d cover).
- ACC-LAB-UK: at ~100/d, stocks out ~early Jul before Print Runner second cycle - place earlier (~mid-May).
- Colour express bridges balloon (Bubbly already on day 0; every week slip = 7d more express per top-seller SKU).

### Scenario C: 22-04-2026 Chemence stays blocked through May (Vik silent another 2 weeks)
- Base: 5,938 stock / 101.7 kit-adj = 58d → stocks out ~9 Jul without 22-04 fill.
- 22-04 Chemence at 17 Jun (sheet) → +1 wk transit = ~25 Jun arrival = OK.
- 22-04 Chemence slipped to mid-Jul completion → arrival ~25 Jul → **~16d gap on Base**.
- Bridge: Sally express on Base, or 03062026/02072026 brings 0 Base (zero in those containers).
- **Risk:** Base cover ties directly to unblocking Vik this week.

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (today)

- **Daniel: place UK 02082026 fill PO tomorrow (13 May)** with recommended +5,300-6,300 units of colours (per Container Gap Analysis above). Sales Analysis will refine.
- **Bubbly (POW-BUB-516) stocks out today** at 3 units. Add to next Sally express list immediately.
- **Joel: pay UK 03062026 balance + UK 02072026 jars** so single 40HQ ships before 18 May Sally completion deadline.
- **Daniel/Remy: chase Vik (Chemence) on 22-04-2026 free-issue** — cc Ldrury@chemence.com. Each week silent = Base risk grows.

### 🟡 WARNING (this week)

- **Remy: place Print Runner ACC-LAB-UK PO ~21-26 May** for 10,000 units. 14-21d local print lead.
- **Remy: outbound Dale (Oils4Life)** to scope next Heal fill timing - not place yet, but get on his radar.
- **Daniel: decide Liquipak Path A/B/C** by end-May (replacement vs accept Sep gap vs cross-region from CA).
- **Joel: B360 PACKUP £8,500 deposit pace conversation** - £1k/week pace = 8.5 weeks. 13 colour SKUs OOS because of locked stock.
- **POW-OVE-487, POW-FAI-308, POW-NOT-065** - confirm size in UK 02082026 fill PO (800-1,000 each).

### 🟢 MONITOR

- **POW-COT-030 (Cotton Candy)** - cleared off today's digest streak, verify it has actually restocked at Fulfillable.
- **POW-CRU-090, POW-JUS-449** - day 1 on today's digest. Confirm if listing issue vs genuine OOS.
- **Bond/Soak/Matte model DSRs** - still 2-3x Shopify rate per 5 May Recap. Greg refresh request stands but not blocking.

---

## CASCADING ARRIVAL PROJECTION

**Target cover: 45-75 days | Effective growth: 0.72x | Actual kit DSR: 78.1/d**

| Stage | Date | Kit Stock | Kit Cover @ Actual |
|---|---|---:|---:|
| **Now** (12 May) | — | 7,339 (STA 99 + COM 3,632 + ULT 3,608) | **94d** |
| **22-04 Chemence lands** (~25 Jun, 44d) | +44d | 7,339 - 3,436 + 0 = 3,903 (kits not in this fill) | **50d** |
| **UK 03062026+02072026 merged** (15 Jul, 64d) | +64d | 3,903 - 1,562 + 4,632 kits = 6,973 | **89d** |
| **UK 02082026** (6 Sep, 117d) | +117d | 6,973 - 4,141 (53d at 78.1) + 2,548 kits = 5,380 | **69d** |

Kit cover never drops below 50d through end-Aug. Healthy at actual rate. At 1.3x scaled (142/d) cover halves - reads tighter but still OK.

### IF UK 03062026/02072026 SLIPS TO END-JULY

- Kits drop to ~28d at stage 2 (still bridged via Complete-kit substitution).
- Bubbly, Train-Wreck, Sincere, Bare Necessity, Daydream all OOS through merge arrival.
- Sally express bridges grow proportionally with the slip.

---

## FOLLOW-UP ITEMS

**Immediate (this week):**
- [ ] Daniel: place UK 02082026 fill PO 13 May with colour additions (Sales Analysis sizing)
- [ ] Joel: pay UK 03062026 balance + UK 02072026 jars by 18 May
- [ ] Daniel/Remy: escalate Vik (Chemence) on 22-04 free-issue + cc Ldrury@chemence.com
- [ ] Add POW-BUB-516, POW-TRA-452, POW-BAR-198, POW-SIN-254, POW-DAY-025 to Sally express list
- [ ] Remy: outbound Dale (Oils4Life)

**By end of month:**
- [ ] Remy: place Print Runner ACC-LAB-UK PO ~21-26 May (10,000 units)
- [ ] Daniel: Liquipak Path A/B/C decision
- [ ] Joel: B360 PACKUP deposit pace conversation
- [ ] Roisin: 432 Base Sweden air-freight quote (ticket open since 4 May)

**Ongoing:**
- [ ] Watch Vik's reply timing on 22-04-2026 free-issue → drives Base cover scenario
- [ ] Watch 22-04 Chemence completion - sheet says 17 Jun, realistic 1 Jul, slip risk to mid-Jul
- [ ] Roisin export 14d Fulfillable deduction history (deferred this cycle, carry to next)
