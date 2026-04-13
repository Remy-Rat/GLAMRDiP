# Component Map

## Kit → Component Consumption (per unit sold)

| Component | SKU | Starter | Complete | Ultimate |
|-----------|-----|---------|----------|----------|
| Heal | LIQ-HEA-5 | 1 | 1 | 1 |
| Base* | LIQ-BAS-2 | 1 | 1 | 1 |
| Sensitive Base* | LIQ-SEN-2 | 1 | 1 | 1 |
| Seal | LIQ-SEA-3 | 1 | 1 | 1 |
| Bond | LIQ-BON-1 | — | 1 | 1 |
| Glow | LIQ-GLO-4 | — | 1 | 1 |
| Remove 120ml | ACC-REM | — | 1 | 1 |
| Remove 500ml | ACC-REM-500 | — | — | 1 |
| Powder colour | POW-* | 1 | 1 | 1 |
| Bubble Mailer | STO-BUB-BAG-L | 1 | 1 | 1 |
| Small Satchel (alt) | STO-MAI-BAG-S | 1 | 1 | 1 |
| Small Box | STO-MAI-2 | 1 | 1 | 1 |
| Instructions | ACC-INS | 1 | 1 | 1 |
| Thank You Card | ACC-THA | 1 | 1 | 1 |

*Base/Sensitive split: approximately 70% Base / 30% Sensitive across all kits.

---

## Kit-Adjusted Demand Formulas

The model DSR for liquids often only captures **standalone Shopify sales**. Real demand must include kit consumption. Use these formulas:

```
kit_total = starter_dsr + complete_dsr + ultimate_dsr

Heal:           standalone + kit_total          (all kits consume 1)
Base:           standalone + kit_total × 0.7    (70% of kit customers choose Base)
Sensitive Base: standalone + kit_total × 0.3    (30% choose Sensitive)
Seal:           standalone + kit_total          (all kits consume 1)
Bond:           standalone + complete + ultimate (Starter doesn't include)
Glow:           standalone + complete + ultimate
Remove 120ml:   standalone + complete + ultimate
Remove 500ml:   standalone + ultimate           (only Ultimate includes)
```

**Example:** If total kits = 120/day and standalone Heal sales = 3/day, total Heal demand = 123/day — NOT 3/day.

---

## Kit SKUs
- **KIT-STA-2** — Starter Kit
- **KIT-COM-4** — Complete Kit
- **KIT-ULT-6** — Ultimate Kit

## Growth Factor
- Base = 80 kits/day (1.0x)
- A growth factor of 1.3x = 104 kits/day
- Recommended calculation: actual 14d kit DSR ÷ 80, then +10% buffer

---

## Packaging SKUs (not sold on Shopify)
These are consumed at warehouse level inside kits. They show 0 in Shopify. Exclude from Shopify DSR comparison. Only assess via 3PL deduction rates.
- STO-BUB-BAG-L (Bubble Mailer Large)
- STO-MAI-BAG-S (Small Satchel)
- STO-MAI-2 (Small Box)
- ACC-INS (Instructions Booklet)
- ACC-THA (Thank You Card)

## Component SKUs (used in local fills)
These are the empty bottles/inners/lids that get shipped to the local filler:
- HEA-EMP, HEA-LID, HEA-BSH — Heal empties
- ACC-RE1-BOT, ACC-RE1-LID, ACC-RE1-INN — Remove 120ml empties
- ACC-RE5-BOT, ACC-RE5-LID, ACC-RE5-INN — Remove 500ml empties

When these go to zero in the 3PL data, it usually means they've been shipped to the filler — NOT a stockout. Cross-reference with Slack for fill PO activity.
