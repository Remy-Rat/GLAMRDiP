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
• [SKU]: 0 sales ... - day N without sales  (or `OOS day N` if thread-explained)
• [SKU]: selling X/d vs projected Y/d (Zx over) - day N above projection
OR • None.

**`Shopify vs 3PL`**
• [3PL deduction breaches last 3d] OR • None.

**`Action Points`**
1. `[new]` [Action].
2. `[ongoing]` [Action carried over from yesterday].
```

Action points are **numbered** so replies can reference them by number ("re: 2 - done").
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

3. **Read yesterday's digest posts FIRST** (before spawning subagents), so you can
   pass yesterday's action list into each subagent. Call `slack_read_channel(C0AT34JKHL7, oldest=<36h ago>)`
   and pull the 4 region posts; extract every action bullet per region (strip the
   `[new]`/`[ongoing]` tag and leading number). Hold this per-region dict in memory.

4. **Gather action points per region** — one subagent per region in parallel.
   Each subagent reads:
   - Region's `#*-inventory` Slack channel (last ~14 days)
   - Region's 3PL channel where applicable (AUS: `#glamrdip-g3pl`, CA: `#glamrdip-ca-247`)
   - Gmail searches scoped to region's filler/3PL/supplier domains (last 14d)

   Channel IDs:
   - AUS: `C08SYFYEUUE` inventory, `C0AKYJ5LDN0` G3PL
   - UK: `C08THPCCCRF` inventory (Fulfillable; no separate 3PL channel)
   - CA: `C08SYG1R39U` inventory, `C090USSSYN9` 247
   - Nordic: `C08THPG5KJ5` inventory

   Pass yesterday's action list for this region into the prompt. The subagent must
   return a compact JSON object with BOTH today's open actions AND any of yesterday's
   actions that appear to have been addressed in regional activity (a PO posted in
   the channel, an email confirmation, a "done" from Remy/Daniel/Greg, etc):
   ```json
   {
     "actions": ["Specific action", "Another action"],
     "completed": ["yesterday action text that was followed through in regional chat/email"]
   }
   ```

   Cap actions at 4 per region. Each action <25 words. Action points are things
   that still need to be done — drop anything already in flight (see
   `feedback_action_points_in_progress.md`). If a yesterday item was actioned in
   the regional channel (e.g. PO placed and posted in `#glamrdip-aus-inventory`),
   it is considered done — put it in `completed`, don't restate in `actions`.
   If a region is genuinely quiet, return empty arrays.

   Subagent prompt template lives in `Ops/Skills/Daily Digest Inventory.md`.

5. **Read yesterday's digest thread replies** in `C0AT34JKHL7` (yesterday's post bodies were already read in step 3). For each of yesterday's 4 region posts, call `slack_read_thread(channel_id=C0AT34JKHL7, message_ts=<post_ts>)`. Extract two things:

   **(a) Completed action items** — which of yesterday's action bullets were marked done/in-flight. Patterns: "actioned", "done", "✅", "complete", "in progress", explicit references (e.g. "re: 2 - placed"). Per `feedback_action_points_in_progress.md`, in-flight investigations also count as completed (suppressed, not tagged ongoing).

   Numbered replies: if someone says "2 done" in the thread, map to yesterday's item #2 by its index in the post.

   **(b) Explained Shopify vs DSR SKUs** — any SKU flagged in yesterday's *Shopify vs DSR* section that a teammate explained as OOS / no-stock / supplier-issue / not-a-listing-issue. Pull those SKUs into `/tmp/explained_skus.json` so today's post renders them as `OOS day N` instead of `day N without sales`. Example: Greg's 23 Apr reply "Both SKUs are 0 sales because there's no fulfillable stock" → add POW-COT-030 and POW-VIB-529 to UK explained list for today.

   **(c) Streak counters** — parse yesterday's post for `day N` markers per SKU (e.g. "day 3 without sales", "OOS day 7"). For each SKU flagged again today, today's streak = yesterday + 1. SKUs not in yesterday's post = streak 1. Build `/tmp/streaks.json` keyed by region → sku → int. If no `day N` marker exists on yesterday's post (pre-streak rollout), treat as streak 1 for today.

6. **Merge into 4 JSON files:**

   ```json
   // /tmp/qualitative.json — today's open actions per region
   { "AUS": ["action 1", "action 2"], "UK": ["..."], "CA": ["..."], "Nordic": [] }

   // /tmp/completed.json — suppress from today. UNION of:
   //   (a) subagent's `completed` array (yesterday's items actioned in regional chat/email)
   //   (b) yesterday's items marked done/in-flight in the digest thread (step 5a)
   { "AUS": ["substring of done item"], "UK": [], "CA": ["..."], "Nordic": [] }

   // /tmp/prior_actions.json — yesterday's action bullets (from step 3), as
   // 5-8 word distinctive substrings. Matching today-actions render as [ongoing].
   { "AUS": ["substring of yesterday action 1"], "UK": ["..."], "CA": ["..."], "Nordic": ["..."] }

   // /tmp/explained_skus.json — SKUs with an OOS/supplier explanation in
   // yesterday's thread (step 5b). Render as "OOS day N" instead of
   // "day N without sales". Refresh each run.
   { "AUS": [], "UK": ["POW-COT-030", "POW-VIB-529"], "CA": [], "Nordic": [] }

   // /tmp/streaks.json — per-SKU day counter (step 5c). yesterday+1 for still
   // flagged; 1 for new. Refresh each run.
   { "UK": { "POW-COT-030": 5, "POW-VIB-529": 3 }, "AUS": {}, "CA": {}, "Nordic": {} }
   ```
   All action matching is case-insensitive substring — keep entries short and distinctive.
   SKU matching is exact. First run (no prior digest): skip step 3 and step 5; omit `--completed`, `--prior`, `--explained-skus`, `--streaks`.

7. **Build the digest posts:**
   ```bash
   python3 Ops/Scripts/daily_digest.py \
     --qualitative /tmp/qualitative.json \
     --completed /tmp/completed.json \
     --prior /tmp/prior_actions.json \
     --explained-skus /tmp/explained_skus.json \
     --streaks /tmp/streaks.json \
     > /tmp/digest_posts.txt
   ```

   Output is 4 sections separated by `===== <REGION> =====` markers — one per region.

8. **Post to Slack** — call `slack_send_message` 4 times, once per region, in order AUS → UK → CA → Nordic. Each post is a top-level message in `C0AT34JKHL7` (not threaded).

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
