# 🇦🇺 AUS Sales Data Analysis — 1 Jun 2026

## DATA FRESHNESS
- **Shopify last date:** 2026-05-31 (1d lag, standard)
- **3PL last date:** 2026-06-01 (fresh)
- **Growth factor (POS MODEL):** 1.3x → scaled target **191/d** (34 + 78 + 35 = 147 base)
- **Actual growth 14d:** 1.26x | **Actual growth 7d:** 1.22x
- **Recommended (actual14 × 1.1):** 1.39x — but per memory [[growth-factor-framing]], **don't lower 1.3x**; this is a health check.

## HEADLINE

W21 hit target (+0.4%). W22 softened -6.1%, but the surge is intact and structural — driven by the $85-gift offer (+329% spike vs 30d). Kit demand has stabilised at ~180/d. The kit MIX is now ULT-heavy (48% vs model 24%), driving the substitution we see at G3PL (ULT 0 stock, COM doing the work). Operationally: AUS 05082026 sizing of 1.6x looks **rich** vs current 1.22x-1.26x actuals; flag as overstock-risk to monitor over next 2-3 weeks before any size-down move.

## DSR: MODEL vs REALITY

### Kits

| SKU | Model base | Model ×1.3 | Shop 7d | Shop 14d | Shop 30d | 3PL 7d | Gap vs Model (30d) |
|---|---|---|---|---|---|---|---|
| KIT-STA-2 | 34.0 | 44.2 | 21.9 | 23.5 | 24.2 | 21.0 | **-45%** |
| KIT-COM-4 | 78.0 | 101.4 | 145.1 | 72.8 | 64.4 | 148.4 | -37% (depressed 30d) |
| KIT-ULT-6 | 35.0 | 45.5 | 12.4 | 89.4 | 90.0 | 12.6 | **+98%** |
| **Combined** | **147.0** | **191.1** | **179.4** | **185.6** | **178.6** | **182.0** | **-6.5%** |

Read:
- **Combined kit demand is stable around 180/d** — within 7% of scaled target.
- **STA is structurally under model** (-45%) — same Shopify-flow STA→COM substitution pattern UK has had. Reduce future STA quantities in containers.
- **ULT is structurally over model** (+98%) on 14-30d, but 7d shows 12/d because of physical OOS at G3PL (substitution masking real demand). True ULT demand is ~90/d.
- **COM 7d 145/d = ULT-substitution absorbing ULT orders into COM picks.** Not real COM demand. True COM demand = ~64/d (30d Shopify).

### Kit Mix Comparison

| SKU | Model share | Actual 14d share | Note |
|---|---|---|---|
| KIT-STA-2 | 23.1% | 12.7% | half of model |
| KIT-COM-4 | 53.1% | 39.2% | under model |
| KIT-ULT-6 | 23.8% | **48.1%** | **2× model** |

**This is the most important signal for ordering decisions.** AUS 05082026 currently brings 1,484 STA + 4,508 COM + 2,352 ULT (29% / 52% / 19% mix). Daniel's intended 1.6x rebuild needs to flip COM and ULT in the mix — recommend trimming COM to ~3,000 and lifting ULT to ~4,500-5,000 if 1.6x sizing holds.

### Heal (kit-adjusted via 3PL)

| Metric | Standalone Shopify | 3PL (kit-adj) | Combined |
|---|---|---|---|
| 7d | 2.0/d | 181.7/d | 183.7/d |
| 14d | 1.8/d | 189.6/d | 191.4/d |
| 30d | 2.4/d | 181.6/d | 184.0/d |

Kit-adj rate tracks combined kit DSR closely (181 vs 180). **Heal kit-pick logic at G3PL is working cleanly.** Model 240/d scaled is 30% overstated — Greg DSR refresh needed.

### Liquids (standalone — pre-packed in kits from China)

| SKU | Shop 7d | Shop 14d | Shop 30d | 3PL 7d | Notes |
|---|---|---|---|---|---|
| LIQ-BAS-2 | 19.3 | 25.2 | 26.8 | 21.9 | Shopify lower than recent — Base OOS earlier in month suppressed |
| LIQ-GLO-4 | 9.0 | 11.9 | 13.0 | 10.1 | Stable |
| LIQ-SEA-3 | 14.4 | 16.8 | 18.9 | 16.0 | Stable |
| LIQ-SEN-2 | 8.0 | 8.1 | 5.3 | 9.1 | **+51% 7d vs 30d** — Sensitive Base trending up |
| LIQ-SEN-4 | 4.4 | 4.8 | 5.0 | 5.3 | Stable |
| LIQ-BON-1 | 6.1 | 6.1 | 7.1 | 7.3 | Stable |
| LIQ-SOA-6 | 3.3 | 4.5 | 4.2 | 4.0 | Stable |

