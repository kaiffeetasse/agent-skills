# Playbooks — Aufgabe → Vorgehen

Ein Playbook pro Aufgabe, die ein Eigentümer wirklich stellt („wie renoviere ich mein Bad?"). Aufbau immer
gleich, damit man schnell zur Antwort kommt:

1. **Kurzantwort** (geht das selbst, wie lange, was kostet grob)
2. **Reihenfolge** (Schritte mit Tagen)
3. **Zahlen** (Aufbauten, Verbräuche, Trockenzeiten, Mengen)
4. **Werkzeug & Material** (kaufen vs. mieten)
5. **Die Fehler, die Geld kosten** (mit Quelle)
6. **Kontrollpunkte** (was man prüft, bevor das nächste Gewerk kommt)
7. **Wann Fachbetrieb** (und warum)
8. **Quellen** + **Unbelegt-Liste**

Regel: nur belegte Zahlen oder als Schätzung markiert. Wo zwei Quellen sich widersprechen, steht der
Widerspruch — nicht der Mittelwert.

## Stand: 23 Playbooks

| Playbook | Datei | Inhalt |
|---|---|---|
| Bad komplett sanieren | `bad.md` | Abdichtung, Fliesen, Wanne, Elektro im Bad, Lichtfarbe, Puffer |
| Decke erneuern | `decke.md` | Streichen, Spachteln Q1–Q4, abhängen, Risse, Trittschall |
| Wände | `waende.md` | Untergrund, Spachtelstufen, Streichen, Tapezieren |
| Estrich & Bodenaufbau | `estrich.md` | Aufbauhöhen, CM-Messung, Ausgleichsmasse, Fugen |
| Fliesen | `fliesen.md` | Untergrund, Zahnung, Verlegeplan, Verbundabdichtung |
| Elektro im Bestand | `elektro.md` | Pfusch-Erkennung, Vorbereitung, Kosten, Normbezug |
| Trockenbau | `trockenbau.md` | Vorsatzschale, Decke, Schacht, Schall-/Brandschutz |
| Dämmung | `daemmung.md` | Dach/Decke/Fassade/Innen, Feuchte, Anschlüsse |
| Fenster & Türen | `fenster-tueren.md` | Tausch, Anschluss, Aufarbeitung, Innentüren |
| Bodenbeläge | `bodenbelaege.md` | Laminat, Vinyl, Parkett, Hybrid, Untergrund |
| Sanitär | `sanitaer.md` | Vorwand, Wasser, Abwasser, Armaturen, Grenzen |
| Heizung & Lüftung | `heizung-lueftung.md` | Heizkörper, FBH, Lüftung, Optimierung |
| Keller & Mauerwerk | `keller-mauerwerk.md` | Ursachen, Abdichtung, Horizontalsperre |
| Schimmel & Feuchte | `schimmel-feuchte.md` | Ursachen-Triage, Lüftungszahlen (UBA), Sanierung |
| Hausbau mit Baufirma | `hausbau-baufirma.md` | Werkvertrag, Grundstück, Angebote, Begehungen, Abnahme |
| Kosten/Bauzeit/Angebote | `kosten-bauzeit.md` | Bauzeitenplan, Angebotscheck, Nachträge, Puffer |
| Werkzeug & Sicherheit | `werkzeug-sicherheit.md` | Ausstattung, Miete, Staub/Asbest, Entsorgung |
| Küche erneuern | `kueche.md` | Arbeitshöhe (Ellbogen − 15 cm), Anschlüsse, Geräte, Fehler, Kosten |
| Außen: Fassade/Terrasse/Einfahrt | `aussen-fassade-terrasse.md` | Anstrich, WDVS-Grenze, Terrassenaufbau, Pflaster, Gefälle, Gerüst-Legende |
| Treppe | `treppe.md` | Streichen/Entlacken (Blei), Belag, Geländer, DIN 18065 |
| Dachboden & Holzbalkendecke | `dachboden-holzdecke.md` | Baurecht, Dämmung, Schwingung/Trittschall, Lastreserven, Holzwurm |
| Entkernen & Entsorgen | `entkernen-entsorgung.md` | Rückbau-Reihenfolge, Schadstoffe, Container/Sortierung, regionale Gebühren |
| Rechtsseite | `recht-renovierung.md` | Verfahrensfreiheit, Nachbarrecht, Denkmalschutz, Versicherung, Helfer |

## Quellenstand

**736 URLs, 734 erreichbar, 0 tot**, 2 bekannt blockiert (kfw.de, landesrecht-bw.de — Inhalt über Browser
geprüft). Stand 09.11.2026, geprüft mit `scripts/linkcheck.py`.

## Prüfstand

Alle Playbooks werden gegen **130 Fehler aus zehn Top-Fehler-Videos** geprüft
(`../transkripte/`, `../fehlerkatalog.json`, `../../scripts/fehlercheck.py`):

```
python3 scripts/fehlercheck.py          # Abdeckung
python3 scripts/fehlercheck.py --gaps   # Lücken je Playbook
python3 scripts/fehlercheck.py --ablate playbooks/elektro.md   # Negativkontrolle
```

Stand 09.11.2026 (nach Durchlauf 2): **96 von 128 bewerteten Fehlern vollständig abgedeckt (75 %),
32 teilweise, 0 ohne jede Abdeckung.** Zwei Fehler sind als Projekt-Anekdote ausgenommen (Wartezeit-Prognose,
Maklerprovision), weil sie keine übertragbare Regel sind. Negativkontrolle (drei Playbooks entfernt) fällt
auf 32 % — der Test unterscheidet. „Teilweise" heißt: das Thema steht drin, aber nicht jede Zahl aus dem
Video. Einzellücken: `--gaps`.

## Was beim Benutzen gilt

- Playbook lesen, dann antworten — nicht aus dem Gedächtnis. Die Zahlen sind belegt, die Erinnerung nicht.
- Wenn das Playbook die Frage nicht deckt: in `../quellen.md` (Recht/Normen) und `../faktencheck.md`
  nachsehen, ob die Fakten belegt sind, sonst als Schätzung antworten und die Lücke benennen.
- Widersprüchliche Quellen werden **als Widerspruch** wiedergegeben, nicht gemittelt (Beispiel: Kostenbänder
  in `estrich.md` 15–25 €/m² vs. 20–35 €/m²).
