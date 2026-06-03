# Sales Data Analysis - UK - 12 May 2026

## DATA FRESHNESS

- **Shopify:** latest day 2026-05-11 (+1d lag normal)
- **3PL (B360 tab):** last valid 2026-05-12, but **tab is frozen Packup snapshot since Fulfillable go-live 14 Apr** → all 14d deductions = 0. **Shopify vs 3PL alignment cannot be run this cycle.** Carry-forward: Roisin export of Fulfillable 14d deduction history (deferred this cycle per user).
- **Growth factor:** 1.3x | Base 84.0/d | Scaled 109.2/d
- **Note on POS MODEL kit DSRs:** Greg refreshed since last cycle. Base now 84/d (was 81/d). STA=13.0, COM=41.6, ULT=54.6 — slightly higher than 5 May (STA 10.7, COM 30.8, ULT ~38).

---

## DSR: MODEL vs REALITY

### Kits

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap 14d |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 13.0 | 5.6 | 8.9 | 10.5 | **-32%** |
| KIT-COM-4 | 41.6 | 44.1 | 35.0 | 29.2 | **-16%** |
| KIT-ULT-6 | 54.6 | 34.7 | 34.2 | 37.0 | **-37%** |
| **TOTAL** | **109.2** | **84.4** | **78.1** | **76.7** | |

**Effective growth factor: 0.93x vs 1.3x target = -28.5% gap.** Significant convergence vs 5 May Recap (0.72x then). Greg's kit DSR refresh tightened the model — actual is now closer to scaled than last cycle suggested.

**Kit mix shift:** STA share collapsed to 11% of total (model expects 12%). COM up to 45% (model 38%). ULT at 44% (model 50%). **Complete-kit substitution behaviour visible in the numbers** — customers buying COM where STA might have been chosen historically. Validates Joel's substitution plan as a working pattern, not just a stop-gap.

### Heal (kit-adjusted)

| Metric | Model DSR | Standalone 7d | Standalone 14d | Kit-adj 7d | Kit-adj 14d | Gap vs Model |
|---|---:|---:|---:|---:|---:|---:|
| LIQ-HEA-5 | 110.5 | 2.9 | 2.0 | 87.3 | 80.1 | **-28%** |

Heal demand 28% below model — same direction as kits. Cover at kit-adj actual = 87d, healthier than model assumes.

### Liquids (standalone; Base + Glow are kit-adjusted at Fulfillable)

| SKU | Model DSR | Shop 14d | Standalone Gap | Notes |
|---|---:|---:|---:|---|
| LIQ-BAS-2 (Base) | 135.2 | 23.6 | -83% **(kit-adj)** | Real = 23.6 standalone + 78.1 kit = 101.7/d → 58d cover. Below model. |
| LIQ-GLO-4 (Glow) | 122.2 | 10.8 | -91% **(kit-adj)** | Real = 10.8 + 78.1 = 88.9/d → 81d cover. Below model. |
| LIQ-SEA-3 (Seal) | 15.6 | 15.9 | +2% | Aligned. |
| LIQ-BON-1 (Bond) | 6.5 | 3.6 | -45% | Bond pre-packed in kits from Sally - real demand IS standalone only. Model overstates 80%. |
| LIQ-MAT-4 (Matte) | 7.8 | 2.5 | -68% | Standalone only. Model overstates 3x. |
| LIQ-SOA-6 (Soak) | 6.5 | 2.5 | -62% | Standalone only. Model overstates 2.6x. |
| LIQ-SEN-2 / LIQ-SEN-4 | 0 | 0 | — | Discontinued (confirmed). Drop from model. |

**Bond/Matte/Soak model staleness flagged but accepted this cycle** (user note). Bond + Glow kit pre-pack from Sally — the model may eventually align if Greg refreshes against actual kit assembly composition.

### Remove Products (bundle-inflated)

| SKU | Model DSR | Shop 14d Standalone | + Bundle Share | Real DSR | Cover |
|---|---:|---:|---:|---:|---:|
| ACC-REM (120ml) | 39.0 | 6.6 | +15.0 (BUN-1) | 21.6 | 64d |
| ACC-REM-500 | 36.4 | 7.9 | +10.8 (BUN-2) | 18.7 | 228d |
| ACC-REM-BOW | 31.2 | 0.8 | +25.8 (both BUN) | 26.6 | 177d |

Liquipak final 800L PO ~160d coverage from 02-04-2026 placement = OOS scenario ~early Sep on ACC-REM (120ml). Remove 500ml + Bowl massively overstocked.

---

## WEEKLY KIT TREND (8w)

