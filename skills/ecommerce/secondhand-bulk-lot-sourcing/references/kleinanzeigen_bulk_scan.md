# Kleinanzeigen Bulk-Lot Scan — konkretes Rezept

Verifiziert 09/2026 (LEGO-Konvolute als Teilebasis für einen 4.608-Teile-Technic-MOC).
Modul: `~/.hermes/skills/devops/kleinanzeigen-monitoring/api/kleinanzeigen.py`
(`from kleinanzeigen import Kleinanzeigen`).

## 1. Suchparameter (bestätigt)

```python
api.search(q="lego konvolut", size=100, count=100, page=0,
           poster_type=None,        # None = privat + gewerblich (ALL NICHT senden)
           include_top_ads=True)    # sonst fehlen echte Anzeigen
```

- `sortType` existiert nicht (HTTP 500) → nur Blättern; Seiten sind nahezu disjunkt.
- Aktive Suche deckt nur ~100 Treffer/Query; 30+ Keywords × 2 Seiten ergaben 3.540 unique ads.
- Kategorie-Scan: `q=""`, `category_id=23` (Spielzeug; **LEGO hat keine eigene
  Unterkategorie**, Modellbau = 249), `location_id` + `distance` + `max_price=150`,
  `page=0..5`. Stadt-ID über `find_locations('<Stadt>')` holen (Beispiel: eigene Stadt → `9027`)
  (`locs[0]` ist „Deutschland" → nach Name filtern).
- Der Such-Datensatz enthält **kein Versandfeld**; Keys sind im Wesentlichen:
  `id, title, description, price_amount, price_type, attributes, latitude, longitude,
  zip_code, state, poster_type, category_id, start_date_time, link, image_url, user_id`.

## 2. Mengen-Parsing (€/kg ohne Ausreißer)

```python
KG_M  = re.compile(r'(\d{1,3}(?:[.,]\d{1,3})?)\s*(?:kg\b|kilo(?:gramm)?\b)', re.I)
GR_M  = re.compile(r'(\d{3,5})\s*(?:g\b|gramm\b)', re.I)
ST_M  = re.compile(r'(\d{2,6}(?:[.,]\d{3})?)\s*(?:teile|steinen?|st(?:ü|ue)ck|pcs|elemente)', re.I)
PERKG = re.compile(r'(je|pro)\s*kilo|kilopreis|preis\s*(je|pro)\s*kg|je\s*kg\b|/\s*kg\b', re.I)

def cand_weights(text):
    w = []
    for m in KG_M.finditer(text):
        v = float(m.group(1).replace(',', '.'))
        if 0.2 <= v <= 300: w.append(v)              # "2,2 kg", "1,850 Kg" -> 1.85
    for m in GR_M.finditer(text):
        v = int(m.group(1))
        if 200 <= v <= 200000: w.append(round(v/1000, 2))   # Sub-Kilo-Lots
    return w

# Preis je Kilo -> Preis IST der Kilopreis, nicht teilen
if PERKG.search(title):
    per_kg, kg = price, None
elif price and (ws := cand_weights(blob)):
    pl = [w for w in ws if 1.0 <= price/w <= 60.0]        # Plausibilitätsband Gebraucht-Bulk
    kg = min(pl, key=lambda w: abs(price/w - 12)) if pl else None   # Zielwert ~12 €/kg
    per_kg = round(price/kg, 1) if kg else None
```

**Warum so:** ein einzelner `\d+\s*kg`-Treffer lieferte 0,1 €/kg-Werte (Scherz „ca. 4500 kg"
im Text, Beiwörter) und stellte die Rangliste auf den Kopf. Ohne plausiblen Kandidaten gilt
das Gewicht als **unbekannt**, nicht als geschätzt.

Zusätzlich sinnvoll: `per_1000 = price/pieces*1000` und die Entfernung per Haversine aus
`latitude/longitude` (Stadtzentrum als Referenz) — der `distance`-Parameter der API
ist ungenau.

## 3. Kandidaten-Filter

- Behalten: Bulk-Wort im **Titel** (`konvolut|sammlung|einzelteile|kiloware|teilepaket|
  schuettware|restposten|gemischt|wuerfelkiste|kiste|sortiment|kg|kilo|…`) + `lego` im Titel.
- Wegwerfen: andere Marke/nicht kompatibel, „nur Figuren/Minifiguren", Anleitung/Katalog/
  Stickerbogen, „suche/gesucht/tausche", konkrete Set-Nummer ohne Bulk-Wort.
- Marktband als Plausibilitätscheck (LEGO-Gebraucht, 09/2026): gemischt 5–8 €/kg,
  Technic-lastig 8–13 €/kg, reine Abhol-Anzeigen als Ausreißer bis 2,5 €/kg.

## 4. Versand vs. Abholung (der einzige verlässliche Weg)

```python
h2  = re.sub(r'\s+', ' ', html)
i   = h2.find('id="viewad-price"'); j = h2.find('viewad-description', i)
txt = re.sub(r'<[^>]+>', ' ', h2[i:j])          # Hauptblock der Anzeige
ship = 'Nur Abholung' if 'Nur Abholung' in txt else \
       ('Versand möglich' if 'Versand möglich' in txt else 'unklar')
```

- `'Versand möglich' in html` ist **falsch-positiv** (Block „Ähnliche Anzeigen" + JSON-LD
  der Beschreibung) → reine Abhol-Anzeigen sehen versendbar aus.
- Ergänzend den Anzeigentext prüfen: `Versand möglich|Versand für|Porto \d|Hermes|DHL`
  vs. `kein Versand|nur (an )?(Selbstabholer|Abholung)|NUR ABHOLUNG!!!!`.
- Bleibt es still → „nicht angegeben → klären" ausgeben.
- Beispiel-Ausbeute von 16 geprüften Lots: 5× explizit „Nur Abholung", 3× „Versand möglich",
  8× im Text nicht angegeben.

## 5. Anzeigenseite lesen + Link-Verifikation

```python
def ad_facts(url):                     # curl -s -L -A "Mozilla/5.0 (X11; Linux x86_64) Chrome/126"
    title = r'<h1[^>]*id="viewad-title"[^>]*>(.*?)</h1>'
    price = r'id="viewad-price"[^>]*>(.*?)</'
    seite = r'<span class="text-body-regular[^"]*">\s*([^<]{2,60})\s*</span>'   # Verkäufername
    aktiv = r'Aktiv seit\s*([^<]{3,25})'                # Glaubwürdigkeit
    online= r'(\d+)\s*Anzeigen online'
    details = html[find('id="viewad-details"') : find('id="viewad-description"')]
```

- Der Details-Block liefert `Art: LEGO & Duplo`, `Zustand: …`, `Nur Abholung` /
  `Versand möglich`; der Beschreibungsblock kommt aus
  `id="viewad-description-text"` (bis `<section` oder `</p></div>`).
- **Jeden ausgegebenen Link prüfen**: Titel-Match gegen den gespeicherten Datensatz UND
  Preis-String. Grund: aus dem Gedächtnis rekonstruierte IDs liefern HTTP 200 mit einer
  **völlig fremden** Anzeige (kein Fehler, kein 404) — Links nie abtippen, immer aus der
  gespeicherten JSON ziehen.
- Preis im Suchindex kann veraltet sein (Anzeigenseite maßgeblich).

## 6. Ergebnisform

Lange Läufe: pro Batch in eine Workspace-JSON appenden (`raw → filtered → verified`),
Ausgabe erst am Ende aus der `verified`-Datei bauen, dann als Tabelle + Datei
(`MEDIA:/pfad/liste.txt`) liefern. So überlebt der Fortschritt Timeouts und die
Zahlen sind nicht aus dem Chatverlauf rekonstruiert.
