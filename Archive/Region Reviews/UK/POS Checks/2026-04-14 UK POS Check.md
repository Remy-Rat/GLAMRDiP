# UK POS Model Check — 14 Apr 2026

## Data Freshness
- POS MODEL last updated: 14 Apr 2026
- B360 data last valid: 14 Apr 2026
- ShipHero: Not available — Fulfillable uses a different system
- Growth factor: 1.1x (base 84/day → scaled 92.4 kits/day)
- Fulfillable went live: 13 Apr 2026 — stock sync enabled, orders processing

---

## Stock Position

No ShipHero CSVs — using POS MODEL "FULFILLABLE" column as the stock source. B360 Packup = incoming transfer from old 3PL.

### Kits
| SKU | Fulfillable | Cover | B360 In | After | UK03 OL | UK07 OL |
|---|---:|---:|---:|---:|---:|---:|
| KIT-STA-2 | 378 | 34d | 493 | 871 | 448 | 336 |
| KIT-COM-4 | 4,479 | 110d | 40 | 4,519 | 1,484 | 1,316 |
| KIT-ULT-6 | 4,630 | 114d | 0 | 4,630 | 700 | 1,148 |

- KIT-STA-2 tightest at 34d but doubles after B360 transfer
- KIT-COM-4 and KIT-ULT-6 comfortable — 110+ days

### Liquids (Kit-Adjusted)
| SKU       | Fulfillable | Model Cover | Kit-Adj DSR | Kit-Adj Cover | B360 In |
| --------- | ----------: | ----------: | ----------: | ------------: | ------: |
| LIQ-BAS-2 |       1,629 |         74d |   114.4/day |           14d |      32 |
| LIQ-GLO-4 |       1,608 |        146d |    92.4/day |           17d |     596 |
| LIQ-HEA-5 |       9,623 |        103d |    93.5/day |          103d |   1,653 |
| LIQ-SEA-3 |       3,119 |        236d |    13.2/day |          236d |     369 |
| LIQ-BON-1 |         635 |        115d |     5.5/day |          115d |     194 |
| LIQ-MAT-4 |         847 |        128d |     6.6/day |          128d |     469 |
| LIQ-SOA-6 |         639 |        116d |     5.5/day |          116d |     588 |
| LIQ-SEN-2 |           0 |         OOS |           — |             — |       0 |
| LIQ-SEN-4 |           0 |         OOS |           — |             — |       0 |

Base and Glow model DSR is understated. Fulfillable confirmed (13 Apr) they are picking Base + Glow + Heal per kit via automation rules. B360 did NOT do this — those liquids were inside the CN kit. Now that Fulfillable picks them, demand jumps from standalone (22/day Base, 11/day Glow) to kit-adjusted (114.4/day Base, 92.4/day Glow).

### Inserts & Packaging
| SKU | Fulfillable | Cover | B360 In | After | Flag |
|---|---:|---:|---:|---:|---|
| ACC-INS | 10,431 | 116d | 7,349 | 17,780 | OK |
| ACC-LAB-UK | 9,421 | 51d | 1,396 | 10,817 | WATCH — no inbound |
| ACC-THA | 26,621 | 145d | 5,246 | 31,867 | OK |
| STO-BUB-BAG-L | 13,633 | 151d | 1,440 | 15,073 | OK |
| STO-BUB-BAG-S | 0 | OOS | 19,445 | 19,445 | B360 transfer needed |
| STO-MAI-2 | 9,480 | 101d | 3,469 | 12,949 | OK |
| STO-MAI-BAG-S | 11,800 | 126d | 3,555 | 15,355 | OK |

---

## Container / Order Status

**B360 Packup** — 288,898 units at old 3PL
- No reference/order number — physical transfer
- Timing: TBD
- Includes: 45 OOS colour SKUs, all STO-BUB-BAG-S (19,445), 7,349 ACC-INS, 5,246 ACC-THA, 1,653 LIQ-HEA-5

**Chemence 10-03-2026 Fill** — 8,000 Base + 8,000 Glow
- Dispatch: 28 Apr. Payment due 27 Apr.
- Delivery to Fulfillable: ~29 Apr.

**UK 03062026** (JS21-20260303-2) — In Production
- Est. Completion: 15 Apr. Est. Arrival: 9 Jun.
- 84,424 units. Daniel: "will be complete very soon."

**UK 02072026** (JS21-20260326-2) — Birthday Sale — In Production
- Est. Completion: 15 May. Est. Arrival: 9 Jul.
- Deposit still required. Growth factor 1.4x.

