# 🇬🇧 UK Sales Data Analysis — 26 May 2026

## Data Freshness
- **Shopify**: latest 2026-05-25 (+1 day lag standard)
- **3PL (B360 tab)**: technically updated to 2026-05-26 but ZERO deduction movement detected (first_stock == latest_stock for 300 SKUs). **3PL deduction integrity BLIND — 4th cycle.** Fulfillable ShipHero feed needs cursor pagination fix. All analysis below is Shopify-driven + bundle/kit math.
- **Growth factor**: 1.3x. Kit base 84/d → scaled 109.2/d.

## Headline

- **Kits at parity, not over-target.** W20 108.7/d → W21 104.7/d → W22 day-1 89.0/d. Two consecutive at-target weeks (~109 scaled). The "+25% surge" reading in Current Issues was off a single noisy day; full W21 actually slightly under target.
- **Real kit business is COM + ULT, not STA.** Mix shift is permanent: model 12/38/50 % → actual 6/59/35 %. STA→COM substitution is the Shopify-flow doing its job.
- **ACC-REM-500 is exploding**: 7d 39.7/d vs 30d 15.2/d = **+161%** spike. Single biggest selling-rate flag in the data. Either a recent CRO/listing change, the free-gift transition leaking through, or a TikTok moment. Cross-reference `#sale-announcements` and `#cro-team-meetings`.
- **47 colours sold 0 in last 14d.** Mostly the 17-OOS-colour B360 packup list + post-Powder-Room residue. Listing-audit candidate list for Gav.

---

## 1. DSR — Model vs Actual

### Kits
| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap vs Model |
|---|---|---|---|---|---|
| KIT-STA-2 | 13.0 | 6.9 | 6.0 | 7.8 | **-54%** |
| KIT-COM-4 | 41.6 | 54.7 | 63.9 | 48.1 | **+54%** |
| KIT-ULT-6 | 54.6 | 36.3 | 37.9 | 36.2 | **-31%** |
| **TOTAL** | 109.2 (scaled) | 97.9 | 107.8 | 92.1 | -1% |

Total at parity; mix dramatically shifted. **Model is stale on per-SKU rates** — Greg should re-derive STA/COM/ULT splits from last 30d Shopify.

### Heal (kit-adjusted: standalone Shopify + kit consumption)
| Metric | Value |
|---|---|
| Model DSR | 110.5/d |
| Shop 14d standalone | 1.4/d |
| Kit consumption (1× per kit × 107.8 kit total) | +107.8/d |
| **Adjusted 14d** | **109.2/d** |
| Gap vs Model | **0%** (model matches reality once kit-adjusted) |

### Locally-filled UK liquids (Base, Glow — kit-adjusted)
| SKU | Model DSR | Shop 14d standalone | + Kit | Adjusted 14d | Gap |
|---|---|---|---|---|---|
| LIQ-BAS-2 | 135.2 | 18.9 | +107.8 | 126.7 | -6% |
| LIQ-GLO-4 | 122.2 | 9.1 | +107.8 | 116.9 | -4% |

Model is now correct on Base/Glow (Greg refresh applied 5 May). **No discrepancy.**

### Other liquids (standalone, CN pre-packed)
| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap vs Model |
|---|---|---|---|---|---|
| LIQ-BON-1 | 6.5 | 3.0 | 3.2 | 3.4 | **-51%** (stale model) |
| LIQ-MAT-4 | 7.8 | 2.6 | 2.1 | 2.3 | **-73%** (stale model) |
| LIQ-SEA-3 | 15.6 | 12.9 | 11.5 | 13.5 | -26% |
| LIQ-SOA-6 | 6.5 | 1.7 | 1.5 | 1.9 | **-77%** (stale model) |
| LIQ-SEN-2 | 8.0 | 0.0 | 0.0 | 0.0 | DISCONTINUED |
| LIQ-SEN-4 | 8.0 | 0.0 | 0.0 | 0.0 | DISCONTINUED |

Bond / Matte / Soak / Sensitive all need model refresh.

