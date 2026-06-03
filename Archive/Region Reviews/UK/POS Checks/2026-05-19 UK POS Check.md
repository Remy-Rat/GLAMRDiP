# 🇬🇧 UK POS Model Check — 19 May 2026

## DATA FRESHNESS

- **POS MODEL last updated:** UPDATED cell empty in the file. Sheet pulled 19 May 12:33 AEST via gcloud — assume today's snapshot.
- **3PL tab (B360):** valid through 19 May but **B360 tab is now a frozen Packup snapshot** — every SKU shows latest_stock == first_stock, deductions all 0. Not a usable live signal.
- **Shopify data:** latest 18 May (1-day lag per standard).
- **ShipHero (Fulfillable):** queried 19 May. **One warehouse only** (id `OjEyODM4NQ==` / Fulfillable). Confirmed Available reconciles to POS MODEL within 1-5 units across all 4 sampled SKUs (KIT-STA-2, ACC-LAB-UK, LIQ-HEA-5, ACC-REM). Sheet is reliable as stock position source.
- **Growth factor:** 1.3x (base 84/d → scaled 109.2/d kits).
- **Kit DSR base in POS MODEL:** STA 10 + COM 32 + ULT 42 = 84/d. **Note:** the POS MODEL kit DSRs do NOT reflect the recent offer-attach surge into COM — when the model rebases, KIT-COM-4 DSR will move from 32 to ~60-73, KIT-STA-2 down from 10 to ~5.

### Manual overrides applied

- **UK 03062026 balance: PAID** (sheet shows "In Production"; user 19 May confirmed paid, shipping consolidated with UK 02072026 as single 40HQ).
- **UK 03062026 + UK 02072026 = single 40HQ.** Sheet shows two separate shipment blocks but they sail together. Arrival 15 Jul shared.
- **UK Powder Room landed 13-14 May but NOT YET checked into ShipHero.** Affects 17+ colour SKUs that physically have stock but show 0 Available. The 47-SKU "colours-14d-zero" list overstates the OOS picture.
- **B360 Packup stock-out: deposit PAID 14 May, but stock-out balance itself still owed** (user 19 May; Remy following up in inventory channel). Treat Packup units as not yet recoverable.
- **UK 02082026 fill PO place date: now ~26 May** (user 19 May; sheet implies 13 May which has passed).
- **KIT-STA-2 substitution: live and passive** — Shopify flow auto-routes to KIT-COM-4 when STA depletes (user 19 May; not a pending decision).
- **Vik (Chemence): Remy emailed today 19 May** chasing completion date for PO 22-04-2026 (sheet ETA 17 Jun — unconfirmed by Chemence).

---

## STOCK POSITION

Cover shown at **projected** (model DSR × growth factor) and **actual** (Shopify-derived; 7d for current pace, 30d for stable baseline). All standalone numbers below; kit-adjusted liquids appear in the next section.

### Kits (Shopify DSR)

| SKU | Stock | Proj DSR | Cov @ Proj | Actual 7d | Cov @ 7d | Actual 30d | Cov @ 30d |
|---|---|---|---|---|---|---|---|
| KIT-STA-2 | 60 | 13.0 | 5d | 5.1 | 12d | 8.9 | 7d |
| KIT-COM-4 | 3,119 | 41.6 | 75d | 73.1 | **43d** | 40.1 | 78d |
| KIT-ULT-6 | 3,321 | 54.6 | 61d | 39.6 | 84d | 35.0 | 95d |
| **All kits** | **6,500** | **109.2** | **60d** | **117.8 (+8% vs proj)** | **55d** | **84.0** | **77d** |

**Headline:** kit demand has fully recovered. 7d Shopify (117.8/d) is 8% above the scaled target (109.2/d). Week 20 (11-17 May) daily rate 108.7/d; week 21 single-day spot reading 137/d on 18 May. The W17 floor at 63/d is no longer the story.

**Mix shift to flag:** COM and ULT have absorbed STA's allocation. Last review's model assumed STA 30/d, COM 41/d, ULT 38/d. Today's 7d: STA 5/d (-83%), COM 73/d (+78%), ULT 40/d (+5%). Greg's POS MODEL kit DSRs need rebasing once the post-substitution rates stabilise.

