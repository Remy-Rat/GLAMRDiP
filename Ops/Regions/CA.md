# 🇨🇦 CA

## Key Info
- **Review Day:** Wednesday
- **Slack Channel:** #ca-inventory (C08SYG1R39U)
- **Order Schedule 3PL Tab:** `B360`

## Inventory Config
- **Labels SKU:** `ACC-LAB-CA`
- **Kit-adjusted items:** LIQ-HEA-5 (Heal), ACC-INS (Instructions) — filled/picked locally per kit
- **3PL-supplied packaging:** STO-BUB-BAG-S (247 supplies their own bubble wrap — exclude from monitoring)
- **ShipHero available:** Yes — 247 Fulfilment runs on ShipHero. **MCP authed 18 May 2026** against the CA ShipHero workspace (account legacy_id 88557, owned by Joel admin@glamrdip.com — different ownership from AUS/UK which are Daniel-owned). Token at `~/.claude/skills/shiphero-public-api/token_ca.json`. Use `TOKEN_FILE=~/.claude/skills/shiphero-public-api/token_ca.json` when running auth scripts; load the token explicitly when querying so the right workspace is hit. Same gotchas as AUS account (see `Regions/AUS.md` for PO name format, singular vs plural query economics, status-vs-quantity-received quirk). CA's PO numbers are sequential and higher (currently PO 38+) vs AUS PO 14 — separate workspaces, separate sequences.
- **Local fillers:** Swift Innovations (Heal, Remove 120ml, Remove 500ml)

---

## 3PL — 247 Fulfilment
- **Zaid** — main contact
- **Slack Channel:** #glamrdip-ca-247 (C090USSSYN9)

---

## Local Filler — Swift Innovations
- **Abhishek Bhambani** — primary contact
- **Jagvir, Kuldeep** — additional contacts
- **Fills:** Heal, Remove 120ml, Remove 500ml

---

## CN Manufacturer — Isay Nail
- **Sally** — all CN filling POs (shared across all regions)

---

## Ingredient Suppliers (for local fills)
- **Greenfield Canada** — local ingredients
- **Amazon Canada** — local ingredients
- **Formulator Sample Shop (FSS)** — various ingredients
- **New Directions Canada** — local ingredients

---

## Local Suppliers
- **Mixam** — local printing (label booklets)
- **Zakka** — bubble mailers / packaging

---

## Shipping Agent
- **Lily** — shared across all regions

---

## Notes
- Gmail searches for CA: search `Swift OR Abhishek` for filler, `247 OR Zaid` for 3PL, `Mixam` for labels

## Overstocking Flag (as of 15 Apr 2026)
- **Growth factor was 2.0x but actual demand is 0.66x.** Every container has been ordered at ~3x required quantity. This compounds order over order.
- Post-container release: ~314 days kit cover vs 45-75 day target. ~13,400 excess kit units at 247.
- CA 21062026 (Birthday Sale, Jul) adds another 4,396 kits. CA 25072026 (Aug) adds 5,404 more.
- **At current demand, CA does not need another kit container until 2027.** Future containers should be sized for colours, accessories, and packaging — not kits.
- Every POS Check should verify actual kit DSR against model and flag if ordering is still based on the inflated growth factor. Target: recalibrate to 0.72x (actual + 10% buffer).
