# POS MODEL CHECK — CA — 15 Apr 2026

## DATA FRESHNESS

- **POS MODEL updated:** date not detected
- **3PL data last valid:** 15 Apr 2026 (today)
- **Shopify latest:** 13 Apr 2026 (2d ago)
- **Growth factor:** 2.0x (Base 80/d → Scaled 160/d)
- **ShipHero exports:** None provided. 247 uses ShipHero but no CSV exports available. Running on POS MODEL + 3PL tab only — no confirmed vs pending split.

**GROWTH FACTOR IS MASSIVELY OVERSTATED.**
Model assumes 2.0x → 160 kits/day. Actual 14d selling: 52.6 kits/day (0.66x). Recommended: 0.72x (actual + 10% buffer). **Every POS MODEL days cover figure is ~3x too optimistic.** All analysis below uses actual rates alongside model rates.

---

## STOCK POSITION

Running without ShipHero — POS MODEL ON HAND used as stock source. No confirmed/pending/quarantined split available.

### Kits

| SKU | Name | On Hand | Model DSR | Model Cover | Actual DSR | Actual Cover |
|---|---|---|---|---|---|---|
| KIT-STA-2 | Starter | 2,477 | 42.0 | 59d | 14.8 | 167d |
| KIT-COM-4 | Complete | 3,779 | 82.0 | 46d | 27.4 | 138d |
| KIT-ULT-6 | Ultimate | 852 | 36.0 | 24d | 10.4 | 82d |

Kits are healthy at actual rates. ULT-6 is the tightest at 82d but CA 03022026 has +2,660 inbound (held at customs).

### Liquids

| SKU | Name | On Hand | Model DSR | Model Cover | Actual DSR | Actual Cover | Flag |
|---|---|---|---|---|---|---|---|
| LIQ-HEA-5 | Heal | 1,547 | 170.0 | 9d | 54.2 (kit-adj) | 29d | CRITICAL — Swift fill arriving ~18-20 Apr |
| LIQ-BAS-2 | Base | 1,618 | 34.0 | 48d | 11.7 | 138d | OK |
| LIQ-SEA-3 | Seal | 1,227 | 24.0 | 51d | 8.6 | 143d | OK |
| LIQ-GLO-4 | Glow | 1,642 | 20.0 | 82d | 6.3 | 261d | OK |
| LIQ-BON-1 | Bond | 877 | 16.0 | 55d | 3.6 | 244d | OK |
| LIQ-SEN-2 | Sensitive Base | 603 | 8.0 | 75d | 4.9 | 123d | OK |
| LIQ-SEN-4 | Sensitive Glow | 453 | 6.0 | 76d | 3.4 | 133d | OK |
| LIQ-MAT-4 | Matte | 868 | 14.0 | 62d | 4.6 | 189d | OK |
| LIQ-SOA-6 | Soak | 338 | 16.0 | 21d | 4.0 | 85d | WARNING — model overstated |

All liquids are fine at actual selling rates. Heal is the only one needing action and the fill is arriving this week.

### Remove Products

| SKU | Name | On Hand | Model DSR | Model Cover | Actual DSR | Actual Cover | Flag |
|---|---|---|---|---|---|---|---|
| ACC-REM-500 | Remove 500ml | 0 | 0 | OOS | 0 (OOS effect) | OOS | Swift fill 3,654 arriving ~18-20 Apr |
| ACC-REM | Remove 120ml | 4,421 | 62.0 | 71d | 25.1 | 176d | OK |
| ACC-REM-BOW | Remove Bowl | 1,420 | 80.0 | 18d | 18.5 (3PL) | 77d | Model DSR overstated (see below) |

**ACC-REM-BOW model DSR (80/d) vs actual 3PL deduction (18.5/d).** The model DSR is massively inflated. Actual demand is ~18.5/d — driven by bundle sales (ACC-REM-BUN-1 = 120ml+Bowl, ACC-REM-BUN-2 = 500ml+Bowl). Shopify only shows 4.9/d because it records bundle SKUs, but 3PL deducts the component bowl per bundle. Greg should update to ~20/d.

**ACC-REM model DSR (62/d) vs Shopify (25.1/d) vs 3PL (41.1/d).** 3PL deducts faster because bundle sales (ACC-REM-BUN-1) consume 1x ACC-REM + 1x ACC-REM-BOW per sale, but Shopify only shows the bundle SKU. True demand including bundles: ~41/d.

---

## CONTAINER / ORDER STATUS

