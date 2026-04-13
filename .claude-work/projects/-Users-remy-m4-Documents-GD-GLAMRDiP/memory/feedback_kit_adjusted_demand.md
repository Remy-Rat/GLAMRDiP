---
name: Kit-adjusted demand rules per region
description: What's picked at the 3PL per kit vs pre-packed from China. Drives which SKUs need kit-adjusted demand in analysis.
type: feedback
---

Kits arrive pre-assembled from China with liquids + accessories. The 3PL adds locally-filled items, colours, and inserts.

**What the 3PL adds per kit (all regions):**
- LIQ-HEA-5 (Heal) — filled locally, kit-adjusted demand
- POW-* (colours) — customer picks at checkout: STA=3, COM=6, ULT=9. Shows as individual Shopify line items, so Shopify already captures total colour demand. No kit-adjustment needed for colours in analysis.
- ACC-INS (Instructions) — picked per kit, kit-adjusted demand

**What the 3PL adds to ALL orders:**
- ACC-LAB (compliance booklet) — consumed per order
- ACC-THA (Thank You Card) — consumed per order

**Region-specific locally-filled liquids (kit-adjusted at 3PL):**
- AUS & CA: Heal only
- UK: Heal + Base (Chemence) + Glow (Chemence)
- Nordic: planned to match UK, not yet in place — treat as Heal only

**Standalone items (NOT in kits):**
- LIQ-SEN-2 (Sensitive Base) — sold separately
- LIQ-SOA-6 (Sensitive Glow) — sold separately
- ACC-REM (Remove 120ml) — standalone / bundle with bowl
- ACC-REM-500 (Remove 500ml) — standalone / bundle with bowl

**Why:** Applying kit-adjusted demand to items that are pre-packed from China massively overstates demand. Only items picked from 3PL stock per kit order need adjustment.

**How to apply:** In sales analysis, only kit-adjust items listed under "What the 3PL adds" for the specific region. All other liquids = standalone Shopify DSR only.
