# 🇬🇧 UK POS Model Check — 26 May 2026

## Data Freshness

- **POS MODEL `UPDATED` cell**: empty (Greg paste-discipline issue — 4th cycle). Assume today's xlsx is current.
- **Shopify**: latest 2026-05-25 (+1 day lag normal).
- **3PL tab (B360)**: last valid 2026-05-26. **BUT — extract shows zero 14-day deduction movement** (first_stock == latest_stock across the board). Continues the 4-cycle Fulfillable deduction-integrity blind documented in [[shiphero-inventory-changes-cap]]. The B360 tab is frozen Packup; Fulfillable's ShipHero feed needs cursor pagination before deductions can be read. **Operational DSR for this POS Check = Shopify 14d (+ kit consumption for kit-adjusted items).**
- **Growth factor**: 1.3x. Kit base 84/d → scaled 109.2/d. W21 day-1 = 137/d (+25% over). Shopify 14d kit total = 107.8/d ≈ on model.

## Manual Overrides Applied (cascade through all downstream math)

| SKU | Sheet value | Override | Source |
|---|---|---|---|
| Powder Room + Chemence 24-03-2026 stock | "Completed" inbound block (10,000 ACC-LAB + 7,568 BAS + 8,000 GLO + 12 colours) | **Now on-hand at Fulfillable** (booked in 19 May per Daniel Slack reply) | Daniel 19 May Slack |
| B360 PACKUP STOCK | Live inbound (493 KIT-STA-2, 1,653 LIQ-HEA-5, 19,445 STO-BUB-BAG-S, 17 OOS colour packups, etc.) | **DO NOT count as guaranteed inbound** — Joel paid £8,500 deposit 14 May but stockout BALANCE not confirmed paid (only deposit allocated per Mason 15 May "your GBP wallet"). | User confirmed 26 May |
| ACC-REM (120ml) operational DSR | Shop 14d = 4.8/d standalone | **Combined = 4.8 standalone + ACC-REM-BUN-1 49.4/d = 54.2/d** (each bundle pulls 1x ACC-REM) | Component Map |
| ACC-REM-BOW operational DSR | Shop 14d = 0.5/d standalone | **Combined = 0.5 + 49.4 (ACC-REM-BUN-1) = 49.9/d** | Component Map |
| LIQ-SEN-2, LIQ-SEN-4 | DSR 8/d, 8/d | **Excluded from action lists — discontinued in UK** | [[uk-discontinued-liquids]] |
| ACC-LAB-UK | Container OL flagged | **Locally printed by Print Runner only** — never flag for CN container space | Region/UK.md |

---

## 1. Stock Position — Headline Table

Cover at operational DSR (= Shopify 14d, or kit-adjusted/bundle-adjusted where noted).

### Kits
| SKU | On Hand | Model DSR | Shop 14d | Op DSR | Cover @ Op | Flag |
|---|---|---|---|---|---|---|
| KIT-STA-2 | 20 | 13.0 | 6.0 | 6.0 | **3.3d** | 🔴 CRITICAL |
| KIT-COM-4 | 2,740 | 41.6 | 63.9 | 63.9 | 42.9d | 🟢 |
| KIT-ULT-6 | 3,074 | 54.6 | 37.9 | 37.9 | 81.1d | 🟢 |

Kit total Shopify 14d = 107.8/d (vs 109.2/d scaled = on target). Mix shifted: STA -60% / COM +54% / ULT -31% vs model — automatic Shopify-flow substitution confirmed working.

### Kit-adjusted liquids (op = standalone Shop 14d + kit consumption per Component Map)
| SKU | On Hand | Model DSR | Shop 14d standalone | Kit consumption | Op DSR | Cover @ Op | Flag |
|---|---|---|---|---|---|---|---|
| LIQ-HEA-5 (Heal) | 5,412 | 110.5 | 1.4 | +109.2 | 110.6 | 48.9d | 🟢 |
| LIQ-BAS-2 (Base) | 4,132 | 135.2 | 18.9 | +109.2 | 128.1 | 32.3d | 🟢 |
| LIQ-GLO-4 (Glow) | 5,546 | 122.2 | 9.1 | +109.2 | 118.3 | 46.9d | 🟢 |
| ACC-INS | 6,797 | 106.6 | n/a | 109.2 | 109.2 | 62.2d | 🟢 |

