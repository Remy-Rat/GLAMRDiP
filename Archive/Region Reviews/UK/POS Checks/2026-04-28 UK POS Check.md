# UK POS Model Check - 28 Apr 2026

## DATA FRESHNESS

- **POS MODEL UPDATED:** 28 Apr 2026 (today, Greg pasted AM)
- **3PL tab last valid:** 28 Apr 2026 (B360 tab — represents frozen B360 Packup stock, NOT live Fulfillable). Fulfillable stock is in POS MODEL col 7 only.
- **Shopify last:** 27 Apr 2026 (+1 day lag, normal)
- **Growth factor:** 1.3x (Greg refreshed from 1.1x since last review)
- **Kit DSR base:** STA=10, COM=32, ULT=42 → 84/day base × 1.3 = 109.2/day scaled
- **Actual 14d kit DSR:** 72.0/day → effective 0.86x growth → -34% vs scaled target

---

## MANUAL OVERRIDES APPLIED

User-confirmed deltas vs POS MODEL paste:

1. **LIQ-BAS-2 Chemence 10-03-2026 inbound: 7,568 (NOT 8,000).** 432 Base redirected to Nordic via Fulfillable transhipment per Daniel's 22 Apr Slack post. POS MODEL still shows 8,000 — Greg to update.
2. **UK 03062026: balance NOT paid; ship-out ~4 May.** POS MODEL says est. completion 28 Apr / arrival 22 Jun. Production complete but balance pending; arrival likely sticks at 22 Jun ± 2-3d (transit ~50d).
3. **UK 02082026 fill PO place date: pushed from 29 Apr to ~13 May.** Two-week slip. Cascades: est. completion ~5 Jul, est. arrival ~30 Aug. POS MODEL still shows old 22 Jun completion / 16 Aug arrival.
4. **B360 Packup: deposit being paid £1k/week of £8,500 total.** ~8.5 weeks at this pace. **Treat all 288,898 Packup units as frozen and unavailable through end of June.**
5. **LIQ-SEN-2 and LIQ-SEN-4: discontinued in UK** (per memory). 0 stock is correct, no flag.

---

## STOCK POSITION — UK — 28 Apr 2026

Fulfillable stock only. POS MODEL projected DSR (1.3x scaled) vs actual (kit-adjusted Shopify for kit-driven SKUs; standalone Shopify for non-kit liquids; deduction-derived for inserts).

```
SKU              Stock   Proj DSR  Cov(Proj)  Actual DSR  Cov(Actual)  Flag
--- KITS ---
KIT-STA-2          223      13.0      17d        10.7         21d      WARNING
KIT-COM-4        4,150      41.6     100d        23.3        178d      OK (fast)
KIT-ULT-6        4,092      54.6      75d        38.0        108d      OK

--- KIT-ADJUSTED LIQUIDS (Heal/Base/Glow + ACC-INS picked per kit) ---
LIQ-HEA-5        8,592     110.5      78d        72.6        118d      OK
LIQ-BAS-2          242     135.2       2d        95.4*         3d      🔴 CRITICAL
LIQ-GLO-4          460     122.2       4d        79.4*         6d      🔴 CRITICAL
ACC-INS          9,411      90.5     104d        72.0^       131d      OK

--- STANDALONE LIQUIDS (pre-packed in CN kits, only standalone Shopify drains) ---
LIQ-SEA-3        2,966      15.6     190d         9.5        312d      OK
LIQ-BON-1          596       6.5      92d         2.4        248d      OK
LIQ-SOA-6          616       6.5      95d         1.4        440d      OK

--- REMOVE PRODUCTS (standalone + bundles) ---
ACC-REM          1,861      39.0      48d        17.6        106d      OK
ACC-REM-500      4,549      36.4     125d         9.4        484d      OK (overstock)
ACC-REM-BOW     5,278      31.2     169d         1.7      3,105d     🟡 OVERSTOCK

--- INSERTS / LABELS (per-order at Fulfillable) ---
ACC-LAB-UK       7,534     217.1      35d       ~140^         54d      🟡 WATCH
ACC-THA         24,762     114.0     217d       ~140^        177d      OK
```

\* Kit-adjusted: standalone Shopify (23.4/d Base, 7.4/d Glow) + scaled kit DSR (72.0/d). Per Component Map UK config.
^ Estimated from kit-adj kit total (72/d) + standalone where applicable. 3PL deductions unavailable in B360 tab post-transition.

---

## STEP 0a — GMAIL & SLACK RECONCILE (since POS MODEL paste 28 Apr AM)

