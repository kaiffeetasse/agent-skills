# Amtliche Dokumente exakt auswerten (Scan ohne Textebene)

Diese Dokumente kommen fast immer als **Scan oder Foto-PDF ohne Textlayer**: Grundbuchauszug,
Erbschein, Notarurkunde/Altvertrag, Versicherungsinformation. Der Fehler ist nicht „OCR lief nicht" —
er ist **selbstsicher aus OCR zu zitieren, wo es auf Genauigkeit ankommt**: Tabellen, Unterschriften,
handschriftliche Nummern.

## 1. Zuerst prüfen: gibt es überhaupt einen Textlayer?

```bash
pdfinfo datei.pdf | grep -Ei "pages|page size|producer|creationdate"
pdftotext -layout datei.pdf - | wc -c      # ~0–10 Zeichen => reiner Scan
```

`Producer: macOS … Quartz PDFContext` deutet stark auf Fotos/Scans hin, die in ein PDF gepackt wurden
→ kein Textlayer. Dann nicht mit `pdftotext`-Varianten Zeit verlieren, sondern direkt OCR.

## 2. Rendern und OCR

```bash
pdftoppm -r 300 -gray -png datei.pdf seiten/v     # 300 dpi, Graustufen bleiben handlich
tesseract --list-langs                            # Sprachpaket (z. B. deu) vorher prüfen
for f in seiten/v-*.png; do tesseract "$f" "${f%.png}" -l deu --psm 6; done
```

300 dpi Graustufen reichen für OCR und sind ~10× kleiner als Farbe. `--psm 6` passt für Briefe und
A4-Tabellen. Pro Seite `.txt` **und** eine zusammengeführte Datei behalten — man grept später darüber.

## 3. Pflicht: jede Seite zusätzlich visuell lesen

OCR ist ein **Entwurf**, nie die Quelle. Jede Inhaltsseite mit Vision nachlesen — und zwar mit der
**Liste der Felder**, die man braucht, nicht mit „was steht da":

> „Lies exakt ab: Spaltenüberschriften, und je Zeile lfd. Nummer, Flurstück, Größe **mit Einheit**,
> Nutzungsart, Lage. Ist die Eintragung rot durchgestrichen oder als gelöscht markiert?"

Belegte Fehlerarten:

- **Unterschriften:** OCR lieferte `Wolt-AlfredeNedener` statt des tatsächlichen `Wolf-Alfred Wegener`,
  und `Lin 9:77`, wo ein Name stand. **Nie einen Namen aus OCR allein berichten.**
- **Handschriftliche Zeichen:** ein handschriftliches Aktenzeichen (`2 UR 981/2001`) war kaum lesbar —
  bestätigt wurde es erst über den **Verweis auf dieselbe Nummer in einem anderen Dokument**.
- **Spaltensemantik, nicht nur Ziffern:** OCR gab eine Grundbuchzeile als
  `1 132.31 103 Musterstraße 12, 12 a 95`. Die `132.31` sah nach Fläche aus — visuell war es die
  *bisherige* laufende Nummer, und die Fläche stand in den Spalten `ha | a | m²` als `8 | 95`
  → **895 m²**. Eine Größe aus OCR-Ziffern allein abzuleiten, ergab eine falsche Zahl.
- **„Gelöscht"-Markierungen:** deutsche Grundbuchauszüge warnen im Kopf selbst, dass **rot**
  dargestellte (also gelöschte) Einträge **schwarz** gedruckt sein können. „Die Zeile sieht leer aus"
  ist damit **kein** Beweis — die Fortsetzungsseiten (`Einlegeblatt 2`, Spalten *Veränderungen /
  Löschungen*) müssen **einzeln** visuell geprüft werden, bevor man „keine gelöschten Einträge"
  behauptet.
- **Kopf-/Fußzeilen:** `Hauptstraße`, `7933 Musterstadt` statt `77933 Musterstadt` — eine fehlende Ziffer in einer
  Postleitzahl sieht man nur, wenn man hinsieht.

## 4. Beweise archivieren, nicht nur das Ergebnis

Bewährtes Layout im Projektordner:

```
quellen/<dokumenttyp>/
├── <JJJJ-MM-TT>_<kurztitel>.pdf      # Arbeitskopie des Originals
├── seiten/<name>-01.png …            # 300-dpi-Seitenbilder (später nachprüfbar)
├── seiten/<name>-01.txt …            # OCR je Seite
├── <name>_OCR.txt                    # OCR zusammengeführt
└── README.md                         # was es beweist + was offen bleibt
```

Das `README.md` **ist** das Produkt: je extrahiertem Faktum eine Zeile mit der Seite, aus der es
stammt, plus ein ausdrücklicher Abschnitt **„Was diese Dokumente NICHT belegen"** und eine Liste der
verbleibenden OCR-Unsicherheiten mit Verweis auf das Seitenbild. Eine spätere Session muss ohne
Neu-Auswertung nachprüfen können — und wissen, welche Zahlen belastbar sind. Die
Reproduktionsbefehle mit ins README.

## 5. Disziplin

- **Nie eine OCR-Vermutung zu einem Faktum hochstufen.** Was nicht lesbar ist, wird als „OCR unsicher,
  siehe `seiten/…png`" notiert.
- **Zweitquelle bevorzugen.** Zwei unabhängige Dokumente mit derselben Zahl (ein Vertrag von 2001 und
  ein Registerauszug von 2026 nennen beide `895 qm`) sind echte Bestätigung; ein OCR-Lauf ist es nicht.
- **Nach jeder Korrektur nachrechnen.** Wenn sich eine Zahl ändert, alle abhängigen Werte mitziehen und
  die Korrektur mit Datum und Grund kennzeichnen statt stillschweigend zu überschreiben.
- **Textlayer-PDFs zuerst `pdftotext -layout`** — Versicherungsinformationen o. Ä. sind oft digital
  erzeugt und in einer Minute vollständig lesbar; dort ist OCR unnötiger Umweg.
