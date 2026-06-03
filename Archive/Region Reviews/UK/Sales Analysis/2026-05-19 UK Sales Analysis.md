# 🇬🇧 UK Sales Data Analysis — 19 May 2026

## DATA FRESHNESS

- **Shopify:** latest 18 May (1-day lag per standard).
- **3PL (B360):** B360 tab is the **frozen Packup snapshot** — every SKU shows latest_stock == first_stock, deductions all 0. Cannot run Step 5 (deduction discrepancy investigation) or Step 6 (Shopify vs 3PL alignment) against this tab.
- **ShipHero (Fulfillable):** Available stock reconciles within 1-5 units across sampled SKUs. `inventory_changes` deduction extraction blocked by 500-edge cap (see POS Check). **Carry deduction integrity check to next cycle** once pagination is implemented.
- **Growth factor:** 1.3x. Base 84/d kits → scaled 109.2/d.

---

## DSR — MODEL vs REALITY

### Kits

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d | Gap vs Model (7d) |
|---|---|---|---|---|---|
| KIT-STA-2 | 10.0 | 5.1 | 5.4 | 8.9 | **-49%** |
| KIT-COM-4 | 32.0 | 73.1 | 58.6 | 40.1 | **+128%** |
| KIT-ULT-6 | 42.0 | 39.6 | 37.1 | 35.0 | -6% |
| **Total** | **84.0** | **117.8** | **101.1** | **84.0** | **+40%** (7d vs base) / **+8%** (7d vs 1.3x scaled) |

Reading: model base of 84/d is exactly the 30d Shopify total — so the model itself is calibrated correctly off historical baseline. The 7d/14d picture shows the **post-substitution mix shift** kicking in: STA collapsing as Shopify flow auto-routes to COM. COM has more than doubled relative to model.

### Kit-adjusted liquids (Heal, Base, Glow, ACC-INS — consumed per kit at Fulfillable)

| SKU | Model DSR | Shop 7d standalone | Kit consumption (7d) | Combined Adj | Gap vs Model |
|---|---|---|---|---|---|
| LIQ-HEA-5 | 110.5 | 1.4 | 117.8 | 119.2 | +8% |
| LIQ-BAS-2 | 135.2 | 16.9 | 117.8 | 134.7 | -0% |
| LIQ-GLO-4 | 122.2 | 9.3 | 117.8 | 127.1 | +4% |
| ACC-INS | 106.6 | — | 117.8 | 117.8 | +11% |

**Greg HAS refreshed Base/Glow DSRs since the last review.** This was the #1 stale-DSR flag at 5 May review ("POS MODEL DSR understated for Base & Glow — model standalone-only, ~90/d Base / 96/d Glow actual"). Today's POS MODEL Base 135.2 matches combined 134.7 within 1 unit; Glow 122.2 matches 127.1 within 4%. **Closed.**

### Liquids (standalone — pre-packed in kits from China; UK regional override)

| SKU | Model DSR | Shop 7d | Shop 14d | Shop 30d |
|---|---|---|---|---|
| LIQ-SEA-3 (Seal) | 15.6 | 10.1 | 14.4 | 12.7 |
| LIQ-BON-1 (Bond) | 6.5 | 3.4 | 3.7 | 3.1 |
| LIQ-SOA-6 (Soak) | 6.5 | 1.3 | 1.9 | 2.0 |
| LIQ-MAT-4 (Matte) | 7.8 | 1.6 | 2.1 | 2.2 |

LIQ-MAT-4 and LIQ-SOA-6 model DSRs are 3-4x actual. Last review flagged Bond 6.5 vs actual 2.4/d, Soak 6.5 vs 2.1/d, Matte 7.8 vs 2.1/d — **still stale**. Greg refresh needed for these three. Sensitive (LIQ-SEN-2/4) already confirmed discontinued and dropped.

### Remove products (model-on-combined per [[uk-remove-bundle-upsell]])

| SKU | Model DSR | Shop 7d standalone | 7d in bundle | 7d combined | Gap vs Model |
|---|---|---|---|---|---|
| ACC-REM (120ml) | 39.0 | 6.3 | 68.4 (BUN-1) | **74.7** | +91% |
| ACC-REM-500 | 36.4 | 5.3 | 12.4 (BUN-2) | 17.7 | -51% |
| ACC-REM-BOW | 31.2 | 0.4 | 80.8 (BUN-1+BUN-2) | 81.2 | +160% |

**ACC-REM-BOW model is 2.5x too low** — Bowl is consumed by both bundle types, so combined demand is 81.2/d vs model 31.2/d. **ACC-REM-500 model is 2x too high** — only 12.4 of 36.4 model rate is real; the rest is presumably Greg's historical baseline before the upsell pulled volume into 120ml. Greg refresh outstanding.

