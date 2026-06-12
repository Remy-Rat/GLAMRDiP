# ShipHero PO Creation — API write access

Raising inbound purchase orders in ShipHero via the API, so 3PLs can receive against them at the same time we recommend a PO. First live PO: `PO 19_12-06-2026 | Oils4Life` (UK, 12 Jun 2026). Costs nothing — API usage is included in the subscription (throttle credits only).

## The two token types (don't mix them up)

| | Read-only (PKCE/OAuth) | Read-write (classic) |
|---|---|---|
| File | `token_<region>.json` | `token_<region>_rw.json` |
| How | `get_token_pkce.sh` + browser login | `get_classic_token.sh` (prompts email + password) |
| Can mutate? | **Never** — ShipHero's OAuth app strips `change:` scopes before consent; no user permission or setting fixes this | Yes — carries the full UI permissions of the login |
| Used for | Order health checks, audits, queries | Creating/updating POs |

All scripts live in `~/.claude/skills/shiphero-public-api/scripts/`, token files one level up. Endpoint `https://public-api.shiphero.com/graphql`, header `Authorization: Bearer <access_token>`.

## 28-day token cycle (the bit to remember)

Classic tokens expire ~28 days after issue. **Renewal does NOT need a password** — the refresh script uses the stored refresh_token:

```bash
TOKEN_FILE=~/.claude/skills/shiphero-public-api/token_uk_rw.json \
  bash ~/.claude/skills/shiphero-public-api/scripts/refresh_classic_token.sh
```

- Run per region file (`token_uk_rw.json`, `token_aus_rw.json`, `token_ca_rw.json`).
- If refresh fails (refresh tokens eventually expire too), fall back to a fresh login: `TOKEN_FILE=... bash .../get_classic_token.sh` in a normal terminal.
- Claude checks token age before any PO write and runs the refresh when needed — but if a write ever fails with an auth error, this is why.
- UK first issued 12 Jun 2026 → first expiry ~10 Jul 2026.

## Region logins

| Region | 3PL / warehouse | Login | Token file |
|---|---|---|---|
| UK | Fulfillable, warehouse 128385 (134297 = dead B360 ghost) | remy+uk@scale-labs.com.au | `token_uk_rw.json` |
| AUS | G3PL | remy+au@scale-labs.com.au | `token_aus_rw.json` |
| CA | 247 (Joel-owned workspace) | remy@scale-labs.com.au | `token_ca_rw.json` |
| Nordic | n/a — Shelfless is not on ShipHero | — | — |

## PO conventions (UK, from PO 1–19)

- `po_number`: `PO <n>_<our PO reference>` — next sequential n (check latest with a quick query)
- Vendor: leave blank or a GLAMRDiP entity — never the real supplier
- `po_date`: expected arrival at the 3PL (≈ our Required Completion date)
- Prices as plain strings ("0.47"), `subtotal`/`total_price` = qty × price, shipping "0.00"
- Line items need `expected_weight_in_lbs: "0"` and `quantity_received/rejected: 0`
- If a recommended PO is later cancelled, close the ShipHero PO too so receiving isn't waiting on a ghost

## Testing a connection without creating anything

Three checks per region, all side-effect free (verified 12 Jun 2026 on all three regions):
1. `{ me { data { email account { legacy_id email } } } }` — right user, right workspace
2. `{ purchase_orders { data(first: 3, sort: "-created_at") { edges { node { po_number } } } } }` — read access + current PO numbering
3. `purchase_order_update` against a bogus po_id — expect `Cannot access the requested purchaseorder. Permission denied` (that's the object-not-yours response; a proven-writer token returns the same). A genuine write block looks like `Missing required scope(s): ...` instead.

## Gotchas

- `fulfillment_status` stays `pending` even after full receipt — completion signal is `quantity_received == quantity` per line
- Plural `purchase_orders` queries need `first: N` or they blow the credit cap; singular `purchase_order(po_number:)` is cheap
- AUS/CA PO numbering and conventions should be confirmed against their own recent POs before the first write in those regions
