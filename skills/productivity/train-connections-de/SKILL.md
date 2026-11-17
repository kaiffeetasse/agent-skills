---
name: train-connections-de
description: "Use for Zugverbindungen, Fahrplan and Sparpreis (DE)."
version: 1.0.0
author: kaiffeetasse
license: MIT
metadata:
  hermes:
    tags: [bahn, zug, hafas, transitous, fahrplan, delfi, verbindungssuche]
    related_skills: [maps, artist-tour-dates]
---

# Zugverbindungen recherchieren (DE/CH/AT)

Trigger: „wann muss ich losfahren", „welche Züge fahren", „Zugverbindung X→Y", Fahrplan-/Anschlussfragen.
Immer: echte Fahrplandaten abfragen (kein Schätzen), Abfahrts-/Ankunftszeiten + Umstiege + Bahnhofsnamen nennen, Quelle angeben.

## Was funktioniert (verifiziert 30.09.2026)

| Quelle | Zugang | Eignung |
|---|---|---|
| **Transitous (MOTIS)** `api.transitous.org` | curl, kein Key | Beste Quelle: tür-zu-tür-Routing inkl. Bus/S-Bahn. Live verifiziert |
| **search.ch** `fahrplan.search.ch/api/route.json` | curl, kein Key | Unabhängige Gegenprobe (SBB-Daten), gut für DE↔CH |
| **bahn.de „Streckenseiten"** `bahn.de/reisen/view/verbindung/<von>/<nach>.shtml` | web_extract | Offizielle DB-Angaben: Direktverbindungen, Reisezeit, erste/letzte Abfahrt, Sparpreis-Beispiele (Stand-Datum beachten!) |
| **ÖBB HAFAS mgate** `fahrplan.oebb.at/bin/mgate.exe` | curl POST | LocMatch funktioniert (s. u.); TripSearch-Req-Format noch ungelöst |
| **DB Navigator vendo-API** `app.services-bahn.de` | curl / `scripts/dbnav.py`, **kein Key** | **Erste Wahl für Fahrplan UND Preise**: echte Sparpreise, Tarifstaffel (SSP/SPP/FLP), Tagesbestpreis, Abfahrtstafel, Gleise. Nur der App-User-Agent ist Pflicht (Abschnitt unten) |

**Geblockt/unbrauchbar in dieser Umgebung:**
- `www.bahn.de/web/api/angebote/fahrplan` → HTTP 403 `OPS_BLOCKED`, auch same-origin als `fetch()` aus der geladenen bahn.de-Seite; `www.bahn.de/web/api/reiseloesung/orte?suchbegriff=…&typ=ALL` antwortet dagegen 200 und liefert die Stations-ID (`A=1@O=…@L=8000290@…`) — brauchbar, wenn die Angebots-API wieder freigeschaltet wird.
- `bahn.de`-Hash-Deeplinks (`…/suche#sts=true&so=…&zo=…&hd=<Datum>`) setzen das Datum **nicht**: die Seite steht auf „Morgen", die Suche endet in „Keine Verbindungen gefunden" — kein Fahrplanbefund, sondern eine blockierte Angebots-API.
- bahn.de im Browser → `ERR_HTTP2_PROTOCOL_ERROR` (Akamai/HTTP2)
- `v6.db.transport.rest` / `v5…` → HTTP 503 (leerer Body); `app.vendo.noncd.db.de` → HTTP 000 (kein Route/DNS)
- `reiseauskunft.bahn.de/bin/query.exe` (alte HAFAS-Weboberfläche) → existiert nicht mehr
- `api.direkt.bahn.guru` → HTTP 000
- ÖBB `query.exe/dn` liefert ohne Session nur das Suchformular (kein Ergebnis-HTML)

## Rezepte

**Lesehilfe für die Beispiele:** Messwerte sind anonymisiert — **A** = Startbahnhof, **B** =
Fernverkehrs-Hub, **C** = Ziel. Preise, Dauern und Uhrzeiten sind echte Abrufe am genannten Datum;
nur die Ortsnamen sind ersetzt.

### 1) Haltestellen-IDs (Transitous)
```bash
curl -s "https://api.transitous.org/api/v1/geocode?text=Frankfurt%20Hbf" -H "Accept: application/json"
# → id wie de-DELFI_de:08317:14506_G (STOP) ; lat/lon nutzbar als fromPlace/toPlace
```
Nicht jede Haltestelle existiert als STOP: Fallback = Koordinaten (`50.099077,8.519076`).

