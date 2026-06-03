# 🇨🇦 CA POS Model Check — 27 May 2026

## Data Freshness

- **POS MODEL last updated:** `UPDATED` cell empty (Greg paste-discipline issue, carried). Sheet content extracted today 11:57 AEST; treated as current.
- **3PL (B360) last valid date:** 2026-05-27 (today).
- **Shopify latest:** through 2026-05-25 (+1d lag, normal).
- **Growth factor:** **2.0x live** (user-confirmed 27 May; intent unchanged from 20 May). Sheet's POS MODEL global growth-factor cell reads 1.7x, which is a **future-container value** (CA 25072026 / planned) per [[future-container-growth-factor]] — Greg cell convention, not a live-rate change. **Use 2.0x = 160/d scaled** for all current-stock projections.
- **Kit base:** STA 21 / COM 41 / ULT 18 = 80/d → **2.0x = 160/d scaled** (live). Future container at 1.7x = 136/d.

### Manual overrides applied (live channel/Gmail context layered over sheet)

- **CA 21062026 arrival:** 1 Jul (Lily vessel confirmation 13 May) — sheet still shows 22 Jul. Greg fix outstanding.
- **Butuo Remove bottles raw goods PO:** placed today 27 May (user-confirmed). Sheet does not reflect.
- **Greenfield SO567407:** paid 21 May (user-confirmed). Delivery "will take ages" (user 27 May) — track as delivery-risk.
- **247 Invoice 305815 ($40,124.48):** Joel received today, due 1 Jun.
- **Glass Slipper:** missing from CA 21062026 Sally PO per Daniel 25 May escalation; window closes tomorrow 28 May with container completion.
- **CA 25072026:** Daniel actively sizing today (was 5 days past target).

---

## Growth Factor Health Check

| Metric | Value |
|---|---|
| Live growth factor (user-confirmed) | **2.0x** |
| Scaled kit DSR (live) | **160/d** |
| Sheet future-container value | 1.7x (CA 25072026 onwards — per [[future-container-growth-factor]]) |
| Actual 14d kit DSR (Shopify) | 123.9/d (STA 13.4 + COM 86.0 + ULT 24.5) |
| Actual growth factor | **1.55x** |
| Gap vs scaled 2.0x | **-23% (selling below scaled target)** |
| Trend | W20 -10% vs 2.0x (160/d) → W21 -23% vs 2.0x (160/d). **Recovery slipping** — second-week test not as strong as W20. |

**Read:** Per [[growth-factor-framing]] don't lower the live 2.0x; it's aspirational and tied to ad-spend ramp. The future-container 1.7x is a Greg observation about post-21062026 sizing assumptions — not an active-rate change. **Watch W22 — if -23% gap holds, the W20 single-week parity print was the peak of the surge, not the start of a trend.**

---

## Stock Position (live, both covers)

Stock from 3PL tab last valid 27 May. **Projected DSR** uses POS MODEL × 1.7x (kit-adjusted where relevant). **Actual DSR** uses 14d 3PL deduction (captures kit + bundle + offer pull). Cover at actual is the operational number; projected is the ambition target.

### Kits
| SKU | Stock | Proj DSR | Cov @ Proj | Actual DSR | Cov @ Actual | Note |
|---|---|---|---|---|---|---|
| KIT-STA-2 | 3,928 | 42.0 (21×2.0) | 94d | 13.2 | **298d** | massive over-build; Shopify 7d 13.6/d |
| KIT-COM-4 | 6,274 | 82.0 (41×2.0) | 77d | 87.6 | **72d** | hot — actual > model, 7d 76/d |
| KIT-ULT-6 | 2,795 | 36.0 (18×2.0) | 78d | 25.1 | **111d** | healthy |
| ALL KITS | 12,997 | 160.0 | 81d | 125.9 | **103d** | actual 1.55x vs scaled 2.0x = -23% gap |

