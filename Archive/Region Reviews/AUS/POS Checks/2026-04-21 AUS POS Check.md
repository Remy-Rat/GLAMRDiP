# POS MODEL CHECK — AUS — 21 Apr 2026

## DATA FRESHNESS

- POS MODEL last updated: **21 Apr 2026** (same-day — user-confirmed, sheet cell H8 agrees)
- 3PL tab (AUS 3GPL) last valid: **21 Apr 2026** (today)
- Shopify sales data through: **20 Apr 2026** (1-day lag, normal)
- Projected DSR (1.3x growth): 191.1 kits/day (STA 44.2 / COM 101.4 / ULT 45.5)
- Actual DSR (14d kit total): 108.7/day = 0.74x of base — see growth factor check below.

---

## MANUAL OVERRIDES APPLIED

| Item | Sheet says | Override | Source |
|---|---|---|---|
| OP Remove 500ml fill Est. Completion | 14 Apr | **~24 Apr** (this week) | User-confirmed 21 Apr ("5,000 units being sent sometime this week") |
| OP Remove 500ml fill Est. Arrival | 19 Apr | **~1–2 May** (7d delivery from OP→G3PL) | Derived from above |
| AUS 09052026 Est. Arrival | 30 May (on sheet) | **30 May confirmed** | Sheet already updated — no override |

No further manual overrides required. Greg's paste is current. PO 11 (Avi 15,000 labels, checked in 17 Apr) already reflected at ACC-LAB = 17,699 on sheet.

---

## KIT-ADJUSTED DSR VALIDATION

AUS kit-adjusted items per Component Map: **LIQ-HEA-5 (Heal), ACC-INS (Instructions)**. ACC-LAB / ACC-THA are per-order (all orders).

| SKU | Model DSR | Kit consumption (1.3x) | 3PL Ded/d (14d) | Verdict |
|---|---:|---:|---:|---|
| LIQ-HEA-5 | 184.6 (implied from 10,449 / 61d) | 191.1 (Heal × 1 per kit) | 123.7 | Model DSR ≈ 1.3x kit. Actual 3PL rate suggests ~0.80x actual selling (aligns with 0.74x kit-level). **Use 123.7/d (3PL) for planning — model is aspirational.** |
| ACC-INS | ~149/d (implied 19,020 / 128d) | 191.1 | 118.4 | Same pattern — model assumes 1.3x, actual 3PL at 118.4/d. Use 118.4/d for planning. |
| ACC-LAB | ~194/d | ~108 (all orders, includes standalones) | 194.5 | Model = 3PL. No adjustment needed. |
| ACC-THA | ~194/d | ~108 | 194.5 | Model = 3PL. No adjustment needed. |

---

## GROWTH FACTOR HEALTH CHECK

| | Value |
|---|---:|
| Model growth factor | 1.3x (→ 191.1/d) |
| Actual 14d kit DSR | 108.7/d = **0.74x** |
| Actual 30d kit DSR | 116.1/d = **0.79x** |
| Gap | **-43% vs model (14d)** / -39% (30d) |

Sustained gap of ~40% for 10+ consecutive weeks. This is a health flag, not a recommendation to lower the factor — 1.3x is the marketing-ambition target and we'd rather be slightly heavy than short.

**Practical impact:** every container sized at 1.3x OL accumulates excess. The cascading projection below flags post-09052026 overstocks on COM (+post-arrival 350d cover), ULT (+170d), Remove Bowl (218d), and Heal (184d). Joel / Daniel should review 08072026 OL quantities at actual run rate before the 29 Apr fill PO place date — this is the same flag carried from 17 Apr.

---

## STOCK POSITION

