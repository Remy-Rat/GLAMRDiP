# SALES DATA ANALYSIS — UK — 15 Apr 2026

## DATA FRESHNESS
- **Shopify:** 14 Apr 2026 (1d ago)
- **3PL (B360):** 15 Apr 2026 (0d ago) -- **B360 data only. No Fulfillable tab yet.** Stock figures below use POS MODEL "Fulfillable" column as source of truth.
- **Growth factor:** 1.1x
- **POS MODEL base:** 84/day (STA 10 + COM 37 + ULT 37) | Scaled: 92.4/day
- **Easter Sale ran 4-12 Apr** across all regions. W15 (6-12 Apr) shows the spike, W16 is post-sale normalisation.

> **3PL data caveat:** B360 stopped fulfilling 13 Apr. Fulfillable is now live but has no tab in the Order Schedule. B360 tab data is historical — deduction rates are still valid for DSR validation (same Shopify orders), but stock levels reflect B360 remaining inventory (being transferred), NOT current Fulfillable stock. POS MODEL "Fulfillable" column is the operational stock source of truth.

---

## DSR: MODEL vs REALITY

### Kits
| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap 14d |
|-----|-----------|---------|----------|----------|---------|
| KIT-STA-2 | 11.0 | 16.4 | 15.0 | 14.1 | **+36%** |
| KIT-COM-4 | 40.7 | 29.3 | 27.9 | 26.3 | **-31%** |
| KIT-ULT-6 | 40.7 | 48.0 | 47.7 | 43.1 | +17% |
| **TOTAL** | **92.4** | **93.7** | **90.6** | **83.5** | **-1.9%** |

- **Actual growth factor: 1.08x** (90.6 actual / 84 base)
- Recommended (actual + 10% buffer): **1.19x**
- vs scaled target: **-1.9%** -- essentially aligned. Model is accurate at the aggregate level.
- Kit mix is skewed: ULT dominates at 53% of volume (model: 44%), COM underperforming at 31% (model: 44%), STA overperforming at 17% (model: 12%)

### Heal (kit-adjusted: standalone + kit consumption at Fulfillable)
| SKU | Model DSR | Standalone 7d | Standalone 14d | Kit-Adj 7d | Kit-Adj 14d | Gap |
|-----|-----------|---------------|----------------|------------|-------------|-----|
| LIQ-HEA-5 | 93.5 | 1.7 | 1.6 | 95.4 | 92.2 | -1% |

Heal model is accurate. Kit-adjusted rate aligned with model.

### Base & Glow (kit-adjusted -- CRITICAL MODEL ERROR)
In UK, Fulfillable picks Base and Glow per kit order (confirmed 13 Apr). POS MODEL still uses standalone rates.

| SKU | Model DSR | Standalone 14d | Kit-Adj 14d | Model Error |
|-----|-----------|----------------|-------------|-------------|
| LIQ-BAS-2 | 22.0 | 5.6 | **96.2** | **Model understated by 77%** |
| LIQ-GLO-4 | 11.0 | 7.1 | **97.7** | **Model understated by 89%** |

Greg must update POS MODEL DSR for Base and Glow to reflect kit-adjusted demand. Every days cover figure in the model is ~4x overstated for these SKUs.

### Liquids (standalone -- pre-packed in kits from CN)
| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap 14d |
|-----|-----------|---------|----------|----------|---------|
| LIQ-SEA-3 | 13.2 | 10.9 | 9.9 | 9.3 | -25% |
| LIQ-BON-1 | 5.5 | 2.9 | 2.9 | 2.7 | -47% |
| LIQ-MAT-4 | 6.6 | 4.0 | 4.0 | 3.3 | -39% |
| LIQ-SOA-6 | 5.5 | 1.6 | 2.0 | 1.9 | -64% |
| LIQ-SEN-2 | 0.0 | 0.0 | 0.0 | 0.0 | -- |
| LIQ-SEN-4 | 0.0 | 0.0 | 0.0 | 0.0 | -- |

All standalone liquids selling below model. Bond (-47%), Soak (-64%), Matte (-39%) — model DSRs are stale. These are manually updated from monthly sales. Recent weeks are consistently lower.

