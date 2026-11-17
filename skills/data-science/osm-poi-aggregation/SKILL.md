---
name: osm-poi-aggregation
description: "Use when counting, ranking or proving the absence of OSM/Overpass POIs, or grouping their name variants."
version: 1.0.0
author: hermes-agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [osm, overpass, poi, aggregation, name-clustering, restaurants, openstreetmap, data-analysis]
    category: data-science
    requires_toolsets: [terminal]
    related: [maps]
---

# OSM POI Aggregation & Name Grouping

Count and rank POIs (restaurants, shops, hotels, …) across a whole country or
area from OpenStreetMap via Overpass, then group their names so spelling /
prefix / transliteration variants of the same place are counted together.

This is the "what are the most common X in country Y, by count" workflow. For
simple nearby-search / geocoding / routing use the `maps` skill instead — this
one is specifically about **bulk aggregation + deduplicating name variants**.

## When to Use

- "Top 10 restaurant names in Germany" / any country
- "How many X are there in region Y" (by `amenity=`/`shop=`/`tourism=`)
- Ranking chains or common place names, where OSM fragments one real name
  across "Zur Linde" / "Gasthaus Linde" / "Linde"
- Any task where you must count OSM objects by a tag value across a large area
- "Gibt es in <Ort> keinen <POI>?" — absence & coverage questions (see
  references/absence-coverage-analysis.md)

## Core technique (see references/overpass-poi-aggregation.md for full code)

1. **Query** — `[out:json]` with `out tags;` over an `area` (country via
   `area["ISO3166-1"="DE"][admin_level=2]`). Whole-country restaurant queries
   return 30–60 MB. **Run curl in the background** (`terminal(background=True,
   notify_on_complete=True)`) — a foreground call times out and loses the file.
   `out tags;` carries **no coordinates** — the moment a later step needs
   lat/lon (distance, map, assigning a POI to a town) use `out body;` for
   nodes and `out center;` for ways/relations, otherwise you get a perfectly
   valid file that silently yields zero usable rows.
2. **PITFALL — 406** — `overpass-api.de` rejects a bare `curl` with no
   User-Agent (returns an HTML 406 page, not JSON). Always send
   `-A "hermes-agent/1.0" -H "Accept: application/json"`.
3. **Count** — one `collections.Counter` over `el['tags']['name']` for all
   `elements`. ~1 s for 100k names; count everything, never sample.
4. **Auto-group** — normalize each name to a "core" by stripping leading
   article/prefix words (`zur`/`zum`/`gasthaus`/`la`/`da`…), trailing generic
   type words (`restaurant`/`grill`/`pizzeria`…), and color/attribute words,
   then map the core to a canonical motif via a regex dictionary (~27 German
   heraldic signs: Linde, Hirsch, Krone, Adler, Post, Löwe, Sonne …).
   This collapses "Zur Linde"(184)+"Gasthaus Linde"(23)+"Linde"(35) → **Linde 466**.
5. **LLM cluster the leftovers** — the Top-1000 ungrouped names still hide
   real variants the regex misses (spelling `PizzaExpress`/`Pizza Express`,
   transliteration `Maharaja`/`Maharadscha`, punctuation `Ruff's`/`Ruff’s
   Burger`). Split into 3 chunks and send to **3 parallel `delegate_task`
   leaf subagents**; each returns strict JSON `[{"canonical","members"}]`,
   merging ONLY true same-name variants — never same-cuisine different places.
6. **Merge & sort** the auto-groups + LLM clusters into one ranked list.

Always tell the user whether a ranking is **raw exact** or **grouped**, and
flag that OSM is community data (lower bound, misses unnamed POIs).

## Absence & coverage questions ("which town has NO <POI>?")

Same tools, different query shape — the aggregation steps above answer "how
many", this answers "is there none", and the naive approach fails in both
directions.

1. **Get the candidate universe with coordinates** — `node(area.de)["place"~"^(city|town)$"]["population"]; out body;`. Keep `population` as a string and filter on `.isdigit()` (tags contain prose and spaces). Some municipalities carry `place` on their boundary relation instead of a node and are then missing from the universe entirely — sanity-check the final top ranks against an official city list before publishing.
2. **Get the POI universe once, for the whole country** — union of tag- and
   name-based selectors (`cuisine~"kebab|kebap|d[oö]ner|doner",i`, `shop=kebab`,
   `name~"..."["amenity"]`); ~6 MB / ~14k elements for döner in DE.
