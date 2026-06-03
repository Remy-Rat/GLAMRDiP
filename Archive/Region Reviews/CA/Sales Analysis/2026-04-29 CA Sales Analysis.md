# Sales Data Analysis — CA — 29 Apr 2026

## DATA FRESHNESS
- Shopify latest: **2026-04-28** (1d ago — normal +1d lag)
- 3PL last valid: **2026-04-29** (today)
- Growth factor: **1.5x** (80/d base → 120/d scaled)
- Kit base DSRs: STA 21, COM 41, ULT 18

## Manual overrides (carrying through from POS Check)
- Customs container CA 03022026 + CA 07042026 — checked in (mass arrivals 25-26 Apr); contributed to massive single-day deduction spikes that DSR script excludes.
- POS MODEL kit-attached DSRs for liquids (Base, Glow, etc.) reflect Sally-side / kit-attached consumption, not 247 standalone deductions. Used as forward sizing tool, not 247 stockout rate.

---

## DSR: MODEL vs REALITY

### Kits — 14d Shopify

| SKU | Model DSR (1.5x) | Shop 7d | Shop 14d | Shop 30d | Gap 14d |
|---|---|---|---|---|---|
| KIT-STA-2 | 31.5 | 13.6 | 13.0 | 13.9 | **-59%** |
| KIT-COM-4 | 61.5 | 23.0 | 23.4 | 25.6 | **-62%** |
| KIT-ULT-6 | 27.0 | 9.0 | 9.8 | 10.0 | **-64%** |
| **TOTAL** | **120.0** | **45.6** | **46.2** | **49.5** | **-61%** |

- **Actual growth factor: 0.58x** (vs 1.5x scaled).
- Recommended growth factor (actual + 10%): **0.64x**.
- Selling **61.5% below scaled target. 9+ consecutive weeks at this gap.**
- **W18 (27-28 Apr) at 38.0/d kits — the lowest 2-day average of the 9-week window.** Direction: trending WORSE post-W17 recalibration.

### Heal — kit-adjusted (247 picks Heal per kit)

| Metric | Rate | Notes |
|---|---|---|
| Model DSR | 127.5/d | Greg's POS MODEL |
| Standalone Shopify 14d | 0.6/d | tiny — almost all Heal moves via kits |
| Kit-adjusted 14d | 46.8/d | matches 3PL deduction (47.9/d) |
| Gap vs model | -63% | aligned with overall kit underperformance |

**Heal IS kit-adjusted at 247.** 47.9/d 3PL ded ≈ 46.8/d kit-adj Shopify (kit sales × 1 Heal per kit + standalone). Data integrity check passes.

### Liquids — standalone Shopify only (kits ship pre-assembled from Sally)

| SKU | Model DSR (kit-attached basis) | Shop 7d | Shop 14d | Shop 30d | Gap 14d | 247 cover @ 14d std |
|---|---|---|---|---|---|---|
| LIQ-BAS-2 (Base) | 25.5 | 5.7 | 5.8 | 8.5 | **-77%** | 263d |
| LIQ-GLO-4 (Glow) | 15.0 | 2.9 | 2.9 | 4.5 | **-81%** | 548d |
| LIQ-SEA-3 (Seal) | 18.0 | 4.1 | 4.4 | 6.3 | **-76%** | 261d |
| LIQ-BON-1 (Bond) | 12.0 | 2.1 | 2.1 | 2.8 | **-82%** | 502d |
| LIQ-SEN-2 | 6.0 | 1.6 | 1.6 | 3.2 | **-73%** | 493d |
| LIQ-SEN-4 | 4.5 | 1.6 | 1.4 | 2.3 | **-69%** | 459d |
| LIQ-SOA-6 | 12.0 | 1.9 | 1.9 | 2.9 | **-84%** | TBD |
| LIQ-MAT-4 | 10.5 | 2.4 | 2.5 | 3.4 | **-76%** | TBD |