**UK 02082026** — Planned
- Fill PO place date: 29 Apr. Est. Completion: 8 Jun. Est. Arrival: 2 Aug.

---

## Local Fill Status

**Chemence — Base, Glow, Seal**
- "11-02-2026 UK Chemence Fill 2nd Part": DELIVERED to Fulfillable ~9 Apr
- "10-03-2026 UK Chemence Fill": Dispatch 28 Apr, payment due 27 Apr
- Next fill: Daniel placing "over coming days" (14 Apr). 6-8 week lead.

**Oils4Life — Heal**: No active fill. 103d cover. No urgency.

**Liquipak — Remove (EXITING)**: Final PO placed 2 Apr. ~160d coverage. No replacement found.

---

## Stock-Out Forecast

### Stockout Before Arrival
| SKU | Stock | DSR | Stocks Out | Inbound | Arrives | Gap |
|---|---:|---:|---|---|---|---|
| LIQ-BAS-2 | 1,629 | 114.4/day | 28 Apr | Chemence 8k | 29 Apr | 0d margin |

### Tight
| SKU | Stock | DSR | Stocks Out | Inbound | Arrives | Gap |
|---|---:|---:|---|---|---|---|
| LIQ-GLO-4 | 1,608 | 92.4/day | 1 May | Chemence 8k | 29 Apr | 2d (OK if B360 +596 arrives) |

### Nothing On Order
| SKU | Stock | DSR | Cover | Note |
|---|---:|---:|---|---|
| ACC-LAB-UK | 9,421 | 183.7/day | 51d | After B360 = 59d. Not on any future container. |

---

## Chemence Fill Forecast (Base & Glow)

Using actual kit-adjusted DSRs: Base 89.6/day, Glow 95.6/day.

### LIQ-BAS-2 (Base)
| Date | Event | Stock | Cover |
|---|---|---:|---:|
| 14 Apr | Current | 1,629 | 18d |
| ~18 Apr | B360 Packup +32 | 1,303 | 15d |
| 29 Apr | Chemence 10-03-2026 +8,000 | 8,317 | 93d |
| ~11 Jun | Next Chemence (8wk) +8,000 | 12,464 | 139d |
| ~28 Oct | STOCKOUT | 0 | 0d |

Place THIRD Chemence fill by: **16-23 Aug 2026** (at 7-8 week lead)

### LIQ-GLO-4 (Glow)
| Date | Event | Stock | Cover |
|---|---|---:|---:|
| 14 Apr | Current | 1,608 | 17d |
| ~18 Apr | B360 Packup +596 | 1,822 | 19d |
| 29 Apr | Chemence 10-03-2026 +8,000 | 8,770 | 92d |
| ~11 Jun | Next Chemence (8wk) +8,000 | 12,659 | 132d |
| ~21 Oct | STOCKOUT | 0 | 0d |

Place THIRD Chemence fill by: **9-16 Aug 2026** (at 7-8 week lead)

### Summary
- After both current + next Chemence fills: ~4 months of Base & Glow cover
- Third fill: place by mid-Aug for arrival by mid-Oct. Calendar this.

---

## PO Recommendations — UK 02082026

Model dates: Fill PO 29 Apr, Completion 8 Jun, Arrival 2 Aug.

Kit simulation (actual DSRs: STA 14.9, COM 28.0, ULT 46.6):

| Kit | After UK07 (9 Jul) | Cover | Hits 17d | Stockout | UK08 Needed By |
|---|---:|---:|---|---|---|
| KIT-STA-2 | 374 | 25d | 17 Jul | 3 Aug | **17 Jul** |
| KIT-ULT-6 | 2,470 | 53d | 14 Aug | 31 Aug | 14 Aug |
| KIT-COM-4 | 4,911 | 175d | 14 Dec | 31 Dec | No rush |

**KIT-STA-2 is the binding constraint.** STA selling 49% above model (14.9 vs 10/day). At actual rate, STA hits 17d cover on 17 Jul — the 2 Aug model arrival is 2 weeks late.

Working back from 17 Jul arrival (STA binding):
- Completion by: 5 Jun
- **Fill PO by: 26 Apr** (12 days from now)
- Raw goods by: 15 Feb (past — confirm at Sally)

**Recommendation:**
- **Fill PO for UK 02082026 should be placed by 26 Apr** (12 days)
- If STA normalises back to 10/day, the 2 Aug arrival is fine — but at current demand it's tight
- Raw goods should already be at Sally for this order — confirm
- Alternative: increase STA allocation on UK 02072026 (Birthday, 9 Jul) as buffer