- **28 Apr 02:44** — Remy chased Viktorija (Chemence) for ETA on 22-04-2026 PO. No reply yet.
- **28 Apr (today, user-confirmed)** — LIQ-BAS-2 inbound = 7,568 (not 8,000 in sheet). Chemence dispatching today UK time.
- **No other 3PL operational events between paste and now.**

POS MODEL is fresh. The only override post-paste is the Base 7,568 quantity.

---

## STEP 0b — GROWTH FACTOR HEALTH CHECK

| Metric | Value |
|---|---|
| POS MODEL growth factor | 1.3x |
| Base kit DSR | 84/day |
| Scaled kit target | 109.2/day |
| Actual 14d kit DSR | 72.0/day |
| Effective actual growth | 0.86x |
| Gap vs target | -34.1% |
| Recommended (actual + 10%) | 0.94x |

**Read:** Greg's 1.3x refresh outpaces real velocity. UK was the healthiest region at 1.07-1.08x actual on 14 Apr — actual has now fallen to 0.86x post-transition. **W17 was the worst kit week in 8 weeks (63/d, -42% vs scaled).** Gap is widening.

**Action:** Don't lower the growth factor outright (aspirational, ad spend driven). But future container quantities should be sized against the 0.86x reality, not 1.3x. Otherwise overstock will accumulate.

---

## STEP 0c — KIT-ADJUSTED DSR VALIDATION

UK Component Map: Heal, Base, Glow, ACC-INS are kit-adjusted (filled / picked locally per kit). Other liquids are standalone.

| SKU | Model DSR (1.3x) | Standalone Shop 14d | Implied kit consumption | Conclusion |
|---|---:|---:|---:|---|
| LIQ-HEA-5 | 110.5 | 0.6 | 109.9 | Model = standalone + scaled kit (1.3x). **Kit-adjusted built in. ✅** |
| LIQ-BAS-2 | 135.2 | 23.4 | 111.8 | Model = 23.4 standalone + ~112 kit. **Kit-adjusted built in. ✅ Greg has updated.** |
| LIQ-GLO-4 | 122.2 | 7.4 | 114.8 | Model = 7.4 standalone + ~115 kit. **Kit-adjusted built in. ✅ Greg has updated.** |
| ACC-INS | 90.5 | 0 | 90.5 | Per-kit only. **Kit-adjusted built in. ✅** |

**Significant change since 21 Apr Recap:** Greg has refreshed POS MODEL DSR for Base + Glow to kit-adjusted figures. The 22 vs 90 / 11 vs 95 understatement flagged in the 14 Apr POS Check is fixed. Carry forward the actual kit-adjusted rates of ~95.4 Base / ~79.4 Glow as the operational rate (real velocity is below model).

---

## STOCK-OUT FORECAST

### 🔴 STOCKOUT BEFORE ARRIVAL

| SKU | Stock | Actual DSR | Stocks Out | Next Inbound | Arrives | Gap |
|---|---:|---:|---|---|---|---:|
| LIQ-BAS-2 | 242 | 95.4/d | ~30 Apr | Chemence 7,568 | 30 Apr | **0d** (arrives just in time) |
| LIQ-GLO-4 | 460 | 79.4/d | ~3 May | Chemence 8,000 | 30 Apr | +3d |
| KIT-STA-2 | 223 | 10.7/d | ~19 May | UK 03062026 +448 | 22 Jun | **-34d gap** |
| POW-CRU-090 (Crush) | 40 | 8.7/d | 02 May | UK 03062026 +200 | 22 Jun | -51d |
| POW-OVE-487 (Over It) | 60 | 7.4/d | 06 May | nothing on order | — | express only |
| POW-JUS-449 (Just Friends) | 31 | 8.4/d | 01 May | UK 02082026 +200 | 30 Aug* | -120d* |
| POW-PEA-068 (Peachy) | 141 | 13.3/d | 08 May | UK 03062026 +1,200 | 22 Jun | -45d |
| POW-GOD-017 (Goddess) | 79 | 6.6/d | 09 May | UK 03062026 +400 | 22 Jun | -44d |
| POW-BUB-516 (Bubbly) | 79 | 6.3/d | 10 May | UK 03062026 +400 | 22 Jun | -43d |
| POW-FAI-308 (Fairytale) | 84 | 5.8/d | 12 May | nothing on order | — | past local fill deadline |
| POW-NOT-065 (Not 2day) | 87 | 5.8/d | 13 May | nothing on order | — | past local fill deadline |
| POW-TRA-452 (Train-Wreck) | 282 | 16.9/d | 14 May | UK 03062026 +800 | 22 Jun | -39d |
| POW-SEA-450 (Seaside) | 93 | 5.2/d | 15 May | UK 02082026 +200 | 30 Aug* | -107d* |
| POW-DAY-025 (Daydream) | 94 | 5.1/d | 16 May | UK 02082026 +200 | 30 Aug* | -106d* |
| POW-SIN-254 (Sincere) | 200 | 9.9/d | 18 May | UK 03062026 +800 | 22 Jun | -35d |

