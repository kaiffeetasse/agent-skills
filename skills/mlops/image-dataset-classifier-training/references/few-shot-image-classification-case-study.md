# Case study: few-shot image classification on a CPU-only box (LEGO parts, Sept 2026)

Worked example for the pipeline in `SKILL.md`. Concrete source URLs live in the user-owned skill
`lego-image-recognition`; this file records what the numbers actually were and which steps failed.
Host: 6 cores, 7.7 GB RAM (~3 GB usable), **no GPU**, ~20 GB free disk, heavy background load.

## Dataset (built from keyless sources: Rebrickable CDN + LDraw packs)

| stage | classes | images | notes |
|---|---|---|---|
| first pass (limits, 8 render colours) | 32 566 unique | 49 594 | 19 % of rows were byte-identical duplicate downloads |
| after expansion (every class + 20 colours) | 108 196–113 165 | 137 983 (9.4 GB) | manifest 147 229 rows |

Throughput: download 120–200 images/s (8 threads, keep-alive); feature extraction **40–55 img/s**
(frozen resnet18 @128 px, ~4 threads).

**The decisive measurement:** max support per (item, attribute) class = **2** — 16 029 classes with
exactly 2 (1 photo + 1 render), **zero classes with ≥3**. The source simply has one distinct image
per class; the early "37 images for one class" reading was duplicate downloads of the same URL.
Everything downstream follows from that.

## Results (frozen resnet18 @128 px + trained head, held-out split)

| task | classes | train/val | cosine top-1 | top-5 | linear | NCM | 1-NN |
|---|---|---|---|---|---|---|---|
| item recognition (attribute-independent) | 3 057 | 46 729/14 198 | **0.750** | 0.932 | 0.109 | 0.692 | 0.740 |
| attribute recognition (unknowns excluded) | 128 | 92 672/30 826 | **0.599** | 0.867 | 0.525 | 0.193 | 0.402 |
| item+attribute joint (≥2 images/class) | 16 029 | 16 029/16 029 | **0.141** | 0.311 | 0.120 | 0.161 | 0.161 |
| cross-domain (train renders → test photos+thumbs) | 16 029 | 16 029/16 029 | **0.226** | 0.406 | 0.172 | 0.303 | 0.303 |
| renders → real photos only | 1 230 | 1 230/1 230 | **0.865** | 0.924 | 0.853 | 0.864 | 0.864 |
| third-party-hosted images (different renderer) | 389 in vocab | — | 0.285 | 0.519 | — | — | — |

Reading it honestly:

* Same pipeline, 729 → 3 057 classes: 0.809 → 0.750 top-1. The model improved; the benchmark got
  4x harder. Always report accuracy **and** vocabulary.
* Attribute (colour) recognition is the weak task (~0.60) and the confusions are **exposure
  artefacts of the source photos**, not look-alike labels: Dark Blue→Blue (789), Dark Azure→Blue
  (733), Dark Red→Red (731), Trans-Clear→White (693), Light Bluish Grey→Black (552). Model colour
  separately, from renders, or as colour *families*.
* The joint head at 0.141 sits **below** 1-NN/NCM (0.161) → 1-shot joint recognition does not work
  with this data. The factorised alternative (separate item + attribute heads, combined) is the
  configuration to ship; `train_heads.py` prints it as `2-head combo` (part-only and colour-only
  top-1 on the same joint validation classes) so the two can be compared directly.
* Sim-to-real is real: 0.865 top-1 over 1 230 classes from renders alone. Renders are the cheapest
  way to get a second domain per class and to bootstrap before fine-tuning on photos.

## Failures and their exact symptoms (all cost real time)

| symptom | cause | fix |
|---|---|---|
| stall at exactly the 1000th image, zero errors | `log()` called while holding a non-reentrant `threading.Lock` → deadlock | `threading.RLock()`, log outside the lock |
| ~1.2 images/s instead of ~150/s | new TLS handshake per image (urllib default) | thread-local `http.client.HTTPSConnection` |
| OOM kill of the downloader (14:19) | 1.44 M-row CSV rows held as Python tuples | stream + reservoir sample |
| 19 % byte-identical files, `_1`/`_2` suffixes | filename = `<id>.jpg`, re-runs re-downloaded the same URLs | `md5(url)[:8]` in the filename + skip classes already in the manifest |
| `Killed` (exit 137) during evaluation, `total-vm: 15.8 GB` | `Xva @ Xtr.T` = 2.85 × 10⁹ floats ≈ 11 GB | batch the kNN/NCM/top-k passes (128–256) |
| `AttributeError: 'list' object has no attribute 'tolist'` | batched evaluator returns Python lists, preview code assumed tensors | `list(pred)` |
| README results table lost 4 of 5 tasks | `--only <task>` rewrote the aggregate summary with just that task | merge all `*_metrics.json` before writing the report |
| `TypeError: string indices must be integers` on the cache | chunk metadata is JSON **strings**; `dict(m)`/`tolist()` on the object array | `json.loads(s) for s in z["meta"]` |
| `--only partcolor3` reported 0 classes | no class has ≥3 images (max = 2) | expected, not a bug — that configuration is impossible with this data |
| 0/5 then 8/8 on the same sample | sampled images whose class was outside the model's 3 057-class vocabulary | filter by vocabulary before sampling; verify through the shipped CLI |

## Job-shape lessons on a weak host

* Feature extraction ran ~40 min for 91 660 images. **Resume-safe, path-keyed chunks** meant three
  killed batches cost only the in-flight chunk.
* `background=true` + `python3 -u … >> log 2>&1`, never `| tail` (buffers → looks hung).
* Training one task per process in a `set -e` loop: when the host killed the batch, the completed
  checkpoints survived and the resume cost minutes, not the whole run.
* Free RAM was the binding constraint (max ~5 GB); anything O(n²) over the dataset had to be batched.
