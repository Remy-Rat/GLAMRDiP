# POS Model Check — CA — 6 May 2026

## DATA FRESHNESS

- **POS MODEL UPDATED:** 6 May 2026 (today, fresh paste)
- **B360 (3PL tab):** **BROKEN** - tab contains a single `#REF!` cell. **No 3PL deduction data available this cycle.** All cover figures below use POS MODEL stock + Shopify-derived DSR. Greg to repair the B360 reference urgently.
- **Shopify latest date:** 5 May 2026 (1d lag, normal)
- **ShipHero CSVs:** not provided (CA = 247 Fulfilment, no ShipHero)
- **Growth factor:** 1.5x (kit base 80/d → scaled 120/d)
- **Actual 14d kit DSR:** 46.4/d (STA 12.3 + COM 25.2 + ULT 8.9). Effective growth ~0.58x; -61% vs scaled.

## MANUAL OVERRIDES (user-confirmed today)

- **Remove 500ml fill:** NOT proceeding this cycle. Lean stance until cash + sell-rate justify.
- **Heal fill (Swift, ~7 May):** lean target. Confirm with Daniel quantity (~5,000) and lock collection date.
- **Mixam 1,300pcs ACC-LAB-CA:** reprint agreed. Stock figure not yet adjusted; treat 1,300 as pending inbound (no firm ETA).
- **POW-COL-G16 / CA-POW-COB-G17 SKU correction:** resolved 4-5 May. Powder Room (24-03-2026) check-in complete; container removed from POS MODEL.
- **CA 21062026 deposit:** still unpaid (15d past 21 Apr deadline). Cash-tight push-to-last-day stance.
- **POW-LAC-196 (Lace) 19 Apr 2,574-unit deduction:** likely same-day reversal per user; deprioritised. Recheck in Sales Analysis.

## STOCK POSITION

### Kits

| SKU | Stock | Projected DSR (1.5x) | Cover @ Projected | Actual 14d DSR | Cover @ Actual |
|---|---|---|---|---|---|
| KIT-STA-2 | 4,199 | 31.5 | 133d | 12.3 | 341d |
| KIT-COM-4 | 8,039 | 61.5 | 131d | 25.2 | 319d |
| KIT-ULT-6 | 3,312 | 27.0 | 123d | 8.9 | 372d |
| **TOTAL kits** | **15,550** | **120.0** | **130d** | **46.4** | **335d** |

Heavy overstock at actual demand. CA 25072026 (no kits would be region-recommended; current PO carries 5,404 kits).

### Liquids (CA = standalone-only; only Heal is kit-adjusted)

| SKU | Stock | Model DSR | Cover @ Model | Shopify 14d | Cover @ Shopify | Comment |
|---|---|---|---|---|---|---|
| LIQ-HEA-5 (Heal) | 8,197 | 127.5 (kit-adj) | 64d | 47.4 (kit-adj) | 173d | model = base+kit; actual much lighter |
| LIQ-BAS-2 (Base) | 1,440 | 25.5 | 56d | 8.2 | 175d | model still kit-attached - **Greg refresh needed** |
| LIQ-GLO-4 (Glow) | 1,543 | 15.0 | 103d | 4.0 | 386d | same |
| LIQ-BON-1 (Bond) | 1,028 | 12.0 | 86d | 2.4 | 428d | overstock |
| LIQ-SEA-3 (Seal) | 1,089 | 18.0 | 60d | 5.6 | 195d | |
| LIQ-SOA-6 (Soak) | 925 | 12.0 | 77d | 2.4 | 385d | |
| LIQ-MAT-4 (Matte) | 1,244 | 10.5 | 119d | 2.7 | 461d | |
| LIQ-SEN-2 (LO Base) | 756 | 6.0 | 126d | 3.1 | 244d | |
| LIQ-SEN-4 (LO Glow) | 622 | 4.5 | 138d | 2.2 | 283d | |

**Note:** Per `Shared/Component Map.md`, only Heal is kit-adjusted in CA. Base/Glow model DSR carrying kit-attached basis is the documented Greg-refresh item.

### Remove products (with bundle deductions)

| SKU | Stock | Model | Standalone Shopify | Combined Rate (incl. bundles) | Cover @ Combined | Comment |
|---|---|---|---|---|---|---|
| ACC-REM (120ml) | 4,081 | 46.5 | 5.5 | 9.3 (+BUN-1 3.8) | 439d | overstock |
| ACC-REM-500 (500ml) | 3,243 | 75.0 | 16.6 | 28.3 (+BUN-2 11.7) | 115d | lean fill defer OK |
| ACC-REM-BOW | 5,597 | 60.0 | 1.4 | 16.9 (+both BUN) | 331d | model still ~3.5x actual |