| Week | Period | Total | Daily | vs Model (109.2/d) |
|---|---|---:|---:|---:|
| W12 | 16-22 Mar | 473 | 67.6 | -38% |
| W13 | 23-29 Mar | 610 | 87.1 | -20% |
| W14 | 30 Mar-5 Apr | 583 | 83.3 | -24% |
| W15 | 6-12 Apr | 671 | 95.9 | -12% |
| W16 | 13-19 Apr | 585 | 83.6 | -23% |
| W17 | 20-26 Apr | 441 | 63.0 | **-42% floor** |
| W18 | 27 Apr-3 May | 532 | 76.0 | -30% |
| W19 | 4-10 May | 558 | 79.7 | -27% |
| W20 partial | 11 May (1d) | 73 | 73.0 | -33% |

**Recovery sustained off W17 floor.** 4-week average 78.4/d. 8-week pattern: persistent 20-42% below scaled. No declining streak; flat baseline at 76-83/d.

**Recommended growth factor: 0.93x × 1.10 = 1.02x.** This is the recommended sizing factor per the formula. The model's 1.3x is aspirational; per memory `feedback_growth_factor_framing.md` don't drop the model factor but flag UK 02082026 sizing decisions are against a 0.93x reality, not 1.3x.

---

## TOP COLOURS (14d Shopify)

Sample of high-volume colours; full list in extract.

| SKU | Name | Model DSR | Shop 14d | Stock | Cover | Status |
|---|---|---:|---:|---:|---:|---|
| POW-CLE-193 | Clean Slate | 117.0 | 30.1 | 11,385 | **378d** | Massive overstock |
| POW-HEA-515 | Heatwave | 35.1 | 24.9 | (check) | OK | Aligned |
| POW-POS-184 | Positively | 36.4 | 20.1 | (check) | OK | -45% vs model |
| POW-PIL-194 | Pillow Talk | 24.7 | 18.2 | OK | -26% |
| POW-TRA-452 | Train-Wreck | 19.5 | 16.2 | 49 | **3d** | **CRITICAL** |
| POW-BAR-198 | Bare Necessity | 16.9 | 12.4 | 189 | **15d** | **CRITICAL** |
| POW-PEA-068 | Peachy | 0 (?) | 9.9 | 0 | OOS | Top-seller OOS |
| POW-SIN-254 | Sincere | 16.9 | 7.8 | 87 | **11d** | **CRITICAL** |
| POW-SLO-192 | Slow Burn | 18.2 | 11.9 | 227 | **19d** | **CRITICAL, no inbound** |

Total colour DSR: 7d=547/d, 14d=570/d. ~7.3 colours per kit at 78.1 kits/d (matches expected ~6 colour units per kit average across STA/COM/ULT mix).

---

## SELLING PERFORMANCE FLAGS

### Sales Spikes (7d > 30d by 50%+)

| SKU | 7d | 14d | 30d | Spike |
|---|---:|---:|---:|---:|
| UK/EU-POW-LIM-G13 | 13.9 | 6.9 | 3.2 | **+334%** |
| UK/EU-POW-GOL-565 | 13.0 | 6.5 | 3.0 | +333% |
| UK/EU-POW-COB-G17 | 17.3 | 8.6 | 4.0 | +332% |
| UK/EU-POW-POW-F17 | 21.6 | 10.8 | 5.0 | +332% |
| UK/EU-POW-VAN-F01 | 17.7 | 8.9 | 4.1 | +332% |
| (~8 more `UK/EU-POW-*` SKUs at +320-330%) | | | | |
| POW-PUM-398 (Pumpkin Spice) | 3.9 | 2.3 | 2.3 | +70% |
| POW-GAM-339 (Game Over) | 5.3 | 3.2 | 3.2 | +66% |

**The `UK/EU-POW-*` cluster all spike near identical +325-334%.** Pattern suggests listing/store change or test launch (e.g. Nordic/Dippi cross-region SKUs newly visible on UK store). Worth a Shopify check — these aren't normal demand pattern. Cross-reference with `#sale-announcements` and `#cro-team-meetings`.

### Sales Drops (7d < 30d by 40%+)