### Remove (bundle-adjusted)
| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Combined Op DSR | Note |
|---|---|---|---|---|---|---|
| ACC-REM (120ml) | 39.0 | 3.3 | 4.8 | 5.8 | **54.2** (4.8 + 49.4 BUN-1) | Combined matches model (+39%) — model was bundle-aware. |
| ACC-REM-500 | 36.4 | **39.7 🚨** | 22.5 | 15.2 | **22.5** (no bundle) | **7d +161% vs 30d.** Major signal. |
| ACC-REM-BOW | 31.2 | 0.6 | 0.5 | 0.7 | **61.1** (0.5 + 49.4 BUN-1 + 11.2 BUN-2) | Bundle pull dominant. |
| ACC-REM-BUN-1 (120ml + Bowl) | n/a | 30.4 | 49.4 | 35.8 | n/a | 14d +38% vs 30d. |
| ACC-REM-BUN-2 (500ml + Bowl) | n/a | 10.0 | 11.2 | 11.9 | n/a | Stable. |

**ACC-REM-500 7d 39.7/d is the standout.** Compared to model 36.4 → 9% over model on 7d. Compared to 30d → +161%. Cover @ 7d burn: 3,797 / 39.7 = 96d (still healthy), but signals demand shift worth confirming.

### Inserts (per-order)
| SKU | Shop 7d | Shop 14d | Shop 30d | Note |
|---|---|---|---|---|
| ACC-LAB | 190.0 | 181.7 | 165.6 | = ACC-LAB-UK (single SKU per user). Rising +15% 14d vs 30d — order count growing. |
| ACC-THA | 190.0 | 181.7 | 165.6 | Identical to ACC-LAB (1 per order each). |

---

## 2. Weekly Kit Trend (W14–W22)

| Week | Dates | Daily Rate | Vs Scaled (109.2) | Notes |
|---|---|---|---|---|
| 14 | 30 Mar–05 Apr | 83.3 | -24% | |
| 15 | 06 Apr–12 Apr | 95.9 | -12% | |
| 16 | 13 Apr–19 Apr | 83.6 | -23% | Fulfillable transition week |
| 17 | 20 Apr–26 Apr | **63.0** | **-42%** | Bottom (transition + B360 lockdown) |
| 18 | 27 Apr–03 May | 76.0 | -30% | Recovery start |
| 19 | 04 May–10 May | 79.7 | -27% | |
| 20 | 11 May–17 May | **108.7** | **-0.5%** | First parity week in 9+ weeks |
| 21 | 18 May–24 May | **104.7** | **-4%** | Held parity |
| 22 (day-1) | 25 May | 89.0 | -18% | Single day; noisy |

**Trajectory: 4-week recovery confirmed.** W17 floor → W21 parity is a 66% climb. **Hold 1.3x growth factor.** Two more at-target weeks before any sizing change per [[growth-factor-framing]].

### Kit mix (14d Shopify)
| Kit | Shop 14d | Share | Model share | Delta |
|---|---|---|---|---|
| STA | 6.0/d | 5.6% | 12% | -54% |
| COM | 63.9/d | 59.3% | 38% | +54% |
| ULT | 37.9/d | 35.2% | 50% | -31% |

**The model's kit mix is wrong for current behaviour.** Either (a) update the per-kit DSRs in POS MODEL to reflect substitution, or (b) keep the model as the "post-substitution-normalisation target" and accept current data is in transition.

---

## 3. Realistic Days Cover (key items, Shopify-driven)

| SKU | OH | Op DSR | Cover | Flag |
|---|---|---|---|---|
| KIT-STA-2 | 20 | 6.0 | 3.3d | 🔴 CRITICAL (substitution to COM absorbs) |
| KIT-COM-4 | 2,740 | 63.9 | 42.9d | 🟢 (tight against 15 Jul: -7d at current rate) |
| KIT-ULT-6 | 3,074 | 37.9 | 81.1d | 🟢 |
| LIQ-BAS-2 | 4,132 | 126.7 | **32.6d** | 🟡 **OOS ~28 Jun** before Chemence (sheet ETA 17 Jun) |
| LIQ-GLO-4 | 5,546 | 116.9 | **47.4d** | 🟡 **OOS ~13 Jul** before Chemence |
| LIQ-HEA-5 | 5,412 | 109.2 | 48.9d | 🟢 Oils4Life 12,370 buffer ready |
| ACC-REM (120ml) | 593 | 54.2 (incl. bundle) | **10.9d** | 🔴 Liquipak final fill the only restock |
| ACC-LAB / ACC-LAB-UK | 2,688 | 181.7 | **14.8d** | 🟡 Print Runner 14-21d lead |
| ACC-THA | 19,916 | 181.7 | 110d | 🟢 |