### Remove Products (standalone, but bundles inflate 3PL deductions)
| SKU | Model DSR | Shop 14d | 3PL Ded/d | Bundle Effect |
|-----|-----------|----------|-----------|---------------|
| ACC-REM | 33.0 | 19.1 | 25.5 | +6.4/d from ACC-REM-BUN-1 |
| ACC-REM-500 | 30.8 | 14.5 | 21.8 | +7.3/d from ACC-REM-BUN-2 |
| ACC-REM-BOW | 26.4 | 3.0 | 16.2 | +13.2/d from both bundles |

Remove Bowl model DSR (26.4) is heavily overstated vs actual depletion rate (16.2). Same pattern as CA -- Greg may have set model DSR from 3PL deduction rates including bundle decomposition rather than actual selling rate.

### Top 15 Colours (by 14d volume)
| SKU | Model | Shop 14d | Gap | Name |
|-----|-------|----------|-----|------|
| POW-CLE-193 | 35.2 | 33.7 | -4% | Clear |
| POW-HEA-515 | 29.7 | 30.5 | +3% | Heaven |
| POW-POS-184 | 30.8 | 26.6 | -14% | Positivi-Tea |
| POW-PIL-194 | 20.9 | 22.2 | +6% | Pillow Talk |
| POW-YOU-256 | 16.5 | 19.4 | +18% | You're The One |
| POW-OAK-283 | 15.4 | 19.1 | +24% | Oak |
| POW-TRA-452 | 16.5 | 18.4 | +12% | Train-Wreck |
| POW-SWE-001 | 18.7 | 18.0 | -4% | Sweetheart |
| POW-BLA-384 | 17.6 | 17.6 | +0% | Black Cherry |
| POW-CHA-011 | 14.3 | 17.5 | +22% | Charmer |
| POW-PEA-068 | 13.2 | 16.2 | +23% | Peachy |
| POW-BAR-198 | 14.3 | 16.1 | +13% | Bare Necessity |
| POW-HAR-139 | 13.2 | 16.0 | +21% | Harmony |
| POW-SIN-254 | 14.3 | 15.9 | +11% | Sincere |
| POW-ILL-001 | 13.2 | 15.6 | +18% | Illusion |

Total colour 14d DSR: **823/day**. Most top colours are selling at or above model. No major colour-level discrepancies.

### Bundle: LIQ-SET (Liquids Set)
- 14d: 0.3/day — negligible. Each sale deducts 1x of all 6 liquids at 3PL. Accounts for ~0/d of 3PL-Shopify gap per liquid.

### Sensitive Base Signal
- Base: 5.6/d standalone (100%) | Sensitive: 0.0/d (0%)
- Zero Sensitive Base demand in UK. Model assumes 0 -- aligned. No need to stock.

---

## WEEKLY KIT TREND

| Week | Dates | Days | Total | Daily | vs Model |
|------|-------|------|-------|-------|----------|
| W8 | 16-22 Feb | 7 | 500 | 71.4 | -22.7% |
| W9 | 23 Feb-1 Mar | 6 | 453 | 75.5 | -18.3% |
| W10 | 2-8 Mar | 7 | 543 | 77.6 | -16.0% |
| W11 | 9-15 Mar | 7 | 585 | 83.6 | -9.5% |
| W12 | 16-22 Mar | 7 | 473 | 67.6 | -26.8% |
| W13 | 23-29 Mar | 7 | 610 | 87.1 | -5.7% |
| W14 | 30 Mar-5 Apr | 7 | 583 | 83.3 | -9.8% |
| **W15** | **6-12 Apr** | **7** | **671** | **95.9** | **+3.8%** |
| W16* | 13-14 Apr | 2 | 166 | 83.0 | -10.2% |

- **Upward trajectory:** W8 (71.4) to W15 (95.9) = +34% over 8 weeks. No 3 consecutive declines.
- **W15 Easter spike:** first week above model in the window. Easter Sale ran 4-12 Apr.
- **W12 dip** (67.6) was an outlier sandwiched between stronger weeks.
- **W11 bump** (83.6) — UK Mother's Day Sale ran 9-15 Mar.
- Post-sale normalisation expected for W16. Early data (83.0/d) is below model but still in the healthy range.

### Kit Mix (14d vs Model)
| Kit | 14d DSR | % of Total | Model % | Gap |
|-----|---------|------------|---------|-----|
| KIT-STA-2 | 15.0 | 17% | 12% | Over-indexed |
| KIT-COM-4 | 27.9 | 31% | 44% | **Under-indexed** |
| KIT-ULT-6 | 47.7 | 53% | 44% | Over-indexed |

