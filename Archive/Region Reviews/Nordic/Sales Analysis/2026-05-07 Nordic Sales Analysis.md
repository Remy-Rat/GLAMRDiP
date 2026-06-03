# 🇸🇪 Nordic Sales Data Analysis — 7 May 2026

> Focused per user direction on significant movement and selling well — not a full exhaustive table dump. **Note: Shelfless 3PL tab is empty in the POS MODEL** so all "deduction" analysis is reconstructed from Shopify (D + GD + bundle decomposition), not from 3PL data.

## DATA FRESHNESS

- Shopify: through 6 May 2026 (1d lag, normal).
- 3PL (Shelfless) tab: empty / not populated in POS MODEL. **No 3PL deduction signal available** — reconciliation against fulfilment-side movement not possible until Greg's rebuild lands.
- Growth factor: 1.5x (kit base 46/d → scaled 69/d).

## HEADLINE: Real consumption is HIGHER than the GLAMRDiP-only Shopify view shows

Shopify still shows two parallel streams in Nordic — GLAMRDiP-prefix and D- (Dippi) — both fulfilling real demand via the swap mechanism. **Looking at GLAMRDiP-prefix only undercounts true consumption by 12-17%.** This matters most for Remove products and a handful of colours where the Dippi stream is still meaningful.

| Window | GLAMRDiP-prefix | D-prefix | Total | D as % |
|---|---:|---:|---:|---:|
| 7d | 557.7/d | 78.8/d | 636.5/d | 12.4% |
| 30d | 525.6/d | 111.0/d | 636.6/d | 17.4% |

Dippi share is **declining steadily** — 17.4% 30d → 12.4% 7d. Clearance is winding down naturally, with most remaining D-stock now sitting idle (33 colours at 0 sales 14d, all D-prefix).

## KIT SELLING — RECOVERING TOWARD BASE

| Kit | Model DSR (1.5x) | 7d | 14d | 30d | vs Model | vs Base 46/d |
|---|---:|---:|---:|---:|---:|---:|
| KIT-STA-2 | 16.5 | 8.1 | 8.4 | 8.3 | -51% | — |
| KIT-COM-4 | 21.0 | 14.7 | 14.3 | 13.0 | -32% | — |
| KIT-ULT-6 | 31.5 | 20.1 | 20.6 | 18.9 | -36% | — |
| **TOTAL** | **69.0** | **42.9** | **43.3** | **40.2** | **-38%** | **-7%** |

Trajectory across windows: 30d 40.2 → 14d 43.3 → 7d 42.9. **Bottoming out and recovering** toward base after the post-transition floor in W14 (17 Mar–5 Apr period was the trough). At base 46/d the gap is now ~7%, well within model tolerance.

**Kit mix flip confirmed.** Ultimate now 47% of kit sales, Complete 34%, Starter 19%. Model assumed 24/30/46 split (Starter-led for old Dippi clearance era). NORDIC 01072026 and 02082026 OL splits already weighted Ultimate-heavy — no urgent rebalance needed.

