# Nordic Review - 4 Jun 2026

> Last touch: 7 May POS Check + Recap (28 days ago). Nothing structured since. Daniel re-engaged 19-29 May with new SUMMARY format and placed NORDIC 09092026 PO. Big news this week: kits are surging, Paragon Remove fill has finally landed (partial), and Heal-in-kits has crossed from "future planning item" to "live operational issue on COM kits within 13-28 days."

## SITUATION RIGHT NOW

- **Kit sales have flipped.** 30d 44.6/d → 7d 72.7/d → W23 6-day rate 42.3/d (sample bias, see below). **Driven by KIT-COM-4 surging from 22.6/d 30d to 48.7/d 7d**, against a model expectation that Ultimate was the dominant kit. Cause unclear from Slack — no Nordic-specific sale in #sale-announcements since May 9 Powder Room launch.
- **COM kits hit the pick-time-liquid wall in 13-28 days** (16 Jun at 7d rate, 1 Jul at 30d rate). After 626 COM units sell, every COM order needs loose Base + Glow + Heal added at the warehouse. Per Daniel 1 Jun.
- **Paragon Remove fill landed partial** (per Adib 3 Jun): 10,020 × 120ml shipped to Shelfless (6,576 on 7 May + 3,444 on 1 Jun), 7,116 × 500ml (capped by short caps; 2,884 bottles still at Paragon awaiting more caps from a new top-up). Stock now reads ACC-REM 6,343 and ACC-REM-500 6,285 in POS MODEL.
- **Chemence Nordic Base/Glow fill PO still not placed.** 26 days past the 9 May deadline from the last review. Cycle is 63 days; if placed today, Shelfless arrival ~6 Aug — borderline-late if COM-pickadd starts 16 Jun and Base loose burns at ~31/d.
- **NORDIC 09092026 PO placed by Daniel 27 May** (20GP, place date 27 May, completion 6 Jul, arrival 30 Aug, 1.5x DSR). **Daniel flagged 3 Jun: no new colour collections were added** despite the PO requesting them. Needs Sally rectification before production locks.
- **Adib comms back online.** Same-week responses on Paragon, Dippi stock tracker, and shipping rate breakdowns. No longer in the comms-freeze pattern of the 7 May recap.

## ACTIONS FROM 7 MAY REVIEW - STATUS

| # | Action | Owner | Status |
|---|---|---|---|
| 1 | Chemence Nordic Base/Glow fill PO place by ~13 May | Joel | 🔴 MISSED. 22 days past, no PO. Window now 9 weeks late on the worst-case planning curve. |
| 2 | Paragon Remove 120ml/500ml landed | Adib/Joel | 🟡 PARTIAL. 10,020 × 120ml delivered (7 May + 1 Jun). 500ml only 7,116 of 10,000 (cap shortage). |
| 3 | Greg switch NORDIC 14012026 to Landed, zero inbound | Greg | 🟡 PARTIAL. Container is in model but extract still shows POS MODEL `updated` blank. Need to verify Greg's reconciliation. |
| 4 | Daniel place NORDIC 02082026 fill PO | Daniel | ✅ DONE - but renamed. Placed as NORDIC 09092026 on 27 May. Note: new colour collections NOT included, flagged 3 Jun for rectification. |
| 5 | Daniel confirm Sensitive Base/Glow status | Daniel | 🟡 Not formally answered. 7 May POS Check had 1,000 SEN-4 inbound on 01072026 and 216 SEN-2 on 02082026. Current extract: 84 SEN-2 + 113 SEN-4, both still on inbound manifests. |
| 6 | Greg populate Nordic Shelfless 3PL tab | Greg | 🔴 STILL MISSED. Extract shows "B360 tab not found" - 3PL deduction integrity remains blind. |
| 7 | Greg/Adib surface ACC-LAB/INS/THA per-language in POS MODEL | Greg/Adib | 🔴 STILL NOT VISIBLE in product table. |
| 8 | Joel re-engage Adib | Joel | ✅ RESOLVED. Adib responsive throughout May 19 - Jun 3. |