Complete Kit is the weak link. Selling 31% below model. CRO team has GLMR-0017 (Replace 2/4/6 kit to 3/6/9) in discussion with Pratik -- may impact kit mix if implemented.

---

## REALISTIC DAYS COVER

Using POS MODEL "Fulfillable" stock as source of truth. Actual DSR uses kit-adjusted rates where applicable.

### Kits & Liquids
| SKU | Stock | Model Cover | Actual DSR | Actual Cover | Status |
|-----|-------|-------------|------------|--------------|--------|
| **KIT-STA-2** | 367 | 33d | 15.0 | **24d** | CRITICAL -- stocks out ~10 May |
| KIT-COM-4 | 4,451 | 109d | 27.9 | 160d | OK |
| KIT-ULT-6 | 4,579 | 113d | 47.7 | 96d | OK |
| LIQ-HEA-5 | 9,532 | 102d | 92.2 (kit-adj) | 103d | OK |
| **LIQ-BAS-2** | 1,469 | 67d | 96.2 (kit-adj) | **15d** | CRITICAL -- stocks out ~30 Apr |
| **LIQ-GLO-4** | 1,499 | 136d | 97.7 (kit-adj) | **15d** | CRITICAL -- stocks out ~30 Apr |
| LIQ-SEA-3 | 3,094 | 234d | 9.9 | 313d | OK |
| LIQ-BON-1 | 629 | 114d | 2.9 | 217d | OK |
| LIQ-MAT-4 | 842 | 128d | 4.0 | 211d | OK |
| LIQ-SOA-6 | 638 | 116d | 2.0 | 319d | OK |

### Remove Products
| SKU | Stock | Model Cover | Actual DSR (3PL-adj) | Actual Cover | Status |
|-----|-------|-------------|----------------------|--------------|--------|
| ACC-REM | 2,163 | 66d | 25.5 | 85d | OK |
| ACC-REM-500 | 4,794 | 156d | 21.8 | 220d | OK |
| ACC-REM-BOW | 5,487 | 208d | 16.2 | 339d | OK |

### Inserts, Labels & Packaging
| SKU | Stock | Model Cover | 3PL Ded/d | Actual Cover | Status |
|-----|-------|-------------|-----------|--------------|--------|
| ACC-INS | 10,341 | 115d | 77.5 | 133d | OK |
| ACC-THA | 26,435 | 144d | 139.3 | 190d | OK |
| **ACC-LAB-UK** | 9,235 | 50d | 139.3 | **66d** | WATCH -- no inbound confirmed |
| **STO-BUB-BAG-L** | 13,543 | 150d | 79.4 | 171d | OK |
| STO-MAI-BAG-S | 11,704 | 125d | 62.6 | 187d | OK |
| STO-MAI-2 | 9,384 | 100d | 62.8 | 149d | OK |

### Colours
| Status | Count |
|--------|-------|
| OOS | 45 |
| Critical (<30d) | 8 |
| Warning (30-60d) | 25 |
| OK (60d+) | 144 |

**Critical colours (<30d):**
- POW-SEA-450 Seaside: 161 units, 21d
- POW-SIN-254 Sincere: 329 units, 23d
- POW-PEA-068 Peachy: 309 units, 23d
- POW-JUS-449 Just Friends: 134 units, 24d
- POW-BUB-516 Bubbly: 161 units, 24d
- POW-FAI-308 Fairytale: 163 units, 25d
- POW-CRU-090 Crush: 163 units, 30d
- POW-GOD-017 Goddess: 164 units, 30d

Sincere and Peachy are both top-15 sellers. Stocking out before UK 03062026 (8 Jun) is likely. B360 Packup stock may include these — unconfirmed.

---

## CONTAINER ARRIVALS DETECTED

### From 3PL data (B360 tab)
| Date | SKUs | Units | Notes |
|------|------|-------|-------|
| 14 Apr 2026 | 194 | +2,409 | B360 reconciliation / Packup prep. Small increases across many SKUs (ACC-LAB +253, ACC-THA +253, STO-MAI-2 +156). Not a container check-in — likely B360 stock count adjustments. |

### POS MODEL Shipments
| Reference | Status | Est Completion | Est Arrival |
|-----------|--------|----------------|-------------|
| B360 PACKUP STOCK | In Production | -- | -- |
| UK 03062026 | On the Way | 14 Apr | **8 Jun** |
| UK 02072026 | In Production | 18 May | 12 Jul |
| UK 02082026 | -- | 22 Jun | 16 Aug |

