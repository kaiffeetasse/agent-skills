---
name: dsgvo-werbewiderspruch
description: "Werbung stoppen / Datenlöschung per DSGVO bei Firmen."
version: 1.0.0
author: kaiffeetasse
license: MIT
metadata:
  hermes:
    tags: [dsgvo, werbung, widerspruch, loeschung, verbraucherrecht]
    related_skills: [paperless-nas-operations, himalaya, deutsches-recht]
---

# Werbewiderspruch & Datenlöschung gegenüber Firmen (DSGVO)

## When to Use

- Der Nutzer schickt einen Werbebrief/Flyer/Scan und sagt „abbestellen“, „kein Bock mehr auf Werbung“,
  „löschen nach DSGVO“, „Werbung stoppen“.
- Eine Firma schreibt ihn unter einer **veralteten Anschrift** an oder wirbt, obwohl er kein Kunde ist.
- Ein Widerspruch soll nachgehalten werden (Bestätigung, Aufsichtsbehörde).

Für jede Werbesendung, die der Nutzer nicht mehr will: adressierte Post, E-Mail, Postbox-Werbung,
Telefonanrufe. Ergebnis ist immer (a) versendete E-Mails an die richtigen Stellen, (b) ein PDF zum
Ausdrucken/Nachhalten, (c) eine Verifikation, dass der Versand wirklich raus ist.

## Ablauf

### 0. Erst analysieren, dann senden (harte Regel)

**Keine Mail geht raus, bevor die Analyse vollständig ist.** Reihenfolge vor dem Versand:

1. Sendung lesen (Absender, Empfänger, alle Kennungen) und **QR-Code/Barcode dekodieren** — darauf
   steht oft die Kampagnen-Quelle (`utm_source`), die man sonst in einer Nachfrage-Mail nachschiebt.
2. Impressum/Datenschutzseite des Absenders und des Markeninhabers prüfen; Verantwortlichen klären
   (Lettershop vs. Marke vs. Konzernmutter) und die Aufsichtsbehörde nach dessen Sitz bestimmen.
3. `references/kontakte.md` und die eigenen Systeme (Dokumentenarchiv) abgleichen: Gibt es eine
   Kundenbeziehung? Stimmt die Anschrift? Welche Nummern sind belegt?
4. Erst wenn 1–3 abgeschlossen sind, den Brief verfassen — **alle** Ergebnisse aus 1–3 gehören in
   diese eine Mail (Herkunft, Kennungen, Altdaten, Verantwortlichenfrage).

Ist ein Punkt danach noch offen und nicht selbst recherchierbar (fehlende Unterlagen, unklarer
Adressat, Entscheidung über Umfang), **frag den Nutzer** (`clarify`) und sende erst nach seiner
Antwort. Ziel ist, **gar nicht erst** in die Lage zu kommen, nachbessern zu müssen: ein Vorgang = eine
Mail pro Adressat (Datenschutz und Service parallel ist erlaubt, weil verschiedene Adressaten sind).

**Nachtrag ist die Ausnahme, nicht die Regel.** Erlaubt und dann sofort und ohne Rückfrage, wenn die
erste Mail sachlich falsch oder unvollständig war und das Rechtsfolgen hat: falscher Adressat,
falsche Kennung/Frist, nachträglich belegte Herkunft von Gewicht oder ein neuer Beweis (z. B. QR-Ziel,
aus dem die Datenquelle hervorgeht). Dann **eine** kurze Ergänzung mit Bezug auf die erste Mail —
nie eine Serie, nie eine bloße Höflichkeitskorrektur, nie eine Wiederholung des Widerspruchs.

### 1. Sendung auslesen
Foto/Scan mit `vision_analyze` lesen (nicht raten): **Absender mit vollständiger Anschrift**,
**Empfängeranschrift**, Datum, Anrede, und **alle Kennungen** — Kundennummer, Mitgliedsnummer,
Ablese-/Auftragsnummer, Dialogpost-Kennung auf dem Umschlag (`*632/17*1-2/165116*`), Beiblatt-Kennung
(`SM-AWB2.1.09/21`). Diese Kennungen gehören in den Betreff und in den Text; ohne sie landet das
Schreiben in der falschen Ablage und die Antwort kommt nicht.

**Die Absenderanschrift gegen das Impressum prüfen, nicht gegen das OCR.** OCR verliest
Straßennamen zuverlässig („Ziegelreutestraße" statt „Ziegelfeldstraße") — eine falsche Anschrift im
PDF ist ein Zustellfehler, den niemand bemerkt. Firmenname + „Impressum"/„Datenschutz" suchen und
die dortige Anschrift übernehmen; die Kennungen (Nummern) dagegen stehen nur auf dem Papier.

