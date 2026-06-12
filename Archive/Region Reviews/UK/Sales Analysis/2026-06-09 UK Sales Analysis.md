# 🇬🇧 UK Sales Data Analysis — 9 Jun 2026

## Data Freshness

- Shopify latest: 2026-06-07 (2d ago; +1d lag normal)
- 3PL: Fulfillable deduction integrity BLIND (5th cycle). 3PL kit-deduction alignment check unavailable.
- POS MODEL extracted: 2026-06-09 11:43
- Growth factor: 1.3x | Base 89/d → Scaled 115.7/d

---

## DSR: Model vs Reality

### Kits

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap 14d |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 6.5 | 0.1 | 0.6 | 3.5 | **-91%** |
| KIT-COM-4 | 68.9 | 89.4 | 73.9 | 68.2 | **+7%** |
| KIT-ULT-6 | 40.3 | 17.4 | 21.6 | 31.7 | -46% |
| **TOTAL** | **115.7** | **106.9** | **96.1** | | |

- **Actual growth: 1.08x. Target 1.3x. Gap -16.9%.** Recommended (actual+10%) = 1.19x.
- Per [[growth-factor-framing]] — hold 1.3x for ordering; flag overstock risk on future ULT containers.

### Kit Mix (14d)

- KIT-COM-4: **77% of mix** (was ~69% in 26 May Sales Analysis). Continuing to consolidate.
- KIT-ULT-6: 22%.
- KIT-STA-2: 1%. STA effectively dead — substitution to COM is permanent.

**Model still expects:** STA 6%, COM 60%, ULT 35%. Per-kit model DSRs need refresh by Greg:
- KIT-STA-2: 6.5 → ~1 (matches dead state)
- KIT-COM-4: 68.9 → 78-90 (running hotter than model)
- KIT-ULT-6: 40.3 → 22-28 (running cooler)

### Heal (kit-adjusted)

- Model: 118.3/d
- Standalone Shopify 14d: 1.4/d (negligible — almost entirely kit-pulled)
- Kit-adjusted 14d: 97.5/d (kit total 96.1 + 1.4 standalone). Gap **-18%** vs model.
- Kit-adjusted 7d: 108.3/d (kit total 106.9 + 1.4). Closer to model as W23 recovers.

### Liquids (standalone)

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap 14d | Note |
|---|---:|---:|---:|---:|---:|---|
| LIQ-BAS-2 | 144.3 | 19.7 | 19.1 | 21.3 | -87% | Kit-adjusted (model = std + kit) |
| LIQ-GLO-4 | 128.7 | 10.6 | 9.9 | 10.3 | -92% | Kit-adjusted |
| LIQ-SEA-3 | 15.6 | 11.0 | 10.6 | 13.3 | -32% | Standalone |
| LIQ-BON-1 | 6.5 | 3.3 | 3.1 | 3.4 | -52% | Standalone |
| LIQ-MAT-4 | 7.8 | 2.0 | 2.4 | 2.4 | -69% | Standalone |
| LIQ-SOA-6 | 6.5 | 2.4 | 2.1 | 2.1 | -68% | Standalone |
| LIQ-SEN-2 | 0 | 0 | 0 | 0 | n/a | Discontinued |
| LIQ-SEN-4 | 0 | 0 | 0 | 0 | n/a | Discontinued |

Base + Glow gaps look extreme on standalone view; actually model = kit-adjusted, so the real picture is: kit-adjusted Base = 115.7 + 19.1 = **134.8/d** vs model 144.3 = **-7%** (essentially aligned).

Note: LIQ-MAT-4 / LIQ-SOA-6 / LIQ-BON-1 all 50-70% below model on standalone — these are kit-pre-packed (CN). The model DSRs are stale (per [[uk-discontinued-liquids]] and 2 Jun refresh list). Greg refresh batch pending.

