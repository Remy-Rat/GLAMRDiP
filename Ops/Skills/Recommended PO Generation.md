# Recommended PO Generation

Generates dated, qty-filled raw goods PO Google Sheets from supplier templates, ready to send to suppliers. One PO file per supplier.

## Inputs

- **Draft xlsx**: `~/Downloads/DRAFT SL Recommended.xlsx` (or wherever Daniel/Remy drops it). Sheet1, column V = Recommended PO qty per SKU. Column A = SKU, column C = supplier.
- **Template folder** (Shared Drive): `00 - TEMPLATES` inside the raw-goods PO root folder (`1briDpv-ADZERBMGUhm6_SCiovFbEK_1U`). One Google Sheet template per supplier, named `<SUPPLIER> - <CATEGORY> RECOMMENDED PO - TEMPLATE`.

## What gets generated

A new folder in My Drive root named `<dd-mm-yyyy> Recommended POs`, containing one Google Sheet per supplier with col V > 0 in the draft. Each file is renamed to its evaluated P.O. Reference, e.g. `02-06-2026 | Raw Goods PO | Glass Bottles | Isay Nail`.

For each PO:
- `C9` (yellow) set to today's date — drives the filename, the P.O. Reference (C8), and the Required Completion auto-calc (`=C9+30`).
- Yellow Qty column (D, E, or F depending on template) filled from draft col V.

## What gets skipped

- **KIT-* SKUs** — Palin gets a kit-component breakdown (inserts + outer boxes per kit type), not the rolled-up KIT SKU. That breakdown is done by hand based on production plans, not from the draft. The script leaves KIT rows at 0 and Remy/Daniel fills them after the script runs.
- **Suppliers not in the script registry**: Brooke (Perfection Pro Drill), Bill (Drill Bits), Alice (Nail Art Liners), Nancy (Nail Wipes), Sunny (Pro Beauty Box). Templates exist for these — add them to `ALL_TEMPLATES` if they come into a cycle.

## Supplier registry (12 suppliers, in template order)

| Supplier (template prefix) | Qty col | Category | Company (in PO Ref) |
|---|---|---|---|
| SALLY | D | Glass Bottles | Isay Nail |
| PALIN | E | Packaging | Elephant Color Printing |
| ELISE | E | Pro Files | Oslong |
| HEATHER | E | Bubble Mailers | Suzhou Star New Material |
| KAY | E | Cuticle Presser | Yiwu Pinpin E-commerce Firm |
| LINDA | F | Nail Tips | Yiwu Felice Cosmetic |
| MARK | D | Jars | Yiwu Pinpin E-commerce Firm |
| MICHELLE | E | Mani Mat | Huizhou Yongli Industrial Co |
| ANDY | E | Satchel | Shenzhen Hongxiang Packaging |
| SELENA | D | Remove Bottles | Butuo |
| 槐夏三时 (Bowls) | E | Remove Bowl | Huzhou Jianaier International Trade |
| ZOE | E | Deluxe Brush | Jiangxi Meichi Cosmetics |

## SKU naming drift (draft → template)

The draft uses some different SKU names than the templates. The script remaps these:

| Draft SKU | Template SKU |
|---|---|
| `ACC-TIP-{ALM,BAL,COF,SQU,STI}` | `LOOSE-TIP-{ALM,BAL,COF,SQU,STI}` |
| `{AU,UK/EU,CA}-EMPTY-JAR` | `{AU,UK/EU,CA}-ACC-JAR` |
| `{region}-EMPTY-REM-BOT-120` | `{region}-ACC-RE1-BOT` |
| `{region}-EMPTY-REM-BOT-500` | `{region}-ACC-RE5-BOT` |
| `ACC-NAI-MAT-002` (Nail Matt Box) | `ACCi-NAI-MAT-BOX` (Mani Mat Box; the `ACCi` typo is in the template) |
| `UK/EU-…` | falls back to `EU/UK-…` if needed (Sally matte bottle template has the order reversed) |

If new SKU drift shows up, add it to `SKU_REMAP` in `build_recommended_pos.py`.

## Supplier-specific rules

Templates with parent + accessory SKUs (lids/seals/inners/brushes per bottle or jar) have their accessory rows auto-totalled from the parent rows above. Configured per-supplier in `sum_total_rows` on `ALL_TEMPLATES` — each entry is `(sku, dst_row, sum_start_row, sum_end_row)` and the script writes `=SUM({qty_col}{start}:{qty_col}{end})` into the dst cell.

### Sally — glass bottle accessories
Three rows below the bottle list. Each bottle needs one of each:
- `EMPTY-GLASS-BOT-LID` (R41)   = SUM(D14:D40)
- `EMPTY-GLASS-BOT-BRUSH` (R42) = SUM(D14:D40)
- `EMPTY-GLASS-BOT-INNER` (R43) = SUM(D14:D40)

### Mark — jar accessories
Jars across the 3 regions all share the same lid and seal SKU:
- `ACC-JAR-LIDS` (R17)  = SUM(D14:D16) — UK/EU + AU + CA jar qtys
- `ACC-JAR-SEALS` (R18) = SUM(D14:D16)

### Selena — remove bottle accessories
Lids and inners are split by size (120ml = RE1, 500ml = RE5), each totalling its size's bottle rows:
- `ACC-RE1-LID` (R17) = SUM(D14:D16) — 120ml bottles (UK/EU + AU + CA)
- `ACC-RE1-INN` (R18) = SUM(D14:D16)
- `ACC-RE5-LID` (R22) = SUM(D19:D21) — 500ml bottles
- `ACC-RE5-INN` (R23) = SUM(D19:D21)

