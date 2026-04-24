---
name: daily-digest-inventory
description: Post the daily inventory digest to Slack #daily-digest-inventory (C0AT34JKHL7) — 4 separate posts, one per region (AUS, UK, CA, Nordic), each with kits projected vs selling, Shopify vs DSR anomalies, Shopify vs 3PL deduction breaches, and action points.
---

## Daily Digest — Inventory

Posts 4 standalone messages to `#daily-digest-inventory` (C0AT34JKHL7), one per region, each self-contained and divider-led.

Audience: Remy, Daniel, Greg.

### Post anatomy

```
─── divider ───
**[ordinal] [Mon] [YYYY] - DAILY DIGEST · [flag] [REGION]**

**Kits:** projecting **X/d**, selling **Y/d** (±N% vs projection)

**`Shopify vs DSR`**
• [over-selling or dead SKUs] OR • None.

**`Shopify vs 3PL`**
• [3PL deduction breaches last 3d] OR • None.

**`Action Points`**
• `[new]` [Action].
• `[ongoing]` [Action carried over from yesterday].
```

`[new]` vs `[ongoing]` is auto-derived by substring-matching today's actions
against yesterday's action texts. See step 5 below.

### Procedure

1. **Prereq:** gcloud authed with Drive scope.
   ```bash
   gcloud auth login --enable-gdrive-access
   ```

2. **Pull POS model data per region** (parallel, run as background commands):
   ```bash
   uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py AUS    > /tmp/digest_aus.json
   uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py UK     > /tmp/digest_uk.json
   uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py CA     > /tmp/digest_ca.json
   uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py Nordic > /tmp/digest_nordic.json
   ```

3. **Gather action points per region** — one subagent per region in parallel.
   Each subagent reads:
   - Region's `#*-inventory` Slack channel (last ~14 days)
   - Region's 3PL channel where applicable (AUS: `#glamrdip-g3pl`, CA: `#glamrdip-ca-247`)
   - Gmail searches scoped to region's filler/3PL/supplier domains (last 14d)

   Channel IDs:
   - AUS: `C08SYFYEUUE` inventory, `C0AKYJ5LDN0` G3PL
   - UK: `C08THPCCCRF` inventory (Fulfillable; no separate 3PL channel)
   - CA: `C08SYG1R39U` inventory, `C090USSSYN9` 247
   - Nordic: `C08THPG5KJ5` inventory

   Each subagent must return a compact JSON object:
   ```json
   { "actions": ["Specific action", "Another action"] }
   ```

   Cap actions at 4 per region. Each action <25 words. Action points are things
   that still need to be done — drop anything already in flight (see
   `feedback_action_points_in_progress.md`).
   If a region is genuinely quiet, return an empty `actions` array.

   Subagent prompt template lives in `Ops/Skills/Daily Digest Inventory.md`.

4. **Write the qualitative input JSON** to `/tmp/qualitative.json` (flat list of
   action strings per region):
   ```json
   {
     "AUS": ["action 1", "action 2"],
     "UK":  ["..."],
     "CA":  ["..."],
     "Nordic": []
   }
   ```