### CA 03022026 + CA 07042026 — HELD AT CUSTOMS
- **POS MODEL:** On the Way, Est. Arrival: 2 Apr 2026
- **Reality:** 13 days past ETA. **Container not paid for customs release** (per Remy, 15 Apr).
- **Contents:** 94,268 units across 104 SKUs (combined)
  - Kits: STA +1,988, COM +4,788, ULT +2,660
  - ACC-REM-BOW: +7,140
  - ACC-INS: +10,080
  - ACC-THA: +8,400
  - ACC-NAI-WIP: +836 (currently at 45 units / 8d cover)
  - LIQ-SOA-6: +648 (216 on CA 03022026 + 432 on CA 07042026)
  - LIQ-MAT-4: +432
  - Plus 80+ colour SKUs
- **ACTION: Joel must pay customs/duties to release. Once released, 247 needs ~3-5 days to check in.**

### 31-01-2026 Swift Innovations Fill
- **POS MODEL:** In Production (STALE)
- **Reality:** Fill COMPLETE. 7,500 Heal + 3,654 Remove 500ml. Collection booked today (15 Apr). Delivery to 247 ~18-20 Apr.
- **POS MODEL OL:** 7,500 Heal + 3,950 Remove 500ml. Actual Remove fill was 3,654 (296 short — acetone ran out).

### 04-03-2026 CA Print Order (Mixam labels)
- **POS MODEL:** In Production (STALE)
- **Reality:** Arrived at 247. 8,700 of 10,000 received (1,300 short — confirmed by 247: 13x650 + 1x250).
- **DOUBLE-COUNT:** POS MODEL projected OH adds 10,000 OL to current stock. But 8,700 is ALREADY in the 9,400 on-hand figure. **ACC-LAB-CA projected OH overstated by ~8,700.**

### CA 21062026 (Birthday Sale)
- **POS MODEL:** In Production, Est. Completion: 21 May, Est. Arrival: 5 Jul
- **Reality:** Deposit needed (~22 Apr deadline). Sally waiting on bottles, B115 jars, deposit.
- **Growth factor on this shipment:** not set in POS MODEL

### CA 25072026
- **POS MODEL:** Ordering, Est. Completion: 22 Jun, Est. Arrival: 6 Aug
- **Not yet placed.** Contains Fire Collection colours + restock.

---

## CORRECTED DAYS COVER

At actual selling rates (not model 2.0x). Key items only.

### CRITICAL (<14d at model rate, needing immediate attention)

| SKU | Stock | Model DSR | Model Cover | Actual DSR | Actual Cover | Inbound | Action |
|---|---|---|---|---|---|---|---|
| LIQ-HEA-5 | 1,547 | 170.0 | 9d | 54.2 | 29d | Swift 7,500 arriving ~18 Apr | Monitor — restock this week |
| ACC-REM-500 | 0 | — | OOS | — | OOS | Swift 3,654 arriving ~18 Apr | Monitor — restock this week |
| ACC-NAI-WIP | 45 | 6.0 | 8d | 1.5 | 30d | Container +836 (customs) | Release container |
| POW-RAD-043 | 727 | — | — | 416.5 | 2d | CA 25072026 +200 (Aug) | See note below |

