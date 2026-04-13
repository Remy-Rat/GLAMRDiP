---
name: Use uv for Python dependencies
description: User prefers uv over pip for running Python scripts — no venvs, no global installs
type: feedback
---

Always use `uv run --with pandas,openpyxl python3 script.py` for xlsx analysis. Never use pip install.

**Why:** User doesn't want to manage pip installs or dependencies manually. uv handles everything via cache without polluting the system.

**How to apply:** Any time Python packages are needed, use `uv run --with <packages>` instead of pip. uv is installed via Homebrew.
