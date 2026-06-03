# AUS Sales Data Analysis - 25 May 2026

---

## DATA FRESHNESS

- **Shopify last date:** 23 May 2026 (2-day lag — 24-25 May not yet pasted)
- **3PL (AUS 3GPL) last valid:** 25 May 2026 (today)
- **POS MODEL updated:** 25 May 2026 (today)
- **Growth factor:** 1.3x global, 1.4x for 07062026 Birthday Sale
- **Kit DSR model:** STA 34 + COM 78 + ULT 35 = 147/d base → 191.1/d at 1.3x

---

## KIT TREND — RECOVERY HOLDING

| Week | Daily kits | vs 191 target |
|---|---:|---:|
| W17 (20-26 Apr) | 86.4 | -55% |
| W18 (27 Apr - 3 May) | 71.7 | -62% (floor) |
| W19 (4-10 May) | 172.7 | -10% |
| **W20 (11-17 May)** | **198.3** | **+4%** |
| **W21 (18-23 May, 6-day partial)** | **188.7** | **-1%** |

**W21 holding at ~+/- target.** No further surge from W20 peak, but no fallback either. The 18 May digest read of 189.8/d aligns with the W21 6-day average of 188.7/d. **Recovery is structural, not noise.**

### Daily kit breakdown (last 14 days)

| Date | STA | COM | ULT | Total | vs 191 |
|---|---:|---:|---:|---:|---:|
| 10 May (Sat W19) | 30 | 130 | 34 | 194 | +2% |
| 11 May (Sun W20) | 22 | 40 | 56 | 118 | -38% |
| 12 May | 13 | 1 | 83 | 97 | -49% |
| 13 May | 18 | 0 | 110 | 128 | -33% |
| **14 May (Daniel COM→ULT swap)** | 23 | 0 | 237 | **260** | **+36%** |
| 15 May (Mani Mat offer ON) | 29 | 2 | 233 | 264 | +38% |
| 16 May | 34 | 2 | 232 | 268 | +40% |
| 17 May (peak) | 32 | 2 | 219 | 253 | +32% |
| **18 May (W20 end)** | 23 | 0 | 197 | 220 | +15% |
| 19 May | 25 | 2 | 159 | 186 | -3% |
| 20 May | 26 | 1 | 152 | 179 | -6% |
| 21 May | 28 | 0 | 148 | 176 | -8% |
| 22 May | 15 | 0 | 144 | 159 | -17% |
| 23 May | 31 | 0 | 181 | 212 | +11% |

**Read:** Peak of 268/d on 16 May coincides with day 1 post-Mani-Mat-offer-attach. W21 settles into 175-215/d range. Daniel's media-spend tightening (per 18 May Slack) is visible — peak dropped from 268 → 175-212/d. **Mix has fully inverted: Complete is dead (avg 1/d post-14-May), Ultimate runs 144-237/d, Starter steady 25-32/d.**

---

## KIT MIX — MODEL IS NOW WRONG

| SKU | Model DSR (1.3x) | Shopify 7d | Shopify 14d | Shopify 30d | vs Model |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 44.2 | 25.7 | 24.9 | 23.7 | -44% |
| KIT-COM-4 | 101.4 | 0.7 | 12.9 | 40.9 | -87% |
| KIT-ULT-6 | 45.5 | 171.4 | 156.1 | 85.5 | **+243%** |
| **TOTAL** | **191.1** | **197.9** | **193.9** | **150.1** | **+1%** |

**Total kit rate is at target. Mix is wrong:**
- ULT is 86% of kit volume (was supposed to be 24%).
- COM is 0% (was supposed to be 53%) — Complete is effectively retired in current offer.
- STA is 13% (was supposed to be 23%) — small underperform.

**User confirmation: "we have been sending ultimate kits"** — Daniel/Joel are substituting Ultimate for Complete in fulfilment (informal, no Shopify swap-flow). So Complete demand is masked by manual substitution.

**Implication for AUS 08072026 sizing (Daniel today):**
- Container should size to the *substituted* mix, not Shopify-reported mix
- If substitution is permanent: ULT ~85% / STA ~15% / COM ~0% of kit volume
- 08072026 sheet currently shows STA 1,372 + COM 3,192 + ULT 1,428 = 5,992 kits, with COM at 53% and ULT at 24% → **opposite of reality**
- **Recommend Daniel flip the mix at 08072026: bring COM down to ~500-1,000, ULT up to ~3,500-4,500**

