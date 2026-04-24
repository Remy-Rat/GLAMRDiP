# Sales Data Analysis — UK — 21 Apr 2026

## DATA FRESHNESS

- Shopify: through **20 Apr 2026** (1-day lag, normal)
- 3PL (B360 tab): last valid **16 Apr**. **Caveat: tab is stale post-13 Apr transition** — Fulfillable data is on the PASTE tab and does not feed the deduction analysis. Treat 3PL deduction rates as B360 wind-down, not a live Fulfillable signal.
- Growth factor: **1.3x** (bumped from 1.1x — intentional per user, new planning bar)
- Base total: 84/d → scaled 109.2/d at 1.3x

---

## DSR: MODEL vs REALITY

### Kits — the headline

| SKU | Projected (1.3x) | 7d | 14d | 30d | Gap (14d) |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 13.0 | 10.4 | 14.0 | 14.2 | **+8%** |
| KIT-COM-4 | 41.6 | 24.0 | 26.7 | 26.6 | **-36%** |
| KIT-ULT-6 | 54.6 | 45.4 | 46.6 | 45.4 | -15% |
| **Total** | **109.2** | **79.8** | **87.3** | **86.2** | **-20%** |

**Actual growth factor: 1.04x (14d) / 1.03x (30d).** Recommended at 10% buffer = 1.14x.

**Read:** the kit rate hasn't changed materially from 14 Apr (90/d then, 87.3 now). What changed is Greg's ambition target — 1.1x → 1.3x means the same actual performance now reads as -20% below plan instead of -5% above plan. The underlying business didn't shift.

**Kit mix (14d):** Ultimate 53% / Complete 31% / Starter 16%. Ultimate-heavy. Model base mix is 50%/38%/12% (42/32/10) — so actual UK buyers skew even more toward Ultimate (+3pp) and less toward Complete (-7pp). STA +4pp above model share.

### Heal — kit-adjusted

| | 7d | 14d |
|---|---:|---:|
| Standalone Shopify | 0.7 | 1.0 |
| Kit-adjusted (stand + kit) | 80.5 | **88.3** |
| Model DSR | — | 110.5 (implied at 1.3x) |
| Gap (14d) | — | **-20%** |

Heal actual at 88.3/d kit-adjusted. 9,035 on hand = 102d cover. No urgency.

### Liquids — KIT-ADJUSTED (Base, Glow)

| SKU | Projected (1.3x, model) | Shopify standalone (14d) | Kit consumption (14d) | Total kit-adj | Gap |
|---|---:|---:|---:|---:|---:|
| LIQ-BAS-2 (Base) | 135.2 | 14.6 | 87.3 | **101.9** | -25% |
| LIQ-GLO-4 (Glow) | 122.2 | 7.0 | 87.3 | **94.3** | -23% |

Both kit-adjusted rates align with the ~20% kit gap. Model DSR for these is **correctly elevated** to account for Fulfillable's automated kit-picking (as of 21 Apr paste).

### Liquids — STANDALONE ONLY (pre-packed in kits from CN)

| SKU | Projected | 7d | 14d | 30d | Gap (14d) |
|---|---:|---:|---:|---:|---:|
| LIQ-SEA-3 (Seal) | 15.6 | 9.6 | 9.4 | 8.5 | -40% |
| LIQ-BON-1 (Bond) | 6.5 | 3.3 | 2.9 | 2.6 | -55% |
| LIQ-MAT-4 (Matte) | 7.8 | 2.7 | 3.1 | 3.0 | -60% |
| LIQ-SOA-6 (Soak) | 6.5 | 1.3 | 1.6 | 1.6 | -75% |
| LIQ-SEN-2 (LO Base) | 0.0 | 0.0 | 0.0 | 0.0 | OOS — legal/source constraint |
| LIQ-SEN-4 (LO Glow) | 0.0 | 0.0 | 0.0 | 0.0 | OOS — legal/source constraint |

**Sensitive lines: user confirmed 21 Apr no stock solution yet due to legal requirements.** These are structurally zero rather than demand zero — both need to either stay OOS with listings flagged or be formally delisted until resolved.

### Remove products (standalone)

| SKU | Projected | 7d | 14d | 30d | Gap (14d) |
|---|---:|---:|---:|---:|---:|
| ACC-REM | 39.0 | 25.4 | 19.0 | 22.5 | -51% |
| ACC-REM-500 | 36.4 | 9.7 | 13.2 | 11.8 | -64% |
| ACC-REM-BOW | 31.2 | 2.4 | 2.8 | 2.4 | **-91%** |

Same ACC-REM-BOW pattern as AUS — standalone demand negligible, model DSR badly overstated. UK sitting on 5,395 units / 2.8/d = **1,927d cover**. Absolutely no need for Remove Bowl on future containers.

### Top 10 colours

