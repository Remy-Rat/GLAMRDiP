# 🇨🇦 CA Sales Data Analysis — 27 May 2026

## Data Freshness

- **Shopify last:** 2026-05-25 (+2d lag from today, normal +1-2)
- **3PL (B360) last valid:** 2026-05-27 (today)
- **POS MODEL:** `UPDATED` cell empty (Greg paste-discipline carried)
- **Growth factor (live):** 2.0x (user-confirmed). Future-container 1.7x per [[future-container-growth-factor]].
- **Kit base:** STA 21 + COM 41 + ULT 18 = 80/d → **2.0x = 160/d scaled.**

---

## Headline: The W20 surge has peaked. W21 + early W22 are slipping.

| Week | Dates | Daily kit rate | vs 160/d scaled (2.0x) | Note |
|---|---|---|---|---|
| W14 | 30 Mar-5 Apr | 47.6 | -70% | floor |
| W15 | 6-12 Apr | 55.4 | -65% | |
| W16 | 13-19 Apr | 52.1 | -67% | |
| W17 | 20-26 Apr | 46.1 | -71% | trough |
| W18 | 27 Apr-3 May | 49.0 | -69% | |
| W19 | 4-10 May | 77.3 | -52% | first lift |
| **W20** | **11-17 May** | **151.9** | **-5%** | **PEAK — first parity-level week in months** |
| **W21** | **18-24 May** | **118.6** | **-26%** | **DOWN 22% vs W20** |
| W22* | 25-26 May (2d) | 96.0 | -40% | partial — too early to confirm |

**Read:** the W20 surge looks like a peak, not the start of a sustained trend.

- W20 → W21: -22% week-over-week drop. That's not noise within a surge — that's the surge cooling.
- W22 partial -40% is 2 data points; **don't conclude until full week prints**, but the directional signal is the same.
- Per the 13 May Joel note ("CA ramped massively since theme change"), this looks more like a 1-2 week conversion bump than a structural lift.
- Per [[growth-factor-framing]] do NOT lower the 2.0x growth factor based on this — it's an aspirational target and still tied to spend ramp. But sizing decisions on **future** containers should bake in the 1.55x actual (which is what the future-container 1.7x is doing — Greg's instinct is correct).

---

## DSR: Model vs Reality

### Kits
| SKU | Model (live 2.0x) | Shop 7d | Shop 14d | Shop 30d | Gap vs Model (30d) |
|---|---|---|---|---|---|
| KIT-STA-2 | 42.0 (21×2) | 13.6 | 13.4 | 12.6 | **-70%** |
| KIT-COM-4 | 82.0 (41×2) | 76.0 | 86.0 | 66.6 | -19% |
| KIT-ULT-6 | 36.0 (18×2) | 23.1 | 24.5 | 19.8 | -45% |

**Kit mix today (14d Shopify):** STA 11% / COM 70% / ULT 20% (vs model 26/51/23).

**Read:** STA is structurally under-indexed at ~30% of model rate. COM is the closest to model (81% of scaled). Same STA→COM substitution pattern UK showed in May. **CA 25072026 sizing today must trim STA hard** (mirrors POS Check call).

### Heal (kit-adjusted in AUS/CA per [[Component Map]])
| SKU | Model | Shop 7d | Shop 14d | Shop 30d | 3PL 14d avg | Note |
|---|---|---|---|---|---|---|
| LIQ-HEA-5 | 144.5 | 1.3 | 1.0 | 1.1 | 128.6 | **Standalone 1.1/d; kit-adjusted via 3PL = 128.6/d** (consistent with COM 86 + STA 13 + ULT 24 = 123/d kit consumption + standalone). Model overstates by ~12%. |

### Liquids (standalone — pre-packed in kits from China)
| SKU | Model | Shop 30d | Gap | Note |
|---|---|---|---|---|
| LIQ-BAS-2 | 28.9 | 8.9 | -69% | model stale |
| LIQ-GLO-4 | 17.0 | 4.3 | -75% | model stale |
| LIQ-SEA-3 | 20.4 | 6.6 | -68% | model stale |
| LIQ-BON-1 | 13.6 | 2.6 | -81% | model stale |
| LIQ-SOA-6 | 13.6 | 2.3 | -83% | model stale |
| LIQ-SEN-2 | 6.8 | 3.9 | -43% | |
| LIQ-SEN-4 | 5.1 | 2.7 | -47% | |
| LIQ-MAT-4 | 11.9 | 3.1 | -74% | model stale |