### 2) Tür-zu-Tür-Plan (Transitous/MOTIS v2)
```bash
curl -s "https://api.transitous.org/api/v1/plan?fromPlace=<id-oder-lat,lon>&toPlace=<id-oder-lat,lon>\
&time=2026-11-26T11:30:00Z&numItineraries=8" -o plan.json
```
- `time` **muss** vollständiges ISO-8601 mit `Z` sein: `2026-11-26T15:25:00` (ohne Z) →
  `parameter "time": failed to parse timestamp`, 0 Itineraries. Der Wert ist **UTC**
  (CET = UTC+1, CEST = UTC+2) — im Winter eine Stunde, nicht zwei.
- **`arriveBy=true` wird von `api.transitous.org` nicht umgesetzt** (live widerlegt 10/2026):
  es kommen trotzdem die *frühesten* Abfahrten des Tages, `time` verschiebt das Fenster nur
  teilweise/unzuverlässig. Für „ich muss um 16:25 dort sein" deshalb **`arriveBy=false` und
  Abfahrtszeiten durchprobieren** (12:00, 12:30 … in UTC), bis die Ankunft passt — oder
  Bahnhof→Bahnhof abfragen und die letzten S-Bahn-/Bus-Legs selbst anhängen.
- **User-Agent setzen.** Per `urllib` ohne Header antwortet der Endpunkt **HTTP 403** (curl geht
  durch); `urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})`.
- `duration` ist in **Sekunden** — `//3600` Stunden, `(//60)%60` Minuten, sonst steht „220 h" da,
  wo 3 h 40 gemeint sind.
- Legs parsen: `itineraries[].legs[]` mit `mode` (HIGHSPEED_RAIL/REGIONAL_RAIL/METRO/BUS), `routeShortName`, `headsign`, `startTime`/`endTime` (ISO+Z → Ortszeit).
- Pitfalls: identische Optionen bei `numItineraries` möglich; in einem Test verschob `maxTransfers` das Zeitfenster (Ergebnisse vor der Wunschzeit) → ohne Zusatzfilter neu abfragen.
- Fertiges Werkzeug statt Copy-Paste: `scripts/transitous_plan.py` — fragt mehrere Abfahrtszeiten je Richtung ab, rechnet Ortszeit→UTC über `Europe/Berlin` (DST-sicher statt hart kodiertem UTC+1), dedupliziert Itineraries und gibt Dauer/Umstiege/Legs aus. `--station` löst beide Orte als Haltestelle auf (Bahnhof→Bahnhof-Gegenprobe).

### 2b) Direktaufruf mit Haltestellen-IDs (Venue → Hotel, nachts)

`scripts/transitous_plan.py` löst seine Orte per Geocoding auf: **Koordinaten (`50.08,8.77`) und
STOP-IDs (`de-DELFI_de:...`) quittiert es mit `Ort nicht gefunden`**, und für manche Paare endet
der `--station`-Lauf in `FEHLER: <HTTPError 404>`. Dann die Plan-API direkt aufrufen — der Endpunkt
nimmt IDs und Koordinaten klaglos:

```python
from zoneinfo import ZoneInfo
import datetime, json, urllib.parse, urllib.request
H = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}   # ohne UA: 403
t = datetime.datetime.fromisoformat("2026-11-20T22:45:00").replace(
        tzinfo=ZoneInfo("Europe/Berlin")).astimezone(datetime.timezone.utc)
q = urllib.parse.urlencode({"fromPlace": stop_id_a, "toPlace": stop_id_b,          # oder "lat,lon"
                            "time": t.strftime("%Y-%m-%dT%H:%M:%SZ"), "numItineraries": 3})
its = json.loads(urllib.request.urlopen(urllib.request.Request(
        "https://api.transitous.org/api/v1/plan?" + q, headers=H), timeout=40).read())["itineraries"]
for it in its:                      # duration ist SEKUNDEN
    legs = [f'{l["mode"]} {l.get("routeShortName","")}' for l in it["legs"] if l["mode"] != "WALK"]
    print(it["startTime"][11:16], "→", it["endTime"][11:16], it["duration"]//60, "Min", legs)
```

- IDs per `api/v1/geocode?text=<Haltestelle>` holen (`type == "STOP"`).
- Das ist der Weg für die Frage „komme ich nach dem Konzert noch zum Hotel“: **Haltestelle am Venue →
  Haltestelle an der Unterkunft**, zwei bis drei Abfahrten nach dem erwarteten Ende, dazu die Lücke
  danach ausweisen („nächste erst 03:33“). Die letzten 400–700 m erscheinen als WALK-Leg.

### 3) Alle Abfahrten/Ankünfte einer Station
```bash
curl -s "https://api.transitous.org/api/v1/stoptimes?stopId=<id>&time=<UTC>&n=400"
# Felder: stopTimes[].place.departure|arrival, mode, routeShortName, headsign
```

