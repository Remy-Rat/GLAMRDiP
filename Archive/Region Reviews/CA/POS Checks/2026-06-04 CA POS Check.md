# 🇨🇦 CA POS Model Check — 4 Jun 2026

## DATA FRESHNESS & MANUAL OVERRIDES

- **POS MODEL re-pulled from Drive:** 4 Jun 2026 12:38 AEST
- **3PL (B360) last valid date:** 2026-06-04 — current
- **Growth factor (sheet):** 2.0x — Kit DSR base 69/d → scaled 138/d (STA 9 + COM 47 + ULT 13)
- **Sheet `UPDATED` cell:** None detected — Greg paste discipline issue (carried)
- **Per-container growth factor:** Sheet does not surface; treat all containers at 2.0x unless otherwise noted

**Manual overrides applied:**
- **CA 21062026 Est. Arrival:** sheet shows **22 Jul** → use **1 Jul** (Lily vessel confirmed 13 May: closes 1 Jun / sails 5 Jun / ETA port 30 Jun / ETA warehouse 1 Jul). Greg still owes the sheet update.
- **CA 21062026 Linda-fill items:** sheet shows 5,000 Coffin + 1,500 Square + 200 Stiletto + 1,000 Ballerina + 1,000 Almond + 1,100 Mani Mat = 9,800 units inbound 1 Jul. **User-confirmed 4 Jun: Linda NOT making it on this container.** Treat all six items as **ZERO on 1 Jul** and ride the next supply window.
- **Swift fill (14-05-2026):** sheet status `Ordering`. **User-confirmed 4 Jun: Joel paid, Greenfield ingredients ARRIVED. Production can start now.** Treat as `In Production — clock starts 4 Jun`.
- **CA 30082026 nail mat:** Greg reduced 10,000 → 200 in PO update (Group DM today). No model impact yet.

---

## TL;DR — THE TWO HARD DATES YOU ASKED FOR

### ACC-REM-500 (Remove 500ml) — OOS gap is unavoidable

| Metric | Date |
|---|---|
| Current stock (B360) | **507 units** |
| Burn rate (3PL 14d) | **90/d** (Shopify 87/d + bundle uplift) |
| **OOS at 247** | **Tue 9 Jun** (5 days from today) |
| Need-at-247 date (3d buffer) | Sat 6 Jun — **already infeasible** |
| Swift FedEx pickup needed by | Sun 31 May — **passed** |
| Realistic Swift arrival at 247 | **Mon 23 Jun – Thu 2 Jul** (Greenfield arrived 4 Jun → 14-21d prod → 5-7d transit) |
| **OOS GAP** | **14-23 days** |

### LIQ-HEA-5 (Heal) — Safe, same Swift fill covers it

| Metric | Date |
|---|---|
| Current stock (B360) | **4,751 units** |
| Burn rate (3PL 14d, kit-adjusted) | **108.3/d** |
| **OOS at 247** | **Fri 17 Jul** (43 days from today) |
| Need-at-247 date (3d buffer) | Tue 14 Jul |
| Swift FedEx pickup needed by | Wed 8 Jul |
| Realistic Swift arrival at 247 | Mon 23 Jun – Thu 2 Jul |
| **Margin** | **15-24 days BEFORE OOS** ✅ |

**The whole picture:** The 14-05-2026 Swift fill (6,500 Heal + 9,000 Remove 500ml + 1,000 Remove 120ml) is one batch arriving **23 Jun – 2 Jul** (Greenfield landed today, Swift can start now). Heal is fine. Remove 500ml has a 14-23 day OOS window. The only remaining lever is:
- **Switch CA upsell from Remove 500ml → Remove 120ml** (3,782 stock / 449d cover — Daniel flagged 27 May; user 4 Jun: "hasn't switched yet but we can"). Switching now cuts demand on 500ml to near zero standalone, narrowing OOS impact materially. Each day of delay on the switch = +1d effective OOS.
- Otherwise: accept the 14-23 day OOS and run backorder messaging — no express bridge available (Swift production is the constraint, not transit).

