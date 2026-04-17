> **Context:** Get region info from `../Regions/[REGION].md`. Get kit-adjusted items from `../../Shared/Component Map.md`. After completing, update `../Context/Current Issues.md`.

# Region Recap Skill

## Trigger
User says something like "do CA recap", "check on UK", "AUS review", "what's going on in Nordic", or any variation requesting a deep look at a specific region.

## Where This Fits

The recap is the **entry point** in the review cycle:

```
1. RECAP (this skill) — what's the story? Slack/Gmail context, what changed, what's open.
2. POS CHECK — what do the numbers say? Stock position, forecasts, actions.
3. SALES ANALYSIS — how are we selling? DSR, trends, discrepancies.
4. USER POSTS SUMMARY — Remy writes the Slack update for the region channel.
5. SUMMARY REVIEW (optional) — check the message against findings.
```

The recap should NOT duplicate quantitative analysis — that's for the POS Check and Sales Analysis. Instead it should:
- Set the narrative context
- Identify what's changed since the last review
- Flag what the POS Check and Sales Analysis should focus on
- Surface decisions that are pending and emails that need action

---

## Region Info
Get the region's channel IDs, supplier contacts, 3PL info, and inventory config from `../Regions/[REGION].md`. Also read `../Context/Current Issues.md` for the region's last known state.

---

## Phase 1 — Slack Context

1. **Read the region's Slack channel** (last 30 days, or since last recap if more recent).
2. **Find all summary messages** (format: `DD.MM.YYYY REGION SUMMARY`). For each one, note the date and key discussion points.
3. **Identify the most recent summary** and read its thread for replies/decisions.
4. **Capture all messages posted after the most recent summary** — these are live updates not yet captured.

### What to extract from each summary:
- Discussion points / action items
- Container & order status at that time
- Selling performance vs forecast (kit % and overall %)
- Any decisions made in replies

### Issue lifecycle tracking:
For each topic mentioned across the summaries, classify it:
- **NEW** — first appearance this cycle
- **ONGOING** — mentioned in 2+ consecutive summaries, stable
- **ESCALATING** — getting worse (stock dropping, timeline slipping, no progress)
- **IMPROVING** — getting better (stock arriving, issue being resolved)
- **RESOLVED** — explicitly closed or no longer mentioned for 2+ summaries
- **STALLED** — action needed but no progress for 2+ weeks

Note when each issue was **first raised** and how many summaries it's appeared in. If something has been flagged 4+ times, say so — that's a pattern, not an incident.

---

## Phase 2 — Email Context

5. **Search Gmail** (last 21 days) using the search terms from the Region file. Run 2-3 targeted searches:
   - The filler(s) — latest fill status, dispatch dates, payment
   - The 3PL — latest operational updates, stock counts, issues
   - Any hot topic identified in Phase 1

6. **For each key email thread**, extract:
   - Last message: who sent it, when, what it says
   - Is there a reply outstanding? From whom?
   - Any specific dates, numbers, or commitments made

7. **Cross-reference email findings with Slack.** Where email gives a more specific date or number than Slack, use the email version. Where Slack has context email doesn't (e.g. Daniel's interpretation), note both.

---

## Phase 3 — Compile the Recap

### Output Structure:

```
🇽🇽 [REGION] Recap — [Today's Date]

THE SITUATION RIGHT NOW
  3-5 dot points. What's the headline? What's the main risk? What's going well?

ACTIONS FROM LAST REVIEW — STATUS  ← REQUIRED
  Pull every action item from the prior Recap + prior POS Check + prior Sales Analysis.
  For each, mark: ✅ DONE, 🟡 IN PROGRESS / PARTIAL, 🔴 MISSED, ❓ UNCONFIRMED.
  Include owner and a one-line note on what actually happened (with date evidence).
  Call out the single action that matters most — "The one that matters: X is N days overdue."
  Rationale: this is explicit accountability. Without this, open actions go stale across reviews
  (e.g. a Heal fill PO flagged for 5+ days with no evidence of placement).

WHAT CHANGED SINCE LAST RECAP
  Diff against the last recap or Current Issues. Explicitly state:
  - What's NEW (not in last recap)
  - What RESOLVED (was open, now closed)
  - What ESCALATED (was flagged, got worse)
  - What IMPROVED (was flagged, got better)

OPEN THREADS
  For each active issue:
  - Status tag: [NEW] [ONGOING] [ESCALATING] [STALLED] [IMPROVING]
  - First raised: [date] ([X] weeks ago)
  - Current state: what Slack + email combined say
  - Outstanding actions: who owes what
  Order by urgency — most actionable first.

SELLING TREND
  Pull the kit % vs forecast from the last 6-8 summaries. Present as a mini table:
  | Period | Kits vs Forecast | Notable |
  Show the trajectory — is it improving, declining, or flat?
  Don't analyse DSR or colour demand here — that's for Sales Analysis.

DECISIONS PENDING
  Explicitly list items waiting on Joel, Daniel, or Greg. These often get buried.
  Format: "[Person]: [what they need to do] — [context/deadline]"

EMAILS NEEDING ACTION
  - Supplier hasn't replied (3+ days)
  - We owe someone a reply
  - Payment or approval waiting

WATCH FOR IN POS CHECK
  Based on what you've learned, flag 3-5 things the POS Check should focus on:
  - "Verify Base/Glow cover at kit-adjusted rate — Fulfillable now picks per kit"
  - "Check if UK 03062026 has STA allocation — STA selling 71% above model"
  - "B360 Packup block — confirm what's actually transferring"
  These are hypotheses from the qualitative context that need data to confirm.

WATCH FOR IN SALES ANALYSIS
  Flag 2-3 things for the Sales Analysis to investigate:
  - "STA demand spike — is 71% sustained or one-off?"
  - "Overall -7% but kits +5% — standalone products dragging?"
  - "First positive kit week since Feb — verify with full data"
```

---

## Phase 4 — Post-Cycle Review (Optional)

After the full cycle (Recap → POS Check → Sales Analysis → user posts Slack summary), the user may ask to review their message. When triggered:

1. Read the user's Slack message
2. Cross-reference against all findings from the three skills
3. Flag:
   - Anything materially incorrect (wrong date, wrong number)
   - Important findings not mentioned
   - Items that could be clearer or more specific
   - Stale info carried forward from a previous summary
4. Suggest additions if warranted — but respect that the user knows their audience

---

## Region-Specific Notes

### AUS
- Use `AUS 3GPL` tab in the order schedule, NOT `B360`
- 3PL channel is #glamrdip-g3pl — read this for fulfilment context (G3PL = Jake, David)
- Outsource Packaging (OP) fills Heal, Remove 120ml, Remove 500ml — check for ingredient status

### UK
- 3PL is Fulfillable (live since 13 Apr 2026). B360 stock-out process underway.
- Fulfillable picks Base + Glow + Heal per kit (automation rules confirmed 13 Apr). POS MODEL DSR for Base & Glow may be understated — flag for POS Check.
- Chemence fills Base, Glow, Seal (6-8 week lead at 8k qty). Oils4Life fills Heal.
- Liquipak exiting — no replacement filler found. Track this as a stalled issue.
- ACC-LAB-UK printed locally by Print Runner (14-21d lead) — don't flag for CN container.
- B360 Packup = stock transfer from old 3PL, not a CN shipment. No Est. Completion/Arrival from Sally.

### CA
- 3PL is 247 Fulfilment. Channel is #glamrdip-ca-247.
- Swift Innovations fills Heal, Remove 120ml, Remove 500ml.

### Nordic
- Transitioned from Dippi brand to GLAMRDiP late March 2026.
- Check for any branding-related stock issues (old labels, etc.).
- Chemence fill may be needed — check Slack for Nordic liquids discussion.

---

## Style Notes
- **Synthesise, don't transcribe.** If the same issue has been in 6 summaries, say "flagged since [date], now in its 6th week" — don't repeat each mention.
- **Combine Slack and email into one view per topic.** Don't have separate Slack and email sections — merge them by topic.
- **Be direct about staleness.** If something has been stalled for weeks, call it out. "Liquipak replacement: 6 weeks, no progress. This is now the longest-running unresolved item."
- **Dates over durations.** "Payment due 27 Apr" not "payment due in 13 days."
- **The recap is context for humans, not data for machines.** Write it so Joel can skim it in 2 minutes and know what needs his attention.

---

## Post-Task
Update `../Context/Current Issues.md` with the current state for this region. Replace that region's section entirely.
