---
name: Kit-adjusted demand only applies to Heal in AUS
description: Kits arrive pre-assembled from China. Only Heal is filled locally and added to kits at G3PL. All other liquids are standalone only.
type: feedback
---

Do NOT apply kit-adjusted demand to all liquids. Kits arrive pre-assembled from China with liquids already inside.

**AUS specifics:**
- Heal (LIQ-HEA-5): only liquid consumed per kit at warehouse level (filled locally by Outsource Packaging, added to kits at G3PL). Kit-adjusted demand applies.
- All other liquids (Base, Sensitive, Seal, Bond, Glow): pre-packed in kits from China. G3PL stock only depletes from standalone Shopify sales.
- Remove 120ml and 500ml: separate standalone items, NOT included in kits.

**POS MODEL DSR:** Manually calculated from monthly sales data, pasted periodically. Already accounts for Heal kit consumption. Monitor variance against actual Shopify selling rates.

**Component Map:** Varies by region and may not be fully accurate yet. User plans to improve it. Don't blindly apply kit consumption formulas — confirm per region what's assembled locally vs pre-packed from China.

**Why:** Applying kit-adjusted demand to all liquids massively overstates demand (3-10x), leading to wrong days cover and false urgency flags.

**How to apply:** In sales data analysis, only kit-adjust Heal. Compare all other liquids' standalone Shopify DSR against POS MODEL DSR. Flag variance between model and actual as the key insight.