**The one that matters: place Chemence Nordic Base/Glow fill PO.** Was the #1 action 4 weeks ago and is now urgent. See "Critical Dates" below for the math.

## STOCK POSITION (4 Jun 2026)

### Kits — surging, but well-stocked
| Kit | On Hand | D-Stock | Combined | 7d/d | 30d/d | Cov @ 7d | Cov @ 30d | Inbound (01072026 / 09092026 / 16102026) |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| KIT-STA-2 | 2,612 | 1 | 2,613 | 9.0 | 7.5 | 290d | 348d | 868 / 0 / 392 |
| KIT-COM-4 | 1,443 | 6 | 1,449 | **48.7** | 22.6 | **30d** | **64d** | 868 / 700 / 812 |
| KIT-ULT-6-UNIT | 3,509 | 3 | 3,512 | 15.0 | 14.5 | 234d | 242d | 1,232 / 1,120 / 1,148 |
| **Total kits/day** | | | | **72.7** | **44.6** | | | |

- KIT-COM-4 cover is the only kit risk. At the 7d rate (48.7/d), bare stock runs out in 30 days = 4 Jul, before NORDIC 01072026 arrival 1 Aug. **At the 30d rate it lasts 64 days (~7 Aug) which clears 01072026 comfortably.**
- W23 (1-3 Jun) is only 3 days of data and could be sale-driven. Worth checking with Gav whether there's a Nordic-specific campaign live. Either way, watch COM through the week.

### Liquids — Heal-in-kits is the headline (see Critical Dates)
| SKU | Stock | D-Stock | Combined | Standalone 7d | Cov @ Standalone | Inbound |
|---|---:|---:|---:|---:|---:|---|
| LIQ-BAS-2 (Base) | 932 | 0 | 932 | 8.9/d | 105d | Express 432 |
| LIQ-BON-1 (Bond) | 603 | 0 | 603 | 1.3/d | 464d | NORDIC 01072026: 432 |
| LIQ-SEA-3 (Seal) | 371 | 48 | 419 | 3.0/d | 140d | 01072026: 864 / 16102026: 216 |
| LIQ-GLO-4 (Glow) | 372 | 829 | 1,201 | 1.6/d | 751d | none |
| LIQ-HEA-5 (Heal) | 0 | **1,657** | 1,657 | 0.3/d | 5,524d | none (HEA-EMP empties: 10k on 09092026) |
| LIQ-MAT-4 (Matte) | 135 | 0 | 135 | 2.3/d | 59d | 09092026: 216 |
| LIQ-SOA-6 (Soak) | 1,021 | 7 | 1,028 | 0.7/d | 1,469d | 01072026: 432 |
| LIQ-SEN-2 (Sens Base) | 84 | 0 | 84 | 1.0/d | 84d | none |
| LIQ-SEN-4 (Sens Glow) | 113 | 0 | 113 | 0.9/d | 126d | 01072026: 1,000 (verify) |

- **Standalone cover is fine across all liquids.** The risk isn't standalone, it's the moment they become kit-attached at pick (next section).
- **LIQ-HEA-5 GD stock is 0.** All on-hand Heal at Shelfless is Dippi-prefix. Adib confirmed Dippi Heal is currently being shipped to standalone Heal buyers via the swap app.
- LIQ-SEN-2/4 sales sustained at ~1/d each on 7d - low but not zero. The "discontinue" decision from 19 Apr is still ambiguous and 1,000 SEN-4 sits on NORDIC 01072026 manifest.

### Remove + Bowl
| SKU | Stock | D-Stock | Combined | Total cons 7d (GD+D+bun) | Cov @ Total | Inbound |
|---|---:|---:|---:|---:|---:|---|
| ACC-REM (120ml) | 6,343 | 0 | 6,343 | 8.8/d | 720d | none (5k on UK 30082026, not Nordic) |
| ACC-REM-500 | 6,285 | 0 | 6,285 | **58.7/d** | 107d | 2,884 still at Paragon (cap-blocked) |
| ACC-REM-BOW | 2,266 | 453 | 2,719 | 4.1/d standalone + bundle | varies | 01072026: 1,000 / 09092026: 2,220 / 16102026: 1,020 |

