> **Context:** Pairs with [Recommended PO Generation](Recommended%20PO%20Generation.md) (which covers PO build). Notion DB is the Master Financial DB (`collection://2b8deea7-139d-81bb-891a-000bac531abe`). Known supplier-side quirks in memory `accessory-sum-rules` (lid/brush/inner are qty-only, bundled in bottle pricing).

# Raw Goods PO Verification Skill

Covers the post-PO lifecycle for raw goods supplier orders (Sally, Mark, Selena, Butuo, Oslong, Elephant Color Printing, etc.). After we place a Recommended PO, the supplier issues a sequence of invoices (deposit → Balance #1 → Balance #2 if applicable) and a packing list. Each invoice needs to be **verified against the original Recommended PO before payment**.

## Trigger
User attaches a supplier invoice (deposit / balance) and asks to "verify before we pay", "check qty against PO", "match against raw goods order". Also trigger when the user mentions a Sally / Mark / Selena / supplier invoice in payment context.

---

## Full Lifecycle

```
[1] Place Recommended PO       → Notion entry created with Deposit / Balance #1 / Balance #2 amounts (AUD)
                                  Drive folder linked for Invoice and Purchase Order docs
[2] Supplier issues deposit    → User drops invoice xls in Downloads
[3] Verify deposit invoice     → THIS SKILL — qty + currency check vs Recommended PO
[4] Pay deposit                → Marked in Notion (Deposit Paid = Yes, receipt URL added)
[5] Supplier issues Balance #1 → Verify same way
[6] Pay Balance #1             → Marked in Notion (Balance #1 Paid = Yes)
[7] (If applicable) Balance #2 → Verify + pay same way
[8] Supplier issues PL         → Cross-check against PO + against shipped container (separate PL Reconciliation skill)
```

Steps don't happen in one sitting — they unfold over the production window (typically 25-30 working days for Sally CN). Each step is its own verification trip.

---

## Procedure for each invoice (steps 3, 5, 7)

### 1. Read the invoice xls
Sally / Mark / Selena invoice templates have: PI number, REF NO, date, line items (No / Product / Qty / Unit Price / Total Amount), TOTAL, DEPOSIT (or BALANCE), payment terms.

```bash
cd /Users/remy-m4/Documents/GD/PL_Recon
uv run --with xlrd python - << 'EOF'
import xlrd
wb = xlrd.open_workbook("/path/to/invoice.xls")
sh = wb.sheet_by_index(0)
for r in range(sh.nrows):
    print(r, [sh.cell_value(r, c) for c in range(sh.ncols)])
EOF
```

Note the PI Number and REF date — this is the lookup key for finding the Notion PO.

### 2. Find the Recommended PO in Notion
Search the Master Financial DB by date + supplier:
```
mcp__claude_ai_Notion__notion-search query: "<DD-MM-YYYY> <Supplier> Recommended PO <category>"
```
e.g. "02-06-2026 Sally Recommended PO glass bottle". The page title pattern is `DD-MM-YYYY | Raw Goods PO | <Category> | <Supplier>`.

### 3. Fetch the Notion page and grab the Recommended PO sheet link
```
mcp__claude_ai_Notion__notion-fetch id: <page_id>
```
Properties on the page include:
- `PO Reference` — full PO label
- `Recommended PO` — Google Sheets URL of the qty sheet
- `Deposit Amount` / `Balance #1 Amount` / `Balance #2 Amount` (AUD)
- `Deposit Paid` / `Balance #1 Paid` / `Balance #2 Paid` checkboxes
- `Status` (e.g. "Placed order (waiting payment)")
- `Invoice` and `Purchase Order` — Drive folder links

### 4. Pull the Recommended PO sheet
```bash
TOKEN=$(/opt/homebrew/share/google-cloud-sdk/bin/gcloud auth print-access-token)
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://www.googleapis.com/drive/v3/files/<SHEET_ID>/export?mimeType=application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" \
  -o supplier_po_<date>.xlsx
```
Sheet structure: row 13 header (SKU / Name / Qty), data rows below, with accessory rows (lid/brush/inner) at the end.

### 5. Match line-by-line
- Supplier invoice product names use label codes + region (e.g. `B114-AU - BOND` = AU region Bond bottle = `AU-EMPTY-BON-BOT` in our SKU taxonomy)
- Label code → region map: **B114=AU**, **B115=CA**, **B116=UK/EU**
- Compare invoice Qty vs Recommended PO Qty for each line
- Sum the invoice total; sum the PO line items × unit price

### 6. Currency check
**Notion totals are in AUD; supplier invoices are in USD.**
- Convert: USD invoice × FX rate → AUD; compare to Notion `Deposit Amount` / `Total Amount`
- Known rate as of 2 Jun 2026 PO: ~1.4259 USD→AUD
- Don't flag a $$ delta as a discrepancy until you've applied the conversion

### 7. Accessory rows (lid/brush/inner) are qty-only
Per memory `accessory-sum-rules`: Sally's `EMPTY-GLASS-BOT-LID` / `-BRUSH` / `-INNER`, Mark's `ACC-JAR-LIDS` / `-SEALS`, Selena's lids+inners are **summed from parent SKUs** and carry **no unit price**. They don't add to the invoice $$. If the Recommended PO total = invoice total (after FX), accessories are bundled in bottle pricing — don't expect a separate invoice for them.

### 8. Report
| Check | Result |
|---|---|
| Qty per line | N/N match (or list variances) |
| Total bottles/units | match |
| Invoice $$ vs PO $$ (after FX) | match |
| Deposit % (typically 30%) | matches Sally's payment terms note |

If clean → safe to pay. If qty variance > 0 → flag to user before payment.

---

## Suppliers seen so far

| Supplier | Pattern | Region prefix on invoice | Accessory SUM rows |
|---|---|---|---|
| Sally (Isay Nail) | Empty bottles, lids, brushes, inners | B114=AU, B115=CA, B116=UK/EU | LID, BRUSH, INNER |
| Mark | Jars | — | LIDS, SEALS |
| Selena | Remove bottles (120ml + 500ml) | — | LID, INNER (split by size) |
| Butuo | Remove bottles | — | (verify next cycle) |
| Oslong | Pro Files | — | n/a |
| Elephant Color Printing | Packaging | — | n/a |

---

## Files

- Working dir: `/Users/remy-m4/Documents/GD/PL_Recon/`
- Notion DB: `collection://2b8deea7-139d-81bb-891a-000bac531abe` (Master Financial Database)
- Related: `[Recommended PO Generation](Recommended%20PO%20Generation.md)`, `[Packing List Reconciliation](Packing%20List%20Reconciliation.md)`, memory `accessory-sum-rules`