### Inserts / packaging (per-order, no Shopify SKU)

| SKU | Stock | Model DSR | Cover @ Model | Notes |
|---|---|---|---|---|
| ACC-INS | 23,153 | 120.0 | 193d | inbound 3,600 on 25072026 |
| ACC-THA | 34,642 | 231.0 | 150d | inbound 11,200 (21062026) + 8,400 (25072026) - heavy overstock building |
| ACC-LAB-CA | 7,823 | 231.0 | 34d | + 1,300 Mixam reprint pending |

At actual order rate (~80-100/d total orders, vs 231/d model), ACC-LAB-CA real cover ~78-98d. Flag for Greg: model rate is ~2.3x actual.

## CHECK-IN PROGRESS

- **CA Powder Room (24-03-2026) (PO 37):** complete. Powder Room + B113 jars checked in at 247 (Anton + Paige confirmation 4 May). SKU correction POW-COL-G16 → CA-POW-COB-G17 applied. Container removed from POS MODEL.
- No other partial check-ins in flight.

## DOUBLE-COUNT DETECTION

No active container check-ins overlap with POS MODEL projections. **No double-counting detected.**

## CORRECTED DAYS COVER (CRITICAL flags only)

At Shopify 14d actual DSR (the real demand picture):

| SKU | Stock | DSR (actual) | Cover | Inbound | Cover After | Flag |
|---|---|---|---|---|---|---|
| POW-GLA-CS02 (Glacier Glow) | 33 | 1.6 | 21d | 600 (15 Jul) | -49d gap | WARNING |
| POW-BLU-ZGD22 (Blue Moon) | 157 | 3.3 | 48d | 600 (15 Jul) | -22d gap | WARNING |
| POW-PEO-SH07 (Peony Puff) | 163 | 2.7 | 60d | 800 (15 Jul) | -10d gap | WATCH |
| POW-LEM-ZGD01 (Lemonade) | 172 | 2.0 | 86d | 600 (15 Jul) | safe | OK |

At projected 1.5x DSR (the order-against rate), the at-risk list expands - kept for visibility:

| SKU | Stock | Model DSR | Cover @ Model | Inbound | Comment |
|---|---|---|---|---|---|
| POW-CAS-CS32 (Cashmere) | 224 | 6.3 | 35d | 600 (21062026) | safe at actual (157d) |
| POW-LAT-CS38 (Latte Cloud) | 221 | 5.9 | 37d | 600 (21062026) | safe at actual |
| POW-SAP-11933 (Sapphire) | 249 | 6.3 | 40d | 600 (21062026) | safe at actual |
| POW-VIO-11932 (Violet Flush) | 225 | 5.3 | 42d | 600 (21062026) | safe at actual |
| POW-BLU-ZGD06 (Blush) | 268 | 4.5 | 60d | 400 (21062026) | safe at actual |

The 29 Apr "11 SKUs at risk" list contracts to 3 once we look at actual Shopify demand.

## PACKAGING & INSERTS

**Cannot compute deduction rates this cycle - B360 tab broken.** Order-rate proxy (model 231/d ACC-THA, 120/d ACC-INS) gives heavy-overstock signal regardless. Recheck in next cycle once Greg repairs B360.

## CONTAINER / ORDER STATUS

### CA 21062026 (Birthday Sale) - In Production
- **POS MODEL:** Est. Completion 31 May, Est. Arrival 15 Jul, Status `Ordering`
- **Slipped 10 days** vs last recap (was 21 May / 5 Jul on 29 Apr)
- **Deposit STILL NOT PAID** - 15 days past 21 Apr deadline
- Brings: NO kits, 59,100 units total - 4,000 ACC-REM-BOW + 11,200 ACC-THA + 10,000 STO-MAI-BAG-S + 10,450 STO-MAI-2 + 7,200 liquids + 13,200 colours (incl. 13 Birthday Sale colours)
- **REALITY:** Sally still waiting on bottles, B115 jars, deposit. Each day of deposit delay = 1 day of arrival slip.
- **ACTION:** Joel - pay deposit. With Sally backdated $150k blocking ships per general policy, this PO is also caught upstream until that's resolved.