### 2. Adressabgleich — der stärkste Hebel
Vergleiche die Empfängeranschrift mit der aktuellen Anschrift des Nutzers. Steht dort eine **alte
Anschrift**, ist der Datenbestand nachweislich **unrichtig** (Art. 5 Abs. 1 lit. d DSGVO) und für
Werbung nicht mehr erforderlich. Diesen Punkt immer ausdrücklich als **Berichtigung nach Art. 16**
verlangen — bei Mitgliedschaften/Verträgen zusätzlich „auch für Beitragsrechnungen und Mahnungen“,
sonst laufen Rechnungen weiter an die alte Adresse.

### 3. Kundendaten aus den eigenen Systemen ziehen
Bevor der Brief rausgeht: Nummern und Vertragsdetails aus Paperless holen (Skill
`paperless-nas-operations`, Abschnitt API-Zugang) — Mitgliedsnummer, Beitragszeitraum, offene
Beträge, Dokumentdaten. Das macht den Brief konkret und belegt, dass der Nutzer Betroffener ist.
Wenn keine Kundenbeziehung besteht: keine Nummer erfinden, sondern **Auskunft nach Art. 14**
verlangen („aus welcher Quelle stammt die Adresse“).

### 4. Brief aufbauen — diese Bausteine gehören hinein
1. **Widerspruch Art. 21 Abs. 2 DSGVO** gegen Verarbeitung zu Direktwerbung, ausdrücklich für
   **alle Kanäle** (Post, E-Mail, Telefon, SMS, App-Postbox) und gegen **Profiling zu Werbezwecken**;
   dazu die Folge aus **Art. 21 Abs. 3** (keine Verarbeitung mehr für diese Zwecke).
2. **Weitergabe an Dritte** ausdrücklich einschließen: verbundene Unternehmen, Kooperationspartner,
   Lettershops und Adressveredler — Werbeadressen kommen fast immer über solche Ketten.
3. **Löschung Art. 17 Abs. 1 lit. a und d** für alle reinen Werbedaten, **mit Ausnahme** gesetzlicher
   Aufbewahrungspflichten für Vertrags-/Beitragsdaten. Pauschal „alles löschen“ wird sonst als
   undurchführbar abgelehnt.
4. **Berichtigung Art. 16** bei veralteter Anschrift (siehe Schritt 2).
5. **Auskunft Art. 15 + Herkunft Art. 14** (gespeicherte Daten, Rechtsgrundlage, Empfänger, Quelle).
6. **Frist 14 Tage** für eine Bestätigung in Textform, sonst Beschwerde bei der zuständigen
   Aufsichtsbehörde (zuständig nach Sitz des Verantwortlichen — Tabelle in `references/kontakte.md`).
7. **Klarstellung, was NICHT gekündigt wird**: „Die Mitgliedschaft/der Vertrag bleibt bestehen,
   widersprochen wird ausschließlich der Werbung.“ Ohne diesen Satz besteht das Risiko, dass ein
   Dienstleister den Widerspruch als Kündigung interpretiert.
8. **Bei gesetzlichen Krankenkassen** ausdrücklich schreiben, dass Werbung **keine gesetzliche
   Aufgabe nach §§ 284, 305 SGB V** ist und sich nicht auf den Versorgungsauftrag stützt — sonst wird
   der Widerspruch mit ebendiesem Auftrag abgewimmelt. Aufsicht: BfDI plus Bundesamt für Soziale
   Sicherung (siehe `references/kontakte.md`).

### 5. PDF erzeugen (eine Seite!)
HTML schreiben, dann `soffice --headless --convert-to pdf <datei>.html --outdir .`.
Damit es auf **eine** Seite passt: `font-size: 9.2pt`, `line-height: 1.34`,
`.sheet { padding: 15mm 19mm 13mm 21mm; }`, `p { margin-bottom: 2.4mm }`.
Rutscht nur die Signatur auf Seite 2, ist die Schrift zu groß — nachjustieren, nicht akzeptieren.
Mit `pdfinfo <datei>.pdf | grep Pages` prüfen. Vorlage: `templates/brief.html`.

### 6. Versand — zwei Adressaten, nicht einer
- **Datenschutzbeauftragter** (formaler Adressat, muss nach Art. 12 antworten)
- **Kundenservice / Mitgliederservice** (setzt die Werbesperre operativ)

Beides anschreiben, gleicher Text, gleiches PDF. Versand per Gmail-SMTP mit den Zugangsdaten aus
`~/.config/himalaya/config.toml` (`auth.raw` = Passwort, `backend.login` = Absender).
`EmailMessage` mit `set_content(<Klartext>)` und `add_attachment(..., subtype="pdf")`.

### 7. Verifikation (Pflicht)
Nach dem Versand per IMAP `"[Gmail]/Gesendet"` prüfen: `SEARCH TO <adresse>`, letzte Mail holen,
Datum + Anhang prüfen. Erst dann „ist raus“ sagen. Dem Nutzer das PDF als `MEDIA:`-Pfad mitschicken.

## Pitfalls