### Other liquids (standalone Shopify only — pre-packed in kits from CN)
| SKU | On Hand | Shop 14d | Cover | Flag |
|---|---|---|---|---|
| LIQ-BON-1 | 493 | 3.2 | 154d | 🟢 |
| LIQ-MAT-4 | 749 | 2.1 | 357d | 🟢 |
| LIQ-SEA-3 | 2,557 | 11.5 | 222d | 🟢 |
| LIQ-SOA-6 | 552 | 1.5 | 368d | 🟢 |

### Remove products (bundle-adjusted)
| SKU | On Hand | Standalone Shop 14d | Bundle pull | Op DSR | Cover @ Op | Flag |
|---|---|---|---|---|---|---|
| ACC-REM (120ml) | 593 | 4.8 | +49.4 (BUN-1) | **54.2** | **10.9d** | 🟡 WARNING |
| ACC-REM-500 | 3,797 | 22.5 | 0 | 22.5 | 169d | 🟢 |
| ACC-REM-BOW | 3,827 | 0.5 | +49.4 (BUN-1) | 49.9 | 77d | 🟢 |
| ACC-REM-BUN-1 (Shopify bundle) | n/a | 49.4 | n/a | n/a | n/a | |

### Inserts / packaging / labels
| SKU | On Hand | Op DSR | Cover | Flag |
|---|---|---|---|---|
| ACC-LAB-UK (locally printed) | 2,688 | 217.1 | **12.4d** | 🟡 WARNING |
| ACC-THA | 19,916 | 181.7 | 110d | 🟢 |
| STO-MAI-2 | 6,706 | 74.0 | 91d | 🟢 |
| STO-MAI-BAG-S | 9,042 | 74.0 | 122d | 🟢 |
| STO-BUB-BAG-L | 9,504 | 106.6 | 89d | 🟢 |
| STO-BUB-BAG-S | 0 | n/a (Fulfillable supplies) | n/a | (per [[uk-fulfillable-liquid-pocket]]) |

---

## 2. Container / Order Status

| Reference | Est. Completion | Est. Arrival | Status | Notes |
|---|---|---|---|---|
| B360 PACKUP STOCK | n/a | n/a | In Production | **Stockout BALANCE unpaid by Joel** — 288k units stranded incl. 17 OOS colour packups, 493 KIT-STA-2, 19,445 STO-BUB-BAG-S, etc. |
| UK Powder Room + Chemence (PO 9 / 24-03-2026) | 2026-05-14 | 2026-05-14 | Completed | **Booked in at Fulfillable 19 May** (Daniel via Roisin). Now on-hand. |
| 22-04-2026 Chemence (LIQ-BAS-2 + LIQ-GLO-4) | — | 2026-06-17 (sheet) | Ordering | **Vik 28 days silent.** Daniel 29 Apr free-issue tracker un-reconciled. Remy chase-email 19 May, no reply. |
| UK 03062026 | 2026-05-21 | **2026-07-15** | On the Way | Consolidated 40HQ with UK 02072026 (per user 19 May, 03062026 balance paid). Carries 448 STA + 1,484 COM + 700 ULT + colours. |
| UK 02072026 | 2026-05-21 | **2026-07-15** | On the Way | Same 40HQ. 336 STA + 1,316 COM + 1,148 ULT + 1,680 ACC-INS + 5,600 ACC-THA. |
| UK 02082026 | 2026-07-13 | 2026-09-06 | **PO place ~27 May (tomorrow)** | 560 STA + 1,148 COM + 840 ULT + 4,080 ACC-INS + 11,200 ACC-THA + colours. **ULT at 840 looks light vs 37.9/d Shopify** (22d post-arrival cover only). |
| Container 7 / 8 / 9 (unnamed) | Aug-Sep | Oct-Nov | Planned | No SKU OLs yet visible. |

---

## 3. Local Fill Status

| Filler | PO | Status | Contents | Risk |
|---|---|---|---|---|
| **Chemence (Vik)** | 22-04-2026 | Ordering | 8,000 LIQ-BAS-2 + 6,000 LIQ-GLO-4 | 🔴 Vik silent 28 days. Sheet ETA 17 Jun unconfirmed. Cycle 6-8w. Free-issue bottles/caps/brushes tracker open since 29 Apr. |
| **Liquipak** | 02-04-2026 (final) | Goods ready | ~4,000 ACC-REM (120ml) + 4,000 ACC-REM-500 | 🔴 **22 May payment deadline missed.** 7d transit once paid. ACC-REM cover **10.9d** at bundle-adjusted rate — every day's delay shrinks the margin. Final Liquipak fill ever. |
| **Oils4Life (Dale)** | — | No active PO | Heal | 🟢 12,370 bottles + 830 lids buffer confirmed by Dale 20 May email. Next fill timing not yet placed. |