---

## OFFER MECHANISM — DECODED

The kit recovery is driven by **AUS-$85-GIF offer SKU at 196.6/d (7d)** — virtually 1:1 with kit volume. Every kit order is qualifying for / taking the gift.

The $85 gift attaches the following free items per 14d 3PL deduction analysis:

| Attached SKU | 3PL ded 14d | Kits 14d | Attach rate | Comment |
|---|---:|---:|---:|---|
| **LIQ-HEA-5 (Heal)** | 2,647 | 2,714 | **0.96** | Heal in nearly every kit (local fill, pre-known) |
| **ACC-NAI-MAT (Mani Mat)** | 2,135 | 2,714 | **0.79** | Free gift via $85 offer (post 15 May switch) |
| **ACC-TIP-SQU (Square Tips)** | 1,423 | 2,714 | **0.52** | **NEW: Free gift via $85 offer (post 19 May)** |
| **ACC-REM-500** | 2,307 | (177/d) | — | Standalone Shopify 152/d + BUN-2 15/d = explains most |
| **POW-CLE-193** | 5,390 (30d) | (1,257 Shopify) | gap +4,133 | Offer-attached colour |
| **POW-TRE010** | 2,131 (30d) | (6 Shopify) | gap +2,125 | Offer-attached colour |
| **POW-SUN-SU015** | 1,398 (30d) | (12 Shopify) | gap +1,386 | Offer-attached colour |
| **POW-CAN-D103** | 496 (30d) | (4 Shopify) | gap +492 | Offer-attached colour |

**Read:** Almost every kit order attaches Mani Mat (~80%) + Square Tips (~52%). Together = 132% — meaning some orders get *both* (Mani Mat + Square Tips bundled). Plus 1+ free POW-* colour per kit (CLE-193, TRE010, SUN-SU015, CAN-D103 are the offer-attached colour pool).

**Mani Mat per user "switched 3 days ago"** but data 22-25 May shows 174-251/d still being deducted. **The Mani Mat offer is still attached, OR there's a residual cleanup picking up old orders.** At minimum, the attach rate hasn't dropped — recalibrate planning to 190/d, not zero.

---

## STANDALONE LIQUIDS (PRE-PACKED IN KITS FROM CN, STANDALONE SHOPIFY ONLY)

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | 3PL 7d | Match? |
|---|---:|---:|---:|---:|---:|---|
| LIQ-BAS-2 | 53.3 | 25.3 | 16.8 | 24.7 | 33.7 | Shop ≈ 3PL within tolerance; **Model 2x reality** |
| LIQ-GLO-4 | 26.0 | 12.9 | 10.1 | 11.6 | 16.7 | 3PL slightly above (bundle/picking) |
| LIQ-SEA-3 | 44.2 | 15.4 | 13.2 | 17.3 | 20.7 | **Model 3x reality** |
| LIQ-BON-1 | 16.9 | 5.1 | 5.4 | 6.2 | 7.1 | **Model 3x reality** |
| LIQ-MAT-4 | 10.4 | 3.9 | 4.1 | 4.2 | 4.9 | Aligned |
| LIQ-SOA-6 | 13.0 | 4.7 | 3.7 | 3.8 | 6.9 | **Model 2-3x reality** |
| LIQ-SEN-2 | 9.1 | 7.3 | 4.9 | 4.6 | 9.5 | Aligned |
| LIQ-SEN-4 | 7.8 | 4.3 | 3.4 | 4.5 | 5.8 | Aligned |
| LIQ-HEA-5 | 184.6 | 1.7 | 2.1 | 2.4 | **197.4** | **Heal kit-adjusted: standalone ~2/d, 3PL ~197/d (in kit) — model is right at the kit-adjusted level** |

**POS MODEL DSR is stale on:**
- LIQ-BAS-2 (model 53.3 vs actual 25-34/d)
- LIQ-SEA-3 (model 44.2 vs actual 15-21/d)
- LIQ-BON-1 (model 16.9 vs actual 5-7/d)
- LIQ-SOA-6 (model 13.0 vs actual 4-7/d)

All of these are pre-packed in kits from CN — the model DSR appears to count kit-attribution that doesn't apply at the AUS 3PL level (because kits arrive assembled). **Greg refresh batch needed.** Won't affect container sizing because liquids ship inside kits from Sally — but does affect cover math when calculating OOS windows.

