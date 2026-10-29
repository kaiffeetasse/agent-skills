---
name: lego-image-recognition
description: Build LEGO part-image datasets keyless; train recognizer.
version: 1.1.0
author: Hermes
license: MIT
metadata:
  hermes:
    tags: [lego, bricklink, rebrickable, dataset, image-classification, computer-vision]
    related_skills: [huggingface-hub, local-llm-inference, marketplace-price-research]
---

# LEGO / BrickLink image dataset + local part recognizer

## When to Use

* Building an image dataset of LEGO parts / minifigs / sets, especially "all images you can find".
* Identifying a LEGO part from a photo **locally** (brickognize-style part + colour prediction).
* Questions about BrickLink APIs, `img.bricklink.com` image URLs, or keyless LEGO catalog data.
* Working in `~/workspace/lego-recognition/` (README.md documents everything, `scripts/` the pipeline).

## Facts about BrickLink APIs (measured)

* `api.bricklink.com` **always** needs OAuth 1.0a: without keys it returns
  `401 {"description":"PARAMETER_ABSENT: OAuth Parameters are Missing"}`. Requirements: BrickLink
  account + **registered seller**, consumer key/secret, **registered static IP**, 5 000 calls/day.
  There is **no** keyless BrickLink API. Every GitHub "bricklink api" repo
  (brickstore, BricklinkSharp, bricklink_py, ryansh100/bricklink-api, davesweb/bricklink-api …)
  is only a client for that same gated API.
* `img.bricklink.com` images work **without login**: `ItemImage/PN/<bl_color>/<part>.png`,
  `SN/0/<set>.png`, `MN/0/<fig>.png`; legacy `P/<color>/<part>.jpg`. No robots.txt there, but the
  API terms forbid storing their content beyond ~24 h → use as small eval set, not a corpus.
* BrickLink colour ids: scrape `www.bricklink.com/catalogColors.asp`; parse `<tr>` rows containing
  `colorID=(\d+)`, then `re.match(r"(.+?)\s+LEGO Color:", text)` → 214 colours, maps ~146/275
  Rebrickable colour names. (BL "Light Bluish Gray"=86, "Dark Bluish Gray"=85, White=1, Black=11.)

## Keyless sources that actually work (verified)

| source | URL | notes |
|---|---|---|
| catalog CSVs | `cdn.rebrickable.com/media/downloads/{parts,colors,elements,inventory_parts,…}.csv.gz` | `inventory_parts.csv` (133 MB) contains ~199 k ready image URLs |
| element photos | `cdn.rebrickable.com/media/parts/elements/<element_id>.jpg` | 192×192 real photos |
| part photos | `cdn.rebrickable.com/media/parts/photos/<color>/<part>-<color>-<uuid>.jpg` | 500×500 real photos |
| sets / figs | `cdn.rebrickable.com/media/sets/<set_num\|fig_num>.jpg` | 28 k + 17 k images |
| LDraw renders | `cdn.rebrickable.com/media/downloads/ldraw/parts_<color_id>.zip` | 150–220 MB per colour, all parts, PNG per part |
| LDraw library | `library.ldraw.org/library/updates/complete.zip` | 145 MB, render your own angles |

Licence: Rebrickable data/images may be used commercially **with attribution**; LDraw is CCAL.
Rebrickable forbids page scraping but allows automating the file downloads ≤1×/day.

**Hard limit of the source (measured):** exactly **one distinct image per (part, colour)** —
113 165 classes, one image each. "37 images for one class" in an early run were duplicate
downloads of the same URL, not distinct photos. So more *distinct* images per class can only come
from another **domain** (element photo / large photo / LDraw render / BrickLink render), never
from re-downloading. Design the dataset around domains, not around per-class counts.

## Pipeline

```bash
cd ~/workspace/lego-recognition
python3 scripts/fetch_catalog.py                                  # CSVs
# breadth: every class that exists (limit 0 = all, skips classes already present per source)
python3 scripts/build_dataset.py --source parts_elements --limit 0 --workers 8 --per-class-cap 1
python3 scripts/build_dataset.py --source parts_photos   --limit 0 --workers 8 --per-class-cap 1
python3 scripts/build_dataset.py --source sets|minifigs  --limit 5000  --workers 8
# second domain per class: 20 colours x (parts present in the manifests)
python3 scripts/build_dataset.py --source renders --limit 2500 --workers 8 \
        --render-colors 0,15,71,72,4,14,1,19,70,2,28,25,272,320,27,47,41,5,11,34
python3 scripts/analyze_ceiling.py                                # how much exists per class (per-class dedupe!)
python3 scripts/analyze_domains.py                                # domain coverage per class
python3 scripts/report_dataset.py                                 # QA + contact sheets
python3 scripts/extract_features.py --size 128 --chunk 1500       # resume-safe, reuses cached rows
python3 scripts/train_heads.py --size 128                         # all tasks + metrics + previews
python3 scripts/train_heads.py --size 128 --only <tag>            # single task (overwrites _summary.json!)
python3 scripts/aggregate_summary.py                              # merge all *_metrics.json -> _summary.json
python3 scripts/summarize_results.py                              # writes README results section
python3 scripts/eval_on_bricklink.py --tag parts_r18              # domain-shift eval
python3 scripts/recognize.py --image <file> --tag parts_r18       # single-image inference
```

