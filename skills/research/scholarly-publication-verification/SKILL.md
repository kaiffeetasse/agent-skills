---
name: scholarly-publication-verification
description: "Verify citations; load and appraise scholarly papers."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Research, Citations, Bibliography, Fulltext, PDF, PeerReview, Appraisal]
    category: research
    related_skills: [grounded-citations, blocked-page-recovery, ocr-and-documents]
---

# Scholarly Publication Verification

Use when the user hands over a **bibliography entry, citation list, CV
publication list, or DOI/title** and asks to check it, load it, or summarize
it. Three phases, always in this order: verify the record → get the full text →
summarize *and* appraise. Skipping phase 1 wastes a retrieval cycle on a
mistyped title; skipping phase 3 turns a summary into an advertisement.

Typical triggers: "prüfe diese Publikationen", "kannst du beide Publikationen
laden und zusammenfassen", "is this citation right?", "give me the full text of
this paper".

## Phase 1 — Verify the record before believing any of it

Search the **exact title in quotes** plus one author surname, then open the
**publisher's own article page** — not the aggregator, not the snippet.

- The publisher page is authoritative for: author order, volume/issue, pages,
  year, DOI, ISSN.
- Many OA journals print a ready-made **BibTeX / ACMRef / EndNote block** on the
  article page. Extract that instead of retyping fields — it is the cheapest
  correct citation source.
- Compare **field by field** with the user's list and report ✓ / ⚠️ / ❌ per
  field with the correction. Real errors found in practice: missing year,
  missing page range, dropped leading article ("A framework…" cited as
  "Framework…"), wrong author-initial form, ISSN variant mismatch.
- **Initial-style lists hide the surname.** "Moumie S., Rafiuzzaman M." looks
  fine but the byline is "Moumie Soulemane" — surname *Soulemane*, so the
  citable form is "Soulemane, M.". Check the byline / Google Scholar profile
  before endorsing the initials.
- **ISSNs come in pairs.** Journals frequently have separate print and online
  ISSNs (IJCSI: Print 1694-0814 / Online 1694-0784). Either can be cited; say
  which one you verified. Journals also misprint their own ISSN in old PDF
  headers — trust the ISSN portal / publisher record over a scanned header.
- **Page ranges disagree between aggregators** (ProQuest said 249–259; other
  reference lists said 249–258). Quote the range you actually verified and note
  the discrepancy rather than silently picking one.
- If two list entries turn out to be the **same study published twice** (near
  identical text, mutual self-citation), say so plainly — see phase 3.

## Phase 2 — Get the full text, cheapest route first

1. **`web_extract` on the publisher article page** — gives abstract, index
   terms and the full reference list even when the PDF is gated.
2. **Publisher PDF: grep, never guess.** Fetch the landing page and look for the
   real href instead of guessing filename patterns:

   ```bash
   curl -sL -A "$UA" "<article-page-url>" -o page.html
   grep -oiE 'href="[^"]*\.pdf[^"]*"' page.html | sort -u
   ```

   Patterns vary wildly (IJCA uses
   `research.ijcaonline.org/volumeNN/numberM/pxc38<articleid>.pdf`). Guessed
   URLs return a 404 storm; the grep returns the file in one call.
3. **OpenAlex as OA locator + metadata cross-check:**

   ```bash
   curl -s "https://api.openalex.org/works?search=<urlencoded title>&per-page=3"
   ```

   Read `primary_location.pdf_url` and every `locations[].pdf_url`. Also gives
   you the DOI. Often `null` — that is a real "no OA copy", not a failure.
4. **Semantic Scholar graph API** (`api.semanticscholar.org/graph/v1/paper/search`
   with `fields=openAccessPdf,externalIds`) — returns **429 without an API key**.
   That is throttling, not absence: space out the retries, or move on.
5. **ResearchGate often already has the full text.** RG renders open-access
   uploads as HTML text on the publication page, so a `web_extract` of it can
   contain the whole paper — sections *and* references. The clean text is
   cached at `~/.hermes/cache/web/<host>-<hash>.md`; slice the paper region and
   you have a working full text with no PDF:

   ```bash
   sed -n '<first-paper-line>,<last-paper-line>p' ~/.hermes/cache/web/<file>.md \
     | sed 's/\\$//' | grep -v '^[[:space:]]*$' | cat -s > paper.txt
   ```

   Locate the boundaries first with
   `grep -nE '^[0-9]\.|Conclusion|References' <file>` and verify you captured
   through the reference list.
