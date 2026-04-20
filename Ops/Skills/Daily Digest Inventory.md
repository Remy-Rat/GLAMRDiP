# Daily Digest — Inventory

Posts the daily inventory digest to Slack `#daily-digest-inventory` (`C0AT34JKHL7`) — 4 separate top-level posts, one per region (AUS, UK, CA, Nordic).

This page is the operator-facing reference. The Claude Code skill spec (the file Claude reads at runtime) lives at `.claude/skills/daily-digest-inventory/SKILL.md`.

---

## Post structure (per region)

```
─── divider (60× U+2500 box-drawing) ───
**[Nth] [Mon] [YYYY] - DAILY DIGEST · [flag] [REGION]**

[1-3 sentence qualitative summary]

**Kits:** projecting **X/d**, selling **Y/d** (±N% vs projection)

**`Shopify vs DSR`**
• [over-selling or dead SKUs] OR • None.

**`Shopify vs 3PL`**
• [3PL deduction breaches last 3d] OR • None.

**`Action Points`**
• [Action]. Owner: **Name**.
```

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

3. **Subagent per region (parallel)** — gather qualitative summary + action points from Slack chats and Gmail (last 14 days).

4. **Write `/tmp/qualitative.json`** keyed by region name:
   ```json
   {
     "AUS": { "summary": "...", "actions": [{"text": "...", "owner": "..."}] },
     "UK":  { ... },
     "CA":  { ... },
     "Nordic": { ... }
   }
   ```

5. **Read yesterday's digest posts and their threads** in `C0AT34JKHL7`. For each region's post, look at the thread replies for items marked actioned/done/in progress, and write `/tmp/completed.json` with short substrings of any of today's actions that should be suppressed:
   ```json
   {
     "AUS": ["jar transfer from G3PL to Outsource", "B360 final check-in"],
     "UK":  [],
     "CA":  ["Mixam on missing 1,300pcs"],
     "Nordic": []
   }
   ```
   Substring match is case-insensitive against `action.text`. Skip this step on the very first run.

6. **Build messages:**
   ```bash
   python3 Ops/Scripts/daily_digest.py \
     --qualitative /tmp/qualitative.json \
     --completed /tmp/completed.json
   ```

7. **Post to Slack** — `slack_send_message` 4 times (AUS → UK → CA → Nordic) to channel `C0AT34JKHL7`.

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

> You're producing a qualitative summary for the **[REGION]** region of GLAMRDiP for a daily inventory Slack digest. Today is **[YYYY-MM-DD]**.
>
> Read the following sources, focusing on the LAST 14 DAYS:
> 1. Slack channel `[INVENTORY_CHANNEL_ID]` — use `mcp__claude_ai_Slack__slack_read_channel` with `limit: 50` and `response_format: "concise"`. If too large, paginate.
> 2. Slack channel `[3PL_CHANNEL_ID]` — same approach (skip if not applicable).
> 3. Gmail — use `mcp__claude_ai_Gmail__search_threads` with queries like `(supplier_term) AND newer_than:14d`, pageSize=10. Only `get_thread` if a snippet is genuinely ambiguous AND important.
>
> [Region context block — 3PL name, fillers, current open issues — see Ops/Regions/[REGION].md for content]
>
> Return ONLY a compact JSON object:
> ```json
> { "summary": "...", "actions": [{"text": "...", "owner": "..."}] }
> ```
> Cap actions at 4. Summary <50 words. Each action <25 words. Output only the JSON.

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