Measured throughput: **120–200 images/s** download (8 threads, keep-alive), **40–55 features/s**
(resnet18 @128 px, ~4 threads, CPU only).

## Pitfalls (all hit for real)

1. **Keep-alive is mandatory.** A fresh TLS handshake per image → 81 ms vs 21 ms per request;
   throughput collapses from ~150/s to ~1/s. Use one `http.client.HTTPSConnection` per worker
   thread (thread-local).
2. **Never hold the 1.4 M-row `inventory_parts.csv` in RAM** on a small box — stream it and use
   reservoir sampling for a uniform subset, otherwise the OOM killer ends the run.
3. **`threading.Lock` + a logging call inside the lock = silent deadlock** (stalled at exactly
   1 000 images). Use `RLock()`.
4. **Filename must be derived from the URL** (`md5(url)[:8]`), and re-runs must skip classes already
   present in that source's manifest (`existing_classes()`), otherwise every re-run re-downloads the
   same URLs under `_1`, `_2` … and you get 19 % byte-identical garbage plus wasted bandwidth.
5. **md5-dedupe before splitting train/val** — but check class support *again after* dedupe, because
   dedupe destroys multi-image classes.
6. **Batched evaluation is mandatory at scale.** With 16 029 classes × 30 826 val images,
   `Xva @ Xtr.T` is 2.85 × 10⁹ floats (≈ 11 GB) → `Killed` (exit 137). Do kNN/NCM/top-k in batches
   of 128–256 (`chunked_knn_accuracy`, `eval_head_batched`, `eval_ncm_batched` in `train_heads.py`).
   A single-task OOM also costs the whole resume batch — check `dmesg -T | grep 'Out of memory'`.
7. **Batched evaluators return Python lists** — `pred.tolist()` then fails with
   `AttributeError: 'list' object has no attribute 'tolist'`. Wrap in `list(...)`.
8. **`train_heads.py --only <tag>` rewrites `models/_summary.json` with just that one task.**
   Always run `aggregate_summary.py` before `summarize_results.py`, or the README table loses tasks.
9. **Head choice dominates**: frozen resnet18 + **cosine classifier with learnable scale** beats a
   plain linear probe by ~7× at 3 057 classes (0.750 vs 0.109 top-1). NCM/1-NN are honest sanity
   baselines (0.692/0.740). Always report several heads.
10. **`pkill -f build_dataset` kills your own shell** (the pattern matches your command line) →
    use `pkill -f 'build_dataset[.]py'`.
11. Long jobs: `background=true` + `python3 -u … > log 2>&1` (never `| tail`, it buffers and hides
    progress); foreground terminal calls die at ~420 s. Make jobs **resume-safe** (skip existing
    files, chunked feature cache, one `--only` task per process) — the harness/other services can
    kill a long batch, and only the completed checkpoints survive.
12. Colour recognition stays the weakest task (~60 %) because product photos have inconsistent
    exposure: Dark Blue→Blue, Dark Azure→Blue, Dark Red→Red, Trans-Clear→White, LBG→Black dominate
    the errors. Model colour separately, from renders, or as a colour-family task.

## Results (CPU only, no GPU — frozen resnet18 @128 px + cosine head)

| task | classes | train/val | top-1 | top-5 | linear | NCM | 1-NN |
|---|---|---|---|---|---|---|---|
| part recognition (colour-independent) | 3 057 | 46 729/14 198 | **0.750** | 0.932 | 0.109 | 0.692 | 0.740 |
| colour (unknown colours excluded) | 128 | 92 672/30 826 | **0.599** | 0.867 | 0.525 | 0.193 | 0.402 |
| part+colour joint (≥2 images/class) | 16 029 | 16 029/16 029 | **0.141** | 0.311 | 0.120 | 0.161 | 0.161 |
| cross-domain (train renders → test photos+elements) | 16 029 | 16 029/16 029 | **0.226** | 0.406 | 0.172 | 0.303 | 0.303 |
| LDraw renders → real photos | 1 230 | 1 230/1 230 | **0.865** | 0.924 | 0.853 | 0.864 | 0.864 |
| BrickLink-hosted images, part model | 389 in vocab | — | 0.285 | 0.519 | — | — | — |

**Factorised heads instead of a joint head (the important result).** Every part+colour class has at
most **2 images total** (one photo-family, one render) — measured: 16 029 classes with exactly 2,
**zero** with ≥3. A joint `part+colour` head therefore trains on ~1 image/class and collapses
(0.141 top-1). Training *separate* part and colour heads on the same split and combining them gives
**3.4× more**: joint top-1 **0.483** / top-5 **0.822** (part-only 0.632, colour-only 0.774;
3 950 parts × 20 colours). Cross-domain (train renders): combo 0.249/0.563 vs joint 0.226/0.406.
So: never ship a joint head — predict part and colour with two heads and combine (or use one of the
countless multi-domain render packs for a third image per class).

Honest reading: accuracy and vocabulary size trade off — the part task went 0.809 (729 classes) →
0.750 (3 057 classes) → the model is better, the benchmark is 4× harder. The joint task needs
**≥3 images per class**; with exactly 2 (one train, one val) no head beats the trivial baselines,
so do not present that number as a recognition capability. Part-alone + colour-alone heads are the
useful product; combine them instead of training the joint head.