---

## 4. Stock-Out Forecast

### 🔴 STOCKOUT BEFORE ARRIVAL (negative gap to first confirmed inbound)

| SKU | OH | Op DSR | Stocks Out | Next Inbound | Gap | Note |
|---|---|---|---|---|---|---|
| KIT-STA-2 | 20 | 6.0 | **3.3d (~29 May)** | UK 03062026 (448 STA, 15 Jul) | **-47d** | Powder Room/Chemence had 0 STA. B360 packup has 493 STA — only releases if Joel pays balance. Substitution to COM is the only bridge. |
| KIT-COM-4 | 2,740 | 63.9 | 42.9d (~8 Jul) | UK 03062026 (1,484 COM, 15 Jul) | **-7d** | Tight. STA→COM substitution increases COM draw rate; risk grows if surge holds. |
| ACC-REM (120ml) | 593 | 54.2 | **10.9d (~6 Jun)** | Liquipak final fill (~4,000, 7d post-payment) | depends on Joel | If Joel pays today: lands ~2 Jun, safe. If paid +7d: lands ~9 Jun, 3d gap. |
| ACC-LAB-UK | 2,688 | 217.1 | **12.4d (~7 Jun)** | Print Runner PO (10,000?, 14-21d post-payment) | depends on Joel | If Joel pays today: lands 9-16 Jun, 2-9d gap. If +7d delay: 9-16d gap. |
| 17 OOS colour packups (POW-CRE-217, POW-BLO-042, etc.) | 0 | varies | OOS NOW | B360 packup release OR UK 03062026 (15 Jul) | varies | See colour list below. |

### 🟡 OOS COLOURS WITH ACTIVE DEMAND (≥5/d Shopify, on_hand = 0)

12 colours selling at ≥5/d that are stocked out today:

| SKU | Shop 14d | Likely path |
|---|---|---|
| POW-SLO-192 | 15.6/d | B360 packup |
| POW-MON-005 | 14.1/d | B360 packup |
| POW-BAR-198 | 13.0/d | B360 packup |
| POW-LAC-196 | 7.6/d | B360 packup |
| POW-PER-229 | 7.1/d | B360 packup |
| POW-GAM-339 | 6.8/d | B360 packup |
| POW-SHH-013 | 6.3/d | B360 packup |
| POW-HEL-387 | 6.1/d | B360 packup |
| POW-KIN-642 | 6.1/d | B360 packup |
| POW-SIN-254 | 6.1/d | B360 packup |
| UK/EU-POW-POW-F17 (Powdered Sky) | 5.2/d | B360 packup OR UK 03062026 |
| UK/EU-POW-BAL-521 | 5.1/d | UK 03062026 |

**All of these clear automatically if Joel pays the B360 stockout balance and the 5-SKU release goes through.** Otherwise OOS until UK 03062026 lands 15 Jul.

### 🟡 WARNING (7-14d cover, but inbound landing well after)
- ACC-LAB-UK 12.4d cover — see above. Print Runner 14-21d lead, gap risk if Joel >5d to pay.
- POW-CRE-217 102u / 10.1/d = 10.1d — in B360 5-SKU release list.
- POW-BUT-098 45u / 4.3/d = 10.5d.
- POW-RID-661 108u / 9.1/d = 11.9d.
- POW-PUM-398 61u / 4.9/d = 12.4d.

### 🟢 SAFE (gap > 7d or healthy cover)
- All kit-adjusted liquids (HEA, BAS, GLO, INS) — Chemence fill provides bridge to UK 03062026 IF Vik delivers 17 Jun.
- LIQ-SEA-3, LIQ-BON-1, LIQ-SOA-6, LIQ-MAT-4 — 150d+ cover.
- ACC-THA, STO-MAI-*, STO-BUB-BAG-L — 80-122d cover.
- ACC-REM-500, ACC-REM-BOW — 77-168d cover.
- KIT-ULT-6 — 81d cover, next inbound 15 Jul gap +31d.

---

## 5. Container Gap Analysis

### UK 03062026 + UK 02072026 (consolidated, lands 15 Jul)

Containers carry adequate kit allocation to bridge to UK 02082026 (6 Sep) **IF** B360 packup releases. Without B360:

- **KIT-STA-2 at +50d**: starts 20, burns 6.0/d × 50 = 300 → need 280. UK 03062026 brings 448 → post-arrival 168 = 28d cover at 6.0/d. Then UK 02082026 brings 560 = 93d at 6.0/d. **OK as long as STA→COM substitution rate doesn't increase.**
- **KIT-COM-4 at +50d**: starts 2,740, burns 63.9 × 50 = 3,195 → -455. UK 03062026 brings 1,484 → 1,029. Then UK 02082026 brings 1,148 at +103d = -3,447 burn → -3,418. **Goes deeply negative by Sep 6** at current Shopify 14d rate.
- **LIQ-BAS-2 / LIQ-GLO-4**: -2,241 / +227 at 15 Jul (kit-adjusted at 128/d, 118/d). Goes more negative by Sep without Chemence fill 17 Jun.

### UK 02082026 (place tomorrow) — gaps to flag

Manifest in sheet: 560 STA + 1,148 COM + 840 ULT + 4,080 ACC-INS + 11,200 ACC-THA + colours.

- **KIT-ULT-6 at 840 looks light**: 37.9/d Shopify 14d → 22d post-arrival cover only. Next container after 02082026 is Oct/Nov. **Recommend bumping to 1,400-1,800.**
- **KIT-COM-4 at 1,148**: 63.9/d × 30d-to-next-container target = 1,917 minimum. **Bump to ~2,000-2,500.**
- **No ACC-REM / ACC-REM-500**: Liquipak exits permanently after current fill. Either (a) place replacement filler decision NOW (Daniel Path A/B/C — 13d stalled), or (b) consider adding ACC-REM-500 to UK 02082026 as a hedge.
- **No Chemence-supplied Base/Glow/Seal** (per region setup — these are local fills). Confirm Chemence pipeline can cover the post-02082026 window.

---

## 6. Cascading Arrival Projection (kits, two scenarios)

### Scenario A — WITHOUT B360 packup release (current state)

| SKU | NOW | After UK 03062026/02072026 (15 Jul) | After UK 02082026 (6 Sep) |
|---|---|---|---|
| KIT-STA-2 | 20 / 3d | 168 / 28d | 728 / 121d |
| KIT-COM-4 | 2,740 / 43d | 1,029 / 16d | **-2,299 / NEG** |
| KIT-ULT-6 | 3,074 / 81d | 1,879 / 50d | -867 / NEG... |
| LIQ-HEA-5 | 5,412 / 49d | -118 / OOS | -5,980 / NEG |
| LIQ-BAS-2 | 4,132 / 32d | -2,273 / OOS | -9,062 / NEG |
| LIQ-GLO-4 | 5,546 / 47d | -369 / OOS | -6,639 / NEG |

**Major kit liquid gap forms by mid-Jul without Chemence fill landing on time.**

### Scenario B — WITH B360 packup release (if Joel pays balance + 5 SKUs collected)

| SKU | NOW | After UK 03062026/02072026 (15 Jul) | After UK 02082026 (6 Sep) |
|---|---|---|---|
| KIT-STA-2 | 20 + 493 packup = 513 / 86d | 997 / 166d | 1,239 / 207d |
| KIT-COM-4 | 2,740 + 40 = 2,780 / 44d | 1,069 / 17d | -2,259 / NEG |
| LIQ-HEA-5 | 5,412 + 1,653 = 7,065 / 64d | 1,535 / 14d | -4,327 / NEG |

B360 release helps STA + Heal materially. COM gap persists either way → **Sales Analysis should confirm whether the +54% Shopify COM rate is structural or driven by the temporary STA shortage**. If COM normalises back to 40/d as STA refills, the gap shrinks. If COM holds at 63.9, UK 02082026 sizing must change.

---

## 7. Local Fill Sizing — Recommendations

### Chemence next fill (after 22-04-2026)

Once 22-04-2026 lands (sheet 17 Jun, unconfirmed):
- LIQ-BAS-2 stock after fill = current 4,132 + 8,000 - burn through 17 Jun = 4,132 + 8,000 - (128.1 × 22) = 9,314 units → 73d cover
- LIQ-GLO-4 = 5,546 + 6,000 - (118.3 × 22) = 8,943 units → 76d cover

At Chemence cycle of 6-8 weeks, next placement: ~12-26 Jun for ETA ~mid-late Aug. **If kit surge stays at 137/d (W21 day-1), kit-adjusted consumption increases to ~145-150/d → cover compresses to 60d post-fill.** Plan to place next Chemence PO ~early Jun.

### Liquipak replacement decision (Path A/B/C — 13 days stalled)

