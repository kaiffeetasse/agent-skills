# DB Navigator (vendo) API — Kurzreferenz

Reverse-Engineered aus `db-navigator-26-20-0.xapk` (`db.vendo.android.vendigator` 26.20.0, Okt 2026).
Der Vollreport (Decompile-Pfade, Buchungsfunnel, RE-Details) liegt außerhalb dieses Repos.
Diese Datei = das, was man beim Abfragen braucht.

## Basis & Auth

```
BASE = https://app.services-bahn.de
```

| Header | Wert | Pflicht | sonst |
|---|---|---|---|
| `User-Agent` | `DBNavigator/Android/26.20.0` | **ja** | `452 OPS_BLOCKED` |
| `X-Correlation-ID` | beliebige UUID | **ja** | `405` mit leerem Body |
| `Content-Type` / `Accept` | `application/x.db.vendo.mob.<bereich>.v<N>+json` | ja | `400` |
| `X-Device-Os-Name` / `-Version` / `-Model`, `X-App-Version`, `Accept-Language` | Android / 34 / Pixel 7 / 26.20.0 / `de-DE, de;q=0.9` | nein | – |

Kein API-Key, kein OAuth für Suche/Preise. `X-acf-sensor-data` (Akamai BAP) braucht nur der
Buchungsfunnel, nicht die Suche.

Content-Types: `location.v3`, `verbindungssuche.v9`, `bahnhofstafeln.v2`, `warenkorb.v9`,
`zuglauf.v2`, `wagenreihung.v4`, `verbindungteilen.v1`, `stammdaten.v7`.

## Endpunkte

| Zweck | Aufruf | Body-Kern |
|---|---|---|
| Stationssuche | `POST /mob/location/search` | `{"searchTerm":"Frankfurt","maxResults":5}` → `locationId`, `evaNr` |
| Verbindung + Preis | `POST /mob/angebote/fahrplan` | `reiseHin.wunsch{abgangsLocationId,zielLocationId,zeitWunsch{reiseDatum,zeitPunktArt}}, reisendenProfil.reisende[], klasse` |
| Tarifstaffel | `POST /mob/angebote/recon` | `verbindungHin{kontext}` (aus `verbindungen[i].verbindung.kontext`), gleiche `reisende` |
| Tagesbestpreis | `POST /mob/angebote/tagesbestpreis` | wie `fahrplan`, `reiseDatum` = `YYYY-MM-DDT00:00:00` |
| Abfahrtstafel | `POST /mob/bahnhofstafel/abfahrt` | `{"ursprungsBahnhofId":"8000290","datum":"YYYY-MM-DD","verkehrsmittel":[]}` |
| Zuglauf | `GET /mob/zuglauf/{zuglaufId}` | – |
| Wagenreihung | `POST /mob/zuglaeufe/halte/by-abfahrt/wagenreihung` | nur ICE, sonst `404 WAGENREIHUNG_NICHT_GEFUNDEN` |

## Preis im fahrplan-Response

```
verbindungen[i].angebote.preise.gesamt.ab.betrag        # Klassenpreis, „ab"
verbindungen[i].angebote.preise.gesamt.streichpreis     # durchgestrichen (nur mit Rabatt)
verbindungen[i].angebote.angebotsMeldungen[]            # z. B. "Preisauskunft nicht möglich"
verbindungen[i].verbindung.kontext                      # Blob für /mob/angebote/recon
```

`recon` liefert `angebotsCluster[].angebotsSubCluster[].angebotsPositionen[].einfacheFahrt.standard`
mit `reisePosition.name` (Super Sparpreis / Sparpreis / Flexpreis), `preis`, `streichpreis`,
`konditionen[]`, `angebotsKontext.angebotsId` und `lupKategorien.angebotsArt`
(`SSP`, `SPP`, `FLP`).

## Gleise und Halte pro Abschnitt

Das Leg selbst trägt kein Gleis. Es steht pro Halt in `verbindungsAbschnitte[].halte[]`:

```
halt.ort.name, halt.abgangsDatum / halt.ankunftsDatum, halt.gleis
```