### Critical / live-actionable
| SKU | Stock | Proj DSR | Cov @ Proj | Actual DSR | Cov @ Actual | Note |
|---|---|---|---|---|---|---|
| **ACC-NAI-MAT (Mani Mat)** | **0** | 0 | OOS | 90.8 (residual) | **OOS NOW** | **Offer replaced with gift card (user 27 May) — no business risk.** Trailing 14d 3PL deduction reflects the pre-swap window; forward demand collapses to ~0.3-0.6/d Shopify standalone. |
| ACC-TIP-SQU (Square Tips) | 175 | 144.5 (stale) | 1.2d | 107.3 (residual) | **1.6d at avg** | Same as above — Linda-attached offer mechanism replaced by gift card. Standalone Shopify only 1.3-1.6/d. **Real cover ~110d at standalone rate**, not 2d. |
| **ACC-REM-500 (Remove 500ml)** | 1,181 | 119 | 10d | 104.7 | **11d** | Swift fill blocked on Joel payment. **This is the only physical critical** post-offer-swap to gift card. |
| LIQ-HEA-5 (Heal) | 5,585 | 144.5 (kit-adj) | 39d | 128.6 | **43d** | rides on same Swift fill; slipped from 49d on 20 May |

### Liquids (other) — all safe at actual rate
| SKU | Stock | Actual DSR | Cov @ Actual | Proj DSR |
|---|---|---|---|---|
| LIQ-BAS-2 | 1,225 | 9.4 | 131d | 28.9 (overstated) |
| LIQ-GLO-4 | 1,422 | 5.0 | 284d | 17.0 (3x overstated) |
| LIQ-SEA-3 | 913 | 8.1 | 113d | 20.4 (overstated) |
| LIQ-BON-1 | 937 | 3.8 | 247d | 13.6 (3x overstated) |
| LIQ-SOA-6 | 851 | 3.3 | 258d | 13.6 (4x overstated) |
| LIQ-SEN-2 | 663 | 5.3 | 125d | 6.8 |
| LIQ-SEN-4 | 551 | 4.0 | 138d | 5.1 |
| LIQ-MAT-4 | 1,174 | 3.5 | 335d | 11.9 |

**Stale POS MODEL DSR flag carried** — Greg refresh outstanding (3-8x overstated on standalone liquids; same as 20 May). Doesn't affect kit-container sizing (liquids are CN pre-packed in kits) but it does inflate the Cov @ Proj column noise.

### Other items
| SKU | Stock | Actual DSR | Cov @ Actual | Note |
|---|---|---|---|---|
| ACC-REM (120ml) | 3,849 | 9.1 | 423d | bundle channel still main; standalone collapsed |
| ACC-REM-BOW | 5,224 | 15.1 | 347d | safe — way overstocked vs current burn |
| ACC-TRA-BAG | 579 | 0 | n/a | **NOT used — site offer replaced with gift card (user 27 May).** Treat as inert stock. |
| ACC-TIP-COF | 611 | 40.3 | 15d | Coffin Tips burning fast (offer pool) |
| ACC-TIP-STI | 399 | 1.0 | 399d | safe |
| ACC-TIP-BAL | 698 | 1.2 | 582d | safe |
| ACC-TIP-ALM | 2,507 | 3.8 | 660d | overstocked |
| ACC-INS | 20,637 | 123.4 | 167d | safe |
| ACC-THA | 31,114 | 167.9 | 185d | safe |
| ACC-LAB-CA | sheet NaN | — | — | Greg deduction rule fix outstanding. 6,878 (20 May) + 1,300 reprint + 10k Mixam (ETA 2 Jun) = comfortable through Aug |
| STO-BUB-BAG-L | 6,544 | 125.7 | 52d | safe |
| STO-MAI-BAG-S | 9,090 | 44.3 | 205d | safe |
| STO-MAI-2 | 9,130 | 44.3 | 206d | safe |

### Breakout colours (POS MODEL DSR understated)
| SKU | Stock | Model DSR | Shopify 7d | Cov @ 7d | Note |
|---|---|---|---|---|---|
| POW-ANG-D09 (Angel Energy) | 922 | 1.7 | 10.4 | 89d | **5.6x model, day 3** |
| POW-BLO-D07 (Bloom) | 738 | 1.7 | 7.6 | 97d | 4.5x model, day 2 |
| POW-SAT-D10 (Satin) | 746 | 1.7 | 7.7 | 97d | 4.5x model, day 2 |
| POW-CLE-193 (offer pool) | 11,870 | — | 29.7 | 78d at 3PL | sustained deduction 152/d 3PL (offer-attached) |
| POW-JUS-449 (offer pool) | 8,886 | — | 6.6 | 68d at 3PL | sustained deduction 130/d 3PL (offer-attached) |