---

## INVENTORY DISCREPANCIES

### Red Flag Deductions (single-day > benchmark)

**Stock Transfers (B360 transition — expected, not alarming):**
| Date | SKU | Deduction | Benchmark | Likely Cause |
|------|-----|-----------|-----------|--------------|
| 25 Mar | LIQ-SEA-3 | 1,663 | 60 | Bulk dispatch to Fulfillable/filler |
| 25 Mar | LIQ-BAS-2 | 1,657 | 90 | Bulk dispatch to Fulfillable/filler |
| 25 Mar | LIQ-GLO-4 | 1,657 | 45 | Bulk dispatch to Fulfillable/filler |
| 31 Mar | KIT-ULT-6 | 859 | 200 | Kit transfer to Fulfillable |
| 7 Mar | KIT-COM-4 | 608 | 200 | Kit transfer to Fulfillable |

These are B360→Fulfillable stock transfers in preparation for the 13 Apr go-live. Three liquids dispatched on 25 Mar likely went to Chemence (Base, Glow) and Oils4Life (potentially). Kits went to Fulfillable.

**Batch Processing / Elevated Deductions:**
| Date | SKU | Deduction | Benchmark | Notes |
|------|-----|-----------|-----------|-------|
| 11 Mar | LIQ-GLO-4 | 873 | 45 | Likely filler dispatch or B360 adjustment |
| 11 Mar | 8 colours | 66-111 | 35 | Elevated colour deductions, batch processing |
| 5 Mar | 3 colours | 65-84 | 35 | Same pattern |

The 11 Mar and 5 Mar colour deductions are elevated but pattern across multiple SKUs suggests batch B360 processing, not stock loss.

### 3PL Data Integrity Note
With B360 no longer fulfilling as of 13 Apr, the B360 tab data from here forward is unreliable for operational deduction tracking. Greg needs to set up a Fulfillable tab (or ShipHero integration) for ongoing analysis.

---

## 3PL DEDUCTION CHECK (kits, 14d)

| SKU | 3PL Ded/d | Shopify/d | Gap | Status |
|-----|-----------|-----------|-----|--------|
| KIT-STA-2 | 15.4 | 15.0 | +0.4 | ALIGNED |
| KIT-COM-4 | 30.8 | 27.9 | +2.9 | ALIGNED |
| KIT-ULT-6 | 48.4 | 47.7 | +0.7 | ALIGNED |

Kits are clean. B360 deduction rates match Shopify sales within tolerance. Data integrity is solid for the pre-transition period.

### Liquids (3PL vs Shopify)
| SKU | 3PL Ded/d | Shopify/d | Gap | Status |
|-----|-----------|-----------|-----|--------|
| LIQ-HEA-5 | 79.4 | 1.6 | +77.8 | Expected — kit consumption at 3PL |
| LIQ-BAS-2 | 1.4 | 5.6 | -4.2 | Aligned — B360 had minimal Base stock |
| LIQ-GLO-4 | 6.7 | 7.1 | -0.4 | Aligned |
| LIQ-SEA-3 | 9.9 | 9.9 | +0.0 | Aligned |
| LIQ-BON-1 | 2.9 | 2.9 | +0.0 | Aligned |

Heal shows the expected kit-adjusted gap — B360 was deducting Heal per kit before transition. Base and Glow 3PL deductions are low because B360 had minimal stock of these (most was already at Fulfillable or local filler). **Fulfillable's deduction rate for Base and Glow should be ~96-98/d once data is available.**

---

## SELLING PERFORMANCE FLAGS

### Sales Spikes (7d > 30d by 50%+)
All spikes are low-volume colours (0.6-1.1/d baseline). Likely natural variance, not material to stock planning.

| SKU | 7d | 14d | 30d | Spike | Name |
|-----|-----|-----|-----|-------|------|
| POW-LUS-015 | 1.9 | 1.3 | 0.8 | +137% | Lustre |
| POW-DRE-D08 | 1.6 | 1.2 | 0.7 | +129% | Dreamer |
| POW-GLI-007 | 1.4 | 0.9 | 0.7 | +100% | Glitter |

Not flagging as actionable — absolute volumes too small.

