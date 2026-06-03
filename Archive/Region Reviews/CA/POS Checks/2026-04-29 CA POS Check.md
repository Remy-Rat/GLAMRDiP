# POS Model Check — CA — 29 Apr 2026

## Manual overrides (user-confirmed today)
- **CA 03022026 + CA 07042026 customs container — checked in at 247 and removed from POS MODEL.** Major arrivals visible 25 Apr (+31,606 units, 21 SKUs incl ACC-INS +10,034, KIT-COM-4 +4,767) and 26 Apr (+59,425 units, 90 SKUs incl ACC-THA +8,303). 9-week customs hold closed.
- **Growth factor — 1.5x** (sheet confirms; 80/d base × 1.5x = 120/d scaled).
- **CA 21062026 deposit — not paid.** PO sized at 1.5x DSR / 20GP, ready to place.
- **CA Powder Room (24-03-2026)** — in transit, ETA 30 Apr (likely tomorrow); not yet checked in.
- **Swift fill (31-01-2026)** — delivered 18 Apr (3PL shows +2,010 units), Heal + Remove 500ml back in stock.

## DATA FRESHNESS
- POS MODEL extracted 29 Apr 13:52 AEST (just-pulled).
- 3PL data last valid: **2026-04-29** (today).
- Container arrival days excluded from DSR calcs: 3 Apr, 18 Apr, 23 Apr, 25 Apr, 26 Apr.
- Growth factor: **1.5x** (80/d base → 120/d scaled).

---

## STOCK POSITION — KEY SKUs

Cover shown at projected DSR (model × 1.5x growth) AND actual DSR (3PL 14d deduction rate, excluding arrival days).

### Kits (post-customs check-in)

| SKU | Stock | Projected DSR | Cover @ Proj | Actual DSR | Cover @ Actual |
|---|---|---|---|---|---|
| KIT-STA-2 | 4,275 | 31.5/d | 136d | 13.0/d | **329d** |
| KIT-COM-4 | 8,231 | 61.5/d | 134d | 23.4/d | **352d** |
| KIT-ULT-6 | 3,372 | 27.0/d | 125d | 9.8/d | **344d** |

**Kits all sit at 125-136d at projected, 329-352d at actual.** Both rates exceed the 45-75d target. The customs container landed straight into a heavy overstock position — see Overstock flags below.

### Liquids

| SKU | Stock | Projected (kit-adj where applicable) | Cover @ Proj | Actual 3PL | Cover @ Actual | Note |
|---|---|---|---|---|---|---|
| LIQ-HEA-5 (Heal) | 8,541 | 120.6/d (kit-adj 1.5x) | 71d | 47.9/d | **178d** | kit-adj |
| LIQ-BAS-2 (Base) | 1,525 | scaled per Remy: ~218/d | "−7d"^ | 6.8/d | **224d** | NOT kit-adjusted at 247 |
| LIQ-GLO-4 (Glow) | 1,589 | scaled per Remy: ~530/d | "−3d"^ | 3.7/d | **429d** | NOT kit-adjusted at 247 |
| LIQ-SEA-3 (Seal) | 1,150 | — | — | 5.8/d | 198d |  |
| LIQ-BON-1 (Bond) | 1,053 | — | — | 2.3/d | 458d |  |
| LIQ-SEN-2 | 788 | — | — | 2.2/d | 358d |  |
| LIQ-SEN-4 | 642 | — | — | 2.4/d | 270d |  |

^ **The Base −7d / Glow −3d cover in today's CA Summary assumes Base/Glow are kit-adjusted (each kit consumes 1 Base + 1 Glow). 247 does NOT pick Base/Glow per kit — kits ship as pre-assembled units from Sally with the liquids inside the box.** 3PL deduction rate for Base (6.8/d) is aligned with Shopify standalone (5.8/d); same for Glow (3.7/d ded vs 2.9/d Shop). At standalone rate Base has 224d cover and Glow has 429d. **No express needed; the urgency in today's summary is a model-DSR artefact.**

### Remove products (driven by bundle SKUs)