### At-risk colours (per 20 May summary, recheck)
| SKU | Stock | Cov @ 7d Shopify | Note |
|---|---|---|---|
| POW-GLA-CS02 (Glacier Glow) | **0** | OOS | Already OOS |
| POW-CAS-CS32 (Cashmere) | 171 | 44d | safe pre-CA 21062026 (arrives 1 Jul, ~35d) |
| POW-LAT-CS38 (Latte Cloud) | 156 | 46d | safe pre-CA 21062026 |
| Blue Moon, Blush, Forest Muse, Lemonade, Peony Puff, Silent Eclipse | mixed | — | restocked in CA 21062026 (600-800/each). Accept OOS window per 20 May decision. |

---

## Local Fill Status

### Swift Innovations 14-05-2026 PO (Heal + Remove 500ml + Remove 120ml)
- **Status:** Ordering (blocked on Joel payment).
- **Raw goods feeders:**
  - New Directions Canada: oils received at Swift 19 May (60L Almond, 4L Jojoba, 1L Orange, 1L Lemon, 600L Coconut) ✅
  - Amazon Canada: Completed ✅
  - Greenfield SO567407: PAID 21 May ✅, **but delivery slow** (user 27 May)
  - Butuo Remove bottles raw goods PO: **PLACED TODAY** (user 27 May) ✅
  - Acetone: in transit per 26 May recap. Status unconfirmed.
- **Gating:** Joel's $1,882.84 prior + $13,064.63 advance CAD (13 days since recommendation). **Plus**: Greenfield delivery lead time (new risk flagged today).
- **Post-payment ETA stack:** ~5-7d Butuo bottles transit + 14d Swift production + 5-7d to 247 = **~25d**. Best-case restock if Joel pays today: ~24-25 Jun.
- **ACC-REM-500 OOS gap if paid today:** ~13d (12 Jun → 25 Jun). If paid Monday 1 Jun: ~17-19d.

### Mixam 14-05-2026 (ACC-LAB-CA 10k)
- **Status:** Ordering, ETA 2 Jun.
- **Plus:** MX2029340 1,300pcs reprint in production, ETA early-mid Jun.

### Linda tip filling (for CA 21062026)
- **Status:** Unscheduled. Daniel owed schedule.
- Components: Mani Mat 1,100 + Coffin 5,000 + Square 1,500 + Stiletto 200 + Ballerina 1,000 + Almond 1,000.
- **Timing risk:** ACC-TIP-SQU at 1.6d cover; Linda fill needs to land before CA 21062026 if the offer keeps Square Tips active.

---

## Container / Order Status

### CA 21062026 (Birthday Sale)
- **POS MODEL:** Est completion 28 May (tomorrow), arrival 22 Jul (**stale — actual 1 Jul** per Lily 13 May).
- **Status:** In Production.
- **Slack:** Daniel 25 May bangbang to Joel — Glass Slipper missing from Sally PO. 2 days silent.
- **Manifest (per 20 May recap):** 672 STA + 1,988 COM + 1,008 ULT + 3,000 small satchels + 3,300 small mailer boxes + 2,160 Matte + 3,024 Soak + 4,000 Remove Bowls + tip pack via Linda + 1,100 Mani Mat + 10,000 Clear.
- **Action:** Glass Slipper add — window closes tomorrow.

### CA 25072026
- **POS MODEL:** Est completion 1 Jul, arrival 25 Aug.
- **Status:** Ordering.
- **Today:** Daniel actively sizing (user 27 May).
- **Sizing concerns:** current draft 5,404 kits + 86,312 units. KIT-STA-2 at 298d cover today → post-21062026 ~333d → post-25072026 ~432d at 13.2/d 3PL. **STA-2 needs heavy trim** (mirrors UK STA→COM substitution pattern).
  - Suggested kit mix based on actual: STA 11% / COM 70% / ULT 20% (vs current ~26/52/22).
  - Daniel call.

### Planned beyond 25072026
- Three placeholder shipments (est arrivals 13 Aug, 29 Aug, 29 Sep). No active sizing needed yet.

---

## Stock-Out Forecast