### CA 25072026 - Ordering / Planned
- **POS MODEL:** Est. Completion 22 Jun, Est. Arrival 6 Aug, Status `Ordering`
- Brings: 5,404 kits + 86,312 units total (heavy mix - all colours + accessories + liquids)
- **REGION FILE FLAG:** "*At current demand, CA does not need another kit container until 2027.*" The 5,404 kits here directly contradicts the post-overstocking guidance.
- **ACTION:** Daniel/Joel/Remy - pre-placement sanity check. Recommend dropping kits entirely and trimming liquids/ACC-THA given existing 100+d cover at actual.

## LOCAL FILL STATUS

### Swift Innovations - Heal fill (planned ~7 May)
- **POS MODEL:** no active inbound block for Heal (locally filled, not on container)
- **Decision:** lean ~5,000 Heal, no Remove 500ml (user confirmed today)
- **Status:** awaiting Daniel lock on quantity + Swift collection booking
- **Sizing math:**
  - Lead: ~5-7d from fill complete to 247 restock (per memory `reference_swift_lead_times.md`)
  - Current Heal: 8,197 units / 47.4/d kit-adjusted actual = 173d
  - At delivery (+7d): 8,197 - 332 = 7,865 → **+5,000 = 12,865 / 47.4/d = 271d cover**
  - At projected 127.5/d: 7,865 + 5,000 = 12,865 / 127.5 = 101d projected cover
- **At actual rate, even a lean 5,000 fill produces 9 months of cover.** Could go leaner (3,000) and still hold ~165d at actual / 62d at projected. Daniel call.

### Swift Remove 500ml fill - DEFERRED
- 3,243 units / 28.3/d combined demand = 115d cover. Not urgent. Re-evaluate next review.

## STOCK-OUT FORECAST

### --- Stockout before arrival (gap < 0 at actual DSR) ---
| SKU | Stock | Actual DSR | Stocks Out | Next Inbound | Arrives | Gap |
|---|---|---|---|---|---|---|
| POW-GLA-CS02 (Glacier Glow) | 33 | 1.6/d | 21d (~27 May) | 21062026 +600 | 15 Jul | -49d |
| POW-BLU-ZGD22 (Blue Moon) | 157 | 3.3/d | 48d (~23 Jun) | 21062026 +600 | 15 Jul | -22d |
| POW-PEO-SH07 (Peony Puff) | 163 | 2.7/d | 60d (~5 Jul) | 21062026 +800 | 15 Jul | -10d |

User stance previously: accept Glacier Glow gap; not expressing. Carry that across all 3 unless commercial decision says otherwise (Sally express also constrained by $150k arrears - likely not viable).

### --- Tight (0-7 day buffer) ---
None.

### --- Nothing on order, under 84d cover ---
None at actual rate. (At model rate, ~10 colours fall in this band but actual rate clears them all.)

### --- Safe ---
~250 SKUs with 90+d cover at actual DSR or with inbound arriving in time.

## WHAT NEEDS ACTION

### 🔴 CRITICAL (today)
- **B360 tab broken (`#REF!`).** Greg to repair. Without this, deduction monitoring + packaging anomaly detection are blind.
- **CA 21062026 deposit still unpaid (15d past deadline).** Joel - pay this week. Each day delays the 15 Jul arrival further.

### 🟡 WARNING (this week)
- **Heal fill (Swift) - lock the call.** Daniel: confirm quantity (~5,000 lean per user / ~3,000 leaner) + collection date for ~7 May. Without lock, the Swift slot is wasted.
- **Mixam reprint confirmation.** Remy chase Mixam Canada (16 days silent) for written reprint confirmation + ETA on the 1,300pcs ACC-LAB-CA.
- **Labels-booklet customer email backlog.** 3 weeks since 15 Apr ask. Remy pull list of orders 20 Mar - 7 Apr fulfilled without booklets.
- **CA 25072026 pre-placement review.** 5,404 kits contradicts region overstock guidance. Daniel/Joel decision before placement.

### 🟢 MONITOR (FYI)
- POW-GLA-CS02 / POW-BLU-ZGD22 / POW-PEO-SH07 stockout windows (Sally express constrained, accept gaps).
- ACC-LAB-CA next Mixam order trigger ~mid-Jul at actual order rate.
- Univar acetone tote refund - Joel side, no recent email trail; possibly already actioned offline. Confirm and close.

## LOCAL FILL FORECAST

### Swift - Heal (LIQ-HEA-5) - kit-adjusted DSR 47.4/d
- Current: 8,197 (173d at actual)
- Fill arriving ~14 May (+5,000) → 12,865 post-fill (271d at actual / 101d at projected 127.5/d)
- Next fill place by: ~mid-Aug at actual rate; ~mid-Jul at projected 1.5x
- **Birthday Sale impact:** 21062026 carries no kits, so no spike adjustment needed for Heal in the 15 Jul-Aug window.

