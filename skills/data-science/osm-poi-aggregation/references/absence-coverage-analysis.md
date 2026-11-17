# Absence & coverage analysis — "which town has no X?"

Workflow for questions like *"largest German city without a döner shop"*,
*"which municipalities have no pharmacy"*, *"where is service Y missing"*.
The deliverable is a **ranked list with evidence and a confidence label per row**,
not a single unhedged name.

## 1. Two universes, both with geometry

```overpass
[out:json][timeout:500];
area["ISO3166-1"="DE"][admin_level=2]->.de;
node(area.de)["place"~"^(city|town|village)$"]["population"];
out body;
```

`out tags;` here is the classic trap: it returns the place nodes **without**
lat/lon and every downstream distance/assignment step silently yields nothing.
14.8k places with geometry ≈ 6 MB.

```overpass
[out:json][timeout:600];
area["ISO3166-1"="DE"][admin_level=2]->.de;
(
  nwr(area.de)["cuisine"~"kebab|kebap|d[oö]ner|doner|doener",i];
  nwr(area.de)["shop"="kebab"];
  nwr(area.de)["name"~"d[oö]ner|doener|kebab|kebap|kepab",i]["amenity"];
);
out center tags;
```

`out center;` gives ways/relations a representative point; nodes keep their own
lat/lon. ~14k elements ≈ 6 MB for döner in Germany.

## 2. Screen: distance from the place node (shortlist only)

```python
CELL = 0.05
grid = {}
for lat, lon in pts:
    grid.setdefault((int(lat // CELL), int(lon // CELL)), []).append((lat, lon))

# for a place: expand rings over the grid, min over haversine-ish distance
# dy = dlat*111.32 ; dx = dlon*111.32*cos(lat)
```

Use the result only to shortlist (e.g. "nearest POI > 2.5 km"). It is **not**
membership: a `place=town` node sits anywhere in the municipality, so a town can
show 8 km while owning a shop in an outer district, and 2 km because a
neighbouring town's shop is close.

## 3. Decide: point-in-admin-boundary

```overpass
[out:json][timeout:180];
area["name"="Mettmann"]["boundary"="administrative"]["admin_level"~"^(6|8)$"]->.a;
nwr(area.a)["amenity"~"^(fast_food|restaurant|food_court)$"];
out center tags;
```

Batch many towns in a single request (union of areas), then assign each POI to
the nearest candidate centre in Python:

```overpass
area["boundary"="administrative"]["admin_level"~"^(6|8)$"]["name"~"^(Olsberg|Kalkar|Pegnitz)$"]->.a;
nwr(area.a)["amenity"~"^(fast_food|restaurant|food_court)$"];
out center tags;
```

Name collisions (`Neuenkirchen`, `Wulfen`, `Epe` = districts, not towns) inflate
counts or invent candidates — drop candidates whose "town" is actually a
district of a larger city before reporting.

## 4. Classify hits generously, then verify the zeros hard

Keyword set that catches real döner shops: `d[oö]ner|doener|kebap|kepab|kebab|
gyros|t[üu]rk|istanbul|saray|bereket|antep|urfa|adana|hasir|ocakba|mangal|izmir|
ankara|pide|lahmacun|bosporus|kapadokya|anatoli|efes|antalya|konya|sultan|kervan|
diyar|divan`. `kebab` alone misses most of them (`Pizza und Kepab Oase`,
`Divan`, `Vorstadt Döner`).

Then, per zero candidate, check external sources before believing OSM:

| Source | What it proves |
|---|---|
| `lieferando.de/lieferdienst/<town>/doner` | which shops serve the town — compare **distance** in the listing; 15 km = delivered from elsewhere, i.e. no local shop |
| `yelp.com/search?find_loc=<town>` | named local shops |
| `ubereats.com/de-en/city/<town>` | local vendor list |
| local directories (`coolibri`, `stadtleben`, `speisekarte.de`, `11880`) | owner-operated shops that never joined a marketplace |
| town website / local paper | existence or explicit "es gibt keinen" |

OSM coverage varies wildly: 39 food POIs for a 38k town means a mapping gap, not
an empty town. Treat "OSM says zero" as "needs verification", never as a result.

## 5. Robust download

```bash
for i in $(seq 1 8); do
  code=$(curl -s -m 900 -A "hermes-agent/1.0" -H "Accept: application/json" \
      --data-urlencode "data@q.overpassql" \
      https://overpass-api.de/api/interpreter -o out.json.tmp -w "%{http_code}")
  ok=$(python3 - out.json.tmp <<'PY'
import json,sys
try:
    d=json.load(open(sys.argv[1]))
    print("OK" if isinstance(d.get("elements"),list) and len(d["elements"])>100 else "BAD")
except Exception:
    print("BAD")
PY
)
  [ "$code" = "200" ] && [ "$ok" = "OK" ] && { mv -f out.json.tmp out.json; break; }
  sleep $(( i * 20 ))
done
```

Parse, do not grep the head: the `osm3s` block pushes `"elements"` past the
first 200 bytes and a head-grep guard discards valid 6 MB downloads. Baseline
country queries take 1.5–8 min; run them one at a time (a second concurrent
heavy query gets 429/502).

## 6. Report shape

Ranked table (largest first) with: rank, place, population, one-line evidence.
Split the verdict explicitly into **belegt** (no shop in the boundary + external
sources show only out-of-town delivery) and **kein Nachweis** (nothing found, but
small-town directories are incomplete). State the cutoff ("all places ≥ 15k
checked individually, 9–15k screened"), the source mix and the date — there is no
official register for "is there a döner shop", so the method is the credibility.
