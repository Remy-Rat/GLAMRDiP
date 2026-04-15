---
name: sales-performance
description: Run a Sales Performance check — growth, kit trends, colour intelligence, repurchase signals, and selling flags for a region.
---

## Sales Performance

Region: $ARGUMENTS (e.g. "UK", "AUS", "CA", "Nordic")

If no region specified, ask which region.

### Instructions

1. Read `Ops/Skills/Sales Performance.md` for the full procedure.
2. Read `Ops/Regions/$ARGUMENTS.md` for region-specific info.
3. If the Order Schedule hasn't been downloaded this session, download a fresh copy from Google Drive (sheet IDs in memory file `reference_google_drive_sheets.md`).
4. Run the extract and sales performance scripts:
   ```bash
   uv run --with pandas,openpyxl python3 Ops/Scripts/extract.py $ARGUMENTS > /tmp/${ARGUMENTS,,}.json
   cat /tmp/${ARGUMENTS,,}.json | uv run --with pandas python3 Ops/Scripts/sales_performance.py
   ```
5. Check `#sale-announcements` (C091PEBAS65) and `#cro-team-meetings` (C098QGQ6NLS) for context on any spikes, drops, or trend changes.
6. Write the narrative combining script output with commercial context.
7. Save the output to `Archive/Region Reviews/$ARGUMENTS/Sales Performance/` using the naming convention `YYYY-MM-DD $ARGUMENTS Sales Performance.md`.

### Post-Analysis

This is a standalone commercial check. Note: "Sales performance check complete."
