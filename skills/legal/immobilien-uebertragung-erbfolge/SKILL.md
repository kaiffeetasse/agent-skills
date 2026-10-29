---
name: immobilien-uebertragung-erbfolge
description: "Use when gifting German real estate to heirs."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [legal, erbrecht, schenkung, grundbuch, immobilien, erbschaftsteuer, pflegeregress, sgb11, bewg, notar]
    related_skills: [deutsches-recht, german-property-valuation, ocr-and-documents, document-to-action-items, grounded-citations]
---

# Immobilienübertragung & vorweggenommene Erbfolge (Deutschland)

Klasse: Übergeber (typisch Eltern oder Großeltern) übertragen Immobilien zu Lebzeiten auf die
nächste Generation — Schenkung, Übergabe- und Zuwendungsvertrag, vorweggenommene Erbfolge, mit oder
ohne Vorbehaltsrechte (Wohnungsrecht, Nießbrauch, Rückforderungsrechte). Auch einschlägig für das
Aufräumen alter Grundbucheinträge aus früheren Übertragungen.

**Abgrenzung:** Für die reine **Bewertung** (Bodenrichtwert, BORIS-BW, BewG) → Skill
`german-property-valuation`. Für **allgemeine** Rechtsfragen und die Repo-Sammlung → Skill
`deutsches-recht`. Dieser Skill ist der **Ablauf** der Übertragung inklusive Grundbuchmechanik und
Pflegeregress.

## Sofort-Diagnose: wo liegt das echte Risiko?

1. **Steuer — fast immer unkritisch.** 400.000 € Freibetrag **je Elternteil** (§ 16 Abs. 1 Nr. 2
   ErbStG) = 800.000 € bei gemeinsamer Übertragung. Ein Ein-/Zweifamilienhaus bleibt darunter, selbst
   mit absurd hohen Annahmen. **Stückelung bringt nichts** — § 14 ErbStG rechnet Erwerbe von derselben
   Person binnen 10 Jahren zusammen. Kurz prüfen, dann abhaken.
2. **Pflegeregress — das reale Risiko.** § 528 BGB → § 93 SGB XII, gerechnet am **Marktwert** der
   Zuwendung (nicht am BewG-Wert), mit 10-Jahres-Auslauf nach § 529 Abs. 1 BGB. Die Frist läuft bis zum
   **Eintritt der Bedürftigkeit**, nicht bis zum Tod. Hier liegt die Arbeit.
3. **Grundbuchstand — was steht tatsächlich drin?** Den Angaben der Beteiligten nie glauben; der
   Auszug widerspricht ihnen regelmäßig.

## Ablauf

1. **Unterlagen beschaffen** → `templates/unterlagen-checkliste.md`
2. **Fakten aus den Dokumenten ziehen** → `references/scanned-official-documents.md`
   (Grundbuchauszug, Erbscheine, Altvertrag, Versicherungen kommen meist als Scan **ohne Textebene**;
   OCR **plus** Sichtprüfung jeder Seite ist Pflicht, nicht Kür)
3. **Normen live prüfen** → `references/normen-und-werte.md`
4. **Rechnen:** Bodenwert/Sachwert, Abschlag für Vorbehaltsrechte (§ 13/§ 14/§ 16 BewG),
   Freibetragsvergleich, **Deckungslücke der Pflegeversicherung**.
5. **Struktur entscheiden:** Vorbehaltsrecht ja/nein, welches Objekt wird belastet, Teilung/WEG
   nötig?, Auflage oder reine Schenkung?
6. **Vertrag vorbereiten:** Phasenplan bis zur Beurkundung, Musterklauseln (siehe Referenz).
7. **Vollzug:** Löschung erledigter Alt-Rechte, Auflassung, Unbedenklichkeitsbescheinigung,
   Anzeige nach § 30 ErbStG (**3 Monate**).

## Die Fallstricke, die Zeit kosten

- ⚠️ **„Getilgt" ≠ „gelöscht".** Zurückgezahlte Grundschulden/Hypotheken bleiben in **Abteilung III**
  stehen, bis eine Löschungsbewilligung des Gläubigers vorliegt. Immer im Auszug nachsehen.
- ⚠️ **Erloschene Rechte bleiben im Grundbuch.** Eine beschränkte persönliche Dienstbarkeit endet mit
  dem Tod des Berechtigten (§ 1090 Abs. 2 i. V. m. § 1061 BGB) — die **Eintragung** aber nicht. Das
  Grundbuch ist dann **unrichtig** und wird nach **§ 22 Abs. 1 GBO** per **Unrichtigkeitsnachweis**
  berichtigt; die Bewilligung nach § 19 GBO ist dann entbehrlich. Praktisch am elegantesten: Löschung
  **im selben Notartermin** wie die Übertragung.
