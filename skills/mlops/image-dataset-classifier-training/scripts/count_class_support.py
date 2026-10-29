#!/usr/bin/env python3
"""
Class-support probe for a cached feature directory.

Answers the question that decides the whole project design: how many images does each class
ACTUALLY have? Run this BEFORE promising "more images per class" or training a joint head.

  python3 count_class_support.py --dir <features_dir> [--mode part|part_color|color]

The chunks are .npz files written as `F` (float32 [n, dim]) + `meta` (one JSON string per row),
because np.array([dict, ...], dtype=object) silently collapses into a 2-D array of VALUES and
loses the keys. Hence the json.loads() below -- do not "simplify" it back to dicts.
"""
import argparse
import glob
import json
import os
import sys
from collections import Counter, defaultdict

import numpy as np

DEFAULT_DIR = os.path.expanduser(
    "~/workspace/lego-recognition/data/features/resnet18_128")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=DEFAULT_DIR)
    ap.add_argument("--mode", default="part_color", choices=["part", "part_color", "color"])
    ap.add_argument("--thresholds", default="2,3,4,8")
    args = ap.parse_args()

    chunks = sorted(glob.glob(os.path.join(args.dir, "*.npz")))
    if not chunks:
        sys.exit(f"no *.npz chunks in {args.dir}")

    counts = Counter()
    domains = defaultdict(Counter)
    n_features = 0
    dim = None

    for path in chunks:
        try:
            with np.load(path, allow_pickle=True) as z:
                F = z["F"]
                metas = [json.loads(s) for s in z["meta"]]
        except Exception as exc:                       # partial/corrupt chunk: skip, don't die
            print(f"  ! skipped {os.path.basename(path)}: {exc}")
            continue
        if dim is None and F.ndim == 2:
            dim = F.shape[1]
        for m in metas:
            if args.mode == "part":
                label = m.get("part_num", "?")
            elif args.mode == "color":
                label = m.get("color_id", "?")
            else:
                label = f"{m.get('part_num', '?')}|{m.get('color_id', '?')}"
            counts[label] += 1
            domains[label][m.get("source", "?")] += 1
        n_features += len(metas)

    thresholds = [int(t) for t in args.thresholds.split(",") if t.strip()]
    print(f"dir            {args.dir}")
    print(f"chunks         {len(chunks)}   features {n_features}   dim {dim}")
    print(f"label mode     {args.mode}")
    print(f"classes        {len(counts)}")
    print(f"max support    {max(counts.values()) if counts else 0}")
    for t in thresholds:
        n = sum(1 for v in counts.values() if v >= t)
        print(f"  >= {t:<3} images per class: {n}")
    multi = sum(1 for v in counts.values() if v >= 2)
    print(f"multi-domain   {sum(1 for c in domains.values() if len(c) >= 2)} classes have >=2 sources")
    print("\nbest-supported classes (label n -> sources):")
    for label, n in counts.most_common(8):
        print(f"  {label:<20} n={n}  {dict(domains[label])}")
    print("\nInterpretation: max support 1-2 means every 'joint' label is 1-shot -- train "
          "factorised heads (one per attribute) and combine them instead of a joint head.")


if __name__ == "__main__":
    main()