5. **Read yesterday's posts in `C0AT34JKHL7` and their thread replies** to (a) identify actions marked done/in-progress and (b) build the prior-action list for `[new]` vs `[ongoing]` tagging. The pattern:
   - `slack_read_channel(C0AT34JKHL7, oldest=<24h ago>)` → finds yesterday's 4 region posts (look for the divider line and `DAILY DIGEST` header).
   - For each of those 4 posts, `slack_read_thread(channel_id=C0AT34JKHL7, message_ts=<post_ts>)` → reads thread replies.
   - **Completed items** — for each region, identify which of *today's* drafted action items have been claimed as done/in-flight in yesterday's thread (patterns: "actioned", "done", "✅", "complete", "in progress", explicit references to the action's content). Per `feedback_action_points_in_progress.md`, in-flight investigations also go here (suppressed, not tagged ongoing).
   - **Prior actions** — extract every action bullet from yesterday's post body (ignoring thread), strip the leading `[new]`/`[ongoing]` tag if present, and write 5-8 word distinctive substrings. These will tag any matching today-action as `[ongoing]`.
   - Build `/tmp/completed.json` and `/tmp/prior_actions.json`:
     ```json
     // /tmp/completed.json — suppress these from today
     {
       "AUS": ["short distinctive substring of done/in-flight item"],
       "UK":  [], "CA": ["..."], "Nordic": []
     }
     // /tmp/prior_actions.json — tag matching today-actions as [ongoing]
     {
       "AUS": ["substring of yesterday action 1", "substring of action 2"],
       "UK":  ["..."], "CA": ["..."], "Nordic": ["..."]
     }
     ```
     Both use case-insensitive substring match. Keep entries short and distinctive.
   - If yesterday is the first run (no prior digest), skip this step (omit both `--completed` and `--prior`).

6. **Build the digest posts:**
   ```bash
   python3 Ops/Scripts/daily_digest.py \
     --qualitative /tmp/qualitative.json \
     --completed /tmp/completed.json \
     --prior /tmp/prior_actions.json \
     > /tmp/digest_posts.txt
   ```

   Output is 4 sections separated by `===== <REGION> =====` markers — one per region.

7. **Post to Slack** — call `slack_send_message` 4 times, once per region, in order AUS → UK → CA → Nordic. Each post is a top-level message in `C0AT34JKHL7` (not threaded).

### Aggregation logic (in `daily_digest.py`)

- **Categories:** Kits (KIT-*), Colours (POW-*), Liquids (LIQ-* + ACC-REM*), Accessories (other ACC-* not packaging, plus HEA-*).
- **Headline shows Kits only.** Other categories feed anomaly detection silently — Liquids/Accessories/Colours all overlap with kit consumption (model DSR includes kit-pulled units while Shopify only counts standalone), so their aggregates are structurally misleading.
- **Projected DSR sums only sellable SKUs** — those that appear in `shopify.sku_dsr`. Excludes warehouse-only components (HEA-EMP, ACC-RE5-BOT, etc.) that have a fill rate but no customer-facing sales.
- **Shopify vs DSR thresholds:**
  - Over-selling: 7d DSR ≥ 3× model DSR AND model DSR ≥ 1/d.
  - Dead: 7d DSR == 0 AND 30d DSR ≥ 2/d (was selling, now nothing — store/listing flag).
  - Cap 3 each per region.
- **Shopify vs 3PL:** uses `tpl.red_flags[]` from `extract.py` (deductions exceeding `DEDUCTION_BENCHMARKS` per SKU). Surfaces top 3 from last 3 days only.

### Slack rendering rules (DO NOT VIOLATE)

The `slack_send_message` MCP uses **standard markdown**, not Slack mrkdwn. The proxy is strict — these have all caused failures during design:

| Rule | Why |
| --- | --- |
| Use `**bold**`, not `*single*` | Single asterisk renders as italic, not bold. |
| Use hyphens (`-`), not em-dashes (`—`) | Em-dashes rejected by proxy ("Invalid content from server"). |
| Use `x`, not `×` | Multiplication sign rejected by proxy. |
| Divider = `─` (U+2500) × 60 | Plain `-` × N parsed as markdown HR → rejected ("invalid_blocks"). |
| Use `\u200B` (zero-width space) on otherwise-blank lines | Plain blank lines collapse; `\u00A0` (NBSP) rejected by proxy. |
| Append `""` then `GAP` to exit a bullet list | Otherwise the next code-styled header gets indented as list continuation. |

Section headers are `**`Shopify vs DSR`**` (bold inline code) so they pop.

### Top divider rule

Every post starts with the divider. No bottom divider — that prevented "Sent using @Claude" footer from appearing to lead the next region's divider.

### Scheduling

Once stable, set up daily cron via `/schedule`. Suggested time: ~08:00 AEST.

### Known issues / future work

- **Gmail subagent permission** — when running subagents, `mcp__claude_ai_Gmail__*` tools may be blocked by permission prompts. Either pre-approve or have the parent context do Gmail searches and inject results into the subagent prompts.
- **Shopify lag** — data is +1 day behind. Header shows the digest date (today), data is yesterday's Shopify. Considered normal; don't surface "data as of" in the post (clutters).
- **UK 3PL channel** — UK transitioned from B360 to Fulfillable 13 Apr 2026; there's no dedicated UK 3PL Slack channel currently. Inventory channel covers it.