### 🔴 OOS NOW or sub-14d
| SKU | Stock | Actual DSR | Days to OOS | Next Inbound | Arrives | Gap |
|---|---|---|---|---|---|---|
| ACC-REM-500 | 1,181 | 104.7 | 11d | Swift fill | ~25 Jun if Joel pays today | **12-14d OOS gap** |
| POW-GLA-CS02 (Glacier Glow) | 0 | 2.3 | already OOS | CA 21062026 | 1 Jul | accept (per 20 May decision) |
| ACC-NAI-MAT (Mani Mat) | 0 | residual | OOS but **no business impact** | CA 21062026 (1,100) | 1 Jul | Site offer replaced with gift card — OOS expected, no swap pressure |
| ACC-TIP-SQU (Square Tips) | 175 | 1.3-1.6 standalone | **~110d** | CA 21062026 (1,500 via Linda) | 1 Jul | Apparent 2d cover was offer-driven; standalone-only burn = healthy |

### 🟡 14-44d, no fresh PO needed (covered by inbound)
| SKU | Stock | Actual DSR | Days to OOS | Notes |
|---|---|---|---|---|
| LIQ-HEA-5 | 5,585 | 128.6 | 43d | Swift fill bundles with Remove 500ml; both unblock with Joel payment |
| ACC-TIP-COF | 611 | 40.3 | 15d | CA 21062026 brings 5,000 (1 Jul, 17d gap) — Linda fill should bridge |

### 🟢 Safe (>44d cover or post-arrival safe)
- All kits, all main liquids, all packaging, ACC-INS/THA/LAB-CA, Remove 120ml/Bowl/Travel Bag, most colours.

### Container gap analysis — CA 25072026 sizing (live today)
Critical SKUs that **must** be sized correctly in Daniel's draft today:
- **KIT-STA-2:** TRIM HARD. Current 1,400 OL → recommend ~300-500. Post-25072026 cover at actual 13.2/d = 432d if untrimmed.
- **KIT-COM-4:** SUPPORT. Current 2,800 OL = healthy at 87.6/d post-arrival ≈ 145d. Could nudge up if W22 confirms sustained 86/d.
- **ACC-REM-500:** Currently ZERO on CA 25072026. With Swift fill cycle landing ~25 Jun, next Swift cycle won't bridge to 25 Aug arrival cleanly. **Either add Remove 500ml to 25072026 or plan a third Swift cycle pre-Aug.**
- **ACC-NAI-MAT / ACC-TIP-SQU / ACC-TIP-COF / Linda-fill items:** With the gift-card offer in place, kit-attach demand for these has collapsed. **Open question for Daniel — does CA 21062026 still need the Linda tip fill (1,100 Mani Mat + 5,000 Coffin + 1,500 Square + Stiletto/Ballerina/Almond)?** If gift card is permanent, scrap or shrink the Linda fill. If offer rotates back later, keep as-is.

---

## Cascading Arrival Projection (kits, at actual 3PL rate)

| Stage | KIT-STA-2 | KIT-COM-4 | KIT-ULT-6 | ALL KITS | Days cover |
|---|---|---|---|---|---|
| Now (27 May) | 3,928 (298d) | 6,274 (72d) | 2,795 (111d) | 12,997 | **103d** |
| After CA 21062026 (1 Jul) | +672 → ~4,150 (314d) | +1,988 → ~5,200 (60d) | +1,008 → ~3,000 (120d) | ~12,350 | **98d** |
| After CA 25072026 (25 Aug, *if* draft holds 1,400/2,800/1,204) | +1,400 → ~5,250 (398d) | +2,800 → ~6,400 (73d) | +1,204 → ~3,650 (146d) | ~15,300 | **122d** ⚠️ |

⚠️ Post-25072026 ALL-KITS cover at 122d exceeds 45-75d target.

**If Daniel trims STA-2 from 1,400 → 400 on CA 25072026:** Total kits post-25072026 ~14,300 → 113d cover (still high but more defensible against W22 surge).

---

## What Needs Action

### 🔴 CRITICAL — act today

1. **Joel: pay Swift advance ($13,064.63 + $1,882.84 prior CAD).** 13 days since recommendation. Every day = +1d ACC-REM-500 OOS gap. Net gap if paid today: 12-14d. (Mon 1 Jun → 17-19d.)
2. **Joel: add Glass Slipper to CA 21062026 Sally PO.** Container completion **tomorrow** (28 May). Daniel 25 May escalation 2 days silent.
3. **Daniel: CA 25072026 sizing today must trim KIT-STA-2 hard** (recommend 300-500 vs current 1,400). Also confirm Remove 500ml allocation — currently zero on the draft. **And confirm Linda tip-fill scope** given the gift-card offer reduces kit-attach demand for Mani Mat / Square / Coffin tips.
4. **Joel: pay 247 Invoice 305815 CAD $40,124.48** (Net 7, due 1 Jun).

