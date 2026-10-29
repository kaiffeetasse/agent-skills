#!/usr/bin/env python3
"""Classify a series of Java jars as obfuscated vs. readable.

Point it at jars already on disk, or at a file of URLs to fetch first.
The verdict is a heuristic on class-name shape; confirm one class per era with
`javap -p -classpath <jar> <class>` (a ProGuard class shows `float a; long b;`
fields and `void a()` methods).

Usage
-----
    python3 scan_jars.py /tmp/mcjar/*.jar
    python3 scan_jars.py /tmp/mcjar                 # walks the dir
    python3 scan_jars.py --fetch urls.txt --cache /tmp/mcjar --json out.json
    python3 scan_jars.py /tmp/mcjar --javap 1       # show members of 1 class per jar

Exit code is always 0 unless no jar could be read.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
import zipfile

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}
SHORT = re.compile(r"[a-z]{1,2}")
CAMEL = re.compile(r"[A-Z][A-Za-z0-9]{2,}")


def fetch(urls_file: str, cache: str) -> list[str]:
    os.makedirs(cache, exist_ok=True)
    paths = []
    with open(urls_file) as fh:
        for line in fh:
            url = line.strip()
            if not url or url.startswith("#"):
                continue
            dest = os.path.join(cache, os.path.basename(url))
            if not os.path.exists(dest):
                try:
                    req = urllib.request.Request(url, headers=UA)
                    with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as out:
                        out.write(r.read())
                    print(f"fetched {os.path.basename(url)}", flush=True)
                except Exception as exc:  # noqa: BLE001
                    print(f"FAILED {url}: {exc}", file=sys.stderr, flush=True)
                    continue
            else:
                print(f"cached  {os.path.basename(url)}", flush=True)
            paths.append(dest)
    return paths


def classify(path: str) -> dict:
    with zipfile.ZipFile(path) as z:
        names = [n[:-6] for n in z.namelist() if n.endswith(".class") and not n.startswith("META-INF")]
    leaves = [n.split("/")[-1] for n in names]
    short = sum(1 for leaf in leaves if SHORT.fullmatch(leaf))
    camel = sum(1 for leaf in leaves if CAMEL.fullmatch(leaf))
    total = len(names) or 1
    verdict = "OBFUSCATED" if (short > 10 and camel < total * 0.3) else "readable"
    roots = sorted({n.split("/")[0] for n in names})
    sample = sorted(set(n for n in names if "/" not in n))[:3] or sorted(set(names))[:3]
    return {
        "jar": os.path.basename(path),
        "classes": len(names),
        "short_leaf": short,
        "camel_leaf": camel,
        "short_pct": round(100 * short / total, 1),
        "verdict": verdict,
        "root_packages": roots[:4],
        "sample": sample,
    }


def javap_probe(path: str, count: int) -> list[str]:
    with zipfile.ZipFile(path) as z:
        classes = [n[:-6].replace("/", ".") for n in z.namelist()
                   if n.endswith(".class") and not n.startswith("META-INF")]
    out = []
    for cls in sorted(classes)[:count]:
        try:
            res = subprocess.run(["javap", "-p", "-classpath", path, cls],
                                 capture_output=True, text=True, timeout=60)
            out.append(f"--- {cls}\n{res.stdout.strip() or res.stderr.strip()}")
        except Exception as exc:  # noqa: BLE001
            out.append(f"--- {cls}\njavap failed: {exc}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", help="jar files or directories to scan")
    ap.add_argument("--fetch", metavar="URLS_FILE", help="file with one jar URL per line; download into --cache first")
    ap.add_argument("--cache", default="/tmp/mcjars", help="download directory (default /tmp/mcjars)")
    ap.add_argument("--javap", type=int, default=0, metavar="N", help="show javap members for the first N classes of each jar")
    ap.add_argument("--json", help="also write the result table to this JSON file")
    args = ap.parse_args()

    paths = list(args.paths)
    if args.fetch:
        paths += fetch(args.fetch, args.cache)

    jars = []
    for p in paths:
        if os.path.isdir(p):
            jars += [os.path.join(p, f) for f in sorted(os.listdir(p)) if f.endswith(".jar")]
        else:
            jars.append(p)
    if not jars:
        print("no jars given (pass paths or --fetch)", file=sys.stderr)
        return 1

    rows = []
    print(f"{'jar':32s} {'classes':>7s} {'short%':>7s}  verdict")
    for jar in jars:
        try:
            row = classify(jar)
        except Exception as exc:  # noqa: BLE001
            print(f"{os.path.basename(jar):32s} {'-':>7s} {'-':>7s}  UNREADABLE ({exc})")
            continue
        rows.append(row)
        print(f"{row['jar']:32s} {row['classes']:7d} {row['short_pct']:7.1f}  {row['verdict']}")
        if args.javap:
            for block in javap_probe(jar, args.javap):
                print("    " + block.replace("\n", "\n    "))

    if args.json:
        with open(args.json, "w") as fh:
            json.dump(rows, fh, indent=1)
        print(f"wrote {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
