---
name: photo-text-extraction
description: >
  Exact text from photos of signs/posters via tesseract OCR.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [OCR, Photos, Tesseract, Text-Extraction, Signs]
    related_skills: [ocr-and-documents, qr-barcode-decoding]
---

# Photo Text Extraction (signs, posters, displays)

## When to Use

- User sends a photo of a sign, poster, price list, event flyer, opening hours,
  or display and you must read it verbatim (dates, counts, email addresses).
- `vision_analyze` output gets truncated, or you need exact digits, not a
  summary.
- Anything printed on physical media that needs precise transcription.

When a user sends a photo of printed matter and you need the EXACT text — dates,
counts, email addresses — do NOT trust a single read. Two-step: tesseract OCR,
then cross-validate with `vision_analyze`.

## Why not vision_analyze alone

- The auxiliary vision model's analysis can get TRUNCATED mid-description on
  busy images (observed repeatedly: output ended after the intro paragraph even
  when asked to transcribe a date list verbatim).
- It summarizes; OCR transcribes. For exact digits, OCR wins.

## Prerequisite: Fix EXIF orientation

Phone photos often have EXIF orientation flags (especially `orientation=6` for
270° CW rotation) that tesseract cannot read. Always auto-orient first:

```python
from PIL import Image
img = Image.open(path)
exif = img.getexif()
orientation = exif.get(0x0112, 1)
if orientation == 3:    img = img.rotate(180, expand=True)
elif orientation == 6:  img = img.rotate(270, expand=True)
elif orientation == 8:  img = img.rotate(90, expand=True)
```

Without this, rotated text produces garbage OCR output even on good photos.

## Recipe: simple sign / poster (verified 2026-08, Barista-Kurs)

1. Get image size first after orientation fix:
   `python3 -c "from PIL import Image; print(Image.open(p).size)"` — crop
   regions are clipped silently beyond the bounds, so know the dimensions.
2. Crop the region of interest GENEROUSLY, with margin on the left — the first
   digit of a date column is the most commonly clipped part:
   `crop = img.crop((x0, y0, x1, y1))`.
3. Upscale 3–6x with `Image.LANCZOS` + `ImageOps.autocontrast` (or grayscale)
   so small digits become legible. Save as PNG.
4. `tesseract crop.png out -l deu --psm 6` — psm 6 = uniform text block, right
   choice for a poster body. `-l deu` helps with German umlauts (still
   imperfect — digits are the reliable part). Check `tesseract --list-langs`
   first.
5. Digits still missed? Use TSV mode for bounding boxes:
   `tesseract crop.png out -l deu --psm 6 tsv`, filter rows with `conf > 0`.
   The box coordinates reveal WHICH column got clipped.
6. Partial date reads (e.g. `3.07.26` — leading digit missing) mean the crop's
   left edge sits inside the column: re-crop FURTHER LEFT and/or upscale more,
   re-run. The leading day-digit is the last thing to come out.
7. Cross-validate: `vision_analyze` the upscaled crop with a SHORT, targeted
   question (e.g. "Antworte NUR mit der Liste, ein Datum pro Zeile") — short
   prompts truncate far less often. Two independent methods agreeing = reliable.
8. If the subject has a website, cross-check the OCR against the live page —
   signs go stale fast (the photographed course dates were all already past).

## Recipe: complex flyer / magazine page (Lidl, IKEA, event flyers)

Phone photos of multi-product flyers need a fundamentally different approach
because text is scattered across images, backgrounds, and large price boxes.

### Problem
- Tesseract on the full image yields garbage (photos, coloured backgrounds,
  rotated decorative text, small font mixed with giant price numerals)
- `vision_analyze` gives verbose *descriptions* but refuses to read exact
  prices and model numbers — it summarizes, it does not transcribe
- The auxiliary vision model (non-native, e.g. DeepSeek on OpenRouter) cannot
  do precise number extraction from photos of printed matter

### Approach

1. **Fix EXIF orientation** (see prerequisite above).

2. **Grid search** — divide the image into a 3×3 grid and OCR each cell with
   `tesseract -l deu --psm 6`. The cell containing the product name or price
   reveals itself by having readable text vs. the others returning only noise:
   ```python
   for row in range(3):
       for col in range(3):
           crop = img.crop((col*w//3, row*h//3, (col+1)*w//3, (row+1)*h//3))
           # tesseract each cell
   ```

3. **Narrow the winning cell** — subdivide into 6 horizontal strips and OCR
   each to locate the exact text line of interest (e.g. "Letzter Preis:" /
   "zum Drucktermin").

4. **Look for price text** — in Lidl-style flyers the price is near "Letzter
   Preis:" or labeled "je Stück". If the price box uses a large/decorative font
   that OCR cannot read, the price number may be invisible to tesseract.

5. **Web fallback** — when OCR identifies the product name but cannot read the
   price number (giant yellow font, decorative numerals), search the web for
   the product make + model + "Preis" / retailer name. This is often faster and
   more reliable than fighting OCR on price boxes:
   ```python
   web_search(f"Lidl {product_name} Preis 2026")
   ```

6. **Cross-check** — compare web price against any partial OCR finds (e.g.
   matching the last two digits). If they agree, trust the web result.

## Pitfalls

- Autocontrast can blow out glare; combine with a wider crop instead of relying
  on contrast alone.
- When cross-checking against a website: German pages ship umlauts as HTML
  entities (`Pl&auml;tze`, `&nbsp;`) — decode with `html.unescape()` before
  comparing (see cron-silent-watchdog for the monitor pattern).
- When numbers matter to the user, present the RAW OCR lines (dates, counts,
  email) in the reply — never a reworded summary.
- **EXIF orientation caught this session**: Even with a good photo, forgetting
  `img.rotate()` before cropping means tesseract sees rotated text and outputs
  noise. Always auto-orient first (see prerequisite above).
- **Non-native vision models cannot read numbers from photos**: Models like
  DeepSeek on OpenRouter (no native vision) produce verbose descriptions but
  refuse to transcribe exact prices, model numbers, or dates from photos of
  printed matter — even when asked explicitly with short, targeted questions.
  Do not waste iterations trying to coax digits out of them; fall through to
  OCR + web_search immediately.
- **Complex layouts defeat raw OCR**: A full-page Lidl flyer with images,
  coloured backgrounds, and rotated decorative elements yields garbage when
  fed whole to tesseract. Grid-search into cells first (see recipe above).