### Remove Products (standalone)

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap 14d | Note |
|---|---:|---:|---:|---:|---:|---|
| ACC-REM | 59.8 | 2.4 | 2.0 | 3.5 | -97% | Bundle drives most (ACC-REM-BUN-1) |
| ACC-REM-500 | 36.4 | 75.0 | 66.5 | 40.6 | **+83%** | Sustained spike (was +136% on 2 Jun) |
| ACC-REM-BOW | 66.3 | 1.1 | 0.9 | 0.7 | -99% | Bundle drives (ACC-REM-BUN-2) |

**ACC-REM-500 +83% sustained over 30d.** 7d (75/d) > 14d (66.5) > 30d (40.6) — still accelerating, not normalising. Cover at actual 41d → OOS ~20 Jul. Locks the Liquipak replacement timing.

---

## Weekly Kit Trend (last 9 weeks)

| Week | Dates | Daily | vs Model |
|---|---|---:|---:|
| W15 | 6-12 Apr | 95.9 | -17.1% |
| W16 | 13-19 Apr | 83.6 | -27.7% |
| W17 | 20-26 Apr | 63.0 | -45.5% |
| W18 | 27 Apr-3 May | 76.0 | -34.3% |
| W19 | 4-10 May | 79.7 | -31.1% |
| W20 | 11-17 May | 108.7 | -6.1% |
| W21 | 18-24 May | 104.7 | -9.5% |
| W22 | 25-31 May | 99.3 | -14.2% |
| **W23** | **1-7 Jun** | **107.0** | **-7.5%** ✓ |

**W23 is the strongest week since W20.** Recovery from the W22 trough is real, not early-week noise. Sequence: W20 peak → W21-W22 normalisation → W23 re-acceleration.

Per [[forecast-dsr-planning-rate]] — hold 1.3x for ordering, treat ~107/d as operational planning rate. If W24 stays at/above 107/d we have two consecutive at-target weeks (counting W20).

---

## Selling Performance Flags

### Sales Spikes (7d > 30d by 50%+, sustained)

| SKU | 7d | 14d | 30d | Spike | Note |
|---|---:|---:|---:|---:|---|
| **ACC-REM-500** | 75.0 | 66.5 | 40.6 | +85% | Sustained 3-week climb. Liquipak replacement urgency. |
| POW-CHA-011 (Charming) | 36.3 | 31.1 | 25.4 | +43% | -30d gap on UK 03062026 (see POS Check) |
| POW-FLO-024 (Flower Child) | 21.6 | 20.0 | 16.9 | +28% | -34d gap |
| POW-TRO-330 (Trophy Wife) | 18.4 | 16.7 | 14.8 | +24% | -39d gap, CRITICAL |
| POW-PRI-215 (Primadona) | 12.9 | 10.4 | 8.6 | +50% | 30 stock, 3d cover. CRITICAL |
| POW-YOU-256 | 31.1 | 24.9 | 18.7 | +66% | Confirm cover; no inbound visible |
| POW-SWE-001 (Sweet Tooth) | 20.7 | 16.3 | 13.2 | +57% | -10d gap UK 03062026 |
| POW-BLO-D07 | 1.9 | 1.2 | 1.0 | +90% | Low-volume tail |
| POW-FRO-001 | 1.3 | 0.7 | 0.8 | +62% | Tail |
| ACC-REM-BOW | 1.1 | 0.9 | 0.7 | +57% | Standalone tiny; bundle still drives |

**POW-SUG-545 (Sugar Rush)** — last cycle flagged 5.6x model day 8. Not in spike list this run (7d 5.0, 14d 6.1, 30d 4.8, +5% — normalised). Reset complete. Model still 1.3 — needs Greg refresh to ~5/d to match the new baseline.

### Sales Drops (7d < 30d by 40%+)

15 colours showing 7d zero sales with 30d > 0. **Likely B360-packup stranded** (no stock = no sales). Cross-reference needed against B360 packup SKU list:

| SKU | 7d | 14d | 30d |
|---|---:|---:|---:|
| POW-SLO-192 | 0.0 | 0.0 | 9.2 |
| POW-BAR-198 | 0.0 | 0.0 | 8.0 |
| POW-GOO-208 | 0.0 | 1.4 | 7.6 |
| POW-AWA-050 | 0.0 | 1.8 | 4.5 |
| POW-PER-229 | 0.0 | 0.0 | 4.0 |
| POW-KIN-642 | 0.0 | 0.1 | 3.6 |
| POW-HEL-387 | 0.0 | 0.0 | 3.4 |
| POW-SHH-013 | 0.0 | 0.0 | 3.5 |
| POW-SWE-258 | 0.0 | 0.9 | 3.5 |
| UK/EU-POW-LIP-570 | 0.0 | 0.6 | 6.5 |
| UK/EU-POW-BAL-521 | 0.0 | 0.5 | 6.7 |
| UK/EU-POW-POW-F17 | 0.0 | 0.1 | 7.5 |
| POW-DAY-025 | 0.0 | 0.0 | 1.4 |
| POW-NOT-065 | 0.0 | 0.0 | 1.3 |
| POW-SEA-450 | 0.0 | 0.1 | 1.2 |

**UK/EU- prefixed** are 3 high-volume colours (~7/d) confirmed unsellable due to packup lock. Joel B360 balance is the unlock.

The remaining 12 split into likely B360-stranded (POW-SLO, POW-BAR, POW-GOO, POW-AWA, POW-KIN, POW-SWE-258 — all 3-9/d historically) vs Gav listing audit candidates (POW-DAY-025, POW-NOT-065, POW-SEA-450 — 1-2/d, likely dead listings).

### Overperformers vs Model (>20% above)

- POW-CHA-011 (Charming): +50% — model 20.8, actual 31.1
- POW-PRI-215 (Primadona): +100%
- POW-FLO-024 (Flower Child): +54%
- POW-TRO-330 (Trophy Wife): +43%
- POW-YOU-256: +28%

### Underperformers (>40% below model)

| SKU | Model | 14d | Gap | Note |
|---|---:|---:|---:|---|
| POW-CLE-193 (Clear) | 162.5 | 26.1 | -84% | Heavy 3PL bundle pull continues |
| POW-CRE-217 (Creme Brulee) | 126.1 | 9.0 | -93% | 5,512 stock = 612d cover. **Massive overstock** |
| POW-ILL-001 (Illusion) | 15.6 | 1.2 | -92% | 653 stock = 544d |
| POW-DRE-771 (Dream Catcher) | 6.5 | 0.4 | -94% | 271 stock = 678d |
| POW-COS-012, POW-MAR-009, POW-MIL-193, POW-STA-033, POW-SUN-394, POW-TRU-70188 | various | all <0.5/d | -90%+ | Model 5-26d cover; actual 100-500+d. Refresh batch. |

These all need Greg DSR refresh. Per [[uk-discontinued-liquids]] and Current Issues 2 Jun list — refresh is in Greg's queue.

### Dead Stock (colours, 0 Shopify 14d)

6 SKUs, 1,275 units idle:
- POW-EVE-019 (370), POW-CAN-016 (198), POW-YUL-007 (198), POW-JAC-619 (184), POW-ICO-775 (175), POW-LOT-411 (150)

All small qty — Gav listing audit candidates with the wider 52-colour 14d-zero list.

---

## Realistic Days Cover (recap from POS Check)

Pulling forward the key risks from POS Check for completeness:

