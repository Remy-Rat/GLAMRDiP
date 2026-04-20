# Component Map

## What's inside the kit from China

Kits arrive from Sally (Isay Nail) **pre-assembled** with liquids and accessories. The 3PL then adds locally-filled items, customer's colour choice, and inserts before shipping.

| Component inside kit from China | SKU         | Starter | Complete | Ultimate |
| ------------------------------- | ----------- | ------- | -------- | -------- |
| Deluxe Brush                    | ACC-BRU     | 1       | 1        | 1        |
| Cuticle Presser                 | ACC-CUT-PRE | 1       | 1        | 1        |
| Base                            | LIQ-BAS-2   | 1       | 1        | 1        |
| Seal                            | LIQ-SEA-3   | 1       | 1        | 1        |
| Bond                            | LIQ-BON-1   | 1       | 1        | 1        |
| Glow                            | LIQ-GLO-4   | 1       | 1        | 1        |

Sensitive Base (LIQ-SEN-2) and Sensitive Glow (LIQ-SOA-6) are sold separately — not included in any kit.

---

## What the 3PL adds per kit order

| Item added at 3PL   | SKU           | STA | COM | ULT | Notes                                              |
| -------------------- | ------------- | --- | --- | --- | -------------------------------------------------- |
| Heal                 | LIQ-HEA-5    | 1   | 1   | 1   | Filled locally — all regions                       |
| Powder colours       | POW-*         | 3   | 6   | 9   | Customer selects at checkout, 3PL picks from stock |
| Instructions         | ACC-INS       | 1   | 1   | 1   | Picked at 3PL — all regions                        |

Occasional bonus colours (1-3 extra) may be added to kits during promotions.

Colours show as individual Shopify line items even in kit orders (customer picks specific colours), so Shopify data already captures total colour demand — no kit-adjustment needed for colours in analysis.

## What the 3PL adds to ALL orders (kit or standalone)

| Item                | SKU     | Per order | Notes                              |
| ------------------- | ------- | --------- | ---------------------------------- |
| Product Info Booklet| ACC-LAB | 1         | Compliance — critical, can't miss  |
| Thank You Card      | ACC-THA | 1         | Insert                             |

## Packaging auto-deductions

| Rule                                             | Packaging                                          |
| ------------------------------------------------ | -------------------------------------------------- |
| Kit order (KIT-STA-2/COM-4/ULT-6 present)       | 1x STO-BUB-BAG-L (Bubble Mailer) per kit          |
| Non-kit order (per 9 total SKUs)                 | 1x STO-MAI-2 (Small Box) + 1x STO-MAI-BAG-S      |
| Individual liquid order                          | 1x STO-BUB-BAG-S (Bubble Wrap Liquid Pocket)      |

Note: outlier orders may require additional packaging. 3PL should have barcodes for the 3 packaging items at the workspace to scan when this occurs.

---

## Standalone items (NOT in kits)

- **ACC-REM** (Remove 120ml) — sold standalone or as a bundle with Remove Bowl
- **ACC-REM-500** (Remove 500ml) — sold standalone or as a bundle with Remove Bowl
- **ACC-REM-BOW** (Remove Bowl) — bundled with Remove products

## Other bundles at 3PL

| Bundle Name              | Bundle SKU    | Contains                                        |
| ------------------------ | ------------- | ----------------------------------------------- |
| Remove 120ml + Bowl      | ACC-REM-BUN-1 | ACC-REM + ACC-REM-BOW                           |
| Remove 500ml + Bowl      | ACC-REM-BUN-2 | ACC-REM-500 + ACC-REM-BOW                       |
| Liquids Set              | LIQ-SET       | LIQ-BAS-2 + LIQ-BON-1 + LIQ-SEA-3 + LIQ-GLO-4 + LIQ-HEA-5 + LIQ-SOA-6 (all 6 liquids, excludes Sensitive Base & Sensitive Glow) |
| Manicure Kit             | ACC-MAN       | ACC-NAI-100/180 + ACC-NAI-240 + ACC-CUT-PRE    |
| Pro File Set             | ACC-NAI-SET   | ACC-NAI-100/180 + ACC-NAI-240                   |

---

## Region-specific: what's filled locally and added at the 3PL

This is what drives **kit-adjusted demand** — only items added at the 3PL have their stock consumed per kit sale. Everything else is inside the pre-assembled kit from China.

### AUS & CA (confirmed)
- **LIQ-HEA-5** (Heal) — kit-adjusted demand
- **ACC-INS** (Instructions) — kit-adjusted demand
- **ACC-LAB**, **ACC-THA** — consumed on ALL orders
- All other liquids: standalone Shopify demand only

### UK (current)
- **LIQ-HEA-5** (Heal) — filled by Oils4Life, kit-adjusted demand
- **LIQ-BAS-2** (Base) — filled by Chemence, kit-adjusted demand
- **LIQ-GLO-4** (Glow) — filled by Chemence, kit-adjusted demand
- **ACC-INS** (Instructions) — kit-adjusted demand
- **ACC-LAB**, **ACC-THA** — consumed on ALL orders
- Other liquids (Seal, Bond, Sensitive): standalone only

### Nordic (planned — not yet in place)
- Planned to match UK setup (Heal + Base + Glow filled locally)
- Until confirmed, treat as AUS/CA setup (Heal only)

---

## Kit SKUs
- **KIT-STA-2** — Starter Kit
- **KIT-COM-4** — Complete Kit
- **KIT-ULT-6** — Ultimate Kit

## Growth Factor
The growth factor scales the sum of the live kit DSRs from the POS MODEL.

**Example:** If POS MODEL DSRs are STA=34, COM=78, ULT=35 (total 147/day), then:
- 1.0x = 147 kits/day
- 1.3x = 191.1 kits/day
- 1.4x = 205.8 kits/day

**Recommended calculation:** actual 14d kit DSR ÷ POS MODEL base total, then +10% buffer.

**Source of truth for DSR:** always the `POS MODEL` tab in the Order Schedule xlsx.

---

## Packaging SKUs (not sold on Shopify)
These are consumed at warehouse level. They show 0 in Shopify. Exclude from Shopify DSR comparison. Only assess via 3PL deduction rates.
- STO-BUB-BAG-L (Bubble Mailer Large)
- STO-BUB-BAG-S (Bubble Wrap Liquid Pocket)
- STO-MAI-BAG-S (Small Satchel)
- STO-MAI-2 (Small Box)

## Inserts (consumed per order, not sold on Shopify)
- ACC-INS (Instructions Booklet) — per kit
- ACC-LAB (Product Info Booklet) — per order, compliance
- ACC-THA (Thank You Card) — per order

## Component SKUs (used in local fills)
These are the empty bottles/inners/lids that get shipped to the local filler:
- HEA-EMP, HEA-LID, HEA-BSH — Heal empties
- ACC-RE1-BOT, ACC-RE1-LID, ACC-RE1-INN — Remove 120ml empties
- ACC-RE5-BOT, ACC-RE5-LID, ACC-RE5-INN — Remove 500ml empties

When these go to zero in the 3PL data, it usually means they've been shipped to the filler — NOT a stockout. Cross-reference with Slack for fill PO activity.
