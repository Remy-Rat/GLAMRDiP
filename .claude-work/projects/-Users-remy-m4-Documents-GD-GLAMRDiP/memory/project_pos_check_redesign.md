---
name: POS Check skill refinements in progress
description: Tracking improvements to the POS Model Check skill based on live test runs
type: project
---

POS Model Check skill was rewritten 14 Apr 2026. First test run on AUS data identified these refinements for the next iteration:

**Improvements to make:**
1. Quarantined stock needs its own callout — 6,463 Heal quarantined was buried in the table
2. Show benchmark vs actual deduction variance % for packaging (not just raw numbers)
3. Keep "Src" column (SH vs POS) as standard — shows what's verified vs assumed
4. Double-count detection: always skip Delivered shipment blocks (already fixed in code, document in skill)
5. Distinguish component stock (empties for fills) from sellable stock in check-in progress
6. "No inbound on order" is worse than "pending check-in" — flag differently in after-arrival projection
7. STO-BUB-BAG-S benchmark of 130 may be outdated (actual 162/day) — flag for Greg to review

**Next test:** CA region (described as cleanest region). Will help validate the skill on a simpler dataset before tackling UK (3PL transition complexity) and Nordic.

**Google Drive sheet IDs needed:** CA, UK, Nordic Order Schedule IDs not yet captured — get these during first run of each region.
