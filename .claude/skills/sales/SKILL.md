---
name: sales
description: Run a Sales Data Analysis — DSR, trends, performance vs model, discrepancies, and selling flags for a region.
---

## Sales Data Analysis

Region: $ARGUMENTS (e.g. "UK", "AUS", "CA", "Nordic")

If no region specified, ask which region.

### Instructions

1. Read `Ops/Skills/Sales Data Analysis.md` for the full procedure.
2. Read `Ops/Regions/$ARGUMENTS.md` for region-specific info.
3. Read `Shared/Component Map.md` for kit-adjusted demand formulas.
4. Read `Ops/Context/Current Issues.md` for the region's last known state.
5. If the Order Schedule hasn't been downloaded this session, download a fresh copy from Google Drive (sheet IDs in memory file `reference_google_drive_sheets.md`).
6. Execute the skill as documented.
7. Save the output to `Archive/Region Reviews/$ARGUMENTS/Sales Analysis/` with today's date as the filename.

### Post-Analysis

After presenting the analysis, the review cycle is complete. Note: "Full review done. Ready to check your Slack summary when you post it."