ACC-REM 120ml stock projection assuming current bundle rate (49.4/d):
- Current 593 → OOS in 11d (~6 Jun) if no fill
- Plus Liquipak final (4,000) — 4,593 / 54.2 = 85d cover (runway to ~late Aug)
- Plus B360 packup ACC-REM-BUN-1 components if released

**No replacement filler = OOS condition kicks in late Aug-Sep when Liquipak final runs out.** Path decision lead time: 13-17d already burned. Daniel decision overdue.

---

## 8. What Needs Action

### 🔴 CRITICAL (act today)

1. **Joel: pay Liquipak final fill balance.** 22 May deadline missed. ACC-REM 120ml at 10.9d cover (bundle-adjusted). 7d transit. Every day's delay shrinks margin.
2. **Joel: pay B360 stockout balance** + confirm 5-SKU release (ACC-NAI-MAT, ACC-FRE-MANI, ACC-TRA-BAG, POW-CRE-217, POW-BLO-042). Daniel asked 14 May — no B360 confirmation yet. 17 OOS colour packups + 493 KIT-STA-2 + 19,445 STO-BUB-BAG-S all stranded.
3. **Joel/Remy: pay Print Runner ACC-LAB-UK PO.** Al chased 17+21 May, Remy's 21 May reply truncated. ACC-LAB-UK at 12.4d cover, 14-21d lead. Risk of gap into mid-Jun.
4. **Vik (Chemence): completion date for PO 22-04-2026 — 28d silent.** Sheet ETA 17 Jun unconfirmed. If slips, LIQ-BAS-2 / LIQ-GLO-4 enter negative cover by 15 Jul. Escalate to Joel.
5. **KIT-STA-2 critical: 20 on hand / 3.3d cover.** Confirm STA→COM substitution Shopify-flow holds. If Shopify auto-routes, no panic. If substitution rate drops, the kit business goes COM-only for 3-6 weeks.

### 🟡 WARNING (act this week)

1. **Daniel: place UK 02082026 fill PO tomorrow (27 May).** Recommend bumping ULT from 840 to 1,400-1,800 and COM from 1,148 to 2,000-2,500. Confirm Chemence pipeline covers post-arrival liquid burn.
2. **Daniel: Liquipak replacement Path A/B/C decision.** 13 days stalled. ACC-REM 120ml OOS window opens late Aug if no replacement filler. Sales Analysis should also test whether Remove 500ml can absorb 120ml demand if free-gift transitions.
3. **Daniel + Remy: free-gift transition mapping (current → Remove 500ml).** Tied to B360 5-SKU release. Tee up the Shopify offer config so it can be flipped same-day.
4. **Remy: reply to Seby (Bill 618199 audit) + Asana FIFO task.** Both due today 26 May.
5. **Remy: re-chase Roisin on Sweden re-ship MO122 quote.** Lost since 4 May. Today's POS doesn't surface it but it's an open obligation.
6. **Remy: chase Mason/Mihir on B360 packup SKU-pull progress** — 11 days stale.

### 🟢 MONITOR

1. **Kit surge durability**: W21 day-1 137/d (+25% over 109/d scaled). Sales Analysis to verify with full week.
2. **ACC-REM-500 overstocked**: 168d cover at 22.5/d standalone. Free-gift transition to 500ml would absorb this.
3. **ACC-LAB vs ACC-LAB-UK SKU split** — Shopify shows ACC-LAB 181.7/d demand; POS MODEL has ACC-LAB-UK at 217/d. Confirm whether both draw stock or only ACC-LAB-UK absorbs all UK demand. Greg to clarify SKU mapping.
4. **Chemence next placement timing**: ~early Jun (6-8w lead → mid-late Aug fill arrival). Don't slip placement waiting on 22-04-2026 confirmation.
5. **Dead-stock candidates** post-Powder Room: 13 colours in WATCH band (14-30d cover) — review with Gav for listing audit.

### ⚫ DATA INTEGRITY

- **Fulfillable / B360 deduction integrity BLIND** — 4th cycle. ShipHero `inventory_changes` cursor pagination still pending. Until fixed, UK POS Checks rely on Shopify-derived DSR + kit-adjustment math, which understates bundle-pull on liquids and accessories. Worth dev time before next review.
- **POS MODEL `UPDATED` cell empty** — Greg paste-discipline fix (4th cycle).
- **ACC-REM model DSR 39/d vs Shopify standalone 4.8/d** — 8x divergence. Reconciles only when bundle is added (49.4/d ACC-REM-BUN-1). Greg refresh: list as 54/d combined or flag the bundle source.
