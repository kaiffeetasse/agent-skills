---
name: renovierung-gewerke-praxis
description: "Use when judging renovation work: Gewerke, Eigenleistung."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [renovierung, bau, gewerke, elektro, handwerk, abnahme, eigenleistung]
    related_skills: [house-wiring-planning, deutsches-recht, german-property-valuation]
---

# Renovierung: Gewerke, Eigenleistung, Abnahme

Praxiswissen für ein Haus/eine Wohnung in Renovierung: **welches Gewerk in welcher Reihenfolge,
was darf man selbst, was kostet es, wie nimmt man ab und dokumentiert es**. Für Strom-/LAN-Planung
im Detail ist `house-wiring-planning` zuständig, für Recht (Mängel, Honorar, HOAI, VOB) die
Klotzkette-Sammlung (siehe „Recht und Planerseite").

## When to Use

- „Was muss zuerst?", „kann ich das selbst?", „was kostet das", „wer macht das?", „Abnahme",
  „Sanierung Bad/Elektro/Dach", „Gewerk", „Eigenleistung", „Bauablauf"
- Kostenschätzung, Materialliste, Bauzeitenplan, Angebotsvergleich, Bauüberwachung ohne Architekt

Nicht hier: reine Netzwerk-/Router-Konfiguration (`home-assistant`, `fritzbox`), Recht im Streitfall
(`deutsches-recht`), Wertermittlung (`german-property-valuation`).

## Grenze zuerst: was der Eigentümer trotz eigenem Haus NICHT selbst macht

- **230 V**: Errichten, Erweitern und Ändern der Anlage hinter der Hausanschlusssicherung ist dem
  **in ein Installateurverzeichnis eingetragenen Installationsunternehmen** vorbehalten — NAV § 13 Abs. 2,
  auch im eigenen Haus. **Instandhaltung** ist von dieser Pflicht ausgenommen (außer im Bereich zwischen
  Hausanschlusssicherung und Messeinrichtung), bleibt aber Arbeit für jemanden, der sie beherrscht:
  Schutzmaßnahmen prüfen und beurteilen ist Ausbildungsinhalt (ElekAusbV § 4 Abs. 2 Nr. 6), kein
  Allgemeinwissen. DGUV Vorschrift 3 bindet **Unternehmer**, nicht Privatleute — für Eigentümer heißt das:
  ohne Messprotokoll keine Sicherheit und im Schadensfall Kürzung nach § 81 VVG. Legale Eigenleistung ist
  Vorarbeit: Schlitze, Dosen, Kabel **nach Vorgabe** einziehen, Fotos, Doku.
- **Gas** (Therme, Herd, Leitungen): Fachbetrieb nach TRGI, ohne Ausnahme.
- **Trinkwasser-Neuinstallation**: Fachbetrieb (DIN EN 806, VDI/DVGW 6023, Keimfreiheit, Druckprobe).
  Kleinreparaturen an Armaturen sind Eigenleistung.
- **Tragwerk**: Statik/Tragwerksplanung, Wanddurchbrüche, Träger, Deckenausschnitte. Eine als „nicht
  tragend" vermutete Wand ist bis zum Gegenbeweis tragend — Zimmerer lernen „tragende und nichttragende
  Bauteile unterscheiden", genau deshalb ist der Durchbruch Facharbeit.
- **Schadstoffe**: Bei **Baubeginn vor dem 31.10.1993** ist mit Asbest zu rechnen – Fassaden-/Dachplatten,
  Putze, Spachtelmassen, Fliesenkleber, Bodenbeläge inkl. Bitumenkleber, Rohrisolierungen,
  Nachtspeicheröfen. **Rechtslage seit 5.12.2024:** Einen gesetzlichen „Generalverdacht" gibt es nicht
  mehr; **§ 5a GefStoffV** verlangt vom Veranlasser Informationen zur Bau-/Nutzungsgeschichte vor Beginn
  und gilt nach **Abs. 4 ausdrücklich auch für private Haushalte** (nachgeprüft am Volltext). BAuA-Leitlinie
  und Verbraucherzentrale halten am **begründeten Verdacht** für Bauten vor dem 31.10.1993 fest. Rückbau ist
  **ASI-Arbeit**: Anzeige 7 Tage vorher, Sachkunde, TRGS 519 — vorher beproben lassen, nicht „mal eben".

Die Grenze ist keine Formalie: ohne Fachbetrieb fehlt die Gewährleistung gegen Dritte, und bei grober
Fahrlässigkeit kürzt der Versicherer die Leistung (§ 81 Abs. 2 VVG).

## Bauablauf: die einzige Reihenfolge, die kein Geld zweimal kostet

1. **Bestandsaufnahme + Schadstoffcheck** – Fotos je Raum, Maße, Feuchte, Querschnitte, Baujahr.
2. **Rückbau** und Entsorgung (Container, Sortierung, Sperrmülltermine).
3. **Rohinstallation** – Elektro (Leerrohre/Kabel), Sanitär, Lüftung, Heizung: **vor** Dämmung und Putz.
4. **Dämmung**, dann Trockenbau/Vorsatzschalen.
5. **Putz/Spachtel**, danach **Estrich** (Dämmung, Randdämmstreifen), Trocknungszeit abwarten.
6. **Abdichtung in Feuchträumen** (DIN 18534), dann **Fliesen**.
7. **Türen/Zargen**, Treppe, Einbaumöbel – nach Fertigboden, vor Maler.
8. **Maler/Spachtelarbeiten** als letzte staubige Schicht.
9. **Endmontage**: Elektro-Fertiginstallation (Fachbetrieb), Sanitär, Küche.
10. **Abnahme + Dokumentation**, Mängelliste, Zahlungsfreigabe.

Fehler in dieser Reihenfolge kosten doppelt: Kabel nach Putz, Estrich nach Türen, Abdichtung nach
Fliesen. Wenn ein Gewerk warten muss, wird das im Plan sichtbar gemacht, nicht „später eingeschoben".

## Eigenleistung: ehrliche Einschätzung statt Optimismus

Selbst machbar, hoher Hebel, geringes Risiko:
- **Rückbau, Entkernen, Entsorgung** (Brecheisen, Stemmhammer, Schutzausrüstung).
- **Schlitze stemmen, Dosen bohren, Kabel nach Vorgabe einziehen**, Fotos der offenen Wand mit Maßband
  – das wertvollste Artefakt des Projekts.
- **Trockenbau** (Vorsatzschalen, abgehängte Decken nach Herstellerstatik), Dämmung.
- **Maler, Spachteln, Schleifen, Grundieren.**
- **Fliesen** an Wand/Boden legen (nicht die Abdichtung ohne Normkenntnis).
- **Böden**: Laminat, Vinyl-Klick, Fertigparkett schwimmend.
- **Außenanlagen**: Pflaster, Terrasse, Zaun, kleinere Erdarbeiten.

„Lieber Fachbetrieb" trotz Eigenleistungs-Optimismus:
- Bad komplett (Abdichtung, Gefälle, Anschlüsse – der teuerste Fehler im Haus).
- Estrich (Bewehrung, Fugen, Höhenlage, Trocknung – danach ist alles zu spät).
- Fenster/Türen im Bestand (Aufmaß, Anschluss, Dichtheit), Dach und Dachanschlüsse.
- Treppen, Geländer, alles mit Absturzhöhe.
- Heizungshydraulik, Lüftung mit Brandschutzanforderungen.

Aufwand realistisch: Eigenleistung braucht nach Erfahrungswert etwa **ein Drittel mehr Zeit** als beim
Profi (einzige belegte Zahl: Verband privater Bauherren, „etwa ein Drittel mehr Zeit", 2004; die oft
zitierten „doppelt so lange" sind quellenlos) und Werkzeug, das man sonst mietet. Werkzeugmiete ist
billiger als ein zweiter Anlauf (Fliesenschneider, Stemmhammer, Trockenbau-Schrauber, Absaugung,
Nivelliergerät).

## Kosten: rechnen statt raten

Kein Preis ohne Quelle. Rechenweg:

1. **Mengen** aus Maßen: Wandfläche = (Raumumfang × Höhe) − Öffnungen; Fliesen + 10 % Verschnitt
   (Diagonal + 15 %), Farbe nach m² und Ergiebigkeit auf dem Eimer, Dämmung nach Plattenmaß.
2. **Preise** nur mit Beleg: Baustoffhandel-Webseite (OBI/Hornbach/Bauhaus) oder Angebot, dazu
   Kleinanzeigen für Restposten. Datum, Quelle und Link zur Zahl notieren.
3. **Lohn** nur als Angebot oder als nachvollziehbarer Satz, nie „so ungefähr".
4. **Nebenkosten** immer mit: Container/Entsorgung, Gerüst, Werkzeugmiete, Anfahrt, Baustrom/-wasser,
   Versicherung (Bauleistungs-/Feuerrohbauversicherung bei größeren Eingriffen), Puffer 10–15 %.

Die Schätzung ist ein **Band** (min/max), keine Punktzahl. Eine Zahl ohne Quelle ist eine Vermutung
und wird so gekennzeichnet.

## Dokumentation, Abnahme, Gewährleistung

- **Foto-Regel**: jede Wand offen, mit Maßband im Bild, je Raum sortiert abgelegt. Später findet
  niemand mehr ein Kabel ohne diese Bilder.
- **Prüfprotokolle einsammeln**: Elektro-Erstprüfung nach **DIN VDE 0100-600** (Prüfpflicht des
  Unternehmers: DGUV Vorschrift 3), Messprotokoll Erdungswiderstand, Druckprobe Wasser,
  Dichtheitsprotokoll Heizung, Kamin/Feuerstätte.
- **Abnahme** = gemeinsame Begehung mit Mängelliste (Fotos, Fristen, Verantwortlicher) und
  unterschriebenem Protokoll. Ohne Abnahme beginnt keine Gewährleistungsfrist – und die Beweislast kippt.
- **Fristen**: Bauwerk **5 Jahre** ab Abnahme nach BGB § 634a Abs. 1 Nr. 2 (auch für Planungs-/Über-
  wachungsleistungen); bei vereinbarter **VOB/B § 13 Abs. 4** regelmäßig **4 Jahre** für Bauwerke,
  kürzer für Anlagen mit Wartungseinfluss. Vertrag lesen, nicht annehmen.
- **Eigenleistung hat keine Gewährleistung**: was man selbst gemacht hat, zahlt man selbst noch einmal.
- **Belegakte/Bauwerksbuch** anlegen: Angebote, Rechnungen, Protokolle, Fotos, Herstellerunterlagen,
  Garantiescheine – pro Gewerk ein Ordner, digital und einmal ausgedruckt.

## Veröffentlicht

Öffentliche Kopie: `github.com/kaiffeetasse/agent-skills` → `skills/house/renovierung-gewerke-praxis`.
Die lokale Fassung ist die Arbeitsversion; veröffentlicht wird eine **Kopie**, kein Symlink, damit der
Installations-Helfer des Repos den Stand aktualisieren kann.

Beim Veröffentlichen gilt: Landkreis- und Ortsnamen generalisieren (die belegten Zahlen bleiben, der Ort
fällt weg), Gebühren-URLs mit Ortsnamen durch die Quellenangabe in Worten ersetzen, interne Pfade und
Job-IDs entfernen. **Nach dem Push in einem frischen anonymen Klon nachweisen, dass die Kopie
funktioniert** — `python3 scripts/fehlercheck.py` muss dort dieselbe Quote melden wie lokal; weicht sie
ab, fehlt eine Datei oder ein Pfad zeigt ins lokale Home.

Der Ablauf steckt in `scripts/publish_skill.py`: kopieren → generalisieren → **abbrechen** bei verbotenen
Mustern (`/home/…`, LAN-IPs, Mails, Telefon) → Prüfskripte im Ziel laufen lassen → committen → pushen.
`--dry-run` zeigt nur, welche Dateien ersetzt würden. Handarbeit vergisst beim zweiten Mal genau eine
Ortsangabe, und die steht dann dauerhaft in der History.

## Recht und Planerseite (liegt lokal)

Die Klotzkette-Sammlung `eine lokale Rechtssammlung
Plugin **`hoai-leistungsphasen-praxis`** die Skills für die Planer-/Bauherrenseite, u. a.
`lph8-bauueberwachung-elektro-erdung-blitzschutz`, `lph8-bauueberwachung-mehrfamilienhaus-effh`,
`abnahmefahrplan`, `bauherrnentscheidung-matrix`, `anrechenbare-kosten-din276-baukostengruppen`,
`fachplaner-tga-brandschutz-tragwerk-koordination`, `foerdermittel-baukosten`. Dazu `bauwirtschaft`,
`bauvergabe`, `fachanwalt-bau-architektenrecht` für Vertrag/Vergabe/Mängelstreit.
Diese Skills liefern Normbezug, Beweislast, Prüfraster, Formulierungen – **nicht** Handwerkspraxis;
die liefert dieser Skill.

### Welche Planer-Frage gehört zu welchem Klotzkette-Skill

Zuordnung in `references/planer-skills.md` (Bauüberwachung Elektro/Erdung/Blitzschutz, MFH/EFH,
`abnahmefahrplan`, `bauherrnentscheidung-matrix`, DIN 276, TGA-Koordination, Mängelstreit).
Die Playbooks hier beantworten **wie man es macht**; diese Skills **wer es schuldet und wie man es beweist**.
## Wer macht was — laut Ausbildungsordnung

Jede Aufgabe hat einen Beruf, der sie gelernt hat; wer die Zuordnung nicht kennt, fragt den falschen und
zahlt zweimal. Kurzfassung (Belege je Paragraph in `references/ausbildungsordnungen.md`):

- **Elektroniker/-in Energie- und Gebäudetechnik** — Schutzmaßnahmen prüfen und beurteilen, Potentialausgleich,
  Wiederholungsprüfungen, Fehleranalyse.
- **Anlagenmechaniker/-in SHK** — Abdichtung an Ver-/Entsorgungsanlagen, Trinkwasserhygiene, Gas/Öl, Inbetriebnahme.
- **Fliesen-, Platten- und Mosaikleger/-in** — Untergrund, **Belegreife messen**, **Verbundabdichtung nach
  Wassereinwirkungsklasse**, Sanieren.
- **Maler/-in und Lackierer/-in** — Untergrund inkl. Blei/Asbest erkennen, Beschichten, Putz/Dämmung/Trockenbau.
- **Trockenbaumonteur/-in** — Feuchträume, Dachausbau, Brandschutz, Sonderdecken (Abdichtung nur beurteilen).
- **Dachdecker/-in** — Dampfsperre/Luftdichtheit, Flüssigabdichtung, An- und Abschlüsse.
- **Zimmerer/Zimmerin** — tragend/nichttragend unterscheiden, Rückbau, Holzkonstruktionen sanieren.
## Playbooks — Aufgabe → Vorgehen

Für konkrete Fragen („wie renoviere ich mein Bad?“, „wie erneuere ich die Decke?“, „was beachte ich bei
XY?“) liegen fertige Playbooks in `references/playbooks/`: Kurzantwort, Reihenfolge mit Tagen, Zahlen,
Werkzeug/Material, die teuren Fehler mit Quelle, Kontrollpunkte, „wann Fachbetrieb“, Quellen.

- **34 Playbooks** in `references/playbooks/` (Abdeckung 128/128 Katalogfehler, Strukturcheck 0 Verstöße) (Index und Prüfstand: `references/playbooks/README.md`):
  `bad.md`, `decke.md`, `waende.md`, `estrich.md`, `fliesen.md`, `elektro.md`, `trockenbau.md`,
  `daemmung.md`, `fenster-tueren.md`, `bodenbelaege.md`, `sanitaer.md`, `heizung-lueftung.md`,
  `keller-mauerwerk.md`, `schimmel-feuchte.md`, `hausbau-baufirma.md`, `kosten-bauzeit.md`,
  `werkzeug-sicherheit.md`, `kueche.md`, `aussen-fassade-terrasse.md`, `treppe.md`,
  `dachboden-holzdecke.md`, `entkernen-entsorgung.md`, `recht-renovierung.md`,
  `waermepumpe-oelheizung.md`, `pv-speicher-wallbox.md`, `elektro-60er-haus.md`,
  `internet-kabelanschluss.md`, `haus-komplettsanierung.md`, `energieausweis-beratung.md`,
  `heizung-alternativen.md`, `smart-home-nachruesten.md`, `foerderung-steuern.md`,
  `dachentwaesserung-regenwasser.md`, `foto-diagnose.md`
- Jedes Playbook endet mit einem **Fehlerkatalog aus der Praxis** und einer **„Unbelegt“-Liste** — die
  Quelle steht als Video-ID + Zeitmarke dabei, Transkripte liegen in `references/transkripte/`.

### Router: Frage → Playbook (erst hier nachsehen, dann antworten)

| So fragt man | Datei |
|---|---|
| Bad sanieren, Dusche/Wanne tauschen, Feuchtraum, „Fliesen im Bad" | `bad.md` |
| Decke streichen, spachteln, abhängen, Risse in der Decke | `decke.md` |
| Wände spachteln/streichen/tapezieren, Wand versetzen, Nische | `waende.md` |
| Estrich, Ausgleichsmasse, Belegreife, „Boden aufbauen", Türblatt zu niedrig | `estrich.md` |
| Fliesen legen, verfugen, großformatig, Abdichtung unter Fliesen | `fliesen.md` |
| Steckdose, Sicherung, FI/RCD, Verteiler, Kabel, „Strom im Bestand" | `elektro.md` |
| Vorsatzschale, abgehängte Decke, Schacht, Brandschutz, Schallschutz | `trockenbau.md` |
| Dämmen: Dach, Fassade, Kellerdecke, Innendämmung, Dampfbremse | `daemmung.md` |
| Fenster/Türen tauschen, einstellen, aufarbeiten, RC2, Anschluss | `fenster-tueren.md` |
| Laminat, Vinyl, Parkett, Kork, Trittschall, Sockelleisten | `bodenbelaege.md` |
| WC, Waschbecken, Vorwand, Armaturen, „Wasser läuft schlecht ab" | `sanitaer.md` |
| Heizkörper, Fußbodenheizung, Heizungstausch, Lüftungsanlage, „GModG/GEG" | `heizung-lueftung.md` |
| Ölheizung raus, Wärmepumpe, Tankentsorgung, JAZ, Heizlast | `waermepumpe-oelheizung.md` |
| Pellet, Fernwärme, Solarthermie, Gas-Hybrid, Infrarot — was passt? | `heizung-alternativen.md` |
| PV, Speicher, Wallbox, Einspeisung, Anmeldung | `pv-speicher-wallbox.md` |
| Förderung, Steuerbonus, Kredit, was gilt 2026 | `foerderung-steuern.md` |
| Energieausweis, Sanierungsfahrplan, Energieberatung | `energieausweis-beratung.md` |
| Elektro komplett neu (Altbau/60er), Nullung, Alu-Leiter, Zählerplatz | `elektro-60er-haus.md` |
| Internet/Kabel/Glasfaser, HÜP, Hausnetz | `internet-kabelanschluss.md` |
| „Haus komplett sanieren", Reihenfolge, Budget, Steuerung | `haus-komplettsanierung.md` |
| Dachrinne, Versickerung, Zisterne, Garage | `dachentwaesserung-regenwasser.md` |
| Smart Home nachrüsten, KNX, Funk, Datensicherheit | `smart-home-nachruesten.md` |
| „Was sagt das Foto?", Risse, Schimmel, Pfusch erkennen | `foto-diagnose.md` |
| Feuchter Keller, Mauerwerk, Salzausblühungen, Risse im Mauerwerk | `keller-mauerwerk.md` |
| Schimmel, Luftfeuchte, richtig lüften, Schimmel entfernen | `schimmel-feuchte.md` |
| Haus bauen, Baufirma auswählen, Werkvertrag, Baubegleitung, Abnahme | `hausbau-baufirma.md` |
| „Was kostet das?", „Wie lange dauert das?", Angebot prüfen, Nachträge | `kosten-bauzeit.md` |
| Werkzeug kaufen/leihen, Staub, Absaugung, Asbest, Entsorgung | `werkzeug-sicherheit.md` |
| Küche planen, Arbeitshöhe, Anschlüsse, Dunstabzug, Geräte | `kueche.md` |
| Fassade streichen/dämmen (außen), Terrasse, Einfahrt pflastern, Gefälle | `aussen-fassade-terrasse.md` |
| Treppe streichen, entlacken (Blei), Belag, Geländer, Steigungsmaße | `treppe.md` |
| Dachboden ausbauen, Holzbalkendecke, Balken streichen, Holzwurm, Last | `dachboden-holzdecke.md` |
| Entkernen, Bauschutt, Container, „was darf ich selbst rausreißen" | `entkernen-entsorgung.md` |
| Genehmigung nötig?, Nachbar/Gerüst, Denkmalschutz, Versicherung, Helfer | `recht-renovierung.md` |

**Bei Mischfragen** („Bad komplett") gilt die Reihenfolge, nicht das Thema: Rohinstallation → Estrich →
Abdichtung → Fliesen → Türen. Dann mehrere Playbooks in dieser Ordnung lesen; das erste bestimmt, was
später nicht mehr zu ändern ist.

**Frage trifft kein Playbook:** erst `references/playbooks/README.md` (Index), dann die allgemeinen
Abschnitte hier (Grenzen, Eigenleistung, Abnahme) — und im Zweifel sagen, dass es dazu (noch) kein
Playbook gibt, statt aus dem Gedächtnis zu antworten.

**Prüfstand statt Bauchgefühl:** `scripts/fehlercheck.py` prüft den Skill gegen die Fehlerliste aus zehn
Top-Fehler-Videos (`references/fehlerkatalog.json`, Stand und aktuelle Quote in
`references/playbooks/README.md`). Nach jeder Inhaltsänderung:

```bash
python3 scripts/fehlercheck.py --gaps        # was fehlt, gruppiert nach Playbook
python3 scripts/fehlercheck.py --ablate playbooks/elektro.md   # Negativkontrolle: Zahl MUSS fallen
python3 scripts/linkcheck.py                 # alle 736 URLs; 404 = tot, Bot-Blocker sind ausgenommen
python3 scripts/strukturcheck.py             # Pflichtabschnitte je Playbook, Quellenzahl, Preis-Datum
```

Zwei Cronjobs halten den Stand: **montags 9:00** der Wächter `~/.hermes/scripts/renov_skill_health.py`
(Abdeckung + Links, schweigt wenn alles gut ist) und **quartalsweise** ein Sammellauf, der neue
Fehler-Videos sucht, transkribiert und einarbeitet.

**Was der Prüfstand nicht kann:** `fehlerkatalog.json` stammt aus zehn Videos. Die später ergänzten
Themen (Küche, Außen, Treppe, Dachboden, Entkernen, Rechtsseite) sind inhaltlich dokumentiert, aber
automatisch noch nicht geprüft — dort gilt nur die Quellenprüfung.

Neue Videos kommen über `scripts/vtt2txt.py` in die Wissensbasis (Auto-Untertitel entdoppeln, Absätze
mit `[hh:mm:ss]`), Ablauf und Fallstricke in `references/tests/README.md`; jede Datei wird in
`references/transkripte/README.md` mit Kanal, Länge, Datum und URL eingetragen.

### Neues Playbook anlegen (bewährtes Vorgehen)

1. **Thema abgrenzen**, nicht überlappen: im `references/playbooks/README.md` nachsehen, welches Playbook
   das Nachbarthema schon hat, und im neuen Text dorthin verweisen statt zu doppeln.
2. **Auftrag an eine Recherche-Spur** (Subagent) mit festen Vorgaben: mind. 12 Quellen aus mindestens drei
   Quellentypen (Behörde/Norm, Hersteller/Fachverband, Forum/YouTube), **jede URL einzeln abrufen und 404
   melden**, Zahlen statt Adjektive, Längenangaben an YouTube-Zitaten, „Unbelegt"-Liste am Ende.
3. **Ausgabe in einen Scratch-Ordner**, nicht direkt in den Skill — die Integration (Index, Querverweise,
   Katalog, Linkprüfung) macht eine Hand, sonst stehen 23 Dateien mit 23 Indexständen da.
4. **Beim Einhängen prüfen, was der Auftrag falsch vorgegeben hat.** Recherche-Spuren korrigieren auch die
   Vorgabe: falsche Normmaße, erfundene Pflichten (eine „Gerüstpflicht ab 3 m" ist schweizerisch, nicht
   deutsch) und überholte Stichtage fallen dabei auf. Widersprüche zwischen zwei Playbooks sofort
   angleichen, sonst hat der Skill zwei Wahrheiten.
5. **Danach**: `fehlercheck.py`, `linkcheck.py`, Index-Zeile, `SKILL.md`-Liste, Abdeckung im README
   nachziehen.

## Bauen und Prüfen — Regeln, die für jede Erweiterung gelten

1. **Playbook zuerst lesen, dann antworten.** Die Zahlen sind belegt, die Erinnerung nicht.
2. **Regel und Anekdote trennen.** Ein Fehler aus einem Video besteht aus einer übertragbaren Regel
   (kommt ins Playbook) und oft aus einer Projekt-Anekdote (Euro-Betrag, Produktname, „7 m³", „1200 € für
   7 Türen"). Nur die Regel wird geprüft; Anekdoten werden im Katalog `scored:false` gesetzt — sonst misst
   der Test Zitate statt Wissen und die Quote wird Theater.
3. **Den Test testen, bevor man ihm glaubt.** Nach jeder Änderung an Katalog oder Matcher eine
   Negativkontrolle fahren (`--ablate <playbook>`); fällt die Quote kaum, sind die Prüfbegriffe zu
   allgemein. Details und die zwei Normalisierungsfallen in `references/tests/README.md`.
4. **Quelle prüfen heißt abrufen, nicht erinnern.** Eine URL, die plausibel klingt, ist keine Quelle: die
   VOB/B steht **nicht** auf gesetze-im-internet.de (404) und ist kein Gesetz, sondern Vertragsbestandteil.
   Status prüfen: 200 = gut, 401/403/429 = existiert (Bot-Schutz), 404/410/000 = tot. **200 ist aber kein
   Inhaltsnachweis**: Landesrechtsportale liefern für jede Dokument-URL eine JS-Hülle mit 200 — dort den
   Text über die amtliche PDF-Fassung holen. Tote Links im Text als tot **markieren**, nicht stillschweigend
   löschen — die Aussage verliert damit ihre Grundlage.
5. **Kein Volltext-Zitat aus einer Norm, die man nicht gekauft hat.** Belegt sind Nummer, Titel und
   gültige Ausgabe; Inhalte nur über eine zitierende Fachquelle.
6. **Normen ändern sich — die Fassung mitprüfen, nicht die Erinnerung.** Beispiel: der Asbest-Generalverdacht
   fiel 2024 aus der GefStoffV, DIN 18065 erlaubt beim Auftritt 23–37 cm (26–32 cm ist Komfortband, keine
   Grenze). Wo eine Zahl aus zweiter Hand kommt, gegen die aktuelle Fassung oder eine Fachquelle prüfen.
7. **Nur was das Modell nicht selbst weiß, ist Pflege wert.** Kalt/Warm-Probe: dieselbe Frage einmal ohne,
   einmal mit Playbook. Steht in der warmen Antwort nur, was die kalte auch hatte, bringt das Playbook
   keinen Nutzen — dann Zahlen, Quellen und Vollständigkeit nachlegen oder es mit einem Nachbarthema
   zusammenlegen. Umgekehrt gilt: wird die kalte Antwort **besser** als das Playbook, ist das Playbook
   falsch und wird korrigiert, nicht verteidigt.
8. **Eine Korrektur gilt für alle Dateien, nicht nur für die, in der sie auffiel.** Sobald ein Stichtag,
   eine Norm oder eine Pflicht berichtigt wird: `grep -rn "<Begriff>" references/` und **jede** Fundstelle
   angleichen. Bleiben Einzelfassungen stehen, liefert der Skill je nach Router-Ziel eine andere Antwort —
   und die nächste Recherche muss den Widerspruch erneut auflösen. Ein korrigierter Asbest-Satz betraf
   sechs Dateien; ein Patch an einer hätte fünf falsche Fassungen konserviert.

Änderst du an diesen Regeln etwas, laufen beide Skripte erneut — sie sind die Regression, nicht die Deko.

Arbeitsweise: erst Playbook lesen, dann die Frage beantworten — nicht aus dem Gedächtnis. Fehlt ein
Playbook, zuerst `references/quellen.md` und `references/faktencheck.md` prüfen, ob die Fakten belegt sind.

## Normen (Orientierung, kein Ersatz für die Norm selbst)

DIN/DIN-VDE sind kostenpflichtig (Beuth/DIN Media); hier nur die Zuordnung mit geprüfter Ausgabe, damit
man beim Fachbetrieb die richtige Nummer nennt. Belege, Ausgaben und die Korrekturen früherer Fassungen:
`references/quellen.md`.

- **DIN 18015-3:2016-09** Leitungsführung und Anordnung der Betriebsmittel (Wohngebäude)
- **DIN VDE 0100-410:2018-10** Schutz gegen elektrischen Schlag; **DIN VDE 0100-540:2024-06** Erdung,
  Schutzleiter, Potentialausgleich; **DIN VDE 0100-520** Kabel/Leitungen (aktuelle Ausgabe prüfen)
- **Prüfung**: Erstprüfung **DIN VDE 0100-600**, Wiederholungsprüfung **DIN VDE 0105-100**
  (die alte **0100-610** ist zurückgezogen)
- **DIN 18014:2023-06** Erdungsanlagen für Gebäude; **DIN EN IEC 62305:2026-02** Blitzschutz, Teile 1–4
- **DIN 18534-1:2025-10** Abdichtung von Innenräumen (Reihe seit 2017)
- **DIN 4108-3:2024-03 / -4:2020-11** Wärmeschutz/Feuchteschutz, **DIN 4109-1/-2:2018-01** Schallschutz,
  **GModG** (früher GEG, seit 29.07.2026 umbenannt; § 71 = 65-%-Pflicht **weggefallen**, § 43 Biotreppe)
- **VOB/C**: **DIN 18322:2023-09** Kabelleitungstiefbau, **DIN 18382:2023-09** Elektro-/Sicherheits-/
  IT-Anlagen, **DIN 18384:2019-09** Blitzschutz/Überspannung/Erdung, **DIN 18386:2019-09** Gebäudeautomation

## Pitfalls

- **Neue Steckdosen an alten zweiadrigen Leitungen ohne Schutzleiter**: zweipolige Steckdosen ohne
  Schutzkontakt waren nur bis 1973 zulässig, und ein PEN-Leiter ist bei Querschnitten unter 10 mm² seit 1973
  für Neuanlagen verboten. Eine neue Schuko-Dose an alter Zweiadrigkeit ist damit unzulässig; Abhilfe heißt
  neue Leitung (stemmen), Aufputzkanal oder Neuaufbau des Stromkreises durch den Fachbetrieb. FI 30 mA ist
  für Steckdosenstromkreise seit 2007 (≤ 20 A) bzw. 10/2018 (≤ 32 A) bei Neu/Erweiterung Pflicht.
- **Bad ohne Abdichtung nach DIN 18534** fliest man nicht: die Norm ist keine Rechtsnorm, aber sie gilt
  über die anerkannten Regeln der Technik als geschuldet (§ 633 BGB), und sie gilt beim Neubau **und** bei
  der Instandhaltung. Wer sie ignoriert, haftet für den Feuchteschaden.
- **Estrich zu früh belegt**: Belegreife wird gemessen (CM-Verfahren), nicht am Kalender abgelesen —
  Zementestrich ≤ 2,0 CM-% (beheizt ≤ 1,8), Calciumsulfat ≤ 0,5. Sonst quellen Holzbeläge, Beläge
  verspannen und reißen.
- **Türen vor Fertigestrich** eingebaut → Absenkung, Kürzen, neu kaufen.
- **Asbest bei Baubeginn vor dem 31.10.1993**: Bodenkleber, Platten, Spachtelmassen, Rohrisolierung werden
  beim Schleifen zur Faserquelle – Erkundung/Probe vor Rückbau, Rückbau nur als ASI-Arbeit mit Anzeige.
  Der gesetzliche „Generalverdacht" ist seit 5.12.2024 entfallen (§ 5a GefStoffV: Informationspflicht, gilt
  auch privat) — der praktische Verdacht bleibt, die Belegkette heißt jetzt BAuA-Leitlinie, nicht Gesetz.
- **Angebot ohne Positionen** („Bad komplett 12.000") ist nicht vergleichbar: nach Positionen, Material
  und Stunden aufschlüsseln lassen.
- **Eigenleistung ohne Bauzeitplan** blockiert das Folgegewerk; jede Woche Verzug kostet Termine.
- **Keine Fotos der offenen Wände** → der teuerste Fehler, den man mit einer Stunde Fotografieren verhindert.

## Belege

- `references/quellen.md` — Index: Recht (NAV inkl. Instandhaltungs-Ausnahme, HwO, BGB, VOB/B, DGUV V3,
  VVG), Normen mit gültiger Ausgabe, Asbest-Regeln, Liste der Korrekturen, „unbelegt"-Liste.
- `references/ausbildungsordnungen.md` — sieben Berufe, Verordnung + Paragraph + wörtliche Zitate.
- `references/praxisbeispiele.md` — 11 Videos und 15 Foren-/Reddit-Threads mit URL, Jahr und Zitat.
- `references/faktencheck.md` — Gegenprüfung von fünf verbreiteten Behauptungen, mit Urteil je Punkt.
- `references/tests/README.md` — wie der Prüfstand funktioniert (Abdeckungstest, Negativkontrolle,
  Katalog-Pflege, Linkprüfung); `references/tests/kalt-warm.md` — die Kalt/Warm-Probe als Maß dafür,
  was ein Playbook tatsächlich hinzufügt.
- `references/transkripte/` — zehn Video-Transkripte mit Zeitmarken (Quelle jedes Fehlers im Katalog).
- `scripts/fehlercheck.py`, `scripts/linkcheck.py`, `scripts/strukturcheck.py` — Abdeckungs-, Link- und
  Strukturprüfung, alle mit Exit-Code; `scripts/publish_skill.py` veröffentlicht die generalisierte Kopie.
- `scripts/vtt2txt.py` — Auto-Untertitel (VTT) entdoppeln und als Transkript mit Zeitmarken schreiben,
  wenn neue Videos in den Katalog sollen.

Regel beim Zitieren: Normnummer + Ausgabe nennen, bei DIN-Volltexten sagen, dass nur Nummer/Titel/Ausgabe
geprüft ist, und jede Zahl ohne Quelle als Schätzung kennzeichnen.