Damit lässt sich eine Umstiegsprüfung bauen (Ankunftsgleis vs. Abfahrtsgleis, Umsteigezeit) und die
Antwort mit „Gleis 9 → Gleis 8“ konkret machen. Die Halte-Liste ist außerdem der Beweis, ob ein Zug
an einem Zwischenbahnhof hält (Zustieg eines Mitreisenden) — fehlt sie, gegen die Abfahrtstafel prüfen.

Hinweis zum CLI: `--json` ist ein **globales** Flag, also `dbnav.py --json search …`; hinter dem
Subcommand wird es nicht geparst und die Ausgabe ist die Tabelle.

## Erlaubte Werte

| Feld | Werte |
|---|---|
| `klasse` | `KLASSE_1`, `KLASSE_2` |
| `zeitPunktArt` | `ABFAHRT`, `ANKUNFT` |
| `reisendenTyp` | `ERWACHSENER`, `SENIOR`, `JUGENDLICHER` (braucht `alter`), `FAMILIENKIND`, `KLEINKIND`, `FAHRRAD`, `HUND` |
| `ermaessigungen[]` | Keys aus `assets/stammdaten/stammdaten_v7.json`, **klassenbindend mit Leerzeichen**: `"BAHNCARD25 KLASSE_2"`, `"KEINE_ERMAESSIGUNG KLASSENLOS"`, `"A-VORTEILSCARD KLASSENLOS"`, … |
| `verkehrsmittel[]` | `ALL`, `HOCHGESCHWINDIGKEITSZUEGE`, `INTERCITYUNDEUROCITYZUEGE`, `NAHVERKERHRSONSTIGEZUEGE`, `SBAHNEN`, `BUSSE`, `SCHIFFE`, `UBAHN`, `STRASSENBAHN`, `ANRUFPFLICHTIGEVERKEHRE` |

## Fehlercodes

| Code | Body | Ursache |
|---|---|---|
| 452 | `{"status":"ERROR","code":"OPS_BLOCKED"}` | User-Agent fehlt/falsch |
| 405 | leer | `X-Correlation-ID` fehlt |
| 400 | `{"domain":"MOB","code":"VALIDIERUNG"}` | Body-Schema falsch |
| 400 | `{"domain":"MODA","code":"FATAL"}` | Ermäßigungs-Key falsch (z. B. `BAHNCARD25` ohne Klasse) |
| 403 | HTML „Access Denied" | falscher Host (`www.bahn.de`-Web-API statt `app.services-bahn.de`) |

## Gemessene Tariflogik (Berlin–Hamburg, 2. Klasse)

| Rabatt | Super Sparpreis | Sparpreis | Flexpreis |
|---|---|---|---|
| keiner | 39,99 € | 46,99 € | 112,80 € |
| BahnCard 25 | 30,99 € | 36,24 € | 84,60 € |
| BahnCard 50 | 30,99 € | 36,24 € | 56,40 € |
| BahnCard 100 | – | – | – („keine Preisauskunft wegen Ermäßigungsart") |

Sparpreise werden nur mit 25 % rabattiert, egal ob BC25 oder BC50 — deshalb identische Werte.

## Buchung (nicht Teil von dbnav.py)

`POST /mob/warenkorb` → `201` + `warenkorbId`; `PATCH /mob/warenkorb/{id}` (Reisende/Zahlung);
`POST /mob/buchungen/anonym`. Warenkorb funktioniert anonym, der letzte Schritt erzeugt einen
Beförderungvertrag — **nur mit ausdrücklicher Freigabe ausführen**.

## Offen

* Hin+Rück kombiniert: `suchParameter.reisewunschRueck` liefert nur eine Richtung;
  `reiseHin` + `reiseWunschRueck` → 400. Kombipreis entsteht erst im Warenkorb.
* Sitzplatzwahl: `recon` liefert die Position (5,50 €), Platzwahl/Wagenreihung nicht implementiert.
* Verbund-/Ländertickets: `POST /mob/katalog/angebot` braucht Cluster-`angebotsId` (unverifiziert).