**Das ist der Endpunkt für „bis wann fahren die Öffis?“.** Der Planer liefert nur *komplette Ketten*:
fällt der Zubringer-Bus weg, verschwindet auch die S-Bahn aus dem Ergebnis, und es sieht aus, als
würde ab 00:15 nichts mehr fahren. Deshalb **je Haltestelle einzeln** abfragen und die letzten
Abfahrten pro Linie nennen:

- **Haltestelle am Venue** (`geocode?text=<Venue> <Stadt>`) → letzter Bus/zweiter Taktbruch.
- **Bahnhof/Haltestelle an der Unterkunft** → Takt und letzte Fahrt der Schiene (S-Bahn fährt in
  Frankfurt/Rhein-Main nachts weiter, oft stündlich, während der Bus längst eingestellt ist).
- Die **Engstelle benennen**, nicht die Linie mit der längsten Betriebszeit: „letzter Bus 01:13, danach
  04:33 — die S-Bahn fährt weiter, aber du kommst nicht mehr hin“ plus Fußweg-Distanz als Ausweg.

**Fahrzeit ≠ Betriebszeit.** Auf „wie lange fahren die Öffis?“ beide Antworten geben: Dauer der
Verbindung (Minuten aus `duration`) **und** die letzten Abfahrten je Linie — die Frage ist je nach
Kontext beides.

### 4) Gegenprobe search.ch
```bash
curl -s "https://fahrplan.search.ch/api/route.json?from=Frankfurt&to=Berlin%20Hbf&date=2026-10-02&time=16:00&num=6"
```

### 5) ÖBB mgate (LocMatch – funktioniert)
```python
body = {"client":{"id":"OEBB","type":"WEB","name":"oebb.at","v":6050600},
        "ver":"1.62","lang":"deu","auth":{"type":"AID","aid":"OWDL4fE4ixNiPBBm"},
        "formatted":False,
        "svcReqL":[{"id":"1|1|","meth":"LocMatch",
                    "req":{"input":{"field":"S","loc":{"type":"S","name":"Frankfurt"},"maxLoc":5}}}]}
# POST https://fahrplan.oebb.at/bin/mgate.exe, Content-Type: application/json
# Pflicht: auth{"type":"AID",...} ; client.type="WEB" erwünscht (client.type="AID" => Parse fail)
# Erfolg = svcResL[0].err == "OK"  (NICHT '"err" fehlt == Erfolg'!)
# Ergebnis: svcResL[0].res.match.locL[].lid  (A=1@O=…@L=<EVA>@p=…)
```
TripSearch mit `dep`/`arr` als lid-String → `PARSE … root.svcReqL.svcReqL.req(dep)`; Format noch nicht geknackt (evtl. verschachteltes loc-Objekt / journey-v2-Spec).

## Preise & Fahrplan: DB-Navigator-App-API (verifiziert 16.11.2026)

**Das ist der Preis-Weg — nicht mehr bahn.de.** Basis `https://app.services-bahn.de`, kein API-Key,
kein Login, kein Cookie, kein Browser. Die Web-API von bahn.de ist gesperrt (`403 OPS_BLOCKED` /
Fehler 751/753), Trainline wirft bei scripted Calls DataDome. Werkzeug: `scripts/dbnav.py`
(stdlib only; `station`, `search`, `offers`, `bestprice`, `departures` live getestet).

```bash
python3 scripts/dbnav.py station    "Frankfurt(Main)Hbf"
python3 scripts/dbnav.py search     "Frankfurt(Main)Hbf" "Berlin Hbf" --at 2026-11-20T17:10
python3 scripts/dbnav.py search     "Frankfurt(Main)Hbf" "Berlin Hbf" --at 2026-11-20T16:30 --pax 2
python3 scripts/dbnav.py offers     "Frankfurt(Main)Hbf" "Berlin Hbf" --at 2026-11-20T16:30 --pax 2
python3 scripts/dbnav.py bestprice  "Frankfurt(Main)Hbf" "Berlin Hbf" --day 2026-11-20 --pax 2
python3 scripts/dbnav.py departures "Berlin Hbf"
python3 scripts/dbnav.py search … --bahncard 25 --child 8 --class KLASSE_1
```

Regeln (alle live getroffen):

* **Header sind die Auth.** `User-Agent: DBNavigator/Android/26.20.0` ist Pflicht (sonst
  `452 OPS_BLOCKED`), `X-Correlation-ID` ist Pflicht (sonst `405` mit leerem Body). Content-Type und
  `Accept` tragen die API-Version (`…verbindungssuche.v9+json`, `…location.v3+json`). Kein Key nötig.
