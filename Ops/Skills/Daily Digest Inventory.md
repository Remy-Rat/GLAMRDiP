# Daily Digest — Inventory

Posts the daily inventory digest to Slack `#daily-digest-inventory` (`C0AT34JKHL7`) — 4 separate top-level posts, one per region (AUS, UK, CA, Nordic).

This page is the operator-facing reference. The Claude Code skill spec (the file Claude reads at runtime) lives at `.claude/skills/daily-digest-inventory/SKILL.md`.

---

## Post structure (per region)

```
─── divider (60× U+2500 box-drawing) ───
**[Nth] [Mon] [YYYY] - DAILY DIGEST · [flag] [REGION]**

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

Action points are **numbered** so threads can reference them ("re: 2 done").
`[new]` vs `[ongoing]` is derived by substring-matching today's actions against
yesterday's action list (see pipeline step 5).

Each post stands alone — no parent post, no thread. Top divider only (no bottom) so the channel reads cleanly without `Sent using @Claude` footers leading.

---

## Pipeline

1. **gcloud auth** with Drive scope:
   ```bash
   gcloud auth login --enable-gdrive-access
   ```

2. **Pull POS model JSON per region** (parallel):
   ```bash
   uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py AUS    > /tmp/digest_aus.json
   uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py UK     > /tmp/digest_uk.json
   uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py CA     > /tmp/digest_ca.json
   uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py Nordic > /tmp/digest_nordic.json
   ```

3. **Read yesterday's digest post bodies FIRST** from `C0AT34JKHL7` — `slack_read_channel(oldest=<36h ago>)`, find the 4 region posts by divider + `DAILY DIGEST` header, extract each region's numbered action bullets (strip `[new]`/`[ongoing]` tag and leading number). Hold per-region in memory so step 4 can pass them into the subagents.

4. **Subagent per region (parallel)** — gather today's open actions from Slack + Gmail (last 14 days), AND identify which of yesterday's actions (passed in from step 3) were followed through in regional chat/email. Subagent returns `{ "actions": [...], "completed": [...] }`. See subagent prompt template below.

5. **Read yesterday's digest thread replies and body** in `C0AT34JKHL7`. For each of the 4 region posts, `slack_read_thread(...)` and pull:
   - **Completed actions** (→ `completed.json`): items marked actioned/done/in-flight, including numbered references like "re: 2 done".
   - **Explained SKUs** (→ `explained_skus.json`): any SKU flagged in yesterday's `Shopify vs DSR` section where a teammate explained it as OOS / no-stock / supplier-issue / not-a-listing issue. Rendered as `OOS day N` today instead of `day N without sales`.
   - **Streak counters** (→ `streaks.json`): parse yesterday's post body for `day N` markers per SKU. If a SKU is still flagged today, streak = N+1. Else streak = 1. Pre-streak-rollout posts = 1.

6. **Merge into 5 JSON files:**
   ```json
   // /tmp/qualitative.json — today's open actions (from subagent `actions`)
   { "AUS": ["action 1", "action 2"], "UK": ["..."], "CA": ["..."], "Nordic": [] }

   // /tmp/completed.json — UNION of subagent `completed` + thread-reply done signals
   { "AUS": ["jar transfer from G3PL"], "UK": [], "CA": ["Mixam 1,300pcs booklet"], "Nordic": [] }

   // /tmp/prior_actions.json — yesterday's action bullets from step 3
   { "AUS": ["Heal local fill"], "UK": ["Chemence payment"], "CA": ["Zakka"], "Nordic": ["Paragon receipt"] }

   // /tmp/explained_skus.json — thread-explained SKUs (OOS etc). Exact SKU match.
   { "AUS": [], "UK": ["POW-COT-030", "POW-VIB-529"], "CA": [], "Nordic": [] }

   // /tmp/streaks.json — per-SKU day counter; yesterday+1 for still-flagged, 1 for new.
   { "UK": {"POW-COT-030": 5, "POW-VIB-529": 3}, "AUS": {}, "CA": {}, "Nordic": {} }
   ```
   Action matching is case-insensitive substring; SKU matching is exact.
   First run: skip steps 3 and 5; omit `--completed`, `--prior`, `--explained-skus`, `--streaks`.

7. **Build messages:**
   ```bash
   python3 Ops/Scripts/daily_digest.py \
     --qualitative /tmp/qualitative.json \
     --completed /tmp/completed.json \
     --prior /tmp/prior_actions.json \
     --explained-skus /tmp/explained_skus.json \
     --streaks /tmp/streaks.json
   ```

8. **Post to Slack** — `slack_send_message` 4 times (AUS → UK → CA → Nordic) to channel `C0AT34JKHL7`.

---

## Region channels for qualitative pull

| Region | Inventory channel | 3PL channel | Gmail focus |
| --- | --- | --- | --- |
| AUS | `C08SYFYEUUE` | `C0AKYJ5LDN0` (G3PL) | Jake/Katrina/G3PL, Peter (Outsource Packaging), Sally, Lily, Mark, Avi |
| UK | `C08THPCCCRF` | — (Fulfillable, no dedicated channel) | Chemence/Viktorija, Fulfillable/Benedict, B360/Borderless/Mason/Chris, Liquipak, Oils4Life/dale |
| CA | `C08SYG1R39U` | `C090USSSYN9` (247) | Swift/Abhishek, 247/Zaid, Mixam |
| Nordic | `C08THPG5KJ5` | — (Shelfless, no dedicated channel) | Shelfless/Axel/bring.com, Adib |

---

## Subagent prompt template

Each parallel agent gets a prompt like this (substitute region-specific bits):

> You're producing action points for the **[REGION]** region of GLAMRDiP for a daily inventory Slack digest. Today is **[YYYY-MM-DD]**.
>
> **Yesterday's action points for this region:**
> [paste yesterday's bullets verbatim, one per line, stripped of tag and number]
>
> Read the following sources, focusing on the LAST 14 DAYS (prioritise the last 24-48h for evidence that yesterday's items were actioned):
> 1. Slack channel `[INVENTORY_CHANNEL_ID]` — use `mcp__claude_ai_Slack__slack_read_channel` with `limit: 50` and `response_format: "concise"`. If too large, paginate.
> 2. Slack channel `[3PL_CHANNEL_ID]` — same approach (skip if not applicable).
> 3. Gmail — use `mcp__claude_ai_Gmail__search_threads` with queries like `(supplier_term) AND newer_than:14d`, pageSize=10. Only `get_thread` if a snippet is genuinely ambiguous AND important.
>
> [Region context block — 3PL name, fillers, current open issues — see Ops/Regions/[REGION].md for content]
>
> Return ONLY a compact JSON object with TWO arrays:
> ```json
> {
>   "actions":   ["Specific open action 1", "Specific open action 2"],
>   "completed": ["yesterday action text that was followed through in regional chat or email"]
> }
> ```
> - `actions`: still-open items. Cap 4. Each <25 words. Drop anything in flight.
> - `completed`: any of the yesterday-items above that show clear follow-through in the regional channel or email (e.g. "PO placed @Peter", order confirmation email, recount posted). **If Remy/Daniel/Greg posted about it in the regional chat, treat it as done** — don't restate. Leave empty if none.
> - **Dated PO convention:** any reference in the channel to a PO in the format `[date] [PO type] [PO company]` (e.g. "UK 03062026 Chemence", "22-04-2026 recommended PO", "CA 21062026 container") means that PO is **already in motion / being placed**. Do not surface it as a "place the next PO" action. Only flag specific unblockers (deposit unpaid, supplier silent, invoice missing).
>
> Output only the JSON.

---

## Aggregation rules (in `daily_digest.py`)

- **Categories:** Kits (`KIT-*`), Colours (`POW-*`), Liquids (`LIQ-* + ACC-REM*`), Accessories (other `ACC-*` excluding packaging, plus `HEA-*`).
- **Headline shows Kits only.** Other categories are structurally misleading on aggregate (model DSR for kit-component liquids includes kit-pulled units, Shopify only counts standalone).
- **Projected DSR sums only sellable SKUs** — those that appear in `shopify.sku_dsr`. Excludes warehouse-only components (HEA-EMP, ACC-RE5-BOT, etc.).
- **Shopify vs DSR thresholds:**
  - Over-selling: 7d DSR ≥ 3× model DSR AND model DSR ≥ 1/d.
  - Dead: 7d DSR == 0 AND 30d DSR ≥ 2/d.
  - Cap 3 each per region.
- **Shopify vs 3PL:** `tpl.red_flags[]` from `extract.py` (per-SKU `DEDUCTION_BENCHMARKS` exceeded). Top 3 from last 3 days only.

---

## Slack rendering rules (the gotchas)

The `slack_send_message` MCP uses standard markdown, not Slack mrkdwn. The proxy is strict.

| Rule | Why |
| --- | --- |
| `**bold**` not `*single*` | Single asterisk renders italic, not bold. |
| Hyphens not em-dashes (`—`) | Em-dashes rejected by proxy. |
| `x` not `×` | Multiplication sign rejected by proxy. |
| Divider = `─` (U+2500) × 60 | Plain `-` × N parsed as markdown HR → rejected. |
| Zero-width space (U+200B) on blank lines | Plain blanks collapse; U+00A0 NBSP rejected by proxy. |
| Append `""` then GAP to exit a bullet list | Otherwise next code-styled header gets indented under the list. |

Section headers use `**`Shopify vs DSR`**` (bold + inline code) so they pop.

---

## Files

- `.claude/skills/daily-digest-inventory/SKILL.md` — Claude-readable skill spec (loaded automatically when invoking `/daily-digest-inventory`).
- `Ops/Scripts/daily_digest.py` — message builder. Reads `/tmp/digest_*.json` and optional `/tmp/qualitative.json`; prints 4 region posts.
- `Ops/Scripts/extract.py` — POS model / 3PL / Shopify extractor (existing). Source of all numbers.
- `Ops/Skills/Daily Digest Inventory.md` — this file.

---

## Test runs (20 Apr 2026)

The format was iterated several times during initial design. Final layout posted at:
- AUS: `https://glamrdipworkspace.slack.com/archives/C0AT34JKHL7/p1776671175883799` (option B header tested last)

Earlier iteration posts in the channel show the format evolution — feel free to delete those once the daily cron is running.

---

## Future work

- **Schedule** the daily run via `/schedule` (target ~08:00 AEST after overnight Shopify paste).
- **Pre-approve `mcp__claude_ai_Gmail__*` for subagents** so the qualitative Gmail layer isn't blocked by per-call permission prompts.
- Consider whether to surface a **trend signal** (7d vs prior 23d, or week-over-week) alongside vs-projection — the current vs-projection comparison shows persistent negatives because growth factor is aspirational.