- **ACC-REM-500 demand surged from 21.8/d 30d to 48.4/d 7d** (GD standalone only). With bundles + Dippi added in, real consumption 58.7/d 7d. **At 6,285 units that's 107d cover** — comfortable, but watch the trajectory. The cap-blocked 2,884 at Paragon would extend cover but unlocking that needs Adib to push Paragon for more 500ml caps.
- ACC-REM 120ml at 720d cover - massively overstocked at this rate. Standalone demand was supressed pre-fill so the 8.8/d figure is the real baseline.
- Bowl looks oversupplied through 30 Aug.

### Empties for local fills
| SKU | Stock | D-Stock | Combined | Inbound |
|---|---:|---:|---:|---|
| ACC-RE1-BOT (120ml) | 10,000 | 0 | 10,000 | 01072026: 5,000 |
| ACC-RE5-BOT (500ml) | 0 | 0 | 0 | 01072026: 5,000 / 09092026: 10,000 |
| HEA-EMP / HEA-LID / HEA-BSH | 0 | 0 | 0 | 09092026: 10,000 HEA-EMP only |

- **Heal empties pipeline does not start arriving until NORDIC 09092026 (30 Aug).** Heal LIDs and Brushes still not on any manifest. Paragon Heal fill is months out unless empties get sent express.

### Tips - all comfortable
All five tip SKUs sit on combined cover >130d. Dippi-prefix tip stock (3,124 pcs per Adib 29 May = Coffin 802 + Square 690 + Stiletto 847 + Ballerina 743 + others) is contributing through the swap mechanism.

### Other accessories
- ACC-PRO-DRI: 355 GD / 0 D / cov 237d at model rate. Daniel's "potential express" flag from 19 Apr no longer applies.
- ACC-NAI-LIN: 480 GD + 877 D = 1,357 combined / 320d cov model. No risk.

### Packaging
- STO-BUB-BAG-L (Bubble Mailer L): 36,626 GD + 7,101 D = 43,727 combined. Still ~2yr cover. Adib's bulk order absorbed.
- STO-MAI-BAG-S: 3,378 + 3,070 D = 6,448. 215d cover. Fine.
- STO-MAI-2: 7,220. 241d cover. Fine.
- ACC-LAB / ACC-INS / ACC-THA: still not in Nordic POS MODEL. Adib prints locally; visibility gap remains.

## CRITICAL DATES — when stock is needed

### 1. KIT-COM-4 Base/Glow/Heal "kits-need-liquids-at-pick" trigger
Per Daniel 1 Jun: 626 of the 1,830 COM kits had B/G/H pre-packed inside. The other 1,204 (from NORDIC 14012026) don't. Once the pre-packed 626 sell through, Shelfless must add 1× Base + 1× Glow + 1× Heal per COM kit at pick.

| Selling rate | COM-prepacked exhaustion | Date |
|---|---:|---|
| 7d (48.7/d) | 13d | **16 Jun 2026** |
| 14d (33.3/d) | 19d | **22 Jun 2026** |
| 30d (22.6/d) | 28d | **1 Jul 2026** |

Most likely window: **17 Jun - 1 Jul** depending on whether the COM surge is sustained.

After that date, Base/Glow/Heal pull rates become (assuming 30d kit rate for forecasting + standalone):
- Base: ~31/d (22.6 COM + 8.8 standalone)
- Glow: ~23/d (22.6 COM + 0.8 standalone)
- Heal: ~23/d (22.6 COM + 0.2 standalone)

Loose stock cover post-trigger (at 30d rates):
- Base: 932 + 432 inbound = 1,364 → **44d** → OOS ~14 Aug at the earliest trigger date
- Glow: 1,201 combined (incl. 829 D-Glow) → **52d** → OOS ~21 Aug
- Heal: 1,657 D-stock (all Dippi) → **72d** if usable → OOS ~10 Sep (but currently being routed to standalone Heal buyers, not kit attach — decision needed)

