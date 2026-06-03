# 🇬🇧 UK Sales Analysis — 2 Jun 2026

## Data Freshness
- **Shopify:** latest 2026-05-31 (+1 day lag standard).
- **3PL tab:** last valid 2026-06-02, but **5th consecutive cycle with zero deduction movement** (Fulfillable inventory_changes still capped at 500 edges, cursor pagination not implemented). 3PL deduction analysis remains BLIND — all analysis below is Shopify-driven + bundle/kit math.
- **Growth factor:** 1.3x. Kit base 89/d → scaled 115.7/d.

## Headline Findings

1. **Kit selling rate has softened for 3 consecutive weeks**: W20 108.7 → W21 104.7 → W22 day-6 99.3/d. **-14% vs scaled (115.7/d).** Not a one-week noise.
2. **Kit mix continues to consolidate around COM**: 69% / ULT 30% / STA 1%. STA functionally dead. Per-kit model DSRs still untouched by Greg (recommendation carried from 26 May).
3. **ACC-REM-500 +136% vs 30d** — sustained from the 26 May +161% spike but decelerating slightly. Still the single largest selling signal.
4. **ACC-REM-BUN-1 collapsed in last 7d**: s7 6.9 vs s30 35.9 (-81%). Stock 0 — bundle can't sell. Will recover once Liquipak fill lands.
5. **One sustained overseller flag**: POW-SUG-545 (Sugar Rush) 5.6x model, day 6. Single SKU vs 26 May's 3-SKU list.
6. **52 colours 14d-zero** — same B360-packup-stranded pattern as 26 May (47). Awaiting Joel B360 balance.

---

## Kit Trend (last 8 weeks)

| Week | Period | Kit DSR | vs scaled 115.7 | Notable |
|---|---|---|---|---|
| W15 | 06-12 Apr | 95.9 | -17% | Fulfillable live |
| W16 | 13-19 Apr | 83.6 | -28% | Transition pain |
| W17 | 20-26 Apr | 63.0 | -46% | Worst point |
| W18 | 27 Apr-03 May | 76.0 | -34% | Slow recovery |
| W19 | 04-10 May | 79.7 | -31% | Floor |
| W20 | 11-17 May | **108.7** | **-6%** | First near-parity week (peak recovery) |
| W21 | 18-24 May | 104.7 | -10% | Held |
| **W22** | **25-31 May (day-6)** | **99.3** | **-14%** | **Softening** |

**Interpretation:** Kit recovery peaked at W20 (108.7/d, basically at scaled target). W21 and W22 each shed ~5/d. The "+25% surge" narrative from W21 day-1 (137/d) was always single-day noise — verified by full-week data at 104.7. **W22's softening is real, but it's a -14% miss, not a collapse.** Hold growth factor at 1.3x; this is one cycle of monitor, not action.

---

## Kit Mix (model vs actual)

| Kit | Model DSR | Actual s7 | % of kit volume | Δ vs 26 May |
|---|---|---|---|---|
| KIT-STA-2 | 6.5 | 1.0 | **1%** | was 6%, declining |
| KIT-COM-4 | 68.9 | 58.4 | **69%** | was 59%, rising |
| KIT-ULT-6 | 40.3 | 25.7 | **30%** | was 35%, falling |

- **STA has effectively disappeared from the basket** (1% of volume). Substitution to COM is structural and accelerating.
- **COM is the workhorse** at 69% of kit volume. Model DSR 68.9 ≈ s7 58.4 ≈ s14 58.9 ≈ s30 54.0. **Model is over-stated by ~5-15/d on COM** — close to right.
- **ULT model 40.3 vs s7 25.7** — over-stated by 14.6/d. Real ULT rate is settling at 25-30/d.
- **POS MODEL kit-component DSRs are stale** — Greg refresh outstanding from 26 May. STA should drop to ~1-2, ULT to ~28, COM stay ~58.

---

## Overseller Flags

**SKUs selling ≥ 3x POS MODEL DSR (and model ≥ 1/d):**

| SKU | Name | Stock | Model | s7 | s14 | s30 | Ratio | Days running |
|---|---|---|---|---|---|---|---|---|
| POW-SUG-545 | Sugar Rush | 24 | 1.3 | 7.3 | 5.9 | 4.1 | **5.6x** | Day 6 |

Sugar Rush is the only sustained overseller. Stock 24 → 3.3d cover at s7 rate. **Will OOS this week.** No CN container brings POW-SUG-545. Listing/marketing audit: is this in a promo, a TikTok moment, or a structural shift?