- **Nicht voreilig senden.** Ein sichtbarer QR-Code, ein fehlendes Impressum oder eine unklare
  Verantwortlichkeit ist kein Grund, sofort zu mailen und später nachzubessern — erst analysieren
  (Schritt 0), dann eine vollständige Mail. Bei Unsicherheit den Nutzer fragen.
- **Nachbessern nur im Härtefall.** Falscher Adressat, falsche Kennung oder ein neuer Beweis mit
  Rechtsfolge dürfen eine einzelne, kurze Ergänzung nach sich ziehen — aber das ist die Ausnahme und
  kein Ersatz für Schritt 0. Erst gar nicht in diese Lage kommen.
- **QR-Code auf dem Mailing auslesen — er nennt oft die Datenquelle.** Gedruckte Kampagnen tragen
  einen Kurzlink mit `utm_source`/`utm_campaign`; damit lässt sich die Kampagne einem Verlag oder
  Magazin zuordnen und die Herkunftsfrage nach Art. 14 wird konkret. Dekodieren ohne Systempakete:
  `python3 -m venv /tmp/qr && /tmp/qr/bin/pip install opencv-python-headless numpy` (ein
  `pip install --user` scheitert an PEP 668), dann `cv2.QRCodeDetector().detectAndDecodeMulti(img)`.
- **Treffer nicht nach Titel beurteilen.** Eine Paperless-Suche liefert auch Dokumente, in denen die
  Firma nur im Fließtext vorkommt (Kontoauszug, SCHUFA-Auskunft, Steuerbescheid) — und umgekehrt echte
  Briefe unter harmlosem Titel. Jeden Treffer über `content` prüfen und nach `<Firma> <Ort>` greppen,
  bevor du sagst, es gäbe keine Unterlagen. Ein vorschnelles „keine Dokumente“ ist ein falscher Befund,
  den der Nutzer in seinem eigenen Archiv sofort widerlegt (er sieht die Trefferzahl in der Suche).

- **Kennung taucht erst nach dem Versand auf → kurze Ergänzungsmail statt zweitem Volltext.** Findet
  sich die Kundennummer erst später (Paperless-Volltext, ältere Schreiben), reicht eine Mail mit
  Betreff „Ergänzung: Kundennummer … / Konto …", den Referenzketten und der Bitte um Zuordnung;
  dasselbe PDF noch einmal anhängen. Ein zweiter kompletter Widerspruch verwirrt die Zuordnung.
- **Nur an den Kundenservice schreiben reicht nicht.** Der Service setzt die Sperre, antwortet aber
  oft nur mit einer Standardmail; der Datenschutzbeauftragte ist der Adressat, der rechtlich zur
  Antwort verpflichtet ist. Immer beide.
- **Adressen nicht raten.** Die Kontaktdaten ändern sich (Fusionen, Marken). Vor dem Versand gegen die
  Datenschutzseite des Unternehmens prüfen; verifizierte Stände stehen in `references/kontakte.md`.
- **Veraltete Anschrift ist der beste Beweis.** Eine falsche Empfängeradresse nicht nur „nebenbei“
  erwähnen, sondern als eigenen Berichtigungsanspruch (Art. 16) führen — sie ist der Grund, warum die
  Daten für Werbung nicht mehr erforderlich sind.
- **„Löschung“ ohne Ausnahme formuliert** führt dazu, dass der Antrag mit Verweis auf
  Aufbewahrungspflichten insgesamt abgelehnt wird. Vertrags-/Beitragsdaten ausnehmen, Werbedaten
  gezielt benennen.
- **Kein Widerspruch gegen die Vertragsbeziehung.** Immer den Satz „Vertrag/Mitgliedschaft bleibt
  bestehen“ einbauen, sonst droht eine ungewollte Kündigung.
- **Sachlich bleiben statt drohen.** Frist und Aufsichtsbehörde nennen; keine Gerichtsdrohung. Das
  wirkt und bleibt verwendbar, falls tatsächlich Beschwerde eingelegt wird.

## Dateien
- `references/kontakte.md` — verifizierte Datenschutz-/Widerspruchsadressen (comdirect, Commerzbank,
  ADAC e.V., ADAC Südbaden, Volksbank Lahr, DAK-Gesundheit, LaVita, GEERS/Sonova, Deutsche Post Direkt)
  und die zuständigen Aufsichtsbehörden.
- `references/betroffene-daten.example.md` — Vorlage für die **lokalen** Kennungen (Mitglieds-,
  Versicherten-, Kundennummern, alte vs. aktuelle Anschrift, Stand der versandten Widersprüche).
  Als `betroffene-daten.md` daneben kopieren und ausfüllen; die Datei ist per `.gitignore` vom Repo
  ausgeschlossen und darf nie veröffentlicht werden.
- `templates/brief.html` — einseitige Briefform (DejaVu Serif, 9.2 pt) zum Kopieren und Anpassen.