---

## STOCK POSITION — KITS & LIQUIDS (4 Jun)

| SKU | Stock | Projected DSR (2.0x) | Cover @ Proj | Actual DSR (3PL 14d) | Cover @ Actual |
|---|---:|---:|---:|---:|---:|
| KIT-STA-2 | 3,847 | 18 | 214d | 11.4 | 339d ⚠️ |
| KIT-COM-4 | 5,942 | 94 | 63d | 71.1 | 84d |
| KIT-ULT-6 | 2,613 | 26 | 101d | 23.2 | 113d |
| **Kits total** | **12,402** | **138** | **90d** | **105.7** | **117d** |
| LIQ-HEA-5 | 4,751 | 142 | 33d | 108.3 (kit-adj) | **44d** |
| LIQ-BAS-2 | 1,151 | 14 | 82d | 10.8 | 107d |
| LIQ-GLO-4 | 1,385 | 8 | 173d | 5.4 | 255d ⚠️ |
| LIQ-SEA-3 | 857 | 12 | 71d | 9.0 | 95d |
| LIQ-BON-1 | 917 | 6 | 153d | 3.5 | 262d ⚠️ |
| LIQ-SOA-6 | 830 | 4 | 208d | n/a | — ⚠️ |
| LIQ-MAT-4 | 1,154 | 6 | 192d | n/a | — ⚠️ |
| LIQ-SEN-2 | 638 | 8 | 80d | 4.2 | 151d |
| LIQ-SEN-4 | 532 | 6 | 89d | 4.0 | 133d |
| ACC-REM (120ml) | 3,782 | 10 | 378d | 8.4 | 449d ⚠️ |
| **ACC-REM-500** | **507** | **121** | **4d** | **90.0** | **6d** 🔴 |
| ACC-REM-BOW | 5,137 | 30 | 171d | 12.7 | 404d ⚠️ |

⚠️ = >150d cover (overstock relative to 45-75d target — see [[growth-factor-framing]])
🔴 = <14d cover at actual rate (critical)

**Notes on rate divergences:**
- **KIT-COM-4** is the only kit running at "tight" by overstock standards: 84d at actual is reasonable given Birthday Sale window.
- **KIT-STA-2** still over-allocated. 339d cover at actual 11.4/d. 21062026 adds 672 + 25072026 adds more (not in this sheet yet for CA — needs separate confirmation). Per [[ca-offer-gift-card]] and [[aus-kit-substitution]] this is a STA→COM substitution candidate; revisit STA qty on future containers.
- **ACC-REM (120ml)** 449d cover — flag for trimming on next container, but useful as fallback if upsell flips off 500ml.

---

## STOCK POSITION — TIPS / FREE GIFT / OFFER POOL

⚠️ **CA 21062026 Linda-fill items LOST per user 4 Jun. Cover below excludes them.**

| SKU | Stock | Model DSR | Cover | Risk |
|---|---:|---:|---:|---|
| ACC-NAI-MAT (Mani Mat) | **0** | — | OOS now | Already swapped out of offer. CA 30082026 brings 200 (Aug). Otherwise no inbound. |
| ACC-TIP-COF (Coffin) | 123 | 2 (model)* | ~60d at model, much shorter if offer active | No inbound; was Linda-fill on 21062026 → DROPPED. |
| ACC-TIP-SQU (Square) | 186 | 4 (model)* | ~46d | Was Linda-fill → DROPPED. |
| ACC-TIP-STI (Stiletto) | 398 | 2 (model)* | ~199d | Was Linda-fill → DROPPED. Low burn. |
| **ACC-TIP-BAL (Ballerina)** | **424** | **4 (model)*** | **~106d at model** | **CURRENT OFFER TIP** per Daniel 27 May. At actual offer burn (10-20/d if attach-mode), cover could be 20-40d. Was Linda-fill → DROPPED. |
| ACC-TIP-ALM (Almond) | 2,478 | 148.4 (model)** | 17d | Greg's model DSR clearly broken (148/d unrealistic). Actual likely 5-10/d → 250-500d. Was Linda-fill → DROPPED. |
| TRA-BAG (Travel Bag) | not in POS MODEL | — | — | Was AUS swap candidate; verify CA stock separately. |