### Growth factor reality check

- Model base 84/d × 1.3x = 109.2/d scaled target.
- Actual 14d kit total: 101.1/d → **0.93 effective growth factor** (-7% vs target).
- Actual 7d kit total: 117.8/d → **1.40 effective growth factor** (+8% vs target).
- Trajectory: W17 (0.75x) → W18 (0.83x) → W19 (0.87x) → W20 (1.18x) → W21 day 1 (1.49x).

**Growth-factor recommendation (per [[growth-factor-framing]]):** do not lower. Recent momentum is taking actual UP through the scaled target. If W21+W22 settle in the 110-120/d range, the 1.3x model is broadly right; if they push to 130+/d, the next container size review should consider 1.4x. Hold for two more weeks before any sizing change.

---

## WEEKLY KIT TREND

| Week | Dates | Rate/d | vs scaled (109.2/d) |
|---|---|---|---|
| 13 | 23-29 Mar | 87.1 | -20% |
| 14 | 30 Mar-5 Apr | 83.3 | -24% |
| 15 | 6-12 Apr | 95.9 | -12% |
| 16 | 13-19 Apr | 83.6 | -23% |
| 17 | 20-26 Apr | **63.0** | **-42%** (floor) |
| 18 | 27 Apr-3 May | 76.0 | -30% |
| 19 | 4-10 May | 79.7 | -27% |
| 20 | 11-17 May | **108.7** | **-0%** (recovered) |
| 21 | 18-18 May (1 day only) | 137.0 | +25% |

**Recovery is structural, not noise.** 5 consecutive weeks below -20% (W13-W17) followed by 3 consecutive improving weeks (W18, W19, W20). W17 is now clearly the bottom. W21 is a single-day reading — wait for the full week before treating 137/d as the new floor.

### Kit mix (Shopify DSR)

| Window | STA | COM | ULT | Total | STA% | COM% | ULT% |
|---|---|---|---|---|---|---|---|
| 7d | 5.1 | 73.1 | 39.6 | 117.8 | 4% | 62% | 34% |
| 14d | 5.4 | 58.6 | 37.1 | 101.1 | 5% | 58% | 37% |
| 30d | 8.9 | 40.1 | 35.0 | 84.0 | 11% | 48% | 42% |
| **Model expects** | **10.0** | **32.0** | **42.0** | **84.0** | **12%** | **38%** | **50%** |

The mix has shifted dramatically in 30 days: STA dropping (12% → 4%) as the substitution flow takes over, COM absorbing the bulk (38% → 62%), ULT giving up share (50% → 34%) but holding absolute volume. **The story is COM, not ULT.**

---

## REALISTIC DAYS COVER

(See POS Check for full table. Repeating headline at actual rates here:)

| SKU | Stock | Actual rate (most relevant) | Cover at actual |
|---|---|---|---|
| KIT-STA-2 | 60 | 5.1/d (7d Shopify) | 12d → substitution covers |
| KIT-COM-4 | 3,119 | 73.1/d (7d Shopify) | **43d** |
| KIT-ULT-6 | 3,321 | 39.6/d (7d Shopify) | 84d |
| ACC-REM (120ml combined) | 843 | 74.7/d | **11d** 🔴 (Liquipak fill pending pay) |
| ACC-LAB-UK | 4,030 | 217.1/d | 18d 🔴 (Print Runner PO pending pay) |

---

## CONTAINER ARRIVALS DETECTED

B360 tab is frozen — Step 4 (auto-detect via 8+ SKU same-day increases) cannot run.

Known recent arrival (from POS MODEL + Slack):
- **UK Powder Room AND Chemence (PO 9 / 24-03-2026)** — landed at Fulfillable 13-14 May. Status `Completed` in POS MODEL with est_arrival 14 May. Physical receipt confirmed by Roisin (Greg picking-list email 29 Apr; Daniel Slack 03/05 "Chemence liquids delivered in the UK"). **Not yet booked into ShipHero** (5+ days stuck in the first-come/first-served queue). When booked, expect 7,568 LIQ-BAS-2 + 8,000 LIQ-GLO-4 + ~12-17 Powder Room colour SKUs to populate at once.

No other inbounds expected before mid-June. Chemence 22-04-2026 next (ETA ~22 Jun pending Vik confirm), then UK 03062026/02072026 sailing as 40HQ for 15 Jul.

---

## INVENTORY DISCREPANCIES

**Cannot run cumulative gap test (Step 5B)** while B360 tab is frozen. ShipHero `inventory_changes` would be the alternative but is blocked by the 500-edge cap.

**Action carried forward:** once ShipHero pagination is implemented (next cycle), re-run the cumulative 3PL-vs-Shopify gap test for UK across all colour and kit SKUs. This is the same data integrity check that was top priority at the 5 May review (3-cycle blind spot) and is still blocked.