---

## What Needs Action

### 🔴 CRITICAL (act today)
- **LIQ-BAS-2 stocks out 28 Apr at kit-adjusted rate.** Chemence dispatches 28 Apr — 0-day margin. Joel must pay by 27 Apr.
- **POS MODEL DSR for Base & Glow is wrong.** Actual kit-adjusted: 114.4/day Base, 92.4/day Glow. Greg needs to update model.
- **B360 Packup transfer has no timeline.** 288,898 units. Confirm date with B360/Fulfillable.

### 🟡 WARNING (act this week)
- **UK 02072026 deposit still required.** Birthday Sale container. Priority per Daniel.
- **UK 02082026 fill PO by 26 Apr.** STA selling 49% above model — 2 Aug arrival may be late.
- **ACC-LAB-UK not on any future container.** 59d cover. Add to UK 02072026.
- **STO-BUB-BAG-S at 0 at Fulfillable.** All 19,445 at B360. Transfer needed.

### 🟢 MONITOR
- UK 03062026 completing ~15 Apr. 84k units arriving 9 Jun.
- Fulfillable ramping up. Minor bundle error (4 orders, rectified).
- EMPTY-GLASS-BOT-INNER under received by 19,228.
- Liquipak final PO — ~160d Remove coverage. No replacement filler.
- Third Chemence fill: calendar mid-Aug placement.

---

## Follow-Up Items

### Immediate (this week)
- [ ] **Joel: pay Chemence by 27 Apr** — 10-03-2026 fill (8k Base + 8k Glow). Base stocks out same day if delayed.
- [ ] **B360 Packup — initiate the stock-out process:**
  - £8,500 GBP stockout deposit not yet paid (Mason asked 13 Apr). Joel to confirm.
  - Work Orders for stocktake + packing not yet submitted by Joel/Greg.
  - Chris (13 Apr): stocktake begins after 55 final orders ship, "I'll provide further details once this commences."
  - No timeline yet for physical transfer to Fulfillable. STO-BUB-BAG-S (19,445 units) at 0 at Fulfillable — blocks liquid order packaging.
  - Don't assume quarantined Base/Glow at B360 is filled product — we only sent ~2k of each to B360. Stocktake will clarify.
- [ ] **Greg: update POS MODEL DSR for Base & Glow** — model uses standalone rates (22/day, 11/day). Fulfillable now picks both per kit. Actual kit-adjusted: ~90/day Base, ~96/day Glow.
- [ ] **Verify stock sync** — Daniel reviewing 14 Apr. Confirm Fulfillable inventory matches POS MODEL "FULFILLABLE" column.

### By end of April
- [ ] **Place UK 02082026 fill PO by ~26 Apr** — STA selling 49-71% above model. At current rate, 2 Aug arrival is 2 weeks late. Fill PO needed ~26 Apr for a mid-Jul arrival.
- [ ] **Confirm raw goods at Sally for UK 02082026** — raw goods deadline was mid-Feb (past). Need confirmation they're in hand.

### By mid-May
- [ ] **Place next Chemence fill by ~12 May** — 8k Base + 8k Glow (confirm if Seal needed too). Targeting arrival pre-Birthday Sale (late Jun/early Jul). 8-week lead = place by 12 May.

### Ongoing
- [ ] **ACC-LAB-UK** — 59d cover at 183.7/day. Printed locally, 14-21d lead time. Not urgent but monitor and reorder when needed.
- [ ] **Nordic Chemence fill** — Joel wants recommended PO. Prep this week (Daniel, 10 Apr).
- [ ] **Liquipak replacement** — no UK filler found. Continue outreach or evaluate CN filling for Remove.
- [ ] **Calendar third Chemence fill ~mid-Aug** — place by 9-16 Aug to maintain cover through Q4.
- [ ] **EMPTY-GLASS-BOT-INNER discrepancy** — under received by 19,228 at Fulfillable. Investigate.
- [ ] **KIT-STA-2** — selling 49-71% above model. Worst case, swap COM for STA (established pattern). Monitor.

### Slack Summary Review (14 Apr)
Remy's updated message covers the key points well. Minor notes for next update:
- B360 Packup transfer deserves its own discussion point — stock-out process not yet initiated, no timeline

---

*Generated by Claude Code — POS Model Check skill*
*Data: UK Order Schedule (Google Drive, downloaded 14 Apr 13:05), Slack #uk-inventory, Gmail (Fulfillable + Chemence threads)*