\* Updated arrival ~30 Aug factoring 13 May fill PO place + ~3.5 month CN production / shipping cycle.

### 🟡 TIGHT (0-7d margin)

| SKU | Stock | Actual DSR | Stocks Out | Inbound | Arrives | Gap |
|---|---:|---:|---|---|---|---:|
| POW-RID-661 (Ride or Diamonds) | 319 | 4.1/d | 14 Jul | UK 02072026 +200 | 12 Jul | +2d |

### 🔴 NOTHING ON ORDER

| SKU | Stock | Actual DSR | Stocks Out | Status |
|---|---:|---:|---|---|
| ACC-LAB-UK | 7,534 | ~140/d | ~1 Jun | **Print Runner PO needed by ~10 May** (14-21d local print lead) |
| POW-OVE-487 (Over It) | 60 | 7.4/d | 06 May | Past CN PO deadline. **Express only.** |
| POW-FAI-308 (Fairytale) | 84 | 5.8/d | 12 May | Past local fill deadline |
| POW-NOT-065 (Not 2day) | 87 | 5.8/d | 13 May | Past local fill deadline |
| POW-COS-012 (Cosmic) | 129 | 3.8/d | 31 May | Past CN PO deadline |
| POW-IMA-264 (Imagine That) | 142 | 2.6/d | 21 Jun | Past CN PO deadline |
| POW-SLO-192 (Slow Burn) | 392 | 10.4/d | 04 Jun | Past CN PO deadline |
| POW-MIL-193 (Milky Way) | 132 | 3.2/d | 08 Jun | Past CN PO deadline |
| POW-BOY-610 (Boy Bye) | 138 | 3.2/d | 10 Jun | Past CN PO deadline |
| POW-MAR-009 (Marshmallow) | 131 | 3.6/d | 03 Jun | Past CN PO deadline |
| POW-HEL-387 (Hello Sunshine) | 132 | 3.7/d | 02 Jun | Past CN PO deadline |
| POW-SUN-394 (Sunflower) | 140 | 2.9/d | 15 Jun | Past CN PO deadline |
| POW-GOO-208 (Good Morning) | 288 | 5.9/d | 15 Jun | Past CN PO deadline |
| POW-LAC-196 (Lace) | 145 | 2.4/d | 27 Jun | Past CN PO deadline |
| POW-CRE-217 (Creme Brulee) | 313 | 4.5/d | 06 Jul | Past CN PO deadline |
| POW-PER-229 (Persuasion) | 156 | 2.2/d | 07 Jul | Past CN PO deadline |

**Plus 31 colours formally OOS** (POS MODEL sheet count; 11 in "Specific Sale Deductions" alternate count). Top-sellers Sincere and Peachy are about to join.

---

## CONTAINER / ORDER STATUS

### UK 03062026 (in production, ship-out ~4 May per user)
- POS MODEL: In Production, est. completion 28 Apr, est. arrival 22 Jun
- Reality: production complete, **balance unpaid**, ship-out delayed to ~4 May
- ETA arrival likely sticks at **22 Jun ± 2-3 days** (sea transit dominates)
- Brings: 448 STA, 1,484 COM, 700 ULT, 5,600 ACC-THA, plus Powder Room colours
- **Action: Joel pay balance this week. Each day delays the May/Jun cover backstop.**

### UK 02072026 — Birthday Sale (in production)
- POS MODEL: In Production, est. completion 18 May, est. arrival 12 Jul
- Brings: 336 STA, 1,316 COM, 1,148 ULT, 5,600 ACC-THA, 1,680 ACC-INS, plus colours
- Deposit paid (14 Apr). On track. Growth factor TBD.

### UK 02082026 (fill PO placement now ~13 May per user)
- POS MODEL: completion 22 Jun / arrival 16 Aug — **stale**, won't update until placed
- Reality post-13 May placement: completion ~5 Jul, arrival **~30 Aug** (2-week slip)
- Brings: 560 STA, 1,148 COM, 840 ULT, 4,080 ACC-INS, 11,200 ACC-THA, plus colours
- ACC-LAB-UK: 0 (Print Runner local — correct)
- **No Base / Glow / Heal in container** (all UK liquids sourced locally — correct)