\* Model DSR is at low standalone level — does not reflect offer-attach burn  
\** Greg DSR error — review

**Critical inference:** Ballerina is the active offer tip; 424 stock with no Linda restock until 30082026 (or later, if Linda capacity issue persists) = an offer-mix change is likely needed mid-cycle. Worth raising the question now whether the offer should rotate to gift-card-only or stick with Ballerina until depletion.

---

## STOCK POSITION — PACKAGING & INSERTS

| SKU | Stock | Deduction/d (14d) | Cover | Benchmark | Anomaly Days |
|---|---:|---:|---:|---:|---:|
| STO-BUB-BAG-L | 5,723 | 106.1 | 54d | 435 | 0 |
| STO-BUB-BAG-S | 0 | 0 | — | — | 247-supplied, not monitored |
| STO-MAI-BAG-S | 8,838 | 43.6 | 203d | 330 | 0 |
| STO-MAI-2 | 8,878 | 43.6 | 203d | 330 | 0 |
| ACC-INS | 19,840 | 103.9 | 191d | 435 | 0 |
| ACC-THA | 30,066 | 147.5 | 204d | 735 | 0 |
| **ACC-LAB-CA** | **0** | 0 | — | 735 | NaN deduction rule unchanged (Greg) |

**ACC-LAB-CA:** 0 stock shown but per Recap 14 May ACC-LAB-CA on hand was 6,878 + 1,300 reprint + 10k Mixam inbound. Sheet not updated. Per [[reference_google_drive_sheets]] this is a recurring Greg fix-needed item — **manual override:** treat as ~6,878 (last known) until Mixam MX2041057 lands.
- **Mixam MX2041057:** 20,000 units. ETA per Mixam email 3 Jun: ship date "Wed Jun 3" (today's email). If shipped today → ~14d to 247 → arrival ~18 Jun.

---

## STOCK-OUT FORECAST

### 🔴 Stockout before next restock (gap < 0)

| SKU | Stock | Burn | OOS | Next restock | Gap |
|---|---:|---:|---|---|---|
| ACC-REM-500 | 507 | 90/d | **Tue 9 Jun** | Swift fill 23 Jun – 2 Jul | **-14 to -23 days** |
| ACC-NAI-MAT | 0 | offer-driven | already OOS | CA 30082026 1 Sep | **-90 days** (acceptable, offer swapped) |
| ACC-TIP-BAL | 424 | uncertain offer-attach | est 20-40d at offer burn | CA 30082026 1 Sep | possibly **-50 to -70 days** if Linda gap persists |

### 🟡 Tight (gap 0-14 days)

None for confirmed stock + confirmed restock.

### Heal cover under W22 slowdown

At current 108.3/d kit-adjusted: **17 Jul** OOS. Swift fill lands 27 Jun – 6 Jul → 11-20d buffer. **Safe.**

If kit DSR recovers back toward 138/d projected, Heal kit-adjusted rate would climb to ~140/d → cover drops from 44d to ~34d → OOS ~8 Jul → 2-11d buffer. Still safe but margin thinner. Watch W23 trend.

### Nothing on order, no risk (cover > 100d at actual)

22 of the 28 monitored SKUs sit at 100d+ cover at actual rate. Per [[growth-factor-framing]], don't recommend cutting orders pre-emptively — note as overstock observation only.

---

## CONTAINER / ORDER STATUS

| Reference | Sheet says | Reality (user-confirmed 4 Jun) | Action |
|---|---|---|---|
| **14-05-2026 Swift Fill** | Ordering | **Paid, fill underway, Greenfield-gated** | Remy chase Greenfield ETA today |
| **CA 21062026** (Birthday Sale, 40HQ) | In Production, completion 28 May, arrival 22 Jul | **Near completion, nearly shipping. Arrival 1 Jul via Lily.** Linda tip items DROPPED. | Greg update sheet arrival 1 Jul. Daniel decide tip routing. |
| CA 25072026 | (sheet column unclear, likely Ordering→Placed) | **Placed, numbers in** (user 4 Jun) | Greg verify sheet status; sizing review carried |
| **CA 30082026** | Ordering, completion 6 Jul, arrival 30 Aug | **Placed 27 May**, 40HQ at 2x DSR. NO new colours per Daniel 2 Jun. Free-gift qty (min 10k) pending Joel sign-off. | Joel: free-gift + colour sign-off. Sally: rectify colour additions. |
| CA 29092026 | Ordering, completion 5 Aug, arrival 29 Sep | Placeholder (per group DM with Greg/Daniel today, set to "Planned" so doesn't double-count stock) | — |
| 14-05-2026 Mixam | Ordering | In production. Ship date Wed 3 Jun per Mixam email today. | Remy confirm tracking |

---

## LOCAL FILL STATUS

### Swift Innovations (14-05-2026) — Heal + Remove 500ml + Remove 120ml

| | |
|---|---|
| Status | Paid; ingredients arrived 4 Jun; production can start |
| Greenfield delivery | ✅ Arrived (user 4 Jun) |
| Swift production lead | 14-21 days from 4 Jun |
| Swift completion window | **Thu 18 Jun – Thu 25 Jun** |
| Transit Swift → 247 | 5-7 days |
| **Arrival at 247 window** | **Mon 23 Jun – Thu 2 Jul** |
| Contents | 6,500 LIQ-HEA-5 + 9,000 ACC-REM-500 + 1,000 ACC-REM + 30,000 STO-BUB-BAG-L (note: large bubble mailer addition) |

### Next Swift fill (placement timing)

Cover after this Swift fill lands (use mid-point 1 Jul):

```
Heal:          4,751 - 27d × 108.3 = 1,827 remaining at 1 Jul + 6,500 = 8,327 → 77d cover → next OOS ~16 Sep
Remove 500ml:    0 (OOS 9 Jun) + 9,000 at 1 Jul → 100d cover at 90/d → next OOS ~9 Oct
Remove 120ml: 3,782 - 27d × 8.4 = 3,555 + 1,000 = 4,555 → 542d (extreme overstock)
```

Next Swift PO place-by date (Swift lead 14d prod + 5-7d transit ≈ 20d, plus ingredient lead ~10d = ~30d):
- **For Heal:** restock by 16 Sep → place by ~17 Aug
- **For Remove 500ml:** restock by 9 Oct → place by ~9 Sep

So **next Swift fill placement window: mid-August**, sized to one full Swift cycle ahead at current rate.

---

## CASCADING ARRIVAL PROJECTION

### Kits — all 3 SKUs at actual 105.7/d combined

| | NOW | After 21062026 (1 Jul) | After 25072026 (~30 Aug)* | After 30082026 (30 Aug) |
|---|---:|---:|---:|---:|
| Kit stock | 12,402 | 12,402 – 27d×106 + 3,668 = 13,210 | + ~5,400 placeholder = ~18,610 | + 4,256 COM = ~22,866 |
| Cover | 117d | 125d ⚠️ | 176d ⚠️ | 216d ⚠️ |

\* 25072026 sizing user-confirmed placed; manifest needs sheet refresh

All three arrivals push kit cover well above 100d target. At W22 actual rate (-25%) this is a slow-walking overstock; per [[growth-factor-framing]] surface as observation, not action.

### Remove / Heal — at actual rates

| | NOW | After Swift Fill (~1 Jul) | After CA 30082026 (30 Aug) |
|---|---:|---:|---:|
| LIQ-HEA-5 | 4,751 / 44d | 8,327 / 77d | 8,327 (no Heal in 30082026) |
| ACC-REM-500 | 507 / 6d | 9,000 / 100d (OOS 9–~27 Jun first) | 9,000 (no 500ml in 30082026) |
| ACC-REM | 3,782 / 449d | 4,555 / 542d | 4,555 (no 120ml in 30082026) |

CA 30082026 has Remove 500ml COMPONENTS (20k bottles/lids/inners) but no finished Remove 500ml — those bottles feed the NEXT Swift fill cycle.

---

## WHAT NEEDS ACTION

### 🔴 CRITICAL (today)

1. **Joel/Daniel: switch CA upsell Remove 500ml → 120ml NOW.** User 4 Jun: "hasn't switched yet but we can". With OOS in 5 days at current 90/d burn and Swift restock 14-23 days post-OOS, the switch is the only remaining lever to materially shrink the impact window. ACC-REM (120ml) has 3,782 stock = 449d cover (plenty of supply for upsell role). Every day's delay on the switch = +1d of 500ml burn against tiny stock.
3. **Daniel: scope CA 21062026 tip routing.** Linda tips not making this container. Two options: (a) chase Linda for separate dispatch to 247 mid-Jun to ride alongside arrival, (b) push to CA 30082026 and accept 60-day delay on offer-attached SKUs (Ballerina is current offer tip — direct impact).

### 🟡 THIS WEEK

4. **Joel: sign off CA 30082026 free-gift qty (min 10k) + 6-12 new colour collections.** Daniel re-flagged 2 Jun. Container Sally lead is 5-6 weeks; window closes for new SKU additions in days.
5. **Sally: rectify CA 30082026 — confirm new colour collections added.** User 4 Jun: "might be added, should be in slack but that's as far as we got". Verify against PO before Sally locks production.
6. **Daniel: decide on Ballerina tip mid-cycle offer rotation.** 424 stock at offer burn likely depletes mid-late June. No restock until 30082026 (Sep) unless Linda recovers.
7. **Greg: sheet hygiene.** Update CA 21062026 ETA 22 Jul → 1 Jul. Fix ACC-LAB-CA NaN deduction rule. Refresh stale DSRs (CA liquids 3-8x overstated standalone; Almond 148/d model is broken).

### 🟢 MONITOR

8. **W22 kit selling at -25% vs 2x scaled.** If W23 holds at -25%, CA 30082026 at 2x is exposed. Per [[growth-factor-framing]] — observe, don't pre-emptively downsize.
9. **Mixam MX2041057 (20k booklets) ship today.** Confirm tracking, ETA 247 ~18 Jun.
10. **POW-CLE-193 + POW-JUS-449 deduction streak.** 8+ days at 4-6x benchmark of 35 (147 on 1 Jun). Colour offer pool still pulling. Stock 10,940 + 10,600 in 21062026 + 10,600 in 30082026 = comfortably resourced.

---

## NEXT-FILL SIZING (for record — not for action this cycle)

When Swift fill #2 placement comes (mid-August window):

| Qty (lean) | Qty (recommended) | Qty (conservative) | Cov @ 1.5x post-fill | Cov @ actual post-fill |
|---:|---:|---:|---|---|
| Heal | 6,500 | 8,500 | 10,500 | 60-80d / 65-95d |
| Remove 500ml | 6,500 | 9,000 | 11,000 | 70-90d / 75-120d |
| Remove 120ml | 0 | 0 | 0 | ACC-REM is at 542d — no fill needed |

Sized to one full Swift cycle (~30d total ingredient + production + transit) plus buffer. Reconsider sizing once W23-W24 kit rate confirms or contradicts the W22 slowdown trend.