Source: AUS 3GPL tab + POS MODEL (today's paste). Two covers per SKU: **Projected** = POS MODEL DSR × 1.3x; **Actual** = 3PL 14d deduction rate (falls back to Shopify where 3PL is anomaly-corrupted — flagged ^).

### Kits
| SKU | Stock | Projected DSR | Cover @ Projected | Actual DSR | Cover @ Actual |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 1,165 | 44.2 | 26d | 30.8 | 38d |
| KIT-COM-4 | 4,878 | 101.4 | 48d | 56.3 | 87d |
| KIT-ULT-6 | 2,867 | 45.5 | 63d | 21.6 | 133d |

### Liquids
| SKU | Stock | Projected DSR | Cover @ Projected | Actual DSR | Cover @ Actual |
|---|---:|---:|---:|---:|---:|
| LIQ-HEA-5 (Heal) | 10,449 | 184.6 | 57d | 123.7 | **84d** |
| LIQ-BAS-2 (Base) | **604** | 53.3 | **11d** | 20.7 | **29d** |
| LIQ-SEN-2 (LO Base) | **97** | 9.1 | 11d | 2.7 | **36d** |
| LIQ-GLO-4 (Glow) | 879 | 26.0 | 34d | 13.9 | 63d |
| LIQ-SEN-4 (LO Glow) | 181 | 7.8 | 23d | 2.9 | 63d |
| LIQ-SEA-3 (Seal) | 2,553 | 20.3 | 126d | 16.3 | 157d |
| LIQ-BON-1 (Bond) | 1,358 | 10.8 | 126d | 8.4 | 162d |

### Remove products
| SKU | Stock | Projected DSR | Cover @ Projected | Actual DSR | Cover @ Actual |
|---|---:|---:|---:|---:|---:|
| ACC-REM-500 | 3,507 | 98.8 | 35d | 52.3 | 67d |
| ACC-REM (120ml) | 7,581 | 28.3 | 268d | 22.4 | 338d |
| ACC-REM-BOW | 1,443 | 75.4 | 19d | 38.0 | **38d** |

### Inserts / packaging
| SKU | Stock | Projected DSR | Cover @ Projected | Actual DSR | Cover @ Actual |
|---|---:|---:|---:|---:|---:|
| ACC-LAB | 17,699 | 243 | 73d | 194.5 | 91d |
| ACC-THA | 32,089 | 243 | 132d | 194.5 | 165d |
| ACC-INS | 19,020 | 191.1 | 100d | 118.4 | 161d |
| STO-BUB-BAG-L | 11,682 | 191.1 | 61d | 167.5 | 70d |
| STO-BUB-BAG-S | 12,902 | — | — | 139.2 | 93d |
| STO-MAI-BAG-S | 19,689 | — | — | 57.7 | 341d |
| STO-MAI-2 | 17,128 | — | — | 58.3 | 294d |

Benchmark anomalies (14d): STO-BUB-BAG-L had 1 day over benchmark (06 Apr: 449 vs 435). STO-BUB-BAG-S near benchmark — monitor. All others clean.

### Colours with anomaly-driven rate divergence
These SKUs have single-day 1,000-unit 3PL spikes that inflate the actual rate (see "3PL Deduction Anomalies" block). Actual DSR uses Shopify 14d as the substitute.

| SKU | Name | Stock | Projected DSR | Cover @ Projected | Actual DSR^ | Cover @ Actual |
|---|---|---:|---:|---:|---:|---:|
| POW-ENE-484 | Energy | 1,008 | 1.3 | 775d | 0.6 | 1,680d |
| POW-JUS-449 | Just Friends | 1,323 | 10.4 | 127d | 5.9 | 224d |
| POW-BRE-109 | Breeze | 1,583 | 10.4 | 152d | 2.8 | 565d |
| POW-DRE-771 | Dream Catcher | 2,125 | 18.2 | 117d | 7.5 | 283d |
| POW-GOL-597 | Golden Child | 2,384 | 16.9 | 141d | 7.2 | 331d |
| POW-CRE-217 | Creme Brulee | 2,080 | 23.4 | 89d | 17.3 | 120d |
| POW-ROY-304 | Royalty | 2,501 | 11.7 | 214d | 10.2 | 245d |
| ACC-TIP-SQU | Square Tips | 2,540 | 11.7 | 217d | 5.8 | 438d |

^ = Shopify-derived (3PL rate corrupted by deduction anomaly).

### Fire Collection — listing-status caveat
7 Fire Collection colours show 3PL rate ~6.5/d and 0 Shopify 14d sales. Actual DSR can't be trusted until Shopify listings are confirmed live.

---

## 3PL DEDUCTION ANOMALIES — STILL UNRESOLVED

The 17 Apr flag of "22,090 units of unexplained colour deductions" has **worsened** — 3 more single-day ~1,000-unit events since:

| Date | SKU | Deduction | Benchmark (35) | Shopify same day |
|---|---|---:|---:|---|
| 2026-04-08 | POW-JUS-449 | 1,006 | ×29 | normal (~6/d) |
| 2026-04-08 | POW-DRE-771 | 1,113 | ×32 | normal (~7/d) |
| 2026-04-11 | POW-ROY-304 | 1,013 | ×29 | normal (~10/d) |
| 2026-04-12 | POW-BRE-109 | 1,007 | ×29 | normal (~3/d) |
| 2026-04-13 | POW-GOL-597 | 1,108 | ×32 | normal (~7/d) |
| 2026-04-13 | POW-CRE-217 | 1,030 | ×29 | normal (~17/d) |
| 2026-04-16 | POW-ENE-484 | 1,001 | ×29 | normal (~1/d) |

Plus the Mar deductions already flagged: POW-MIL-193 (1,020 on 19 Mar), POW-FRO-001 (1,014 on 29 Mar), POW-HEA-641 (402 on 27 Mar), POW-CRI-762 (400 on 14 Apr).

**Running total of unexplained colour deductions: ~31,500 units** (up from ~22,090 on 17 Apr).

These are NOT Shopify sales — Shopify shows normal rates on the same days. Possible causes: stock adjustments, transfer events, work-order consumption, or data-entry error. Katrina's promised response (EOD Fri 18 Apr) never came. **Escalate.**

**Working assumption for this check:** use Shopify DSR (not 3PL) for these 10 SKUs. They all have 100+ days of real cover, not the 5–25d the 3PL rate suggests.

Also worth noting: the Mar ACC-RE5-BOT/LID/INN ~15,000-unit deductions are **explained** — those are the Remove 500ml bottle/inner/lid transfers to OP for the fill now finishing. Keep those off the anomaly list.

---

## CONTAINER / ORDER STATUS

### AUS 09052026 (JS21-20260303-1)
- POS MODEL: In Production, Est. Completion 30 Apr, Est. Arrival 30 May
- Slack: B114 jars finishing 20 Apr. Sally needs ~10 days fill + pack → Lily shipping 10 May-ish
- Recap (17 Apr): decision = B114 (Joel), on track
- **Action:** WeChat ping Lily this week to confirm fill window start.

### AUS 07062026 (JS21-20260326-1, Birthday Sale)
- POS MODEL: In Production, Est. Completion 16 May, Est. Arrival 15 Jun. **Growth factor 1.4x** (per Current Issues note)
- Deposit: ✅ paid
- **Note:** sheet shows 15 Jun arrival — a week later than 7 Jun in Upcoming Orders doc. Upcoming Orders needs updating post-review.

### AUS 08072026 — Fill PO place date 29 Apr (8 days away)
- POS MODEL: no status set yet, Est. Completion 15 Jun, Est. Arrival 15 Jul
- Per Upcoming Orders: "Not yet ordered. Contains Fire Collection colour restock."
- **Critical gaps (17 Apr flag still open):** 0 ACC-LAB, 0 ACC-THA, 0 ACC-BRU, 0 ACC-CUT-PRE on OL.
- **Action:** Daniel must review kit-mix + insert quantities before 29 Apr.

### AUS Powder Room (24-03-2026)
- Local fill. Sally sending powder + stickers to OP. Jar transfer G3PL → OP still not arranged.
- Joel 17 Apr: launch pushed to Mother's Day window (~early May) with Gav's campaign.
- **Action:** Joel + Gav lock Mother's Day date; Remy arrange G3PL→OP jar courier once date set.

### OP Remove 500ml fill (24-03-2026)
- POS MODEL: In Production, stale Exp 2 dates on sheet (14 Apr / 19 Apr)
- Reality (user-confirmed 21 Apr): 5,000 units being sent this week. Arrival to G3PL ~1–2 May.
- **Action:** Greg — update Exp 2 dates.

### Container #5 (unnamed)
- On sheet: Est. Completion 15 Jul, Est. Arrival 14 Aug. No reference, no OL yet.

---

## LOCAL FILL STATUS

### Outsource Packaging (Peter)
- **Remove 500ml fill in flight** — 5,000 units dispatching this week → G3PL ~1–2 May.
- **Heal fill PO — NOT PLACED** (flagged 13 Apr, now 8 days overdue). Daniel's 20 Apr plan: draft recommended PO 22 Apr.
- All ingredients for both fills are onsite at OP (acetone, calcium chloride, coconut oil, vitamin E — confirmed 15 Apr + 2 Apr).

### Avi Printing (ACC-LAB)
- **PO 11 closed** — 15,000 delivered 15 Apr, checked in 17 Apr. ACC-LAB now at 17,699.
- **Next Avi PO needed by mid-May** to avoid gap post-08072026 (more below).

---

## STOCK-OUT FORECAST — by container window

Framing per user preference (container-centric). Using actual 3PL DSR where Shopify aligns; Shopify DSR where 3PL is corrupted by anomalies.

### Window 1: now → AUS 09052026 arrival (30 May, 39 days away)

**STOCK OUT BEFORE ARRIVAL (gap < 0)** — actionable:

| SKU | Stock | DSR | Stocks out | Gap to 30 May | Resolution |
|---|---:|---:|---|---:|---|
| LIQ-BAS-2 | 604 | 20.7 (3PL) | ~20 May | **-10d** | ✅ Joel 17 Apr: express with Powder Room |
| LIQ-SEN-2 | 97 | 2.7 (3PL) | ~26 May | -4d | ✅ Joel 17 Apr: express with Powder Room |
| KIT-STA-2 | 1,165 | 30.8 (Shop) | ~28 May | -2d | ✅ Joel 17 Apr: substitute with Complete Kit |
| ACC-REM-BOW | 1,443 | 3.3 (Shop)* | — | +800d | ⚪ Joel 17 Apr: hold (was flagged at 38/d 3PL) |

\* Remove Bowl: 3PL deducts 38/d because BUN-1/BUN-2 bundles also deduct it. Real standalone demand ~3/d. 09052026 brings 6,840 — massive overstock incoming.

**TIGHT (gap 0–7d) — monitor:**

None once Window 1 overrides are applied. Heal cover hits ~58d at Remove fill arrival (1–2 May) which is safe for the window.

**NOTHING ON ORDER under 84d (flag only — investigation / local fill):**

- None critical after correcting the 10 anomaly SKUs above. All the "critical" colours from the raw forecast (POW-ENE, POW-JUS, POW-BRE, POW-DRE, POW-GOL, POW-CRE, POW-ROY) are false alarms driven by the mystery deductions.

### Window 2: AUS 09052026 → AUS 07062026 arrival (30 May → 15 Jun, 16 days)

Container delivers 2,016 STA, 3,052 COM, 1,036 ULT, 2,592 Base, 432 LOB, 1,296 Glow, 432 LOG, plus colours and accessories. All kit + liquid SKUs are replenished.

**Live risks in this window:**

- **POW-JUS-449 / POW-BRE / POW-GOL / POW-DRE / POW-CRE / POW-ROY** — the anomaly colours. Sheet forecast says they stock out 4–14 May; Shopify says 120–565d. **If the 3PL anomaly is real stock loss, these will genuinely stock out pre-07062026.** 07062026 brings 400 each. That's barely 2 months Shopify cover. **Need Katrina to explain the deductions BEFORE 07062026 arrives** — otherwise we don't know true inventory.

### Window 3: AUS 07062026 → AUS 08072026 arrival (15 Jun → 15 Jul, 30 days)

Container delivers 1,260 STA, 3,164 COM, 1,244 ULT + 11,200 ACC-THA + 2,000 Remove Bowl + 2,376 Base. No ACC-LAB, no ACC-INS, no ACC-CUT-PRE, no ACC-BRU.

- **ACC-LAB at 08072026 arrival:** starting 17,699 now / 194.5/d = 91d cover (→ stocks out ~21 Jul). 07062026 brings 0. 08072026 brings 0. Then nothing. So if the 08072026 fill PO is placed on time and no new Avi PO is in the pipeline, **ACC-LAB hits zero ~21 Jul (6 days after 08072026 arrives). Tight.**
  - **Recommendation:** place Avi PO for 20,000 ACC-LAB by mid-May 2026. Pushes next deadline to ~late Sep.
- **ACC-THA:** well-stocked across all three containers. Post-07062026 projection: ~63,000 units. Fine.

### Window 4: AUS 08072026 → container #5 (15 Jul → 14 Aug, 30 days)

- Container #5 unnamed, no OL data yet. Too early to analyse.

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (act today)
- **Place Heal fill PO with OP — 8 days overdue.** Recommended qty below in Local Fill Forecast.
- **Draft express PO for Base / LO Base / LO Glow with Powder Room dispatch** (Joel 17 Apr decision). Quantities:
  - Base: ~500 units (covers 10-day gap + 10-day buffer post-arrival)
  - LO Base: ~100 units
  - LO Glow: ~100 units (optional — 181 units already covers to 19 May; but Joel wants express)
- **Escalate mystery colour deductions to Katrina** — now 10 SKUs, ~31,500 units, no reply since her EOD Fri 18 Apr commitment.

### 🟡 WARNING (act this week)
- **AUS 08072026 kit-mix review** (Daniel, by 29 Apr): reduce COM/ULT at 0.74x actual rate, bump STA, add 20,000 ACC-LAB + 20,000 ACC-THA, add ACC-BRU + ACC-CUT-PRE (unless Sally default-adds for kits).
- **Greg updates POS MODEL Exp 2 dates** for OP Remove 500ml (real dates ~24 Apr complete / ~1 May arrival).
- **ShipHero product-name corruption** — stalled since 16 Apr. Daniel to pick a workaround this week.
- **OP fill timing ping Peter** — confirm actual dispatch day for Greg's sheet update.

### 🟢 MONITOR (FYI)
- **Blue Moon (POW-BLU-ZGD22)** — 497 units at G3PL, OOS on site. Unconfirmed if relisted since 17 Apr.
- **Fire Collection listings** — 7 colours showing ~6.5/d 3PL and 0 Shopify. Likely a listing issue, not demand.
- **STO-BUB-BAG-L** — one day (06 Apr) 14 units over benchmark. Not escalating.
- **Cascading overstock signal** — COM, ULT, Remove Bowl all post-arrival cover >200d. Flag for 08072026 sizing.

---

## LOCAL FILL FORECAST

### Heal fill (LIQ-HEA-5) — OP

- Lead time: **58d** (21d ingredients → 30d fill → 7d ship, ingredients already on site so starts at filling phase ≈ ~37d if sent today)
- Actually: per Lead Times file, OP total from all ingredients-on-site = 28d (14d filling + 7d ship). Using 28d for recommended.
- Current stock: 10,449 | 3PL actual rate: 123.7/d
- Stock at delivery (if placed 22 Apr, delivered 20 May): 10,449 − (28 × 123.7) = **6,985 units**
- Stock at delivery if placed 29 Apr (one week slip): 10,449 − (35 × 123.7) = **6,120 units**

| Fill Qty | Post-fill stock | Cover @ 123.7/d (3PL) | Cover @ 184.6/d (1.3x model) |
|---:|---:|---:|---:|
| 10,000 | 16,985 | 137d | 92d |
| 12,000 | 18,985 | 154d | 103d |
| **15,000 (recommended)** | 21,985 | 178d | 119d |
| 18,000 | 24,985 | 202d | 135d |

**Recommendation: 15,000 units.** Lines up well against Heal's position — no container inbound for this SKU ever, OP is the only source. 15k provides ~6 months of cover which matches typical OP cycle.

### Remove 500ml fill — OP (already placed — current fill)

- Current fill: 5,000 units arriving ~1–2 May
- Post-fill stock: 3,507 + 5,000 − (10 days × 52.3) = 8,000
- Cover at 52.3/d post-fill: **153d** → next fill needed by mid-Sep at 28d lead = place mid-Aug
- No urgency. Peter + Daniel already discussing 1000L IBC sizing for future supply (20 Apr).

---

## PO RECOMMENDATIONS

| SKU / PO | Place by | Action |
|---|---|---|
| **Heal fill (OP, ~15,000)** | **22 Apr (this week)** | Draft today. 8 days overdue. |
| **Base / LO Base / LO Glow express (Sally via Lily)** | **22 Apr this week, with Powder Room** | Joel 17 Apr decision. Daniel to draft. |
| **AUS 08072026 Fill PO** | 29 Apr (Sally, 8 days) | Review kit qtys at 0.74x actual + add ACC-LAB/THA/BRU/CUT-PRE. |
| **Next Avi ACC-LAB PO (20,000)** | ~15 May | Prevent ~21 Jul gap after 08072026 arrival. |
| **Next OP Remove 500ml fill** | ~15 Aug | Plenty of cover until then. |

---

## CASCADING ARRIVAL PROJECTION

Target cover band: 45–75 days. DSR = 3PL 14d rate where reliable, Shopify where 3PL is anomaly-corrupted.

### Kits (at 3PL rate)

| SKU | Now | After 09052026 (30 May) | After 07062026 (15 Jun) | After 08072026 (15 Jul) |
|---|---:|---:|---:|---:|
| KIT-STA-2 | 1,165 / 38d | +2,016 → 1,977 / 64d | +1,260 → 2,744 / 89d | +1,372 → 3,191 / 104d ⚠️ |
| KIT-COM-4 | 4,878 / 81d | +3,052 → 5,570 / 92d | +3,164 → 7,825 / 129d ⚠️ | +3,192 → 9,201 / 152d ⚠️ |
| KIT-ULT-6 | 2,867 / 118d | +1,036 → 2,955 / 122d ⚠️ | +1,244 → 3,856 / 159d ⚠️ | +1,428 → 4,554 / 188d ⚠️ |

⚠️ = post-arrival cover exceeds 100d — **overstock risk at 0.74x actual run rate**. Mostly driven by COM + ULT OLs being sized at 1.3x.

### Liquids / Remove

| SKU | Now | After 09052026 | After 07062026 | After 08072026 |
|---|---:|---:|---:|---:|
| LIQ-BAS-2 | 604 / 29d (gap -10d) | ~2,592 / 125d ⚠️ (assuming express bridges) | +2,376 / 217d ⚠️ | +1,944 / 229d ⚠️ |
| LIQ-HEA-5 | 10,449 / 84d | +15,000 fill → ~21,985 / 178d ⚠️ | no inbound → ~15,180 / 123d ⚠️ | no inbound → ~11,470 / 93d |
| ACC-REM-500 | 3,507 / 67d | +5,000 fill (1-2 May) → 8,000 / 153d ⚠️ | no inbound → ~7,000 / 134d ⚠️ | no inbound → ~5,440 / 104d ⚠️ |
| ACC-REM-BOW | 1,443 / 38d | +6,840 → ~6,800 / 179d ⚠️ | +2,000 → ~8,230 / 217d ⚠️ | +2,640 → ~9,730 / 256d ⚠️ |

### Inserts

| SKU | Now | After 09052026 | After 07062026 | After 08072026 |
|---|---:|---:|---:|---:|
| ACC-LAB | 17,699 / 91d | +0 → ~10,100 / 52d | +0 → ~7,180 / 37d | +0 → ~1,340 / **7d** 🔴 |
| ACC-THA | 32,089 / 165d | +30,800 → ~55,300 / 285d ⚠️ | +11,200 → ~63,650 / 327d ⚠️ | +0 → ~57,810 / 297d ⚠️ |
| ACC-INS | 19,020 / 161d | +5,280 → ~19,685 / 166d ⚠️ | +6,720 → ~24,090 / 203d ⚠️ | +5,280 → ~26,120 / 220d ⚠️ |

### Delay scenarios

- **If AUS 09052026 slips 10 days** (arriving 9 Jun instead of 30 May):
  - LIQ-BAS-2 gap widens from 10d → 20d. Express must cover 20d not 10d.
  - LIQ-SEN-2 gap widens from 4d → 14d.
  - KIT-STA-2 gap 2d → 12d. Complete Kit substitution must cover 12d.
  - No other SKUs move into critical — 3PL rate keeps them fine.

- **If OP Heal fill slips 2 weeks** (delivered early Jun instead of 20 May):
  - Heal burndown at 123.7/d: 10,449 − 60 × 123.7 = 3,027 at delivery. Still above zero. **Tolerable but tight.**
  - If fill slips 30 days (placed mid-May): burndown 10,449 − 90 × 123.7 = **-680. OOS briefly.** Don't let this slip.

### Overstock flags (post-09052026 and beyond)

At 0.74x actual kit rate and 0 in-kit standalones:
- **COM-4**: post-08072026 cover 152d vs 60d target. ~4,600 excess units.
- **ULT-6**: post-08072026 cover 188d vs 60d target. ~2,650 excess units.
- **Remove Bowl**: 256d vs 60d. ~7,700 excess.
- **Heal**: 178d vs 75d after next fill. Can re-size next fill smaller.

**Recommendation: scale AUS 08072026 kit OL down ~25–30%** (from 1.3x to 0.95–1.0x) or delay and reduce container size. This is the call Daniel needs to make by 29 Apr.

---

## FOLLOW-UP ITEMS

### Immediate (today–tomorrow)
- [ ] Draft Heal fill PO (~15,000 units) → email Peter
- [ ] Draft Base / LO Base / LO Glow express (Sally via Lily WeChat) → ~500 / 100 / 100 units
- [ ] Escalate colour deduction anomalies to Katrina (now 10 SKUs, ~31,500 units)
- [ ] Ping Peter for actual 500ml fill dispatch day

### By end of month
- [ ] Daniel: AUS 08072026 kit + insert quantity revision by 29 Apr
- [ ] Place next Avi ACC-LAB PO (~20,000) ~15 May
- [ ] Greg: POS MODEL Exp 2 date correction for OP Remove 500ml
- [ ] ShipHero name sync decision with Jake

### Ongoing
- [ ] Verify Fire Collection + Blue Moon Shopify listings live
- [ ] Monitor W16 kit rate vs W15 recovery — next full week data arrives Mon
