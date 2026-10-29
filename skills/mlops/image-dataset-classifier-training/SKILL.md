---
name: image-dataset-classifier-training
description: Build image datasets from web sources; train classifiers.
version: 1.0.0
author: Hermes
license: MIT
metadata:
  hermes:
    tags: [computer-vision, dataset-building, image-classification, cpu-training, few-shot]
    related_skills: [huggingface-hub, lego-image-recognition, data-acquisition-patterns]
---

# Image dataset building + local classifier training

## When to Use

* "Download all images you can find of X and train a recognition model locally" (brickognize-style
  part/object recognizers, product/defect/category classifiers).
* Harvesting a large image corpus from a public CDN or API into a labelled local dataset.
* Training/evaluating an image classifier on a **CPU-only, low-RAM** box (no GPU, ~8 GB RAM).
* Any task where classes have very few images each (1–3) — few-shot / 1-shot classification.

A worked, fully measured instance of this pipeline (LEGO parts, keyless sources) lives in the
user-owned skill `lego-image-recognition`; use it for the concrete URLs. This skill holds the
**transferable** method and the traps.

## Pipeline shape (proven end to end)

```
1. catalog         keyless CSV/JSON metadata dumps -> local SQLite/CSV (part/item + attribute per row)
2. candidates      stream the big dump, dedupe by URL, sample (reservoir) -> list of image URLs
3. download        keep-alive HTTP, 8 threads, deterministic filenames, skip existing -> data/images/<class>/<id>_<hash>.jpg
4. manifest        append one JSON row per saved file: path, class keys, source/domain, size
5. QA              count files vs manifest rows, md5-dedupe, class-support histogram, contact sheets
6. features        frozen ImageNet backbone -> cached feature chunks (resume-safe, path-keyed)
7. heads           train classifiers on the CACHED features (seconds-minutes, re-runnable)
8. eval            batched top-1/top-5 + baselines (linear / NCM / 1-NN) + OK/MISS preview grids
```

Decoupling 6 from 7 is the single most valuable design decision: a long feature extraction that
dies must never force you to re-train, and a head experiment must never cost another extraction.

## Rules that keep the dataset honest and the runs survivable

1. **One distinct image per class is the norm, not a bug.** Measure availability *per class* before
   promising "more images per class" (a global URL dedupe makes every class look like it has 1 —
   see `scripts/count_class_support.py`). If the source has one image per class, extra images can
   only come from another **domain** (product photo vs. thumbnail vs. render) — never re-downloading.
2. **Report accuracy together with vocabulary size.** 0.81 over 729 classes and 0.75 over 3 057
   classes are not "worse" — the benchmark got 4x harder. Always state both, or the number is
   meaningless.
3. **Factorise joint labels.** "part+colour"-style joint heads are 1-shot when each class has ~1
   image and reach *below* trivial baselines; the same data trained as two separate heads and
   combined is the usable product. Measure and print the combination, don't just the joint head.
4. **md5-dedupe before splitting train/val**, then re-check class support *after* dedupe (dedupe
   silently destroys the only multi-image classes you had).
5. **Batch every O(n_val × n_train) computation.** At 16 k classes / 30 k val images the similarity
   matrix is ~2.9 × 10⁹ floats (>11 GB) → the OOM killer ends the run (exit 137). Batch size 128–256.
6. **One task per process** (`--only <task>`), or a single failing task costs the whole batch. A
   `set -e` loop of per-task invocations is the right shape.
7. **Head choice dominates feature quality**: on frozen features, a cosine classifier with learnable
   scale beat a plain linear probe by ~7x at 3 k classes (0.750 vs 0.109) and 3x at 729 classes
   (0.809 vs 0.281). Always train several heads on identical features — it is nearly free — and
   report linear / NCM / 1-NN as sanity baselines. If a linear probe trails 1-NN, your head is wrong,
   not your data.
8. **Sim-to-real works**: a head trained purely on renders transferred to real photos (0.865 top-1
   over 1 230 classes; 0.226 over the full 16 k classes that include low-res thumbnails). Renders
   are cheap, controllable augmentation — bootstrap with them, then fine-tune on real photos.
9. **Do not present a measured weak number as a capability.** A 1-shot joint head at 0.141 top-1
   against 0.161 for 1-NN means "this configuration does not work" — say so, and name the
   configuration that does.

## Pitfalls (each one cost real time)

1. **Keep-alive is mandatory** for bulk image downloads: one TLS handshake per image = ~81 ms/req vs
   ~21 ms keep-alive; throughput collapses from ~150/s to ~1/s. One `http.client.HTTPSConnection`
   per worker thread (thread-local).
2. **Never load a multi-GB metadata dump into RAM** (a 1.4 M-row CSV with Python tuples = swap
   death / OOM kill). Stream it and use reservoir sampling for a uniform subset.
3. **`threading.Lock` + a log call inside the lock = silent deadlock** (it stopped at exactly the
   1000th image). Use `RLock()`.
4. **Filenames must derive from the content/URL** (`md5(url)[:8]`) and re-runs must skip classes
   already in the manifest, otherwise every re-run re-downloads the same URLs as `_1`, `_2`, …
   (19 % byte-identical garbage in the first attempt, plus wasted bandwidth).
5. **`np.array([dict, ...], dtype=object)` silently collapses into a 2-D array of values** and loses
   the keys. Store metadata as **JSON strings** in npz chunks and parse with
   `json.loads(s) for s in z["meta"]`. Symptom of getting it wrong: `TypeError: string indices must
   be integers` or `ValueError: dictionary update sequence element #0 has length 1`.
6. **`pkill -f <script>` kills your own shell** because the pattern matches your own command line.
   Use `pkill -f 'script[.]py'`.
7. **Long jobs: `background=true` + `python3 -u … > log 2>&1`.** Never pipe to `tail` (buffers, hides
   progress); foreground terminal calls die at ~420 s. Make every stage **resume-safe** — the host
   killed several batches mid-run, and only checkpoints survived.
8. **Preview/plot code must accept the type the batched evaluator returns** (Python lists, not
   tensors): `pred.tolist()` → `AttributeError: 'list' object has no attribute 'tolist'`.
9. **A single-task run overwrites the aggregate summary file.** Regenerate the merged summary from
   the per-task metric files before writing any report/README from it.
10. **Verify with a real end-to-end call on the final artifact** before reporting: run the shipped
    inference CLI on images of *known* label and check the vocabulary filter — sampling images whose
    class is outside the model's vocabulary makes any model look broken (0/5 vs 8/8 once filtered).

## Support files

* `references/few-shot-image-classification-case-study.md` — the measured numbers, the wrong turns,
  and the exact failure symptoms from the LEGO run (LEGO parts, 124 k images, CPU only).
* `scripts/count_class_support.py` — re-runnable probe: reads the cached npz feature chunks and
  prints class support + domain mix. Use it before promising "more images per class".
