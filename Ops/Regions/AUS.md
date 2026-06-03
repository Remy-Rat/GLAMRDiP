# 🇦🇺 AUS

## Key Info
- **Review Day:** Monday
- **Slack Channel:** #aus-inventory (C08SYFYEUUE)
- **Order Schedule 3PL Tab:** `AUS 3GPL` (do NOT use `B360` — that's the old 3PL)

## Inventory Config
- **Labels SKU:** `ACC-LAB`
- **Kit-adjusted items:** LIQ-HEA-5 (Heal), ACC-INS (Instructions) — filled/picked locally per kit
- **3PL-supplied packaging:** None — all packaging tracked in G3PL
- **ShipHero available:** Yes. AUS 3GPL tab in Order Schedule remains the daily-snapshot view (Greg's AM paste). **MCP authed for live AUS-account queries** from 18 May 2026 — use for mid-day check-in confirmations, supplier-event verification, and quick PO line-item lookups ahead of tomorrow's paste. Export PO CSVs only for partial-check-in reconciliation. **Scope:** AUS account only — UK is on Fulfillable (not ShipHero), CA 247 is a separate ShipHero account requiring its own OAuth.

### ShipHero MCP — query gotchas (AUS)
- **PO name format:** `PO N _RefName` with a space-underscore between them (e.g. `PO 14 _AUS 05052026`, `PO 11_24-03-2026_Booklet AVI`). The shorthand in `## G3PL Known Issues` below ("PO 7 = AUS 07032026") is the conceptual mapping, not the literal ShipHero string.
- **Use singular `purchase_order(po_number: ...)`** when you know the PO. The plural `purchase_orders` without a `first: N` cap will exceed the 4,004 max credits-per-operation and fail with code 30.
- **`fulfillment_status: pending` ≠ unreceived.** Status doesn't always flip from Pending → Closed. Authoritative completion signal is `line_items.quantity_received == quantity` per SKU.
- **Credit budget:** ~5-10 credits per typical PO query, 4,004 baseline restoring at 60/sec. Generous for ops-style use.
- **Token file:** `~/.claude/skills/shiphero-public-api/token_response.json` (28-day refresh).

- **Local fillers:** Outsource Packaging (Heal, Remove 120ml, Remove 500ml)

---

## 3PL — G3PL
- **Jake** — Director — jake@g3pl.com.au
- **Katrina** — Operations Manager — katrina@g3pl.com.au
- **Phone:** +61 3 5277 3572
- **Address:** 2 Mackey St, North Geelong VIC 3215
- **Slack Channel:** #glamrdip-g3pl (C0AKYJ5LDN0)
- **SLA:** 48hr inbound (KPI: 8 business hours), 800+ orders/day fulfilment
- **System:** ShipHero

### G3PL Known Issues
- B360 packup stock arrived mixed/unsorted — caused weeks of inbound delay
- ShipHero PO status doesn't always update (Pending → Closed) — hard to tell when inbound is finalised
- Billing section shows white screen — Jake sends itemised reports manually with each invoice
- SLA not consistently met in first 2 months of operation
- PO naming: PO 7 = AUS 07032026, PO 9 = B360 Packup, PO 10 = Outsource Packaging fill delivery

---

## Local Filler — Outsource Packaging
- **Peter** — pjoseph@outsourcepackaging.com.au
- **Address:** 4/167 Westall Road, Clayton South VIC 3169
- **Phone:** +61 03 8521 3480 / +61 0412 811 713
- **Fills:** Heal, Remove 120ml, Remove 500ml
- **Ships to:** G3PL (2 Mackey St, North Geelong VIC 3215)
- **Lead time:** ~28 days total (7d transit to OP + 14d filling + 7d delivery to G3PL)

---

## CN Manufacturer — Isay Nail
- **Sally** — all CN filling POs
- Produces kits, powders, liquids, accessories for all regions

---

## Ingredient Suppliers (for local fills)
- **Sydney Solvents** — Acetone (sales@sydneysolvents.com.au, contact: Derryn, Allister for refunds)
- **New Directions Australia** — Coconut Oil, Vitamin E
- **Green Living Australia** — Calcium Chloride
- **Formulator Sample Shop (FSS)** — various ingredients

---

## Local Printer
- **Avi Printing** — label booklets

---

## Shipping Agent
- **Lily** — shipping agent for all regions (use WeChat for urgent contact)

---

## Notes
- Switched from B360 (Borderless 360) to G3PL in Feb 2026
- Stock sync: check if enabled (Daniel asked 13 Apr 2026)
- Greg (greg@glamrdip.com) handles stock master, reconciliation, ASNs at GLAMRDiP
- Joel's admin email: admin@glamrdip.com (often sends supplier emails from this)
- Joel's SP Holdings email: joel@spholdingsfze.com (used for some supplier payments)
