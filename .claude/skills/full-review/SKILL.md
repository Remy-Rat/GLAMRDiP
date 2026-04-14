---
name: full-review
description: Run a full region review — Recap, POS Model Check, and Sales Data Analysis in sequence.
---

## Full Region Review

Region: $ARGUMENTS (e.g. "UK", "AUS", "CA", "Nordic")

If no region specified, ask which region.

### Instructions

Run all three skills in sequence for the specified region:

1. **Recap** — Read and execute `Ops/Skills/Region Recap.md`. Present findings. Save to `Archive/Region Reviews/$ARGUMENTS/Recaps/`.
2. **POS Check** — Read and execute `Ops/Skills/POS Model Check.md`. Use context from the recap to focus the analysis. Save to `Archive/Region Reviews/$ARGUMENTS/POS Checks/`.
3. **Sales Analysis** — Read and execute `Ops/Skills/Sales Data Analysis.md`. Save to `Archive/Region Reviews/$ARGUMENTS/Sales Analysis/`.

All three outputs use today's date as the filename.

Between each step, present the output and pause for the user to confirm before moving to the next step. The user may want to provide additional context (e.g. "B360 Packup stock is the stock from our old 3PL") before the POS Check runs.

### Context Files (read once at start)
- `Ops/Regions/$ARGUMENTS.md`
- `Ops/Context/Current Issues.md`
- `Ops/Context/Upcoming Orders.md`
- `Shared/Component Map.md`
- `Ops/Context/Deduction Benchmarks.md`
- `Ops/Context/Lead Times.md`

### Post-Review
After all three are complete:
- Update `Ops/Context/Current Issues.md` with combined findings.
- Update `Ops/Context/Upcoming Orders.md` if container/order status changed.
- Note: "Full review done. Ready to check your Slack summary when you post it."
