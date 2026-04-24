# Claude Code — Using `--add-dir` to Share Context

A short guide for the Scale Labs / GLAMRDiP team on pointing Claude Code at our Obsidian "business brain" while working in a different project.

---

## What it does

`--add-dir` gives the Claude Code session access to a directory **outside** the one you launched it from. Claude can then Read/Grep/Glob files there — meaning you can bring GLAMRDiP context (SOPs, client notes, past recaps, people, style guides) into a session that's rooted in a totally different project.

Without `--add-dir`, Claude is sandboxed to the directory you launched it in and can't see anything above or beside it.

---

## Basic usage

Launch Claude Code from your working project and add the brain:

```bash
claude --add-dir ~/Documents/GD/glamrdip
```

Multiple directories are fine:

```bash
claude --add-dir ~/Documents/GD/glamrdip --add-dir ~/notes/clients
```

For a narrower scope (recommended when you only need a slice):

```bash
claude --add-dir ~/Documents/GD/glamrdip/Ops
```

---

## Read vs. write behaviour

**There is no built-in `--add-dir` read-only flag.** By default, any directory added this way is fully read/write — Claude can Edit, Write, and even delete files there.

Two options to constrain this:

### Option 1 — Tell Claude in the session

Just say it at the start:

> "Treat `~/Documents/GD/glamrdip` as reference only — do not write or edit anything in there."

Fine for ad-hoc sessions. Relies on Claude following the instruction.

### Option 2 — Enforce it via `settings.json` (recommended)

Add `permissions.deny` rules to `.claude/settings.json` (project) or `~/.claude/settings.json` (global). Deny rules take precedence over everything else, so Claude is hard-blocked from writing.

```json
{
  "permissions": {
    "deny": [
      "Edit(/Users/remy-m4/Documents/GD/glamrdip/**)",
      "Write(/Users/remy-m4/Documents/GD/glamrdip/**)",
      "NotebookEdit(/Users/remy-m4/Documents/GD/glamrdip/**)"
    ]
  }
}
```

Notes on path syntax:
- `/absolute/path/**` — matches everything under that directory, recursively
- `~/path/**` — home-relative also works
- You can also deny `Bash(rm *)` etc. if you want a belt-and-braces approach


---

## Persistent setup: `additionalDirectories`

If you always want the brain available without typing `--add-dir` every time, add it to `settings.json` on the project where you work:

```json
{
  "permissions": {
    "additionalDirectories": [
      "/Users/remy-m4/Documents/GD/glamrdip"
    ],
    "deny": [
      "Edit(/Users/remy-m4/Documents/GD/glamrdip/**)",
      "Write(/Users/remy-m4/Documents/GD/glamrdip/**)"
    ]
  }
}
```

This is the cleanest setup for recurring use — open Claude Code in any project and the brain is already attached, read-only.

---

## Use cases for the team

| Scenario | Setup |
|---|---|
| Drafting a campaign in a new folder, need product/colour context | `--add-dir ~/Documents/GD/glamrdip/Shared` |
| Writing code/docs in an unrelated project, want to reference SOPs | `--add-dir ~/Documents/GD/glamrdip/Ops` + read-only deny rules |
| Doing analysis on a CSV but need DSR context from past recaps | `--add-dir ~/Documents/GD/glamrdip/Archive` |
| Building something that *should* write back to the vault (e.g. a new recap) | `--add-dir` with no deny rules — full read/write |

---

## Tips

1. **Point at the smallest useful subtree.** Adding the whole vault works, but narrower = faster + more relevant. Grep over `Ops/` alone is tighter than grepping the entire vault.
2. **The vault's root `CLAUDE.md` auto-loads** when Claude enters that directory tree, so Claude already knows the vault map, team, and routing rules. You don't need to re-explain it.
3. **Check what's actually loaded.** If you're unsure, ask Claude: "What directories do you have access to right now?" It'll tell you.
4. **Deny rules are case-sensitive and path-exact.** Use absolute paths; don't rely on `~` expansion inside the JSON unless you've tested it.
5. **Combine with sandbox mode** for high-trust-but-verify workflows — defense in depth.

---

## Quick reference

```bash
# One-off, full access
claude --add-dir ~/Documents/GD/glamrdip

# One-off, narrow scope
claude --add-dir ~/Documents/GD/glamrdip/Ops

# Read-only via settings (add to .claude/settings.json in your working project)
# See "Option 2" above
```

Docs: <https://code.claude.com/docs/en/cli-reference.md> · <https://code.claude.com/docs/en/permissions.md>
