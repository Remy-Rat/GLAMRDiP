> **Context:** Get region info (Order Schedule sheet IDs in memory `reference_google_drive_sheets.md`, container reference labels from `../Context/Upcoming Orders.md`). Known Sally-side SKU mislabels are in memory `project_pl_sally_sku_quirks.md`.

# Packing List Reconciliation Skill

Reconciles a Sally CN packing list (the `PL-JS21-*.xls` Lily/Sally emails when a CN container is loading) against the OL column for that container in the Order Schedule. Surfaces overs, unders, missing lines, PL extras, and Sally's cell-level notes — in OL row order — so deviations can be raised with Sally before the container ships.

## Trigger
User asks to reconcile, check, or match a packing list against an OL / Order List / Order Schedule, or provides a Sally `PL-JS21-*.xls` for a specific container reference (e.g. "AUS 07062026", "CA 25072026"). Also trigger on "does Sally's PL match what we ordered", "any overrides on the PL", "what did Sally change".

---

## Inputs

1. **Sally's PL .xls** — emailed by Sally/Lily. Filename pattern `PL-JS21-<YYYYMMDD>-<n>*.xls`, usually with Chinese in parentheses (e.g. `(澳洲柜0326)更新6.9`). User typically drops it in `~/Downloads/`.
2. **Container reference** — the label as it appears in the Order Schedule POS MODEL row 6, e.g. `AUS 07062026`, `CA 25072026`. Confirm with user if not obvious from filename.
3. **Region** — determines which Order Schedule to download. The PL filename hint is usually enough (`澳洲` = AUS, `加拿大` = CA, `英国` = UK).

---

## Procedure

### 1. Pull the latest Order Schedule

Always re-pull. Greg updates OL values as Daniel revises the manifest — a stale schedule will show the wrong OL.

```bash
cd /Users/remy-m4/Documents/GD/PL_Recon
TOKEN=$(/opt/homebrew/share/google-cloud-sdk/bin/gcloud auth print-access-token)
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://www.googleapis.com/drive/v3/files/<SHEET_ID>/export?mimeType=application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" \
  -o <region>_order_schedule.xlsx
```

Sheet IDs in memory `reference_google_drive_sheets.md`.

### 2. Run the reconciliation script

```bash
cd /Users/remy-m4/Documents/GD/PL_Recon
uv run --with xlrd --with openpyxl python reconcile_pl.py \
  --pl "/Users/remy-m4/Downloads/PL-JS21-...xls" \
  --os <region>_order_schedule.xlsx \
  --ref "<REGION DDMMYYYY>" \
  --out <REGION>_<DDMMYYYY>_PL_vs_OL.xlsx
```

The script:
- Reads PL per-carton rows (block from row 9 to the `TOTAL` row, typically ~990)
- Sums by SKU; strips Sally's `AU-` / region prefix; applies known aliases (see memory `project_pl_sally_sku_quirks.md`)
- Rescues blank-SKU rows by matching colour code (PL col B) + product name against OL
- Pulls OL qty from the POS MODEL column whose row-6 label matches `--ref`
- Outputs xlsx with one row per OL line in row order, then PL-only extras, then unresolved blank-SKU rows

### 3. Read the output

Columns: `OL row | Product | OL SKU | PL SKU | OL Qty | PL Qty | Variance | Status | Notes`

Status colours:
- Green = Match
- Amber = Under (Sally short)
- Red = Over (Sally extra)
- Grey = OL-only (missing from PL) / PL-only (not in OL) / blank-SKU row

### 4. Walk variances with the user

For each non-green row, ask:
- **Over** — intentional uplift (e.g. kit qty bumped) or Sally over-fill? Get confirmation, save reasoning to context if it's a one-off.
- **Under** — known trim (Daniel told Sally to drop), or Sally short-supply? If short-supply, this is the leverage point — push back via Daniel/Lily before container ships.
- **OL only — not in PL** — discontinued/dropped item that shouldn't have been on OL (e.g. AUS 07062026 had `POW-TID-W006` Tidal Turn discontinued), or Sally missed it.
- **PL only — not in OL** — Sally adding a useful component (e.g. Heal inner not on OL) or shipping wrong item.
- **PL row missing SKU** — Sally PL template gap; flag for Sally to fix in next cycle.

### 5. New aliases / quirks
If a new SKU mislabel surfaces (Sally applies a wrong code), update the alias map in `reconcile_pl.py` (`PL_TO_OL_ALIAS` dict) and add a note to memory `project_pl_sally_sku_quirks.md`.

### 6. Post-recon
- Save the output xlsx in `/Users/remy-m4/Documents/GD/PL_Recon/` (it stays there as the working dir)
- Action items to flag to Daniel/Sally typically: SKU mislabels (so G3PL/247 doesn't check in against the wrong code), shortfalls worth pushing back on, PL-only extras worth confirming as intentional

---

## Outputs

- `<REGION>_<DDMMYYYY>_PL_vs_OL.xlsx` — colour-coded variance table in OL order
- Verbal/Slack summary of the non-green lines with the over/under interpretation per item

---

## Known Sally-side SKU quirks (AUS — extend as new ones surface)

See memory `project_pl_sally_sku_quirks.md` for the live list. Highlights:

- `AU-ACC-REM-500` on PL = empty Remove 500ml bottle (`ACC-RE5-BOT`), **not** filled Remove Solution. Sally's English label "Remove Solution (500ml)" is misleading — Chinese col B `500ml紫色塑料瓶` and ~49 g/unit weight confirm empty.
- `AU-POW-SEN-217` = Creme Brulee (`POW-CRE-217`) — Sally uses manufacturer's internal powder code.
- `AU-EMPTY-CAR-BOT` = Heal Empty Bottle (`HEA-EMP`).
- `EMPTY-GLASS-BOT-LID/BRUSH/INNER` = Heal Lid / Brush / Inner. INNER has no OL line — Sally side-corrects an OL omission.
- Colour rows sometimes ship with blank SKU; colour code (PL col B) + name match resolves them.

---

## Files

- Script: `/Users/remy-m4/Documents/GD/PL_Recon/reconcile_pl.py`
- Working dir: `/Users/remy-m4/Documents/GD/PL_Recon/`
- Memory: `reference_pl_recon_script.md`, `project_pl_sally_sku_quirks.md`
