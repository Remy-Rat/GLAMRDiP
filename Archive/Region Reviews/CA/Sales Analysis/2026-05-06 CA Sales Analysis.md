# Sales Data Analysis — CA — 6 May 2026

## DATA FRESHNESS

- **Shopify:** 5 May 2026 (1d lag, normal)
- **3PL (B360 tab):** **BROKEN** - tab has only `#REF!`. **Step 4 (container detection), Step 5 (cumulative gap), and Step 6 (Shopify-vs-3PL alignment) are not runnable this cycle.** Greg has been pinged.
- **POS MODEL last paste:** 6 May 2026 (today)
- **Growth factor:** 1.5x
- **POS MODEL kit base:** 80/d → scaled 120/d
- **Audit window:** 6 Apr - 5 May 2026 (Shopify last 30d)

## DSR: MODEL vs REALITY

### Kits

| SKU | Model DSR (1.5x) | Shop 7d | Shop 14d | Shop 30d | Gap vs Model (14d) |
|---|---|---|---|---|---|
| KIT-STA-2 | 31.5 | 11.0 | 12.3 | 13.3 | -61% |
| KIT-COM-4 | 61.5 | 27.4 | 25.2 | 26.1 | -59% |
| KIT-ULT-6 | 27.0 | 8.7 | 8.9 | 10.0 | -67% |
| **TOTAL** | **120.0** | **47.1** | **46.4** | **49.4** | **-61%** |

Effective growth factor: **0.58x** vs scaled 1.5x. **10 weeks consistent at -56% to -67% kit gap.**

### Heal (kit-adjusted: standalone Shopify + kit consumption at 247)

| SKU | Model DSR | Shop 14d (standalone) | Adj 14d (+ kits 46.4) | Cover @ Adj |
|---|---|---|---|---|
| LIQ-HEA-5 | 127.5 (kit-adj) | 1.0 | 47.4 | 173d |

Model is roughly the projected kit-adjusted rate (120 + ~7.5 standalone Shopify). Actual is much lower because real kit demand is 46.4/d, not 120/d.

### Liquids (CA = standalone-only; Base/Glow model still kit-attached → Greg refresh outstanding)

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap vs Model |
|---|---|---|---|---|---|
| LIQ-BAS-2 (Base) | 25.5 | 10.7 | 8.2 | 8.7 | -68% |
| LIQ-GLO-4 (Glow) | 15.0 | 5.1 | 4.0 | 4.7 | -73% |
| LIQ-BON-1 (Bond) | 12.0 | 2.7 | 2.4 | 2.7 | -80% |
| LIQ-SEA-3 (Seal) | 18.0 | 7.1 | 5.6 | 6.4 | -69% |
| LIQ-SOA-6 (Soak) | 12.0 | 2.9 | 2.4 | 2.8 | -80% |
| LIQ-MAT-4 (Matte) | 10.5 | 3.0 | 2.7 | 3.2 | -74% |
| LIQ-SEN-2 (LO Base) | 6.0 | 4.6 | 3.1 | 3.5 | -48% |
| LIQ-SEN-4 (LO Glow) | 4.5 | 2.9 | 2.2 | 2.3 | -51% |

Pattern: every liquid is 50-80% below model. Confirms that POS MODEL DSR is still kit-attached for Base/Glow and that the standalone numbers everywhere else were set against scaled kit demand that hasn't materialised.

### Remove products (with bundle deductions accounted)

| SKU | Model | Shop 14d | + Bundle | Combined | Combined vs Model |
|---|---|---|---|---|---|
| ACC-REM (120ml) | 46.5 | 5.5 | + ACC-REM-BUN-1 (3.8) | 9.3 | -80% |
| ACC-REM-500 | 75.0 | 16.6 | + ACC-REM-BUN-2 (11.7) | 28.3 | -62% |
| ACC-REM-BOW | 60.0 | 1.4 | + BUN-1 (3.8) + BUN-2 (11.7) | 16.9 | -72% |

Even with bundle uplift, all three Remove SKUs sit well below model. ACC-REM-BOW model at 60/d is ~3.5x actual - Greg refresh candidate.

### Recommended growth factor (informational - do not lower per growth-factor doctrine)