* **Preis kommt inline** in `angebote.preise.gesamt.ab` (bei Teilpreisen `.einzel.ab`), kein
  Zusatzaufruf. `angebotsMeldungen: ["Preisauskunft nicht möglich"]` = für diese Fahrt gibt es keinen Tarif.
* **Personen = Länge der `reisende`-Liste** (`--pax 2` = zwei Objekte); ein `anzahl`-Feld gibt es
  nicht. **Kein Gruppentarif**: 2 Personen = 2× Einzelpreis. Getrennte Tickets je Startbahnhof sind
  deshalb fast immer billiger — gemessen 20.11.2026, 2 Personen, Beispielstrecke: durchgebucht
  165,98 €, getrennt gebucht 119,98 € (66,99 € ab dem ersten Startbahnhof + 52,99 € ab dem
  zweiten, gleiches Ziel).
* **Deutschlandticket eines Mitreisenden ändert die Ticketstruktur.** Dann nur die
  Fernverkehrsstrecke kaufen und die Nahverkehrs-Etappen mit dem D-Ticket fahren — gemessen
  20.11.2026 mit BC25: durchgebucht 62,24 €, dagegen ICE ab dem Fernverkehrs-Startbahnhof 39,74 €
  + D-Ticket für den Zubringer (RB/RE dorthin) und die letzte Etappe (RE zum Zielbahnhof). Ob eine konkrete Fahrt im D-Ticket steckt, prüft man mit
  `fahrverguenstigungen: {deutschlandTicketVorhanden: true, nurDeutschlandTicketVerbindungen: true}`
  in `/mob/angebote/fahrplan` — die Antwort trägt dann „Verbindung für Personen im D-Ticket
  enthalten". Vorher fragen, wer eins hat: ein einziges D-Ticket in der Gruppe verschiebt die
  günstigste Buchung um 20–30 %. Bei nur 5 Minuten Umstieg auf den ICE lieber einen Takt früher
  (RB-Zubringer) oder doch den durchgebundenen Sparpreis nehmen.
* **5 Minuten Umstieg sind fahrplanmäßig erlaubt, aber kein Puffer.** Bei getrennten Tickets auf
denselben Zug ist der Schaden begrenzt: **verpasst man wegen Verspätung den Anschluss, ist die
Zugbindung automatisch aufgehoben** (DB-Regel; ebenso bei erwarteter Ankunftsverspätung ≥ 20 Min —
das steht auch auf jedem Online-Ticket). Man darf dann ohne Neukauf den nächsten Zug nehmen.
Deshalb bei knappen Umstiegen **immer den Folgezug mitliefern** (nächster ICE ab Zustiegsbahnhof,
Ankunft am Ziel, was das für den Abend bedeutet) und den sicheren Zubringer eine Stunde früher als
Alternative nennen — nicht nur „5 Min ist knapp“ sagen. Rechnet man mit BC25, kostet der sichere
Weg oft nur 10 € mehr als die Sparvariante: das ist die Empfehlung wert.
* **BahnCard-Keys sind klassenbindend mit Leerzeichen**: `"BAHNCARD25 KLASSE_2"`. `--bahncard 25`
  erzeugt das korrekt; `"BAHNCARD25"` allein → `400 MODA/FATAL`. BC25 und BC50 rabattieren nur
  Sparpreise identisch (25 %), den Flexpreis voll; BC100 liefert absichtlich keinen Preis.
* `search` zeigt nur den günstigsten „ab"-Preis. **Die Produktstaffel** (z. B. Super Sparpreis
  133,98 / Sparpreis 151,98 / Flexpreis 190,20 für 2 Pers.) samt Bedingungen und buchbarer
  `angebotsId` kommt nur aus `offers` (= `/mob/angebote/recon`) mit **derselben** `reisende`-Liste.
* Kinder: `JUGENDLICHER` **braucht `alter`** (`--child 8`), sonst Erwachsenenpreis (2 Erw. + Kind 8 J.
  = 70,49 €, ohne `alter` = 112,97 €). `FAHRRAD` ist ein eigener Reisenden-Typ (+14,99 €).
* Paging: `frueherContext`/`spaeterContext` aus der Antwort als `--context` zurückgeben.
* Für „welcher Tag/welche Uhrzeit ist billig" **`bestprice`** nehmen (Tagesbestpreis je 3-h-Scheibe,
  ein Aufruf = ein Tag) statt vieler Einzelsuchen.
* `departures` liefert die Live-Abfahrtstafel (braucht `evaNr` aus `station`).