---

## 4. Container Arrival Auto-Detection (3PL data)

🚫 **Cannot run.** B360 tab is frozen post-13 Apr transition; Fulfillable ShipHero deductions blind. The known booking event (Powder Room/Chemence at Fulfillable 19 May) is confirmed via Slack/Gmail, not the 3PL feed. Until the cursor pagination fix lands, container arrivals can't be auto-detected for UK.

---

## 5. Inventory Discrepancy Detection (red flags)

🚫 **Cannot run.** Same 3PL blind. No daily deduction series to compute single-day or cumulative gaps. Carry as **4th-cycle stalled item — dev time needed.**

This blocks the meaningful integrity check (Shopify vs 3PL alignment) and creates a structural risk: if Fulfillable picking errors are happening, we won't see them in this data. The bundle math from POS Check (ACC-REM 4.8 standalone + 49.4 BUN-1 = 54.2/d combined) is the only sanity check available, and it relies on Shopify-side data only.

---

## 6. Selling Performance Flags

### 🚨 Standout: ACC-REM-500 7d 39.7/d (+161% vs 30d 15.2/d)
The biggest signal in the data. Possible drivers:
- Recent CRO/landing-page change pushing 500ml over 120ml
- Free-gift transition already partially live (Daniel 12 May: "switching from current free-gift to Remove 500ml when current free-gift stock runs")
- A TikTok/Reels moment
- Pricing error or unintended discount

**Action**: Check `#cro-team-meetings` and `#sale-announcements` for 18-25 May activity. If structural, ACC-REM-500 cover compresses from 168d to ~96d at the new rate — still healthy but worth confirming Liquipak final fill carries the right quantity.

### Sales Spikes (7d +50% above 30d)
| SKU | 7d | 30d | Spike | Note |
|---|---|---|---|---|
| ACC-REM-500 | 39.7 | 15.2 | **+161%** | See above |
| POW-WIS-133 | 6.4 | 2.8 | +129% | Wisteria — listing/CRO check |
| POW-CAS-CS32 | 4.3 | 2.2 | +95% | Cashmere (Powder Room CS code) — post-launch flow |
| POW-AWA-050 (Awakening) | 9.0 | 4.8 | +88% | Flagged in daily digest 25 May (day 2 above) |
| POW-WHI-099 | 5.0 | 2.7 | +85% | |
| POW-COR-481 | 3.7 | 2.0 | +85% | |
| POW-VIO-11932 | 4.7 | 2.6 | +81% | Powder Room post-launch |
| POW-BLU-ZGD22 | 6.9 | 4.2 | +64% | Powder Room post-launch |
| POW-GOO-208 | 15.7 | 9.8 | +60% | Note: only 3u on hand → critical |
| POW-SWE-258 | 7.7 | 4.8 | +60% | Only 6u → critical |
| POW-ENV-035 (Envy) | 5.1 | 3.3 | +55% | Flagged in daily digest (day 5 above) |
| POW-AFT-669 | 8.7 | 5.6 | +55% | |
| POW-BUT-098 | 5.7 | 3.7 | +54% | |
| POW-SUG-545 | 4.7 | 3.1 | +52% | Flagged in daily digest (day 2 above) |
| ACC-NAI-LIN | 5.0 | 2.9 | +72% | |

**Powder Room flow visible**: CS32 / VIO-11932 / BLU-ZGD22 etc are post-19-May book-in. Strong launch signal — Gav can confirm.