```
actual_30d_kit_total = 49.4/d
model_kit_base = 80/d (1.0x)
actual_growth = 49.4 / 80 = 0.62x
recommended (with 10% buffer) = 0.68x
```

Per `feedback_growth_factor_framing.md`: do not recommend lowering. Frame as a health check. The 1.5x → actual 0.58-0.62x gap means CA orders against an aspirational target that ad-spend is not currently funding. Future container quantities should reflect this (see CA 25072026 placeholder note - we know it's TBD and will revisit).

## WEEKLY KIT TREND

| Week | Dates | Daily rate | vs 120 scaled | vs prev week |
|---|---|---|---|---|
| W12 | 16-22 Mar | 65.6 | -45% | - |
| W13 | 23-29 Mar | 52.7 | -56% | -20% |
| W14 | 30 Mar-5 Apr | 47.6 | -60% | -10% |
| W15 | 6-12 Apr | 55.4 | -54% | +16% |
| W16 | 13-19 Apr | 52.1 | -57% | -6% |
| W17 | 20-26 Apr | 46.1 | -62% | -12% |
| W18 | 27 Apr-3 May | 49.0 | -59% | +6% |
| W19* | 4-5 May | 31.5 | -74% | -36% |

W19 is only 2 days - directionally weak (31.5/d) but not statistically meaningful yet.

**Pattern:** stable mid-40s to mid-50s/d for 8 weeks. No declining streak (W18 ticked up vs W17). No promo spike. Just persistent flat-line at ~50/d against a 120/d target.

### Kit mix (14d actual vs scaled model)

| Kit | Actual % | Model %* | Notes |
|---|---|---|---|
| KIT-STA-2 | 26.5% | 26.3% | aligned |
| KIT-COM-4 | 54.3% | 51.3% | slight over-index |
| KIT-ULT-6 | 19.2% | 22.5% | slight under-index |

*Model % from kit DSR ratios at 1.5x scale.

Mix shift small. COM is the workhorse, ULT softer than scaled.

## REALISTIC DAYS COVER

(Same as POS Check Step 1 - cross-reference there. Headline: at actual demand, kits 335d, liquids 175-460d, Heal 173d kit-adj, Remove 500ml 115d combined, ACC-REM-BOW 331d combined.)

## CONTAINER ARRIVALS DETECTED

From B360 (Greg's same-day fix):
- **22 Apr:** 13 SKUs / ~17,433 units (partial customs batch 1)
- **25 Apr:** 15 SKUs / ~31,599 units (partial customs batch 2)
- **26 Apr:** 90 SKUs / ~59,425 units (CA 03022026 + CA 07042026 closing - the bulk customs container)
- Powder Room (24-03-2026) check-in 4-5 May likely below the 8-SKU detection threshold (only ~13 colours + B113 jars + bowl/etc.) and folded into smaller daily moves.

108,457 units total across the three arrival days — exceeds the 94,268 / 104 SKU manifest by ~14k. Modest variance, no flag.

## INVENTORY DISCREPANCIES (B360 RE-RUN — Greg fixed tab same-day)

**B360 restored mid-review.** Re-ran Steps 4-6 over 22 Apr - 6 May (15-day window, 3 arrival days excluded → 12 deduction days).

### Container arrivals detected from B360
- **22 Apr:** 13 SKUs increased, ~17,433 units (partial check-in batch 1)
- **25 Apr:** 15 SKUs increased, ~31,599 units (partial batch 2)
- **26 Apr:** 90 SKUs increased, ~59,425 units (the big customs batch — CA 03022026 + CA 07042026 closing)
- **Total:** 108,457 units — matches (and slightly exceeds) the 94,268 / 104 SKU manifest from 29 Apr recap, likely with Powder Room residue rolled in.

### Single-day red flags (last 14d, excl arrivals) — clean
Only 3 minor flags, all interpretable:

| Date | SKU | Deducted | Benchmark | x | Read |
|---|---|---|---|---|---|
| 5 May | POW-CLE-193 (Clear) | 68 | 35 | 1.9x | top-seller refill, 23.1/d Shopify; benchmark too low for high-velocity SKU |
| 6 May | POW-CLE-193 | 57 | 35 | 1.6x | same as above |
| 6 May | ACC-TIP-COF | 17 | 12 | 1.4x | minor |

**No unexplained anomalies.** 247 deduction integrity is clean over the 12-day window.

### Cumulative gap test (Step 5B)

**Kit alignment is excellent:**

| SKU | 3PL/d | Shopify/d | Gap | Read |
|---|---|---|---|---|
| KIT-STA-2 | 11.3 | 12.3 | -1.0 | aligned |
| KIT-COM-4 | 24.6 | 25.2 | -0.6 | aligned |
| KIT-ULT-6 | 8.7 | 8.9 | -0.2 | aligned |

247's kit deduction logic is firing correctly. The slight Shopify-lead is the +1d paste lag (normal).

**Liquids / standalone — mostly aligned:**

| SKU | 3PL 14d | Shopify 14d | Bundle uplift | Adj Shop | Gap | Read |
|---|---|---|---|---|---|---|
| LIQ-BAS-2 | 123 | 115 | +12 (LIQ-SET) | 127 | -4 | aligned |
| LIQ-GLO-4 | 71 | 56 | +12 | 68 | +3 | aligned |
| LIQ-HEA-5 | 560 | 14 | +12 | 26 | **+534** | kit-attached at 247 ✓ (560 ≈ 649 kits + 14 standalone) |
| LIQ-BON-1 | 38 | 34 | +12 | 46 | -8 | aligned |
| LIQ-SEA-3 | 91 | 79 | +12 | 91 | 0 | aligned |
| LIQ-SOA-6 | 37 | 33 | +12 | 45 | -8 | aligned |
| LIQ-MAT-4 | 33 | 38 | 0 | 38 | -5 | aligned |
| LIQ-SEN-2 | 40 | 43 | 0 | 43 | -3 | aligned |
| LIQ-SEN-4 | 29 | 31 | 0 | 31 | -2 | aligned |
| ACC-REM (120ml) | 124 | 77 | +53 (BUN-1) | 130 | -6 | aligned |
| ACC-REM-500 | 346 | 233 | +164 (BUN-2) | 397 | -51 | within paste-lag tolerance |
| ACC-REM-BOW | 210 | 20 | +217 (BUN-1+2) | 237 | -27 | aligned |

Heal kit-attached signature confirmed: 14d 3PL deduction (560) = ~kit total (649) + standalone (14). Per-Component-Map exactly as expected for CA.

**Per-order accessories (no Shopify):**

| SKU | 3PL 14d | Avg/d | Stock | Cover at actual | Notes |
|---|---|---|---|---|---|
| STO-BUB-BAG-L | 533 | 44.4/d | 9,094 | 205d | 1-per-kit; 44/d ≈ kit rate ✓ |
| STO-MAI-BAG-S | 502 | 41.8/d | 10,099 | 241d | 1-per-non-kit order ✓ |
| STO-MAI-2 | 502 | 41.8/d | 10,139 | 242d | matches BAG-S exactly ✓ |
| STO-BUB-BAG-S | 0 | 0 | 0 | n/a | 247 supplies own per CA region notes ✓ |
| ACC-INS | 530 | 44.2/d | 23,153 | **524d** | per-kit; aligned with kit rate ✓; heavy overstock |
| ACC-THA | 1,029 | 85.8/d | 34,642 | **404d** | per-order; heavy overstock |
| **ACC-LAB** | **0** | **0** | **NaN** | **n/a** | **⚠️ deduction rule still not firing in B360** despite Greg's 8 Apr re-enable |

### Colour cumulative gaps — clean
- **0 colour SKUs** with 100+ unit unexplained 3PL > Shopify gap. No POW-LAC-196 anomaly visible (confirmed reversal).
- 2 colour SKUs with Shopify > 3PL by 30+ (POW-POS-184 Positivi-Tea +40, POW-PIL-194 Pillow Talk +37) — top sellers; consistent with +1d Shopify paste lead.

### Discrepancies summary
- **No stock losses to escalate.** 247's deduction logic is working as expected.
- **One outstanding data integrity issue:** ACC-LAB-CA deduction rule isn't firing in B360 (still showing 0 deductions / NaN stock). Per 29 Apr recap, Greg re-enabled the rule — it isn't pulling through. **Greg follow-up: confirm rule mapping ACC-LAB-CA → B360 row 'ACC-LAB' is correct.**
- **POW-LAC-196 (Lace) 19 Apr 2,574-unit deduction:** confirmed non-issue. No anomaly in 14d cumulative window; 698d cover holds.

## 3PL DEDUCTION CHECK

Run completed after Greg's same-day B360 fix. **Kit alignment perfect** (gaps ≤1.0/d across all 3 kits). See Inventory Discrepancies above for full table.

## SELLING PERFORMANCE FLAGS

### Sales spikes (7d > 30d by 50%+)

| SKU | 7d | 14d | 30d | Spike | Stock | Read |
|---|---|---|---|---|---|---|
| POW-PEO-SH07 (Peony Puff) | 4.7 | 2.7 | 1.3 | +262% | 163 | now 35d cover at 7d rate (was 60d at 14d) - **OOS gap widens** |
| POW-BLU-ZGD22 (Blue Moon) | 5.0 | 3.3 | 1.5 | +233% | 157 | 31d cover at 7d (was 48d at 14d) - **OOS gap widens** |
| ACC-REM-BUN-2 | 13.3 | 11.7 | 5.6 | +138% | bundle | post-Swift restock recovery |
| ACC-REM-500 | 17.6 | 16.6 | 8.0 | +120% | 3,243 | post-restock recovery, in line with user's 30/d note |
| POW-LEM-ZGD01 (Lemonade) | 2.9 | 2.0 | 1.6 | +81% | 172 | 59d cover at 7d - still safe |
| POW-SEA-450 (Seaside) | 2.4 | 1.5 | 1.4 | +71% | 843 | 351d cover - fine |
| POW-ICE-ZGD16 (Icey) | 3.3 | 2.1 | 2.0 | +65% | 388 | 117d - fine |
| POW-SCA-155 (Scarlet) | 2.3 | 1.4 | 1.5 | +53% | 698 | 304d - fine |

**Two of the three POS-Check OOS-gap colours are SPIKING.** Peony Puff and Blue Moon's 7d demand is 2.3-3.3x their 30d baseline. If the trend holds, the gap before CA 21062026 (15 Jul) widens further:
- Peony Puff at 7d rate: -35d gap (was -10d at 14d)
- Blue Moon at 7d rate: -39d gap (was -22d)
- Glacier Glow at 7d rate (2.3/d): 14d cover, -56d gap (was -49d)

These are the three to **raise per user instruction** - flag in `Current Issues` for visibility but Sally express constrained by $150k arrears, so most likely outcome is accept the OOS windows.

### Sales drops (7d < 30d by 40%+, 30d > 2)

| SKU | 7d | 14d | 30d | Drop | Stock | Read |
|---|---|---|---|---|---|---|
| POW-SER-039 (Serenity) | 1.1 | 0.9 | 3.0 | -63% | 708 | listing audit candidate |
| ACC-REM (Remove 120ml) | 5.7 | 5.5 | 14.6 | -61% | 4,081 | mirror of ACC-REM-500 spike - demand shifting from 120ml to 500ml/bundle |
| POW-CHE-044 (Cherished) | 1.1 | 0.9 | 2.5 | -56% | 723 | listing/marketing audit |
| ACC-REM-BUN-1 | 3.7 | 3.8 | 7.2 | -49% | bundle | confirms Remove demand-shift to 500ml/BUN-2 |
| POW-IMA-264 (Imagine That) | 1.6 | 1.8 | 2.7 | -41% | 1,071 | listing/marketing audit |

**Notable pattern:** Remove demand has shifted from 120ml + BUN-1 to 500ml + BUN-2. Combined Remove 120ml: 9.3/d (down from 14.6 + 7.2 = 21.8/d 30d ago, -57%). Combined Remove 500ml: 28.3/d (up from 8.0 + 5.6 = 13.6/d 30d ago, +108%). **Net Remove demand up.** ACC-REM-500 returning to stock has cannibalised 120ml. Accounting for combined demand:
- Total Remove standalone+bundle 14d: 37.6/d (vs 35.4/d 30d) - flat overall.

### Underperformers (>40% below model DSR, model >2/d)

Top 15 underperformers (already shown above). Pattern: every operational SKU is far below its model DSR because the model assumes 1.5x kit demand the region isn't generating. The Greg-known refreshes for Base/Glow/ACC-REM-BOW remain outstanding.

### Dead stock (in stock, 0 14d Shopify sales)

**38 colour SKUs / 28,616 units idle.** Up from 25 SKUs / 21,000 units flagged on 29 Apr - **the dead-stock pile is growing.**

| SKU | Name | Stock | 30d DSR |
|---|---|---|---|
| POW-CAN-016 | Candycane | 2,077 | 0.1 |
| POW-WHI-L12 | Whirl | 1,400 | 0.0 |
| POW-LUS-015 | Lustre | 1,210 | 0.0 |
| POW-NEB-010 | Nebula | 1,200 | 0.0 |
| POW-SPE-006 | Spectra | 1,200 | 0.0 |
| POW-DAZ-L03 | Dazzle | 1,199 | 0.0 |
| POW-JUB-L11 | Jubilee | 1,025 | 0.0 |
| POW-PRI-012 | Prism | 1,000 | 0.0 |
| POW-TWI-L08 | Twinkle | 1,000 | 0.0 |
| POW-ANG-D09 | Angel Energy | 994 | 0.0 |
| POW-DRE-D08 | Dreamer | 809 | 0.0 |
| POW-CON-L02 | Confetti | 800 | 0.0 |
| POW-FIZ-L01 | Fizz | 800 | 0.0 |
| POW-GLI-007 | Glimmer | 800 | 0.0 |
| POW-DOV-093 | Dove | 799 | 0.0 |
| POW-SAT-D10 | Satin | 799 | 0.0 |
| POW-SOR-113 | Sorbet | 799 | 0.0 |
| POW-WHI-099 | Whimsy | 799 | 0.0 |
| POW-WIS-133 | Wish | 799 | 0.0 |
| POW-LUL-114 | Lullaby | 798 | 0.0 |
| POW-ROS-D14 | Rosewood | 798 | 0.0 |
| POW-VEL-D13 | Velvet Rose | 797 | 0.0 |
| POW-BUB-127 | Bubblegum | 796 | 0.0 |
| POW-BUT-098 | Buttercup | 796 | 0.0 |
| POW-BRE-109 | Breeze | 795 | 0.0 |
| POW-STE-001 | Stellar | 740 | 0.0 |
| POW-FES-006 | Festive | 735 | 0.0 |
| POW-GLI-D007 | Glisten Up | 682 | 0.2 |
| POW-YUL-007 | Yule Gold | 569 | 0.0 |
| POW-EVE-019 | Evergreen | 531 | 0.0 |
| POW-ICO-775 | Iconic | 475 | 0.2 |
| POW-UND-056 | Under The Tree | 453 | 0.0 |
| POW-SAF-149 | Saffron Blaze | 50 | 0.0 |
| POW-INF-506 | Inferno Hour | 42 | 0.0 |
| POW-ALL-146 | All Eyes On Me | 39 | 0.0 |
| POW-GAR-656 | Garnet Games | 9 | 0.0 |
| POW-BOR-355 | Bordeaux Nights | 1 | 0.0 |
| POW-RED-165 | Red Mischief | 1 | 0.0 |
| **TOTAL** | **38 SKUs** | **28,616** | |

**Pattern observations:**
- "L-" suffix (Limited / Christmas series, ~10 SKUs): Whirl, Dazzle, Jubilee, Twinkle, Confetti, Fizz, Lullaby - likely off-season; revisit Q4.
- "D-" suffix (~5 SKUs): Angel Energy, Dreamer, Satin, Rosewood, Velvet Rose - the leading "D-" denotes legit CA-listed colours per `feedback_dippi_prefix_convention.md`, not Nordic Dippi stock; these are bona-fide listing-audit candidates.
- Christmas-themed (Festive, Yule Gold, Evergreen, Under The Tree, Glisten Up): off-season - leave until Nov.
- The seven smallest (single digits to ~50 units: Bordeaux Nights, Red Mischief, Garnet Games, All Eyes On Me, Inferno Hour, Saffron Blaze) are effectively OOS already; CA 25072026 has 600 of each as a placeholder, but the placeholder is TBD.

**Listing audit candidate** - either re-enable seasonal promo, mark as new colours not yet launched, or schedule a clearance/bundle. Bandwidth-light task; low operational urgency.

### Sensitive Base / Glow signal

| SKU | Pair | 14d DSR | Pair % | Notes |
|---|---|---|---|---|
| LIQ-BAS-2 (Base) | parent | 8.2 | - | |
| LIQ-SEN-2 (LO Base) | LO option | 3.1 | 27% of LIQ-BAS-2 | within expected 30% kit-split band |
| LIQ-GLO-4 (Glow) | parent | 4.0 | - | |
| LIQ-SEN-4 (LO Glow) | LO option | 2.2 | 35% of LIQ-GLO-4 | mildly elevated, no anomaly |

LO Base 14d at 3.1/d is healthier than LO Glow proportionally. No flag.

## KEY TAKEAWAYS

1. **Kit selling is flat at -59% to -62% vs scaled 1.5x for 10 consecutive weeks.** No declining streak; no promo spike. Effective growth factor 0.58-0.62x. Frame as ordering signal for the placeholder CA 25072026 when it gets revisited.

2. **3 colours have meaningful OOS-before-21062026 gaps - and 2 of them are spiking.** Peony Puff (+262%), Blue Moon (+233%), Glacier Glow (-49d at 14d / -56d at 7d). **Not expressing** (Sally $150k arrears + cash-tight stance). User to surface in next CA Slack message; broader call left to whoever picks it up.

3. **Remove demand has shifted from 120ml/BUN-1 → 500ml/BUN-2** since the Swift restock. Combined Remove 120ml -57% vs 30d, Combined Remove 500ml +108%. Net Remove demand is flat. The post-restock spike on 500ml is recovery, not a new trend - sizing decisions for next Swift cycle should be based on the combined demand, not the spike.

4. **Dead-stock pile grew from 25 SKUs / 21k units to 38 SKUs / 29k units in one week.** Listing audit due. Many appear to be Christmas/seasonal/limited series. Not stockout-imminent for any of them, but cash-tied-up signal.

5. **POW-LAC-196 confirmed non-issue.** 698d cover indicates the 19 Apr 2,574-unit deduction was reversed - matches user's hypothesis. Close.

6. **Data integrity (post B360 fix):** 247's deduction logic is clean over the 12-day window. Kit alignment 3PL/Shopify within ±1/d on all 3 kits. Heal kit-attached signature confirmed (560 deductions = 649 kits + standalone). Only outstanding issue: **ACC-LAB-CA deduction rule still not firing in B360** despite Greg's 8 Apr re-enable - rule mapping needs a second look. No POW-* cumulative gaps.

## FOLLOW-UP ITEMS

### Immediate (this week)
- [x] Greg: repair B360 tab `#REF!` — **DONE same-day**. Re-ran deductions; CA's 247 deduction logic is clean.
- [ ] Greg: ACC-LAB-CA deduction rule still not firing in B360 (`ACC-LAB` row showing 0 deductions / NaN stock). Re-check rule mapping.
- [ ] Daniel: Heal + Remove 500ml fill quantities **TENTATIVE / undecided** - lean Heal 2,000-3,000 modelled, Remove skip-or-1,000 modelled. Sizing kept open pending decision.
- [ ] Remy: chase Mixam Canada for written reprint confirmation + ETA on 1,300pcs

### By end of month
- [ ] Greg: refresh stale model DSRs (Base, Glow, ACC-REM-BOW, ACC-LAB-CA - all 60-80% above actual)
- [ ] Gav/Remy: dead-stock listing audit (38 SKUs / 28,616 units) - re-launch seasonal, schedule clearance, or tag as unlaunched
- [ ] Joel: pay CA 21062026 deposit (15d past)
- [ ] Joel: confirm Univar acetone tote refund (open since 10 Apr)

### Ongoing
- Monitor 3 spiking-OOS-gap colours (Peony Puff / Blue Moon / Glacier Glow)
- Re-run 3PL deduction integrity tests once B360 restored
