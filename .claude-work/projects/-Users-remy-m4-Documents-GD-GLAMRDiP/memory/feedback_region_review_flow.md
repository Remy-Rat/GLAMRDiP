---
name: Region review chain flow
description: Run Region Recap → POS Check → Sales Analysis in sequence, pausing for user context between each step
type: feedback
---

When running a full region review, chain the three skills in order with pauses:

1. **Region Recap** (Slack + Gmail context) → present findings → ask: "anything I should know before the POS check? delays, decisions, WeChat/Sally/Lily context?"
2. **POS Model Check** (stock position + forecast) → present findings (informed by user answers) → ask: "anything off? known PO issues, shipment delays, context I'm missing?"
3. **Sales Data Analysis** (selling performance + discrepancies) → present findings (informed by all prior context)

**Why:** User context from WeChat, Sally PO Tracker, Lily Shipment Tracker, and verbal decisions isn't in Slack/Gmail. Pausing between steps lets the user inject this context before it cascades into wrong conclusions. Example: PO 35 labels — 8,700 received and under investigation, completely changed the POS check output.

**How to apply:** Always pause and ask after each step. Don't chain all three silently. The user's operational knowledge fills gaps that data alone can't.
