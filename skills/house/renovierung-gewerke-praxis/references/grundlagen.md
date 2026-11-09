# Grundlagen (ausgelagert aus SKILL.md)

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