### Kit-Adjusted Liquids (consumed +1 per kit at Fulfillable)

Kit consumption rate to use: 117.8/d (7d Shopify kit total).

| SKU | Stock | Standalone 7d | Kit consumption | Combined DSR | Cov @ Combined | Model says |
|---|---|---|---|---|---|---|
| LIQ-HEA-5 | 6,099 | 1.4 | 117.8 | 119.2 | 51d | 55d @ 110.5 |
| LIQ-BAS-2 | 4,959 | 16.9 | 117.8 | 134.7 | 37d | 37d @ 135.2 |
| LIQ-GLO-4 | 6,290 | 9.3 | 117.8 | 127.1 | 49d | 51d @ 122.2 |
| ACC-INS | 7,473 | — | 117.8 | 117.8 | 63d | 70d @ 106.6 |

**Greg has updated Base/Glow DSRs** since last review — POS MODEL Base 135.2 matches actual 134.7, Glow 122.2 within 4% of actual 127.1. Last review's flagged "POS MODEL DSR understated for Base/Glow" is now closed. (Heal model 110.5 vs actual 119.2: model slightly low but acceptable.)

### Remove products (combined Shopify rate per [[uk-remove-bundle-upsell]])

The before-cart bundle upsell consolidates demand into ACC-REM-BUN-1 (Remove 120ml + Bowl). Model on combined rate:

| SKU | Stock | Standalone 7d | Bundle 7d (BUN-1 / BUN-2) | Total demand | Cover | Model says |
|---|---|---|---|---|---|---|
| ACC-REM (120ml) | 843 | 6.3 | 68.4 (BUN-1) | **74.7/d** | **11d** 🔴 | 22d @ 39.0 |
| ACC-REM-500 | 4,132 | 5.3 | 12.4 (BUN-2) | 17.7/d | 233d | 114d @ 36.4 |
| ACC-REM-BOW | 4,120 | 0.4 | 68.4 + 12.4 = 80.8 | 81.2/d | 51d | 132d @ 31.2 |

**ACC-REM (120ml) is the critical Remove SKU** — 11d cover at combined rate. Liquipak final 800L fill is sitting awaiting payment (user 19 May). Once paid: ~4,000 ACC-REM units land, refreshes to ~55d cover.

**Model heavily overstates Remove-Bowl and Remove-500ml cover** because Greg's model DSRs don't account for the bundle split — bowls and 500ml are both bundled with 120ml, so much heavier demand than the model thinks. Greg refresh outstanding for ACC-REM-BOW (60/d model → ~80/d actual) and ACC-REM-500 (model overstated by ~50% vs actual).

### Inserts / packaging (deduct on every order)

ACC-LAB and ACC-THA deduct 1 per ORDER (not per item). With Fulfillable shipping ~217 orders/day (POS MODEL DSR, derived from order count not unit count), expected daily deduction matches.

| SKU | Stock | Model DSR | Cov @ Model | Notes |
|---|---|---|---|---|
| ACC-LAB-UK | 4,030 | 217.1 | **18d** 🔴 | Print Runner PO drafted 14 May (10k units), Joel pending payment. PR lead 14-21d. |
| ACC-THA | 21,259 | 217.1 | 98d | Safe. Future containers bring more. |
| ACC-INS | 7,473 | 106.6 (model) / 117.8 (actual) | 63d | Kit-adjusted; safe. |
| STO-BUB-BAG-L | 10,280 | 106.6 | 96d | Per-kit deduction. Safe. |
| STO-BUB-BAG-S | 0 | 0 | n/a | **No longer our supply** — Fulfillable provides these (user 19 May). Remove from GLAMRDiP monitoring. |
| STO-MAI-BAG-S | 9,673 | 110.5 | 88d | Safe. |
| STO-MAI-2 | 7,351 | 110.5 | 67d | Safe. |

### Colours

**47 colour SKUs registered 0 sales in last 14 days** (Shopify). Caveat: 12-17 of these are Powder Room collection sitting physically at Fulfillable but not booked into ShipHero yet — they aren't really OOS, just blocked at warehouse. Per the 12 May summary count, 17 colours OOS due to B360 Packup lock + UK 03062026 delay.