## Running it

```bash
python3 Ops/Scripts/build_recommended_pos.py            # all 11 suppliers
python3 Ops/Scripts/build_recommended_pos.py Sally      # just one
python3 Ops/Scripts/build_recommended_pos.py --date 2026-06-02   # backdate
```

Auth: needs an access token for `remy@glamrdip.com` with Drive + Sheets access. The script calls `gcloud auth print-access-token --account=remy@glamrdip.com`. If that fails, re-run `gcloud auth login --enable-gdrive-access` (see user-level CLAUDE.md notes).

Output is idempotent for the folder (won't create a duplicate if today's folder already exists) but **NOT** for the files inside — re-running will copy fresh templates each time, so delete old PO files first or change the date.

## Manual checks before sending

1. Open each generated PO. Check the yellow Qty cells look right (no `#REF!`, no obviously-wrong rounding).
2. Check the P.O. Reference (C8) text is correct — it's what the supplier sees and what becomes the filename.
3. Check Required Completion (C10) is 30 days out — fine 90% of the time but bump for Chinese New Year, big POs, etc.
4. For Palin: confirm the KIT rows have the manual breakdown (script leaves them at 0). E.g. "5,500 Complete inserts, 6,500 Complete outer box, 500 Ultimate insert".
5. For Sally: confirm the lid/brush/inner SUM resolves correctly (open the cell and check the formula).

## After-checks workflow (manual today, automatable later)

Once the POs in the dated staging folder look right, two follow-up steps land them in their permanent home and in Notion. **Always ask Remy before running either step** — the staging-folder review may catch an issue, and writes to the Shared Drive + Notion are visible to the wider team.

### Step A — move PO files into supplier folders (Shared Drive)

Each file moves out of `<dd-mm-yyyy> Recommended POs` (My Drive root) and into its supplier folder inside the raw-goods root (`1briDpv-ADZERBMGUhm6_SCiovFbEK_1U`, a Shared Drive). Use `files.update(addParents, removeParents, supportsAllDrives=True)` — the file ID and URL are preserved.

Supplier folder IDs:

| Supplier | Folder name | Folder ID |
|---|---|---|
| Sally | SALLY - BOTTLES | `1kyHAlclmlAYh_incApG4t0oBCDo1ufJ_` |
| Palin | PALIN - PACKAGING | `1-W7GdXdKS0A0JMmEz0k_1WlWg1T4V9sp` |
| Elise | ELISE - PRO FILES | `1Dbb2EQn_wKwh7VmozenIRPSbMzMAzFa9` |
| Heather | HEATHER - BUBBLE MAILERS | `1kaFGhsW-rn69Pc8Sc0FIXbj8ezPwY9yS` |
| Kay | KAY - CUTICLE PRESSERS | `1HhPPa9OdQkK2CyXeQGVCtwz9KDrXbAwA` |
| Linda | LINDA - NAIL TIPS | `1IK6yMXZ7ub3Mxgl1CTtxFn3kPuNOgyRG` |
| Mark | MARK - JARS | `1eq_cZ01G0U08DBGXFMFzKjG1dSo38XI-` |
| Michelle | MICHELLE - MANI MATS | `13_FJAdlxfj4OrAZ1Vfr-uYWn8RN1UN_K` |
| Andy | ANDY - SMALL SATCHELS | `12LYGV9EQf6taOJaGgwNKFz2b37KHpwLY` |
| Selena | SELENA - REMOVE BOTTLES | `1DIKxZsUMtg_a6OqDQIAmDcgyF-gSGF00` |
| Bowls | 槐夏三时 - REMOVE BOWLS | `1IbbCNDM5iR3PeEEEmDg5xCRN3-zgMoNr` |
| Zoe | ZOE - DELUXE BRUSH | `1vVNlyvYN3OC6zXupa50Cx4ZeC_6qmoQv` |

### Step B — create Notion entries in the Raw Goods Dashboard

**Ask first.** Then add one row per supplier to the Master Financial Database (`collection://2b8deea7-139d-81bb-891a-000bac531abe`) with these properties:

- `PO Short Reference` (title) + `PO Reference` (text) — both set to the same evaluated PO Ref, e.g. `02-06-2026 | Raw Goods PO | Glass Bottles | Isay Nail`
- `Region` = `ALL` (default — bump to a specific region if the PO is region-only)
- `Recommended PO` (url) = the Google Sheet share link
- `date:Order Date:start` = today (the C9 place date)
- `date:Est. Completion:start` = today + 30 days (or +25 for Mark/Kay; match the template's C10 formula)
- `Manufacturer` (select) = the Notion option matching the supplier — note these aren't all just "Sally" etc:
  - Sally → `Sally`
  - Palin → `Palin - Packaging`
  - Elise → `Elise - Pro Files`
  - Heather → `Heather - Bubble Mailers`
  - Kay → `Kay - Cuticle Pressers`
  - Linda → `Linda - Nail Tips`
  - Mark → `Mark - Jars`
  - Michelle → `Michelle - Nail Mats`
  - Andy → `Andy - Small Satchels`
  - Selena → `Selena - Remove Bottles`
  - Bowls (槐夏三时) → `Nico - Remove Bowl`
  - Zoe → `Zoe - Deluxe Brush`
- `PO Type` = `Raw Goods PO`
- `Status` = `Recommended`

The GD finance team fills the rest (Deposit/Balance amounts, Invoice, Purchase Order link, etc.) once they actually place the order.
