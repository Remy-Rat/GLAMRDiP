# GLAMRDiP — Operations Vault

Operational knowledge base for **GLAMRDiP**, a nail dip powder brand sold across AUS, UK, CA, and Nordic regions. Managed by Scale Labs (Remy, Daniel) on behalf of the brand owner (Joel) and internal inventory manager (Greg).

The vault is also an Obsidian-compatible note structure and a Claude Code project. It pairs day-to-day inventory ops docs with automated scripts and Claude skills that drive the weekly review cadence and the daily Slack digest.

---

## Vault layout

| Folder | What lives here |
| --- | --- |
| `Ops/` | Inventory, fulfilment, supply chain, 3PLs, ordering, stock analysis. Primary domain. |
| `Marketing/` | Campaigns, CX comms, launches, ads, socials (in development). |
| `Shared/` | Products, people, component maps — referenced from both domains. |
| `Archive/` | Completed reports, old weekly summaries. |
| `.claude/` | Claude Code skills, settings, permissions. |

`CLAUDE.md` (and per-domain `Ops/CLAUDE.md`, `Marketing/CLAUDE.md`) tells Claude how to navigate the vault when invoked.

---

## Prerequisites

If you're cloning this vault onto a new machine, install:

| Tool | Why |
| --- | --- |
| **Claude Code** ([install](https://claude.com/claude-code)) | Runs the skills/agents that drive reviews and the daily digest. |
| **Python 3.11+** | All scripts in `Ops/Scripts/` are Python. |
| **uv** ([install](https://docs.astral.sh/uv/getting-started/installation/)) | Used to run scripts with ephemeral deps (`uv run --with pandas,openpyxl ...`). |
| **gcloud CLI** ([install](https://cloud.google.com/sdk/docs/install)) | Needed to fetch the POS Model Google Sheets via the Drive API. |
| **Obsidian** (optional) | If you want the markdown rendered as a note vault rather than read in your editor. |

Slack and Gmail data come through MCP connectors configured inside Claude Code — no local install required, but you must be signed into the same Slack workspace and Gmail account.

---

## First-time setup

1. **Clone or copy the vault** to your machine.
2. **gcloud auth with Drive scope** — required before any POS model fetch:
   ```bash
   gcloud auth login --enable-gdrive-access
   ```
   (Default `gcloud auth login` only gets GCP scopes — the `--enable-gdrive-access` flag adds Drive/Sheets.)
3. **Confirm script paths** — `Ops/Scripts/extract.py` hardcodes the gcloud binary at `/opt/homebrew/share/google-cloud-sdk/bin/gcloud` (macOS Apple Silicon default). If your install lives elsewhere, update that line.
4. **Open Claude Code in this directory** — the `.claude/` config and CLAUDE.md will load automatically.
5. **Try a smoke test:**
   ```bash
   uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py AUS > /tmp/digest_aus.json
   ```
   If you get a non-empty JSON file, auth is working.

For unattended scheduled runs (e.g. daily digest cron), use a **service account** instead of user OAuth — see "Scheduling the daily digest" below.

---

## Skills (Claude Code commands)

Slash commands available inside Claude Code. Each is an entry point that orchestrates Slack/Gmail reads, script runs, and synthesis.

| Skill | What it does |
| --- | --- |
| `/full-review` | Full weekly review for one region (Recap → POS Check → Sales Analysis). Mandatory pauses between phases. |
| `/recap` | Region recap — qualitative review via Slack + Gmail. |
| `/pos-check` | POS Model Check — stock position, forecasts, container status, local fills. |
| `/sales` | Sales Data Analysis — DSR, trends, performance vs model. |
| `/sales-performance` | Sales Performance — growth, kit trends, colour intelligence, repurchase signals. |
| `/daily-digest-inventory` | Posts the daily inventory digest to Slack `#daily-digest-inventory` (4 region posts). |

Skill specs live at `.claude/skills/<skill-name>/SKILL.md`. Operator-facing references for the more involved ones live at `Ops/Skills/<Skill Name>.md`.

---

## Scripts (`Ops/Scripts/`)

| Script | Purpose |
| --- | --- |
| `extract.py` | Pulls a region's Order Schedule sheet (POS MODEL, 3PL, SHOPIFY tabs) and emits structured JSON. Source of all numbers. |
| `daily_digest.py` | Builds the 4 per-region Slack posts from `extract.py` output + optional qualitative input. Encodes Slack rendering rules. |

Both scripts are designed to be re-runnable, idempotent, and called by skills — but you can also run them standalone.

---

## Daily digest — operational notes

The daily digest is the most automated artefact in the vault. Full reference: `Ops/Skills/Daily Digest Inventory.md`.

**Pipeline (what `/daily-digest-inventory` does end-to-end):**
1. Runs `extract.py` for all 4 regions in parallel → `/tmp/digest_*.json`.
2. Spawns 4 parallel subagents (one per region) to read Slack inventory channels + Gmail (last 14d) and synthesize a 1-3 sentence summary + action points.
3. Writes consolidated qualitative input to `/tmp/qualitative.json`.
4. Runs `daily_digest.py --qualitative /tmp/qualitative.json` → 4 region message strings.
5. Posts each to `C0AT34JKHL7` via the Slack MCP.

**Channels referenced:**
- AUS: `C08SYFYEUUE` inventory, `C0AKYJ5LDN0` G3PL.
- UK: `C08THPCCCRF` inventory.
- CA: `C08SYG1R39U` inventory, `C090USSSYN9` 247.
- Nordic: `C08THPG5KJ5` inventory.
- Output: `C0AT34JKHL7` (`#daily-digest-inventory`).

---

## Scheduling the daily digest

For unattended scheduled runs, switch from user OAuth to a **service account** so tokens don't expire on you:

1. In the GCP project that owns the POS model sheets, create a service account.
2. Download its JSON key (e.g. `~/.config/glamrdip-digest-sa.json`) — keep it out of git.
3. Share each of the 4 POS model sheets (see IDs in `Ops/Scripts/extract.py`) with the service account's email — Viewer access is enough.
4. Either set `GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json` before running, or update `extract.py`'s token call to use `--impersonate-service-account=...`.
5. Once the script runs without manual reauth, schedule via `/schedule` inside Claude Code.

Suggested cron time: ~08:00 AEST (after overnight Shopify paste, before the ANZ team's day).

---

## Reusability for other brands

The structure here (vault + scripts + skills) is reusable, but several things are hardcoded to GLAMRDiP and would need swapping for a different brand:

- Sheet IDs in `Ops/Scripts/extract.py` (one per region).
- Slack channel IDs in `Ops/Regions/*.md`, `.claude/skills/*/SKILL.md`, and `Ops/Skills/Daily Digest Inventory.md`.
- Region taxonomy (AUS/UK/CA/Nordic) — would need to map to the new brand's regions.
- Supplier / 3PL contacts in `Ops/Regions/*.md`.
- Deduction benchmarks in `extract.py` (per-SKU thresholds).

Within Scale Labs / GLAMRDiP, anyone with Slack + Drive access can clone and run after the prerequisites above. For a different brand, allow ~half a day to swap the hardcoded refs.

---

## Team

- **Remy** (remy@scale-labs.com.au) — inventory & ops, Scale Labs.
- **Daniel** (daniel@scale-labs.com.au) — inventory & ops, Scale Labs.
- **Joel** (joel@jdsbrands.com.au) — business owner, GLAMRDiP / JDS Brands.
- **Greg** (greg@glamrdip.com) — internal inventory manager, GLAMRDiP.
- **Gav** — marketing, Scale Labs.

Full contact details: `Shared/People.md`.
