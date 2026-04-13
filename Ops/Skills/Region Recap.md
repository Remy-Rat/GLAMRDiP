# Region Recap Skill

## Trigger
User says something like "do CA recap", "check on UK", "AUS review", "what's going on in Nordic", or any variation requesting a deep look at a specific region.

---

## Region Info
Get the region's channel IDs, supplier contacts, and 3PL info from `../Regions/[REGION].md`.

---

## Instructions

### Phase 1 — Slack Context (always do this)

1. **Read 30 days of the region's Slack channel.** This is the primary source of truth.
2. **Identify the most recent summary** (format: `DD.MM.YYYY REGION SUMMARY`). Read its thread for any replies.
3. **Identify the previous summary** before that one. Compare: what was flagged then vs what's resolved now? What's still open?
4. **Capture all messages posted after the most recent summary** — these are live updates, follow-ups, and new issues.

### Phase 2 — Email Context (always do this)

5. **Search Gmail for recent emails** (last 21 days) involving the region's key contacts. Use the supplier/contact names from the Region file. Run 2-3 targeted searches, for example:
   - The filler company
   - The 3PL
   - Any known hot topic
6. **Read the most recent emails in the key threads** — focus on: what was the last message, who sent it, is there a reply outstanding?

### Phase 3 — Compile the Recap

Present the recap in this structure:

---

#### 🇽🇽 [REGION] Recap — [Today's Date]

**The situation right now:**
A dot point breakdown in plain-English summary of where things stand. What's the main thing going on?

**Open threads:**
For each active issue, cover:
- **What it is**
- **Where it's at** — last known status from Slack + email combined
- **What's outstanding** — who owes what, any emails awaiting reply, decisions needed
- **How long it's been** — if something has been dragging, say so

Order by urgency — the thing that needs action soonest goes first.

**Containers & Orders:**
- What's in transit and when it's expected
- What's in production and estimated completion
- What's planned but not yet placed
- Any POs from #general-inventory that are relevant to this region and haven't been confirmed as placed

**Selling performance:**
Note the most recent DSR vs actual from the last summary. If underselling has been a trend, note how many weeks.

**Emails needing action:**
List any email threads where:
- A supplier hasn't replied and it's been 3+ days
- We owe someone a reply
- A decision is waiting on Joel or Daniel

---

## Region-Specific Notes

### AUS
- Use `AUS 3GPL` tab in the order schedule, NOT `B360`
- 3PL channel is #glamrdip-g3pl — read this for fulfilment context

### UK
- Transitioning from B360 to Fulfillable (mid-April 2026)
- Run the recap against BOTH 3PLs until transition confirmed complete
- Check for any Borderless 360 handover emails

### Nordic
- Transitioned from Dippi brand to GLAMRDiP late March 2026
- Check for any branding-related stock issues (old labels, etc.)

---

## Style Notes
- Don't just repeat Slack messages — synthesise. If the same issue has been mentioned in 4 consecutive summaries, say "this has been flagged since [date]".
- Combine Slack and email into one view per topic.
- Be direct about what needs action vs what's just context.
- If a channel has been quiet or the summary is stale (14+ days old), flag that upfront.

---

## Post-Task
Update `../Context/Current Issues.md` with the current state for this region.
