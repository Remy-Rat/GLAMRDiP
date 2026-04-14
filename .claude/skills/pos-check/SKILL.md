---
name: pos-check
description: Run a POS Model Check — stock position, forecasts, container status, local fills, and action items for a region.
---

## POS Model Check

Region: $ARGUMENTS (e.g. "UK", "AUS", "CA", "Nordic")

If no region specified, ask which region.

### Instructions

1. Read `Ops/Skills/POS Model Check.md` for the full procedure.
2. Read `Ops/Regions/$ARGUMENTS.md` for region-specific info (3PL tab name, inventory config, kit-adjusted items, local fillers).
3. Read `Shared/Component Map.md` for kit-adjusted demand formulas.
4. Read `Ops/Context/Deduction Benchmarks.md` and `Ops/Context/Lead Times.md`.
5. Read `Ops/Context/Current Issues.md` for the region's last known state.
6. Download a fresh copy of the Order Schedule from Google Drive (sheet IDs in memory file `reference_google_drive_sheets.md`).
7. Execute the skill as documented.
8. Save the output to `Archive/Region Reviews/$ARGUMENTS/POS Checks/` with today's date as the filename.
9. Update `Ops/Context/Current Issues.md` and `Ops/Context/Upcoming Orders.md` with findings.

### Post-Check

After presenting the check, note: "Ready for `/sales $ARGUMENTS` when you are."