### 🟡 WARNING — act this week

5. **Daniel: Linda tip-fill decision for CA 21062026** — Square Tips at 1.6d cover *at the trailing 14d rate*, but that rate was offer-driven. Standalone burn is 1.3-1.6/d (110d cover). If gift card stays as the offer, Linda fill is overkill; if it rotates back to tips/Mani Mat, keep as-is.
6. **Daniel/Joel: monitor Greenfield delivery ETA.** User flagged "will take ages" — could extend Swift production restart even after Joel payment. Consider alt-supplier if delivery slips beyond Swift's other-ingredient ready date.
7. **Joel: pay Zakka balance pre-17 Jun release** (via Vanessa).
8. **Joel: explicit Greenfield SO567407 payment confirmation** (evidence on 21 May email is strong; close the loop).
9. **Greg: refresh POS MODEL DSR** for CA liquids + ACC-REM-500 + ACC-REM standalone (3-5x overstated).
10. **Greg: fix ACC-LAB-CA B360 deduction rule (NaN).**
11. **Greg: update CA 21062026 sheet arrival 22 Jul → 1 Jul.**
12. **Greg: paste-discipline — fill `UPDATED` cell.**
13. **Greg / Daniel: reconcile growth-factor cell.** Sheet's global GF cell reads 1.7x but user intent is 2.0x live; the 1.7x relates to future-container sizing per [[future-container-growth-factor]]. Worth documenting in POS MODEL header so digest extract picks up the live rate.

### 🟢 MONITOR

14. POW-ANG-D09 / POW-BLO-D07 / POW-SAT-D10 breakout (5.6/4.5/4.5x model). Stocks 922/738/746, cover ~90/97/97d at 7d Shopify rate. Healthy. POS MODEL DSR understated for these — Greg add to refresh batch.
15. POW-CLE-193 / POW-JUS-449 sustained 5-6x benchmark deductions (offer-attached). Stocks 11.9k / 8.9k → 78d / 68d cover. FYI.
16. Dead-stock listing audit (21 SKUs / 14,021 idle) — list with Gav, no movement.

---

## Local Fill Forecast (next placement)

### Swift — next cycle (post-14-05-2026)
- Once 14-05-2026 lands (~25 Jun if paid today), ACC-REM-500 cover ~9,000 + ~remaining stock at restock → ~80d.
- Lead time: ~4-5w fill + ~1w to 247 = ~5w (35d) from PO place to restock.
- **Next Swift PO place by:** ~mid-Aug (to bridge to a Sep arrival). Not urgent — but **CA 25072026 should also include ACC-REM-500** to avoid stacking too much on local fill cycle.

### Mixam — next labels reorder
- Current 10k landing 2 Jun + 1.3k reprint mid-Jun + existing 6,878 ≈ 18k. At 261.8 model / ~167.9 3PL = 67-107d.
- **Next Mixam PO place by:** ~Jul (30d lead, watch the W22-W24 print).

### Linda — Tips fill for 21062026
- Active. Daniel to schedule. Trigger: ACC-TIP-SQU at 1.6d cover means imminent Linda fill needed to bridge.

---

## Follow-Up Items

**Immediate (today/tomorrow)**
- [ ] Joel: Swift payment (>$13k + prior).
- [ ] Joel: Glass Slipper on CA 21062026 (window: 28 May).
- [ ] Daniel: CA 25072026 sizing (trim STA-2, add Remove 500ml, confirm Linda tip-fill scope vs gift-card offer).
- [ ] Joel: pay 247 Invoice 305815 by 1 Jun.

**This week**
- [ ] Daniel: schedule Linda tip filling.
- [ ] Joel: Zakka balance.
- [ ] Greg: POS MODEL housekeeping (DSR refresh + ACC-LAB-CA NaN + 21062026 arrival + UPDATED cell).
- [ ] Daniel/Joel: Greenfield delivery ETA chase.
- [ ] Remy: 247 Apr rate sheet ack (Regina, 8d stale).

**Carried**
- [ ] Gav: booklet-missing CX email rollout (16d).
- [ ] Gav/Remy: dead-stock listing audit.
