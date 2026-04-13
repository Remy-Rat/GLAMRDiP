# Improvement Roadmap — last updated 13 Apr 2026

## Priority 1 — Remove manual friction
- [ ] **Google Drive for Desktop** — install sync app so Claude can read Order Schedule xlsx directly from a synced folder path. Eliminates the download step.
- [ ] **Standalone analysis script** — write `analysis.py` in this repo, run with `uv run --with pandas,openpyxl analysis.py AUS`. Repeatable, anyone on the team can run it.

## Priority 2 — Richer context per analysis
- [ ] **Slack + Gmail cross-referencing** — after analysis, auto-pull last 7d from regional inventory channels + search Gmail for supplier updates. Turns numbers into numbers + context.
- [ ] **Per-region component maps** — document what's filled locally vs pre-packed from China for UK, CA, Nordic. Prevents incorrect kit-adjusted demand calculations.

## Priority 3 — Reduce manual maintenance
- [ ] **DSR staleness detection** — flag when POS MODEL DSR drifts significantly from actual Shopify DSR over multiple weeks. Prompt Greg to refresh.
- [ ] **CNTR TRACKER replacement** — auto-detect arrivals from 3PL data (already working). Either stop maintaining the manual tracker or auto-generate updates from detections for Greg to confirm.
- [ ] **Scheduled weekly runs** — once file path is stable via Drive sync, run AUS Monday, UK Tuesday, CA Wednesday, Nordic Friday. Auto-update Current Issues and archive to Weekly Summaries.