For this cycle, no inventory-discrepancy signal extractable.

---

## 3PL DEDUCTION CHECK

Same constraint as Step 5. Deferred to next cycle.

---

## SELLING PERFORMANCE FLAGS

### Sales spikes (7d > 30d by 50%+, min 30d ≥ 2/d)

| SKU | 7d | 14d | 30d | Spike |
|---|---|---|---|---|
| POW-LAC-196 (Lace) | 9.6 | 6.1 | 3.8 | **+152%** |
| **UK-£45-GIF (gift trigger)** | **117.6** | **100.6** | **47.8** | **+146%** |
| **ACC-REM-BUN-1 (Remove 120ml bundle)** | **68.4** | **56.6** | **30.0** | **+128%** |
| POW-ENV-035 (Envy) | 5.1 | 3.2 | 2.3 | +121% |
| POW-MON-005 (Money) | 18.6 | 13.8 | 8.9 | +108% |
| POW-PER-229 | 9.0 | 6.9 | 4.6 | +95% |
| POW-AWA-050 | 6.0 | 4.7 | 3.2 | +87% |
| POW-PRI-215 | 8.0 | 6.4 | 4.3 | +86% |
| POW-CRE-217 | 10.6 | 7.7 | 5.8 | +82% |
| **KIT-COM-4** | **73.1** | **58.6** | **40.1** | **+82%** |
| POW-GAM-339 (Game Over) | 8.1 | 6.7 | 4.5 | +79% |
| POW-INF-195 (Infatuated) | 4.1 | 2.9 | 2.3 | +78% |

**The three spikes that matter:**
1. **UK-£45-GIF (+146%)** — the £45 gift-with-purchase trigger is now firing at 117.6/d, basically at kit-volume parity. This is the offer mechanic driving the kit recovery (and is well-aligned with the Daniel 14 May offer-attach swap from AUS — same pattern, different region).
2. **ACC-REM-BUN-1 (+128%)** — the before-cart Remove 120ml+Bowl upsell is the second large engine. Confirms the [[uk-remove-bundle-upsell]] memory: standalone ACC-REM has collapsed (-24% on 7d vs 30d) but combined demand is up sharply.
3. **KIT-COM-4 (+82%)** — direct effect of the kit-mix shift toward Complete kits via the Shopify flow.

Top-10 spike colours likely tied to the same offer mechanics — POW-LAC-196, POW-MON-005, POW-ENV-035, POW-GAM-339, POW-INF-195 are showing as a coherent set of "Apr-launched colours getting fresh wind in late May." Worth Gav scanning whether these were recently surfaced on the storefront / collection front pages.

### Sales drops (7d < 30d × 0.4, min 30d ≥ 2/d)

| SKU | 7d | 14d | 30d | Drop |
|---|---|---|---|---|
| POW-BUB-516 (Bubbly) | 0.0 | 3.4 | 4.2 | **-100%** |
| POW-FAI-308 (Fairytale) | 0.0 | 3.2 | 4.5 | **-100%** |
| POW-JUS-449 (Just Friends) | 0.0 | 0.0 | 3.1 | **-100%** |
| POW-PEA-068 (Peachy) | 0.0 | 2.9 | 8.4 | **-100%** |
| POW-OVE-487 (Over It) | 0.1 | 0.2 | 4.3 | -97% |
| POW-DUS-346 (Dusk) | 0.3 | 0.4 | 5.8 | -94% |
| POW-CRU-090 (Crush) | 0.3 | 0.1 | 4.1 | -92% |
| POW-GOD-017 (Goddess) | 0.4 | 3.6 | 4.3 | -90% |
| POW-ROY-304 (Royale) | 0.6 | 0.6 | 4.4 | -86% |
| POW-ILL-001 (Illusion) | 1.0 | 1.6 | 6.0 | -83% |
| POW-OUR-772 (Our Time) | 1.0 | 1.1 | 5.5 | -81% |
| POW-SEA-450 (Seaside) | 1.1 | 1.1 | 3.7 | -70% |
| POW-COS-012 (Cosmo) | 0.6 | 0.5 | 2.0 | -70% |
| UK/EU-POW-LIM-G13 (Powder Room) | 1.1 | 7.5 | 3.5 | -68% |
| POW-PAR-321 (Paradise) | 0.7 | 0.7 | 2.2 | -68% |
| UK/EU-POW-COB-G17 (Powder Room) | 1.4 | 9.4 | 4.4 | -68% |
| POW-DAY-025 (Daydream) | 1.6 | 4.2 | 4.5 | -64% |
| UK/EU-POW-BUT-528 (Powder Room) | 1.1 | 6.5 | 3.0 | -63% |

**Three explanations cover most of the drop list:**

