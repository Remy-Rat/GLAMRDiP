# 🇸🇪 Nordic POS Model Check — 7 May 2026

## DATA FRESHNESS

- **POS MODEL:** xlsx re-pulled today; `UPDATED` cell = empty (Greg hasn't filled the freshness marker — Nordic-specific gap, AUS/CA/UK have them populated).
- **3PL (Shelfless) tab:** empty (`tpl.last_valid_date = None`). No fulfilment-side cross-check available. Greg's "rebuild Nordic POS MODEL B360 tab" task from previous cycles still outstanding. **All cover figures below are model-only — no 3PL deduction reality check.**
- **Shopify:** through 2026-05-06 (1d lag, normal).
- **ShipHero:** N/A — Shelfless does not use ShipHero.
- **Growth factor:** 1.5x (kit base 46/d → scaled 69/d).
- **Manual overrides applied:** NORDIC 14012026 treated as **Landed and Checked In** per user (sheet still shows On the Way / est arrival 22 Apr — Greg to update). User confirmation: "lots of Glow on hand"; "432 Base coming from UK Chemence so Base is okay"; "Dippi-prefix kits not selling — only new GLAMRDiP kits"; "growth factor 1.5x is real."

## STOCK POSITION

Two cover columns: **Cov @ Model DSR** (Greg's per-SKU rate × 1.5x where applicable) and **Cov @ Actual** (Shopify 30d standalone). Combined stock (GLAMRDiP + Dippi D-prefix) where Dippi is still picking via swap.

### Kits (kit base actual 7d 42.9/d, 14d 43.3/d, 30d 40.2/d vs scaled 69/d)

| SKU | Stock | D-Stock | Combined | Model DSR | Cov @ Model | Actual 7d | Cov @ Actual | Inbound (01072026 / 02082026) |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| KIT-STA-2 | 2,832 | 1 | 2,833 | 16.5 | 172d | 8.1 | 350d | 868 / 1,008 |
| KIT-COM-4 | 2,699 | 6 | 2,705 | 21.0 | 129d | 14.7 | 184d | 868 / 1,092 |
| KIT-ULT-6-UNIT | 3,918 | 3 | 3,921 | 31.5 | 124d | 20.1 | 195d | 1,232 / 1,568 |

D-kits at ~0/d. Stock is fine on all three at the actual rate; even at scaled 1.5x model, no kit is below 124d cover.

### Liquids

| SKU | Stock | D-Stock | Combined | Model DSR | Cov @ Model | Actual 7d / 30d | Cov @ Actual | Inbound |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| LIQ-BAS-2 (Base) | 778 | 0 | 778 | 27.0 | 29d | 5.9 / 10.3 | 76-132d | Express Base 432 + 14012026 216 |
| LIQ-BON-1 (Bond) | 691 | 0 | 691 | 9.0 | 77d | 2.4 / 3.6 | 192-288d | 14012026 432 |
| LIQ-SEA-3 (Seal) | 400 | 199 | 599 | 15.0 | 27d^ | 2.4 / 2.4 | 250d | 14012026 648 |
| LIQ-GLO-4 (Glow) | 400 | 912 | 1,312 | 12.0 | 33d^ | 0.9 / 1.4 | 937d | none |
| LIQ-HEA-5 (Heal) | -3 | 1,697 | 1,694 | 0 (model blank) | n/a | 0.1 / 0.4 | 4,235d | none |
| LIQ-MAT-4 (Matte) | 187 | 0 | 187 | 7.5 | 25d | 1.0 / 1.4 | 134d | 14012026 300 |
| LIQ-SOA-6 (Soak) | 1,048 | 37 | 1,085 | 6.0 | 181d | 0.9 / 0.8 | 1,356d | 01072026 300 |
| LIQ-SEN-2 (Sens. Base) | 117 | 0 | 117 | 7.5 | 16d | 0.7 / 1.6 | 73d | 02082026 216 |
| LIQ-SEN-4 (Sens. Glow) | 137 | 0 | 137 | 6.0 | 23d | 1.6 / 1.5 | 91d | 01072026 1,000 |

^ Model cover for Seal and Glow looks worse than reality because model_dsr assumes kit-attached pull. **Per Region/Component Map ambiguity for Nordic:** Heal/Bond/Glow planned to be added at Shelfless per kit (kit-adjusted), but Adib's 19 Apr message said "no GLAMRDiP liquids filled by Paragon" for Heal — actual kit-adjusted setup is partial / in flux. Treat Bond+Glow as plausibly kit-adjusted (Chemence fill route confirmed) and Heal as standalone-only until Paragon Heal fill begins.

**Sensitive line:** Daniel 19 Apr said discontinued ("won't be replenished"), but NORDIC 01072026 has 1,000 LIQ-SEN-4 inbound and 02082026 has 216 LIQ-SEN-2. **Either OL hasn't been zeroed by Greg or the discontinuation decision was reversed.** Confirm with Daniel.

### Remove products & Bowl

| SKU | Stock | D-Stock | Combined | Model DSR | Cov @ Model | Actual 7d / 30d | Cov @ Actual | Inbound |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| ACC-REM (120ml) | 0 | 20 | 20 | 0 | n/a | 0.0 / 0.5 | **40d** | Paragon 10,000 (overdue 18d) |
| ACC-REM-500 (500ml) | -3 | 92 | 89 | 0 | n/a | 5.7 / 5.0 | **18d** | Paragon 10,000 (overdue 18d) |
| ACC-REM-BOW (Bowl) | 2,572 | 577 | 3,149 | 28.5 | 90d | 1.1 / 1.0 | 3,149d | 14012026 500 + 01072026 300 + 02082026 200 |

**ACC-REM-500 at 18d is the tightest on-hand cover in the region.** Paragon Remove fill (10k 120ml + 10k 500ml) was Adib's 19 Apr "next week" promise — 18 days late, no Shelfless inbound yet. If Paragon fill lands within ~14d the gap closes; if it slips further, ACC-REM-500 OOS is real.

ACC-REM (120ml) Shopify 7d = 0/d almost certainly because there's no fulfillable stock — true demand is not 0/d. 30d 0.5/d may also be supressed. Once Paragon fill lands, expect ACC-REM consumption to lift toward what 30d says.

ACC-REM-BOW massively overstocked at actual 1.0/d.

### Empties (component bottles for local fills)

| SKU | Stock | D-Stock | Combined | Inbound |
|---|---:|---:|---:|---|
| ACC-RE1-BOT (120ml empties) | 20,000 | 9,225 | 29,225 | 01072026 5,000 |
| ACC-RE5-BOT (500ml empties) | 10,000 | 8,906 | 18,906 | 01072026 5,000 |
| HEA-EMP / HEA-LID / HEA-BSH | 0 | 0 | 0 | none |

29k Remove 120ml empties + 19k Remove 500ml empties at Shelfless are the input pool for Paragon's filling. **Heal empties at 0** — if/when Heal kit-adjustment activates and a Heal Paragon fill is initiated, empties pipeline needs setting up first.

### High-volume accessories / tips

| SKU | Stock | D-Stock | Combined | Actual 30d | Cov @ Actual | Inbound |
|---|---:|---:|---:|---:|---:|---|
| ACC-TIP-ALM (Almond) | 2,223 | 0 | 2,223 | 6.2 | 359d | none |
| ACC-TIP-COF (Coffin) | 1,299 | 843 | 2,142 | 0.6 | 3,570d | 01072026 400 + 02082026 500 |
| ACC-TIP-BAL (Ballerina) | 1,699 | 776 | 2,475 | 0.4 | 6,188d | 01072026 100 |
| ACC-TIP-SQU (Square) | 500 | 716 | 1,216 | 0.4 | 3,040d | none |
| ACC-TIP-STI (Stiletto) | 500 | 858 | 1,358 | 0.2 | 6,790d | 01072026 400 |
| ACC-PRO-DRI (Pro Drill) | 381 | 0 | 381 | 1.9 | 200d | none |
| ACC-NAI-LIN (Nail Liner) | 480 | 954 | 1,434 | 1.9 | 755d | 01072026 100 |
| ACC-NAI-SET (Pro File Set) | n/a | n/a | n/a | 2.0 | n/a | n/a |
| ACC-BRU (Deluxe Brush) | n/a | n/a | n/a | 0.8 | n/a | n/a |

Daniel 19 Apr flagged **Pro Drill + Nail Art Liner** as candidates for Birthday Sale express. At actual 30d rate Pro Drill 200d / Nail Liner 755d cover — **no express needed**. NORDIC 01072026 lands 15 Jul; both safe well past that.

### Packaging & inserts (warehouse-only — no Shopify signal)

| SKU | Stock | D-Stock | Combined | Model DSR | Cov @ Model | Inbound |
|---|---:|---:|---:|---:|---:|---|
| STO-MAI-BAG-S (Small Satchel) | 3,922 | 3,070 | 6,992 | 90.0 | 78d | 01072026 2,000 + 02082026 2,000 |
| STO-MAI-2 (Small Box) | 8,299 | 0 | 8,299 | 90.0 | 92d | 14012026 3,636 + 01072026 3,434 + 02082026 1,616 |
| STO-BUB-BAG-L (Bubble Mailer L) | 37,893 | 7,101 | 44,994 | 60.0 | 750d | 14012026 2,400 + 01072026 3,600 + 02082026 960 |
| ACC-LAB / ACC-INS / ACC-THA | not in Nordic POS MODEL | — | — | — | — | — |

**STO-BUB-BAG-L at 750d (~2 years) is Adib's $20k bulk order.** Operationally fine, cash drag flagged at 30 Apr recap. Adib confirmed no Shelfless storage cost.

ACC-LAB / ACC-INS / ACC-THA are absent from the Nordic POS MODEL product table — Adib prints these locally per language (PRODUCTINFORMATION_FI/DK/NO/SE, DRILL-MANUAL, plus per-region ACC-LAB-NO/SE/DK/FI). Stock confirmed in-hand at Shelfless per Adib 19 Apr but quantities not surfacing in Greg's model. **Visibility gap — separate issue from this POS Check.**

### Colours

3 colours flag at <100d cover on 30d actual rate; all are D-prefix (Dippi clearance) and have generous container inbound:

| SKU | On Hand | D-Stock | Combined | 7d | 30d | Cov @ 30d | Inbound Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| POW-DRE-D08 | 235 | 0 | 235 | 3.6 | 3.8 | 62d | 1,800 |
| POW-BLO-D07 | 357 | 0 | 357 | 6.0 | 5.7 | 63d | 3,200 |
| POW-BUT-098 (Buttercup) | 365 | 0 | 365 | 4.3 | 5.1 | 72d | 200 |

Buttercup (Daniel 19 Apr flagged at 9d cover) is now 72d — recovered. Not a Birthday Sale risk anymore.

**33 colours** show 0 sales 14d (incl. 33 with stock). Almost all D-prefix or limited-edition C-S series. Listing audit candidate, not a stock risk.

## DOUBLE-COUNT DETECTION

**Container NORDIC 14012026 is in the model as "On the Way" but per user has landed and been checked in.** Every SKU with an inbound from this container is potentially over-stated by that quantity if Greg has already added it to on-hand AND left it in inbound.

Spot checks on the data: KIT-STA-2 on_hand 2,832 (no jump from prior recap baseline expectation), suggesting the 1,204 inbound HAS been added to on-hand — meaning **inbound column is the double-count to subtract** when projecting forward. But the Shelfless ASN (PO 101559) was incomplete per 30 Apr recap (100-row limit), so some of the 14012026 SKUs may NOT yet be in Shelfless on-hand → not double-counted.

**Action: Greg to switch NORDIC 14012026 to "Landed" status and zero the inbound column, keeping only the 2 missing colours (POW-GLA-CS02, POW-LAT-CS38) as still-pending if Adib hasn't located them yet.**

## CONTAINER / ORDER STATUS

| Ref | Sheet status | Sheet ETA | Reality | Action |
|---|---|---|---|---|
| Express Base | (blank header) | — | 432 BAS earmarked from UK Chemence fill, air-freight quote outstanding from Roisin/Fulfillable since 4 May | Daniel chase Roisin for quote (already in today's digest action points) |
| NORDIC 14012026 | On the Way | 22 Apr | **LANDED 20 Apr, ASN partial — 2 colours (Glacier Glow, Latte Cloud) still missing balance** | Greg switch to Landed; Adib + Greg close the 2-SKU gap |
| NORDIC 01072026 | In Production | Completion 21 May / Arrival 15 Jul | Confirmed In Production. Birthday Sale-ish container — review kit splits given mix flip. | Daniel/Joel review Ultimate-heavy mix vs sheet allocations (KIT-STA 868, KIT-COM 868, KIT-ULT 1,232 = 41% Ultimate by units) |
| NORDIC 02082026 | Ordering | Completion 15 Jun / Arrival 9 Aug | Status Ordering — fill PO not yet placed. | Daniel place fill PO with Sally |
| (unnamed) col 63 | (no ref) | Completion 22 Jul / Arrival 15 Sep | Placeholder block. | Daniel/Greg confirm what's planned here |

## LOCAL FILL STATUS

| Filler | Items | Status | Deadline |
|---|---|---|---|
| **Paragon** | Remove 120ml + 500ml (10k each) | 18d past Adib's "next week" arrival promise. Shelfless still 0. | Daniel/Joel escalate via direct ask — channel chases not working. |
| **Chemence Nordic** | Base / Glow / Bond / Seal | **PO not placed.** Per user, no urgency right now: 432 Base air-freight from UK handles immediate gap, Glow + Bond + Seal stock all >100d at actual rate. Cycle 6w fill + 1w ship + 2w buffer = 63d, so PO for arrival before NORDIC 01072026 (15 Jul) needs to be placed by ~13 May to land before container | Joel decision: place this week if covering buffer, defer to ~early Jun if 01072026 on track |
| **Paragon Heal** | (not currently in pipeline) | Heal not on Paragon fill. Standalone Heal demand is 0.1-0.4/d so not urgent. If kit-adjustment activates (Region file plans this), need to set up empties → Paragon → Shelfless cycle. | None right now; revisit when Heal kit-adjustment goes live |

## STOCK-OUT FORECAST

### CRITICAL (act within ~14 days)

- **ACC-REM-500: 89 combined units / 5.0/d 30d = 18d cover.** No firm Paragon ETA. If Paragon's 10,000 lands by ~25 May, gap closes. If past 25 May, brief OOS through to NORDIC 01072026 arrival 15 Jul (~50d gap potential).

### WARNING (act within ~30 days)

- **ACC-REM (120ml): 20 combined / 0.5/d 30d = 40d** (likely supressed because OOS — true demand probably higher). Same Paragon dependency.
- **POW-BUT-098 (Buttercup): 365 / 5.1/d = 72d.** No NORDIC inbound until 02082026 (200 units, +Aug). Buttercup is one of Adib's flagged top sellers — monitor.

### MONITOR

- LIQ-MAT-4: 187 / 1.4/d = 134d. Inbound 14012026 300 once ASN closes.
- LIQ-SEN-2 / LIQ-SEN-4: 73-91d cover. Inbound 01072026 / 02082026.
- 3 D-prefix colours (DRE-D08, BLO-D07, BUT-098 already covered) at 60-72d — clearance velocity matter for Sales Analysis, not POS Check.

### NOTHING ON ORDER (no inbound, monitor)

- LIQ-GLO-4 (Glow): 1,312 combined, no inbound. At 1.4/d 30d = 937d. Fine.
- LIQ-HEA-5: 1,694 combined, no inbound. At 0.4/d 30d = 4,235d. Fine until Heal kit-adjustment turns on.
- ACC-PRO-DRI: 381 combined, no inbound. At 1.9/d = 200d.
- ACC-TIP-ALM: 2,223, no inbound. At 6.2/d = 359d.

## CASCADING ARRIVAL PROJECTION (kits, at actual 30d 40.2/d total)

| Stage | Date | KIT-STA cover | KIT-COM cover | KIT-ULT cover | Total kit cover |
|---|---|---:|---:|---:|---:|
| NOW | 7 May | 350d | 184d | 195d | combined ~205d |
| After NORDIC 14012026 (Landed already, sheet pending) | 7 May effective | (no change to on-hand if Greg has integrated) | | | |
| After NORDIC 01072026 | 15 Jul | adds 868 / 868 / 1,232 | post-arrival drops dependent on selling rate | | ~250d cover post-arrival |
| After NORDIC 02082026 | 9 Aug | adds 1,008 / 1,092 / 1,568 | | | ~340d cover post-arrival |

At sustained -7% vs base 46/d (current actual ~43/d), **post-NORDIC 02082026 kit cover is ~11 months at actual demand**. Effectively no kit shortage risk for the rest of 2026 at current selling. The growth-factor-1.5x scenario (69/d) brings cover down to 6-7 months which is also generous.

**Container kit-mix observation:** kit splits in NORDIC 01072026 (KIT-STA 868 / COM 868 / ULT 1,232) and 02082026 (1,008 / 1,092 / 1,568) match actual mix reasonably well (Ultimate-led). Continue at 02082026 placement; no urgent rebalance needed.

## CONTAINER GAP ANALYSIS

### NORDIC 02082026 (Ordering, fill PO not placed)

Status sheet: completion 15 Jun, arrival 9 Aug. SKU OL allocations look reasonable for the kit-mix-flipped reality. Specific gaps to consider:

- **No ACC-REM-500 / ACC-REM (120ml) on container.** Both depend on Paragon refills, not Sally container. Acceptable — these are local-fill items.
- **No Heal on container.** As above, kit-adjusted setup not yet active. Acceptable.
- **No ACC-LAB / ACC-INS / ACC-THA listed.** Adib prints locally; correct.

### NORDIC 01072026 (In Production)

Sheet OLs visible. No critical gaps surfaced — kits, colours, key liquids all represented. Production complete window per sheet ~21 May, leaves 8 weeks ship + buffer to 15 Jul arrival.

## PO RECOMMENDATIONS

| PO | Owner | Recommendation | Deadline |
|---|---|---|---|
| Chemence Nordic Base/Glow/Bond/Seal fill | Joel | At actual rates: Base 132d + 432 inbound = ~210d, Glow 937d, Bond 192d + 432 inbound = ~250d, Seal 250d. **Defer until ~early June.** No 9 May deadline panic. | Place by ~13 May only if you want to lock the 1 Jul arrival window; otherwise early Jun is safe |
| Paragon Remove top-up | Joel/Daniel/Adib | Push the existing 10k + 10k Paragon order to landing first. Once landed, ACC-REM at 20,000 + ACC-REM-500 at 10,000 = ~50-100d cover at actual rate. **Next Paragon fill not needed for ~3 months.** | After current fill lands |
| Heal Paragon fill | Joel/Daniel | Not needed currently (565d combined cover at actual standalone rate). Plan for when kit-adjustment goes live. | Defer |
| Sally Birthday Sale fill PO (NORDIC 02082026) | Daniel | Fill PO not yet placed per sheet status "Ordering". Production completion target 15 Jun = need to place ~6 weeks back = early-mid May. | Place by ~15 May |

## WHAT NEEDS ACTION

🔴 **CRITICAL (this week)**

1. **ACC-REM-500: 18d cover, Paragon fill 18d overdue.** Joel/Daniel direct escalation to Adib for Paragon despatch confirmation + tracking number. The longer this slips, the harder OOS becomes to avoid through to 15 Jul container arrival.
2. **Greg to switch NORDIC 14012026 to "Landed" + zero its inbound column** so the projected on-hand isn't double-counted in next data pulls. Carry remaining 2 missing colours (POW-GLA-CS02, POW-LAT-CS38) as residual.
3. **Daniel/Greg to place NORDIC 02082026 fill PO with Sally.** Sheet shows In Ordering, completion target 15 Jun = place by ~15 May.

🟡 **WARNING (this fortnight)**

4. **Joel to place Chemence Nordic Base/Glow/Bond/Seal fill PO by ~13 May** if buffer-conservative; otherwise early Jun is safe at actual rates. Decision frame: do you want NORDIC liquids to arrive before 1 Jul container or are you happy stitching with bridges (UK 432 air-freight + existing stock)?
5. **Daniel/Joel decision on Sensitive Base/Sensitive Glow.** Sheet has 1,000 Sens-Glow on 01072026 and 216 Sens-Base on 02082026 contradicting Daniel's 19 Apr discontinuation note. Either zero those OLs or revoke the discontinuation.

🟢 **MONITOR (FYI)**

6. **POW-BUT-098 (Buttercup) at 72d cover, no near inbound.** Top-seller flag from 19 Apr; not urgent at actual rate.
7. **Greg to populate Nordic POS MODEL B360 / Shelfless tab** so future POS Checks have a 3PL deduction reality check. Backlog from prior cycles.
8. **Greg/Adib to surface ACC-LAB-NO/SE/DK/FI, ACC-INS-NO/SE/DK/FI, ACC-THA stocks** in the POS MODEL — Adib has them at Shelfless but they aren't visible in the product table.

## FOLLOW-UP ITEMS

- [ ] Joel: direct ask to Adib re Paragon Remove fill landing ETA + tracking
- [ ] Greg: switch NORDIC 14012026 to Landed; zero inbound column except missing 2 SKUs
- [ ] Daniel: place NORDIC 02082026 fill PO with Sally by ~15 May
- [ ] Joel: Chemence Nordic Base/Glow/Bond/Seal fill PO — decide place-now or defer to early Jun
- [ ] Daniel: confirm Sensitive Base/Glow discontinuation reality vs sheet OLs
- [ ] Greg: rebuild Nordic Shelfless 3PL tab (long-standing)
- [ ] Greg/Adib: surface ACC-LAB / ACC-INS / ACC-THA per-language stocks in POS MODEL

## WATCH FOR IN SALES ANALYSIS

1. **Top-seller stock-out risk through 15 Jul (NORDIC 01072026 arrival).** Already covered by colour analysis here but Sales Analysis should sanity-check at 7d trend rate not just 30d.
2. **D-prefix vs GLAMRDiP-prefix sales velocity.** D-sales running 111/d 30d total; quantify by category and identify which SKUs are dragging on Dippi clearance.
3. **Kit mix stability.** 7d 42.9, 14d 43.3, 30d 40.2 — direction is upward not downward. Quantify the trajectory to see if the -34% to -38% gap vs scaled is closing.