**POW-RAD-043 (Radiant):** The 416.5/d actual DSR is an artefact. The SKU went inactive on 10 Apr (Gav's rename), was reactivated 14 Apr, and 829 units were deducted on 11 Apr (red flag). Real demand is likely ~7-14/d based on the 14d Shopify rate. Ignore the 2d cover figure.

### WARNING (<30d at model rate)

| SKU | Stock | Model Cover | Actual Cover | Inbound | Note |
|---|---|---|---|---|---|
| KIT-ULT-6 | 852 | 24d | 82d | Container +2,660 | Fine at actual rate |
| LIQ-SOA-6 | 338 | 21d | 85d | Container +648 | Fine at actual rate |
| ACC-REM-BOW | 1,420 | 18d | 77d | Container +7,140 | Model DSR overstated (80 vs 18.5) |

---

## PACKAGING & INSERTS

| SKU | Stock | Ded/day | Cover | Benchmark | Flag |
|---|---|---|---|---|---|
| STO-BUB-BAG-L (Bubble Mailer) | 10,083 | 59.0 | 171d | 435 | OK — Zakka order ready but unpaid |
| STO-BUB-BAG-S (Liquid Pocket) | 0 | 0.0 | — | — | 247 supplies their own (per region config) |
| STO-MAI-BAG-S (Small Satchel) | 10,861 | 59.6 | 182d | 330 | OK |
| STO-MAI-2 (Small Box) | 10,902 | 59.6 | 183d | 330 | OK |
| ACC-INS (Instructions) | 14,036 | 55.0 | 255d | 435 | OK |
| ACC-THA (Thank You Card) | 27,959 | 111.3 | 251d | 735 | OK |
| ACC-LAB-CA (Labels Booklet) | 9,400 | — | ~85d* | 735 | OK — just restocked |

*ACC-LAB-CA deduction rate not yet stable (only back in stock since early April). Using ACC-THA rate (111.3/d) as proxy for total orders. At 111/d: 9,400 / 111 = 85d cover.

All packaging healthy. No urgency.

---

## CONTAINER ARRIVALS DETECTED (from 3PL data)

- **4 Mar:** 8 SKUs, +2,255 units. Top: POW-JUS-449 +796, POW-MON-005 +590. Likely reconciliation from the Feb cycle count discrepancy (247 returned some corrections).
- **3 Apr:** 9 SKUs, +14 units. Tiny — returns or small corrections.
- **NO large container check-in detected.** The CA 03022026 + CA 07042026 shipment (94,268 units) has NOT arrived at the 3PL.

---

## LOCAL FILL STATUS

### Swift Innovations — Heal + Remove 500ml (ref: 31-01-2026)

| Item | Ordered | Produced | Status |
|---|---|---|---|
| LIQ-HEA-5 (Heal) | 7,500 | 7,500 | Complete since ~25 Feb, held at Swift |
| ACC-REM-500 (Remove 500ml) | 3,950 | 3,654 | Complete 13 Apr. 296 short (acetone exhausted) |
| ACC-REM (Remove 120ml) | 0 | 0 | Removed from PO — ingredients reallocated to 500ml |

- **Collection:** Booked today (15 Apr), 10am-4pm. 4 pallets.
- **Transit:** ~3-5 days Swift → 247.
- **Restock at 247:** ~18-20 Apr.

### Post-Fill Projection

| SKU | Current | + Fill | = Total | Actual DSR | Post-Fill Cover |
|---|---|---|---|---|---|
| LIQ-HEA-5 | 1,547 | +7,500 | 9,047 | 54.2/d | 167d |
| ACC-REM-500 | 0 | +3,654 | 3,654 | ~12.3/d* | ~297d |

*Remove 500ml pre-OOS Shopify rate was 12.3/d (30d average). Post-restock demand may bounce back.

### Next Fill — On Hold
Joel said "hold for a little" (9 Apr) due to underselling + cash flow. Given the massive post-fill coverage (167d Heal, 297d Remove 500ml), no next fill is needed for months.

---

## STOCK-OUT FORECAST

### STOCKOUT BEFORE ARRIVAL

| SKU | Stock | DSR | Stocks Out | Next Inbound | Arrives | Gap |
|---|---|---|---|---|---|---|
| POW-GLA-CS02 (Glacier Glow) | 65 | 2.6 | ~10 May | CA 21062026 +800 | 5 Jul | -56d |
| POW-ORC-038 (Orchid) | 710 | 29.0 | ~9 May | CA 25072026 +200 | 6 Aug | -89d |
| POW-OPA-040 (Opal) | 744 | 18.3 | ~25 May | CA 25072026 +200 | 6 Aug | -73d |
| POW-BLO-042 (Blossom) | 726 | 18.2 | ~24 May | Nothing on order | — | — |
| POW-RED-165 (Red Mischief) | 1 | 5.9 | NOW | CA 25072026 +600 | 6 Aug | -113d |
| POW-GAR-656 (Garnet Games) | 9 | 5.7 | ~16 Apr | CA 25072026 +600 | 6 Aug | -112d |
| POW-BOR-355 (Bordeaux Nights) | 1 | 6.7 | NOW | CA 25072026 +600 | 6 Aug | -113d |

**Note:** POW-ORC-038, POW-OPA-040, POW-BLO-042 are all from the new colour collection that just launched. Demand is spiking (300%+ above 30d baseline). These will stock out in 3-6 weeks with no restock until August at earliest. Consider adding to CA 21062026 if not too late.

### NOTHING ON ORDER (no inbound)

| SKU | Stock | DSR | Stocks Out | Note |
|---|---|---|---|---|
| LIQ-HEA-5 | 1,547 | 54.2 | 13 May | Swift fill arriving ~18 Apr — will cover |
| ACC-LAB-CA | 9,400 | ~111 | ~mid-Jul | Print Order already received. Need new Mixam order before then |
| POW-BLO-042 (Blossom) | 726 | 18.2 | 24 May | New launch colour, nothing on any container |

### SAFE
204 SKUs with 45+ days cover at actual selling rates. Stock is abundant relative to demand.

---

## RED FLAG DEDUCTIONS

| Date | SKU | Deduction | Benchmark | Note |
|---|---|---|---|---|
| 2 Mar | ACC-RE5-INN | 9,999 | 100 | Component transfer to Swift for filling — EXPECTED |
| 11 Apr | POW-RAD-043 | 829 | 35 | SKU went inactive after rename — NOT real sales |
| 4 Mar | POW-FLO-024 | 206 | 35 | Reconciliation day (cycle count correction) |
| Multiple | POW-CLE-193 | 38-84/d | 35 | Clear is #1 colour. Genuinely high demand, not anomalous |

---

## SHOPIFY vs 3PL ALIGNMENT

**Kits: ALIGNED.** 3PL deductions match Shopify sales within 3 units/day. Data integrity is clean.

| SKU | 3PL Ded/d | Shopify/d | Gap | Status |
|---|---|---|---|---|
| KIT-STA-2 | 15.3 | 14.8 | +0.5 | ALIGNED |
| KIT-COM-4 | 30.6 | 27.4 | +3.2 | ALIGNED |
| KIT-ULT-6 | 11.5 | 10.4 | +1.1 | ALIGNED |

**Heal: 3PL FASTER (expected).** 3PL deducts 61.1/d vs Shopify 1.6/d standalone. The difference (59.5/d) is kit consumption — Heal is kit-adjusted. Aligns with 57.2 kits/d × 1 Heal per kit.

**Remove Bowl & Remove 120ml: 3PL FASTER (bundle effect).** 3PL deducts component SKUs per bundle sale. Shopify only records the bundle SKU. Gap is expected.

---

## WHAT NEEDS ACTION

### CRITICAL (act today)
- **Release container (CA 03022026 + CA 07042026).** 94,268 units, 104 SKUs, 13 days past ETA. Joel needs to pay customs/duties. This single action restocks the entire region.
- **POS MODEL growth factor: 2.0x → 0.72x recommended.** Every model forecast is ~3x overstated. This misleads ordering decisions. Greg to update.
- **POS MODEL shipment statuses stale.** Swift fill = "In Production" (complete). Mixam labels = "In Production" (received). CA 03022026/07042026 = "On the Way" (held at customs). Greg to update all.

### WARNING (act this week)
- **New colour collection stocking out.** Orchid (24d), Opal (41d), Blossom (40d), and 5 other new colours will stock out well before any container arrives. If CA 21062026 can still be amended, add these. If not, accept the gap.
- **ACC-LAB-CA next order.** 9,400 on hand, ~85d cover. Need to place next Mixam order within 2 months. Also chase Mixam on 1,300 unit shortfall from current order.
- **Zakka bubble mailers.** Joel: pay balance and confirm delivery address to 247. 18+ days overdue.
- **CA 21062026 deposit.** Deadline ~22 Apr. Sally waiting on this.

### MONITOR (FYI)
- Swift fill arriving ~18-20 Apr. Heal + Remove 500ml restocked. Long runway post-fill.
- ACC-REM-BOW model DSR overstated (80/d model vs 18.5/d actual). Greg to update.
- ACC-REM model DSR overstated (62/d model vs 41/d 3PL deduction). Bundle effect.
- POW-RAD-043 (Radiant) data artefact from SKU rename — ignore the 416/d "DSR."

---

## FOLLOW-UP ITEMS

### Immediate
- [ ] Joel: pay customs/duties to release CA 03022026 + CA 07042026
- [ ] Greg: update POS MODEL growth factor to 0.72x
- [ ] Greg: update shipment statuses (Swift = Completed, Mixam = Delivered, containers = Held)
- [ ] Greg: correct ACC-REM-BOW model DSR from 80/d to ~20/d

### By End of Month
- [ ] Joel: pay CA 21062026 Birthday Sale deposit (deadline ~22 Apr)
- [ ] Joel: pay Zakka bubble mailer balance + confirm delivery address
- [ ] Remy: chase Mixam on 1,300 unit ACC-LAB-CA shortfall
- [ ] Consider adding new colour collection to CA 21062026 if still possible

### Ongoing
- [ ] Monitor Swift fill delivery and 247 check-in (~18-20 Apr)
- [ ] Monitor container release and check-in once Joel pays
- [ ] Verify ACC-LAB-CA deduction rate once it stabilises (currently using ACC-THA as proxy)