| SKU | Stock | Shopify standalone | 3PL Ded (incl bundles) | Cover @ 3PL |
|---|---|---|---|---|
| ACC-REM (Remove 120ml) | 4,148 | 11.9/d | 20.3/d | 204d |
| ACC-REM-500 (Remove 500ml) | 3,457 | 8.4/d | 25.5/d | 136d |
| ACC-REM-BOW (Remove Bowl) | 5,722 | 2.1/d | 13.1/d | **437d** |

ACC-REM-BOW: 437d at actual; the Region file's flagged 80/d model DSR was wrong, **actual is 13.1/d** (already noted in 22 Apr POS Check; Greg correction outstanding).

Remove 500ml — Remy's today summary cites "actual 30/d vs projected 75/d (3 days post-restock)". 3PL 14d ded shows 25.5/d (matches). At 30/d: 115d cover. At 75/d projected: 46d cover. **Either rate, Remove 500ml is comfortably above the 28d local-fill lead-time. No imminent fill pressure.**

### Inserts / Packaging

| SKU | Stock | 3PL Ded/d | Cover | Benchmark | Status |
|---|---|---|---|---|---|
| ACC-INS | 23,479 | 42.8/d | 549d | 435 | OK |
| ACC-THA | 35,305 | 70.7/d | 499d | 735 | OK |
| ACC-LAB-CA | 8,487 | 0.0/d (recent) | — | — | model says 37d; deduction rule re-enabled but 14d activity flat — see anomalies |
| STO-MAI-BAG-S | 10,440 | 28.4/d | 368d | 330 | OK |
| STO-MAI-2 | 10,480 | 28.5/d | 368d | 330 | OK |
| STO-BUB-BAG-L | 9,420 | 43.9/d | 215d | 435 | OK |
| STO-BUB-BAG-S | 0 | 0.0 | — | — | EXCLUDE — 247 supplies (per Region config) |

### Anomaly deductions (>>benchmark, last 14d)

| Date | SKU | Deduction | Benchmark | Likely cause |
|---|---|---|---|---|
| 30 Mar | ACC-THA | 29,578 | 735 | check-in/restock event |
| 13 Apr | STO-MAI-2 | 11,077 | 330 | restock event |
| 15 Apr | STO-BUB-BAG-L | 10,053 | 435 | restock event |
| **19 Apr** | **POW-LAC-196 (Lace)** | **2,574** | **35** | **investigate — bulk pull or bundle?** |
| 24 Mar | POW-EMB-602 | 5,702 | 35 | likely correction/cycle count |
| 16 Mar | POW-HAR-139 | 2,577 | 35 | likely correction/cycle count |

**POW-LAC-196 (Lace)** — single 2,574-unit deduction on 19 Apr. Stock dropped to 2,546 today; if real demand, only 9d cover at the 287/d post-event rate. Almost certainly a bulk corruption — Shopify shows minimal Lace sales. **Flag for Greg / 247: was this a real sale event or a stock adjustment?** Cover is in question until clarified.

---

## OVERSTOCK FLAGS (post-customs check-in)

Target 45-75d cover. After the 25-26 Apr check-ins:

| SKU | Cover @ Actual | vs 75d target | Excess units |
|---|---|---|---|
| KIT-STA-2 | 329d | +254d | +3,300 units |
| KIT-COM-4 | 352d | +277d | +6,475 units |
| KIT-ULT-6 | 344d | +269d | +2,635 units |
| ACC-REM-BOW | 437d | +362d | +4,740 units |
| Multiple liquids (Base, Glow, Bond, Seal, Sen-2/4) | 200-450d | +125-375d | substantial |

**Implication:** CA 21062026 (Birthday Sale, 20GP, sized at 1.5x = 120/d kits) brings additional kits and liquids on top of this stack. At current actual demand (~46/d kits), the post-21062026 position will deepen overstock unless either (a) demand scales toward the 1.5x target, or (b) container quantities are trimmed before placement.

Per the Region file overstocking flag: at 0.66x actual demand, CA does not need another kit container until 2027. The 1.5x recalibration sized 21062026 for the upside, not the downside. **Worth a final sanity-check before Joel pays the deposit** — particularly on kit quantities.

---

## CONTAINER / ORDER STATUS