### Sales Drops (7d -50% below 30d) — all OOS, not listing issues
| SKU | 7d | 30d | Drop |
|---|---|---|---|
| POW-TRA-452 | 0.0 | 10.4 | -100% (OOS, B360 packup) |
| POW-SIN-254 | 1.9 | 7.4 | -74% (OOS) |
| POW-PEA-068 | 0.4 | 5.5 | -93% (OOS) |
| POW-DAY-025 | 0.0 | 3.5 | -100% (OOS) |
| POW-GOD-017 | 0.0 | 3.3 | -100% (OOS) |
| POW-FAI-308 | 0.0 | 3.2 | -100% (OOS) |
| POW-NOT-065 | 0.1 | 3.2 | -97% (OOS) |
| POW-BUB-516 | 0.0 | 3.0 | -100% (OOS) |
| POW-OVE-487 | 0.0 | 2.5 | -100% (OOS) |
| POW-CRU-090 | 0.0 | 2.1 | -100% (OOS) |

All correlate with the OOS list. **Not listing issues — these are stranded in B360 packup**. Resolves the moment Joel pays balance + 5-SKU release (and the broader packup transfer completes).

### Overperformers (>20% above model DSR)
- KIT-COM-4 (+54%) — already noted, substitution
- ACC-REM-500 (+9% on 7d, +161% on trend) — major
- POW-HEA-515 (model 30d 31.1, 14d 38.1 → +22%) — top-selling colour

### Underperformers (>40% below model DSR)
- KIT-STA-2 (-54%) — substitution
- KIT-ULT-6 (-31%) — substitution
- LIQ-BON-1 (-51%), LIQ-MAT-4 (-73%), LIQ-SOA-6 (-77%) — all standalone liquids with stale model DSR. **Greg refresh needed.**

### Dead Stock (47 colours with 14d = 0)
**First 20** (full list in extract): POW-AUR-023, POW-BEY-825, POW-BRE-109, POW-BUB-516 (OOS), POW-COT-030, POW-ENI-024, POW-FAI-308 (OOS), POW-GLO-018, POW-JUS-449 (OOS), POW-LUM-021, POW-MIR-015, POW-SHI-777, POW-SOL-019, POW-TRE010, POW-VIB-529, POW-EUP-014, POW-RUS-624, POW-STA-826, POW-FES-006, POW-DAW-W015.

Split into 3 buckets:
- **OOS-driven** (selling will resume when packup releases): ~25 SKUs (mostly POW-*-3xx range and the named OOS list)
- **Genuinely dead / unlaunched**: ~15-20 SKUs (POW-AUR-023, POW-BEY-825, POW-LUM-021, etc.)
- **Discontinued / phased out**: LIQ-SEN-2, LIQ-SEN-4 already known

**Gav listing-audit candidates**: cluster (b) above — pull whichever have stock on hand but no demand for 30+ days for delisting consideration.

---

## 7. Key Takeaways

1. **Kit recovery is at parity, not surging.** W20-21 both ~105-108/d vs 109.2 scaled. The "+25% W21 day-1" narrative in Current Issues was off a noisy single day. **Hold growth factor, hold container sizing, don't reactively over-order.**

2. **Real kit mix is COM-dominant**: 59% of UK kit volume is COM, not 38% as model assumes. STA→COM substitution is working automatically (Shopify-flow). **POS MODEL per-kit DSRs need refresh** to match (Greg).

3. **ACC-REM-500 +161% on 7d** is the single biggest selling signal in the data and warrants 30-min investigation. CRO change? Free-gift transition partially live? Confirm before final Liquipak fill payment so we know quantities are right.

4. **47 dead-stock colours** — break into OOS-driven (waits for B360 release) vs unlaunched/dead (listing audit). Pass to Gav.

5. **POS MODEL per-SKU DSR refresh needed**: Bond (6.5→3.2), Matte (7.8→2.1), Soak (6.5→1.5), STA (13→6), ULT (54.6→38), COM (41.6→64). Greg.

6. **3PL deduction integrity remains BLIND** — 4th cycle. Dev time to add cursor pagination to ShipHero `inventory_changes` query is now a critical blocker for sane Sales Analysis. Schedule before W22 review.

7. **OOS-driven sales drops** are NOT listing issues; they're B360-packup-stranded. Don't pull the colours from the site — they'll come back the moment Joel pays the balance.