1. **B360 Packup stockout** — the 5 OOS no-pipeline colours flagged 5 May (POW-JUS-449, POW-OVE-487, POW-SEA-450, POW-FAI-308, POW-NOT-065) are confirmed dead on 7d. POW-PEA-068, POW-BUB-516, POW-CRU-090, POW-GOD-017 join the list. **Resolution depends on Joel paying B360 stock-out balance.**

2. **Powder Room not booked into ShipHero** — UK/EU-POW-LIM-G13, UK/EU-POW-COB-G17, UK/EU-POW-BUT-528 all dropped because Fulfillable hasn't checked the inbound in yet. 14d > 30d shows they were selling well; 7d collapse is the book-in delay. Resolves when Roisin processes the receipt.

3. **Genuine demand softening** — POW-DUS-346, POW-ILL-001, POW-OUR-772, POW-ROY-304, POW-COS-012, POW-PAR-321, POW-DAY-025 are not in either of the above categories. These are real listing/demand questions, but most are at low absolute volume (1-6/d). Bandwidth-light listing review candidates.

### Last review's "8 colours dropped 40-55%" follow-up

| SKU | 7d | 14d | 30d | Status vs last review |
|---|---|---|---|---|
| POW-FLA-CS24 | 0.4 | 0.8 | 0.6 | Still depressed; absolute volume tiny |
| POW-BLU-ZGD06 | 0.6 | 1.1 | 1.1 | Stable low |
| POW-VIO-ZGD21 | 1.6 | 1.8 | 1.1 | Slightly improved |
| POW-PIN-SU016 | 1.1 | 1.4 | 1.2 | Stable |
| POW-GHO-771 | 0.9 | 1.1 | 1.0 | Stable |
| POW-CAS-CS32 | 1.6 | 2.0 | 1.7 | Stable |
| POW-AWA-050 | 6.0 | 4.7 | 3.2 | **+87% recovered** |
| POW-IMA-264 | 2.6 | 2.9 | 2.5 | Stable |

**Of the 8, only POW-AWA-050 has materially recovered.** The other 7 are all **in stock with healthy units** (87-363 each; 17-279 days cover):

| SKU | Stock | Model cover | Reading |
|---|---|---|---|
| POW-FLA-CS24 | 363 | 279d | Genuine overstock |
| POW-BLU-ZGD06 | 351 | 135d | Genuine overstock |
| POW-VIO-ZGD21 | 153 | 118d | Demand softening |
| POW-PIN-SU016 | 153 | 59d | Demand softening |
| POW-GHO-771 | 147 | 57d | Demand softening |
| POW-CAS-CS32 | 325 | 63d | Demand softening |
| POW-IMA-264 | 87 | 17d | Demand softening |

**Confirmed: these are demand-side issues, not stockout artefacts.** At <2/d absolute volume, the listing-review-vs-acceptable-tail decision belongs with Gav, not inventory. Worth bundling into a Gav listing audit rather than chasing individually.

### Dead stock (POW-* with 0 sales 14d)

47 colour SKUs registered 0 sales in last 14 days. Breakdown estimate:
- ~12-17 Powder Room SKUs (physically at warehouse, awaiting Fulfillable check-in — not really dead)
- ~17 B360 Packup colours (locked, awaiting stock-out balance payment)
- ~13-18 genuinely idle SKUs (no stock or zero demand)

True dead-stock count will be clearer once Powder Room books in and B360 releases — likely lands at 15-20 SKUs.

### Sensitive Base signal

Per [[uk-discontinued-liquids]] — LIQ-SEN-2 and LIQ-SEN-4 are discontinued in UK. Not analysed.

---

## KEY TAKEAWAYS

1. **The kit recovery is real.** 5 consecutive weeks improving, W20 at parity with scaled target, W21 day-1 reading at +25%. Don't lower the growth factor; let the surge settle and re-test in 2 weeks.
2. **The recovery is driven by the £45-GIF offer mechanic, the Remove bundle upsell, and the Shopify flow switching STA → COM.** All three are working as designed.
3. **17 OOS colours from the 12 May summary are still the headline drag** on the all-board number (-55% on 5 May, still around that on 12 May). Two unlocks: Joel pays B360 stock-out balance; Roisin books in Powder Room. Both should land in the next 1-2 weeks if pushed.
4. **Greg refresh status:** Base/Glow updated (closed); Bond/Soak/Matte still stale; ACC-REM-BOW model 2.5x too low; ACC-REM-500 model 2x too high; ACC-INS model slightly low. Next refresh batch should hit these 5.
5. **Data integrity blind spot persists.** B360 tab is frozen Packup; ShipHero `inventory_changes` capped at 500 edges. Cumulative deduction-gap test deferred to next cycle once pagination is implemented. This is now the 4th cycle without a UK 3PL deduction integrity view.
