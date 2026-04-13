---
name: carton-fulfillment-labels
description: |
  Create warehouse carton fulfillment label PDFs containing product NAME, SKU, QTY, six fillable/pre-printable fields (BATCH NO, CARTON NO, GROSS WEIGHT, NET WEIGHT, DIMENSIONS, PO NUMBER), plus embedded EAN (product) and TUN (carton) barcodes from official supplier PDFs. Includes a self-service web app (label-app.py) for non-technical users to fill in fields and generate labels via browser. Use this skill whenever the user mentions carton fulfillment labels, warehouse labels, product identification labels with both EAN and TUN codes, or batch-producing labels for a product line where each label needs a GTIN-13 product code AND an ITF-14 carton code side by side. Also trigger on references to "instant gels labels", GLAMRDiP barcode processing, or any label task that needs dashed borders stripped from BarcodePlus / GS1 barcode PDFs.
---

# Carton Fulfillment Label Creator — Instant Gels

## TLDR

This skill creates warehouse fulfillment labels that carry both an **EAN product barcode** and a **TUN carton barcode** side by side, along with a product name, SKU, pre-printed quantity, and six fillable fields (BATCH NO, CARTON NO, GROSS WEIGHT, NET WEIGHT, DIMENSIONS, PO NUMBER). Any field can be pre-printed with a value or left as a blank handwriting line for the supplier to fill in manually. It was built originally for the **Instant Gels** product line, where each carton needs to be identified with both codes during supplier handover. The barcodes are pulled from official GS1 / BarcodePlus PDFs, cleaned of dashed dimension borders and "Actual width/height" annotations, and rendered as sharp pure-black-and-white rasters so there are no anti-aliasing artifacts.

A companion **web app** (`label-app.py`) provides a browser-based UI for non-technical users to fill in the six fields and generate labels without using the command line or Claude directly.

## When to use

- User wants carton fulfillment labels (not retail stickers - those use the `sticker-labels` skill)
- Each label must show BOTH an EAN-13 and an ITF-14 (TUN) barcode
- Label has six fillable fields (BATCH NO, CARTON NO, GROSS WEIGHT, NET WEIGHT, DIMENSIONS, PO NUMBER) - any can be pre-printed or left as blank handwriting lines
- Source barcode PDFs come from the GLAMRDiP / BarcodePlus provider with dashed dimension borders
- User has a data sheet spreadsheet with product names, SKUs, EAN numbers, TUN numbers, and quantities

## Label layout

Default page size: **A6 landscape (148mm x 105mm)**. Layout top to bottom:

1. **NAME: [Product Name]** - Helvetica-Bold 16pt, left-aligned
2. **SKU: [SKU Code]** - Helvetica-Bold 13pt, left-aligned
3. **QTY: [Quantity]** - Helvetica-Bold 12pt, left-aligned (pre-printed from data sheet's TUN QTY column)
4. **14mm logical gap** separating the header block from the fillable fields
5. **Three rows of paired fields** (Helvetica-Bold 10pt), each row 8.5mm apart:
   - Row 1: **BATCH NO:** ___ | **CARTON NO:** ___
   - Row 2: **GROSS WEIGHT:** ___ | **NET WEIGHT:** ___
   - Row 3: **DIMENSIONS:** ___ | **PO NUMBER:** ___
   - Each field either shows the pre-printed value or a blank handwriting line
6. **Two barcodes side by side** at the bottom:
   - EAN (PRODUCT) on the left
   - TUN (CARTON) on the right
   - Matched heights (~22mm), natural aspect ratios preserved
   - 16mm gutter between barcodes
   - Small caption "EAN (PRODUCT)" / "TUN (CARTON)" in 7pt centered below each

Outer border: 1.2pt rule offset 3mm from the page edges.

## CRITICAL: Barcode processing pipeline

The official barcode PDFs from the GLAMRDiP / BarcodePlus provider contain two problems that must be addressed:

1. **Dashed dimension borders and "Actual width/height" annotation text** that must be removed
2. **Tiny low-resolution raster images inside** (EAN 214x122px, TUN 270x122px) with grey anti-aliased edge pixels that cause visible speckle artifacts when scaled up via vector embedding

The solution is a four-step pipeline that combines techniques from two predecessor skills (`Barcode Processing Guide - EAN.md` and `sticker-labels-skill-tun-codes.md`):

### Step 1 - Clean the content stream

Strip the dashed border drawing commands and the "Actual width/height" text blocks from each barcode PDF's content stream.

**EAN PDFs** (GLAMRDiP EAN-13 format): the content stream contains, in order, line width, stroke colour, barcode image, three white rectangles, three text blocks for the numbers, two 8pt text blocks for the dimension labels, then the dashed border line segments. Keep through the **third** BT/ET block:

```python
from pypdf import PdfReader, PdfWriter

def clean_ean(src, dst):
    reader = PdfReader(src)
    writer = PdfWriter()
    writer.add_page(reader.pages[0])
    page = writer.pages[0]
    co = page.get("/Contents").get_object()
    data = co.get_data().decode('latin-1')
    pos = 0
    for _ in range(3):
        bt = data.find('BT\n', pos)
        et = data.find('ET\n', bt)
        pos = et + 3
    co.set_data((data[:pos] + '\n').encode('latin-1'))
    with open(dst, 'wb') as f:
        writer.write(f)
```

**TUN PDFs** (GLAMRDiP ITF-14 format): the content stream has a different order - image, four bearer bar line commands, white rectangle, ONE 20pt text block for the barcode number, then two 8pt text blocks for the dimension labels, then the dashed border segments. Keep through the **first** BT/ET block:

```python
def clean_tun(src, dst):
    reader = PdfReader(src)
    writer = PdfWriter()
    writer.add_page(reader.pages[0])
    page = writer.pages[0]
    co = page.get("/Contents").get_object()
    data = co.get_data().decode('latin-1')
    bt = data.find('BT\n')
    et = data.find('ET\n', bt)
    co.set_data((data[:et+3] + '\n').encode('latin-1'))
    with open(dst, 'wb') as f:
        writer.write(f)
```

### Step 2 - Render at 1200 DPI

```python
from pdf2image import convert_from_path
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

DPI = 1200
s = DPI / 72
ean_img = convert_from_path(cleaned_ean_pdf, dpi=DPI)[0]
tun_img = convert_from_path(cleaned_tun_pdf, dpi=DPI)[0]
```

### Step 3 - Crop to the barcode region

**EAN crop** - use a generous region that covers the dashed border area (the content stream cleanup already removed the dashed lines, so there's nothing to leak):

```python
# EAN crop (pixels at 1200 DPI from page origin top-left)
left=int(28*s); top=int(34*s); right=int(135*s); bottom=int(112*s)
ean_cropped = ean_img.crop((left, top, right, bottom))
```

**TUN crop** - derived from the proven MediaBox `[35, 663, 460, 802]` in the `sticker-labels` skill. Converting PDF bottom-origin y to pdfplumber top-origin y on an A4 page (841.89pt tall): y_top = 841.89-802 = 39.89, y_bot = 841.89-663 = 178.89.

```python
# TUN crop
left=int(35*s); top=int(39.89*s); right=int(460*s); bottom=int(178.89*s)
tun_cropped = tun_img.crop((left, top, right, bottom))
```

### Step 4 - Threshold to pure black/white

This is the critical step that kills the grey anti-aliased edge pixels from the source images. Without it, you get visible speckle/fringe artifacts around characters like the "8" in the EAN human-readable number.

```python
ean_bw = ean_cropped.convert("L").point(lambda p: 0 if p < 128 else 255, mode='1').convert("L")
tun_bw = tun_cropped.convert("L").point(lambda p: 0 if p < 128 else 255, mode='1').convert("L")
ean_bw.save("ean_hires.png")
tun_bw.save("tun_hires.png")
```

After this step every pixel is pure black (0) or pure white (255). The resulting PNGs are the sharp assets to embed in the label.

## Full label build code

The `fields` dict contains the six fillable values. Empty string = draw a blank handwriting line. Non-empty = print the value.

```python
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

def draw_field_row(c, y, x_left, x_right, label_a, val_a, label_b, val_b, font_size):
    """Draw two labelled fields side by side. If val is truthy, print it; otherwise draw a handwriting line."""
    c.setFont("Helvetica-Bold", font_size)
    mid = (x_left + x_right) / 2
    gap = 5*mm

    c.drawString(x_left, y, label_a)
    lw_a = c.stringWidth(label_a, "Helvetica-Bold", font_size)
    a_start = x_left + lw_a + 2*mm
    a_end = mid - gap/2
    if val_a:
        c.setFont("Helvetica", font_size); c.drawString(a_start, y, val_a)
        c.setFont("Helvetica-Bold", font_size)
    else:
        c.setLineWidth(0.8); c.line(a_start, y - 0.5*mm, a_end, y - 0.5*mm)

    x_b = mid + gap/2
    c.drawString(x_b, y, label_b)
    lw_b = c.stringWidth(label_b, "Helvetica-Bold", font_size)
    b_start = x_b + lw_b + 2*mm
    if val_b:
        c.setFont("Helvetica", font_size); c.drawString(b_start, y, val_b)
        c.setFont("Helvetica-Bold", font_size)
    else:
        c.setLineWidth(0.8); c.line(b_start, y - 0.5*mm, x_right, y - 0.5*mm)


def build_label(output_path, name, sku, qty, ean_png, tun_png, fields=None):
    """fields is a dict with keys: batch_no, carton_no, gross_weight, net_weight, dimensions, po_number.
    Empty/missing values produce blank handwriting lines."""
    if fields is None: fields = {}
    W, H = 148*mm, 105*mm
    c = canvas.Canvas(output_path, pagesize=(W, H))

    # Outer border
    c.setLineWidth(1.2)
    c.rect(3*mm, 3*mm, W-6*mm, H-6*mm)

    margin = 6*mm
    x = margin
    x_right = W - margin
    y = H - margin

    # NAME
    c.setFont("Helvetica-Bold", 16)
    y -= 5.5*mm
    c.drawString(x, y, f"NAME: {name}")

    # SKU
    y -= 6*mm
    c.setFont("Helvetica-Bold", 13)
    c.drawString(x, y, f"SKU: {sku}")

    # QTY
    y -= 5.5*mm
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x, y, f"QTY: {qty}")

    # 14mm logical gap then 3 rows of paired fields at 10pt, 8.5mm apart
    field_size = 10
    row_gap = 8.5*mm
    y -= 14*mm

    draw_field_row(c, y, x, x_right,
        "BATCH NO:", fields.get('batch_no', ''),
        "CARTON NO:", fields.get('carton_no', ''), field_size)
    y -= row_gap
    draw_field_row(c, y, x, x_right,
        "GROSS WEIGHT:", fields.get('gross_weight', ''),
        "NET WEIGHT:", fields.get('net_weight', ''), field_size)
    y -= row_gap
    draw_field_row(c, y, x, x_right,
        "DIMENSIONS:", fields.get('dimensions', ''),
        "PO NUMBER:", fields.get('po_number', ''), field_size)

    # Barcodes
    ean_pil = Image.open(ean_png)
    tun_pil = Image.open(tun_png)
    ean_ar = ean_pil.size[0]/ean_pil.size[1]
    tun_ar = tun_pil.size[0]/tun_pil.size[1]

    bc_h = 22*mm
    ean_w = bc_h * ean_ar
    tun_w = bc_h * tun_ar
    avail = W - 2*margin
    gutter = 16*mm
    if ean_w + tun_w + gutter > avail:
        f = (avail - gutter) / (ean_w + tun_w)
        bc_h *= f; ean_w *= f; tun_w *= f

    side = (avail - ean_w - tun_w - gutter) / 2
    ean_x = margin + side
    tun_x = ean_x + ean_w + gutter

    caption_gap = 4.5*mm
    bottom_pad = margin + 1.5*mm
    bc_y = bottom_pad + caption_gap

    c.drawImage(ImageReader(ean_png), ean_x, bc_y, width=ean_w, height=bc_h, mask='auto')
    c.drawImage(ImageReader(tun_png), tun_x, bc_y, width=tun_w, height=bc_h, mask='auto')

    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(ean_x + ean_w/2, bottom_pad, "EAN (PRODUCT)")
    c.drawCentredString(tun_x + tun_w/2, bottom_pad, "TUN (CARTON)")

    c.showPage()
    c.save()
```

## Data source

The skill expects an .xlsx data sheet with at minimum these columns (use the column names from the Instant Gels data sheet as the reference naming):

- **GLAMRDiP NAME** - product name for the NAME line
- **SKU** - SKU code for the SKU line
- **GTIN BARCODE** - 13-digit EAN product code (used to locate the matching EAN PDF)
- **TUN CODE** - 14-digit ITF-14 carton code (used to locate the matching TUN PDF). May be prefixed with "TUN:" and whitespace in the raw data - strip before matching
- **TUN QTY** - integer quantity pre-printed on the label as QTY

Barcode PDFs live in two sibling folders - one for EAN and one for TUN. Match them to data rows by extracting all digit sequences from each filename and checking if any known EAN/TUN code is a substring of the concatenated digits (same approach as `sticker-labels` skill):

```python
import re
def match_barcodes(folder, known_codes):
    barcode_map = {}
    for root, dirs, files in os.walk(folder):
        for f in files:
            if not f.endswith(".pdf"):
                continue
            all_digits = ''.join(re.findall(r'\d+', f))
            for code in known_codes:
                if code in all_digits and code not in barcode_map:
                    barcode_map[code] = os.path.join(root, f)
                    break
    return barcode_map
```

## Data sheet normalisation (important)

Before matching, normalise every row:

- **Name**: strip whitespace, replace `\n` with a space, then title-case (`' '.join(w.capitalize() for w in s.split())`). Some rows in the source sheet are lowercase, trailing-spaced, or contain embedded newlines.
- **SKU**: strip whitespace only (preserve case and internal hyphens).
- **GTIN (EAN)**: cast to int to drop the `.0` from openpyxl, then `.zfill(13)`.
- **TUN**: the column value is like `"TUN: 04897152410025"` or `"TUN:4897152410049"` or `"TUN:  04897152410247"`. Strip the `TUN:` prefix, strip all spaces, then `.zfill(14)`. Some rows are missing the leading zero in the sheet - zero-padding fixes this.
- **QTY**: cast to `int`.

## Step-by-step process

1. **Read the data sheet** with openpyxl, normalise every row per the rules above.
2. **Locate the two barcode folders** (one for EAN, one for TUN) and build filename-to-digits maps using `''.join(re.findall(r'\d+', filename))`.
3. **Cross-reference** - for every data row verify exactly one EAN PDF and exactly one TUN PDF match (substring match of the normalised code against the filename digits). Report any missing or ambiguous entries before proceeding.
4. **Ask the user two clarifying questions before batch processing**:
   - Output filename format (default: `CARTON STICKER - {SKU} - {NAME}.pdf`)
   - Individual PDFs per product vs single multi-page PDF
5. **Generate one sample label** for approval before batch processing. NEVER skip this step.
6. **On approval, sort rows by SKU** and batch generate - for each row: clean the EAN PDF (content stream), clean the TUN PDF (content stream), render both at 1200 DPI, crop, threshold to B/W, save temp PNGs, then build the label PDF. Clean up temp files between rows.
7. **Verify** - run the verification pass below against all generated PDFs before presenting them.

## Verification pass (mandatory)

After the full batch is generated, run a verification script that for every row in the sheet confirms:

1. The expected output file exists
2. The extracted PDF text contains the product NAME, SKU, and `QTY: {qty}`
3. Exactly one PDF in the EAN folder has the row's GTIN as a digit substring
4. Exactly one PDF in the TUN folder has the row's TUN code as a digit substring

```python
from pypdf import PdfReader

def verify(rows, labels_dir, ean_files_digits, tun_files_digits, name_fmt):
    errors = []
    for r in rows:
        path = os.path.join(labels_dir, name_fmt.format(**r))
        if not os.path.exists(path):
            errors.append(f"Missing: {path}"); continue
        txt = PdfReader(path).pages[0].extract_text() or ""
        if r['name'] not in txt: errors.append(f"{r['sku']}: NAME missing in text")
        if r['sku']  not in txt: errors.append(f"{r['sku']}: SKU missing in text")
        if f"QTY: {r['qty']}" not in txt: errors.append(f"{r['sku']}: QTY missing in text")
        ean_hits = [f for f,d in ean_files_digits.items() if r['gtin'] in d]
        tun_hits = [f for f,d in tun_files_digits.items() if r['tun']  in d]
        if len(ean_hits) != 1: errors.append(f"{r['sku']}: EAN source matches={len(ean_hits)}")
        if len(tun_hits) != 1: errors.append(f"{r['sku']}: TUN source matches={len(tun_hits)}")
    return errors
```

Report results as a per-row table (SKU, NAME, EAN, TUN, text OK, EAN source OK, TUN source OK) so the user can see the full result set at a glance.

## Web app (label-app.py)

A self-contained Flask web app lives alongside the data in the working folder. Non-technical users can open a browser, fill in the six fields, and generate all labels without touching the command line or Claude.

### How to run

```bash
cd "Instant gel test"          # or wherever the data sheet + barcode folders are
pip install flask pypdf pdf2image reportlab Pillow openpyxl --break-system-packages
python label-app.py
# Open http://localhost:5050
```

### What it does

1. Reads the data sheet on page load and lists all products with EAN/TUN match status
2. Shows six global input fields (all optional - blank = handwriting line on the label)
3. Products are shown with checkboxes (all selected by default, can deselect individual SKUs)
4. On "Generate Labels" click, the server runs the full 4-step barcode pipeline for each selected product and saves individual PDFs to the `CARTON STICKER LABELS/` folder
5. Reports success/failure with the list of generated filenames

### Dynamic - adding new products

The app reads the data sheet and scans the EAN/TUN folders fresh on every request. To add new products:
1. Add the row to the data sheet (name, SKU, GTIN, TUN code, qty)
2. Drop the EAN and TUN barcode PDFs into the respective folders (filename must contain the barcode number as digits)
3. Refresh the page - the new product appears automatically

### Configuration

The four folder paths are set at the top of `label-app.py`:
- `DATA_SHEET` - path to the .xlsx data sheet
- `EAN_FOLDER` - folder containing EAN barcode PDFs
- `TUN_FOLDER` - folder containing TUN barcode PDFs
- `OUTPUT_FOLDER` - where generated label PDFs are saved

If the folder structure changes (e.g. new product line with different folder names), update these paths.

## Dependencies

```bash
pip install flask pypdf pdf2image reportlab Pillow openpyxl --break-system-packages
```

Also requires `poppler-utils` (for pdf2image):
- macOS: `brew install poppler`
- Ubuntu/Debian: `apt install poppler-utils`

## Output

Default: one PDF per product, saved to a `CARTON STICKER LABELS/` subfolder under the working directory. Default filename format (what the user chose for the Instant Gels run):

```
CARTON STICKER - {SKU} - {Name}.pdf
```

e.g. `CARTON STICKER - INS-GLA-25001 - Glaze Check.pdf`. Always ask the user to confirm or change the naming format before batching - previous alternatives discussed include `{SKU} - {Name}.pdf`, `{Name}.pdf`, and `{SKU}.pdf`.

Alternative output formats the user may request:
- One multi-page PDF with all labels (set the PDF title metadata to `CARTON STICKER - {SKU} - {Name}` per page equivalent)
- Grouped by collection (the data sheet has a COLLECTION column)
- Different page size (A6 landscape is the default, but confirm if the user has specific printer/sticker stock requirements)

## Important notes

- ALWAYS generate a single test label and get approval before batch processing
- ALWAYS ask about filename format and single-vs-multi PDF output before batching (see clarifying-questions step)
- ALWAYS run the verification pass (NAME/SKU/QTY text + unique EAN source + unique TUN source) before presenting the final batch
- The barcodes MUST come from the supplied official PDFs, NOT regenerated with python-barcode. The official ones are guaranteed scannable and match the supplier's validated artwork
- The pure black/white thresholding step (Step 4 in the pipeline) is mandatory - without it you get visible speckle artifacts from the grey anti-aliased edge pixels in the source raster images
- The EAN and TUN cleanup uses DIFFERENT numbers of BT/ET blocks to keep (3 for EAN, 1 for TUN) because their content streams have different structures. Do not apply the EAN technique to TUN PDFs or vice versa
- Zero-pad GTIN to 13 digits and TUN to 14 digits before matching against filename digits - some sheet rows drop the leading zero on the TUN
- QTY is always pre-printed from the data sheet's TUN QTY column; the six fillable fields (BATCH NO, CARTON NO, GROSS WEIGHT, NET WEIGHT, DIMENSIONS, PO NUMBER) can be pre-printed or left as blank handwriting lines depending on what the user provides
- The web app (`label-app.py`) is the recommended way for non-technical users to generate labels. It reads the data sheet dynamically, so new products are picked up automatically when added to the sheet + barcode folders
- Current default barcode height (26mm) is below GS1's 80% minimum for both formats (EAN-13 min = 20.74mm tall, ITF-14 min = 41.28mm tall at 80%). For warehouse scanning this is generally fine, but if strict GS1 compliance is required the label size will need to increase