**Borderline (s7 elevated but stock too low to call durably):**
- POW-ENV-035 (Envy): s7 9.6 vs s30 4.8 = 2.0x, but only 1 unit stock — flag will collapse as stock empties.

vs 26 May Sales Analysis: 3-SKU overseller list (SUG, VIO-11932, AWA-050) narrowed to 1. Indicates the W21 broad overshoot was one-off; only Sugar Rush is sustaining.

---

## ACC-REM-500 Spike — Status Check

| Window | Sales/d | vs 30d |
|---|---|---|
| 7d (25-31 May) | **58.0** | **+136%** |
| 14d | 44.8 | +82% |
| 30d | 24.6 | baseline |

vs 26 May Sales Analysis: was 39.7/d (7d) → +161%. **Today**: 58/d → +136%. **Absolute rate is up (+18.3/d) but the +X% trend is decelerating because the 30d baseline is moving up too.**

Interpretation: this is genuine spike, not noise. Three plausible drivers:
1. **Free-gift transition partially leaking through** (Daniel 12 May: "switching from current free-gift to Remove 500ml when current free-gift stock runs"). The Mat / Tray / Travel Bag are 0 stock today; if some kit orders are auto-attaching ACC-REM-500 as substitute gift, that would inflate it.
2. **ACC-REM-BUN-2 (500ml + Bowl bundle)** sales — s30 10.4/d. Marginal but contributes.
3. **CRO / landing-page change pushing 500ml**. Worth checking with Gav.

**ACC-REM-500 stock 3,248 + 571 B360 packup = 3,819 units / 58/d = 66d cover.** Comfortable even at the elevated rate. No action.

---

## ACC-REM-BUN-1 Collapse — Stock-Driven

| Window | Sales/d | vs 30d |
|---|---|---|
| 7d | **6.9** | -81% |
| 14d | 24.1 | -33% |
| 30d | 35.9 | baseline |

**ACC-REM stock 519 → bundle cannot ship if 120ml isn't available.** The s7 collapse is forced by OOS, not demand.

When Liquipak fill lands (~16 Jun if Joel pays Mon 9 Jun): bundle should snap back to 25-35/d range. Re-evaluate after that.

**Combined Remove demand (s14):**
- ACC-REM-BUN-1: 24.1 (Remove 120ml + Bowl bundle)
- ACC-REM-BUN-2: 8.1 (Remove 500ml + Bowl bundle)
- ACC-REM standalone: 2.5
- ACC-REM-500 standalone: 44.8
- **Total Remove demand**: ~80/d, of which ~75% is 500ml-attached. **500ml is now the primary Remove SKU**, 120ml is secondary.

---

## OOS-Driven Dead List (52 colours, 14d=0 sales)

Same pattern as 26 May (47 colours). Most are B360-packup-stranded SKUs that will resume selling when Joel pays B360 balance and stock releases. Top 10 alphabetic: POW-AUR-023, POW-BEY-825, POW-BRE-109, POW-BUB-516, POW-COT-030, POW-CRU-090, POW-DAY-025, POW-ENI-024, POW-GLO-018, POW-GOD-017.

**Sub-categories (carried from 26 May, ~5 days net change):**
- **OOS-driven (B360-stranded)**: ~28 SKUs. Will resume on balance payment.
- **Unlaunched / never moved**: ~16-20 SKUs. POW-AUR-023, POW-BEY-825, POW-LUM-021 etc. Listing audit candidate.
- **Already-known discontinued**: LIQ-SEN-2 and LIQ-SEN-4 (per region notes).

**Newly cooled (s7=0 & s30≥3/d that were selling before):**

| SKU | s7 | s14 | s30 | Stock | Probable cause |
|---|---|---|---|---|---|
| POW-SLO-192 (Slow Burn) | 0 | 8.1 | 11.2 | 0 | OOS — needs restock or B360 release |
| POW-BAR-198 (Bare Necessity) | 0 | 4.7 | 10.0 | 0 | OOS |
| POW-MON-005 (Moon Magic) | 0 | 7.0 | 9.0 | 0 | OOS |
| POW-TRA-452 (Train-Wreck) | 0 | 0 | 6.5 | 0 | Dead since W21 |

These all map to flagged SKUs in today's daily digest (POW-SLO-192, POW-BAR-198, POW-MON-005 marked day 1-2 without sales). They're OOS-driven, not listing issues. UK 03062026 (PO 10) brings: 1,600 BAR + 200 MON + 800 TRA + ~1,200 SLO via Powder Room/Chemence pipeline. Inbound 15 Jul.

