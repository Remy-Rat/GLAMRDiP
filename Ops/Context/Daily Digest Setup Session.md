# Daily Digest — Setup Session In Progress

Snapshot of an active setup session. Resume by re-opening the Claude Code session below or by following the **Where we left off** section.

## Session

- **Session ID:** `553de27d-e7a9-48b2-a858-5e4b44136ceb`
- **Started:** 2026-04-20
- **Working directory:** `/Users/remy-m4/Documents/GD/GLAMRDiP`
- **Resume command:** `claude --resume 553de27d-e7a9-48b2-a858-5e4b44136ceb` (or use `/resume` inside Claude Code and pick this session)

## Goal

Set up unattended scheduled daily digest. Need Google service account auth that doesn't expire overnight (user `gcloud auth login` was dying every 24h).

## What's been done

1. **GCP project created**: `glamrdip-ops-vault` under `glamrdip.com` workspace org
2. **APIs enabled**: Drive + Sheets
3. **Service account created**: `glamrdip-ops@glamrdip-ops-vault.iam.gserviceaccount.com`
4. **Org policy block hit** (`iam.disableServiceAccountKeyCreation`) — couldn't override at project level (needs `roles/orgpolicy.policyAdmin`, even Workspace owner blocked).
5. **Pivoted to SA impersonation** (no key needed):
   - Granted Remy `roles/iam.serviceAccountTokenCreator` on the SA.
   - Ran `gcloud auth application-default login` — ADC saved to `~/.config/gcloud/application_default_credentials.json`.
6. **Updated `Ops/Scripts/extract.py`** to use SA impersonation via `gcloud auth print-access-token --impersonate-service-account=...`. Configurable via `GLAMRDIP_SA_EMAIL` env var (default = the SA above).
7. **Shared the AUS sheet** with the SA email as Viewer.

## Where we left off — current blocker

Test command:
```bash
uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py AUS > /tmp/test_aus.json
```

Auth works (warning shows impersonation active), file downloads, but `pd.read_excel` fails with `Excel file format cannot be determined` — meaning the downloaded file isn't a real xlsx. Likely Drive returned an HTML/JSON error response instead of the file.

## Next concrete actions to try (in order)

1. **Inspect the downloaded file** to see what Drive actually returned:
   ```bash
   head -c 500 /tmp/aus_order_schedule.xlsx
   ```
   - If HTML/JSON error → permission issue (sheet share didn't propagate, or sharing was incorrect).
   - If looks like binary garbage → some other issue, dig into pandas.

2. **If permission error**: re-check the AUS sheet share — open `https://docs.google.com/spreadsheets/d/1fUitkQWryQmKdWLwvjyRG_C_-yh0v5lHjvQa3urBGr8/edit` → Share → confirm `glamrdip-ops@glamrdip-ops-vault.iam.gserviceaccount.com` is listed with Viewer access.

3. **If still failing**: try without impersonation as a sanity check:
   ```bash
   GLAMRDIP_SA_EMAIL="" uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py AUS
   ```
   This reverts to user creds (Remy's personal gcloud auth). If that works, the issue is specifically the SA — likely needs Drive scope on the impersonation token, or the SA needs additional roles.

4. **Possible alternate fix**: use the `googleapis-auth` Python library directly instead of the gcloud subprocess approach. Cleaner, scoped tokens, less error-prone:
   ```python
   from google.auth import impersonated_credentials, default
   source_credentials, _ = default()
   target_credentials = impersonated_credentials.Credentials(
       source_credentials=source_credentials,
       target_principal="glamrdip-ops@glamrdip-ops-vault.iam.gserviceaccount.com",
       target_scopes=["https://www.googleapis.com/auth/drive.readonly"],
   )
   target_credentials.refresh(Request())
   token = target_credentials.token
   ```
   Add `google-auth` to the `uv run --with` list.

5. **Once AUS works**: share the other 3 sheets and run all 4 in parallel to confirm.

6. **Then**: try `/schedule` to set up the daily cron.

## Files touched in this session

- `README.md` — full vault setup documentation (new content)
- `Ops/Scripts/daily_digest.py` — new file, builds 4 per-region Slack posts
- `Ops/Scripts/extract.py` — updated to use SA impersonation
- `Ops/Skills/Daily Digest Inventory.md` — operator reference
- `.claude/skills/daily-digest-inventory/SKILL.md` — Claude-readable skill spec (final design)
- `~/.claude-work/projects/-Users-remy-m4-Documents-GD-GLAMRDiP/memory/feedback_slack_message_rendering.md` — saved Slack rendering rules

## Key context to remember on resume

- The 90-day SA key approach didn't work because of org policy. Switched to **SA impersonation with ADC** — Remy's user creds (via ADC) generate short-lived tokens that act as the SA.
- ADC refresh tokens are more stable than `gcloud auth login` tokens but still tied to user identity. If they also expire, fallback options: ask org admin to override the policy (Path A), or set up Workload Identity Federation.
- The 4 sheet IDs are in `Ops/Scripts/extract.py:21-26`.
- SA email: `glamrdip-ops@glamrdip-ops-vault.iam.gserviceaccount.com`