All liquids sit 70-85% below model on standalone rate. **Standalone-rate cover at 247 ranges 260-548d** — not stockout territory. (Kit-attached consumption is real but happens at Sally's CN factory inside finished kits, not at 247.)

### Remove products

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap 14d | Note |
|---|---|---|---|---|---|---|
| ACC-REM (120ml) | 46.5 | 5.3 | 11.9 | 18.5 | **-74%** | 7d slowing further (-71% vs 30d) |
| ACC-REM-500 (500ml) | 75.0 | **15.7** | 8.4 | 3.9 | **-89%** | **bouncing back post-restock — see spikes** |
| ACC-REM-BOW (Bowl) | 60.0 | 1.1 | 2.1 | 3.5 | **-96%** | model is 80/d but actual 2.1/d standalone. Bowl bundle (BUN-2) lifts 3PL ded to 13.1/d — still -78% under model |

### Top 20 Colours (14d volume)

All top sellers at -40% to -64% vs model. Total colour DSR: 7d=339.7, 14d=351.9. Top 5:

| SKU | Name | Shop 14d | Stock | Cover @ 14d |
|---|---|---|---|---|
| POW-CLE-193 | Cleopatra | 17.6 | 15,218 | 864d ⚠️ |
| POW-POS-184 | (unknown) | 14.7 | (post-arrival) | depending on stock — verify after 26 Apr check-in |
| POW-HEA-515 | (unknown) | 13.7 | (post-arrival) | — |
| POW-PIL-194 | Pillow | 12.7 | (post-arrival) | — |
| POW-MON-005 | Moon Magic | 10.1 | (post-arrival) | — |

**POW-CLE-193 at 864d cover** — extreme overstock continuing.

---

## WEEKLY KIT TREND (8 weeks)

| Week | Dates | Daily kits | vs 1.5x target |
|---|---|---|---|
| W10 | 03-08 Mar | 61.0 | -49% |
| W11 | 09-15 Mar | 70.9 | -41% |
| W12 | 16-22 Mar | 65.6 | -45% |
| W13 | 23-29 Mar | 52.7 | -56% |
| W14 | 30 Mar-05 Apr | 47.6 | -60% |
| W15 | 06-12 Apr | 55.4 | -54% |
| W16 | 13-19 Apr | 52.1 | -57% |
| W17 | 20-26 Apr | 46.1 | **-62%** |
| W18 | 27-28 Apr (2d) | 38.0 | **-68%** |

- **No improving trajectory.** W11 was the peak (70.9/d). Every week since is worse on a 4-week trailing average.
- W18 partial reads as the worst single 2-day window — but only 2 days, watch through Friday before locking the read.
- Kit mix stable: COM 51%, STA 28%, ULT 21%. Roughly aligned with model split (Base 17.5% / 51.3% / 22.5%).

---

## REALISTIC DAYS COVER (key SKUs)

Already covered in POS Check. Headline: kits all 329-352d cover, liquids 260-550d, ACC-REM-BOW 437d. Region is post-customs-arrival in heavy overstock at actual demand rates.

The exception is Glacier Glow (POW-GLA-CS02) at 49 units / 1.1/d standalone = 45d, with -23d gap to CA 21062026 arrival.

---

## CONTAINER ARRIVALS DETECTED (from 3PL data)

| Date | SKUs | Total Units | Top SKUs | Match |
|---|---|---|---|---|
| 03 Apr | 9 | 14 | POW-PIL-194, POW-CRU-328, POW-POS-184 | minor adjustment |
| 18 Apr | 12 | 2,010 | POW-PRI-012 +1,000, POW-TWI-L08 +1,000 | **Swift fill leg** (Heal/Remove 500ml + small adjustments) |
| 23 Apr | 10 | 10 | minor — likely cycle count adjustments |
| **25 Apr** | **21** | **31,606** | **ACC-INS +10,034, KIT-COM-4 +4,767, ACC-REM-BOW +4,485** | **Customs container CA 03022026 + 07042026 (partial)** |
| **26 Apr** | **90** | **59,425** | **ACC-THA +8,303, POW-POS-184 +3,578, POW-HEA-515 +2,384** | **Customs container CA 03022026 + 07042026 (main)** |

**The customs container landed 25-26 Apr across two days. ~91k units / 111 SKU entries.** Manifest was 94,268 units / 104 SKUs — close match (some line items may have hit on 23/25 Apr). Reconciliation worth verifying with Greg over the next week.

---

## INVENTORY DISCREPANCIES

### 5A — Single-day red flags (flagged by deductions.py)

| Date | SKU | Deduction | Benchmark | Class | Action |
|---|---|---|---|---|---|
| 30 Mar | ACC-THA | 29,578 | 735 | **Container restock event** (positive) | not a deduction — likely script flagged as movement |
| 13 Apr | STO-MAI-2 | 11,077 | 330 | **Restock event** (positive) | n/a |
| 15 Apr | STO-BUB-BAG-L | 10,053 | 435 | **Restock event** (positive) | n/a |
| 24 Mar | POW-EMB-602 | 5,702 | 35 | **⚠️ Unexplained spike** — but already flagged Mar | confirmed previous review |
| 16 Mar | POW-HAR-139 | 2,577 | 35 | **⚠️ Unexplained spike** | already escalated |
| **19 Apr** | **POW-LAC-196 (Lace)** | **2,574** | **35** | **⚠️ Unexplained — investigation underway** | **user investigating** |
| 8 Apr | ACC-NAI-240 | 1,581 | 90 | bundle/correction — verify | low priority |
| 5 Apr | POW-TEM-627 | 1,106 | 35 | unexplained | minor |
| 2 Apr | POW-DAY-025 | 1,101 | 35 | unexplained | minor |
| 11 Apr | POW-MOO-401 | 1,101 | 35 | unexplained | minor |

### 5B — Cumulative gap test (3PL > Shopify by 30d)

Critical to verify whether colour SKU stock accounts are short:

- **POW-LAC-196 (Lace):** 3PL 30d ded ~287/d × 30 = 8,610 vs Shopify ~1.5/d × 30 = 45. **Gap: ~8,565 units across 30d, traceable to single 19 Apr spike.** Investigation underway with 247 — expected to be a stock event, not real demand.
- Other top-volume colours show 30d 3PL ded reasonably aligned with Shopify within bundle/kit-pick allowances.

### 5C — Stock gains (positive)

- 25-26 Apr customs check-in (covered above).
- Smaller positive movements on 18 Apr (Swift) and 3/23 Apr (cycle count adjustments).

### 5D — Component transfers

No active component transfers in window — the Swift fill leg (ACC-RE5-BOT etc → Swift) happened pre-window in March.

---

## 3PL DEDUCTION CHECK (kits, excluding container days)

| SKU | 3PL Ded/d | Shopify/d | Gap | Status |
|---|---|---|---|---|
| KIT-STA-2 | 12.5 | 13.0 | -0.5 | **ALIGNED** |
| KIT-COM-4 | 23.4 | 23.4 | +0.0 | **ALIGNED** |
| KIT-ULT-6 | 9.7 | 9.8 | -0.1 | **ALIGNED** |

**Data integrity good for kits.** Greg's deduction logic at 247 is firing correctly.

---

## SELLING PERFORMANCE FLAGS

### Sales Spikes (7d > 30d by 50%+)

| SKU | 7d | 14d | 30d | Spike vs 30d |
|---|---|---|---|---|
| ACC-REM-BUN-2 (Remove 500ml + Bowl bundle) | 10.1 | 5.4 | 2.5 | **+304%** |
| ACC-REM-500 (Remove 500ml standalone) | 15.7 | 8.4 | 3.9 | **+303%** |

**Driver:** Remove 500ml restocked from Swift on 18 Apr, post-OOS catch-up. Customers who were waiting and the BUN-2 bundle both spiked. Expected behaviour. Watch whether 7d rate sustains over the next 14d.

### Sales Drops (7d < 30d by 40%+)

15 SKUs flagged. Notable:
- **ACC-REM (Remove 120ml)** — 5.3/d 7d vs 18.5/d 30d (**-71%**). Fundamental slowdown OR cannibalised by Remove 500ml restock.
- **ACC-REM-BOW (Remove Bowl)** — 1.1/d vs 3.5/d (**-69%**). Same dynamic.
- **POW-RAD-043 (Radiant)** — 1.0/d vs 4.0/d (-75%). Was reset to 0 on 10 Apr (Gav's request, ShipHero edit). Possibly listing issue still — verify with 247.
- **POW-CHA-047, POW-SER-039, POW-BLO-042** — 70%+ drops on slower-moving colours; less concerning.

### Dead Stock (in stock at 247, 0 Shopify in 14d)

**25 colour SKUs / ~21,000 units sitting at 247 with zero customer demand in 14d.** All real CA stock (Dippi `D-POW-*` prefix is Nordic-only; CA codes with embedded "D"/"L" letters in the suffix are legitimate CA SKUs).

Top idle SKUs:

| SKU | Units idle |
|---|---|
| POW-WHI-L12 | 1,400 |
| POW-POP-D109 | 1,316 |
| POW-LUC-D110 | 1,223 |
| POW-DAZ-L03 | 1,199 |
| POW-JUB-L11 | 1,025 |
| POW-TWI-L08 | 1,000 |
| POW-ANG-D09 | 994 |
| POW-DRE-D037 | 891 |
| POW-DRE-D08 | 809 |
| POW-CON-L02 | 800 |
| POW-CAN-016 | 2,077 |
| POW-REI-008 | 1,327 |
| POW-FES-006 | 735 |

**Action:** Listing audit — confirm each is live on the CA Shopify, has visible stock, and isn't blocked by a sync issue. If genuinely de-listed, flag as discontinued and stop tracking demand against it.

### Sensitive Base Signal

| Variant | 14d Shop | Share |
|---|---|---|
| LIQ-BAS-2 (Base) | 5.8 | 78% |
| LIQ-SEN-2 (Sensitive Base) | 1.6 | 22% |

22% Sensitive — close to model's 30% assumption. Mix is healthy.

---

## KEY TAKEAWAYS

1. **9-week underselling consistent and slightly worsening.** W18 day-1-2 at -68% vs scaled 1.5x target. 0.58x actual growth factor. The 1.5x recalibration on 22 Apr does not change the demand picture — only the planning baseline.
2. **Customs container check-in confirmed.** 25-26 Apr arrivals account for ~91k units; reconciles to the 94k manifest within margin. Any short-receipts will surface in 247's reconciliation over the next week.
3. **POW-LAC-196 (Lace) anomaly** — 2,574-unit 19 Apr deduction has no Shopify offset. ~8,565-unit 30d cumulative gap. User investigating with 247.
4. **Remove 500ml + BUN-2 spike (+304%)** — expected post-restock catch-up. Monitor whether 7d rate sustains. Validates that the 14d rate (8.4/d standalone) understates the real ongoing demand. **Don't size the next Remove 500ml fill purely off 14d.**
5. **Liquid standalone DSR all 70-85% below model** — same direction as kits, slightly steeper. Consistent with 247 not picking liquids per kit (kits ship pre-assembled).
6. **Kit data integrity intact.** 3PL kit deductions match Shopify within 0.5/d. Greg's 247 deduction logic is firing.
7. **Dead stock at 247: 25 colour SKUs / ~21,000 units idle 14d.** All real CA stock. Top: POW-CAN-016 (2,077), POW-WHI-L12 (1,400), POW-POP-D109 (1,316). Worth a Shopify listing audit.
8. **Heal kit-adjusted rate (46.8/d) matches 3PL ded (47.9/d).** Heal-per-kit attach at 247 is working correctly.

---

## FOLLOW-UP ITEMS

- [ ] POW-LAC-196 (Lace) 19 Apr deduction investigation (user)
- [ ] Verify 25-26 Apr customs container reconciliation against 94k manifest (Greg/247)
- [ ] Listing audit on 25 dead-stock CA colour SKUs (~21,000 units idle 14d) — Gav/Remy
- [ ] POW-RAD-043 (Radiant) 7d drop — confirm listing live and stock not zeroed-out (247)
- [ ] Watch ACC-REM-500 + BUN-2 spike sustainment over next 14d before sizing next fill
- [ ] Consider whether Remove 120ml -71% drop reflects cannibalisation by Remove 500ml or genuine slowdown
- [ ] Greg: POS MODEL DSR refresh — Base/Glow/liquids show 70-85% under standalone Shopify; ACC-REM-BOW model 80/d still vs actual 13.1/d