### Sales Drops (7d < 30d by 40%+)
| SKU | 7d | 14d | 30d | Drop | Name | Likely Cause |
|-----|-----|-----|-----|------|------|-------------|
| **POW-ICE-266** | 0.7 | 0.4 | 3.4 | **-79%** | Iced Latte | Check if OOS on website or delisted |
| **POW-BOU-222** | 3.9 | 8.4 | 13.6 | **-71%** | Bouquet | 30d avg inflated by Easter Sale peak; post-sale normalisation + possible OOS check |

POW-BOU-222 (Bouquet) is the bigger concern — was a top-20 seller (13.6/d 30d avg) but collapsed to 3.9/d in 7d. 14d at 8.4 shows the decline is accelerating. Check Shopify listing status.

### Overperformers (>20% above model DSR)
| SKU | Model | Actual 14d | Gap | Name |
|-----|-------|------------|-----|------|
| KIT-STA-2 | 11.0 | 15.0 | +36% | Starter Kit — stocks out faster |
| POW-EMB-602 | 8.8 | 14.4 | +64% | Embrace — trending significantly |
| POW-OAK-283 | 15.4 | 19.1 | +24% | Oak |
| POW-PEA-068 | 13.2 | 16.2 | +23% | Peachy — already critical cover |
| POW-CHA-011 | 14.3 | 17.5 | +22% | Charmer |
| POW-HAR-139 | 13.2 | 16.0 | +21% | Harmony |

POW-EMB-602 (Embrace) at +64% is the standout. Not in the critical cover list but model DSR is significantly underestimating actual demand.

### Underperformers (>40% below model DSR)
| SKU | Model | Actual 14d | Gap | Notes |
|-----|-------|------------|-----|-------|
| LIQ-SOA-6 | 5.5 | 2.0 | -64% | Soak — model stale |
| ACC-REM-500 | 30.8 | 14.5 | -53% | Remove 500ml — model stale |
| LIQ-BON-1 | 5.5 | 2.9 | -47% | Bond — model stale |
| ACC-REM | 33.0 | 19.1 | -42% | Remove 120ml — model stale |
| ACC-REM-BOW | 26.4 | 3.0 | -89% | Remove Bowl — model includes bundle decomposition |

Model DSR is stale for all liquids and Remove products. Manually updated from monthly sales. Current selling is consistently lower across the board.

### Dead Stock (in stock, 0 Shopify sales in 14d)
- **1 colour:** POW-HOL-022 (Holiday), 200 units. Likely unlaunched or seasonal holdover.

### CRO Context
From #cro-team-meetings:
- **GLMR-0008 Kit video experiment**: Positive, implementing. +4.66% conversion uplift. Could boost kit sales 4-5% going forward.
- **GLMR-0012 Sticky colour bar**: Launched ~8 Apr, testing in UK. May boost ARPU via easier colour adds.
- **GLMR-0013 Colour selector popup**: Being re-launched after bug check.

These CRO wins could push actual selling rates higher. Monitor next 2-4 weeks for lift.

---

## KEY TAKEAWAYS

1. **Base and Glow at 15d actual cover — Chemence fill is make-or-break.** POS MODEL shows 67d and 136d cover because it uses standalone DSR (22/d and 11/d). Actual kit-adjusted demand is ~96-98/d. Chemence 8,000 Base dispatches 28 Apr, 8,000 Glow ~29 Apr. Zero-day margin. **If either fill slips by 2 days, kits can't ship.** Greg must update model DSRs immediately.

2. **KIT-STA-2 at 24d cover (stocks out ~10 May).** 367 units at 15/d actual. B360 Packup has ~496 STA kits that could extend to ~11 Jun if transferred promptly. UK 03062026 arrives 8 Jun. Need the Packup transfer confirmed or STA added to an earlier fill.

3. **Growth factor is accurate at 1.1x.** Actual: 1.08x. Recommended: 1.19x. Unlike AUS (0.83x actual) and CA (0.66x actual), UK selling is essentially at target. No ordering adjustment needed on this front.

4. **8 colours in critical cover (<30d), including top sellers Sincere (23d) and Peachy (23d).** 45 colours OOS. Some OOS colours likely have stock in B360 Packup — need the transfer to happen to restore availability.

5. **B360 data going stale — Greg needs a Fulfillable tab.** All operational 3PL analysis from here forward requires either a Fulfillable tab in the Order Schedule or ShipHero data exports from Benedict. Without this, weekly sales analysis loses its 3PL validation layer.