---

## REMOVE / 500ml / BOWLS

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | 3PL 7d | Notes |
|---|---:|---:|---:|---:|---:|---|
| ACC-REM (120ml) | 19.5 | 3.3 | 2.9 | 4.9 | 18.9 | **Shopify standalone collapse**. REM-BUN-1 9.1/d at standalone, the rest is picking inflation |
| ACC-REM-500 | 152.5 | **159.9** | 152.9 | 92.4 | 178.0 | **W21 sustained**. Bundle BUN-2 15.3/d explains residual gap. Real standalone DSR is 160/d, model 152.5 is close |
| ACC-REM-BOW | 75.4 | 7.7 | 6.9 | 4.6 | 35.0 | Shopify standalone collapsed (was 4-7/d 30d). 3PL deduction comes from BUN-1 + BUN-2 component picking. **Model 75.4 is wrong** |
| ACC-REM-BUN-1 | — | 9.1 | 9.6 | 20.6 | — | Bundle pulling 120ml + bowl |
| ACC-REM-BUN-2 | — | 15.3 | 15.5 | 17.0 | — | Bundle pulling 500ml + bowl |

**Read:**
- ACC-REM-500 surge confirmed: 7d 160/d vs 30d 92/d = +73%. Driven by $85-gift offer attaching the 500ml.
- ACC-REM 120ml standalone is dead (3.3/d). Bundle-only channel now.
- ACC-REM-BOW standalone Shopify collapsed (7/d). All Bowl deductions are bundle-driven. Existing 18 stock OOS today; 09052026 brings 6,840 (207d at current rate — almost overstock).

---

## SELLING PERFORMANCE FLAGS

### 🔴 Spikes (7d significantly above 30d)

| SKU | 7d | 30d | Ratio | Likely driver |
|---|---:|---:|---:|---|
| KIT-ULT-6 | 171.4 | 85.5 | **2.01x** | Daniel 14 May offer-swap COM → ULT |
| ACC-REM-500 | 159.9 | 92.4 | 1.73x | $85-gift offer attaching 500ml |
| AUS-$85-GIF | 196.6 | 125.4 | 1.57x | Offer adoption climbing |
| POW-CHA-011 | 33.7 | 21.4 | 1.57x | Colour demand spike (check if listing-driven) |
| POW-NOT-065 | 12.9 | 7.5 | 1.71x | Colour |
| POW-LAC-196 | 12.4 | 7.8 | 1.59x | Colour |

### 🔴 Drops (7d significantly below 30d, baseline >5/d)

| SKU | 7d | 30d | Ratio | Likely driver |
|---|---:|---:|---:|---|
| KIT-COM-4 | 0.7 | 40.9 | 0.02x | Offer-swap killed Complete (user: substituting Ultimate) |
| ACC-REM-BUN-1 | 9.1 | 20.6 | 0.44x | $85-gift now pulls 500ml, 120ml bundle losing share |
| AU-POW-COB-G17 | 2.6 | 6.6 | 0.39x | AU-prefix colour fading - check listing |
| AU-POW-AMB-572 | 2.1 | 5.3 | 0.40x | Same |
| AU-POW-VAN-F01 | 3.0 | 6.3 | 0.48x | Same |
| AU-POW-ROS-522 | 3.3 | 6.5 | 0.50x | Same |
| AU-POW-LIM-G13 | 2.7 | 5.1 | 0.53x | Same |
| AU-POW-MAP-564 | 3.1 | 5.2 | 0.60x | Same |

**Pattern:** Several AU-prefix colour SKUs are fading. Likely the AUS-specific Powder Room collection or similar - check if these are being deprioritised on listings or just normalising post-Powder-Room-arrival. Worth a Gav listing audit.

### ⚫ Dead Stock

POS Check noted overstock flags. Sales side confirms:
- KIT-COM-4 at 0.7/d but 3,502 stock + 3,052 inbound on 09052026 + 3,164 on 07062026 = catastrophic overstock if substitution continues
- LIQ-MAT-4 at 4/d but 1,829 stock + 5,400 on 07062026 = 1,800d cover post-arrival
- LIQ-BON-1, LIQ-SOA-6 similar
- ACC-TIP-BAL/STI/ALM all stable-low (1-3/d) with 200-400d cover