| SKU | 7d | 14d | 30d | Drop | Likely Cause |
|---|---:|---:|---:|---:|---|
| POW-CRU-090 (Crush) | 0.0 | 2.8 | 5.9 | -100% | OOS (B360 692 locked) |
| POW-JUS-449 (Just Friends) | 0.0 | 2.1 | 5.8 | -100% | OOS (B360 1,152 locked) |
| POW-OVE-487 (Over It) | 0.3 | 4.1 | 5.9 | -95% | OOS (B360 1,610 only) |
| POW-DUS-346 | 0.6 | 6.1 | 9.2 | -93% | check listing/stock |
| POW-ROY-304 | 0.6 | 4.2 | 6.9 | -91% | check listing/stock |
| POW-SEA-450 (Seaside) | 1.1 | 4.4 | 5.1 | -78% | low stock (27u) + B360 locked |
| POW-PEA-068 (Peachy) | 5.9 | 9.9 | 11.8 | -50% | OOS (B360 875 locked) |

**Most drops are B360-PACKUP locked OOS** — not demand softening. Releasing B360 stock would restore most of these to normal selling rates.

### Overperformers (>20% above model)

- POW-EMB-602 (Emerald): +16% (just under threshold but trending up)
- Most colours sit below model — no significant overperformers.

### Underperformers (>40% below model)

Many. Pattern: model DSR set when growth-factor was tracking closer to 1.3x. Now at 0.93x effective, every colour 30-50% below model is consistent with the overall demand picture.

### OOS Colours — Lost Opportunity (Sorted by 30d DSR)

17 storefront-OOS colours confirmed against site (user screenshots 12 May). All show SOLD OUT.

Sorted by 30d DSR descending — top = highest lost opportunity per day.

| # | SKU | Name | Stock | 30d DSR | 14d DSR | 7d DSR | B360 | 03062026 | 02072026 | 02082026 | B360 Days | Pipeline Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | POW-PEA-068 | Peachy | 0 | **11.8** | 9.9 | 5.9 | 875 | 1,200 | 400 | 800 | 74d | OK — 03062026 restocks |
| 2 | POW-GOD-017 | Goddess | 0 | **6.3** | 5.6 | 6.7 | 523 | 400 | 200 | 200 | 83d | OK — 03062026 restocks |
| 3 | POW-BUB-516 | Bubbly | 3 | **5.9** | 5.4 | 6.7 | 727 | 400 | 200 | 400 | 123d | OK once B360 releases |
| 4 | POW-CRU-090 | Crush | 0 | **5.9** | 2.8 | 0.0 | 692 | 200 | 200 | 400 | 117d | OK — 03062026 +200 light, bump 02082026 |
| 5 | POW-FAI-308 | Fairytale | 0 | **5.9** | 5.9 | 6.4 | 1,636 | 0 | 0 | **0** | 277d | **Zero CN inbound — long-term gap** |
| 6 | POW-OVE-487 | Over It | 0 | **5.9** | 4.1 | 0.3 | 1,610 | 0 | 0 | **0** | 272d | **Zero CN inbound — long-term gap** |
| 7 | POW-JUS-449 | Just Friends | 0 | **5.8** | 2.1 | 0.0 | 1,152 | 0 | 0 | 200 | 198d | OK, bump 02082026 to 600 |
| 8 | POW-VIB-529 | Vibes | 0 | 0.4 | 0.0 | 0.0 | 931 | 0 | 0 | 0 | ∞ | Slow seller; B360 covers |
| 9 | POW-BRE-109 | Breeze | 0 | 0.3 | 0.0 | 0.0 | 190 | 400 | 0 | 200 | 633d | OK — 03062026 |
| 10 | POW-COT-030 | Cotton Candy | 0 | 0.2 | 0.0 | 0.0 | 626 | 0 | 200 | 200 | ∞ | OK — 02072026 |
| 11 | POW-SHI-777 | Shine Bright | 0 | 0.1 | 0.0 | 0.0 | 493 | 0 | 0 | 0 | ∞ | Slow seller; B360 covers |
| 12 | POW-RUS-624 | Rustle | 0 | 0.0 | 0.0 | 0.0 | 317 | 0 | 0 | 200 | ∞ | Dormant; B360 covers |
| 13 | POW-BEY-825 | Beyond | 0 | 0.0 | 0.0 | 0.0 | 358 | 0 | 0 | 0 | ∞ | Dormant; B360 covers |
| 14 | POW-STA-826 | Star-Gazer | 0 | 0.0 | 0.0 | 0.0 | 602 | 0 | 0 | 0 | ∞ | Dormant; B360 covers |
| 15 | POW-TRE010 | Treasure | 0 | 0.0 | 0.0 | 0.0 | 526 | 0 | 0 | 0 | ∞ | Dormant; B360 covers |
| 16 | POW-FES-006 | Festive | 0 | 0.0 | 0.0 | 0.0 | 369 | 0 | 0 | 0 | ∞ | Seasonal; B360 covers |
| 17 | POW-STA-009 | Star Pine | 0 | 0.0 | 0.0 | 0.0 | 1,046 | 0 | 0 | 0 | ∞ | Seasonal; B360 covers |
| **Total** | | | | **48.5** | | | **12,673** | | | | | |

