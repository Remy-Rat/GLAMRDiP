---
name: Always verify user context against source data
description: When user provides context during region reviews (dates, statuses, decisions), verify against Gmail/Slack before incorporating into the analysis
type: feedback
---

When the user provides contextual updates during the review chain (e.g. "Chemence fill ready Apr 20-24", "duties being paid"), always verify against the actual source — Gmail thread, Slack message, or POS MODEL data — before incorporating into the analysis.

**Why:** User recalled Chemence fill ready "Apr 20-24" but the email actually said dispatch 28 Apr with payment needed by 27 Apr. This 4-8 day difference changed the Base/Glow forecast from "safe" to "tight, 1-3 day margin." Incorrect context cascades into wrong conclusions.

**How to apply:** After the user provides context at each pause point in the review chain, verify key dates and statuses against Gmail/Slack before running the next step. A quick email read takes seconds — getting the date wrong affects the entire forecast.