| SKU | Name | Projected | 14d | 30d | Gap (14d) |
|---|---|---:|---:|---:|---:|
| POW-CLE-193 | Clear | 41.6 | 31.7 | 31.1 | -24% |
| POW-HEA-515 | Heart | 35.1 | 29.6 | 28.6 | -16% |
| POW-POS-184 | Posh | 36.4 | 25.9 | 25.8 | -29% |
| POW-PIL-194 | Pillow | 24.7 | 22.2 | 20.8 | **-10%** |
| POW-SWE-001 | Sweet | 22.1 | 19.1 | 17.1 | -14% |
| POW-TRA-452 | Trance | 19.5 | 18.3 | 17.9 | **-6%** |
| POW-PEA-068 | Peachy | 15.6 | 16.9 | 15.7 | **+8%** |
| POW-YOU-256 | Young | 19.5 | 16.8 | 17.5 | -14% |
| POW-OAK-283 | Oak | 18.2 | 16.4 | 17.0 | -10% |
| POW-BAR-198 | Bare Necessity | 16.9 | 15.8 | 14.8 | -7% |
| POW-HAR-139 | Hard to Get | 15.6 | 15.7 | 15.5 | **+1%** |
| POW-EMB-602 | Ember | 10.4 | 13.4 | 12.3 | **+29%** |

Top colours much tighter to model than AUS. Peachy, Hard to Get, Ember beating model; several others within 10%. UK colour mix is the healthiest of the four regions.

---

## WEEKLY KIT TREND (last 9 weeks)

| Week | Dates | Kits | Daily | vs Projected (109.2) | Notable |
|---|---|---:|---:|---:|---|
| W9 | 23 Feb–01 Mar | 453 | 75.5 | -31% | 6d week |
| W10 | 02–08 Mar | 543 | 77.6 | -29% | B2 transition prep |
| W11 | 09–15 Mar | 585 | 83.6 | -23% | — |
| W12 | 16–22 Mar | 473 | 67.6 | **-38%** 🔻 | B360 mailer shortage + OOS |
| W13 | 23–29 Mar | 610 | 87.1 | -20% | Recovery |
| W14 | 30 Mar–05 Apr | 583 | 83.3 | -24% | — |
| W15 | 06–12 Apr | 671 | **95.9** | **-12%** ⬆ | Easter sale 4–12 Apr |
| W16 | 13–19 Apr | 585 | 83.6 | -23% | **First full week on Fulfillable (live 13 Apr)** |
| W17 | 20 Apr | 61 | 61.0 | -44% | 1 day, not a trend |

**Read:**
- W15 Easter bump (+15% wk-on-wk) consistent with AUS pattern.
- **W16 holding steady at 83.6/d** post-transition — no material dent from the B360 → Fulfillable live-switch. Healthy signal for the migration.
- W16 rate aligns with the 9-week baseline (80–87/d band). UK's "normal" is clearly ~84/d — which is exactly the model base. The 1.3x ambition is the gap.

---

## CONTAINER ARRIVALS DETECTED

| Date | SKUs | Units | Top 3 | Match |
|---|---:|---:|---|---|
| 14 Apr | 194 | +2,409 | ACC-LAB +253, ACC-THA +253, STO-MAI-2 +156 | B360 tidy-up / Fulfillable initial PO processing |
| 16 Apr | 16 | +16 | trivial (+1 each) | Noise |

B360 tab is now essentially static post-transition. Real Fulfillable inbound (Chemence, etc.) flows through the PASTE tab and POS MODEL header, not the B360 daily snapshot.

---

## INVENTORY DISCREPANCIES

### Transition-related ~1,000-unit single-day deductions (Mar)

Wave of ~1,000-unit deductions across 12 colours between 10–25 Mar plus a trio on 25 Mar for Base/Seal/Glow (~1,657 each). **Not an anomaly — these are the B360 pre-transition consolidations:**

- 25 Mar Base+Seal+Glow ~1,657 each: the documented 982 quarantined Complete Kit swap + related work orders
- 10–25 Mar colour ~1,000 spikes: B360 packup consolidation moves (stock pulled off active shelves into packup cartons)
- 12 Mar POW-ORC-038 2,099: single large allocation — possibly bulk transfer or work order

All explained by the 3PL transition. **No open integrity action** unless the totals don't reconcile with the packup stock counts (cross-ref when packup inventory list lands from Mason/Chris).

### Kit 3PL deductions vs Shopify (14d, B360)

| SKU | 3PL Ded/d (B360) | Shopify/d | Gap |
|---|---:|---:|---:|
| KIT-STA-2 | 17.2 | 14.0 | +3.2 aligned |
| KIT-COM-4 | 28.8 | 26.7 | +2.1 aligned |
| KIT-ULT-6 | 45.5 | 46.6 | -1.1 aligned |

Kits aligned within 3/d across the final B360 operating period. **No integrity red flag.**

### Base/Glow 3PL rate caveat

Pre-transition, B360 was NOT deducting Base/Glow per kit (liquids were inside the kit box). Post-transition, Fulfillable DOES deduct per kit. So the "3PL slower" flag on LIQ-BAS-2 (1.2/d B360 vs 14.6/d Shopify standalone) is an artefact of the old 3PL setup — not a real data gap. Going forward on Fulfillable, the 3PL deduction should match kit-adjusted ~100/d.

---

## SELLING PERFORMANCE FLAGS

