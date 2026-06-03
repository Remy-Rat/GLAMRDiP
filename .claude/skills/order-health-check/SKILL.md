---
name: order-health-check
description: Pulls a daily order-health report from ShipHero across AUS, UK, CA. Surfaces backorders, stale orders (unfulfilled >2 business days), and orders with active hold flags. Outputs an Excel file with one tab per category plus a Summary. Use when the user asks for an order health check, backorder list, stale order report, or 'what's stuck in the warehouse'.
---

# Order Health Check

Runs a 3-region ShipHero report and writes an xlsx to `~/Downloads/order_health_<date>.xlsx`.

## When to invoke

- `/order-health-check` — test mode (capped pagination, fast, ~3k credits per region)
- `/order-health-check --full` — paginate everything, slower, ~5k+ credits per region
- `/order-health-check --regions UK` — restrict to one region
- `/order-health-check --by-region` — also writes per-region xlsx files alongside the combined one (for VA hand-off)

Combinable: `/order-health-check --full --by-region`

## What it reports

**Backorders** — orders with `has_backorder: true`. Region | Order# | Date | SKU | Product | Qty backordered.

**Stale orders** — orders placed before 2 business days ago AND `fulfillment_status` not in (`fulfilled`, `canceled`, `cancelled`). Includes any active hold flags. Region | Order# | Order Date | Age | Status | On Hold | Hold reasons.

**On Hold** — orders where any of `holds.{fraud,address,shipping_method,operator,payment,client}_hold == true`. Wider sweep (last 30 days). Region | Order# | Date | Status | Hold reasons.

## How it's invoked

The bash script handles everything:

```bash
uv run --with pandas,openpyxl python3 ~/.claude/skills/order-health-check/scripts/build_report.py [flags]
```

Flags:
- `--test` (default): caps stale pagination at 6 pages/region, hold sweep at 200 orders, backorders at first 20 orders. Suitable for daily on-demand use without burning credits.
- `--full`: paginates until exhausted on all three categories. Use sparingly.
- `--regions <CSV>`: defaults to `AUS,UK,CA`. Pass any subset (e.g. `--regions AUS,CA`). Nordic is not on ShipHero — skip.
- `--by-region`: in addition to the combined file, write `order_health_<region>_<date>.xlsx` for each region — handy for emailing the VA / CX team a region-specific list.
- `--out-dir <path>`: defaults to `~/Downloads`.

## Gotchas (learned from build phase)

- Each region has custom `fulfillment_status` strings: AUS uses `GlamrDip` plus dashed variants by kit type (`GlamrDip - Starter Kit`, `GlamrDip - Complete Kit`, `GlamrDip - Ultimate Kit`, `GlamrDip Large`); UK uses `GLAMRDIP D-PACK Ready`; CA uses `GLAMRDiP`. The script uses two-layer discovery: `KNOWN_INFLIGHT_FALLBACKS` baseline + dynamic `updated_from` discovery. Update the fallback list when new statuses appear in the wild.
- `quantity_shipped` on line items is unreliable for "is this shipped" — use `fulfillment_status` only.
- `hold_until_date` is almost never populated. The real signal lives in `holds.{*_hold}` booleans.
- The `orders` plural query returns orders OLDEST-first by date. Good for stale, but for backorders you may want the most-recent — paginate accordingly.
- Per-account 4,004 credit max per single operation. Always cap `first: N` (max 20-30 to stay well under). The plural query without `first:` will fail.
- Token files are per-region: `~/.claude/skills/shiphero-public-api/token_<region>.json`. See `[[shiphero-mcp]]` memory.

## After running

Brief the user with:
- Counts per region from the Summary tab
- Top finding (e.g. "AUS has 3 stale orders > 14 days — check #AU2389049")
- Any on-hold orders flagged (rare; if any appear, surface them prominently)
- File path to the saved xlsx

Don't dump the whole table into chat — point at the file.

## Future work

- macOS `launchd` for local 8am daily run (computer must be awake)
- Or migrate token files to GCP Secret Manager + run via `/schedule` on Anthropic infra (computer-off proof) — needs token relocation work
- Slack post option (auto-post summary counts to `#daily-digest-inventory`)
- Track week-on-week deltas (is the backorder/stale list growing?)