### UK Powder Room AND Chemence (arriving 30 Apr — TOMORROW)
- POS MODEL: Completed, arrives 30 Apr
- Contents: 7,568 Base (override) + 8,000 Glow + Powder Room colours + 30 Powder Room kit colours per kit
- This is the cycle-defining event. Confirm landing tomorrow with Roisin / Ben.

### 22-04-2026 Chemence (next fill)
- POS MODEL: Ordering, est. completion 17 Jun (60-day from placement)
- Contents: 8,000 Base + 6,000 Glow
- ETA chase pending — Remy emailed Vik 28 Apr AM

### B360 PACKUP STOCK (frozen)
- **Treat as fully unavailable through end of June.** £1k/week deposit pace = ~8.5 weeks to fund the £8,500 stock-out deposit before transfer can begin.
- Locked: ~493 STA, 40 COM, 1,653 Heal, 7,349 ACC-INS, 5,246 ACC-THA, 19,445 STO-BUB-BAG-S, 1,396 ACC-LAB-UK, plus 45 OOS colour SKUs and significant inserts.

---

## LOCAL FILL STATUS

### Chemence — 10-03-2026 (Base + Glow)
- Status: **Dispatching today UK time** (user-confirmed)
- 7,568 Base + 8,000 Glow → Fulfillable ~30 Apr. Delivers Base/Glow from CRITICAL into ~80-100d cover.
- 432 Base for Nordic transhipment routes via Fulfillable.

### Chemence — 22-04-2026 (next)
- Status: Ordering. Vik chased 28 Apr for ETA. 60-day target → ~17 Jun completion.
- 8,000 Base + 6,000 Glow.
- Lead time: 6-8 weeks at 8k qty (Vik confirmed 13 Apr).

### Oils4Life — Heal
- No PO active. Last fill 25-02-2026 direct to Fulfillable. Heal at 8,592 / 118d kit-adjusted = healthy.
- **No urgency.** Next placement ~2-3 weeks out (target 60-90d post-fill cover).

### Liquipak — Remove (EXITING)
- Final PO 02-04-2026 placed; payment receipt 9 Apr.
- ~160d Remove cover from final fill. OOS scenario: early Sep if no replacement.
- **No replacement filler found in 7+ weeks.** Stalled.

---

## PACKAGING & INSERTS

3PL deduction view unavailable (B360 tab is frozen Packup, not Fulfillable live). Estimated rates from POS MODEL projections:

| SKU | Fulfillable | Proj DSR | Days Cover | Notes |
|---|---:|---:|---:|---|
| ACC-LAB-UK | 7,534 | ~140/d | 54d | **Print Runner PO needed by ~10 May** |
| ACC-INS | 9,411 | ~72/d | 131d | OK |
| ACC-THA | 24,762 | ~140/d | 177d | OK |
| STO-BUB-BAG-L | unknown | per kit | ? | Confirm with Fulfillable on next ShipHero export |
| STO-BUB-BAG-S | unknown (19,445 frozen at B360) | low | ? | OK once packup freed |
| STO-MAI-2 | unknown | low | ? | OK |

**Action:** Request Fulfillable export of current packaging stock + 14-day deduction history via Roisin.

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (act today)

1. **LIQ-BAS-2 + LIQ-GLO-4** — 2-3d cover. Confirm Chemence dispatch went out today and lands tomorrow. **If delayed even 24h, Base goes OOS for kits.** This is the highest-stakes item this cycle.
2. **Joel pay UK 03062026 balance.** Every day = mid-Jun cover slipping further. 22 Jun arrival isn't holding until balance is cleared.
3. **POW-OVE-487 (Over It): 60 units, 8d cover, nothing on order.** Express PO or skip launch from rotation.

### 🟡 WARNING (act this week)

4. **KIT-STA-2 — 17d cover (Fulfillable only).** Stocks out ~19 May. UK 03062026 brings 448 but lands 22 Jun = **5-week STA gap**. Options: (a) substitute COM (4,150 / 100d) for STA orders during gap; (b) push 22-04-2026 Chemence + Sally on STA-only express; (c) accept temporary OOS.
5. **ACC-LAB-UK — 7,534 / 54d / no inbound.** Place Print Runner PO by ~10 May. Recommended ~10,000 units (matches 22-04-2026 Chemence + UK 02072026 cycle through Aug).
6. **Place UK 02082026 fill PO** — target now 13 May per user (was 29 Apr).
7. **Top-seller colours stocking out before UK 03062026:** Peachy (8 May), Goddess (9 May), Bubbly (10 May), Train-Wreck (14 May), Sincere (18 May). 6-7 week OOS gap on top sellers. Express via Sally or accept gap.
8. **15+ colours past CN PO deadline with nothing on order** — formally accept these will OOS through May/June or place express. List in WHAT NEEDS ACTION below.

