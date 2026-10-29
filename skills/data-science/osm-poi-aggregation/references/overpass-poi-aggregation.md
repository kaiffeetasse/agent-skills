# Overpass Bulk POI Aggregation & Name Grouping — detail

## 1. The query (whole-country, count by name)

```overpass
[out:json][timeout:900];
area["ISO3166-1"="DE"][admin_level=2]->.a;
nwr(area.a)[amenity=restaurant][name];
out tags;
```

- `out tags;` (not `out body;`) keeps the JSON small — we only need `tags.name`.
- Whole-country restaurant queries return **30–60 MB**. Run `curl` in the
  background (`terminal(background=True, notify_on_complete=True)`) — a
  foreground call times out at 60–600 s and you lose the download.
- Mirrors: `overpass-api.de/api/interpreter` (primary) or
  `overpass.kumi.systems/api/interpreter` (fallback; slower, rarely 406s).

## 2. PITFALL — overpass-api.de returns HTTP 406 "Not Acceptable"

A bare `curl --data-urlencode` (no UA) gets a 406 HTML page, not JSON.
**Fix:** send a User-Agent + Accept header.

```bash
curl -s -A "hermes-agent/1.0" -H "Accept: application/json" \
     --data-urlencode "data@/tmp/oq.txt" \
     https://overpass-api.de/api/interpreter -o /tmp/rest.json
```

Without the UA the request is rejected before query execution — durable quirk
of that server, not a transient error.

## 3. Counting

```python
import json
from collections import Counter
data = json.load(open('/tmp/rest.json'))
c = Counter(el['tags']['name'].strip()
           for el in data['elements'] if 'tags' in el and el['tags'].get('name'))
```

`data['elements']` includes nodes + ways + relations; each is one POI. The sum
of all counts == total named POIs. A `Counter` over 100k names runs in ~1 s —
no sampling needed, count everything.

## 4. Automatic grouping (regex over normalized "core")

Strip leading article/prefix words and trailing generic type words, collapse
declensions, then keep a heraldic/core dictionary of canonical forms.

```python
import re
LEAD = r"(gasthaus|gasthof|landgasthof|gaststätte|restaurant|pizzeria|taverna|hotel|zur|zum|zu|den|der|die|das|la|il|da|...) "
ATTR = r"(alter|alte|golden(er|e|es)?|grün(er|e|es)?|schwarz(er|e|es)?|...) "
HERALD = [ (r"linden?","linde"), (r"hirsch(en|e)?","hirsch"),
           (r"löwen?|loewen?","löwe"), (r"adler","adler"),
           (r"krone","krone"), (r"sonne","sonne"), ... ]  # ~27 motifs

def core(name):
    s = name.lower()
    s = re.sub(r'["\'`´„“”().,-]',' ', s)
    s = re.sub(r'\s+',' ', s).strip()
    prev = None
    while prev != s:
        prev = s
        s = re.sub(rf'^{LEAD}\b\s*','', s).strip()
        s = re.sub(rf'\s*\b(restaurant|grill|pizzeria)$','', s).strip()
        s = re.sub(rf'^{ATTR}\b\s*','', s).strip()
    for pat, canon in HERALD:
        if re.fullmatch(pat, s):
            return canon
    return s or name.lower()

groups = {}
for name, n in c.items():
    groups.setdefault(core(name), Counter())[name] += n
```

Result: "Zur Linde"(184) + "Gasthaus Linde"(23) + "Linde"(35) + ... collapse to
**Linde = 466**. Biggest jumps when grouping: Hirsch (#26 raw → #2 grouped),
Krone (#15 → #3), Adler (#9 → #4).

Caveat: this ONLY bundles names matching a known motif dictionary. Foreign
chains (Akropolis, L'Osteria, Poseidon) don't have German prefix variants, so
they already sit near-complete as a single name and grouping barely changes
them — don't conflate "not in the heraldic list" with "dropped".

## 5. Semantic clustering of the leftovers via LLM

Auto-grouping leaves tens of thousands of singletons. The Top-1000 ungrouped
(by count) still contain real variants the regex misses: spelling
(`PizzaExpress`/`Pizza Express`, `Cancun`/`Cancún`), transliteration
(`Maharaja`/`Maharadscha`, `Zorbas`/`Sorbas`), punctuation
(`Ruff's Burger`/`Ruff’s Burger`). Delegate these to parallel LLM subagents:

- Split the 1000-name TSV into 3 chunks; one `delegate_task` call with
  `tasks=[...]` (3 leaf subagents, runs in background).
- Prompt each: merge ONLY true spelling/format/transliteration variants of the
  SAME name; **do NOT merge same-cuisine different restaurants**; return
  strict JSON `[{"canonical": "...", "members": [...]}, ...]`.
- Merge the subagent clusters back into the auto-grouped list, then sort.

Be conservative in the prompt — false merges (two different "Asia ..." names)
are worse than missed merges.

## 6. Caveats to report to the user

- OSM is community data, not an official register — counts are a lower bound
  and miss unnamed/POI-without-name entries.
- Accent / punctuation / capitalization differences count as separate names
  until normalized; always state whether a ranking is "raw exact" or "grouped".
- Generic words that are actually categories (e.g. "Mensa", "Kantine",
  "Biergarten") inflate if not filtered — flag them.
