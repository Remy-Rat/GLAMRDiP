# Lead Times

## Target Cover & PO Timing

Target kit cover before restock: **14-21 days** (lean inventory).

Work backwards from the target stock-out date to set PO milestones:

```
Target restock date (14-21d kit cover remaining)
  ← minus 30 days shipping = Est. Completion date needed
  ← minus 40 days production = PO Place Date
  ← minus 70 days from completion = Raw Goods PO Place Date

Timeline example:
  Day 0:   Raw goods PO placed
  Day 70:  Raw goods arrive at Sally → production starts
  Day 110: Production complete (40 days)
  Day 140: Arrives at 3PL (30 days shipping)
```

## Shipping Times (from CN completion to 3PL)

| Region | Shipping | Notes |
|---|---|---|
| AUS | ~30 days | Standard vessel (POS MODEL: "Vessels - 16 days" for express) |
| CA | ~32-45 days | POS MODEL: "Vessels - 32 days (Forecast 45 days)" |
| UK | ~42 days | POS MODEL: "Vessels - 42 days" |
| Nordic | ~42 days+ | Assume same as UK for now, likely longer — update when confirmed |

Express shipments are faster (~16 days to AUS per POS MODEL) but more expensive.

## Local Fill Lead Times

### AUS — Outsource Packaging (Heal, Remove 120ml, Remove 500ml)
- Transit to OP: ~7 days
- Filling: ~14 days
- Delivery to G3PL: ~7 days
- **Total: ~28 days** from all ingredients at OP

### CA — Swift Innovations (Heal, Remove 120ml, Remove 500ml)
- Total: TBD — Remy to confirm

### UK — Chemence (Base, Glow, Seal) / Oils4Life (Heal)
- Chemence: **6-8 weeks** at 8,000 unit quantities (Viktorija confirmed 13 Apr 2026). Payment required before dispatch (usually day before). Delivery to Fulfillable via Woodview courier (no tracking, next-day delivery from Corby).
- Oils4Life (Heal): TBD — Remy to confirm
- Liquipak (Remove 120ml/500ml): EXITING — final PO placed Apr 2026, no replacement filler found. ~160d coverage from 800L pre-mix.

## How to Use for Stock-Out Forecasting

For each SKU:
```
days_until_stockout = confirmed_stock / actual_DSR
days_until_restock  = est_arrival - today  (from POS MODEL shipment block)
gap                 = days_until_stockout - days_until_restock

gap > 0  → stock lasts until restock arrives
gap = 0  → cuts it close, monitor
gap < 0  → will stock out |gap| days before restock arrives
```

For items with no inbound on order:
```
days_until_stockout = confirmed_stock / actual_DSR
if days_until_stockout < 14+40+30 = 84 days → too late to place a new CN PO and receive in time
if days_until_stockout < 14 → already critical, only local fill or express shipment can help
```