Once Fulfillable books in Powder Room (Roisin chasing) AND B360 stock-out balance is paid, the OOS list shrinks substantially.

---

## CHECK-IN PROGRESS

No active ShipHero PO CSVs provided. Powder Room is the only PO in flux (physically at Fulfillable since 13-14 May, ShipHero check-in pending). Visible from Slack: Daniel 18 May ASAP message — Fulfillable processing inbounds first-come/first-served per SLA; Roisin can't override. Joel mentioned marking Powder Room OOS in UK theme as interim measure — not done as of 19 May.

---

## DOUBLE-COUNT DETECTION

No live double-count risk identified. Powder Room is on POS MODEL with status `Completed` and est_arrival 14 May, but Available in ShipHero/B360 is 0 for the Powder Room SKUs since they're not booked in. Sheet doesn't list separate Express Shipment OL columns for partial check-in detection.

When Fulfillable books Powder Room in, expect ~12-17 colour SKUs to land at once. Watch for the OOS count to shrink.

---

## CONTAINER / ORDER STATUS

| Ref | POS MODEL status | Est. Completion | Est. Arrival | Reality |
|---|---|---|---|---|
| UK Powder Room AND Chemence | Completed | — | 14 May | Physically landed 13-14 May; not booked into ShipHero. Roisin chased today (Remy, 19 May 02:03 UTC). |
| 22-04-2026 Chemence (next fill) | Ordering | 17 Jun | — (next-day after completion via Woodview) | **Vik silent 20 days.** Remy emailed today asking completion date. Blocks: free-issue caps/brushes confirmation (Daniel sent tracker 29 Apr, no reply). |
| UK 03062026 | In Production | 21 May | 15 Jul | **Balance PAID** (user 19 May). Consolidating with UK 02072026 as single 40HQ. Brings 448 STA + 1,484 COM + 700 ULT + 5,600 ACC-THA + 432 SEA + 216 BON + 21,400 colours + 11,580 STO + 40,000 component empties. |
| UK 02072026 | In Production | 21 May | 15 Jul | Birthday Sale container. Brings 336 STA + 1,316 COM + 1,148 ULT + 5,600 ACC-THA + 1,680 ACC-INS + colours. Sally still requires jars. |
| UK 02082026 | (no status) | 13 Jul | 6 Sep | **PO place date now ~26 May** (user 19 May; was 13 May, slipped). Brings 560 STA + 1,148 COM + 840 ULT + 4,080 ACC-INS + 11,200 ACC-THA + colours. |
| (unnamed #6) | — | 12 Aug | 6 Oct | Placeholder. |
| (unnamed #7) | — | 13 Aug | 7 Oct | Placeholder. |
| B360 PACKUP STOCK | In Production | — | — | Sheet treats as inbound shipment. 288,898 units locked at B360. Release blocked on stock-out balance payment. |

**Stale POS MODEL dates flagged:**
- UK 03062026 status still "In Production" — should flip to "Shipping" once Sally confirms sailing.
- UK Powder Room status "Completed" with est_arrival 14 May — accurate at the sheet level, but it's not actually live until Fulfillable books it in.

---

## LOCAL FILL STATUS

| Fill | Status | Notes |
|---|---|---|
| 22-04-2026 Chemence (BAS 8k + GLO 6k) | Ordering | Blocked on Vik. Remy chased today 19 May. Sheet completion 17 Jun unconfirmed. |
| Final Liquipak 02-04-2026 (Remove 120ml + 500ml) | Ready for despatch | **Goods are made; awaiting GLAMRDiP payment** (user 19 May). Approx 4,000 ACC-REM + 4,000 ACC-REM-500 from the 800L pre-mix. Liquipak then exits permanently — no replacement filler identified (9 weeks stalled). |
| Oils4Life Heal | No active PO | Dale silent 21d+; Remy outbound chase still pending. Heal at 51d combined cover today — still healthy but plan window narrowing. |
| Print Runner ACC-LAB-UK | Drafted not placed | Recommended PO (10k) sent to Joel 14 May. Lead 14-21d. **Joel to pay** to release. |

---

## STOCK-OUT FORECAST

### Stocks out BEFORE next inbound (forecasted DSR primary; 7d surge in parentheses as watch signal)

| SKU | Stock | Forecast DSR | Stocks Out @ forecast | Next Inbound | Arrives | Gap |
|---|---|---|---|---|---|---|
| ACC-REM (120ml combined) | 843 | 38.3 (30d combined) | ~26 Jun | Liquipak final fill | 7d post-pay | comfortable if pay by 19 Jun. At 7d surge 74.7/d: stocks out 30 May → **pay by 22 May**. |
| ACC-LAB-UK | 4,030 | 217.1 (model) | ~6 Jun | Print Runner 10k | 14-21d post-pay | **0-7d gap** if Joel pays today; wider if delayed |
| KIT-STA-2 | 60 | 13.0 (model) | ~24 May | UK 03062026/02072026 | 15 Jul | -52d → substitution covers (Shopify flow auto-routes to KIT-COM-4 when STA depletes) |
| KIT-COM-4 | 3,119 | 41.6 (model) | ~6 Aug | UK 03062026/02072026 (+2,800 COM) | 15 Jul | comfortable at forecast. ⚠️ Actual 7d 73/d is 76% over forecast — **watch only, not actioning sizing per user 19 May** |

### Nothing on order

| SKU | Cover | Notes |
|---|---|---|
| LIQ-HEA-5 | 51d (12 Jul) | No CN container brings Heal. Local fill needed by ~25 Jun (Oils4Life lead unknown). |
| Liquipak Remove 120ml long-term | 60d post-fill (~end Jul) | No replacement filler. Decision overdue. |

### Safe

ULT (84d), LIQ-BAS-2 (37d, Chemence 22-04 arriving), LIQ-GLO-4 (49d, Chemence 22-04 arriving), LIQ-SEA-3 (184d Shopify or 170d model), all packaging except STO-BUB-BAG-S (B360-locked, may need transfer).

---

## CASCADING ARRIVAL PROJECTION

Stage 0 = now (19 May). Stage 1 = after Chemence 22-04 fill arrives (assume 22 Jun if Vik confirms completion 17 Jun + 1d Woodview transit). Stage 2 = after UK 03062026/02072026 land (15 Jul). Stage 3 = after UK 02082026 lands (6 Sep).

Kit rate used: 109.2/d forecasted (84/d base × 1.3x). Per user 19 May, use forecasted DSR for planning; flag actual > forecast as a watch signal only.

Per-kit DSR at forecast: STA 13.0, COM 41.6, ULT 54.6.

| SKU | Now | After 22-04 (~22 Jun) | After 03062026+02072026 (15 Jul) | After 02082026 (6 Sep) |
|---|---|---|---|---|
| KIT-STA-2 | 60 / 5d | 60-13×34 = -382 → OOS, substituting to COM | -382-13×23+784 = 103 / 8d | 103-13×53+560 = -26 → OOS gap |
| KIT-COM-4 | 3,119 / 75d | 3,119-41.6×34 = 1,705 / 41d | 1,705-41.6×23+2,800 = 3,548 / 85d | 3,548-41.6×53+1,148 = 2,491 / 60d |
| KIT-ULT-6 | 3,321 / 61d | 3,321-54.6×34 = 1,465 / 27d | 1,465-54.6×23+1,848 = 2,057 / 38d | 2,057-54.6×53+840 = 1 / 0d 🔴 |
| LIQ-HEA-5 (forecast 110.5) | 6,099 / 55d | 6,099-110.5×34 = 2,342 | 2,342-110.5×23+0 = -200 → OOS gap | needs Oils4Life fills before |
| LIQ-BAS-2 (forecast 135.2) | 4,959 / 37d | 4,959-135.2×34+8,000 = 8,362 / 62d | 8,362-135.2×23+432 = 5,684 / 42d | 5,684-135.2×53 = -1,482 → OOS gap |
| LIQ-GLO-4 (forecast 122.2) | 6,290 / 51d | 6,290-122.2×34+6,000 = 8,135 / 67d | 8,135-122.2×23 = 5,324 / 44d | 5,324-122.2×53 = -1,153 → OOS gap |
| ACC-REM (combined forecast 38.3) | 843 / 22d | needs Liquipak final fill | post-Liquipak ~4,000 added | ~120d cover after fill |
| ACC-LAB-UK | 4,030 / 18d | needs Print Runner PO placed | Print Runner brings ~10,000 | next PR PO needed mid-Jul |

### Critical gaps to surface (at forecasted DSR)

1. **KIT-ULT-6 OOS ~25 Aug-6 Sep gap (~12 days)** at forecast 54.6/d. Stock at 02082026 arrival projects to ~0. Needs more ULT on 02082026 or an interim bridge.
2. **LIQ-HEA-5 OOS ~14 Jul** if no Oils4Life fill placed. Heal is in every kit. Outbound Dale today.
3. **LIQ-BAS-2 OOS late Aug** post-15 Jul container at forecast rate. Chemence next-next fill needs scheduling immediately after 22-04 lands.
4. **LIQ-GLO-4 OOS late Aug** same dynamic as BAS.

⚠️ **Watch flag (not actioning per user 19 May):** Actual 7d kit total 117.8/d exceeds forecast 109.2/d by 8%; KIT-COM-4 7d is 73/d (76% over forecast 41.6/d). If the surge holds, KIT-COM-4 stocks out earlier (~1 Jul vs forecast 6 Aug) and the 15 Jul arrival becomes tight. **Re-test in 2 weeks once more post-substitution data lands.**

### If Vik silence continues past 17 Jun

LIQ-BAS-2 stocks out ~6 Jul at 134.7/d combined (4,959/134.7 = 37d from today). UK 03062026 brings only 0 BAS (correction: 03062026 brings 432 BAS for Sweden transhipment, NOT for UK fulfilment). So Vik fill IS the next BAS replenishment. Each week Vik slips = 1 week closer to BAS OOS.

### Overstock flags (post-arrival > 100d cover)

- KIT-STA-2 post-02082026: 165d (vs target 45-75d). Excess driven by substitution model — STA demand has structurally collapsed. Consider future containers carrying less STA, more COM.
- KIT-ULT-6: stays roughly in range.

---

## PACKAGING & INSERTS — INTEGRITY NOTE

B360 tab is frozen Packup (not live deductions). The ShipHero MCP integration (first attempt this cycle) confirmed Fulfillable's live picture matches POS MODEL Available within 1-5 units across sampled SKUs.

**ShipHero deduction extraction — first-cycle learnings:**
- `inventory_changes` query works but is capped at 500 edges per SKU per request (no obvious cursor pagination through the response shape used today).
- For high-volume SKUs (KIT-COM-4, ACC-LAB-UK, ACC-THA, LIQ-HEA-5), 500 edges = only the oldest 2-7 days. Latest days are truncated.
- Daily breakouts sampled (where complete): KIT-COM-4 ranged 22-82/d (peak 14 May = 82); KIT-ULT-6 daily ~30-50; ACC-REM 1-19/d.
- 14 May 82 KIT-COM-4 deductions = anomaly day worth flagging — verify against Shopify.
- **Carry forward to next cycle:** implement cursor pagination on `inventory_changes` to get full 14d window for high-volume SKUs.

For this cycle, fall back to Shopify DSR + model DSR as primary rates. Defer "Shopify vs 3PL deduction" integrity testing until pagination is fixed.

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (act today)

1. **Joel: pay Liquipak balance** to release final 800L Remove fill. Goods are ready to ship (~7d transit). At forecast 38.3/d combined, latest pay date = **19 Jun** (stocks out 26 Jun, less 7d transit). At current 7d surge 74.7/d, latest pay date = **22 May**. **Recommend pay this week** to avoid the surge-risk.
2. **Joel: pay B360 stock-out balance.** Deposit (14 May) only covered deposit. Stock-out itself unfunded. 17 OOS colours locked + STO-BUB-BAG-S 19,445 + 5,246 ACC-THA + 7,349 ACC-INS + 493 STA etc. Remy following up in inventory channel.
3. **Joel: pay Print Runner ACC-LAB-UK** (14-05-2026 PO). 10k units. Lead 14-21d. Current cover 18d at 217/d.
4. **Remy: reply to Seby on Bill 618199 invoice audit** (Asana due today).
5. **Remy: chase Roisin for Powder Room book-in ETA + Sweden re-ship MO122 quote** (chased 19 May; both still outstanding).

### 🟡 WARNING (act this week)

6. **Remy: outbound Dale (Oils4Life)** for next Heal fill timing. 21d+ silent. Heal at 51d cover combined — fill window narrowing.
7. **Daniel: place UK 02082026 fill PO** by 26 May (per user 19 May). Consider sizing COM up given the surge (currently 1,148 COM; rate suggests 2,000+).
8. **Daniel: Liquipak replacement decision** (Path A/B/C). 9 weeks stalled.
9. **Joel: mark Powder Room collection OOS** on UK theme until Fulfillable books in — committed 14 May, not done.
10. **Daniel + Remy: free-gift transition plan** (current → Remove 500ml) — surfaced 12 May, no follow-up plan.

### 🟢 MONITOR (FYI)

11. **KIT-COM-4 likely OOS gap ~1 Jul → 15 Jul** at current 73/d 7d rate. No bridge available — accept and CX-plan.
12. **STO-BUB-BAG-S** — Fulfillable supplies these directly (user 19 May). No GLAMRDiP action needed; drop from monitoring.
13. **Greg POS MODEL refresh** post-Sally consolidation acknowledgement and post-Powder Room book-in. Also kit DSR rebase once 4 weeks of post-substitution data accumulate.
14. **POS MODEL UPDATED cell empty** — Greg to fix the timestamp paste discipline.

---

## PO RECOMMENDATIONS

Target: maintain 14-21d kit cover (lean).

| SKU / Item | Current | Inbound | Recommended action | Place by |
|---|---|---|---|---|
| ACC-LAB-UK | 4,030 / 18d | Print Runner 10k PO drafted (Joel pending pay) | Pay now; lead 14-21d | TODAY |
| ACC-REM (120ml) | 843 / 22d @ forecast 38.3 | Liquipak final ~4k (paid trigger; 7d transit) | Pay by 19 Jun @ forecast; **by 22 May if surge holds** — recommend this week | 22 May (safe) |
| LIQ-HEA-5 | 6,099 / 51d | None | Outbound Dale for next Oils4Life fill | This week |
| LIQ-BAS-2 | 4,959 / 37d | Chemence 22-04 +8,000 (~22 Jun) | Confirm Vik completion | Already in flight |
| LIQ-GLO-4 | 6,290 / 49d | Chemence 22-04 +6,000 (~22 Jun) | Confirm Vik completion | Already in flight |
| UK 02082026 fill PO | — | — | Place — consider COM up to 2,000-2,500 from 1,148 | 26 May (slipped target per user) |
| Liquipak replacement | — | None | Decide Path A/B/C | This week (decision) |
| ACC-THA | 21,259 / 98d | 11,200 on 02082026 + 5,600 each on 03062026/02072026 | None | OK |
| Future ACC-LAB-UK | — | After current 10k lands | Plan top-up by ~mid-Jul | Mid-Jun |

---

## FOLLOW-UP ITEMS

### Immediate (today / Wed)
- [ ] Joel: pay Liquipak balance
- [ ] Joel: pay B360 stock-out balance
- [ ] Joel: pay Print Runner labels PO
- [ ] Remy: reply to Seby on invoice audit
- [ ] Remy: chase Roisin Powder Room book-in
- [ ] Joel: mark Powder Room OOS on UK theme

### By end of week
- [ ] Remy: outbound Dale (Oils4Life)
- [ ] Daniel: UK 02082026 PO place (26 May), with COM upsize
- [ ] Daniel: Liquipak replacement Path decision
- [ ] Vik: completion date + free-issue (waiting on Remy's 19 May email reply)
- [ ] Daniel + Remy: free-gift transition plan

### Ongoing
- [ ] ShipHero deduction extraction: implement cursor pagination for next cycle
- [ ] Greg: POS MODEL kit DSR rebase once 4 weeks of post-substitution data
- [ ] Greg: refresh ACC-REM-BOW and ACC-REM-500 model DSRs (bundle-aware)
- [ ] Greg: fix UPDATED cell paste discipline
