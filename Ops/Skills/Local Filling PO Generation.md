# Local Filling PO Generation

Generates dated, qty-filled Local Filling PO Google Sheets from supplier templates. Sibling to `Recommended PO Generation.md` (Raw Goods). One PO file per supplier per region per cycle — Local Filling POs are usually split by destination region, not consolidated like Raw Goods.

## Domain

"Local Filling" = liquid-filling work done in-region (UK/EU/CA) by partner manufacturers, as opposed to bulk CN filling. Each supplier owns one or more SKUs and fills them in the destination region's currency and lead time.

Suppliers (Shared Drive folders inside `11qPGIINWUMj1tndHray_Rt7nNjtteBnS`):

| Supplier | Folder name | Folder ID | Status |
|---|---|---|---|
| Chemence | CHEMENCE | `1mtiKOCDxl4TLTNLsgZZEuvOh-VdjZ1OR` | Live, scripted manually (see below) |
| Oils4Life | OILS4LIFE | `1vH5g2DJ1aSghN9d7EwK5ly9fCj7Bk-W4` | Template exists, not yet scripted |
| Liquipak | LIQUIPAK | `15E64vv5wkn6RUAweyl7udLfrBsmBxARm` | Template exists, not yet scripted |
| Swift Innovations | SWIFT INNOVATIONS | `1rFEJVDa7y2y40e2w_kT_fbPDUPowH3f_` | Template exists, not yet scripted |
| Outsource Packaging | OUTSOURCE PACKAGING | `1I-WavaVvCwq0fRxPmCAPOKiaofHCaBjJ` | Template exists, not yet scripted |

Templates folder: `00 - TEMPLATES` inside the Local Filling root = `1NSut5G5hWROTq_8-P__YQxlOm3hSFR6A`.

## Inputs

- The recommended qtys come from a separate planning step (POS Check / next-fill PO sizing per region) — there's **no consolidated draft xlsx** like Raw Goods has. The user gives qtys directly per region per SKU.
- For Chemence: typically qtys for `LIQ-BAS-2` (Base) and `LIQ-GLO-4` (Glow). `LIQ-SEA-3` (Seal) usually stays at 0.

## Naming convention

Filename — region included between the date and "Local Filling PO":

```
dd-mm-yyyy | <REGION> Local Filling PO | <Supplier>
```

Examples:
- `02-06-2026 | UK Local Filling PO | Chemence`
- `02-06-2026 | NORDIC Local Filling PO | Chemence`
- `02-06-2026 | EU Local Filling PO | Chemence`

The C8 P.O. Reference formula in each template evaluates to `dd-mm-yyyy | Local Filling PO | <Supplier>` **without** the region. That's the existing convention — do **not** edit the formula to add the region. The region only lives in the filename.

## Chemence specifics

### Template structure
- Sheet name: `Recommended Purchase Order`
- C8: PO Reference formula
- C9: P.O. Recommended Place date (yellow)
- C10: Required Completion — default formula `=C9+21` (3-week lead)
- R13: header — SKU | Name | Barcode | Qty | Unit price | Total price
- R14: `LIQ-BAS-2` — Base (Chemence Filled), unit price £0.90
- R15: `LIQ-SEA-3` — Seal (Chemence Filled), unit price £0.74 — usually 0
- R16: `LIQ-GLO-4` — Glow (Chemence Filled), unit price £0.90
- R17: Total = `=SUM(G14:G16)`

Qty col = `E`. Unit price col = `F`. Total = `G`.

### Completion dates often overridden
The default `=C9+21` is a starting point. Remy or Joel typically sets a hard completion date per PO based on shipping windows and Vik's production calendar. Overwrite C10 with a number value (date serial) — that replaces the formula with the hard date.

### Notion entries
Same Master Financial DB as Raw Goods (`collection://2b8deea7-139d-81bb-891a-000bac531abe`). For each PO add a row with:
- `PO Short Reference` (title) + `PO Reference` (text) = filename with region (e.g. `02-06-2026 | UK Local Filling PO | Chemence`)
- `Region` = **`UK` always for Chemence** (the Chemence tab on the Local Filling Dashboard filters by Region=UK). Destination region lives in the title. See `[[chemence-region-uk-in-notion]]`.
- `Manufacturer` = `Chemence`
- `PO Type` = `Local Filling PO`
- `Status` = `Recommended`
- `Recommended PO` = sheet share URL
- `Order Date` = today (= C9)
- `Est. Completion` = the hard-set C10 date

### Communicate completion dates to Vik
Vik (Chemence rep) needs to confirm each PO's target completion date so Chemence can plan production and the team can plan shipping. The Slack DM to Joel (DM `D09QFSDMK6G`) typically includes the completion date alongside each hyperlink so Joel can relay to Vik in one go.

## Other-supplier pattern (when one comes online)

When the next Local Filling supplier (Oils4Life / Liquipak / Swift / Outsource Packaging) lands in a cycle:

1. Open their template under `00 - TEMPLATES` and note: which row(s) have SKUs, which col is Qty, whether C8 formula includes "Local Filling PO" string.
2. Confirm the destination region convention — single PO covering all regions, or one per region like Chemence.
3. Confirm Notion Region value — does that supplier's tab also filter on UK, or does it use the real destination region?
4. Copy the template into the supplier's folder, set C9 + qtys, rename per the convention above, set C10 if overridden.
5. Ask before creating Notion entries (`[[ask-before-notion-writes]]`).

When the second supplier is wired up, this is when to consider a `build_local_filling_pos.py` script paralleling `build_recommended_pos.py`. Until then, the manual path is fine — Local Filling cycles are smaller (3–6 POs vs Raw Goods' ~12) and the qty inputs are bespoke per region.

## Manual checks before sending

1. Open each PO. Confirm yellow Qty cells, C9 place date, C10 completion date.
2. Confirm the C8 PO Reference text matches the filename pattern (minus the region).
3. Confirm the Total in G17 looks right.
4. Confirm Notion entry's `Region` matches the supplier's tab filter (UK for Chemence).
5. Confirm the Slack DM draft has completion dates alongside each link, since Vik handover depends on those dates.