- ⚠️ **Deshalb: Löschungspflicht + widerrufliche Vollmacht in den neuen Vertrag.** Altverträge regeln
  das nicht — und 25 Jahre später steht das erloschene Recht noch drin.
- ⚠️ **Form nach § 29 Abs. 1 GBO:** Erklärungen brauchen **öffentliche oder öffentlich beglaubigte
  Urkunden**. Eine Kopie „zur Kenntnisnahme" genügt nicht → Ausfertigung oder beglaubigte Abschrift
  nachfordern.
- ⚠️ **„Gemeinschaftlicher Erbschein" = mehrere Erben EINES Erblassers**, nicht zwei Erblasser. Für die
  Löschung zählt bei Gesamtgläubigern der Erbschein des **zuletzt** verstorbenen Berechtigten.
- ⚠️ **„Auflösend bedingt" heißt nicht automatisch „bis zum Tod".** Im belegten Fall lautete die
  Bedingung wörtlich „erlischt, wenn der Berechtigte **keinen Wohnsitz** mehr hat". Immer den
  Originalvertrag lesen, statt die Bedingung zu unterstellen.
- ⚠️ **Zeitachse aus dem Grundbuch rekonstruieren.** Ein EDV-Neufassungsvermerk „**ohne
  Eigentumswechsel**" heißt: der Eigentümer stand schon **vor** jenem Datum im Blatt. Ein späterer
  Erbfall hat das Objekt dann **nicht** übertragen — genau das wollen Beteiligte oft glauben.
- ⚠️ **§ 14 Abs. 3 BewG:** Endet das Recht mit dem Tod des **zuletzt** Sterbenden, gilt der **höchste**
  Vervielfältiger (in der Regel die jüngere/weibliche Person). Die Tabelle wird jährlich neu
  bekanntgegeben — aktuelle Fassung ziehen, nicht die Zahl von gestern weiterverwenden.
- ⚠️ **Gesamtkosten ≠ Eigenanteil.** Bei der Pflegelücke zuerst § 43 SGB XI und private Zusatztarife
  abziehen; der Eigenanteil ist dann deutlich kleiner als die genannte Heimplatz-Miete.
- ⚠️ **Ein Wohnungsrecht „an einem der Häuser" geht auch auf einem einzigen Flurstück** (§ 1093 BGB:
  „ein Gebäude oder einen Teil eines Gebäudes") — man muss dafür nicht zwingend realteilen. Das
  entspannt Teilungsfragen, ändert aber nichts daran, dass das belastete Haus nicht frei vermietbar
  ist: **die Wahl des belasteten Objekts ist die eigentliche Strukturfrage.**

## Arbeitsweise (von diesem Nutzer erwartet)

- **Normen nie aus dem Gedächtnis** — immer live über MCP `gesetzessuche`. Fehlt ein Gesetz dort
  (z. B. **SGB XI**), direkt bei gesetze-im-internet.de holen — derselbe Primärquelle-Strang. Die
  Fundstelle im Ergebnis kennzeichnen, nicht verschweigen.
- **Rohdaten archivieren** unter `quellen/<typ>/` mit einem README, das sagt, **was** jedes Dokument
  beweist und **was offen bleibt**.
- **Annahmen als Annahmen kennzeichnen**; jede Zahl ohne Quelle ist eine Schätzung, keine Aussage.
- **Widersprüche offen korrigieren** — mit Datum und Begründung, statt stillschweigend zu ersetzen.
  Nutzerangaben sind Hypothese, nicht Faktum.
- **Nichts behaupten, was nicht belegt ist.** Lieber die Lücke benennen als „voraussichtlich"
  formulieren.
- Sprache: **Deutsch**, fachlich und knapp, ohne Erklärtexte.

## Support-Dateien

| Datei | Inhalt |
|---|---|
| `references/normen-und-werte.md` | Verifizierte Normen und Zahlen: Erbfolge-Fristen, Wohnungsrecht, GBO-Berichtigung, BewG/Vervielfältiger, SGB XI, Pflegeregress-Rechnung, Musterklauseln |
| `references/scanned-official-documents.md` | Grundbuchauszug / Erbschein / Altvertrag exakt auswerten: OCR-Pipeline, Pflicht-Sichtprüfung, Archivierung |
| `templates/unterlagen-checkliste.md` | Checkliste der zu beschaffenden Unterlagen + Fragenkatalog an die Übergeber |

## Rechtlicher Vorbehalt

Kein Rechtsgutachten, keine Steuerberatung. Die **Beurkundungspflicht nach § 311b BGB** heißt: der
Notar ist ohnehin im Verfahren — nie als optional darstellen. Fristen und Steuer immer gegen die
Primärquelle und mit Steuerberater/Notar prüfen.
