---
name: software-version-archaeology
description: Use when asked which version of a program first did X.
---

# Software Version Archaeology

Answer "which version first …" / "when was X introduced or removed" by **fetching and inspecting the real builds**, instead of trusting a wiki, forum post or blog. Secondary sources are for *locating* the boundary and cross-checking — the artifact is the evidence.

## When to use
- "What was the first version that …", "when did they stop …", "which build introduced …"
- A wiki/forum claim is hedged ("believed to be", "confirmed") or two sources conflict
- Legacy releases are needed as real files (Java jars, installers, ROMs, images) to analyse or run

## Evidence levels — label every claim
1. **Artifact-verified** — the build was downloaded and inspected (class names, bytecode, strings, hashes). Strongest.
2. **Contemporaneous documented** — release notes, IRC/mailing-list logs, changelog, issue comment from that day. A *statement*, not the artifact.
3. **Community claim** — wiki infobox/trivia, forum, blog, video. Weakest: use it to find the boundary, never as the final answer.

If the artifact is lost, say so and report level 2/3 explicitly. Never present a level-3 claim as verified (the user expects honest live verification — never claim).

## Workflow
1. **Find the machine-readable version index, not the download page.**
   - Vendor manifests/CDNs, e.g. Mojang: `https://piston-meta.mojang.com/mc/game/version_manifest_v2.json` → per-version json → `downloads.client.url` (on piston-data / launcher.mojang.com). Covers `old_alpha` back to `rd-132211`, `old_beta`, `release`.
   - Community vaults fill the pre-manifest gaps. Omniarchive: index `https://omniarchive.net/downloads/`, jars `https://vault.omniarchive.uk/archive/java/client-<era>/<id>.jar` (eras: preclassic, classic, indev, infdev, alpha, beta, release, april-fools, misc). Send a normal `User-Agent`; scrape hrefs ending in `.jar`.
   - Other fallbacks: archive.org collections, `meta.celestia.sh/versions/v1/<id>.json`, project mirrors.
2. **Enumerate → download into a cache dir keyed by version id**, skipping existing files so reruns resume. Append results to a JSON file in the workspace as you go — a timeout must not lose the batch.
3. **Scan the artifacts programmatically**: archive listing (zip/tar), leaf-name patterns, `javap -p` / `strings` for deeper checks. See `scripts/scan_jars.py`.
4. **Binary-search the transition**, then inspect the immediate neighbours *and* whether versions in between are lost/unarchived. Report "between A and B" when the first post-change build is missing.
5. **Cross-check the secondary source and read its footnote**: does it rest on the artifact or on something indirect? State which, and deliver both answers — "earliest confirmed by evidence = X, earliest surviving and directly checkable = Y".

## Obfuscation detection (Java jars)
First pass by class-name shape:
- Obfuscated: many single/two-letter leaf names, either at the jar root (`a.class`, `aa.class`) or in lettered packages (`com/mojang/minecraft/a/b`), few CamelCase names.
- Not obfuscated: readable dotted packages (`com/mojang/rubydung/Level`).

Confirm on one or two classes: `javap -p -classpath x.jar com.mojang.minecraft.a` → ProGuard output shows fields `float a; long b;` and methods `void a()`. Name shape alone is a heuristic, never the verdict.

## Pitfalls
- **A wiki's "confirmed" is not verification.** The Minecraft Wiki's "earliest obfuscated version = Classic 0.0.2a" rests on an IRC stack trace from that day (`at com.mojang.minecraft.a.g.a(Unknown Source)`); the jar itself is lost. Always open the cited reference before repeating the claim.
- **Dev/private builds ≠ release builds.** Some surviving old artifacts are private/dev builds and were never obfuscated (the launcher's `c0.0.11a` jar is actually an early 0.0.12a *dev build*). Do not generalise from an unrepresentative artifact — and do not let it "disprove" a release-side change.
- **Characteristics drift across the series.** Obfuscation/packaging style changed repeatedly (package-preserving single-letter names → flat root classes). Classify per build; never assume one scheme for a whole era.
- **Lost ≠ never existed.** Missing builds mean the boundary can only be bracketed, not pinned to a version number.
- **Long scans: the foreground terminal caps at 600 s.** Split into several medium calls or run `background=true, notify_on_complete=true`; cache per file so partial progress survives. Filter in Python, not with pipes (`| tail` masks exit codes).
- One jar per era is not a scan — walk the whole series; the interesting part is often exactly where you did not expect it (here: obfuscation predates Alpha by seven months).

## Support files
- `references/minecraft-java-builds.md` — endpoints plus the verified Minecraft: Java Edition obfuscation timeline (0.0.2a evidence claim → 0.0.12a first surviving obfuscated jar → Indev/Infdev style switch → Nov 2025 de-obfuscation).
- `scripts/scan_jars.py` — re-runnable classifier: point it at a directory of `.jar` files (or a URL list) and it reports class counts, short-leaf share and an obfuscation verdict per build.
