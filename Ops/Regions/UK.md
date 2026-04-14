# 🇬🇧 UK

## Key Info
- **Review Day:** Tuesday
- **Slack Channel:** #uk-inventory (C08THPCCCRF)
- **Order Schedule 3PL Tab:** `B360` (transitioning to Fulfillable)

## Inventory Config
- **Labels SKU:** `ACC-LAB-UK` — printed locally by Print Runner, 14-21 day lead time. Do not flag for CN container space.
- **Kit-adjusted items:** LIQ-HEA-5 (Heal), LIQ-BAS-2 (Base), LIQ-GLO-4 (Glow), ACC-INS (Instructions) — picked by Fulfillable per kit via automation rules (confirmed 13 Apr 2026)
- **Fulfillable kit rules:** Each kit order adds 1x ACC-INS + 1x LIQ-BAS-2 + 1x LIQ-GLO-4 + 1x LIQ-HEA-5. Bond + Seal are already in the CN kit. Each order adds 1x ACC-LAB-UK + 1x ACC-THA.
- **3PL-supplied packaging:** TBD — confirm with Fulfillable
- **ShipHero available:** Yes — Fulfillable runs on ShipHero. PO exports may be available on request via Benedict.
- **Local fillers:** Chemence (Base, Glow, Seal — 6-8 week lead time at 8k qty), Oils4Life (Heal)
- **Exiting filler:** Liquipak (Remove 120ml/500ml) — no longer filling. Final PO placed Apr 2026. No replacement found.

---

## 3PL (current) — Fulfillable
- **Benedict Chidzoy** (ben@fulfillable.co.uk) — enterprise accounts, main contact
- **Location:** BUR1, Dettingen Way, Bury St Edmunds, IP33 3YB
- **Status:** Live since 13 Apr 2026. Stock sync enabled. Orders processing from UK21177824 onwards.
- **WMS:** ShipHero (same as AUS/CA)

## 3PL (old) — Borderless 360 / B360
- **Chris Taylor** (chris@borderless360.com) — UK ops, handling stock take
- **Mason Asato** (mason@borderless360.com) — account management, stock-out process
- **Status:** Stopped fulfilling 13 Apr 2026. Stock-out process underway:
  - 55 final orders fulfilled → stock take → packing → transfer to Fulfillable
  - £8,500 GBP deposit required (not confirmed paid as of 14 Apr)
  - Work Orders for stocktake + packing: Joel confirmed will submit
  - ~288,898 units remain at B360 pending transfer
  - Portal access: Joel requested 90 days (Mason offered 14 days)

---

## Local Fillers
- **Chemence** — Base fills, Glow fills (from empty bottles)
- **Oils4Life** — Heal fills
- **Liquipak** — EXITING. Previous filler for Remove 120ml + Remove 500ml. No longer used.

---

## CN Manufacturer — Isay Nail
- **Sally** — all CN filling POs

---

## Ingredient Suppliers (for local fills)
- **The Soapery** — local ingredients
- **Formulator Sample Shop (FSS)** — various ingredients
- **CFS Fibreglass** — local ingredients
- **Inoxia** — local ingredients

---

## Local Printer
- **Print Runner** — local printing

---

## Shipping Agent
- **Lily** — shared across all regions

---

## Notes
- 3PL transition from B360 to Fulfillable completed 13 Apr 2026. B360 stock-out process underway.
- **POS MODEL DSR for Base & Glow is understated** — model shows standalone rates only. Fulfillable picks both per kit. Actual kit-adjusted: ~90/day Base, ~96/day Glow (as of Apr 2026). Model needs updating by Greg.
- **B360 "Packup" block on POS MODEL** = stock transfer from old 3PL. Not a CN shipment. Timing depends on B360 stock-out process completion.
- Gmail searches for UK: `Chemence OR Viktorija` for filler, `Fulfillable OR Benedict` for 3PL, `B360 OR Borderless OR Mason OR Chris` for old 3PL, `Liquipak` for exiting filler, `Oils4Life OR dale` for Heal filler
