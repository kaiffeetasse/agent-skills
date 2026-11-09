# Die zehn besten deutschsprachigen Online-Quellen für Handwerks-Anleitungen

Stand 09.11.2026. Jede Zeile am Tag der Prüfung per HTTP-Abruf getestet; wo „Stichprobe" steht, wurde
zusätzlich ein Fachartikel geladen und auf Zahlen, Normbezüge und Datum geprüft.

Die Liste ist **nach Nutzwert für praktische Anleitungen** sortiert, nicht nach Prestige. Wichtig: keine
dieser Seiten ist eine Primärquelle für Zahlen. Zahlen belegt man mit Gesetz, Norm, Datenblatt oder
Messung — diese Seiten sagen einem, **wo** man suchen muss und **wie** es praktisch geht.

## 1. BauNetz Wissen — baunetzwissen.de

Das nächste, was es zu einem „Wikipedia für Bauen" gibt: redaktionell betreute Fachbeiträge zu Bauphysik,
Konstruktion, Materialien, Gebäudetechnik, mit Kennwerten und Detailzeichnungen. Kostenlos, werbefrei,
Autoren sind Architekten und Ingenieure. **HTTP 200.** Einschränkung: Seiten sind JS-lastig, ein einfacher
Textabruf liefert oft nur die Navigation — im Browser vollständig.
Beispiel: `baunetzwissen.de/bauphysik/fachwissen/waermeschutz/der-u-wert-als-bauphysikalische-kenngroesse-433`

## 2. Selbst ist der Mann — selbst.de ⚠️ nur noch als Archiv

**Korrektur vom 09.11.2026:** Die Seite ist als Artikelarchiv **tot**. Jede Artikel-URL antwortet **301**
und leitet auf `bauer-plus.de/selbst-info` um — dort steht eine Magazin-Landingpage, kein Anleitungsarchiv
(`curl -skIL` selbst geprüft). Inhalte sind nur noch über **Wayback-Kopien** erreichbar (2023–2026).
Wer daraus zitiert, nennt die Archivkopie mit Datum. Für neue Recherchen: nicht mehr verwenden,
stattdessen Nr. 3, 4 und 7.

## 3. OBI Magazin — obi.de/magazin

Ratgeber und Anleitungen für Heimwerker, breit (Bad, Boden, Garten, Elektro-Basics). **HTTP 200.**
Wichtig: tiefe Links veralten schnell — bei uns sind mehrere `obi.de/magazin`-Adressen inzwischen **404**.
Wer daraus zitiert, prüft den Link am Zitiertag und nennt das Datum.

## 4. HORNBACH Ratgeber — hornbach.de/ratgeber

Anleitungen plus Projektpläne und Materiallisten, oft mit Preisbezug. **HTTP 403 für Skripte**
(Bot-Schutz, „Client Challenge") — im Browser normal nutzbar. Für Automatisierung ungeeignet.

**Messhinweis:** OBI und bau.net beantworten **HEAD** mit 404, auf **GET** aber 200. Ein Linkchecker, der nur
HEAD prüft, meldet beide als tot — `linkcheck.py` prüft deshalb seit dem 09.11.2026 mit GET nach.

## 5. Elektropraktiker — elektropraktiker.de

Fachzeitschrift für Elektrotechnik mit frei zugänglichen Fachartikeln (z. B. „Prüfung von
Fehlerstrom-Schutzschaltern", ep 4/2009, 52 Zahlenwerte im Text). **HTTP 200.** Für Elektro-Themen die
beste deutschsprachige Praxisquelle; ältere Artikel sind teils Abo, aber die Fundstellen bleiben zitierbar.

## 6. IKZ und SBZ — ikz.de / sbz-online.de

Sanitär, Heizung, Klima. IKZ hat ein offenes Praxis-Archiv (Artikel von 2004 bis heute), SBZ liefert
Branchen- und Technikbeiträge. **Beide HTTP 200.** Achtung: Archivtexte sind teils Jahrzehnte alt — Datum
prüfen, sonst zitiert man eine Norm von 2004 als geltend.

## 7. Malerblatt, bauhandwerk, dach+holzbau — malerblatt.de / bauhandwerk.de / dach-holzbau.de

Die Gewerke-Fachpresse: Maler und Lackierer, Ausbau/Trockenbau, Dach und Holzbau. **Alle HTTP 200.**
Hier stehen die Details, die in Heimwerker-Ratgebern fehlen (Untergrund, Systemaufbau, Verarbeitungsgrenzen).

## 8. BAU.NET Forum — bau.net

Über 100.000 Forenbeiträge seit 25 Jahren, gegliedert nach Gewerk (Estrich, Heizung, Elektro …).
**HTTP 200.** Das ist Erfahrungswissen, **kein Beleg**: für Symptome und Fehlersuche sehr wertvoll
(„wer hatte das auch?"), für Zahlen und Normen unbrauchbar. Immer gegen Fachquelle prüfen.

## 9. Verbraucherzentrale — verbraucherzentrale.de

Unabhängig, gut für Recht, Geld, Förderung, Verträge, Abzocke. **HTTP 200.** Keine Bautechnik — die
Grenze ist klar: für „wie dämme ich" nichts, für „was darf der Handwerker berechnen" viel.

## 10. Baufachinformation (Fraunhofer IRB) — baufachinformation.de

Bibliothek und Volltextarchiv für Baufachliteratur; Themen-Dossiers (z. B. Schimmel) mit Zusammenfassungen.
**HTTP 200.** Wichtig: die Inhalte sind **kostenpflichtig** (Bücher 30–90 €, Aufsätze als PDF), frei ist
der Nachweis. Genau dafür ist es gut: man findet den Aufsatz, der eine Zahl belegt — nicht die Zahl selbst.

## Nicht in die Liste, aber für Zahlen unverzichtbar

- **Gesetze**: `gesetze-im-internet.de` — GModG (früher GEG), BGB, HwO, BBiG, TKG, StrlSchG, TrinkwV.
- **Normen**: `beuth.de` (DIN Media) und `vde-verlag.de` — kostenpflichtig, aber die einzige belastbare
  Quelle für Maße und Klassen. Im Skill stehen deshalb nur Nummer, Titel und Ausgabe, keine abgeschriebenen
  Normtexte.
- **Bauaufsicht**: `dibt.de` — allgemeine bauaufsichtliche Zulassungen (AbZ) und Leistungserklärungen.
- **Statistik/Preise**: Destatis, Bundesnetzagentur (MaStR, Einspeisevergütung), KfW/BAFA-Merkblätter.

## Wie diese Liste im Skill verwendet wird

Regel im Skill: **Anleitungen** dürfen aus 1–8 kommen, **Zahlen** nur aus Gesetz, Norm, Datenblatt,
Messung oder amtlicher Statistik. Forum (8) ist Hinweis, nie Beleg. Herstellerseiten (Knauf, PCI, Schöck,
Wienerberger) sind für Systemaufbauten erste Wahl — aber interessengeleitet, deshalb immer mit einer
neutralen Quelle gegenprüfen.