NORDIC 01072026 arrives 1 Aug. Contents: 432 BON + 864 SEA + 432 SOA. **Zero Base or Glow on 01072026.**
NORDIC 09092026 arrives 30 Aug. Contents: 216 MAT + Heal empties (10k) + Remove empties. **Zero filled Base/Glow/Heal on 09092026 either.**

Conclusion: **Chemence Nordic Base/Glow fill is the only path to Base/Glow before 30 Aug.** Cycle is 63 days. If placed today (4 Jun), goods at Shelfless ~6 Aug. That means we will run on the current Base + Express 432 + Glow combined stock for 8-11 weeks. The 30d-rate math says we'd OOS Base around 14 Aug, so a Chemence PO placed today lands 8 days before the Base wall.

### 2. Heal — there is no path before Chemence/Paragon kicks in
- Real consumption when COM-pickadd starts: ~23/d
- Loose Heal available: 1,657 (all D-prefix, currently routed to standalone swaps)
- 1,657 / 23 = ~72 days cover from the 17 Jun trigger → ~28 Aug OOS
- HEA-EMP empties arrive 30 Aug. Add Paragon fill cycle (probably 4-8 weeks). Fresh Heal arrives Shelfless ~mid Oct at the earliest.
- **Gap: 28 Aug to ~mid-Oct = 4-7 weeks of Heal OOS** if D-Heal is rerouted to kit attach AND standalone Heal swap continues.