### 🟢 MONITOR (FYI)

9. **Heal at 118d cover** — no action needed for ~6-8 weeks.
10. **22-04-2026 Chemence ETA** — chase Vik if no reply by Thu.
11. **B360 Packup deposit pace** — at £1k/week, 8.5 weeks to fund. Worth a conversation with Joel about accelerating if any of the 493 STA / 7,349 ACC-INS / 19,445 STO-BUB-BAG-S start to bite.
12. **W17 kit DSR drop to 63/d (-42%)** — biggest dent in 8 weeks. Discussed in Sales Analysis.
13. **ACC-REM-BOW: 5,278 / 3,105d cover** — substantial overstock. Don't include in any container until late 2026.

---

## CASCADING ARRIVAL PROJECTION (kits)

Target: 45-75d cover. Actual kit DSR: 72/d (STA 10.7 + COM 23.3 + ULT 38.0).

| | NOW | After Powder Room+Chem (30 Apr) | After UK 03062026 (22 Jun) | After UK 02072026 (12 Jul) |
|---|---:|---:|---:|---:|
| KIT-STA-2 | 223 / 21d | 223 / 21d | 110 / 10d* | 446 / 42d |
| KIT-COM-4 | 4,150 / 178d | 4,150 / 178d | 4,418 / 190d | 4,768 / 205d |
| KIT-ULT-6 | 4,092 / 108d | 4,092 / 108d | 2,732 / 72d | 2,832 / 75d |
| **All kits** | 7,108 ~/100d | 7,108 ~/100d | 7,260 / 100d | 8,046 / 112d |

\* STA stocks out ~19 May. By 22 Jun arrival, STA = 0 + 448 - (consumption from out-of-stock period... realistically 0) = 448 then drains again. Reality: STA goes OOS for ~5 weeks, customers default to COM/ULT.

**Read:** kit total cover stays >100d throughout. The mix is the problem — STA gap and ULT slow drain.

### IF UK 03062026 SHIPS OUT 4 MAY (per user) AND ARRIVAL HOLDS AT 22 JUN

- STA gap exactly as modelled above (~5 weeks).
- COM and ULT untouched.
- **No marginal worsening from balance delay vs sheet.** The risk is if balance delays further → 4 May becomes 11 May → arrival slips to ~29 Jun → STA gap extends to 6 weeks.

### IF UK 03062026 ARRIVAL SLIPS TO 5 JUL

- STA OOS gap: ~7 weeks
- ULT: 4,092 - 7×38 = 4,092 - 1,862 = 2,230 / 59d at arrival. Still OK.
- COM: 4,150 - 7×23 = 3,989 / 172d. Plenty.
- Liquids unaffected (Chemence on next 22-04 cycle).

---

## PO RECOMMENDATIONS

| SKU | Stock | Actual DSR | Cover | Action | Place By |
|---|---:|---:|---:|---|---|
| ACC-LAB-UK | 7,534 | ~140/d | 54d | Print Runner PO ~10,000 units | **~10 May** |
| KIT-STA-2 | 223 | 10.7/d | 21d | Express via Sally (next CN order) OR accept ~5wk gap | **decide this week** |
| Chemence next (post 22-04-2026) | — | — | — | Place 3rd Chemence PO ~6 weeks before 22-04 lands (~5 May) | **early May** |

---

## FOLLOW-UP ITEMS

**Immediate (today/tomorrow):**
- [ ] Confirm Chemence dispatch out today UK time and tracking visibility for 30 Apr arrival
- [ ] Joel pay UK 03062026 balance
- [ ] Roisin: confirm Fulfillable received and booked in 30 Apr Chemence delivery (Base 7,568 + Glow 8,000)

**By end of this week:**
- [ ] Decide STA gap strategy (substitute, express, accept)
- [ ] Decide on Print Runner PO size + timing for ACC-LAB-UK
- [ ] Vik reply chase on 22-04-2026 Chemence ETA

**Ongoing:**
- [ ] B360 Packup deposit pace conversation with Joel
- [ ] Liquipak replacement decision (accept ~20% uplift or keep searching)
- [ ] Greg: refresh POS MODEL to reflect 7,568 Base on 30 Apr Chemence shipment
- [ ] Greg: refresh POS MODEL UK 02082026 dates after 13 May placement
