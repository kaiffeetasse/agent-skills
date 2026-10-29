---
name: osm-poi-aggregation
description: "Bulk OpenStreetMap/Overpass POI counting and name grouping — most-common-restaurant/chain analysis, normalization across spelling/prefix/transliteration variants, LLM semantic clustering of leftovers."
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

## Core technique (see references/overpass-poi-aggregation.md for full code)

1. **Query** — `[out:json]` with `out tags;` over an `area` (country via
   `area["ISO3166-1"="DE"][admin_level=2]`). Whole-country restaurant queries
   return 30–60 MB. **Run curl in the background** (`terminal(background=True,
   notify_on_complete=True)`) — a foreground call times out and loses the file.
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

## Verification

```bash
# Quick sanity: file is JSON, element count == sum of name counts
python3 -c "import json; d=json.load(open('/tmp/rest.json')); \
  print(len(d['elements']), sum(1 for e in d['elements'] if e.get('tags',{}).get('name')))"
```
