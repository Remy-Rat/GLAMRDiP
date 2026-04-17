---
name: full-review
description: Run a full region review — Recap, POS Model Check, and Sales Data Analysis in sequence, with mandatory pauses between phases.
---

## Full Region Review

Region: $ARGUMENTS (e.g. "UK", "AUS", "CA", "Nordic")

If no region specified, ask which region.

### Upfront questions (cap at 4)

Before starting, ask at most 4 decision-relevant questions. Skip anything already answered in memory or Region/Context files. Good questions: scope (skip commercial Sales Performance?), ShipHero availability, POS MODEL freshness assumption, supplier-specific scenarios known to be in flux. Bad questions: things you can derive from files, or things that don't change what you'd produce.

### Phase sequence — MANDATORY PAUSES

Run the three skills in order. **Pause for user confirmation after every phase.** Do not chain phases without a user checkpoint. The pause is what lets the user correct a figure (e.g. "ACC-LAB is actually 18,344 post-Avi, not 3,397") before it contaminates the next phase's output.

1. **Recap** — Execute `Ops/Skills/Region Recap.md`. Save to `Archive/Region Reviews/$ARGUMENTS/Recaps/`. Pause.
2. **POS Check** — Execute `Ops/Skills/POS Model Check.md` (includes Step 0a Gmail reconcile). Save to `Archive/Region Reviews/$ARGUMENTS/POS Checks/`. Pause.
3. **Sales Analysis** — Execute `Ops/Skills/Sales Data Analysis.md`. Save to `Archive/Region Reviews/$ARGUMENTS/Sales Analysis/`. Pause.
4. **Post-review** — Update `Ops/Context/Current Issues.md` and `Ops/Context/Upcoming Orders.md`.

Filename convention: `YYYY-MM-DD REGION Type.md` (e.g. `2026-04-15 CA POS Check.md`).

### Pause template (use this, don't improvise)

After each phase, present output in this format. Keep it tight — the saved file is the artefact; the pause summary is only for decisions that need your input now.

```
✅ [Phase] saved to [path]

Top findings (max 3):
- [finding 1]
- [finding 2]
- [finding 3]

Before [next phase], any of these need correcting?
1. [specific question, max 4]
2. ...
```

Do NOT include a 10-bullet recap of the phase's content. If the user needs detail they will open the file.

### Data freshness rules

- **Always re-pull the Order Schedule xlsx** at the start of the run. Never rely on a previous extract (even from today) — Greg updates POS MODEL daily, sometimes multiple times, and the 3PL tab updates separately.
- **Always run Step 0a (Gmail reconcile)** in the POS Check. A POS Check without a Gmail reconcile against the POS MODEL paste time is a guess.
- **Flag manual overrides at the top** of every phase output, with source of truth (user-confirmed / Gmail thread / Slack message).

### Methodology discipline

- If you spot a methodology choice mid-draft (e.g. "this container uses 1.4x not 1.3x"), **commit or skip** — don't leave a dangling caveat. Either redo the affected math or don't raise it. Hedges are landmines for the reader.
- Manual overrides must cascade to every downstream calculation. Don't silently use sheet values after declaring an override.

### Context Files (read once at start)
- `Ops/Regions/$ARGUMENTS.md`
- `Ops/Context/Current Issues.md`
- `Ops/Context/Upcoming Orders.md`
- `Shared/Component Map.md`
- `Ops/Context/Deduction Benchmarks.md`
- `Ops/Context/Lead Times.md`

### Post-Review
After all three phases + pauses complete:
- Update `Ops/Context/Current Issues.md` with combined findings.
- Update `Ops/Context/Upcoming Orders.md` if container/order status changed.
- Note: "Full review done. Ready to check your Slack summary when you post it."
