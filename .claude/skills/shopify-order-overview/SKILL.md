---
name: shopify-order-overview
description: Run the daily Shopify Order Overview — creates dated Google Sheets per region (AUS/UK/CA) with fulfillable orders >48h, backordered SKUs, orders affected by backorder, and orders on hold; then posts a summary to Slack channel C0B4TNW1FPW with hyperlinks. Auto-archives sheets older than 14 days.
---

## Shopify Order Overview

Daily flow that produces one dated Google Sheet per ShipHero region (AUS / UK / CA) and posts a Slack DM summary to Remy.

Audience: Remy (DM only for now; eventually a shared channel).

### What gets produced

**Per region, a fresh dated Google Sheet** in folder `Shopify Order Overview` (ID `1owM2WBXTsvQ0O9-eJsBR1SK9qOMPnUeJ`) named `<REGION> Order Overview - YYYY-MM-DD`, anyone-with-link viewer, 4 tabs:

1. **Fulfillable Orders >48h** — Order# + Order Date for orders dated ≤ 2 business days ago, in an in-flight status, not backordered and not on hold. The 3PL should pick these now.
2. **Backordered SKUs** — SKU, Product, Warehouse, On Hand, Backorder (pcs short), Allocated, Available. From the ShipHero `products` endpoint (source of truth, matches inventory view). Filter enabled.
3. **Orders Affected by Backorder** — one row per affected order with comma-separated `Product -qty` list and total pcs short.
4. **On Hold** — orders flagged with any `*_hold` (payment, fraud, address, shipping_method, operator, client). Hold reasons listed.

**A Slack DM** to `C0B4TNW1FPW` with the date, region headers (`**`<REGION> ORDER OVERVIEW`**`), and per-region: hyperlink to that day's sheet, count of orders unfulfilled >48h, and backordered SKU list (pcs short).

### Collaborative notes

Each tab has a **Notes** column. Anyone with the sheet link has editor access -- the team can type comments directly into the Notes cell next to any order or SKU (e.g. "3PL says address being verified", "customer requested hold").

On the next day's run, if the same order/SKU appears again, its note is **carried forward verbatim** from the most recent prior dated sheet (matched by Order Number for the order-keyed tabs, by SKU for the Backordered SKUs tab). Carried-forward Notes cells are highlighted in **light orange** (#FCE5CD) so the team can see at a glance which comments are repeats from a prior day vs new today.

When an order/SKU drops off the report (shipped, fulfilled, etc.), its note isn't preserved -- the historical dated sheet still has it (14-day archive window).

### CA-specific filter

CA's ShipHero has 3 warehouses labelled "Primary"; the Concord ON warehouse is defunct and holds phantom backorder values. The script excludes warehouse_id `V2FyZWhvdXNlOjkwNzk5` automatically. See [[ca-shiphero-ghost-warehouse]] in memory.

### Procedure

1. **Run the script for all 3 regions** (creates sheets, populates tabs, archives old sheets >14 days, emits JSON):
   ```bash
   uv run --with google-auth,google-auth-oauthlib,google-api-python-client \
     python3 /Users/remy-m4/Documents/GD/GLAMRDiP/.claude/skills/shopify-order-overview/scripts/region_order_overview.py ALL
   ```

2. **Read the JSON payload** the script wrote to `/tmp/order_overview_last_run.json`. It contains the date, per-region URLs, fulfillable counts, and backordered SKU list with units short.

3. **Build the Slack message** following the format below, populating from the JSON. Today's date in human-readable form (e.g. "19 May 2026").

   ```
   ────────────────────
   **SHOPIFY ORDER OVERVIEW - <DD Mon YYYY>**

   **`AUS ORDER OVERVIEW`**
   • [Order Review Report](<aus_url>)
   • <N> orders unfulfilled >48h
   • Backordered SKUs (pcs short):
      • <Product> -<n> pcs <delta_annotation>
      • ...
   OR (if no backordered SKUs): • Backordered SKUs (pcs short): None.

   ​

   **`UK ORDER OVERVIEW`**
   ...

   ​

   **`CA ORDER OVERVIEW`**
   ...
   ```

   **Delta annotation rules** (from `bo_skus[].delta_vs_prior` in JSON):
   - `delta_vs_prior == "new"` → append `(new)`. Means SKU just started backordering today.
   - `delta_vs_prior` starts with `+` → append `(<delta> since <prior_snapshot_date>)`. Means we are **still selling while OOS** — call this out, it's the key signal.
   - `delta_vs_prior == "0"` or `-N` → no annotation (stable or improving).
   - `delta_vs_prior == ""` (no prior snapshot) → no annotation.

   Example with deltas:
   ```
   • Powdered Sky -192 pcs (+8 since 2026-05-18)
   • Secret Lagoon -171 pcs
   • Bubbly -1 pcs (new)
   ```

   Slack formatting rules (per [[slack-message-rendering]]):
   - `**bold**` not `*italic*`
   - No em-dashes; use hyphens
   - `────────────────────` (U+2500) for dividers
   - Empty `​` line (U+200B) between regions for extra vertical gap

4. **Post via `claude_ai_Slack` MCP** `slack_send_message`:
   - `channel_id`: `C0B4TNW1FPW`
   - `message`: the formatted block from step 3
   - Return the message link to the user

5. **Brief the user** with a short status: counts per region, top backorder findings, file URLs, and confirmation Slack was posted. Don't dump the full SKU lists in chat — they're in Slack and on the sheets.

   **Critically: surface any SKU whose backorder is GROWING (positive delta).** A growing backorder means we're still selling while OOS — that's a Shopify-side action item (typically: turn off the variant in Shopify until stock lands). Be explicit: "Powdered Sky still selling while OOS — backorder grew +8 since yesterday. Consider disabling on Shopify."

### Things to note when running

- **First-run prereq**: gcloud must be authed with Drive scope. If permission errors, run `gcloud auth login --enable-gdrive-access`.
- **Auto-archive** runs as part of the script — trashes any sheet in the folder named `<REGION> Order Overview - YYYY-MM-DD` whose date is more than 14 days old. Untouched files (manual notes, other docs in the folder) are not affected.
- **Credit cost is modest** — products endpoint is much cheaper than line-item aggregation; full UK run uses ~1500 credits.
- **Holds detection** uses the in-flight status sweep, not the 30-day raw window — catches recent payment holds reliably (the older approach missed orders from today).
- **The "BO SKUs" line is the actionable picture, not the order count.** Earlier iterations showed "X orders on backorder"; we replaced with units-short per SKU because that's what stock-side action requires.

### Memory references

- [[shiphero-mcp]] — token files per region
- [[ca-shiphero-ghost-warehouse]] — Concord ON filter rationale
- [[slack-message-rendering]] — Slack MCP formatting gotchas
- [[digest-formatting]] — no italics, blank lines between sections