Read: All liquid standalone Shopify rates are 60-90% below model DSRs that are based on kit-adjustment math (model assumes Greg's combined rate). **Greg's POS MODEL liquid DSRs are mostly correct from a stock-cover standpoint** — they reflect kit consumption at G3PL pre-pack, which is accurate. But for standalone Shopify forecasting, use these much lower rates.

### Remove / Tips / Offer Attach

| SKU | Shop 7d | Shop 14d | Shop 30d | 3PL 7d | Read |
|---|---|---|---|---|---|
| ACC-REM | 4.3 | 4.1 | 4.2 | 8.1 | Bundle channel only — Shopify near-dead |
| ACC-REM-500 | **152.3** | 156.1 | 129.7 | 158.6 | **+17% above 30d** — current offer driver |
| ACC-REM-BOW | 0.3 | 4.4 | 4.9 | 2.6 | OOS-driven collapse (was 33/d, now 0.3) |
| ACC-TIP-COF | 0.0 | 0.1 | 0.9 | — | OOS since 18 May, dead |
| ACC-TIP-SQU | 3.1 | 3.6 | 4.4 | **68.0** | **3PL >> Shopify** — kit-attached via offer (52%) |
| ACC-TIP-BAL | 1.9 | 2.4 | 2.2 | **114.3** | **3PL >> Shopify** — investigate if attached |
| ACC-TIP-ALM | 6.1 | 6.6 | 7.5 | 6.7 | Aligned, standalone |
| ACC-NAI-MAT | 0.9 | 1.9 | 2.5 | **140.7** | **3PL >> Shopify** — offer-attached (79%) |
| ACC-TRA-BAG | 0.0 | 0.1 | 0.1 | — | **Becoming new offer SKU** — no flow yet |
| ACC-FRE-MANI | 0.0 | 0.0 | 0.5 | — | Dead — retire |
| ACC-REM-BUN-1 | 1.1 | 5.5 | 19.4 | — | -94% 7d — bundle volume collapsing |
| ACC-REM-BUN-2 | 1.4 | 8.9 | 12.9 | — | -89% 7d — bundle volume collapsing |

**ACC-TIP-BAL 114/d 3PL deduction is the surprise.** Shopify only 1.9/d, so this isn't customer-driven demand. Hypotheses:
- New offer attach we haven't catalogued yet
- 3PL using BAL as a "default tip" in mixed orders
- A reconciliation event

**Action: ask Daniel/Greg what's driving BAL deductions before assuming OOS forecast applies.**

## WEEKLY KIT TREND

| Week | Range | Daily | vs 1.3x (191/d) |
|---|---|---|---|
| W14 | 30 Mar - 5 Apr | 105.4 | -44.8% |
| W15 | 6-12 Apr | 135.3 | -29.2% |
| W16 | 13-19 Apr | 88.3 | -53.8% |
| W17 | 20-26 Apr | 86.4 | -54.8% |
| W18 | 27 Apr - 3 May | 71.7 | **-62.5% floor** |
| W19 | 4-10 May | 172.7 | -9.6% **← recovery begins** |
| W20 | 11-17 May | 198.3 | **+3.8%** |
| W21 | 18-24 May | 191.9 | +0.4% |
| W22 | 25-31 May | 179.4 | -6.1% |

**Recovery is structural and durable.** Three consecutive weeks at/near target after a -62% floor. W22 softening of -6% is well within normal week-to-week noise — not a trend reversal. The $85-gift offer is the driver: AUS-$85-GIF SKU itself shows 7d 55.7/d vs 30d 13.0/d (+329%).

## SELLING PERFORMANCE FLAGS

### Spikes (7d ≥50% above 30d)
| SKU | 7d | 14d | 30d | vs 30d |
|---|---|---|---|---|
| AUS-$85-GIF | 55.7 | 27.9 | 13.0 | **+329%** |
| KIT-COM-4 | 145.1 | 72.8 | 64.4 | +125% (substitution) |
| LIQ-SEN-2 | 8.0 | 8.1 | 5.3 | +51% |

### Drops (7d ≤60% of 30d)
| SKU | 7d | 14d | 30d | Cause |
|---|---|---|---|---|
| ACC-REM-BOW | 0.3 | 4.4 | 4.9 | OOS (offer dropping it) |
| ACC-REM-BUN-1 | 1.1 | 5.5 | 19.4 | offer rotation away from bundles |
| ACC-REM-BUN-2 | 1.4 | 8.9 | 12.9 | offer rotation |
| KIT-ULT-6 | 12.4 | 89.4 | 90.0 | physical OOS |
| **AU-POW-* (8 SKUs)** | 0.7-2.4 | — | 5-10 | **AU-prefix collection fading entirely** |

The 8 dropping AU-POW-* SKUs (VAN-F01, LIM-G13, ROS-522, BUT-528, LIP-570, BAL-521, POW-F17, MAP-564) are all 70-90% below their 30d rate. This isn't an OOS issue — the AU-prefix collection is being phased out commercially. Confirms 25 May listing-audit recommendation.

### Dead stock
**25 POW-* SKUs with 50+ stock and 0 Shopify in 14d, total 7,613 units.** Lower than 6 weeks ago but still a listing-audit pile.

### Overperformers vs Model
- KIT-ULT-6 (+98% on 14-30d when OOS not factored)
- ACC-REM-500 (+17% on 7d) — likely sustainable given offer-bundle attach
- LIQ-SEN-2 (+51% on 7d) — recent trend

### Underperformers vs Model
- KIT-STA-2 (-45%) — structural, account for in future sizing
- LIQ-BAS-2 standalone (-72% vs model 69/d) — model is overstated because it includes kit consumption that's pre-packed
- All POS MODEL liquid DSRs except Heal — flagged for Greg refresh

## INVENTORY DISCREPANCIES

### Cumulative gap test — 3PL drops 30d vs Shopify 30d

| SKU | 3PL drops | Shop 30d | Gap | Class |
|---|---|---|---|---|
| POW-TRE010 | 2,135 | 7 | 2,128 | **Offer-attached colour (Treasure)** — expected |
| POW-CAN-D103 | 1,738 | 8 | 1,730 | **Offer-attached colour (Candy Cloud)** — expected |
| POW-SUN-SU015 | 1,401 | 15 | 1,386 | **Offer-attached colour (Sun Pop)** — expected |
| POW-CLE-193 | 6,680 | 6,227 | 453 | Offer-attached (Clear) — within normal range |

**Total unexplained gap across top 20: 5,697 units — all classified as $85-gift offer attach.** This aligns with the memory entry [[aus-85gift-offer-attaches]]: ~8,000 colour units consumed outside Shopify standalone over 30d. **3PL deduction integrity is clean.** No unexplained stock losses to flag for Jake.

### Container arrival detection
- **10 Apr 2026**: 118 SKUs increased, +128k units. **B360 Packup arrival** (largest SKUs: THA, INS, MAI bags, RE5 bot).
- **14 Apr 2026**: 197 SKUs increased, +195k units. **Stock-correction or re-paste event** post-B360 Packup — POW-CLE-193 +39k as the largest entry. Likely Greg-driven reconciliation/transition cleanup.

No container arrivals detected in May. **Next arrival = AUS 09052026 ETA 22 Jun** (consistent with POS Check).

## SHOPIFY vs 3PL DEDUCTION CHECK (kits)

| SKU | Shop 7d | 3PL 7d | Gap | Read |
|---|---|---|---|---|
| KIT-STA-2 | 21.9 | 21.0 | -0.9 | aligned ✅ |
| KIT-COM-4 | 145.1 | 148.4 | +3.3 | aligned ✅ |
| KIT-ULT-6 | 12.4 | 12.6 | +0.2 | aligned ✅ (both depressed by OOS) |

**Kit deduction logic working cleanly.** This matches W21 finding from prior reviews — no post-website-switch oversell artefact on AUS.

## KEY TAKEAWAYS

1. **Kit demand has stabilised around 180/d** — three consecutive weeks at scaled target after recovery. W22 -6% softening is noise, not reversal. Hold 1.3x growth factor.
2. **Kit MIX has shifted dramatically toward ULT** (48% vs model 24%). The 05082026 fill PO should rebalance — ULT up, STA down, COM moderate.
3. **AUS 05082026 sized at 1.6x looks rich** — actuals 1.22x-1.26x. Daniel's call to provide buffer is defensible, but flag as overstock risk if sales don't accelerate by 3 weeks from now.
4. **Offer attach signal is loud and clean** — Mani Mat 140/d, Square Tips 68/d, Ballerina 114/d (unconfirmed driver), Treasure/Candy Cloud/Sun Pop colours 50-60/d each. Total offer pull ~400/d on accessory/colour SKUs, ~150/d on Remove 500ml.
5. **W22 softening + offer rotation overlap** — Mani Mat depleting (140/d 7d, 0 stock now), Square Tips at 7d cover. Offer pivot to Travel Bag + Empowered (recommended) needs to be live by mid-week or attach-driven kit volume drops.
6. **3PL deduction integrity is clean.** No unexplained colour or kit losses. The 5,700 unit "gap" is entirely $85-gift offer attach.
7. **ACC-TIP-BAL 114/d 3PL is unexplained** — Shopify only 1.9/d standalone. Either undocumented offer attach or 3PL anomaly. Action: ask Daniel/Greg.
8. **AU-prefix colours fading entirely** — 8 SKUs at 70-90% below 30d on 7d. Confirms commercial deprecation. Bundle into Gav listing audit.
9. **HEAL kit-adjusted deduction (182/d 3PL) matches kit total (180/d Shopify)** — kit pick logic clean. POS MODEL Heal DSR 240/d is 30% overstated; Greg refresh needed.
10. **AUS-$85-GIF +329% on 7d** is the engine of recovery. As long as this offer SKU stays north of 30/d, kit demand will hold above 150/d.
