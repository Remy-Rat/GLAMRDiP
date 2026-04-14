---
name: ShipHero PO exports for check-in tracking
description: User can export ShipHero PO CSVs on demand — key to solving the partial container check-in problem
type: reference
---

## ShipHero PO Export
User can export Purchase Order CSVs from ShipHero on demand. These show per-SKU:
- **Quantity** — what was expected on the PO
- **Quantity Received** — what's been checked in so far
- **On Hand** — current G3PL stock (across all POs, not just this one)
- **Available** — on hand minus backorders

## How this solves the double-counting problem
The POS MODEL has Express Shipment columns with OL (Order List) quantities for inbound orders. But if G3PL is partway through checking in a container, some of those OL units are already in G3PL ON HAND.

Using ShipHero PO data:
- `Quantity Received >= Quantity` → PO fully checked in, no pending stock
- `Quantity Received < Quantity` → still checking in, pending = Quantity - Quantity Received
- True pending inbound = sum of (Quantity - Quantity Received) across all active POs

## Quarantined stock
ShipHero exports may show QUARANTINED SKUs (e.g. LIQ-BAS-2-QUARANTINED, LIQ-HEA-5-QUARANTINED). This is stock at G3PL that is NOT available for sale. Flag separately in POS checks.

## PO naming
- PO 9 = B360 Packup
- PO 10 = Outsource Packaging fill delivery
- PO 7 = AUS 07032026
- Active POs change — check CNTR TRACKER or Slack for current list

## Export format
CSV with headers: Product, SKU, Quantity, On Hand, Backorder, Available, Reorder Level, Manufacturer Sku, Quantity Received, Item Price, Total Price