| SKU | Stock | Actual DSR (or kit-adj) | Cover | Trajectory |
|---|---:|---:|---:|---|
| LIQ-BAS-2 | 1,395 | 130/d kit-adj | **11d** | OOS 20 Jun. Chemence lands 10 Jul = **-20d gap** |
| LIQ-GLO-4 | 2,547 | 117/d kit-adj | 22d | OOS ~1 Jul. Chemence lands 10 Jul = **-9d gap** |
| LIQ-HEA-5 | 2,908 | 108/d kit-adj | 27d | OOS ~6 Jul. **Oils4Life PO needed by 14 Jun** |
| ACC-REM-500 | 2,718 | 66.5/d | 41d | **OOS ~20 Jul**. Liquipak replacement decision drives this. |
| ACC-LAB-UK | 1,423 | ~110/d (kit+std) | 13d | PO 17 at Fulfillable, awaiting Roisin book-in |
| ACC-TIP-COF | 68 | 117/d | <1d | Current offer; 1,389 in B360 packup |
| KIT-STA-2 | 11 | 0.6/d (Shopify) | 18d at actual | Substitution to COM holds. UK 03062026 +448 lands 22 Jul. |

---

## Container Arrivals Detected

No container arrivals in last 60d in the 3PL tab (Fulfillable deduction blind). Powder Room booked in 19-20 May (out of 60d window now).

---

## Inventory Discrepancies (3PL Integrity)

**Cannot run.** Fulfillable `inventory_changes` 500-row pagination cap continues (5th cycle). No 3PL deduction data available for kit alignment or red-flag detection.

Next cycle: implement cursor pagination per [[shiphero-inventory-changes-cap]] before this becomes a real integrity gap.

---

## 3PL Deduction Check

**Cannot run** — same blind spot. ShipHero `inventory_changes` cap.

---

## Bundle / LIQ-SET Activity

LIQ-SET (6-liquid bundle) negligible: 7d 0.3, 14d 0.2, 30d 0.1.

ACC-REM-BUN-1 (120ml + Bowl) and ACC-REM-BUN-2 (500ml + Bowl) drive most ACC-REM* and ACC-REM-BOW deductions. Without 3PL data we can't quantify the split precisely; standalone Shopify shows ACC-REM-500 standalone is genuinely 75/d (separate from bundle).

---

## Key Takeaways

### What needs action

1. **LIQ-BAS-2 -20 day OOS gap stands** (Jun 20 → Jul 10 Chemence landing). Mitigation plan still missing — Joel/Daniel must commit to express, kit-throttle, or attach reduction this week.
2. **ACC-REM-500 +83% sustained, 41d cover.** Liquipak replacement timing is now driven by this — onboarding decision must happen by ~mid-Jun for any chance of bridging.
3. **ACC-LAB-UK 13d cover** — PO 17 book-in at Fulfillable is the unblocker. Daily chase Roisin.
4. **Oils4Life Heal fill PO by 14 Jun.** Heal 27d cover, 51d lead. Recommended 8,000 units.
5. **B360 packup lock holds ~15 OOS colours hostage.** Joel £8,500 balance + Abdul disposal-quote dispute. 3 UK/EU- prefix colours (LIP-570, BAL-521, POW-F17) plus 12+ legacy SKUs effectively dead until released.

### What's FYI

- **W23 kit recovery confirmed: 107.0/d, -7.5% vs scaled.** Strongest week since W20. Two-week trough behind us.
- **Kit mix: COM 77%, ULT 22%, STA 1%.** Substitution to COM permanent. Greg per-kit DSR refresh needed.
- **Growth factor health: actual 1.08x vs target 1.3x.** Gap -17%. Hold for ordering per [[growth-factor-framing]]; flag overstock on future ULT containers.
- **POW-SUG-545 reset complete** — was 5.6x model for 8+ days, now at +5% vs 30d. Model still 1.3, needs Greg refresh to ~5/d.
- **POW-CRE-217 massive overstock** (5,512 / 9/d = 612d). Future containers should trim.
- **5+ POW colours overperforming model 28-100%** (CHA, FLO, TRO, YOU-256, PRI). UK 03062026 quantities (1-3 weeks cover at actual) will create gaps regardless of mitigation.
- **Fulfillable 3PL deduction blind 5th cycle.** Real integrity gap until cursor pagination implemented.
- **Heal kit-adj actual 108-117/d** — POS MODEL 118.3 already correct; no refresh needed.