### Swift - Remove 500ml - DEFERRED this cycle
- Re-evaluate at next review (13 May). At 28.3/d combined, 115d cover holds through end of August.

## PO RECOMMENDATIONS

Target: 14-21d kit cover (lean) at projected. Lead times: 84d (raw goods → delivery), 44d (filling PO → delivery), 30d (shipping only).

### Kits - no PO needed before 2027
At actual demand (335d cover now → 360d after 25072026 lands), no kit PO needed even past CA 25072026. Region file recommendation stands: future containers should NOT carry kits.

### ACC-LAB-CA (Mixam local print) - next order trigger
- 7,823 + 1,300 reprint = 9,123 expected
- At actual ~80-100/d order rate: 91-114d cover post-reprint
- **Next Mixam order ~mid-Jul** (lead 14-21d at Mixam Canada)

### CA 25072026 (Ordering, est. completion 22 Jun) - reduce before placement
- Drop kits entirely (5,404 → 0)
- Trim liquids: at 100-460d cover, CA does not need any LIQ-* on this PO.
- Trim ACC-THA from 8,400 to ~0 (already 150d model / ~250d actual cover, plus 11,200 inbound on 21062026).
- Keep colours (variety) and ACC-INS (3,600 is reasonable at 192d → 222d post-arrival).

## CASCADING ARRIVAL PROJECTION

Actual kit DSR: 46.4/d. Projected (1.5x): 120/d.

|  | NOW | After CA 21062026 (15 Jul) | After CA 25072026 (6 Aug) |
|---|---|---|---|
| Kits stock | 15,550 | ~12,302 | ~16,685 |
| Cover @ projected | 130d | 103d | 139d |
| Cover @ actual | 335d | 265d | 360d ⚠️ |

**At actual demand, CA finishes Aug with 360 days of kit cover.** Even at projected 1.5x, post-25072026 sits at 139d - well above the 45-75d target.

### Overstock flags (post-arrival cover > 100d)
- All 3 kits: 250-370d cover at actual. Reduce 25072026 kit qty.
- ACC-THA: 250d actual now → ~340d post-21062026 → ~430d post-25072026. Stop ordering this until 2027.
- ACC-INS: 192d actual now → ~210d post-25072026.
- LIQ-* (Base, Glow, Bond, Seal, Soak, Matte): 175-461d actual now. 21062026 + 25072026 add another ~100-200d cover.
- ACC-REM (120ml): 439d actual.
- ACC-REM-BOW: 331d actual + 4,000 (21062026) + 2,700 (25072026) = ~570d.

### Delay scenario - if CA 21062026 slips further (Sally $150k bridge)
- All 3 OOS-gap colours (Glacier Glow, Blue Moon, Peony Puff) widen by 1 day per 1 day slip.
- Kit cover well-buffered - no kit risk.
- ACC-THA / ACC-REM-BOW already heavily overstocked - delay is operationally fine for kits + accessories; only the 3 colours feel it.

## FOLLOW-UP ITEMS

### Immediate (this week)
- [ ] Greg: repair B360 tab `#REF!` so deduction monitoring works again
- [ ] Joel: pay CA 21062026 deposit (15d past deadline)
- [ ] Daniel: lock Heal fill quantity (~5,000 lean) + Swift 7 May collection date
- [ ] Remy: chase Mixam Canada for written reprint confirmation + ETA
- [ ] Remy: pull labels-booklet affected order list for Gav/CX (3 weeks open)

### By end of month
- [ ] Daniel/Joel/Remy: CA 25072026 pre-placement review - recommend no kits, trim liquids + ACC-THA
- [ ] Greg: refresh POS MODEL DSR for Base/Glow (drop kit-attached double-count) and ACC-REM-BOW (60/d → ~17/d actual)
- [ ] Greg: refresh ACC-LAB-CA model DSR (231/d → ~80-100/d actual order rate)
- [ ] Joel: confirm Univar acetone tote refund received - close the open thread

### Ongoing
- Monitor 3 colour OOS gaps (Glacier Glow / Blue Moon / Peony Puff) - accept unless commercial reason
- ACC-LAB-CA next Mixam order trigger ~mid-Jul at actual rate
- Watch effective growth factor 0.58x vs 1.5x scaled - 10 weeks consistent. No recommendation to lower (per growth-factor doctrine), but factor into 25072026 sizing.