### CA 03022026 + CA 07042026 (combined)
- **Status:** ✅ DELIVERED & checked in (user-confirmed; 3PL shows mass arrivals 25-26 Apr).
- Removed from POS MODEL.
- 90 SKUs / +59,425 units on 26 Apr alone — confirms the 94,268 unit / 104 SKU manifest landed approximately as expected.
- **Outstanding:** Verify actual checked-in totals match manifest (any short-receipts in the next few days of 247 reconciliation).

### CA Powder Room (24-03-2026)
- POS MODEL: In Production (or in-transit slot).
- User-confirmed: in transit, ETA tomorrow 30 Apr.
- B113 jars confirmed.
- **Outstanding:** Confirm 247 check-in by Friday 1 May; flag short-receipts.

### CA 21062026 (Birthday Sale)
- POS MODEL: **Ordering**, Est. Completion **21 May**, Est. Arrival **5 Jul**.
- 1.5x DSR / 20GP / Daniel reconfigured 22 Apr / "ready to place".
- **Deposit not paid** (now 8 days past 21 Apr deadline).
- Sally waiting on bottles, B115 jars, deposit.
- **Outstanding:** Joel — pay deposit & confirm placement.

### CA 25072026
- POS MODEL: **Ordering**, Est. Completion **22 Jun**, Est. Arrival **6 Aug**.
- Includes Fire Collection restock + colours.
- Not yet placed.

### Two unnamed planned shipments
- POS MODEL shows future shipments at completion 29 Jun / arrival 13 Aug AND completion 15 Jul / arrival 29 Aug.
- Likely Container #5 (or similar) drafts.

---

## LOCAL FILL STATUS

### Swift Innovations — 31-01-2026 fill
- ✅ DELIVERED (Freightera confirmed 21 Apr; 3PL shows +2,010 units check-in line on 18 Apr; Heal + Remove 500ml back in stock).

### Swift — Next fill (Heal + Remove 500ml combined, ~7 May tentative)
- Per Remy's today summary: "We will likely need to do a heal fill next week on the 7th, we could likely do these at the same time."
- **At actual DSR, neither liquid is urgent:**
  - Heal: 8,541 units at 47.9/d kit-adj = 178d cover. Even at 1.5x scaled (120/d), 71d cover.
  - Remove 500ml: 3,457 units at 25.5/d 3PL = 136d cover. At Remy's 30/d post-restock estimate, 115d.
- **Sizing recommendation (lean / recommended / conservative):**

  | Heal qty | Cov @ 47.9/d actual | Cov @ 120.6/d projected |
  |---|---|---|
  | 5,000 | post-fill ~268d | post-fill ~107d |
  | 7,500 | post-fill ~321d | post-fill ~127d |
  | 10,000 | post-fill ~374d | post-fill ~148d |

  | Remove 500ml qty | Cov @ 25.5/d actual | Cov @ 75/d projected |
  |---|---|---|
  | 2,500 | post-fill ~217d | post-fill ~73d |
  | 4,000 | post-fill ~276d | post-fill ~93d |
  | 6,000 | post-fill ~354d | post-fill ~120d |

  Given the underlying overstock posture, **lean is the right move on both** — 5,000 Heal + 2,500 Remove 500ml, or skip and re-evaluate in 4 weeks.
- **Outstanding:** Daniel — decide qty + timing for combined fill placement.

### Mixam — 04-03-2026 ACC-LAB-CA
- 8,700 of 10,000 received (1,300 short). Still no reply from Mixam Canada (10 days since Mixam AU forwarded). Remy following up via email per today's confirmation.
- ACC-LAB-CA: 8,487 on hand. 3PL recent ded 0/d (rule recently re-enabled per 8 Apr Slack thread; verify deduction is now flowing). **Plan next Mixam order around mid-Jun** at projected 47/d kit-attach rate (since each kit gets one).

---

## STOCK-OUT FORECAST

Reconciling today's CA Summary list (computed at projected/scaled DSR) against actual DSR:

| Today's flag | Cover at projected | Cover at actual | Real risk? |
|---|---|---|---|
| Base −7d | -7d (assumes kit-adjust, 247 doesn't) | 224d | ❌ artefact |
| Glow −3d | -3d (same assumption) | 429d | ❌ artefact |
| Blue Moon −35d | 32d | 239d | ❌ |
| Blush −17d | TBD (not in critical script output) | not flagged | likely ❌ |
| Cashmere −30d | 38d | 118d | ❌ |
| Glacier Glow −60d | 7d | 45d | ⚠️ **YES** — 49 units, actual 1.1/d, gap to 21062026 (5 Jul) is −23d |
| Latte Cloud −27d | 40d | 167d | ❌ |
| Lemonade −35d | 32d | 320d | ❌ |
| Peony Puff −42d | 25d | 490d | ❌ |
| Sapphire Nights −26d | 41d | 235d | ❌ |
| Violet Flush −23d | 44d | 138d | ❌ |

**Of the 11 flagged: only Glacier Glow (POW-GLA-CS02) is a genuine pre-21062026 risk at actual DSR. 49 units, ~45d cover, container 67d away → ~23d OOS gap.**

### Other genuine risks (from script):

| SKU | Stock | DSR (actual) | Cover | Inbound | Gap |
|---|---|---|---|---|---|
| **POW-GLA-CS02 (Glacier Glow)** | **49** | **1.1/d** | **45d** | CA 21062026 +600 (5 Jul) | **−23d OOS** |
| POW-ALL-146 (All Eyes On Me) | 39 | 0/d (no recent sales) | — | CA 25072026 +400 | likely paused/listing — verify |
| POW-RED-165 (Red Mischief) | 1 | 0/d | — | CA 25072026 +600 | likely OOS already |
| POW-GAR-656 (Garnet Games) | 9 | 0/d | — | CA 25072026 +600 | likely OOS already |
| POW-BOR-355 (Bordeaux Nights) | 1 | 0/d | — | CA 25072026 +600 | likely OOS already |
| POW-INF-506 (Inferno Hour) | 42 | 0/d | — | CA 25072026 +400 | listing question |
| POW-SAF-149 (Saffron Blaze) | 50 | 0/d | — | CA 25072026 +400 | listing question |
| **POW-LAC-196 (Lace)** | **2,546** | **287.9/d (anomaly)** | **9d (if real)** | nothing on order | **investigate** |

### Stockout vs nothing-on-order
- **POW-LAC-196 (Lace)** — 2,574-unit single-day deduction 19 Apr. Probably a stock event, not real demand. **If real**, 9d cover and no inbound = critical. **Verify with 247 before any action.**
- **ACC-LAB-CA** — 8,487 on hand, deduction rate currently 0/d (rule recently re-enabled). Plan next Mixam order ~mid-Jun.

### Full safe set
218 SKUs sit at 45+ days cover. The customs container's arrival has put the broader catalogue in good shape.

---

## CASCADING ARRIVAL PROJECTION (Kits)

At actual kit DSR (46.2/d total: STA 13.0, COM 23.4, ULT 9.8):

| SKU | NOW (29 Apr) | After Powder Room (~30 Apr, no kit content) | After CA 21062026 (~5 Jul, +1,800 STA / +3,200 COM / +1,400 ULT @ 1.5x sized 20GP) | After CA 25072026 (~6 Aug) |
|---|---|---|---|---|
| KIT-STA-2 | 4,275 / 329d | 4,275 / 329d | 5,225 / 402d ⚠️ | further +arrivals |
| KIT-COM-4 | 8,231 / 352d | 8,231 / 352d | 9,901 / 423d ⚠️ | further +arrivals |
| KIT-ULT-6 | 3,372 / 344d | 3,372 / 344d | 4,135 / 422d ⚠️ | further +arrivals |

(Kit OL quantities from 21062026 are ballpark — verify against final reconfigured PO before placement.)

**At actual demand, every container compounds overstock.** If demand scales to 1.5x (120/d), post-21062026 kit cover lands at ~165d (KIT-STA-2 5,225 / 31.5/d) — still well above the 45-75d target.

### If CA 21062026 is delayed
- All kits remain comfortably stocked through the next container window. Delay risk is low.
- Genuine risk SKU: Glacier Glow only. A 21062026 delay extends the existing ~23d OOS gap.

---

## CONTAINER GAP ANALYSIS — CA 21062026

Pre-placement check (Daniel reconfigured to 1.5x / 20GP on 22 Apr):

- **Kit quantities:** Verify the 20GP cuts the kit OL substantially. If the 1.5x DSR (120/d) was used as the 70-day target, the PO will still over-stock at actual demand. **Recommend final review against actual 14d kit DSR before deposit pays.**
- **Glacier Glow:** Container has 600 units inbound. Current 49 stocks out ~12 Jun, container arrives 5 Jul → 23d gap. Express via Sally would need to be triggered now if we want to avoid the gap; otherwise accept.
- **ACC-LAB-CA:** Should NOT be on this container (locally printed via Mixam). Confirm 0 in OL.
- **ACC-REM-BOW:** 437d cover. Should be cut from container quantities if any allocated.
- **Liquids (Base, Glow):** Already 224d / 429d cover. Any liquid OL on this container is overstock-on-overstock.

---

## PO RECOMMENDATIONS

Target: 14-21d kit cover (lean). At 46.2/d actual, that's 650-970 kits. We are at 15,878 kits combined → **~344d cover. No CN PO needed for kits in 2026.**

| Category | Action |
|---|---|
| Kits | No new PO needed. CA 21062026 + CA 25072026 will both deepen overstock unless demand scales. |
| Heal / Remove 500ml | Optional fill ~7 May (lean: 5,000 Heal + 2,500 Remove 500ml) OR skip and re-evaluate in 4 weeks. |
| ACC-LAB-CA | Mixam reorder ~mid-Jun (allow 14-21d lead time + buffer). |
| Glacier Glow | Express via Sally OR accept 23d OOS pre-21062026. |
| Lace (anomaly) | Verify stock with 247 before any action. |

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (act today)
- **Joel:** Pay CA 21062026 deposit — **8 days past deadline**, blocking Sally + B115 jars + bottles.
- **Verify POW-LAC-196 deduction event** — 2,574-unit single-day pull on 19 Apr. If real, only 9d cover. Slack/email 247.
- **Glacier Glow decision** — 23d OOS gap pre-21062026. Express via Sally OR accept gap (recommend accept given low actual DSR / 49 unit stock makes express uneconomical).

### 🟡 WARNING (act this week)
- **Daniel:** Decide Heal + Remove 500ml fill quantities and timing for ~7 May Swift placement (recommend lean: 5,000 Heal / 2,500 Remove 500ml — or skip).
- **Remy:** Re-chase Mixam Canada on 1,300-unit ACC-LAB-CA shortfall (10 days no reply).
- **Greg:** POS MODEL DSR for Base / Glow appears kit-adjusted at scaled rate, but 247 doesn't pick per kit — produces misleading "−7d" / "−3d" cover in summaries. Recalibrate to standalone Shopify rate.
- **Greg:** ACC-REM-BOW model DSR still 80/d in sheet vs actual 13.1/d — outstanding from 15 Apr / 22 Apr reviews.

### 🟢 MONITOR (FYI)
- 247 check-in of remaining Powder Room (24-03-2026) — expected 30 Apr.
- POW-LAC-196 anomaly investigation (above).
- ACC-LAB-CA deduction flow re-enabled — confirm rule is firing this week.
- 9-week underselling pattern at 46% of 1.5x scaled target. Joel marketing-side; Remy/Daniel watching for trajectory shift.
- Customs container short-receipt reconciliation as 247 finishes their inbound process.

---

## FOLLOW-UP ITEMS (for Current Issues update)

- [ ] CA 21062026 deposit — 8 days overdue (Joel)
- [ ] Glacier Glow gap decision (Daniel/Joel)
- [ ] Lace deduction anomaly verification (Remy with 247)
- [ ] Heal + Remove 500ml fill decision (Daniel)
- [ ] Mixam Canada re-chase (Remy)
- [ ] POS MODEL DSR corrections — Base, Glow, ACC-REM-BOW (Greg)
- [ ] Powder Room 30 Apr arrival check-in confirmation
- [ ] Pre-21062026 kit quantity sanity-check vs actual demand (Remy/Daniel)