### Lost Opportunity Math

- **Daily DSR lost across 17 storefront-OOS SKUs: 48.5 units/day.**
- **Top 7 (active demand): 47.5 units/day** — virtually all the lost opportunity sits in the first 7 lines.
- **7-day lost units (if status quo holds):** ~340 units.
- **30-day lost units:** ~1,455 units.
- **Revenue proxy at £9 list price:** ~£3,060 lost weekly / ~£13,100 lost over a 30-day window. (Margin-adjusted figure from Gav for a hard number.)

### B360 Coverage Test — All 17 Are Recoverable

**Every one of the 17 storefront-OOS SKUs has B360 PACKUP stock.** The tightest cover is Peachy at 74d (875 units / 11.8/d). The next is Goddess at 83d. The other 15 all have 100d+ B360 cover at current rates.

**Total locked at B360 for these 17 SKUs: 12,673 units.** Releasing B360 PACKUP clears the entire storefront-OOS list for at least 74 days — well past the merged UK 03062026/02072026 arrival on 15 Jul. **B360 unlock is the single highest-leverage action for this entire OOS picture.**

### The Two Long-Term Exceptions

**POW-FAI-308 (Fairytale) and POW-OVE-487 (Over It)** have **zero CN inbound** on any of the three planned containers (03062026, 02072026, 02082026). At 5.9/d each, B360 covers them for ~270d (until ~Feb 2027). They need to be added to a **future container (02082026 or beyond)** if we want continuous stock past then.

**Recommended add to UK 02082026 (place tomorrow):**
- **POW-FAI-308: 800 units**
- **POW-OVE-487: 800 units**
- Bump POW-JUS-449 from 200 → 600 (covers ~100d post-arrival)

Total recommended add for OOS coverage: **2,000 units**.

### Seasonal/Dormant Listings (6 SKUs, lines 12-17)

POW-RUS-624, POW-BEY-825, POW-STA-826, POW-TRE010, POW-FES-006, POW-STA-009 — all 0/d demand for 30+ days. B360 PACKUP has 3,218 units across these 6. **Listing decision (Gav/Remy):** either delist until B360 releases and seasonal merch re-launches, or accept storefront-OOS state. No CN action needed.

---

### Dead Stock (in stock, 0 Shopify 14d)

| SKU | Stock |
|---|---:|
| POW-CAN-016 | 199 |
| POW-CAN-D103 | 199 |
| POW-REI-008 | 198 |
| **Total** | **596 units** |

Tiny — 3 SKUs, all suspected un-launched or quietly retired colours. Low priority.

### Sensitive Base / Glow

LIQ-SEN-2 + LIQ-SEN-4: both 0 stock, 0 sales 14d. **Confirmed dormant in UK.** Drop from model on next refresh.

---

## CONTAINER ARRIVALS DETECTED

| Date | SKU Count | Total Units | Pattern |
|---|---:|---:|---|
| 2026-04-14 | 194 | +2,409 | Fulfillable go-live - opening balance paste |
| 2026-04-16 | 15 | +15 | Single-unit corrections (data scrub) |

**No live deductions since 14 Apr** — B360 tab is now a frozen Packup snapshot. Live Fulfillable deduction history not in this sheet.

---

## INVENTORY DISCREPANCIES

Cannot run cumulative gap test for UK this cycle — B360 deduction tab frozen since 14 Apr. The single-day red flags below are all pre-transition (3 Apr - 16 Apr) and represent stock movements during the B360 → Fulfillable transition, not live demand anomalies.

### Historical (pre-transition) single-day flags worth noting:

| Date | SKU | Deduction | Benchmark | Likely Cause |
|---|---|---:|---:|---|
| 04 Apr | POW-SLO-192 | **5,707** | 35 | Pre-transition stock movement / batch transfer to Fulfillable |
| 16 Apr | STO-MAI-BAG-S | 3,565 | 330 | Packaging transfer to Fulfillable |
| 06 Apr | POW-POS-184 | 1,031 | 35 | Pre-transition transfer |
| 03 Apr | POW-OUR-772 | 1,018 | 35 | Pre-transition transfer |
| 04 Apr | POW-PER-229 | 1,004 | 35 | Pre-transition transfer |

