# Minecraft: Java Edition — archived builds & the obfuscation timeline

All figures below were produced by downloading the actual jars and inspecting them
(2026-10-08). Use this as the worked example for `software-version-archaeology`.

## Endpoints that work

| Source | What it has | How |
|---|---|---|
| Mojang `piston-meta` | Full release/snapshot list + `old_alpha`/`old_beta` | `https://piston-meta.mojang.com/mc/game/version_manifest_v2.json` → entry `url` → JVM json → `downloads.client.url` |
| Omniarchive vault | Pre-manifest builds (Classic 0.0.12a–0.0.29, all Indev, most Infdev) + server jars | index `https://omniarchive.net/downloads/`, page per era, jars `https://vault.omniarchive.uk/archive/java/client-<era>/<id>.jar` (eras: `preclassic classic indev infdev alpha beta release april-fools misc`). Needs a normal `User-Agent`. |
| minecraft.wiki | Version metadata, per-version trivia, obfuscation-map article | `https://minecraft.wiki/w/Java_Edition_<era>_<version>` |
| `meta.celestia.sh` | Per-version `.json` metadata for old builds | linked from wiki infoboxes |

Manifest coverage at time of check: 61 `old_alpha`/`old_beta` entries — pre-classic `rd-132211` … `rd-161348`,
`c0.0.11a`, `c0.0.13a(_03)`, `c0.30_01c`, `inf-20100618`, then `a1.0.4` … `a1.2.6`, `b1.0` … `b1.8.1`.
**Not** in the manifest (Omniarchive only): Classic `0.0.12a`–`0.0.29`, all Indev (2009-12-23 … 2010-02-23), most Infdev.
Omniarchive listing counts seen: classic 28 jars, indev 23, infdev 27.

Skipping existing files in the cache dir is what makes a 100+ jar scan survive timeouts — name each download by its version id.

## Verified obfuscation timeline

| Build | Date | `.class` count | Verdict (artifact-verified) |
|---|---|---|---|
| `rd-132211` | 2009-05-13 | 13 | readable — `com/mojang/rubydung/Level` |
| `c0.0.11a` (launcher jar) | launcher build is an **early 0.0.12a dev build** | 37 | readable — dev build, never obfuscated |
| `c0.0.12a_03` | 2009-05 (0.0.12a = 2009-05-19) | 33 | **obfuscated** — `com/mojang/minecraft/a/a/…`, fields `float a; long b;`, methods `void a()` (javap-confirmed) |
| `c0.0.13a_03` | 2009-05 | 44 | obfuscated, same scheme |
| `c0.0.14a_08` … `c0.30*` | 2009-05 … 2009-12 | 51–181 | obfuscated; package skeleton kept (`com/mojang/minecraft/level/tile/a`), a few kept names (`MinecraftApplet`, `Entity`, `Level`, `AABB`) |
| `in-20091223-1459` (first Indev) | 2009-12-23 | 113 | obfuscated (`com/mojang/minecraft/a/…`, `net/minecraft/a/a/…`) |
| `inf-20100227-1433` … `inf-20100625-1917` | 2010-02 … 2010-06 | 289–358 | obfuscated, letters inside packages |
| `inf-20100627` → `inf-20100630-1835` | 2010-06-27 … | 356–363 | **scheme switch**: flat root classes `a.class`, `aa.class`, `ab.class` |
| `a1.0.4` … `b1.8.1` | 2010-07 … 2011-09 | 375–881 | flat root scheme; only `net/minecraft/client/MinecraftApplet.class`, `net/minecraft/isom/IsomPreviewApplet.class` kept |
| `a1.1.0` and later | 2010-09 … | 473+ | additionally `net/minecraft/client/Minecraft.class` kept readable |
| `26.4-snapshot-3` | 2026-10-06 | 11504 | **not obfuscated** (`net/minecraft/client/Camera`, `…/ClientBootstrap`), 0 short-leaf names |

So, answering the session's question: **earliest version with documented evidence of obfuscation = Classic 0.0.2a (2009-05-16);
earliest surviving jar that is directly verifiable as obfuscated = Classic 0.0.12a (`0.0.12a_03`)**.
Obfuscation is therefore ~7 months older than Alpha — not an "early Beta" thing as forum folklore says.

## Secondary-source cross-check (do this, and read the footnote)

- `minecraft.wiki/w/Java_Edition_Classic_0.0.2a` → Trivia: *"This is the earliest version of Minecraft confirmed to have its code obfuscated."*
  The citation is the TigIRC log of 2009-05-16: `(13:45:03) PFawkes: at com.mojang.minecraft.c.run(Unknown Source)` /
  `(13:45:20) PFawkes: at com.mojang.minecraft.a.g.a(Unknown Source)`. The jar itself: **"Client not archived"** → evidence level 2, not level 1.
  The old fandom mirror states it flatly ("This was the first version of Minecraft to have its code obfuscated") — that flattening is exactly the trap.
- End of obfuscation: minecraft.net article *"Removing obfuscation in Java Edition"*; the `25w46a` (2025-11-11) infobox lists **both** an Obfuscated and an Unobfuscated client download. Verified independently: the current release client jar contains zero short-leaf class names.
- Related: obfuscation *maps* have shipped in `client.json` from `19w36a` onward (`minecraft.wiki/w/Obfuscation_map`), useful for remapping old crash traces.

## Minimal scan recipe

```python
import json, urllib.request, os, zipfile, re
vm = json.load(urllib.request.urlopen('https://piston-meta.mojang.com/mc/game/version_manifest_v2.json'))
for v in [x for x in vm['versions'] if x['type'] in ('old_alpha','old_beta')]:
    fn = f'/tmp/mcjar/{v["id"]}.jar'
    if not os.path.exists(fn):
        j = json.load(urllib.request.urlopen(v['url']))
        urllib.request.urlretrieve(j['downloads']['client']['url'], fn)
```

Then classify with `scripts/scan_jars.py` (same heuristic the findings above came from), and confirm one class per era with
`javap -p -classpath <jar> com.mojang.minecraft.a` (or `net.minecraft.client.Minecraft` for later builds).