(Note: the daily digest's `weekly_kit_trend` data structure under-counts by excluding KIT-ULT-6-UNIT, which is the actual SKU key in Shopify — the weekly figures of 17-26/d should be ~doubled. Use `sku_dsr` aggregation as authoritative.)

## SIGNIFICANT DEDUCTIONS — THE BIG ONE

**ACC-REM-500 total real consumption is 28-38/d, not 5/d.**

| Component | 7d | 30d |
|---|---:|---:|
| ACC-REM-500 (GLAMRDiP standalone) | 5.7 | 5.0 |
| D-ACC-REM-500 (Dippi standalone) | 9.4 | 14.7 |
| ACC-REM-BUN-2 (GD bundle = 1× Remove 500ml + 1× Bowl) | 5.3 | 6.1 |
| D-ACC-REM-BUN-2 (Dippi bundle) | 7.6 | 12.0 |
| **TOTAL Remove 500ml depletion** | **28.0** | **37.8** |

Combined Remove 500ml on-hand: 89 units (effectively 0 GLAMRDiP + 92 Dippi). **3.2 days cover at 28/d.** Paragon's 10,000-unit fill is 18 days late on Adib's promise. **This is the single most urgent operational risk in the region** and a stronger flag than what the POS Check showed at 18d.

Remove 120ml total real consumption: 7d ~0/d, 30d 0.3/d. Both genuinely supressed (no fulfillable stock + no Dippi standalone Remove 120ml SKU active either — the D-ACC-REM-BUN-1 is also at 0). Once Paragon fill lands, expect demand to lift; baseline forecast 30/d is reasonable on the same 1:1 ratio with Remove 500ml unless GLAMRDiP repositions the 120ml SKU's role.

Remove Bowl total real consumption: 7d 16.1/d (vs the standalone 1.0/d the POS Check showed at first read). Combined Bowl stock 3,149 → 195 days cover at total 16.1/d. Still generous but less ridiculous than the 3,149d figure suggested.

## TOP SELLERS — THINGS GOING WELL

### POW-CLE-193 — runaway top colour (Crystal Clear / Clear)

- 7d 37.6/d, 14d 37.6/d, 30d 34.2/d. **Sustained at 4x next-largest colour.**
- Same SKU shows up in the AUS daily digest's 3PL deduction breaches (257 + 236 + 203 across 4-7 May = 7.3x benchmark). In Nordic Shopify confirms this is real demand, not a deduction-anomaly.
- Combined Nordic stock: confirm against Shelfless once tab is rebuilt — POW-CLE-193 D-stock and GD-stock both worth checking.
- **Flag for the team:** if the AUS POW-CLE-193 deduction spikes are real consumption (the simplest read given Nordic shows the same demand pattern), it's likely a unique colour breakout, not a 3PL data error.

### Other strong performers (>5/d 14d, GLAMRDiP-prefix only)

| SKU | 7d | 14d | 30d | Note |
|---|---:|---:|---:|---|
| POW-HEA-515 | 10.1 | 10.6 | 9.5 | Stable top-2 |
| POW-BAR-198 | 9.9 | 10.1 | 9.7 | Stable |
| POW-BOU-222 | 8.6 | 9.4 | 9.3 | Stable |
| POW-POS-184 | 7.3 | 9.3 | 9.2 | Slight 7d softening (-21%) |
| POW-PEA-068 | 6.9 | 7.7 | 6.5 | Stable |
| POW-PIL-194 | 6.7 | 6.9 | 7.0 | Stable |
| POW-SLO-192 | 7.0 | 6.7 | 5.9 | +19% 7d trending up |
| POW-CRE-217 | 6.7 | 6.0 | 5.3 | +26% 7d spike |
| POW-CHA-011 | 6.9 | 5.9 | 5.0 | +38% 7d spike |
| POW-BLO-D07 | 6.0 | 5.9 | 5.7 | D-prefix still pulling |
| POW-TRA-452 | 5.3 | 5.0 | 4.3 | +23% 7d trending up |
| POW-OAK-283 | 3.9 | 4.9 | 5.3 | Softening |

Eight colours selling 5-10/d sustainable — the GLAMRDiP colour wall is healthy.

### Sales spikes (7d > 30d by 50%+)

| SKU | 7d | 30d | Spike |
|---|---:|---:|---:|
| POW-VIO-ZGD21 | 1.6 | 0.6 | +167% |
| POW-BLU-ZGD06 | 4.4 | 2.2 | +100% |
| POW-ROS-ZGD20 | 1.7 | 0.9 | +89% |
| POW-ICE-ZGD16 | 1.7 | 1.0 | +70% |
| POW-HEA-641 | 3.6 | 2.2 | +64% |
| POW-BLU-ZGD22 | 2.3 | 1.4 | +64% |
| POW-RID-661 | 3.4 | 2.1 | +62% |
| POW-PER-229 | 2.9 | 1.8 | +61% |
| POW-SIN-254 | 3.7 | 2.4 | +54% |

Multiple **ZGD-suffix** SKUs spiking — these are Christmas/winter limited series carry-overs gaining traction. Notable that POW-BLU-ZGD22 (Blue Moon) is also flagging as low cover in the CA region (last 14d cover analysis from 6 May CA recap). Cross-regional pattern; could reflect a TikTok/social signal.

### Kit-attached items confirming kit volume

ACC-LAB and ACC-THA both 46/d 7d (per-order) → confirms total order volume (kits + standalone) is ~46 orders/day. ACC-LAB / ACC-THA stocks aren't in the POS MODEL Nordic table but Adib confirmed in-stock locally.

## SIGNIFICANT DROPS

| SKU | 7d | 14d | 30d | Drop vs 30d | Likely cause |
|---|---:|---:|---:|---:|---|
| LIQ-BAS-2 (Base) | 5.9 | 7.7 | 10.3 | -43% | Listing OOS check needed; or true demand cooling |
| POW-BLA-384 | 2.3 | 3.4 | 4.0 | -43% | Investigate listing |
| D-ACC-NAI-SET | 2.1 | 2.6 | 4.1 | -49% | Dippi clearance natural drop |
| D-LIQ-GLO-4 | 2.0 | 2.8 | 4.0 | -50% | Dippi clearance natural drop |
| D-ACC-REM-500 | 9.4 | 13.2 | 14.7 | -36% | Dippi clearance natural drop |
| D-ACC-REM-BUN-2 | 7.6 | 11.6 | 12.0 | -37% | Dippi clearance natural drop |

The Dippi-prefix drops are the EXPECTED winding-down of clearance. The two GLAMRDiP-prefix drops worth checking:

- **LIQ-BAS-2** at -43% — Base sold 10/d 30d ago, now 5.9/d 7d. Investigate whether listing went OOS for any window. Stock is 778 + Express Base 432 + 14012026 216 = ~1,420 units inbound, so cover is fine; the demand drop is the question.
- **POW-BLA-384** at -43% (sold 4/d → 2.3/d). Check Shopify listing status; if active, just demand softening.

## DEAD STOCK — DIPPI CLEARANCE BACKLOG

**33 colour SKUs at 0 sales 14d, ALL Dippi-prefix.** Selection (first 15):

D-POW-CRE-217, D-POW-CHA-011, D-POW-ENV-035, D-POW-OUR-772, D-POW-BUB-516, D-POW-TRA-452, D-POW-OAK-283, D-POW-FLO-024, D-POW-VEL-D13, D-POW-CEL-D06, D-POW-ROS-D14, D-POW-DRE-D08, D-POW-ANG-D09, D-POW-BLO-D07, D-POW-LUC-D110.

Several of these are NOT on the dead list at GLAMRDiP-prefix level — POW-CRE-217 (6.7/d), POW-CHA-011 (6.9/d), POW-TRA-452 (5.3/d), POW-OAK-283 (3.9/d), POW-DRE-D08 / BLO-D07 (5.9/d each in GLAMRDiP-prefix). **What this means:** the swap mechanism is firing on the GLAMRDiP SKU even though Dippi stock is still in-warehouse, but the D-prefix Shopify SKU hasn't sold standalone in 14 days because the listing path now goes via GLAMRDiP. Adib's 16 Apr explanation matches: D-stock is being consumed via the swap, but the D-prefix Shopify SKU shows 0 because customers see the GLAMRDiP page.

**This is fine operationally** — the Dippi stock is still selling, just under the GLAMRDiP brand. The "dead colour" count is misleading.

**However:** for any D-suffix SKU (D-POW-ENV-035 type — i.e. Dippi-only SKUs with no GLAMRDiP equivalent), 0 sales = real dead stock. From the visible list, several look like they map to existing GLAMRDiP SKUs and several are pure-Dippi. **Listing audit candidate** — Gav/Remy bandwidth-light task: identify which Dippi colours have GLAMRDiP equivalents (sales firing via swap) vs pure-Dippi (true dead) vs limited-edition (always-going-to-be-dead).

## KEY TAKEAWAYS

1. **🔴 ACC-REM-500 is the headline risk.** True consumption 28-38/d (D + GD + bundles), only 92 combined units on hand = 3 days cover. Paragon 10,000 fill must land within ~3 days or go OOS. Joel/Daniel direct ask to Adib needed (per recap).

2. **🟢 Kit recovery is real.** -38% vs 1.5x scaled but only -7% vs base 46/d. Trajectory recovering across 30d→14d→7d. Reasonable to maintain ordering at 1.5x as aspirational; sizing decisions are bang on at base.

3. **🟢 POW-CLE-193 is a runaway top colour** at 37.6/d sustained, 4x next colour, and matching the AUS deduction pattern (which suggests AUS spikes are real demand, not a 3PL data error). Worth a Joel-level commercial conversation: is this a TikTok signal? Should we lean in?

4. **🟢 GLAMRDiP colour wall is healthy.** 8 colours selling 5-10/d sustainably plus 9 spike colours showing momentum. ZGD-suffix carry-over series gaining traction.

5. **🟡 Listing investigations.** LIQ-BAS-2 -43% drop and POW-BLA-384 -43% drop both warrant a 5-minute Shopify listing check.

6. **🟡 Dippi dead-stock list is misleading.** 33 D-prefix colours show 0 sales 14d, but most are still moving via the swap to GLAMRDiP listings. True dead-Dippi-stock is the subset with no GLAMRDiP equivalent — listing audit candidate, no urgency.

7. **🟢 Sensitive Base discontinuation confirmed by user.** Sheet OL on NORDIC 02082026 (216 units LIQ-SEN-2) needs zeroing. Sense Glow (LIQ-SEN-4) status awaiting clarification — sheet has 1,000 on NORDIC 01072026.

## ACTIONS FOR FOLLOW-UP

- [ ] Joel/Daniel: direct Adib ask on Paragon Remove 500ml landing — 3-day window
- [ ] Greg: zero LIQ-SEN-2 OL on NORDIC 02082026 (216 units) per discontinuation
- [ ] Daniel: confirm LIQ-SEN-4 (Sense Glow) — discontinue or keep
- [ ] Remy: 5-min Shopify listing check on LIQ-BAS-2 and POW-BLA-384
- [ ] Gav/Remy (low priority): Dippi-colour listing audit — separate "still-swapping" from "true dead" from "limited-edition end-of-life"
