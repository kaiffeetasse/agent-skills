# Worked example: IJCA 2012 / IJCSI 2011 "hidden web indexing"

Session-recorded commands and outcomes. Everything below was actually run;
routes marked FAILED are recorded so a future session doesn't repeat them.

## The two list entries as handed over

```
Moumie S., Rafiuzzaman M., Mahmud H. — "Crawling the hidden web: An approach to
dynamic web indexing." IJCA (ISSN 0975-8887), Vol. 55, Nr. 1.

Mahmud H., Moumie S., Rafiuzzaman M. — "Framework for dynamic indexing from
hidden web." IJCSI (ISSN 1694-0784), Vol. 8, Nr. 5.
```

## Verified record (publisher pages)

| Field | Entry 1 (verified) | Entry 2 (verified) |
|---|---|---|
| Title | Crawling the Hidden Web: An Approach to Dynamic Web Indexing | **A** framework for dynamic indexing from hidden web |
| Authors (byline order) | Moumie Soulemane, Mohammad Rafiuzzaman, Hasan Mahmud | Hasan Mahmud, Moumie Soulemane, Mohammad Rafiuzzaman |
| Venue | International Journal of Computer Applications (IJCA) | International Journal of Computer Science Issues (IJCSI) |
| Vol / No | 55 / 1 | 8 / 5 (**No 2**) |
| Date | October 2012 | September 2011 |
| Pages | 7–15 | 249–259 (ProQuest) — 249–258 in other reference lists |
| DOI | 10.5120/8717-7290 | none |
| ISSN | 0975-8887 | Print 1694-0814 / Online 1694-0784 |
| Publisher | Foundation of Computer Science (FCS), NY, USA | IJCSI Publication (Mahebourg, Mauritius) |
| Affiliations | IUT Board Bazar, Gazipur-1704, Bangladesh + Manarat International University, Dhaka | IUT, Gazipur-1704 |

Corrections to report: missing year and page range (both entries), dropped
leading "A" (entry 2), missing issue sub-number "No 2" (entry 2), ISSN needs
the print/online qualifier (entry 2), surname of "Moumie S." is *Soulemane*.

## Phase 1 — what worked

- `web_search` on the exact quoted title + one surname → publisher landing page
  (`ijcaonline.org/archives/volume55/number1/8717-7290/`) plus ProQuest,
  ResearchGate, Google Scholar records.
- `web_extract` of the IJCA article page returned the page's own
  **ACMRef / BibTeX / EndNote block** → pages 7–15, DOI, ISSN, issue date in one
  shot. No field retyping needed.
- The IJCA page's reference list [23]/[24] cited the IJCSI paper by title → that
  is how the duplicate-publication relation was spotted.
- Beall's-list check: `web_search "IJCSI Beall's list predatory delisted Scopus"`
  → `beallslist.net/standalone-journals/` lists *International Journal of
  Computer Science Issues*. IJCA (FCS) is unindexed low-repute but not listed.

## Phase 2 — retrieval, exactly what happened

IJCA (worked):

```bash
# guessed patterns -> 404
#   https://www.ijcaonline.org/archives/volume55/number1/moumie-2012-ijca-908717.pdf
#   https://www.ijcaonline.org/archives/volume55/number1/8717-7290.pdf
# grep the landing page instead:
curl -sL -A "$UA" "https://www.ijcaonline.org/archives/volume55/number1/8717-7290/" -o page.html
grep -oiE 'href="[^"]*\.pdf[^"]*"' page.html | sort -u
# -> https://research.ijcaonline.org/volume55/number1/pxc3877290.pdf
curl -sL -A "$UA" -o ijca_55-1_7-15.pdf "https://research.ijcaonline.org/volume55/number1/pxc3877290.pdf"
file ijca_55-1_7-15.pdf        # PDF document, version 1.5, 9 page(s)
pdftotext ijca_55-1_7-15.pdf ijca.txt   # 5825 words -> real text layer
```

IJCSI (no PDF obtainable — but full text obtained anyway):

- FAILED: direct download `researchgate.net/.../A-framework-for-dynamic-indexing-from-hidden-web.pdf` → **403**
- FAILED: `ijcsi.org/papers/IJCSI-8-5-2-249-259.pdf` and www variant → **404**
- FAILED: `ijcsi.org/index.php?view=volume8issue5` → **200 but gutted**: a
  1658-byte page whose only hrefs are `mailto:` links. Site up, archive empty.
- FAILED: `r.jina.ai/<RG-pdf-url>` → **403 Cloudflare "Just a moment..."**
- FAILED (throttle, not absence): Semantic Scholar
  `api.semanticscholar.org/graph/v1/paper/search?...&fields=openAccessPdf` →
  `{"message": "Too Many Requests"}` 429 on two attempts
- WORKED: OpenAlex API gave DOI for entry 1 and `null` pdf for entry 2 —
  correct "no OA copy" answer:
  `api.openalex.org/works?search=framework%20for%20dynamic%20indexing%20from%20hidden%20web`
- WORKED (the actual full text): the earlier `web_extract` of the **ResearchGate
  publication page** had rendered the open-access upload as HTML text, cached at
  `~/.hermes/cache/web/www.researchgate.net-68717b0e69.md`. It contained the
  complete paper (sections 1–6 + References).

```bash
grep -nE '^[0-9]\.\s*[A-Z]|^[0-9]\.[0-9]|Conclusion|References' \
  ~/.hermes/cache/web/www.researchgate.net-68717b0e69.md | head -60
# paper body: ~line 182 (1.Introduction) .. ~1690 (end of References)
sed -n '170,1690p' ~/.hermes/cache/web/www.researchgate.net-68717b0e69.md \
  | sed 's/\\$//' | grep -v '^[[:space:]]*$' | cat -s > ijcsi.txt   # 4939 words
```

Table extraction (the trap):

```bash
pdftotext -layout -f 13 -l 14 ijca_55-1_7-15.pdf -   # EMPTY
pdftotext -layout -f 7  -l 8  ijca_55-1_7-15.pdf -   # correct: printed 13-14
```

9-page PDF printed as pp. 7–15 ⇒ offset 6. Plain (non-`-layout`) mode had
scrambled Table 4 into an unusable stream; `-layout` on the right page gave:

```
Iteration | Level | Links | Words R | Words D | Time(level 2)
5         | 1 / 2 | 282 / 259  | 2034 / 3746  | 854 / 1095 | 0'48
10        |       | 608 / 565  | 4143 / 7727  | 1461/1917 | 1'04
50        |       | 3096/2750  | 20396/38680 | 5592/7155 | 10'51
```

## Phase 3 — appraisal notes actually delivered

- The two papers are **one study, twice published**: ~80 % verbatim overlap;
  IJCA (2012) is the extended version (adds Jaccard similarity detection, Java/
  NetBeans + Karmasphere/Cloudera implementation, experimental setup, Table 4,
  result analysis, 7 vs 5 limitations) and cites the IJCSI paper as ref [23].
- Evidence is thin: one test domain (`www.dmoz.org`), one consumer PC
  (Core2 Duo 2.80 GHz, 4 GB RAM, 25–30 kbps), no baseline, no precision/recall.
- Table 4 contradicts itself: "Links" *falls* from 282 (level 1) to 259
  (level 2) while every other counter grows, and level-1 rows are identical
  across all iterations.
- Venue: IJCSI on Beall's list and dropped from Scopus ~2013; IJCA unindexed
  low-repute. Content still stated as scope-limited but coherent.