### Zeitzonen-Falle: die Plan-API liefert UTC

`api/v1/plan` gibt `startTime`/`endTime` **mit `Z` (UTC)** zurück. Wer die Zeichenkette roh slict
(`it["startTime"][11:16]`), zeigt im Winter **eine Stunde zu früh** (Sommer: zwei). Konkret:
`"2026-11-20T16:27:00Z"` = **17:27 Ortszeit**, nicht 16:27 — die DB-API und die
Transitous-Abfahrtstafel sagen übereinstimmend 17:27 (ICE 276), 17:58 (ICE 70).

**Regel:** jede Zeit aus `plan` mit `datetime.fromisoformat(s.replace("Z","+00:00"))
.astimezone(ZoneInfo("Europe/Berlin"))` umrechnen — nie roh ausgeben. `stoptimes` liefert dagegen
bereits lokale Zeit — dort nicht doppelt umrechnen. Bei Anschlüssen/Events gilt die DB-API als
Maßstab; im Zweifel die Halte-Liste aus `dbnav.py --json` gegen die eigene Rechnung halten.

### Antwortform: Tarifwahl und Verbindungswahl

Nennt der Nutzer Tarif + Rabatt („Super Sparpreis, beide mit BahnCard 25“), nicht schätzen, sondern
die exakte Konfiguration rechnen:

1. `search … --pax N --bahncard 25` für den Preis, `offers … --pax N --bahncard 25` für die Staffel.
2. **Ganze Staffel zeigen, mit Streichpreis**: SSP / SPP / FLP als Tabelle (z. B. 124,48 / 137,98 /
   149,50, statt 165,98). Der Streichpreis belegt, dass der Rabatt wirklich eingerechnet ist.
3. **Split-Variante mit Rabatt NEU rechnen**, nicht den unrabattierten Split skalieren — die
   Sparpreis-Kontingente sind je Relation und Rabatt eigene Preise.
4. **Flexpreis immer als Versicherung mitnennen, mit Preisabstand.** Mit BahnCard 25 liegen SSP und
   FLP oft nur 20–30 € auseinander (124,48 vs. 149,50), während der Super Sparpreis **nicht
   erstattbar** ist. Ein Halbsatz „25 € gegen ein verfallenes 124-€-Ticket“ ist für den Nutzer mehr
   wert als die reine Preistabelle.