6. **Jina Reader on an RG PDF link will be Cloudflare-blocked** ("Just a
   moment…"). Don't burn calls on it; RG has no public PDF endpoint. If a live
   render is truly needed, it takes `JINA_API_KEY` (see
   `blocked-page-recovery`).
7. **"Site up but gutted" is a real state.** An OA journal's domain can answer
   200 with an index page containing nothing but `mailto:` links, while every
   paper URL 404s. That is an empty archive, **not** proof the paper doesn't
   exist — fall back to the RG/aggregator record, and check Wayback before
   declaring anything unavailable.
8. **`pdftotext` discipline:**
   - Always verify the text layer before summarizing:
     `pdftotext in.pdf - | wc -w`. Near-zero words ⇒ scanned page, needs OCR
     (see `ocr-and-documents`) — do not summarize an empty extraction.
   - **Plain mode scrambles tables** into a meaningless column-major stream.
     For any table you intend to quote, re-extract with
     `pdftotext -layout -f <p> -l <p> in.pdf -`.
   - **PDF page index ≠ printed page number.** For a 9-page article printed as
     pp. 7–15, printed p. 14 is PDF page 8. Find the page by paging, not by
     arithmetic on the wrong offset — and if one page range returns empty,
     adjust the range instead of concluding the content is missing.

## Phase 3 — Summarize *and* appraise

Structure the write-up so the user can check it:

1. Bibliographic header with the corrected fields (vol/issue/pages/year/DOI).
2. Problem & motivation (with the paper's own headline numbers).
3. Method, as the paper's own numbered steps.
4. Framework / figures, described as a flow.
5. Implementation & experimental setup (tools, machine, test data).
6. **Results with the actual numbers** — reproduce the table; don't say
   "results improved".
7. Conclusion + stated future work.
8. **Critical assessment** — separate section, never blended into the summary.

Critical-assessment checklist:

- **Venue repute:** check Beall's list (`beallslist.net/standalone-journals/`)
  and Scopus/WoS indexing. Say what it means for citability.
- **Duplicate publication:** near-identical text across two venues, with one
  citing the other, is one study counted twice. Report it as such and say which
  version to cite (usually the extended one) — and give the exact pages/DOI.
- **Evidence strength:** how many test domains, how many machines, is there a
  baseline, any precision/recall/coverage metric? "Higher coverage" backed only
  by growing word counts is a claim, not a measurement.
- **Internal inconsistencies:** tables whose columns contradict their own
  definitions (a counter that *falls* between levels while everything else
  grows; identical rows across all iterations) are worth flagging.
- **Do not equate venue repute with content quality.** A weak journal can hold
  a technically reasonable method; say both — "method is sound for its scope,
  venue is predatory, evidence is thin".
- **State the scope limits the authors themselves admit** (here: only GET forms
  with a single text field — a small slice of the deep web).

## Output conventions

- Answer in **German**, concise, with a per-field verification table
  (✓ / ⚠️ / ❌ + correction) before any summary.
- Numbers belong in a real markdown table, not prose.
- Deliver the retrieved PDF as a **chat attachment**: a line
  `MEDIA:/absolute/path.pdf`. Keep the extracted `.txt` full texts on disk and
  name their paths so the user can reuse them.
- End with a concrete offer (BibTeX entries, a half-page exposé), not a wall of
  options.

## Pitfalls

- **Trusting the user's fields.** Every one of them is a claim to verify.
- **Citing an aggregator as the record.** ProQuest/RG/Scholar snippets are
  leads; the publisher page is the source.
- **Guessing PDF URLs.** One grep of the landing page beats five 404s.
- **Reading 429 / Cloudflare / 404 as "does not exist".** Each has a distinct
  fallback; only an exhausted ladder justifies "unavailable" — and then say
  which routes you tried.
- **Summarizing from the abstract** when the full text was retrievable.
- **Quoting a table from plain `pdftotext` output.** It will be wrong.
- **Silently merging two versions of one paper** into one summary.

## References

- `references/worked-example-ijca-ijcsi.md` — full worked verification of the
  IJCA 2012 / IJCSI 2011 duplicates, with the exact commands that worked, the
  ones that failed, and the corrected citation fields.