**Recommend: Greg refresh model DSRs from current Shopify reality, especially for KIT-COM-4 (set to 0 or 5 until offer re-introduces it), liquids (BAS/SEA/BON/SOA), and tips (ALM/BAL/STI).**

---

## 3PL DEDUCTION INTEGRITY CHECK

**Kits (excluding container arrival days):**

| SKU | Shopify 14d/d | 3PL 14d/d | Gap | Read |
|---|---:|---:|---:|---|
| KIT-STA-2 | 24.9 | 24.7 | -0.2 | Aligned ✅ |
| KIT-COM-4 | 12.9 | 5.9 | -7.0 | 3PL deducting slower (returns? or paste lag?) |
| KIT-ULT-6 | 156.1 | 164.9 | +8.8 | Within tolerance ✅ |

**Daniel's 7 May concern of post-website-switch oversell artefact:** STA + ULT aligned to within 1-10/d. COM gap of 7/d is small (10% of model rate) and possibly explained by Shopify lagging refunds/cancellations. **No systemic oversell artefact detected on AUS.**

---

## CUMULATIVE COLOUR DISCREPANCIES (30d window)

3PL deducted significantly more than Shopify sold:

| SKU | 3PL 30d | Shopify 30d | Gap | Interpretation |
|---|---:|---:|---:|---|
| POW-CLE-193 | 5,390 | 1,257 | **+4,133** | Offer-attached colour pool (every kit gets it free) |
| POW-TRE010 | 2,131 | 6 | **+2,125** | Same - barely any standalone, all kit-attach |
| POW-SUN-SU015 | 1,398 | 12 | **+1,386** | Same |
| POW-CAN-D103 | 496 | 4 | **+492** | Same |

**Total ~8,000 units attributed to $85-gift offer colours over 30 days.** Stock these as offer-fuel SKUs. Verify these colours are correctly stocked and Sally is restocking them in containers (POS Check confirmed POW-CLE-193 high deduction is sustained).

---

## KEY TAKEAWAYS

1. **W21 kit rate 188.7/d (-1% vs target) — recovery confirmed structural.** Two consecutive weeks at/near target after 6+ weeks below. Hold 1.3x growth factor for 08072026 sizing. Don't lean-cut.
2. **Mix is fully inverted from model.** ULT 86% / STA 13% / COM 0% of kit volume. Daniel/Joel sending Ultimate in place of Complete is the actual fulfilment pattern. **08072026 today must flip the kit allocation** — COM down to ~500-1,000, ULT up to 3,500-4,500.
3. **$85-gift offer is the engine.** 196.6/d at 1:1 with kits. Attaches Mani Mat (~80%) + Square Tips (~52%) + offer-pool colours (CLE-193, TRE010, SUN-SU015, CAN-D103). **Free-gift SKU supply is now critical-path.**
4. **Mani Mat offer "switched" per user — data disagrees.** 174-251/d deductions on 22-25 May. Either offer still attached, residual order flow, or layered with Square Tips. Joel/Daniel confirm exact offer config today.
5. **Square Tips is the NEW offer tip** (post-19 May). 52% of kits attach a Square. Was 3-9/d (idle); now 200/d. **No Sally inbound on any container. Push Sally to add Square to 07062026 (still in production).**
6. **POS MODEL DSR is stale on multiple liquids and KIT-COM-4.** Greg refresh batch:
   - KIT-COM-4: 101 → 1
   - LIQ-BAS-2: 53.3 → 25
   - LIQ-SEA-3: 44.2 → 15
   - LIQ-BON-1: 16.9 → 6
   - LIQ-SOA-6: 13.0 → 5
   - ACC-REM-BOW: 75.4 → 7 (standalone) + bundle pull
7. **No oversell artefact on AUS kits.** Shopify ≈ 3PL within tolerance. Daniel's 7 May concern doesn't manifest in current 14d data.
8. **AU-prefix colour SKUs fading** (COB-G17, AMB-572, VAN-F01, ROS-522, LIM-G13, MAP-564). 6 SKUs down 40-60%. Listing audit candidate for Gav.
9. **POW-CLE-193 + POW-TRE010 + POW-SUN-SU015 + POW-CAN-D103** are the AUS offer-attached colour pool. ~8,000 units consumed over 30 days outside Shopify standalone. Make sure restock cadence sustains.