These look like one-time bulk transfers, not lost stock. The POW-SLO-192 5,707-unit move is interesting given today's POS shows 5,597 of it locked in B360 - so those units may have stayed at B360 and the 4 Apr deduction was an internal accounting movement, not a Fulfillable inbound. Worth Greg verifying when B360 PACKUP releases.

**Until Fulfillable deduction export lands (carried as 4th-cycle item), no live data-integrity check is possible for UK.**

---

## UK 02082026 SIZING RECOMMENDATION

Place tomorrow 13 May. Current sheet contents: 560 STA + 1,148 COM + 840 ULT + 4,080 ACC-INS + 11,200 ACC-THA + existing colours.

### Container size against actual 0.93x growth (not 1.3x):

- **Kit sizing in container is conservative-sufficient.** 2,548 kits total (560+1,148+840) at actual 78.1/d = 33d cover boost - adequate as a top-up between UK 02072026 (15 Jul) and the September fill cycle.
- **Per Joel's container-merge plan,** UK 03062026 + UK 02072026 land together 15 Jul with 4,632 kits. Stock at 02082026 arrival (6 Sep) = ~6,973 - 4,141 consumption (53d at 78.1) + 2,548 = 5,380 kits = 69d cover. Within 45-75d target.

### Colour additions (recommended additions to fill PO):

| SKU | Current Stock | Shop 30d | Reason | Recommended Add |
|---|---:|---:|---|---:|
| **POW-OVE-487** | 0 | 5.9 | Zero CN inbound anywhere; B360 1,610 only | **800** |
| **POW-FAI-308** | 0 | 5.9 | Zero CN inbound anywhere; B360 1,636 only | **800** |
| **POW-NOT-065** | 23 | 5.2 | B360 only 118 (real no-pipeline) | **800** |
| **POW-JUS-449** | 0 | 5.8 | Existing 200 inadequate (36d), B360 1,152 locked | **bump +400 to 600** |
| **POW-SEA-450** | 27 | 5.1 | Existing 200 inadequate (~140d only post-stockout), B360 1,659 locked | **bump +200 to 400** |
| **POW-CRU-090** | 0 | 5.9 | Existing 200 in 03062026 inadequate, B360 692 locked | **+400** (split 03062026/02082026) |
| **POW-DAY-025** | 12 | 5.5 | Only 200 in 02082026; B360 855 locked but not soon | **+400 to 600** |
| **POW-SLO-192** | 227 | 11.4 | **5,597 in B360**, no CN inbound. Hold if B360 releases by Jul; otherwise add | **conditional 800** |

**Net recommended add: 4,200-5,200 units across 7-8 SKUs.** Most cost-effective lever is still the B360 PACKUP release (18,732 units total locked across the 14 critical-OOS colours). UK 02082026 should be sized assuming B360 doesn't release.

### Don't add (despite Shopify drops):

- POW-PEA-068 (Peachy): 03062026 already brings 1,200 → 102d post-arrival cover
- POW-GOD-017 (Goddess): 03062026 +400 = 63d post-arrival
- POW-SIN-254 (Sincere): 03062026 +800 = 80d post-arrival

These are all serviced by the merged July landing.

---

## KEY TAKEAWAYS

1. **Effective growth is 0.93x after Greg's refresh, not 0.72x.** Closer to scaled than 5 May suggested. W18→W19 confirms recovery off W17 floor (-42%). UK 02082026 sizing decisions should anchor on 0.93x reality with 1.3x ambition headroom.

2. **The 13 OOS / dropping colours are 70%+ a B360 PACKUP unlock problem.** 18,732 units locked across 14 critical SKUs. Accelerating £8,500 deposit pay-pace would clear 11 of these faster than Sally express or UK 02082026 additions.

3. **UK 02082026 fill PO place 13-15 May with +4,200-5,200 colour additions** across 7-8 SKUs prioritising the 3 zero-CN-inbound colours (POW-OVE-487, POW-FAI-308, POW-NOT-065) at 800 each. Other adds are top-ups to inadequate existing quantities.

4. **Complete-kit substitution is showing up in the kit mix data** — STA share dropped to 11% (model 12%), COM up to 45% (model 38%). Customers are converging on COM. Validates Joel's plan as a working pattern even outside the STA-gap context.

5. **UK/EU-POW-* spike cluster (10 SKUs at +325-334% spike)** needs a Shopify listing check. Suspicious uniformity — likely a listing or test launch, not organic demand. Cross-check `#sale-announcements` / `#cro-team-meetings`.

6. **Fulfillable deduction-history export is now the single highest-value data integrity action for UK.** 4 cycles carried; deferred again this cycle per user direction. Without it, alignment checks impossible and stock-loss detection blind.