---

## POS MODEL DSR — Refresh Priorities

Items where model materially overstates real demand (Shopify 30d standalone). Greg refresh recommended (carried from prior reviews):

| SKU | Model | s30 | Diff | Notes |
|---|---|---|---|---|
| LIQ-BAS-2 | 144.3 | 20.8 (std) | -123 | Already kit-adjusted in model (1 per kit + std). Model probably correct combining ~99 kit + 19 std = 118 ≈ model 144 with growth factor. Holds. |
| LIQ-GLO-4 | 128.7 | 9.6 (std) | -119 | Same pattern. ~99 kit + 9 std = 108 ≈ closeish to model. |
| LIQ-HEA-5 | 118.3 | 1.6 (std) | -117 | Same. ~99 kit + 1.6 std = 101 ≈ 118 with margin. |
| POW-CLE-193 | 162.5 | 32.0 (std) | -130 | Offer-pool colour (Daniel mentioned attaches to free-gift). Standalone Shop dramatically understates true pull. **Model likely correct.** |
| ACC-TIP-ALM | 126.1 | 4.9 | -121 | **🔴 Model wrong.** Almond not in current offer. Should refresh to ~5/d. |
| POW-VIO-11932 | 115.7 | 2.5 | -113 | **🔴 Model wrong.** Was a Powder Room launch SKU. Refresh to ~3/d. |
| ACC-REM | 59.8 | 4.0 (std) | -56 | Bundle-inflated. True combined ~40/d. **Refresh.** |
| ACC-NAI-240 / ACC-NAI-100/180 | 15.6 | 1.8-1.9 | -14 | **🔴 Model wrong** for both. Refresh to ~2/d each. |
| POW-OUR-772 | 18.2 | 2.1 | -16 | **🔴 Model wrong.** Refresh. |
| POW-DUS-346 | 16.9 | 1.6 | -15 | **🔴 Model wrong.** Refresh. |
| POW-OAK-283 | 20.8 | 6.9 | -14 | Refresh. |
| POW-ROY-304 | 14.3 | 1.3 | -13 | Refresh. |
| POW-ILL-001 | 15.6 | 2.0 | -14 | Refresh. |
| POW-SWE-001 | 22.1 | 10.0 | -12 | Refresh. |
| KIT-STA-2 | 6.5 | 5.2 | -1.3 | Marginal — but s7=1, declining. **Refresh to ~1-2/d.** |
| KIT-COM-4 | 68.9 | 54.0 | -15 | Acceptable but could refresh to ~58/d. |
| KIT-ULT-6 | 40.3 | 33.4 | -7 | Refresh to ~28-33/d. |

**Greg refresh ask:**
- Tip SKUs (ALM most critical at 121/d overstated)
- Per-kit DSRs (STA 6.5→1, COM 68.9→58, ULT 40.3→28)
- Several POW-* colours with stale model values from pre-Powder Room
- LIQ-SEN-2/4 to 0 (discontinued)

---

## Recommendations

1. **Kit DSR softening is real but not actionable today.** -14% W22 vs scaled. Hold the 1.3x growth factor and the container sizing as recommended in POS Check. If W23 (1-7 Jun) comes in below 95/d → revisit.
2. **Kit mix DSR refresh is overdue.** STA model 6.5 vs actual 1.0 is the most obvious. Greg priority.
3. **ACC-REM-500 spike is structural** (no longer a "look into it" item — it's been 14 days at elevated rate). Treat 50-60/d as the new baseline for sizing. PO 11 brings only 400 units — fine because it's still mostly attached via BUN-2.
4. **POW-SUG-545 (Sugar Rush) is the only durable overseller.** OOS in 3-4 days. Audit listing/promo to identify driver — if structural, recommend adding to next CN PO.
5. **POW-CLE-193 model 162.5/d is correctly high** (offer-attach colour). Don't refresh — it's holding the line on a real consumption.
6. **47 → 52 colour dead-list creep is mostly B360-stranded.** Joel B360 balance payment unlocks 28+ of them. The remaining 16-20 are listing-audit candidates for Gav (same list as 26 May).
7. **Free-gift offer rotation is consuming the broader basket more aggressively than the kit data shows.** Overall -28% (per 26 May summary 18-25 May) vs kits -3% means standalone product attach to kits is rising. Re-test 1-7 Jun.
8. **No 3PL deduction analysis possible — 5th cycle BLIND.** ShipHero cursor pagination work is now blocking trend analysis and overdue from a dev-priority view.