5. **Vor dem Buchungsaufruf neu abfragen.** Sparpreise sind kontingentgebunden und bewegen sich
   täglich: dieselbe Relation kostete an zwei Tagen 52,99 € bzw. 39,74 € (BC25), und der Tagesbest-
   preis nennt einen anderen Wert als die Einzelverbindung. Also unmittelbar vor „hier sind deine
   Buchungsdaten“ noch einmal `search`/`offers` laufen lassen und **die Uhrzeit mitliefern**
   („live abgefragt, <Datum>") — sonst kauft der Nutzer zu einem Preis, den es nicht mehr gibt.

Kommt danach „welche Verbindung?“, **genau eine** empfehlen — mit Abfahrt/Ankunft, **Gleis je Halt**,
Umsteigezeit und einem Satz je Alternative, warum sie ausscheidet (zu spät zur Show, vor der
Abfahrtsgrenze des Mitreisenden, Anschluss reißt). Keine Auswahlliste ohne Empfehlung.

Gleise stehen nicht im Leg, sondern in `verbindungsAbschnitte[].halte[].gleis` — mit
`dbnav.py --json` holen (globales Flag **vor** dem Subcommand).

### Fallback: Streckenseite + Hub-Split (wenn die App-API nicht erreichbar ist)

Fahrplan gibt es billiger (Transitous), **Preise nur bei der DB**. Der SPA-/Formular-Weg ist aus
dieser Umgebung **nicht gangbar** (Stand 11/2026): bahn.de antwortet schon auf der Startseite mit
`Fehler 751/753 – Verhalten Ihres Browsers ähnelt dem eines Bots`, und zwar auch mit frischem
Stealth-Profil, `locale="de-DE"` + `timezone="Europe/Berlin"`. Die Sperre hängt nicht an Sprache
oder Zeitzone — Formularvarianten durchprobieren kostet nur Turns.

**Regel: nach EINEM Fehlschlag umschalten** und mit diesen zwei Hebeln antworten:

1. **Hub-Split rechnen — der wichtigste Hebel.** Durchgebuchtes Ticket bis zum Zielort ist oft deutlich
teurer als Sparpreis bis zum Fernverkehrs-Hub plus Nahverkehr. Real gemessen: A→C durchgebucht
**36,99–38,99 €**, dagegen A→B (Hub) **ab 17,98 €** plus S-Bahn B→C (≈5 €) = **≈23 €** bei gleicher
Gesamtfahrzeit. Beide
Varianten nennen, die Aufteilung empfehlen — und dazusagen, dass der Nahverkehrsteil ein eigenes
Ticket ist (bzw. mit Deutschlandticket abgedeckt).
2. **Streckenseite als Anker, Datum mitliefern.**
   `https://www.bahn.de/reisen/view/verbindung/<von>/<nach>.shtml` via `web_extract` liefert drei
   Beispielverbindungen mit „ab X,XX €" und einem Stand-Datum. Diese Preise gelten für die dort
   genannten Tage, **nicht für den Zieltermin** — im Satz immer als Anker kennzeichnen („Anker vom
   24.11., dein Termin kann abweichen") und den Nutzer auf den DB-Navigator für den Tagespreis
   verweisen. Die Seite beantwortet zusätzlich „schnellste Verbindung", „direkt?", „erster/letzter
   Zug" — das sind belastbare Aussagen, die der Feed oft nicht hat.

**Sparpreis ist personenbezogen — es gibt keinen 2-Personen-Rabatt.** Auf „was kostet das für uns
zwei“ gehört 2 × Einzelpreis plus die Hub-Split-Rechnung; Gruppenersparnis gibt es nur bei
Quer-durchs-Land-/Ländertickets, und die gelten nicht im ICE. Buche ich für zwei Personen, die an
verschiedenen Bahnhöfen derselben Fahrt zusteigen, ist das eine Buchung zum früheren Startbahnhof;
Zustieg an einem späteren Bahnhof derselben Fahrt ist bei zuggebundenen Sparpreisen üblich, aber als
„vor dem Kauf bestätigen lassen“ formulieren, nicht als Tarifzusage.

**Trainline ist kein Ausweg — die Oberfläche ist vermessen, der Preisabruf bleibt zu.**
Die Seite lädt im Stealth-Browser ohne Sperre; `/api/journey-search/` liegt aber hinter DataDome
(Captcha als same-origin `fetch`, auch nach einer erfolgreichen Suche), und ein Reload der
Results-URL mit geändertem `outwardDate` löst es ebenfalls aus. Verifizierte Selektoren, damit sie
nicht neu erarbeitet werden müssen: `#jsf-origin-input` / `#jsf-destination-input` (Vorschläge als
`[role=option]`, per `mousedown`+`click` wählen), `[data-testid=add-adult-passenger-button]`,
Kalenderzelle `[data-testid=jsf-calendar-date-button-<Tag>]` in
`[data-testid=calendar-month-<YYYY-MM>]` (setzt das Datum korrekt), Uhrzeit über die beiden
`<select>` `#jsf-outbound-time-time-picker-hour` und `#jsf-outbound-time-time-picker`. Zwei Fallen
dabei: die Ergebnisse öffnen sich in einem **neuen Tab** (Response-Listener an den Kontext hängen,
nicht an die Seite), und ein Klick nach Button-Text trifft den Booking.com-Popunder —
„Günstige Tickets finden“ ist der `type=submit` **innerhalb** der Form mit `#jsf-origin-input`.
Nach dem Setzen von Datum/Uhrzeit öffnet der Submit keinen Results-Tab mehr: Sackgasse, nicht
weiterdebuggen.

Für Gruppen zusätzlich: Preis pro Person × Personen × Richtungen, plus letzte Meile (Taxi/ÖPNV) —
und das gegen die Autokosten stellen (km × Kilometersatz + Parken + Wertverlust), damit die Empfehlung
nicht nur „günstigster Tarif" ist, sondern die günstigste Anreise.

## Wichtige Pitfalls

1. **DELFI/Transitous ist für DB-Fernverkehr lückenhaft.** Beispiel: Ab dem Startbahnhof (EVA der Station) zeigte der Feed am 02.10.2026 fast nur Regionalverkehr + TGV/NJ/FLX, obwohl DB-Website und Presse direkte ICEs (A→B, 1:38–1:42, ~16×/Tag) ausweisen. **Suchergebnisse ≠ vollständiger Fahrplan** — bei Widerspruch immer DB-Streckenseite zusätzlich lesen und den Konflikt transparent machen.
2. **`routeShortName` ist nicht immer gesetzt** → dann `prodL[0].prodCtx.name/line/catOut` nutzen.
3. **search.ch** gibt bei Nicht-CH-Relationen tlw. absurde Umwege (A→B über zwei ferne Knoten statt direkt) — nur als Plausibilitätscheck nutzen.
4. **Preise zuerst über die DB-Navigator-App-API** (`scripts/dbnav.py`, Abschnitt oben) — die liefert
   echte Tagespreise ohne Key. Erst wenn die nicht erreichbar ist: die **Web**-Angebots-API ist
   gesperrt (`403 OPS_BLOCKED`), der SPA-/Formular-Weg ebenfalls (Fehler 751/753). Dann nicht mehr Turns in Formular-Varianten stecken, sondern auf **Hub-Split +
   Streckenseiten-Anker** wechseln, die Anker mit ihrem Datum kennzeichnen und den Tagespreis beim
   Nutzer lassen. Für Gruppen die **Gesamtsumme** rechnen (Preis × Personen × Richtungen, plus letzte
   Meile/Taxi) und gegen die Autokosten stellen.
5. **Letzte Rückfahrt prüfen** (Konzert/Event!): nach Mitternacht oft nur noch Nightjet; Zubringer-S-Bahn-Transfer am Hbf kann 2 Minuten betragen → unrealistisch, Puffer einplanen.
6. **Anreise-Details aus der Venue-Seite** holen (Buslinie direkt zur Halle, Fußwege, Parkgebühr, Öffnungszeiten des Parkplatzes) — steht selten in Fahrplan-APIs.
7. **Die letzte MEILE prüfen, nicht nur den letzten Zug.** Beim Heimweg ist der Anschlussbus der
   Engpass: ab dem Bahnhofsvorplatz fährt der letzte Bus zum Wohnort oft schon **21:45** (danach erst 05:45).
   Wer nur „letzter Zug" prüft, liefert eine Rückfahrt, die am Bahnhof strandet. Immer zusätzlich
   `Hbf → Wohnadresse` ab der geplanten Ankunftszeit abfragen und den **letzten Anschluss**
   ausdrücklich nennen; fällt er weg, Taxi-Kosten/Abholung als Konsequenz dazuschreiben.
   Verifizierte Kette als Beispiel: Ankunft **21:36** → S-Bahn 21:41 → Wohnort **22:09** geht noch;
   Ankunft **21:58** ist die Grenze — danach nur Taxi (6 km, 18–22 €).
8. **Rückfahrt in beide Richtungen prüfen.** `fromPlace`/`toPlace` werden beim Kopieren leicht
   nicht getauscht — dann sieht die Antwort plausibel aus und beschreibt die Hinfahrt. Kontrolle:
   erste Leg-`from` muss die Venue sein.
9. **Zwei Varianten anbieten statt einer:** „pünktlich" (Ankunft ~Zielzeit, oft 3 Umstiege) und
   „entspannt" (~1 h Puffer, meist eine Verbindung früher). Bei Event-Anreise ist die frühe
   Variante oft die bessere Empfehlung — Einlass beginnt meist 60 min vor der Aufzeichnung.
10. **Tür-zu-Tür-Abfragen lassen Fernverkehr aus — bei dünner Trefferliste Bahnhof→Bahnhof gegenprüfen.**
   Kommt für ein Abendfenster (19–21 Uhr) als früheste Option nur eine Nachtverbindung, ist das in der
   Regel eine Lücke des Tür-zu-Tür-Routings, nicht der Fahrplan: dieselbe Relation Bahnhof→Bahnhof
   lieferte 19:27 / 19:50 / 20:55 mit 1–3 Umstiegen, während tür-zu-tür erst 23:19 einstieg. Vor der
   Aussage „fährt nur nachts" also `fromPlace`/`toPlace` auf die beiden Hbf setzen, erneut fragen und
   die letzten S-Bahn-/Bus-Legs selbst anhängen.
11. **Zieldatum jenseits des Feed-Horizonts → plausible, aber absurde Itineraries.** Für Termine weit
   in der Zukunft (Jahresfahrplan des Folgejahres) antwortet der Planner nicht leer, sondern baut
   Umwege über ferne Knoten: A→Leipzig „13 h über Berlin", A→Freiburg mit Ankunft am nächsten
   Morgen. **Erkennungsregel:** Dauer gegen die bekannte Regelzeit der Relation prüfen (Beispiele:
   ~27 Min auf einer Nahverkehrsrelation, ~5 h, ~6:20); >1,5× erwartete Dauer ⇒ Ergebnis
   wegwerfen. Dann nur die Streckenseite zitieren (Dauer, Umstiege, Direktverbindungen/Tag, letzte
   Abfahrt, Sparpreis-Beispiele) **mit Stand-Datum** und sagen, dass die konkreten Zeiten erst ab
   Fahrplanfreigabe (~180 Tage) feststehen. Niemals eine 13-h-Verbindung als „so fährt man" ausgeben.
12. **Grenzrelationen (CH→DE) fehlen im Feed am Abend komplett.** Eine CH→DE-Relation lieferte nach
   21:45 nur einen FlixBus um 03:35 und Morgen-TER, obwohl die Strecke abends regulär RE/ICE fährt. Das ist eine Abdeckungslücke (ausländischer Betreiber), kein
   Fahrplanbefund — **nicht** „danach fährt nichts mehr" behaupten. Stattdessen: Lücke benennen,
   auf SBB/DB verweisen, und wenn die Alternative Auto/Taxi ohnehin sinnvoller ist (Rückfahrt nach
   22:00, Gruppe), das als Empfehlung hinschreiben statt eine unbelegte Verbindung zu konstruieren. Dasselbe Muster
gilt für **Inlandsrelationen mit Umstieg** (Gegenrichtung nach 22:15: im Feed nur Nachtzüge um
01:45/02:15, obwohl die Kette über den Hub abends regulär fährt) — Lücke benennen
und prüfen lassen, nie „danach fährt nur noch die Nacht" behaupten.
13. **Streckenseiten-Slugs sind gepflegt, nicht geraten.** `…/verbindung/<von>/<nach>.shtml`
   existiert für manche Paare, während die Schreibweise mit Zusatz (`-main`, `-breisgau`) 404
   liefert, obwohl die Relation befahren wird. Ein 404 heißt **nicht** „keine Verbindung": andere
   Schreibweise probieren (kurz statt lang, Bindestrich-Orte) oder auf Transitous Bahnhof→Bahnhof
   ausweichen. Zwei 404 hintereinander sind
   ein Slug-Problem, kein Fahrplanbefund — und dürfen nicht als „die Züge fahren abends nicht" in
   die Antwort wandern.
14. **Ob der Zug am Zustiegsbahnhof hält, steht in `intermediateStops` — nicht im Leg.** Bei
   gemeinsamer Reise (einer startet früher, der andere steigt unterwegs zu) genügt „ICE X→Y" nicht:
   dieselbe Relation fährt nicht immer über denselben Knoten. Real fuhr ein ICE der Relation A→B den
   Zustiegsbahnhof komplett um (über einen anderen Knoten), während die Parallelzüge dort hielten —
   der Mitfahrer hätte in ein anderes Fahrzeug umsteigen müssen. Vor der Zusage prüfen:
   `[s for s in leg.get("intermediateStops") or [] if "<Stadt>" in s.get("name","")]` und die
   Abfahrt dort mitliefern.   Fehlt `intermediateStops` ganz, ist das eine Feed-Lücke → Bahnhof→
   Bahnhof gegenprüfen, nicht annehmen.
15. **Ein gebuchtes Ticket gegen den Plan prüfen, nicht nur ablegen.** Aus dem PDF/der Bestätigung
   gehören fünf Felder in die Antwort: **Zielbahnhof** (endet das Ticket am Hub statt am Zielort,
   braucht die letzte Etappe ein eigenes Ticket/D-Ticket), **Zugbindung** (nur der genannte Zug;
   Nahverkehr RE/RB/S ist ungebunden), **Gültigkeitsfenster** (beginnt oft am Vortag 00:00),
   **Storno** (Super Sparpreis = ausgeschlossen) und **Rabatt/Name** (BahnCard + Lichtbildausweis
   sind bei der Kontrolle Pflicht). Weicht der Zielbahnhof vom Reiseziel ab, das **prominent**
   sagen — sonst steht der Mitreisende in Frankfurt ohne Weiterfahrt.
16. **Ähnliche Bahnhofsnamen verwechseln sich.** Zwei Stationen, deren Namen sich um wenige
   Buchstaben unterscheiden (Beispiel: Frankfurt (Main) / Frankfurt (Oder)), rutschen in einer Tabelle
   durch — dort steht dann der Zustiegsbahnhof statt des Ziels. Vor dem Absenden jede Zeile lesen
   und prüfen, ob Start- und Zielbahnhof zur Reise passen (Zustieg vs. Ziel), und die Namen einmal
   gegen die Anfrage abgleichen.

## Beiblätter

- `references/db-navigator-api.md` — Kurzreferenz der DB-Navigator-API (Auth-Header, Endpunkte, Felder,
  Tarif-/Rabatt-Keys) aus dem Reverse-Engineering der Android-App.
- `scripts/dbnav.py` — CLI-Client (nur stdlib): `station`, `search`, `offers`, `bestprice`, `departures`.
- `scripts/transitous_plan.py` — Transitous-Planer für Tür-zu-Tür-Abfragen (Dauer, Umstiege, Abfahrten).