**Read:** standalone liquid model DSRs are 3-5x overstated (same finding as 20 May). Greg refresh still outstanding. Doesn't impact CN container sizing (liquids ship pre-packed in kits) but inflates the projected-DSR cover noise.

### Remove + Bowl
| SKU | Model | Shop 7d | Shop 14d | Shop 30d | 3PL 14d | Note |
|---|---|---|---|---|---|---|
| ACC-REM (120ml) | 52.7 | 1.6 | 1.9 | 3.0 | 9.1 | **standalone collapsed; bundle channel dominant** (ACC-REM-BUN-1 5.4/d, ACC-REM-BUN-2 6.1/d) |
| ACC-REM-500 | 119.0 | 91.7 | 96.4 | 69.3 | 104.7 | hot — actual > model. 30d understates because of the recent surge window. |
| ACC-REM-BOW | 68.0 | 2.4 | 2.1 | 2.2 | 15.1 | standalone tiny; bundle channel + offer pull explains 3PL |

---

## Top 15 colours by 14d Shopify

| SKU | 7d | 14d | 30d | Name |
|---|---|---|---|---|
| POW-HEA-515 | 39.6 | 43.5 | 33.1 | Heaven |
| POW-PIL-194 | 31.9 | 31.9 | 27.2 | Pillow Talk |
| POW-POS-184 | 25.9 | 28.6 | 23.2 | Positivi-Tea |
| POW-CLE-193 | 29.7 | 27.4 | 27.9 | Clear |
| POW-CHA-011 | 17.1 | 20.1 | 16.4 | Charming |
| POW-MON-005 | 18.7 | 19.9 | 16.3 | Moon Magic |
| POW-TRA-452 | 19.3 | 19.9 | 17.4 | Train-Wreck |
| POW-BAR-198 | 14.6 | 16.1 | 14.3 | Bare Necessity |
| POW-BLA-384 | 13.9 | 15.8 | 13.3 | Blackout |
| POW-HAR-139 | 13.7 | 15.1 | 13.2 | Hard to Get |
| POW-GOD-017 | 12.1 | 14.9 | 12.3 | Goddess |
| POW-PEA-068 | 13.9 | 14.1 | 14.0 | Peachy |
| POW-BOU-222 | 11.6 | 13.2 | 10.8 | Boujee |
| POW-YOU-256 | 12.3 | 13.2 | 11.5 | Yours Truly |
| POW-EMB-602 | 10.4 | 12.7 | 10.9 | Embers |

---

## Selling Performance Flags

### 🔼 Sales spikes (7d ≥ 1.5x 30d, 30d ≥ 1)

**6 D-suffix colours are breakout, +320-335% vs 30d** (per memory [[dippi-prefix-convention]], non-leading D in suffix is a legit CA-native code — not Nordic Dippi):

| SKU | 7d | 14d | 30d | Spike vs 30d |
|---|---|---|---|---|
| POW-DRE-D08 | 7.4 | 3.7 | 1.7 | +335% |
| POW-ANG-D09 | 10.4 | 5.2 | 2.4 | +333% |
| POW-VEL-D13 | 6.0 | 3.0 | 1.4 | +329% |
| POW-SAT-D10 | 7.7 | 3.9 | 1.8 | +328% |
| POW-ROS-D14 | 6.4 | 3.2 | 1.5 | +327% |
| POW-BLO-D07 | 7.6 | 3.8 | 1.8 | +322% |

**Read:** these 6 colours move together — same shape, same magnitude. Likely a **new collection launch** or **theme push** dropped these into rotation around 20 May. Today's digest already flagged ANG/BLO/SAT at day 3/2/2 above projection.

