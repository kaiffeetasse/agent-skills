# Gridded puzzles in photos (Kreuzworträtsel, Gewinnspiel-Rätsel)

For "here's a photo of a printed puzzle, solve it" — contest/quiz crosswords printed on
flyers, packaging, or magazine pages. The clues are easy to read; the *grid geometry and
the numbered cells* are what defeats a casual read, and the answer is only verifiable if
every crossing letter is checked. Verified 2026-10-11 on a Krasser Stoff / Tony's
Chocolonely "Wunschkonzert" crossword (photographed flyer, 8 clues, 13 numbered cells).

## Order of work

1. **Read the clues first** — `vision_analyze` on the whole image plus 2-3 row strips.
   Clue text is large; that part is reliable. Transcribe the questions verbatim, including
   the exact wording (it decides the answer form: singular/plural, "wer", quotes).
2. **Derive the grid from pixels, not from eyeballing.** Photo shading makes several
   readings plausible; do the arithmetic.
3. **Solve the clues by research**, then **fit** them to the slot lengths.
4. **Verify every crossing letter** before writing the answer down.
5. Report the answer table *plus* the solution word with per-cell provenance.

## Grid extraction (PIL + numpy)

```python
a = np.array(Image.open(path).convert('RGB')).astype(int)
lum = a.mean(axis=2)
# 1) grid lines: columns/rows with many dark pixels
dark = lum < 110
cols = [i for i, c in enumerate(dark.sum(axis=0)) if c > 80]   # group runs of ±2 px
rows = [i for i, c in enumerate(dark.sum(axis=1)) if c > 80]
#    → line centres, cell pitch = spacing between lines (~65 px in a phone photo)
# 2) classify each cell by the CENTRE PATCH average (never a single pixel)
patch = a[y0+0.35*h : y0+0.65*h, x0+0.30*w : x0+0.70*w].reshape(-1,3).mean(axis=0)
avg = patch.mean(); r, b = patch[0], patch[2]
#    BLACK avg<95 | GRAY 95..152 | LIGHT avg>=186 and (r-b)>=20 | else paper background
```

- The **`(r-b) >= 20` saturation test** is what separates a light cell (~200,184,165)
  from the paper (~170,165,150). Brightness alone overlaps; hue does not.
- **Shadows fake absent cells**: a cell sitting in a shadowed band can read like paper.
  Before concluding a row/column is shorter, zoom that region with `vision_analyze`
  (row strip `[x0, y0, x1, y1]`) and look at it. Line-detection bands also *merge* two
  cells where a printed line is faint — cross-check the count visually.
- A **black square inside a clue's row = a space inside the answer**. The row then holds
  *two* cell groups that are one solution (3 cells + black + 6 cells = "MIA MORGAN").
- Rows are not necessarily aligned to the same column grid: the long bottom row started
  4 cells left of the main grid. Detect each band's own cell boundaries.

## Reading the tiny numbers in the shaded cells — montage, one vision call

13 separate `vision_analyze` crops is 13 round-trips. Instead: crop every shaded cell,
upscale 3x (`Image.LANCZOS`), and tile them into ONE image with the cell coordinates
drawn underneath, then one vision call reads all digits at once.

```python
S = 3; cell = 66*S; pad = 28
out = Image.new('RGB', (cols*(cell+pad)+pad, rows*(cell+pad+26)+pad), (255,255,255))
d = ImageDraw.Draw(out)          # d.text((x, y+cell+4), name, fill=(0,0,0)) as label
out.paste(im.crop(box).resize((cell, cell), Image.LANCZOS), (x, y))
```
Digits printed white-on-grey are unreadable at 1x and perfectly crisp at 3x.

## Solving rules that save the session

- **Numbered shaded cells = positions of the solution word** (usually a bottom legend
  strip of the same count). So: fill the answers, read the numbered cells in order, and
  the solution word falls out — and it *validates* the answers. Build it letter by letter
  and check it makes a real word before presenting it (e.g. `_ONZER_SOMM_R` → only
  KONZERTSOMMER fits, which forces the letters of three still-unknown slots).
- **Slot length = count of contiguous cells** in the clue's direction, black squares
  included as spaces. If a candidate answer from research does not match the slot's letter
  count, it is the wrong answer *for this grid* — do not stretch it.
- **Pin unknown answers by pattern, not by guessing.** From the crossings you get a mask
  (e.g. `??T?EK`, 2nd letter = 4th letter of the crossing word). Then fetch ONE
  authoritative list — the promoter's/venue's artist roster, the campaign page, the label's
  catalogue — and pattern-match against it. For the Kruasser-Stoff puzzle, fetching the
  119-act roster page (`/artists`) turned `??T?EK` into FITZEK and `___I_A` into BIBIZA in
  one call; guessing band names from memory produced nothing usable.
- **Distrust clue-fitting answers whose length is wrong.** "Kissin' Dynamite" is genuinely
  the 2026 20-year-jubilee act, but 14 letters ≠ 6 cells: the clue was a trap and the
  pattern was the tiebreaker. Research confirms a *candidate*; the grid decides.
- **When the puzzle belongs to a promo** (sponsor named, prize count named), its answers
  are almost always acts/products of that promo's universe — fetch the campaign page and
  the roster; the sponsor's own sweepstake page also gives the submission route and the
  **deadline** (check it against today's date before offering to help submit).
- Report per-cell provenance: `1 K (FITZEK, 6. Buchstabe) · 2 O (WUNSCHKONZERT, 8.) …`
  That is what makes the solution auditable instead of asserted, and it surfaces a wrong
  answer immediately (a letter that does not fit both words).