### 📈 Sales spikes (7d > 30d by 50%+)

| SKU | Name | 7d | 14d | 30d | Spike |
|---|---|---:|---:|---:|---:|
| LIQ-BAS-2 | Base (standalone) | 26.4 | 14.6 | 7.8 | **+238%** |
| POW-FRI-778 | ? | 2.3 | 1.3 | 0.6 | +283% |
| POW-VIO-11932 | ? | 1.7 | 1.3 | 0.6 | +183% |
| POW-ICE-266 | ? | 5.0 | 2.7 | 3.3 | +52% |

**Base standalone +238% is material.** 26.4/d last 7 days vs 7.8/d 30d avg. Combined with kit consumption (~87/d), Base is burning through 113/d post-W15. Tightens the Chemence 28 Apr fill math — even without a Nordic split, 833 / 113 = 7.4d = stocks out ~28 Apr.

**If this 7d rate holds**, Base will stock out the same day Chemence dispatches. Zero margin for dispatch slip. Ping Viktorija mid-week to confirm 28 Apr is firm.

### 📉 Sales drops (7d < 30d by 40%+)

| SKU | 7d | 14d | 30d | Drop | Likely cause |
|---|---:|---:|---:|---:|---|
| POW-BRE-109 | 0.0 | 1.2 | 1.5 | -100% | Possibly OOS on Fulfillable (colour backorder list) |
| POW-COT-030 | 0.0 | 2.7 | 4.2 | -100% | Same |
| POW-VIB-529 | 0.0 | 2.1 | 2.5 | -100% | Same |
| POW-LUC-D110 | 0.4 | 1.2 | 1.3 | -69% | Possibly OOS |
| POW-NEB-010 | 0.6 | 1.1 | 1.5 | -60% | Possibly OOS |
| POW-EMP-009 | 1.0 | 1.5 | 2.1 | -52% | — |
| POW-HEA-823 | 0.6 | 1.0 | 1.2 | -50% | — |
| ACC-PRO-DRI | 0.7 | 1.4 | 1.3 | -46% | — |
| ACC-NAI-100/180 | 0.9 | 0.9 | 1.5 | -40% | Post-Easter normalisation |

The three zero-7d colours (POW-BRE-109, POW-COT-030, POW-VIB-529) likely map to the "45+ colours OOS on Fulfillable" that didn't transfer cleanly from B360. **Cross-ref with the Fulfillable backorder list** (from CX team 14 Apr).

### Standout underperformers vs model

- **KIT-COM-4 -36%** — biggest kit-level gap. Complete share running 31% vs model 38%. Worth Gav/Angelo checking whether Complete's positioning needs tuning (either more prominence or the COM→ULT upsell is too strong).
- **ACC-REM-BOW -91%** — same as AUS, model DSR badly wrong. Cut Remove Bowl from future UK containers.

### 💀 Dead stock

Only 1 SKU: POW-HOL-022 (200 units). UK has the cleanest listing hygiene of the four regions — only 1 dead-stock SKU vs AUS's 23.

### Sensitive Base signal

Mix: 100% Base / 0% Sensitive (no stock). Structural, not demand-driven. Legal-constraint per user — excluded from analysis until resolved.

---

## KEY TAKEAWAYS

1. **UK post-transition sales held up.** W16 (first full Fulfillable week) at 83.6/d = W9–W14 baseline. No go-live dent — that's a win.
2. **Base standalone spike (+238% 7d) tightens Chemence margin to zero.** At 113/d combined kit + standalone, 833 units burns out 28 Apr same day Chemence dispatches. Verify 28 Apr firm.
3. **Growth factor at 1.3x is ambitious vs current 1.04x actual.** Intentional per user. Monitor whether marketing plan delivers the lift across the next 2–3 weeks before 02082026 fill PO sizing (29 Apr deadline).
4. **Transition noise cleanly explained.** Mar ~1,000-unit colour deductions are B360 packup consolidation. Kit 3PL deductions align with Shopify within 3/d. No data integrity issue.
5. **Listing hygiene excellent** (1 dead-stock SKU), but ~3 colours showing 7d = 0 sales likely tied to the Fulfillable colour backorder list. Cross-check.

---

## FOLLOW-UP ITEMS

### Immediate
- [ ] Ping Viktorija (Chemence) to confirm 28 Apr dispatch is firm — Base burn rate says 0-day margin
- [ ] Cross-check zero-7d colours (POW-BRE-109, POW-COT-030, POW-VIB-529) against Fulfillable colour backorder list

### By end of month
- [ ] Decide on Sensitive Base/Glow: keep listings live with OOS flag, or delist until legal resolves?
- [ ] Gav/Angelo: review KIT-COM-4 positioning — 36% under model, could be CRO/messaging not supply
- [ ] Daniel: cut ACC-REM-BOW from UK 02082026 (1,927d cover, 0 demand standalone)

### Ongoing
- [ ] Watch Fulfillable deduction rates become available in PASTE / new tab (currently still B360 tab for script analysis — ask Greg when a Fulfillable daily snapshot tab will exist)
- [ ] Monitor W17 to see if post-Easter softness holds or recovers