3. **Do NOT rank by distance from the place's label node.** A `place` node sits
   anywhere inside a spread-out municipality: a real in-town POI can be 8 km
   from the node and a neighbouring town's POI 1 km from it. Use the
   **admin-boundary area filter** instead:
   `area["name"="X"]["boundary"="administrative"]["admin_level"~"^(6|8)$"]->.a; nwr(area.a)["amenity"~"^(fast_food|restaurant)$"]; out center tags;`
4. **Batch many towns into one request** — `area[...]["name"~"^(A|B|C)$"]->.a`
   unions the boundaries; then assign each returned POI to the nearest
   candidate centre in Python. One request instead of 40.
5. **Pre-screen cheaply, confirm expensively** — the distance scan is fine as a
   *shortlist* (towns whose nearest POI is >2–3 km); the answer itself must come
   from the boundary query plus an external source.
6. **Verify every "zero" externally** before reporting absence (Lieferando /
   Yelp / Uber Eats / local business directories). In practice most OSM zeros
   are mapping gaps, not döner-free towns — a 38k city with 39 food POIs and no
   kebab tag had four real shops. Report a ranked list with per-entry status
   (**belegt** vs **kein Nachweis**) and name the method + date.

## Pitfalls

- **406 without User-Agent** on overpass-api.de — see step 2.
- **Foreground timeout**: whole-country queries take 1–5 min; background the curl.
- **Don't conflate "not in the heraldic dict" with "dropped"** — foreign chains
  (Akropolis, L'Osteria) have no German prefix variants, so they already sit
  near-complete as one name; they're correctly excluded from the German-sign
  grouping, not lost.
- **Conservative merging**: false merges (two different "Asia …" places) are
  worse than missed merges — constrain the LLM prompt hard.
- Generic category words ("Mensa", "Kantine", "Biergarten") inflate counts if
  not filtered — flag them explicitly.
- **Name matching needs typo + local-brand tolerance** — `Kebap`/`Kepab`/`Kebab`,
  `Döner`/`Doener`, plus the shop names people actually use (Istanbul, Saray,
  Antep, Urfa, Divan, Mangal, Hasir, Bosporus…). A `kebab`-only regex reports
  shops as absent when they are simply named differently.
- **A zero-row geo step usually means missing coordinates, not missing POIs** —
  assert `'lat' in el or 'center' in el` before filtering, and print the count of
  rows dropped for lacking geometry.
- **502/429 "at capacity" is server load, not a bad query** — retry with
  exponential backoff (6–8 attempts, 15–20 s × attempt). Never run two heavy
  country queries concurrently, and kill stale retry loops: they keep
  overwriting the output file you already validated.
- **Validate a download by parsing it, not by grepping the head** — the `osm3s`
  metadata block pushes `"elements"` past the first few hundred bytes, so a
  `head -c 200 | grep` guard throws away good 6 MB files. Download to
  `<out>.tmp`, `json.load` it, check the element count, and only then `mv` into
  place — a failed retry can never clobber a good file.
- **Never `pkill -f <pattern>`** when that pattern also appears in your own
  command line — it matches your own shell and kills the turn (exit −15). Kill
  the exact PID from `pgrep`/`ps`.

## Verification

```bash
# Quick sanity: file is JSON, element count == sum of name counts
python3 -c "import json; d=json.load(open('/tmp/rest.json')); \
  print(len(d['elements']), sum(1 for e in d['elements'] if e.get('tags',{}).get('name')))"
```

For any query whose result feeds a geo step, also assert coordinates are
present (a valid JSON file with 14k elements but no `lat`/`center` will pass the
check above and still break every distance calculation):

```bash
python3 -c "import json; e=json.load(open('/tmp/places.json'))['elements']; \
  print(len(e), 'with geometry:', sum(1 for x in e if 'lat' in x or 'center' in x))"
```
