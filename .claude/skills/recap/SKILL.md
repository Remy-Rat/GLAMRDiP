---
name: recap
description: Run a Region Recap — qualitative review of a region via Slack + Gmail. Entry point for the review cycle.
---

## Region Recap

Region: $ARGUMENTS (e.g. "UK", "AUS", "CA", "Nordic")

If no region specified, ask which region.

### Instructions

1. Read `Ops/Skills/Region Recap.md` for the full procedure.
2. Read `Ops/Regions/$ARGUMENTS.md` for region-specific info (channel IDs, contacts, inventory config).
3. Read `Ops/Context/Current Issues.md` for the region's last known state.
4. Execute the skill as documented.
5. Save the output to `Archive/Region Reviews/$ARGUMENTS/Recaps/` with today's date as the filename (e.g. `2026-04-14.md`).
6. Update `Ops/Context/Current Issues.md` with findings.

### Post-Recap

After presenting the recap, note: "Ready for `/pos-check $ARGUMENTS` when you are."
