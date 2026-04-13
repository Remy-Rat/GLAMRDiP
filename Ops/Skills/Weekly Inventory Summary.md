# Weekly Inventory Summary Skill

## Trigger
Run every Monday morning. Summarise the past 7 days across all 5 inventory channels.

---

## Regional Review Schedule
Each region has a standard weekly review day. Use these as the baseline for task due dates:
- 🇦🇺 AUS — Monday
- 🇬🇧 UK — Tuesday
- 🇨🇦 CA — Wednesday
- 🇸🇪 Nordic — Friday

These are not strict — summaries may be posted earlier or later depending on the week. Always use the actual date of the most recent summary message, not the scheduled day, as your reference point.

---

## Channels to Read
Get channel IDs from `../Channels/Slack Channels.md`:
- #aus-inventory
- #ca-inventory
- #nordic-inventory
- #uk-inventory
- #general-inventory

---

## Instructions

For each channel, follow these steps:

### Step 1 — Find the most recent weekly summary message
Look for the most recent message that follows the format `[DD.MM.YYYY] [REGION] SUMMARY` (e.g. `20.01.2026 AUS SUMMARY`). This is the anchor message for the region's review.

### Step 2 — Check for thread replies on that summary
Read the thread on the summary message. If any replies indicate that an action point has been resolved or addressed, note this against the relevant action point.

### Step 3 — Identify all other messages posted after the summary
Any messages sent in the channel after the summary message (that are not part of the summary thread) should be captured as **"Other Activity"**. Include who sent it and a brief description of what it covers.

### Step 4 — Build the region summary in the format below

---

## Output Format

Lead the entire summary with a **🚨 Urgent Items At a Glance** block at the very top, listing all 🚨 items across all regions in one place before the per-region breakdowns begin.

For each region, produce the following structure:

---

### 🌏 [REGION] — *Summary from [DD MMM YYYY]*

#### 📋 Action Points
For each action point from the summary, apply the following status indicators:

- 🚨 **URGENT** — use when the original message contained ‼️, or keywords like "urgent", "critical", "ASAP", "OOS", "out of stock", "backorder", "stock out", "desperate", or where a deadline is imminent. Also use for any new urgent messages posted *after* the summary.
- ⁉️ **NEEDS FOLLOW-UP** — use when an action point was tagged to someone but has received no reply or acknowledgement, or when the same issue has appeared in multiple prior summaries without resolution.
- ⚠️ **OPEN** — unresolved but not yet urgent
- ✅ **RESOLVED** — confirmed resolved in a thread reply or follow-up message (cite who confirmed and when)
- 🔄 **IN PROGRESS** — partially addressed or acknowledged but not complete

Include the person responsible where tagged (e.g. *→ Joel to action*)

#### 🚢 Container Status
List all containers mentioned, grouped by status:
- **📋 Planned** — order not yet placed
- **🏭 In Production** — deposit paid, being manufactured
- **✈️ In Transit** — shipped, awaiting arrival
- **✅ Arrived** — received at warehouse

Format each container as:
`[Container ID] ([size if known]) — [relevant detail e.g. ETA, est. completion date]`

#### 💬 Other Activity This Week
Bullet point any messages sent in the channel this week that were not part of the summary or its thread. Include sender name and a brief summary of the message content. If there was no other activity, write *None this week.*

---

## Final Section — Cross-Regional Notes

After all 5 regions, add a brief **Cross-Regional Notes** section pulling out anything from `#general-inventory` that affects multiple regions (e.g. raw goods orders, PO process updates, Spain/France launch prep, etc.).

---

## Asana Task Creation
For every 🚨 and ⚠️ action point, create a task in Remy's Asana My Tasks (assignee: me). Do not add tasks to any project.

Each task should include:
- A clear task name prefixed with the region (e.g. "CA — Decision needed: release Heal now or wait for Remove 500ml?")
- A description with the full context and a reference to the source channel and summary date
- A due date based on the logic below
- Priority: high for 🚨, medium for ⚠️

### Due Date Logic
Use the regional review schedule and urgency level to set due dates:

| Urgency | Due Date Rule |
|---|---|
| 🚨 URGENT | 2 days from the summary date — needs attention before the next review |
| ⚠️ OPEN | Set to the region's next scheduled review day |
| ⁉️ NEEDS FOLLOW-UP | Set to 4 days from the summary date |

If the summary was posted late, adjust due dates relative to the actual summary date, not the scheduled day.

---

## Urgency Detection Rules
When scanning messages, flag as 🚨 URGENT if any of the following are present:
- ‼️ emoji in the original message
- Words/phrases: "urgent", "critical", "ASAP", "OOS", "out of stock", "stock out", "backorder", "desperate", "very urgent", "immediately", "today please"
- A named deadline that is within 48 hours of the summary date
- A stockout that is actively occurring with no inbound stock imminent

Flag as ⁉️ NEEDS FOLLOW-UP if:
- An action point is addressed to someone but no reply or acknowledgement exists in the thread or subsequent messages
- The same issue appeared in a prior week's summary and is still unresolved
- A message was sent asking a question with no response

---

## Tone & Style
- Keep action points concise — one line each
- Do not reproduce long message text verbatim; summarise clearly
- If a channel has had no activity in the past 7 days, note: *"No activity this week — last update was [date]."*
- The audience is the business owner (Joel) and inventory manager (Daniel) — keep it sharp and operational

---

## Post-Task
After completing the weekly summary, update `../Context/Current Issues.md` with the current state for all regions.