- Stocks 738-922 units each. At 7d burn (6-10/d) = ~90-120d cover. Healthy.
- POS MODEL DSR on all of these is set to ~1.7/d (the future-container kit-base × 1.7 default). **Model is 4-6x understated.** Add to Greg refresh list.
- POW-ANG-D09 also leads on cumulative 3PL gap (720 deducted last 30d vs 72 Shopify). The 3PL deduction is ~10x Shopify — possible kit-attach mechanism (the gift-card offer doesn't attach physical colours, so this is a *separate* pull mechanism, or the gift-card swap is too recent to reflect). **Worth confirming with Daniel.**

Other notable spikes:
- POW-CAS-CS32 (Cashmere) +77%, POW-SEA-450 (Sealed) +54% — small but trending.

### 🔽 Sales drops (7d ≤ 0.6x 30d, 30d ≥ 2)
Minimal:
- CA-POW-BAL-521 (Ballet): 1.4 vs 3.0 (-53%)
- ACC-REM (120ml): 1.6 vs 3.0 (-47%) — consistent with bundle channel dominance
- CA-POW-LIP-570 (Lipstick): 1.1 vs 2.0 (-45%)

### Overperformers vs model
- KIT-COM-4 (76/d 7d vs model 82, but 14d hit 86 = +5% above model)
- POW-HEA-515 Heaven (43.5/d 14d, no model DSR set — flag for Greg)
- Most top-15 colours don't have model DSRs to compare against — they're not in the kit DSR base. Standard for colours; flag if Greg starts tracking.

### Underperformers vs model
- Kits all under model (STA -70%, ULT -45%, COM -19%). Same story as DSR table above.
- Most liquids -65 to -85% (model stale, not selling slow).
- LIQ-HEA-5 standalone -99% (consistent with kit-adjusted picture; standalone selling has always been ~0/d).

### Dead stock
7 POW SKUs in stock with 0 14d Shopify, **1,167 total idle units** — down from 21 SKUs / 14,021 units on 20 May (-94% units).

| SKU | Stock | Name |
|---|---|---|
| POW-JUB-L11 | 1,025 | Jubilee |
| POW-SAF-149 | 50 | Saffron Blaze |
| POW-INF-506 | 42 | Inferno Hour |
| POW-ALL-146 | 39 | All Eyes On Me |
| POW-GAR-656 | 9 | Garnet Games |
| POW-RED-165 | 1 | Red Mischief |
| POW-BOR-355 | 1 | Bordeaux Nights |

**Read:** the surge has effectively cleared the dead-stock pile. POW-JUB-L11 (Jubilee, 1,025) is the lone large idle — likely an unlaunched or recently-retired colour. Check with Gav. Everything else is sub-50 units = noise.

---

## 3PL vs Shopify Integrity

### Kit deduction alignment (last 14d, container arrivals excluded)
| SKU | 3PL avg/d | Shopify 14d/d | Gap |
|---|---|---|---|
| KIT-STA-2 | 13.2 | 13.4 | -0.2 |
| KIT-COM-4 | 87.6 | 86.0 | +1.6 |
| KIT-ULT-6 | 25.1 | 24.5 | +0.6 |

**Read:** Kit integrity is clean. All within ±2/d on 14d. 3PL deduction logic is working as expected.

### Cumulative 30d gap (3PL > Shopify by ≥ 300 units, colours)

| SKU | 3PL 30d | Shopify 30d | Gap | Reading |
|---|---|---|---|---|
| POW-JUS-449 | 3,897 | 159 | **3,738** | offer-attached, sustained (Just Friends) |
| POW-CLE-193 | 4,566 | 837 | **3,729** | offer-attached, sustained (Clear — used in every dip) |
| POW-ANG-D09 | 720 | 72 | 648 | **breakout colour with kit-attach mechanism** |
| POW-SAT-D10 | 531 | 54 | 477 | same |
| POW-BLO-D07 | 510 | 54 | 456 | same |
| POW-DRE-D08 | 489 | 51 | 438 | same |
| POW-ROS-D14 | 441 | 45 | 396 | same |
| POW-VEL-D13 | 411 | 42 | 369 | same |
| POW-HEA-515 | 1,314 | 993 | 321 | Heaven — small gap, likely legit kit-pick (Top-of-list selling colour) |

**Read:**
- POW-CLE-193 + POW-JUS-449: the two known offer-pool colours. 9 consecutive days at 4-6x benchmark per 20 May, sustained through W21. Stocks 11,870 / 8,886 = 78d / 68d cover at 3PL burn. **Continues per the offer mechanism**, but if the gift-card swap is genuinely physical-SKU-removing, these should normalise within the next 7 days. **Watch.**
- 6 D-suffix breakout colours: identical ~9-10x ratio of 3PL/Shopify. This is **the smoking gun** — they are being pulled into kits via some attach mechanism (possibly the older offer or a coupled SKU rule). With the gift-card change today, these gaps should also start to close.
- POW-HEA-515: small gap (321), legit kit-pick variance. No action.

### Red flags last 14 days (top hits)
| Date | SKU | Deduction | Bench | Ratio |
|---|---|---|---|---|
| 16 May | ACC-NAI-MAT | 199 | 15 | **13.3x** |
| 19 May | ACC-NAI-MAT | 151 | 15 | 10.1x |
| 18 May | ACC-NAI-MAT | 147 | 15 | 9.8x |
| 25 May | POW-CLE-193 | 212 | 35 | 6.1x |
| 25 May | POW-JUS-449 | 172 | 35 | 4.9x |
| 25 May | ACC-REM-500 | 151 | 100 | 1.5x |
| 13-24 May | POW-CLE-193 (10 days) | 141-208 | 35 | 4.0-5.9x |

**Read:** confirms the offer mechanism was driving ACC-NAI-MAT (Mani Mat), POW-CLE-193 (Clear), POW-JUS-449 (Just Friends) up to and including 25 May. Mani Mat is now OOS (depleted to 0). The other two will normalise once the offer-mechanism change (gift card replacement) propagates.

---

## Container Arrivals Detected (last 60d)
| Date | SKUs +ve | Note |
|---|---|---|
| 18 Apr 2026 | 8+ | CA 03022026 / 07042026 telex release window |
| 23 Apr 2026 | 8+ | continued check-in |
| 25 Apr 2026 | 8+ | CA Powder Room (24-03-2026) check-in (per 247 channel 4 May reconciliation) |
| 26 Apr 2026 | 8+ | continued check-in |

No fresh arrivals since 26 Apr. **CA 21062026 next arrival: 1 Jul (per Lily confirmation).**

---

## Sensitive Base signal
LIQ-SEN-2 30d 3.9/d / LIQ-BAS-2 30d 8.9/d = 30% Sensitive split. Model assumes 70/30 split. **Inverted** — Sensitive over-indexed at 30% standalone. Note: Base also goes into kits so the 70/30 standalone-only split isn't directly comparable. Sensitive demand is healthy.

---

## Key Takeaways (3-5 bullets)

1. **The W20 kit surge is cooling.** W20 151.9/d (peak, -5% vs scaled) → W21 118.6/d (-26%) → W22 partial 96/d (-40%). Watch W22 full print; if it confirms <120/d, recalibrate marketing/spend expectations. **Don't lower the live 2.0x yet** per [[growth-factor-framing]], but bake the slip into CA 25072026 sizing — Greg's future-container 1.7x is the right instinct.
2. **CA 25072026 sizing (Daniel today) must trim KIT-STA-2 hard.** Actual STA 14d is 13.4/d (32% of model 42), but draft has 1,400 in OL. Recommended: trim to 300-500. Mirror UK STA→COM substitution pattern.
3. **6 D-suffix colours are breakout** (POW-ANG/BLO/SAT/DRE/ROS/VEL-D07/08/09/10/13/14). +320-335% vs 30d. 3PL deduction is 9-10x Shopify on each → they are being pulled into kits via some attach mechanism. **Stock is healthy (90-120d at 7d burn).** Add to Greg POS MODEL refresh batch and check with Daniel if there's a specific attach rule.
4. **Dead-stock pile collapsed from 14,021 → 1,167 units** (21 → 7 SKUs). Surge cleared the long-tail. Only POW-JUB-L11 (1,025) is a meaningful idle — Gav listing audit candidate.
5. **POW-CLE-193 + POW-JUS-449 sustained ~5x benchmark deductions** through 25 May. Stocks 11.9k / 8.9k = 78d / 68d cover at burn — safe. With the gift-card offer change (27 May), expect these to normalise within 7d. Watch the digest tomorrow.
6. **Kit deduction integrity clean** (±2/d on 14d kits). 3PL logic working correctly; no data integrity issue to raise with 247.

---

## Watch list for next cycle (W22 full + W23)

- [ ] **W22 full print** (1 Jun) — confirms whether surge cooling is a 1-week dip or a structural slip.
- [ ] **POW-CLE-193 + POW-JUS-449 deduction rate** — should normalise within 7d of gift-card offer change. If still elevated, the offer change hasn't propagated as expected.
- [ ] **D-suffix breakout** — does it persist? If it's a launch/collection effect, durable. If it was offer-attached, drops with the gift-card swap.
- [ ] **KIT-COM-4 burn** — currently 86/d (+5% above model). If sustained, CA 25072026 can support holding 2,800 COM. If softening, trim.
- [ ] **ACC-REM-500 selling rate** during the OOS window. 91.7/d 7d through 25 May — if the OOS forces customers off the offer, the rate will collapse and reset the demand picture.