Options to mitigate:
- (a) Stop routing D-Heal to standalone-swap (small demand 1.2/d combined GD + D Heal standalone) and reserve for kit attach. Buys time.
- (b) Bring HEA-EMP forward — air-freight a portion ahead of NORDIC 09092026. Daniel's call.
- (c) UK Oils4Life can fill Heal in 21d at 8k qty — send empties UK → fill → ship to Sweden. Roughly 6 weeks total. If ordered now, lands ~mid-July - the earliest realistic path.
- (d) Substitute COM orders to STA + standalone Bond, as Axel proposed 1 Jun (Daniel rejected as a process fix, but it's still a possible bridge if other paths fail).

### 3. KIT-COM-4 itself
At 7d 48.7/d the bare-stock COM lasts 30 days (~4 Jul), but NORDIC 01072026 doesn't arrive until 1 Aug. Gap: 28 days at the 7d rate.
At the 30d 22.6/d rate, bare stock lasts 64 days (~7 Aug) - clears 01072026. So this risk is entirely dependent on whether the 7d surge holds. **Watch W23 full-week data Mon 8 Jun.**

### 4. NORDIC 01072026 in production
- Last status: completion 28 May per Remy's 29 May summary. Three weeks earlier than the sheet's previous 21 May estimate.
- Arrival per current POS MODEL: 1 Aug 2026.
- 28 May: Remy recommended pulling 1,000 Pro File 100/180 — Joel to update PO.

### 5. NORDIC 09092026 placed - colour collections gap
Daniel 3 Jun: no new colour collections added despite the recommendation. Sally lead 5-6 weeks; rectification window is closing fast.

## SELLING TREND

| Week | Dates | Days | Total | /day | vs base 46/d | vs scaled 69/d |
|---|---|---:|---:|---:|---:|---:|
| W15 | 06-12 Apr | 14 | 274 | 19.6 | -57% | -72% |
| W16 | 13-19 Apr | 14 | 253 | 18.1 | -61% | -74% |
| W17 | 20-26 Apr | 14 | 279 | 19.9 | -57% | -71% |
| W18 | 27 Apr-3 May | 14 | 319 | 22.8 | -50% | -67% |
| W19 | 04-10 May | 14 | 287 | 20.5 | -55% | -70% |
| W20 | 11-17 May | 14 | 264 | 18.9 | -59% | -73% |
| W21 | 18-24 May | 14 | 161 | 11.5 | -75% | -83% |
| W22 | 25-31 May | 14 | 412 | 29.4 | -36% | -57% |
| W23 | 01-03 Jun | 6 | 254 | 42.3 | -8% | -39% |

> Note: the `weekly_kit_trend` from extract.py shows "days=14" against 7-day windows - likely double-counting STA+COM+ULT or a script bug. Treat directional trend as accurate, absolute /day figures with caution. The Shopify sku_dsr aggregation (72.7/d 7d, 44.6/d 30d) is the more authoritative read.

What this says: **kits bottomed W21 then recovered hard W22-W23.** W21 was likely a data/processing gap (or one bad week); W22-W23 are tracking close to model base for the first time since transition. The KIT-COM-4 surge (22.6→48.7/d on 30d→7d) is doing most of the lift.

**No Nordic-specific campaign visible in #sale-announcements covering this window.** Worth asking Gav whether a Nordic-specific email/promo ran late May.

## D-STOCK SWAP - WHAT'S STILL FIRING

Per Adib 29 May, Dippi stock currently used for standalone individual sales via swap app:

| Item | Dippi qty remaining (Adib 29 May) | Notes |
|---|---:|---|
| Heal | 1,657 | Routed to standalone Heal buyers. **Decision needed: keep here, or reserve for kit attach?** |
| Glow | 829 | Routed to standalone D-LIQ-GLO-4 sales (3.1/d 7d) and bundle/kit demand fill |
| Seal | 48 | Selling 6.1/d via D-LIQ-SEA-3 — running low |
| Soak | 7 | Effectively done |
| Nail Tips (combined) | 3,124 | Coffin 802 + Square 690 + Stiletto 847 + Ballerina 743 |
| Remove Bowl | 453 | D-ACC-REM-BOW selling 2.7/d 7d |
| Nail Art Liners | 877 | Effectively no D-prefix sales — Greg may have GLAMRDiP-mapped all of these |
| Colours | ~47,339 | Long tail — most sell via GD-sku swap, not D-sku standalone |

**Items going dormant per Adib (no longer being used):**
- Dippi mailer bags (7,101 still on hand)
- Dippi instruction booklets
- Dippi thank you cards
- Dippi small mailer bags
- Dippi kits (only 10 pcs total — effectively gone)

The 29 May discussion point from your summary: **stop accounting for the dormant Dippi items in the model.** Decision still pending on Joel/Daniel side.

## OPEN THREADS

**[ESCALATING] Chemence Nordic Base/Glow fill PO - 22 days past 13 May deadline**
- First raised: 19 Apr (Daniel rebuild)
- Action: Joel to email Vik this week. Use UK 22-04-2026 PO as template. Suggest 4k Base + 3k Glow.

**[ONGOING] Heal in kits decision tree**
- New issue this cycle. Per Daniel 1 Jun: 30 days cover before COM kits need pick-time Heal. After that, ~23/d consumption.
- Action: Daniel/Joel choose path (UK Oils4Life bridge / express HEA-EMP / reroute D-Heal / accept gap).

**[PARTIAL] Paragon Remove fill**
- 10,020 × 120ml delivered. 7,116 × 500ml delivered, 2,884 capped at Paragon awaiting more closures.
- Action: Adib push Paragon for cap supply / Paragon top-up order. Remy + Daniel to reconcile real Paragon-on-hand vs sheet (Daniel asked 4 Jun).

**[NEW] NORDIC 09092026 missing new colour collections**
- Daniel flagged 3 Jun: rectification needed before Sally locks production. Joel sign-off + Wiktoria curation pending.

**[ONGOING] Greg's Nordic POS MODEL tabs incomplete**
- B360 tab still not found by extract. ACC-LAB / ACC-INS / ACC-THA per-language still not in product table. POS MODEL `updated` cell blank.
- Action: Greg to populate.

**[ONGOING] Sensitive line discontinuation reality**
- 19 Apr Daniel said "will sell out, won't be replenished." 7 May POS Check found 1,000 SEN-4 inbound on 01072026 + 216 SEN-2 on 02082026. Today: SEN-2 stock 84, SEN-4 stock 113, both still selling ~1/d.
- Action: Daniel confirm yes/no. If yes, zero the OLs. If no, plan replenishment cadence.

**[ONGOING] Shelfless FIFO and Paragon stock tracker**
- Daniel 1 Jun pushed hard: FIFO must be enforced, stock tracker must be filled out, Remy + Daniel introduced direct to Shelfless + Paragon to take over.
- Action: Adib to schedule introductions.

**[ONGOING] D-variant pricing delta**
- Open since 16 Apr. No movement. Small kr 0.29-3.60 rounding errors on D-priced items routed via swap. Joel/Daniel decision.

## DECISIONS PENDING

- **Joel:** Place Chemence Nordic Base/Glow fill PO this week. 22 days late on the planning curve.
- **Joel:** Sign off NORDIC 09092026 colour additions + free-gift qty (min 5k Travel Bag/French Dip Tray/Mani Mat).
- **Joel/Daniel:** Heal bridge strategy (UK Oils4Life vs HEA-EMP air-freight vs accept gap).
- **Joel/Daniel:** Reserve Dippi Heal for kit-attach vs continue swap-to-standalone-buyers.
- **Daniel:** Confirm Sensitive Base/Glow discontinuation — zero or keep.
- **Daniel:** D-variant pricing fix decision (open 7 weeks).
- **Adib:** Schedule Shelfless + Paragon intros for Remy and Daniel.

## RECOMMENDED ACTIONS (CRITICAL)

🔴 **THIS WEEK**

1. **Joel: place Chemence Nordic Base/Glow fill PO.** ~4,000 Base + ~3,000 Glow. Brief Vik: "Nordic - complete by Fri 14 Aug." Lands Shelfless ~21 Aug. This is the only path that gets fresh Base/Glow to Shelfless before late October.
2. **Daniel/Joel: lock Heal bridge strategy.** Recommend UK Oils4Life parallel order (3k-5k Heal) - 6 week cycle, lands ~mid July, well before D-Heal exhausts.
3. **Daniel: NORDIC 09092026 colour collections rectification.** Push Joel for sign-off + Wiktoria selection this week. Sally lead 5-6w from 27 May = production locks ~10 Jul.
4. **Adib: push Paragon for caps for the remaining 2,884 × 500ml.** Each unblocked unit is ~12hrs of cover at current burn.

🟡 **THIS FORTNIGHT**

5. **Greg: rebuild Shelfless 3PL tab in POS MODEL.** Has been the long-standing visibility gap for 5+ cycles.
6. **Greg: add ACC-LAB-NO/SE/DK/FI, ACC-INS-NO/SE/DK/FI, ACC-THA per-language stocks to POS MODEL product table.**
7. **Daniel: confirm Sensitive line status.** Either zero 01072026 1,000 SEN-4 OL + 02082026 216 SEN-2 OL, or formally drop the discontinuation.
8. **Remy + Daniel: get introduced to Shelfless + Paragon direct, per Daniel 1 Jun.**

🟢 **MONITOR**

9. **W23 full-week kit data Mon 8 Jun.** If KIT-COM-4 sustains at >40/d, recompute COM bare-stock OOS date and consider expediting NORDIC 01072026.
10. **D-Heal allocation visibility.** Once D-Heal stock starts running low, decide who has priority.
11. **POW-BLO-D07 cover 22d** at 9/d 7d, only 200+800 inbound from 09092026/16102026. Watch.

## WATCH FOR NEXT REVIEW

- Did Chemence Nordic PO go in? If not, this becomes a 2-month overdue item.
- Is COM-4 surge sustained or did W23 prove a one-week spike?
- Did Adib unblock the 500ml Paragon stock?
- Did NORDIC 09092026 colour collection issue get rectified before Sally locked?
- Heal bridge path - chosen and in motion?
