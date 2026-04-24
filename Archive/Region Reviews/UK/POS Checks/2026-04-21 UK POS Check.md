# POS MODEL CHECK — UK — 21 Apr 2026

## DATA FRESHNESS

- POS MODEL last updated: **21 Apr 2026** (user-confirmed; H8 cell agrees)
- Fulfillable stock source: **PASTE tab** (today's paste) → flows through to POS MODEL ON HAND column (labelled `FULFILLABLE`)
- B360 tab: stale post-13 Apr transition. Don't use for any Fulfillable cover calc
- Shopify sales data through: **20 Apr 2026** (1-day lag)
- **Growth factor: 1.3x** (bumped from 1.1x seen on 14 Apr). Base 84/d → scaled 109.2/d at 1.3x
- Kit DSRs on sheet: STA 10 / COM 32 / ULT 42

## MANUAL OVERRIDES

| Item | Sheet says | Override | Source |
|---|---|---|---|
| UK 03062026 Est. Arrival | 14 Jun (sheet) | **Slipping — balance unpaid, container not shipped** | User-confirmed 21 Apr |
| B360 Packup transfer | "In Production" | **No transfer yet; 1–2 weeks out** | User-confirmed 21 Apr. 288,898 units still at B360 |
| UK Powder Room (local fill) | n/a | **Ready to ship, on track** | User-confirmed 21 Apr |

UK 03062026 was previously expected to ship and arrive ~14 Jun. Balance hasn't been paid. Real arrival will be later than 14 Jun — **flag downstream calcs as "at risk"**.

---

## KIT-ADJUSTED DSR VALIDATION

UK kit-adjusted items (Fulfillable picks per kit automation rules, confirmed 13 Apr): **LIQ-HEA-5, LIQ-BAS-2, LIQ-GLO-4, ACC-INS**. Per-order: ACC-LAB-UK, ACC-THA.

| SKU | Model DSR (on sheet) | Kit-adjusted actual (14d) | Verdict |
|---|---:|---:|---|
| LIQ-HEA-5 | ~88/d implied | standalone 1.0 + kit 87.3 = **88.3** | Model aligned ✓ |
| LIQ-BAS-2 | **135.2** (= 833/6.16d) | standalone 14.6 + kit 87.3 = **101.9** | Model now includes kit consumption ✓ (was 22/d on 14 Apr — Greg updated) |
| LIQ-GLO-4 | **122.2** (= 959/7.85d) | standalone 7.0 + kit 87.3 = **94.3** | Model updated ✓ |
| ACC-INS | ~87/d implied | 87.3 (per-kit) | Aligned |
| ACC-LAB-UK | 217.1 | Needs per-order actual — Shopify doesn't sell it; 3PL data stale | Use model as planning rate |
| ACC-THA | Similar to LAB | Same | Use model |

Greg has refreshed the UK POS MODEL DSR for Base and Glow to reflect Fulfillable's kit-picking setup. Good.

---

## GROWTH FACTOR HEALTH CHECK

| | Value |
|---|---:|
| Model growth factor | **1.3x** (bumped from 1.1x on 14 Apr) → 109.2/d |
| Actual 14d kit DSR | **87.3/d = 0.80x** of base 84 |
| Actual 30d kit DSR | 86.2/d = 0.77x |
| Gap to model | **-20% (14d)** |

**Reading:** UK's actual kit rate hasn't materially changed (87/d today vs 90/d on 14 Apr). What shifted is the aspirational target — 1.3x projects 109.2/d which is ~25% above current run rate.

Context-in-progress: if 1.3x is now the planning bar for UK alongside AUS, future container sizing should be reviewed. At the prior 1.1x target (92.4/d) we were 94% to target — healthy. At 1.3x we're 80% — manageable but requires the marketing plan to deliver on the lift.

---

## STOCK POSITION

Source: Fulfillable PASTE (21 Apr). Two covers per SKU — **Projected** (POS MODEL DSR × 1.3x) and **Actual** (Shopify 14d kit-adjusted for kit-consumed SKUs; standalone otherwise; 3PL rate for per-order SKUs).

### Kits
| SKU | Stock | Projected DSR | Cover @ Projected | Actual DSR | Cover @ Actual |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 300 | 13.0 | 23d | 14.0 | **21d** |
| KIT-COM-4 | 4,306 | 41.6 | 104d | 26.7 | 161d |
| KIT-ULT-6 | 4,299 | 54.6 | 79d | 46.6 | 92d |

### Liquids (kit-adjusted where consumed per kit)
| SKU | Stock | Projected DSR | Cover @ Projected | Actual DSR | Cover @ Actual | Note |
|---|---:|---:|---:|---:|---:|---|
| LIQ-HEA-5 (Heal) | 9,035 | 88.3 | 102d | 88.3 | 102d | Aligned |
| LIQ-BAS-2 (Base) | **833** | 135.2 | **6d** | 101.9 | **8d** | CRITICAL |
| LIQ-GLO-4 (Glow) | **959** | 122.2 | **8d** | 94.3 | **10d** | CRITICAL |
| LIQ-SEN-2 (LO Base) | **0** | 0 (no kit use) | — | 0.0 standalone | OOS | not on any container |
| LIQ-SEN-4 (LO Glow) | **0** | 0 | — | 0.0 | OOS | not on any container |
| LIQ-SEA-3 (Seal) | 3,036 | ~22 | 138d | 9.4 | 323d | Safe |
| LIQ-BON-1 (Bond) | 609 | ~11 | 55d | 2.9 | 210d | Safe |

### Remove products (standalone — not kit-adjusted)
| SKU | Stock | Projected DSR | Cover @ Projected | Actual DSR (Shop) | Cover @ Actual |
|---|---:|---:|---:|---:|---:|
| ACC-REM (120ml) | 1,978 | ~28 | 71d | 19.0 | 104d |
| ACC-REM-500 | 4,685 | ~14 | 335d | 13.2 | 355d |
| ACC-REM-BOW | 5,395 | ~4 | 1349d | 2.8 | 1927d |

### Inserts / packaging (per-order; Shopify doesn't sell — use model/3PL rate)
| SKU | Stock | Projected DSR | Cover @ Projected | Note |
|---|---:|---:|---:|---|
| ACC-LAB-UK | 8,361 | 217.1 | 39d | Locally printed; Print Runner 14–21d lead. Next PO needed ~end April |
| ACC-THA | 25,589 | 217.1 | 118d | Safe |
| ACC-INS | 9,850 | 109.2 | 90d | Safe |
| EMPTY-GLASS-BOT-INNER | 2,500 | 257.4 | 10d | Component SKU — goes to Chemence for refills, not a retail stockout |

---

## CONTAINER / ORDER STATUS

### UK Powder Room + Chemence (combined shipment arriving 30 Apr)
- Contents: **8,000 LIQ-BAS-2** + **8,000 LIQ-GLO-4** (Chemence fill) + Powder Room jars (user-confirmed ready to ship)
- Status on sheet: **Completed** (Est. Arrival 30 Apr)
- Payment: Chemence balance due 27 Apr (Joel to action)
- Daniel's 20 Apr note: consider splitting Base/Glow from this fill to Nordic to bridge their gap — **decision needed before 27 Apr**

### UK 03062026
- Sheet: On the Way, Est. Comp 20 Apr, Est. Arr 14 Jun
- **Reality per user 21 Apr: balance unpaid, container not shipped → arrival will slip.** Unknown new ETA
- Contents: 448 STA, 1,484 COM, 700 ULT, 216 Bond, 432 Seal, 5,600 ACC-THA, 10,000 empty glass bottle inners
- **Owner: Joel. Action: pay balance this week; confirm new Est. Completion + Arrival with Sally/Lily**

### UK 02072026 (Birthday Sale)
- Sheet: In Production, Est. Comp 18 May, Est. Arr 12 Jul
- Deposit paid ✅
- Contents: 336 STA, 1,316 COM, 1,148 ULT, 1,080 Seal, 216 Bond, 1,680 ACC-INS, 5,600 ACC-THA, 60,000 empty bottle inners

### UK 02082026 (fill PO place date 29 Apr — 8 days away)
- Sheet: Est. Comp 22 Jun, Est. Arr 16 Aug
- Contents: 560 STA, 1,148 COM, 840 ULT, 864 Seal, 432 Bond, 4,080 ACC-INS, 11,200 ACC-THA, 20,000 empty bottle inners
- **Gaps:** 0 ACC-LAB-UK, 0 ACC-REM-BOW, 0 LIQ-SEN-2, 0 LIQ-SEN-4. ACC-LAB-UK is locally printed so expected. Sensitive lines have been OOS and need a separate order.

### B360 Packup (holding pen — no transfer yet)
- Status: "In Production" on sheet. User-confirmed 1–2 weeks out.
- **Critical SKUs waiting to move:** KIT-STA-2 **493** units (1.6× current Fulfillable stock); LIQ-HEA-5 1,653; LIQ-GLO-4 596; ACC-INS 7,349; ACC-LAB-UK 1,396; ACC-THA 5,246; KIT-COM-4 40; ACC-REM 43; LIQ-SEA-3 369; LIQ-BON-1 194; EMPTY-GLASS-BOT-INNER 20,864
- **Not there:** LIQ-BAS-2 32 (trivial); no Sensitive Base/Glow

---

## LOCAL FILL STATUS

### Chemence (Base + Glow)
- **10-03-2026 fill: 8,000 Base + 8,000 Glow** — on track for 28 Apr dispatch, 27 Apr payment, arrival Fulfillable ~30 Apr
- **Daniel's 22 Apr action**: re-issue with Nordic split
- **Next Chemence order** (Viktorija 13 Apr): 6–8 week lead time for new 8k order. Daniel placing "over coming days" — status unclear.

### Oils4Life (Heal)
- Last PO 25-02-2026 dispatched to Fulfillable. Heal stock 9,035 / 88.3/d kit-adj = 102d cover. Not urgent.

### Liquipak (Remove 120ml/500ml) — EXITING
- Final PO (02-04-2026) placed, payment sent 9 Apr. ~160d coverage post-fill
- No replacement filler found. Stock-out scenario ~early Sep if no replacement

### Print Runner (ACC-LAB-UK)
- Last PO 10-03-2026. Current stock 8,361 / 217/d = 39d → stocks out ~29 May
- Next Print Runner PO needed ~early May (14–21d lead). **Flag for Remy**

---

## STOCK-OUT FORECAST — by container window

### Window 1: now → UK Powder Room + Chemence (30 Apr, 9 days away)

**CRITICAL — stock-out this window:**

| SKU | Stock | Actual DSR | Stocks out | Bridge |
|---|---:|---:|---|---|
| LIQ-BAS-2 | 833 | 101.9 | **29 Apr (-1d)** | Chemence 28 Apr dispatch. **0–1d margin if on time.** If Nordic split reduces UK's portion, recompute. |
| LIQ-GLO-4 | 959 | 94.3 | 1 May (+1d) | Chemence same shipment. Same margin. |
| LIQ-SEN-2 | 0 | 0 std | **OOS now** | No inbound. Place order or flag OOS on site |
| LIQ-SEN-4 | 0 | 0 std | **OOS now** | No inbound. Place order or flag OOS on site |

**If Nordic takes 2,000 each:** UK gets 6,000 Base + 6,000 Glow → post-fill 6,833 / 101.9 = 67d Base; 6,959 / 94.3 = 74d Glow. Still fine through to Chemence-next fill (6–8 week lead).

**If Nordic takes 4,000 each:** UK gets 4,000 each → post-fill 4,833 / 101.9 = 47d Base; 4,959 / 94.3 = 53d Glow. Tighter but feasible.

**Recommendation on split:** up to 2,000 each to Nordic is comfortable. More than that starts compressing UK's cover to under 50d, which is marginal given 6–8 week Chemence lead times.

### Window 2: 30 Apr → UK 03062026 (uncertain arrival — assume mid–late Jun at earliest)

This is now the biggest planning uncertainty. Balance unpaid → container not shipped. Sheet says 14 Jun arrival but that assumed normal shipping from a completed container. Realistic new arrival unclear.

**Assuming UK 03062026 arrives ~1 Jul (2-week slip) instead of 14 Jun:**

| SKU | Stock + Chemence | Actual DSR | Stocks out | UK 03062026 OL | Gap |
|---|---:|---:|---|---:|---:|
| KIT-STA-2 | 300 | 14.0 | 12 May | +448 | **~50d gap** before STA restocks |
| KIT-COM-4 | 4,306 | 26.7 | 11 Sep | +1,484 | Safe |
| KIT-ULT-6 | 4,299 | 46.6 | 22 Jul | +700 | Safe |
| LIQ-BAS-2 post-Chemence | ~6,833* | 101.9 | 6 Jul | 0 | Next arrival needed from NEXT Chemence order or UK 02082026 Aug |
| LIQ-GLO-4 post-Chemence | ~6,959* | 94.3 | 15 Jul | 0 | Same |

\* Assumes full 8k each to UK (no Nordic split) and no consumption during the 9-day wait.

**STA bridge options if UK 03062026 arrives 1 Jul+:**
1. B360 Packup transfer (493 STA units) — would extend by ~35d if it lands next 1–2 weeks as planned
2. Substitute with Complete Kits (pattern already established pre-transition)
3. Sally express STA via Lily

**Joel's call** likely sticks with packup + Complete substitution. Confirm packup transfer tracking with Mason/Chris this week.

### Window 3: UK 03062026 → UK 02072026 (Birthday Sale, 12 Jul)

Assuming 03062026 lands ~1 Jul, gap to 02072026 is ~11 days. Short window, nothing to flag.

### Window 4: 02072026 → UK 02082026 (16 Aug)

Gap ~35 days. Need to verify ACC-LAB-UK is placed locally via Print Runner for this window — no container inbound for it.

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (act today / this week)
- **Joel: pay Chemence balance by 27 Apr** — 8,000 Base + 8,000 Glow dispatch 28 Apr. 0–1d margin. Non-negotiable deadline.
- **Joel: pay UK 03062026 balance** — every day of slip adds to the STA/Base/Glow gap after Chemence. Already 13 days open.
- **Daniel / Remy: confirm Nordic Chemence split before 27 Apr** — size at up to 2,000 each to keep UK ≥67d post-fill.
- **LIQ-SEN-2 / SEN-4 — OOS on Fulfillable, 0 on any container.** Place emergency order or pull listings.

### 🟡 WARNING (act this week)
- **Print Runner ACC-LAB-UK PO** — 39d cover, next order needs ~early May placement (14–21d lead). Size for 15,000 to cover through Aug.
- **Starter Kit bridge plan** — 300 stock + 493 B360 packup pending + 448 UK 03062026 (delayed). Confirm packup transfer to Fulfillable in next 1–2 weeks; otherwise STA gap widens materially. Complete Kit substitution should be prepared either way.
- **UK 02082026 kit-mix review** (Daniel, by 29 Apr fill PO place date) — at 0.80x kit rate vs 1.3x projection, container OL may be over-sized. Include Sensitive Base + Sensitive Glow to resolve OOS.
- **Empty Glass Bottle Inners** — 2,500 on hand, 10d at model rate. These are Chemence components. Confirm whether in-flight or on next container.

### 🟢 MONITOR
- 45+ colour backorders on Fulfillable from B360 non-transfers — will resolve as packup moves (1–2 weeks per user)
- Heal fill: 102d cover, next Oils4Life fill not urgent — place ~end May for ~July delivery
- Liquipak coverage: ~160d from 2 Apr final PO → stocks out ~early Sep. Replacement still needed

---

## LOCAL FILL FORECAST

### Chemence Base + Glow (in-flight)
- **Current fill:** 8,000 Base + 8,000 Glow dispatching 28 Apr (payment 27 Apr)
- Post-fill Base (UK only, no split): 6,833 + (consumption 0d) = 6,833 → **67d cover**
- Post-fill Glow: 6,959 → **74d cover**
- **Next fill place by:** ~12 May if 6–8 week lead and target ≥ Chemence pipeline cycle. Daniel already said "placing over coming days" 14 Apr — verify status.

### Oils4Life Heal
- Stock 9,035 / 88.3/d = 102d cover. Place next PO ~end May for ~1 Jul delivery.

### Print Runner ACC-LAB-UK
- Stock 8,361 / 217.1/d = 39d → runs out ~29 May. Place PO early May, target 15,000 units.

### Liquipak (exiting)
- Final PO arrived (or arriving). ~160d cover of Remove. No replacement.

---

## PO RECOMMENDATIONS

| SKU / PO | Place by | Action |
|---|---|---|
| Chemence balance (8k Base + 8k Glow) | **27 Apr** | Joel — hard deadline |
| UK 03062026 balance | **This week** | Joel — unpaid, blocks ship |
| Nordic Chemence split decision | **26 Apr** | Daniel — size cut before payment lodged |
| LIQ-SEN-2 / LIQ-SEN-4 — emergency | **This week** | Options: add to UK 02082026 container (8 days to fill PO deadline), place express CN, or pull listings |
| UK 02082026 Fill PO | **29 Apr** | Daniel — review quantities at 0.80x actual, add Sensitive Base/Glow, no ACC-LAB-UK needed |
| Next Chemence order (new 8k) | **~30 Apr** | Daniel — 6–8 week lead means this is the Jun/Jul Base + Glow backstop |
| Print Runner ACC-LAB-UK (15,000) | **~5 May** | Remy |
| Next Oils4Life Heal fill | **~25 May** | Remy |
| Liquipak replacement search | **Ongoing** | Daniel — 6+ weeks with no match |

---

## CASCADING ARRIVAL PROJECTION

Assumptions: Chemence 30 Apr arrives in full (no Nordic split applied here — use this as a "clean" baseline). UK 03062026 arrival pushed to **1 Jul** (2-week slip from sheet's 14 Jun, pending balance payment).

### Kits (at actual kit rate)

| SKU | Now | After Powder+Chemence (30 Apr) | After 03062026 (~1 Jul) | After 02072026 (12 Jul) | After 02082026 (16 Aug) |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 300 / 21d | 300 / 21d | -660 (STOCKOUT ~12 May) → +448 = ~0-140d* | +336 → ~140d + ~24d | +560 → ~180d ⚠️ |
| KIT-COM-4 | 4,306 / 161d | 4,306 / 161d | ~2,440 / 91d +1,484 = 144d ⚠️ | +1,316 = 160d ⚠️ | +1,148 = 170d ⚠️ |
| KIT-ULT-6 | 4,299 / 92d | 4,299 / 92d | ~1,107 / 24d +700 = 39d | +1,148 = 57d | +840 = 56d |

\* STA will stock out ~12 May unless B360 Packup (493 units) moves across, or Complete substitution kicks in, or Chemence+Powder Room arrival includes kit components (check).

### Liquids (kit-adjusted)

| SKU | Now | After 30 Apr | After ~1 Jul | After 12 Jul | After 16 Aug |
|---|---:|---:|---:|---:|---:|
| LIQ-BAS-2 | 833 / 8d | +8,000 → 8,833 / 87d | 2,085 / 20d, no inbound | no inbound → -943 (NEED next Chemence) | no inbound |
| LIQ-GLO-4 | 959 / 10d | +8,000 → 8,959 / 95d | 2,627 / 28d | no inbound → -700 (NEED next Chemence) | no inbound |
| LIQ-HEA-5 | 9,035 / 102d | 9,035 / 102d | 3,055 / 35d | 3,055 / 35d | 3,055 / 35d |

**The gap to watch:** after 30 Apr Chemence fill, there is NO Base/Glow on any CN container. **UK relies entirely on the next Chemence fill** (6–8 week lead from placement) to avoid a mid-July stockout. Daniel's "placing over coming days" quote from 14 Apr needs closing — is that order placed?

### Inserts / per-order

| SKU | Now | After 30 Apr | After ~1 Jul | After 12 Jul | After 16 Aug |
|---|---:|---:|---:|---:|---:|
| ACC-LAB-UK | 8,361 / 39d | 8,361 / 39d + Print Runner PO in window | Depends on PR PO | Depends | +0 |
| ACC-THA | 25,589 / 118d | same | +5,600 = 22,400 / 103d | +5,600 = 24,200 / 112d | +11,200 = 31,200 / 144d ⚠️ |
| ACC-INS | 9,850 / 90d | same | +0 = 2,060 / 19d 🔴 | +1,680 = 3,680 / 33d | +4,080 = 6,910 / 63d |

🔴 **ACC-INS gap**: at current rate 87/d and no inbound before UK 03062026, Instructions stock drops to ~2,060 by ~1 Jul. That's 19d cover. UK 02072026 adds 1,680 (22 Jul supplier lead, 12 Jul arrival). Tight. B360 packup has 7,349 ACC-INS — **packup transfer timing becomes material**: if packup lands in the next 2 weeks, this gap closes. If not, Instructions may stock out in late June.

### Delay scenarios

**If UK 03062026 slips to mid-Jul or later** (3+ week slip from sheet):
- KIT-STA-2 stockout extends from 12 May through to container arrival — Complete Kit substitution essential.
- LIQ-BAS-2 / LIQ-GLO-4 burn through post-Chemence buffer earlier — next Chemence fill must land by early Jul.
- ACC-INS: already tight at 14 Jun arrival, tighter still at mid-Jul. Packup or 02072026 must bridge.

**If B360 Packup does NOT transfer in 1–2 weeks** (user's working assumption):
- KIT-STA-2: lose 493 bridging units — stockout windows widens to full 50d before UK 03062026 arrival (or longer if unshipped)
- ACC-INS: lose 7,349 units — pushes stockout risk earlier into June
- ACC-LAB-UK: lose 1,396 — adds pressure on Print Runner PO timing

---

## FOLLOW-UP ITEMS

### Immediate (today–27 Apr)
- [ ] Joel: pay UK 03062026 balance + Chemence balance
- [ ] Daniel: confirm Nordic Chemence split size by 26 Apr
- [ ] Daniel: confirm next (new) 8k Chemence order placement status ("placing over coming days" from 14 Apr)
- [ ] Place emergency order or pull listings for LIQ-SEN-2 / LIQ-SEN-4 (both OOS)

### By end of month
- [ ] Daniel: UK 02082026 Fill PO revision by 29 Apr (kit-mix at 0.80x, add Sensitive Base + Glow)
- [ ] Remy: place Print Runner ACC-LAB-UK PO (~15,000) by 5 May
- [ ] Daniel / Joel: push B360 packup transfer (confirm stock-out deposit + work orders)
- [ ] Confirm Fulfillable stock-sync stable (pre-empt the name-corruption issue AUS had)

### Ongoing
- [ ] Monitor the 45+ Fulfillable colour backorders (resolve once packup moves)
- [ ] Liquipak replacement filler search — 6+ weeks, still none
