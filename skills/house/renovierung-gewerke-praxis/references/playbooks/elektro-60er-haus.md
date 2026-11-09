# Elektro komplett neu im 60er-Haus — Bestand, Recht, Ablauf, Auslegung, Kosten, Eigenleistung

> **Preisstand 09/2026.** Alle Preise sind Orientierungswerte inkl. MwSt. aus den genannten Quellen —
> regional verschieden, keine Angebote. Wer später damit rechnet, prüft sie neu.

**Zielgruppe:** Eigentümer eines Eigenheims, Baujahr ca. 1960–1969, die Elektrik vollständig erneuern (nicht nur eine Steckdose nachrüsten).
**Stand:** 09.11.2026. Jede Zahl trägt eine Quellennummer [Q#]; die Quellen stehen mit URL, Typ und Prüftiefe in §10. Normtexte (DIN/DIN VDE) sind kostenpflichtig — hier sind **Nummer, Titel und Ausgabe** über zitierende Fachquellen belegt, nicht der Normvolltext.

> **Die Grenze, die alles andere bestimmt:** Errichten, Erweitern und Ändern der Anlage hinter der Hausanschlusssicherung darf nur ein in ein Installateurverzeichnis eingetragenes Installationsunternehmen — auch im eigenen, selbst bewohnten Haus (NAV § 13 Abs. 2 Satz 4) [Q1]. Ausgenommen ist nur **Instandhaltung** (Satz 5), und auch die nicht im Abschnitt zwischen Hausanschlusssicherung und Messeinrichtung [Q1]. Dieses Playbook beschreibt deshalb Bestandsaufnahme, Planung, Vorbereitung, Kosten und Ablauf — nicht das Anklemmen.

> **Korrektur einer verbreiteten Fehlzuordnung:** Die Fachbetriebspflicht steht in **§ 13 NAV**, nicht in § 19. § 19 NAV regelt den **Betrieb** der Anlage und die **Mitteilungs-/Zustimmungspflicht** bei Erweiterungen und Ladeeinrichtungen [Q2]. Wer „§ 19“ zitiert, meint meist § 13 Abs. 2.

---

## 1. In 60 Sekunden

1. **Ein 60er-Haus hat selten eine „schlechte“ Anlage — es hat eine von 1965.** Typisch: Wechselstromzähler auf einer Zählertafel, ein bis drei Stromkreise für das ganze Haus, zweiadrige Leitungen, klassische Nullung, kein RCD [Q21][Q20].
2. **Der Bestandsschutz endet dort, wo du anfängst.** Für den unveränderten Teil gilt: keine Anpassungspflicht, solange der Betrieb sicher ist (so ausdrücklich die TAB 2026) [Q3]. Jede Erweiterung/Änderung wird dagegen nach den **aktuellen** Regeln ausgeführt [Q3][Q9].
3. **Zweiadern ohne PE ist das K.-o.-Kriterium.** An einen Stromkreis ohne Schutzleiter kommt keine neue Schuko-Dose; der Kreis muss neu [Q24][Q11].
4. **Ein RCD mit 500 mA ist kein Personenschutz.** Gefordert sind **30 mA** für Steckdosenstromkreise bis 32 A und für Beleuchtungskreise in Wohnungen [Q12][Q23].
5. **Der Zählerplatz ist der teuerste Einzelposten — und der, der am häufigsten „vergessen“ wird.** Zählertafeln nach DIN 43853 sind bei Erweiterungen nicht mehr zulässig [Q3]; ein zeitgemäßer Platz braucht SLS, Überspannungsschutz und Platz für Messsystem/Steuerung [Q5][Q22].
6. **Eigenleistung endet vor der Klemme:** Schlitze, Dosen, Leerrohre, Kabel nach Vorgabe einziehen, Fotos — alles legal. Anklemmen, messen, in Betrieb nehmen: nein [Q1][Q7].
7. **Kalkuliere 86–127 €/m² für die Komplettsanierung im Altbau** — bei 120 m² sind das rund 10.300–15.200 €, bei 150 m² 12.900–19.050 € [Q25].

---

## 2. Was in einem Haus Baujahr 1960–1969 typisch drin ist

Diese Tabelle ist eine **Befundliste für die Sichtprüfung**, keine Ferndiagnose. Der Zählerkasten wird **nicht geöffnet** — Sichtprüfung genügt für die erste Einschätzung, und ELEKTRO+ schreibt das ausdrücklich [Q20].

### 2.1 Die zehn Befunde

| # | Befund | Erkennungsmerkmal (Laie) | Risiko | Foto-Hinweis |
|---|---|---|---|---|
| 1 | **Klassische Nullung** (TN-C, PEN statt PE+N) | In der Dose sind PE und N **gebrückt**; nur zwei Adern; Schuko-Dose mit Brücke zwischen Schutzkontakt und N | Bricht der PEN, liegen **230 V** am Gehäuse [Q11]; ein RCD löst bei einem Körperschluss nicht aus, weil der Fehlerstrom über den PEN zurückfließt und keine Differenz entsteht | Dose von vorn, Klemmen sichtbar, Maßband daneben |
| 2 | **Zweiadrige Leitung ohne Schutzleiter** | Nur zwei Adern (oft schwarz/blau oder schwarz/grau), kein grün-gelber Leiter; oft **Stegleitung** direkt im Putz | Geräte der Schutzklasse I (Metallgehäuse) sind im Fehlerfall unter Spannung; keine neue Schuko-Dose zulässig [Q24] | Aderenden mit Farbe + Querschnitt, Nahaufnahme |
| 3 | **Aluminiumleiter** | Silbrige, weiche Adern; kein Kupferglanz an der Schnittfläche; Klemmen mit Fettresten | Kaltfluss und Oxidation an Klemmstellen → Übergangswiderstand, Erwärmung, Brand [Q30]; Cu/Al-Mischverbindungen ohne Spezialklemme unzulässig [Q24] | Aderquerschnitt + Klemme, Licht von der Seite |
| 4 | **Einzeladern im Stahlpanzer-/Blechrohr** (Bergmannrohr) | Graues, steifes Blechrohr in der Wand, runde Blechdosen, oft kein PE | Rohr ist mechanischer Schutz, **kein** Schutzleiter; Dosen korrodiert, Adernisolierung versprödet [Q30] | Rohrende, Doseninneres, Rohrdurchmesser |
| 5 | **Zu wenige Stromkreise** | Ein Zähler, wenige Schraubsicherungen; „eine Sicherung für das ganze Geschoss“ | Überlast durch moderne Verbraucher; ein Fehler schaltet das halbe Haus ab [Q21][Q23] | Zählertafel komplett, Sicherungsanzahl zählen |
| 6 | **Kein RCD / FI** | Kein Gerät mit **Testtaste** im Verteiler; oder Testtaste vorhanden, aber Gerät mit **500 mA** statt 30 mA | Kein Zusatzschutz bei Körperkontakt; 500 mA liegt weit über der Gefährdungsschwelle (50 mA) [Q23][Q20] | Verteilerfront, Gerätebeschriftung lesen |
| 7 | **Zählertafel nach DIN 43853 ohne SLS** | Zähler auf Holz-/Bakelit-Tafel, Schraubsicherungen (deutet auf Installation **vor 1979**), kein selektiver Hauptleitungsschutzschalter | Bei Erweiterung **nicht mehr zulässig** [Q3]; kein laienbedienbares Trennen, kein Reserveschutz | Gesamtansicht Tafel + Sicherungsart |
| 8 | **Kein Überspannungsschutz** | Kein SPD-Gerät im Zähler-/Verteilerfeld, kein Typ-2-Ableiter | Schäden an Elektronik/Heizung bei Gewitter; bei Neuanlagen seit **14.12.2018** gefordert [Q22] | Zählerfeld, NAR/AAR-Bereich |
| 9 | **Kein Hauptpotentialausgleich / PEN nicht aufgetrennt** | Keine Haupterdungsschiene auffindbar; Wasser-/Gasleitung nicht angeschlossen; Antennenkabel ohne Erdung | PEN darf für Antennen-, PV-, Blitzschutz- und Kommunikationsanlagen **nicht** als Erdungsleiter dienen [Q3]; Berührungsspannung auf Rohrleitungen | Haupterdungsschiene, Anschlüsse, Querschnitte |
| 10 | **Nachgerüstete Schuko-Dose am alten Kreis** | Neue Dose, alte Leitung; Dose ohne PE-Anschluss, Gehäuse aus Kunststoff | Der häufigste „Pfusch im Bestand“: die Dose sieht neu aus, der Schutz fehlt [Q24] | Dose abnehmen lassen, Adernzahl dokumentieren |

### 2.2 Was das Baujahr konkret bedeutet

- **Nullung:** Die klassische Nullung ist in Deutschland seit **1. Mai 1973** für Neuanlagen verboten (Übergangsfrist bis 31.03.1974). PEN-Verbindungen sind nur noch mit mindestens **10 mm² Kupfer** bzw. **16 mm² Aluminium** zulässig [Q11]. Ein 1965 errichtetes Haus ist damit **vor** dieser Zäsur — die Brücke in der Dose ist der Normalfall, nicht der Pfusch.
- **Aluminium:** Die Verwendung war vor allem in der DDR verbreitet; dort führten die Zwischenschichten an Klemmstellen und die Bruchgefahr zu Problemen, und für Alu geeignete Klemmen waren zwingend [Q30]. In Westdeutschland ist Alu in Wohngebäuden seltener, aber vorhanden — der Blick auf die Ader entscheidet, nicht das Baujahr [Q24].
- **Leitungsführung:** Einzeladern im Blechrohr halten sich bis in die **1950er Jahre**, danach PVC-ummantelte Kupferkabel und Stegleitung im Putz; Abzweigdosen blieben oft Aufputz aus Bakelit [Q30].
- **Alte Aderfarben lesen:** in Installationen der 1960er/70er ist **grau der Neutralleiter**, **rot der Schutzleiter** und **schwarz die Phase**. Grau war und ist also N — der Unterschied steckt beim **Schutzleiter**: früher **rot**, heute **grün-gelb**. Wer nach heutiger Farblogik umklemmt, hält den roten Leiter für Phase und vertauscht damit N und PE.
- **Zählertafel:** Ein Zähler auf Holz- oder schwarzer Bakelit-Tafel bedeutet laut ELEKTRO+: Anlage „mindestens 50 Jahre alt“ [Q20]. Bei Baujahr 1960–69 ist das der Regelfall — und damit der Punkt, an dem die TAB 2026 hart wird [Q3].

### 2.3 Die Sichtprüfung in 20 Minuten (ohne Werkzeug)

1. **Zählertafel fotografieren** (Gesamt + Sicherungsart). Nichts abschrauben, nichts berühren [Q20].
2. **Testtaste** am FI drücken, falls vorhanden — sie muss auslösen; empfohlen **zweimal im Jahr** [Q20].
3. **Eine Steckdose je Geschoss** abschrauben lassen (Elektrofachkraft) und fotografieren: Adernzahl, Farben, Brücke.
4. **Verteilerbeschriftung** prüfen: beschriftet? Stromlaufplan vorhanden? [Q20]
5. **Haupterdungsschiene** suchen (Keller, beim Hausanschlusskasten): vorhanden, angeschlossen, Querschnitt?
6. **Rauchmelder** zählen: Schlafräume und Rettungswege (siehe §3.6) [Q8].

**Messen darfst du nicht.** Isolationswiderstand, Schleifenimpedanz, RCD-Auslösezeit und Drehfeld sind Prüfaufgaben der Elektrofachkraft; die Erstprüfung nach DIN VDE 0100-600 darf „ausschließlich eine befähigte Person (Elektrofachkraft)“ durchführen [Q13].

**Wenn du überhaupt prüfst, dann zweipolig mit Lastzuschaltung** (z. B. **Duspol**): Spannung ist erst bestätigt, wenn die Last zugeschaltet ist — ein Phasenprüfer zeigt auch Induktion und damit „Spannung“, wo keine ist.

---

## 3. Recht und Pflicht

### 3.1 Wer darf was — NAV § 13

| Tätigkeit | Erlaubt? | Beleg |
|---|---|---|
| Schlitze stemmen/fräsen, Dosenlöcher bohren | ja (Bauleistung, keine Elektroarbeit) | [Q1][Q14] |
| Leerrohre, Kabelkanäle, Dosen setzen | ja | [Q1][Q24] |
| Leitungen **nach Vorgabe** einziehen (Weg, Querschnitt, Stromkreis vom Betrieb festgelegt) | ja | [Q1][Q24] |
| Adern anklemmen, Verteiler bestücken, absichern | **nein** | [Q1] |
| Messen, Erstprüfung, Inbetriebnahme | **nein** | [Q1][Q13] |
| Zählerantrag, Anmeldung beim Netzbetreiber | **nein** (macht der eingetragene Betrieb) | [Q1][Q3] |
| Instandhaltung (z. B. Schalter tauschen) | ja, aber **nicht** zwischen HAK und Messeinrichtung — und praktisch nur durch jemanden, der die Schutzmaßnahme beurteilen kann | [Q1][Q7] |

**Die Ausnahme ist eng:** § 13 Abs. 2 Satz 5 NAV nimmt nur **Instandhaltungsarbeiten** aus, und ausdrücklich **nicht** den Abschnitt zwischen Hausanschlusssicherung und Messeinrichtung einschließlich Messeinrichtung [Q1]. „Ich darf in meinem Haus alles reparieren“ ist damit falsch, sobald der Zählerplatz betroffen ist.

**Zwei Nebenregeln, die gern übersehen werden:**
- **Spannungsfall HAK → Zähler:** höchstens **0,5 %**, bezogen auf die Nennstromstärke der vorgeschalteten Sicherung (NAV § 13 Abs. 4) [Q1]. Ein Forumsteilnehmer hält dem entgegen, es seien „0,5 %, 1,0 % oder 1,5 %“ [Q28] — der Verordnungstext ist eindeutig; die abweichenden Werte stammen aus älteren TAB-Fassungen. Widerspruch dokumentiert, Gesetzestext gilt.
- **Mitteilungspflicht:** Erweiterungen und Änderungen sind dem Netzbetreiber mitzuteilen, soweit sich die vorzuhaltende Leistung erhöht; Ladeeinrichtungen sind vor Inbetriebnahme mitzuteilen, und über **12 kVA** Summen-Bemessungsleistung brauchen sie die vorherige Zustimmung (NAV § 19 Abs. 2) [Q2].

### 3.2 Bestandsschutz — was er trägt und was nicht

Der Begriff steht **nicht** in der NAV und nicht in DIN VDE 0100-200; er ist baurechtlich geprägt: Eine Anlage, die nach den Regeln ihrer Errichtungszeit ordnungsgemäß errichtet wurde, darf in diesem Zustand weiterbetrieben werden [Q11].

**Vier Voraussetzungen, alle gleichzeitig** (ELEKTRO+):
1. Die Anlage entsprach den zum Errichtungszeitpunkt gültigen DIN-VDE-Normen **und entspricht ihnen noch**.
2. Folgenormen oder andere Regelwerke haben **keine** Anpassung verlangt.
3. Die Anlage wird unter den Bedingungen betrieben, für die sie ausgelegt war.
4. Es bestehen **keine Mängel**, die Leib, Leben oder Sachen gefährden. [Q9]

Zusätzlich nennt ELEKTRO+ die Lebensdauer: Für eine Anlage am Ende ihrer Betriebszeit („üblicherweise **40 Jahre**“) kann Bestandsschutz grundsätzlich nicht mehr geltend gemacht werden [Q9].

**Was der Bestandsschutz praktisch bedeutet:**
- Der **unveränderte** Teil darf bleiben — die TAB 2026 sagt das ausdrücklich: „Für den bestehenden Teil der Kundenanlage (der nicht verändert oder erweitert worden ist) gibt es seitens der TAB keine Anpassungspflicht, sofern die sichere und störungsfreie Stromversorgung gewährleistet ist.“ [Q3]
- **Erweiterung** (ein Stromkreis oder auch nur eine Steckdose kommt hinzu) und **Änderung** (z. B. Steckdose versetzen) müssen nach den **aktuellen** Regeln ausgeführt werden; der bestehende Teil kann unverändert bleiben, wenn die vier Voraussetzungen erfüllt sind [Q9][Q3].
- **Aber:** Die klassische Nullung **hat** nach Auffassung der Fachliteratur Bestandsschutz, und eine Anpassungsforderung an die aktuellen Normen wird „aus jetziger Sicht … nicht zu erwarten“ sein [Q10]. Das ist der Widerspruch, den man aushalten muss: Der Kreis mit Brücke darf bleiben — eine **neue** Schuko-Dose daran ist trotzdem unzulässig, weil die Erweiterung aktuelle Regeln auslöst [Q9][Q24].

**Die Praxisformel der Elektriker:** „Wenn du nichts an der Elektrotechnik ändern würdest, könntest du es noch eine Zeit lang lassen — aber wenn du jetzt umbaust, weitere Steckdosen erweiterst, musst du das Ganze neu machen.“ [Q23, 00:01:47]

### 3.3 TAB des Netzbetreibers — was 2026 neu ist

Die **TAB Niederspannung** (BDEW-Bundesmusterwortlaut, Version 1.0, Stand **30.07.2026**) gilt für Anlagen, die neu angeschlossen, erweitert oder verändert werden; sie ist Bestandteil der Netzanschlussverträge [Q3]. Jeder Netzbetreiber veröffentlicht seine Fassung mit Ergänzungen.

| Regel | Inhalt | Beleg |
|---|---|---|
| Geltungsbereich | neu / erweitert / verändert; **keine** Anpassungspflicht für den unveränderten Teil | [Q3] § 1 (3) |
| Erweiterung/Änderung | „nach VDE-AR-N 4100 auszuführen“; Errichter prüft, ob der Zählerplatz angepasst werden muss | [Q3] § 4.4 (1), (3) |
| Reserveplätze | nutzbar nur mit Trennvorrichtung im NAR (oder gleichwertig) **und** AAR ≥ 150 mm mit Hauptleitungsabzweigklemme, **nicht** als Stromkreisverteiler | [Q3] § 4.4 (6) |
| **Zählertafeln** | „(Reserve-) Zählertafeln nach DIN 43853 sind bei Erweiterungen **nicht zulässig**.“ | [Q3] § 4.4 (7) |
| Erdung | PEN/Neutralleiter des Verteilnetzes darf **nicht** als Erdungsleiter für Erzeugungs-, Antennen-, Blitzschutz- und Kommunikationsanlagen dienen | [Q3] § 11 (2) |
| Überspannungsschutz | Einbau nach DIN VDE 0100-443; Auswahl/Einsatz nach VDE-AR-N 4100 Abschnitt 11.2 | [Q3] § 11 (3) |
| Anmeldung/Inbetriebsetzung | erfolgt über das Verfahren des Netzbetreibers, durch den Errichter | [Q3] § 4.1, § 4.2 |

**Der Zählerplatz im Bestand ist kein Automatismus.** Der VDE-FNN-Hinweis „Zählerplätze in Bestandsanlagen“ beschreibt, wann ein vorhandener Platz weiterverwendet werden darf und wann nicht: Grundsätzlich gilt bei einer Erweiterung VDE-AR-N 4100 Abschnitt 4.4; ist eine Ertüchtigung des bestehenden Platzes nicht möglich, ist ein **neuer** Zählerplatz nach aktueller Anwendungsregel zu errichten [Q4]. Ein AAR von 150 mm Höhe darf nur die Zuleitung zum nachfolgenden Stromkreisverteiler aufnehmen; fehlt bei Dreipunkt-Zählerplätzen ohne Zählersteckklemme eine laienbedienbare Trennvorrichtung, ist sie nachzurüsten [Q4].

### 3.4 VDE-AR-N 4100:2026-04 — die Maße, die den Zählerplatz bestimmen

Die Anwendungsregel ist in der Ausgabe **2026-04** erschienen und gilt seit **06.03.2026** [Q5][Q6]. Für neu zu errichtende Zähleranlagen bis 63 A:

| Element | Maß / Anforderung | Beleg |
|---|---|---|
| Zählerfeld (ZF) | **450 mm** hoch, davon 300 mm für die Messeinrichtung (eHZ) | [Q5] |
| Raum für Zusatzanwendungen (RfZ) | **150 mm** hoch, 12 TE je Zählerfeld; **nicht** als Stromkreisverteiler nutzen | [Q5] |
| Anlagenseitiger Anschlussraum (AAR) | **300 mm** hoch; darf **nicht** Stromkreisverteiler sein | [Q5] |
| Trennvorrichtung | **SLS** (selektiver Hauptleitungsschutzschalter), laienbedienbar, sperr- und plombierbar, im NAR | [Q5] |
| Hauptschalter | bei **3-Punkt-Zählern** im AAR jetzt Pflicht | [Q5] |
| Überspannungsschutz | SPD **Typ 1 oder Typ 2** im NAR/AAR | [Q5] |
| APZ | im Kommunikations- oder Verteilerfeld des Zählerschranks; außerhalb nicht gestattet | [Q5] |
| Hauptleitung | Einführung von unten/seitlich/hinten, **nicht von oben**; 5-poliges Sammelschienensystem | [Q5] |

**Erdung im Bestand:** Für Neubauten ist eine Erdungsanlage nach **DIN 18014** verpflichtend. Für Bestandsbauten gilt bei Nachrüstung: PEN oder Neutralleiter dürfen nicht mehr als Erdungsleiter verwendet werden — betroffen sind u. a. Blitzschutz, Erzeugungsanlagen, Antennenanlagen und Breitbandkabelnetze [Q6]. Wer also PV, Wallbox oder eine neue Antenne plant, löst dieses Thema aus, auch wenn die übrige Anlage bleibt.

**Was das für ein 60er-Haus heißt:** Eine Zählertafel nach DIN 43853 erfüllt keines dieser Merkmale. Sie ist bei Erweiterungen unzulässig [Q3] — der Zählerschrank ist damit kein „Nice-to-have“, sondern der Punkt, an dem die Sanierung faktisch beginnt.

### 3.5 DGUV Vorschrift 3 — Adressat ist der Unternehmer

- **Elektrofachkraft** ist, wer aufgrund fachlicher Ausbildung, Kenntnisse und Erfahrungen die Arbeiten beurteilen und Gefahren erkennen kann (§ 2 Abs. 3) [Q7].
- Elektrische Anlagen sind „nur von einer Elektrofachkraft oder unter Leitung und Aufsicht einer Elektrofachkraft“ zu errichten, zu ändern und instand zu halten (§ 3 Abs. 1) [Q7].
- Geprüft wird **vor der ersten Inbetriebnahme** und nach Änderung/Instandsetzung vor Wiederinbetriebnahme, außerdem in bestimmten Zeitabständen (§ 5 Abs. 1) [Q7].
- Bei festgestelltem Mangel: unverzüglich beheben, bei dringender Gefahr die Anlage im mangelhaften Zustand **nicht verwenden** (§ 3 Abs. 2) [Q7].

**Einordnung:** Die DGUV Vorschrift 3 bindet **Unternehmer**, nicht private Eigentümer. Für ein selbst genutztes Einfamilienhaus gibt es damit keine gesetzliche Prüfpflicht — aber auch keine Befreiung von den anerkannten Regeln der Technik. Praktische Folge: Wer vermietet oder gewerblich nutzt, ist näher dran an der Prüfpflicht; wer selbst wohnt, braucht das Protokoll trotzdem für Versicherung, Verkauf und Gewährleistung.

### 3.6 Rauchmelderpflicht in Baden-Württemberg

§ 15 Abs. 9 LBO BW (Fassung vom 16.03.2026, gültig ab 28.02.2026): „Aufenthaltsräume, in denen bestimmungsgemäß Personen schlafen, sowie Rettungswege von solchen Aufenthaltsräumen in derselben Nutzungseinheit sind jeweils mit mindestens einem Rauchwarnmelder auszustatten. … Die Sicherstellung der Betriebsbereitschaft obliegt den unmittelbaren Besitzern.“ [Q8]

Für die Elektrosanierung heißt das: Rauchmelder entweder **vernetzt** mit 230-V-Versorgung und Batterie-Reserve oder funkvernetzt; in jedem Fall in Schlaf- und Kinderzimmern sowie in Fluren, die Rettungswege sind. Die Pflicht trifft den **Besitzer**, nicht den Elektriker — sie gehört aber in dieselbe Bauphase, weil Deckendosen und Leitungen jetzt liegen.

### 3.7 Weitere Pflichten, die im selben Zug anfallen

- **Gewährleistung:** 5 Jahre ab Abnahme bei Bauwerken (BGB § 634a Abs. 1 Nr. 2) [Q32] — gilt auch für die Elektroinstallation als Bauwerksteil. Ohne Abnahmeprotokoll beginnt die Frist nicht sauber zu laufen.
- **Steuer:** 20 % der **Arbeitskosten** (max. **1.200 €/Jahr**) für Renovierungs-, Erhaltungs- und Modernisierungsmaßnahmen nach § 35a Abs. 3 EStG; Voraussetzung sind Rechnung und Überweisung, keine Barzahlung [Q31]. Material ist **nicht** förderfähig.
- **Steuerbare Verbraucher:** Wer Wallbox oder Wärmepumpe einbaut, landet bei § 14a EnWG und braucht die Steuerbarkeit im Zählerplatz; DEHN nennt die Schwelle **> 4,2 kW** Summenleistung [Q6]. Die Anmeldung macht der eingetragene Betrieb [Q3].
- **Vermietung/Nutzungsänderung:** Bei Änderung der Nutzung (z. B. Einliegerwohnung, Büro) prüft der Errichter, ob der Zählerplatz angepasst werden muss [Q3].

---

## 4. Ablauf der Komplettsanierung — mit Tagen

Realistisch für ein EFH 120 m², ein Geschoss + Keller, ohne Rohbauänderungen. „Tag“ = Arbeitstag einer eingespielten 2-Mann-Kolonne; Eigenleistung verschiebt die Dauer nach hinten, nicht nach vorn.

| Tag | Schritt | Wer | Ergebnis / Nachweis |
|---|---|---|---|
| **0** | Baujahr sichern, Bestandsaufnahme, Fotos je Raum | Eigentümer | Raumliste, Fotos, Zählerbild [Q20] |
| **1** | Messungen: Isolationswiderstand, Schutzleiterdurchgang, Schleifenimpedanz, RCD-Auslösezeit, Drehfeld | Elektrofachkraft | Messprotokoll als **Vorher**-Bild [Q13] |
| **1–2** | Planung: Stromkreise, Dosen, Leerrohre, Verteilerplatz, Zählerplatz, Netzwerk | Betrieb + Eigentümer | Stromkreisverzeichnis, Doseplan je Raum, Aufmaß [Q18][Q19] |
| **2** | Anmeldung beim Netzbetreiber / Zählerantrag | eingetragener Betrieb | Anmeldebestätigung [Q3] |
| **3–4** | Rückbau: alte Dosen, Leitungen, Zählertafel; Schlitze und Dosenlöcher nach Vorgabe | Eigentümer möglich | offene Wände dokumentiert [Q14] |
| **4–5** | Leerrohre, Kabelkanäle, Hohlwanddosen, Durchbrüche (nicht tragend) | Eigentümer möglich | Fotos mit Maßband je Wand |
| **5–6** | Leitungen einziehen (nach Vorgabe), Kennzeichnung, Aderreserve | Eigentümer/Betrieb | Leitungsplan mit Nummern |
| **6–7** | Neuer Zählerschrank, SLS, Überspannungsschutz, Hauptleitungsabzweigklemmen | Betrieb | Zählerplatz nach VDE-AR-N 4100 [Q5] |
| **7** | Unterverteilung je Geschoss setzen, RCD-/RCBO-Gruppen, Reservefelder | Betrieb | Verteilerbeschriftung [Q18] |
| **7–8** | Hauptpotentialausgleich, Erdung, Anschluss Wasser/Gas/Heizung/Antenne | Betrieb | Messprotokoll Erdungswiderstand [Q3] |
| **8** | Rohinstallation abnehmen, Putz/Fliesen/Estrich kann folgen | Betrieb + Eigentümer | Freigabe schriftlich |
| **9** | Endmontage: Schalter, Steckdosen, Rauchmelder, Außensteckdosen | Betrieb | Stückliste abgehakt |
| **10** | Erstprüfung DIN VDE 0100-600, Inbetriebsetzung, Zählerwechsel | Betrieb + Netzbetreiber | Prüfprotokoll, Stromlaufplan, Übergabe [Q13] |
| **11** | Abnahme, Mängelliste, Restzahlung | beide | unterschriebenes Protokoll [Q32] |

**Die Prüfung ist kein Schlussritual, sondern eine Messreihe.** DIN VDE 0100-600:2017-06 verlangt **Besichtigen, Erproben, Messen**, mit **16 Sichtprüfungsanforderungen** (Abschnitt 6.4.2.3) und zehn Messschritten in fester Reihenfolge: Durchgängigkeit, Isolationswiderstand der Anlage, Isolation SELV/PELV, isolierende Fußböden/Wände, Spannungspolarität, Schutz durch automatische Abschaltung, RCD-Prüfung im TN-Netz, Phasenfolge, Funktionsprüfungen, Spannungsfall [Q13]. Mindestwert Isolation: **1 MΩ** bei 500 V Messgleichspannung für Anlagen ≤ 500 V [Q13].

**Terminlogik, die Geld spart:**
- **Rohinstallation vor Putz und Estrich.** Kabel nach dem Putz bedeutet stemmen, drecken, zweimal zahlen [Q21].
- **Zählerwechsel braucht einen Termin des Netzbetreibers/Messstellenbetreibers** — vorher Kühlgeräte leeren und das Zeitfenster schriftlich bestätigen lassen [Q3].
- **Fotos, bevor die Wand zu ist.** Jede Wand offen, mit Maßband im Bild, je Raum sortiert. Das ist das billigste und wertvollste Dokument des Projekts [Q24].

---

## 5. Auslegung

### 5.1 Stromkreise — Mindestausstattung und Realität

DIN 18015-2:2021-10 regelt die Mindestausstattung; die folgende Zuordnung ist der Auszug aus der HEA/RAL-Planungshilfe 2023, nicht der Normtext selbst [Q17].

| Wohnfläche | Allgemeine Stromkreise (Mindestausstattung) |
|---|---|
| bis 50 m² | 3 |
| über 50–75 m² | 4 |
| über 75–100 m² | 5 |
| über 100–125 m² | 6 |
| darüber | 7 |

Quelle: [Q17]; die Norm selbst ist kostenpflichtig, DIN 18015-2:2021-10 [Q17][Q18]. **Zusätzlich** bekommt jeder Großverbraucher einen eigenen Stromkreis: Herd, Geschirrspüler, Waschmaschine, Trockner, Warmwassergerät, Heizung, Rollläden, Sauna [Q18].

**Realistische Planung für 120 m² (Vorschlag, keine Normzahl):** 12–16 Stromkreise — Küche (2–3), Herd (1), GS/WaMa/Trockner (2), Bad (1–2), Wohnen (2), Schlafen/Kind (2–3), Flur/Licht (1–2), Außen/Garage (1–2), Heizung (1), Reserve Wallbox/PV (2). Die Portale rechnen für ein EFH mit **12–14** Stromkreisen [Q25] — die DIN-Mindestzahl von 6 ist die Untergrenze, nicht das Ziel.

### 5.2 RCD-Aufteilung: Gruppen statt „ein FI für alles“

- **Pflicht:** RCD mit **I∆n ≤ 30 mA** für Steckdosenstromkreise bis **32 A**, die Laien zugänglich sind; Beleuchtungsstromkreise in Wohnungen zusätzlich nach Abschnitt 411.3.4. Die Ausgabe 2018-10 hat den Anwendungsbereich von 20 A auf 32 A erweitert [Q12].
- **Aufteilung:** DIN 18015-2 verlangt, „die Zuordnung von Fehlerstrom-Schutzeinrichtungen (RCDs) zu den Stromkreisen … so vorzunehmen, dass das Abschalten eines Fehlerstrom-Schutzschalters nicht zum Ausfall aller Stromkreise führt“ (zitiert nach [Q12]). DIN VDE 0100-530:2018-06 empfiehlt zusätzlich die Aufteilung auf mehrere FI-Schutzschalter [Q12].
- **RCBO (FI/LS) je Kreis** ist die sauberste Lösung: Personen-, Leitungs- und Brandschutz in einem Gerät, allpolige Abschaltung, und im Fehlerfall fällt nur dieser Kreis [Q12].
- **Kritische Kreise separat:** Kühl-/Gefriergeräte, Router, Heizungssteuerung, Alarmanlage. Das ist Praxisempfehlung, keine Normzahl [Q12].
- **Typ:** Typ A ist der Standard für Hausinstallationen. DIN VDE 0100-530:2018-06 führt erstmals den **Typ F** für bestimmte Anwendungsfälle ein und verlangt Brandschutzschalter für definierte Fälle [Q12]. Sonderanwendungen (Ladestationen, Frequenzumrichter, PV) haben eigene Anforderungen an den RCD-Typ — Auswahl durch den Betrieb.
- **Kein Ersatz für Leitungsschutz:** Der RCD schützt Personen, nicht die Leitung; Überlast- und Kurzschlussschutz bleiben eigene Aufgabe (DIN VDE 0100-430) [Q15][Q16].

**Was das Messgerät zeigen muss:** Die Auslösefenster stammen aus der Produktnorm, nicht aus der Errichtungsnorm — Sinus **0,5–1 × I∆N**, pulsierender Gleichstrom **0,35–1,4 × I∆N**, glatter Gleichstrom **0,5–2 × I∆N**. Ein RCD Typ A wird mit pulsierendem Gleichstrom geprüft (größte Bandbreite); Prüfgeräte erhöhen in Stufen **< 1/30 I∆N** (DIN EN 61557), manche mit **6 mA DC**-Offset. Nach **DIN VDE 0100-600:2017-06, 6.4.3.7.1** ist die Schutzmaßnahme nachgewiesen, wenn die Abschaltung bei **≤ I∆N** erfolgt — gemessene Werte über 30 mA sind deshalb erklärbar, aber im Protokoll mit Prüfstromart zu dokumentieren ([Elektropraktiker, „Prüfung von RCDs“](https://www.elektropraktiker.de/nachrichten/nachricht/pruefung-von-rcds?p=all), 28.01.2020, geprüft 09.11.2026, HTTP 200).

### 5.3 Querschnitte, Absicherung, Längen

| Querschnitt | Strombelastbarkeit NYM-J, 2 belastete Adern | Typische Absicherung | Einsatz |
|---|---|---|---|
| **1,5 mm²** | 16,5 A (A1/A2) · 18,5 A (B1) · 17,5 A (B2) · 21 A (C) | **B16** | Licht, Steckdosen, Standardkreis [Q15] |
| **2,5 mm²** | höher, verlegeartabhängig | 16 A, teils 20 A | Küche, Großverbraucher, lange Wege, Zuleitung UV [Q15] |
| **4 mm² / 6 mm²** | projektiert | nach Herstellerangabe | Herd, Durchlauferhitzer, Wallbox, Wärmepumpe — Auslegung durch den Betrieb |

**Merksätze:**
- **1,5 mm² ist für einen B16-Steckdosenkreis ausreichend.** Ein Mindestquerschnitt von 2,5 mm² für Steckdosen ist in keiner Norm festgelegt; Mindestquerschnitt für feste Verlegung von Laststromkreisen ist **1,5 mm²** (DIN VDE 0100-520, Abschnitt 524, Tabelle 52.2) [Q15].
- **Absicherung folgt der Leitung, nicht dem Verbraucher.** 1,5 mm² trägt bei A1/A2 16,5 A — ein B16 passt, ein B20 nicht [Q15].
- **Länge begrenzt den Querschnitt.** Bei 3 % Spannungsfall sind mit 3×1,5 mm² und 16 A etwa **18 m** möglich; darüber 2,5 mm² oder kürzere Wege [Q15].
- **Durchlauferhitzer ist kein Steckdosenkreis.** Er braucht einen eigenen Drehstromkreis; Querschnitt und Absicherung folgen der Geräteanleitung und der Verlegeart. In Foren werden für 21 kW sowohl 5×4 mm² mit 32 A als auch 5×6 mm² mit 32 A vertreten [Q28] — der Widerspruch ist ungeklärt, deshalb entscheidet die Herstellerangabe, nicht das Forum.

### 5.4 Spannungsfall — vier Werte, die zusammengehören

| Abschnitt | Grenzwert | Quelle |
|---|---|---|
| HAK → Zähler | **0,5 %** (Nennstromstärke der vorgeschalteten Sicherung) | NAV § 13 Abs. 4 [Q1] |
| Zähler → letzter Verbraucher | **3 %** | DIN 18015-1 (zitiert nach [Q34]) |
| Netzanschluss → Verbraucher (gesamt) | **4 %** | DIN VDE 0100-520:2013-06, Abschnitt 525.1 / Anhang G [Q33][Q15] |
| Beleuchtung / andere Verbraucher (IEC-Tabelle G.52.1) | **3 % / 5 %** | DIN VDE 0100-520 Anhang G [Q33] |

Der Unterschied ist keine Sprachverwirrung: Die 3 %/5 % sind die internationale Tabelle (Anhang G, informativ), die 4 % die Empfehlung für die Gesamtanlage, die 3 % die deutsche Planungsvorgabe hinter dem Zähler. Wer 3 % einhält, liegt in allen Fassungen richtig [Q15][Q33][Q34].

### 5.5 Verlegeart, Häufung, Dämmung

Die Strombelastbarkeit hängt an der **Verlegeart** (A1, A2, B1, B2, C …) und den Umgebungsbedingungen: Bei 1,5 mm² liegen zwischen dem günstigsten und dem ungünstigsten Fall der geprüften Tabelle **4,5 A** (16,5 A bis 21 A) — dieselbe Leitung, dieselbe Sicherung, anderer Weg [Q15]. Wer Leitungen in gedämmte Wände, abgehängte Decken oder in Rohre mit anderen Leitungen legt, verändert die Verlegeart und muss sie neu bewerten lassen (DIN VDE 0298-4 in Verbindung mit DIN VDE 0100-520) [Q15][Q33].

**Praktische Konsequenz:** Der Leitungsweg wird **vor** dem Einziehen festgelegt, nicht beim Ziehen. Wenn die Dämmung später kommt, ist die Bewertung zu spät.

### 5.6 Installationszonen (DIN 18015-3:2016-09)

| Zone | Lage | Breite | Vorzug |
|---|---|---|---|
| waagerecht unten | 15–45 cm über Fertigfußboden | 30 cm | 30 cm [Q19] |
| waagerecht Mitte (Küche/Arbeitsraum) | 100–130 cm über FF | 30 cm | 115 cm [Q19] |
| waagerecht oben | 15–45 cm unter der Decke | 30 cm | 30 cm [Q19] |
| senkrecht | 10–30 cm neben Wandkante/Ecke, Tür, Fenster | **20 cm** | 15 cm [Q19] |
| Schalterhöhe | — | — | 105 cm (oberste Bedienstelle) [Q19] |
| Decke/Boden | 30 cm breite Zone, 20 cm Abstand zur Wand | — | — [Q19] |

Die Norm gilt für **Unterputz**; Aufputz ist frei [Q19]. Für ein 60er-Haus ist das ein wichtiger Punkt: Die alten Leitungen liegen oft **diagonal** und außerhalb jeder Zone — deshalb vor jedem Bohren Leitungssucher, und nach der Sanierung Fotos der Zonen [Q24].

### 5.7 Verteilung, Zuleitung, Unterverteilung je Geschoss

- **Verteiler:** bei Einraumwohnungen mindestens **3-reihig**, bei Mehrraumwohnungen mindestens **4-reihig**, mit **12 Teilungseinheiten je Reihe** [Q18].
- **Reserve:** Die 3-/4-reihige Bauform nach DIN 18015-2 ist die **Untergrenze**, nicht das Ziel [Q18]. Plane zusätzlich eine freie Reihe und Platz für einen Drehstromkreis (Herd, Wallbox, Wärmepumpe) — die häufigste Nachrüstung ist die, für die kein Platz war (Erfahrungswert, keine Normzahl).
- **Unterverteilung je Geschoss** ist bei 120 m² sinnvoll, wenn Leitungswege lang werden: kürzere Wege, kleinere Querschnitte, weniger Spannungsfall. Bei einem 60er-Haus mit zentralem Kellerzähler ist die Steigleitung sonst schnell der Engpass — die Hauptleitung wurde früher oft in **5×6 mm²** oder **5×10 mm²** gelegt [Q22].
- **Zuleitung UV:** Querschnitt nach Strombelastbarkeit, Spannungsfall (3 %) und Abschaltbedingung — gerechnet, nicht geschätzt; die Rechnung macht der Betrieb, nicht der Bauherr [Q33].
- **Kabelkanäle:** nicht auf den heutigen Bedarf dimensionieren. Ein Kanal, in den später ein zweites Kabel soll, ist der Grund für Aufputz-Flickerei — Reserve kostet beim Einbau einen Bruchteil der Nachrüstung (Erfahrungswert, keine Normzahl).
- **Außen/Garage:** eigener RCD (30 mA), **IP44**, abschließbare oder allpolig abschaltbare Steckdosen; im Außenbereich ist der RCD ohnehin Pflicht für ortsveränderliche Betriebsmittel bis 32 A [Q12][Q24].
- **Hauptpotentialausgleich:** Mindestquerschnitt **6 mm² Cu / 16 mm² Al / 50 mm² Stahl**, mehr als **25 mm² Cu** braucht die Verbindung zur Haupterdungsschiene nicht (DIN VDE 0100-540, Abschnitt 544.1). Bei großen Außenleiterquerschnitten ist nicht der Mindestquerschnitt, sondern der Spannungsfall am Leiter die Grenze ([Elektropraktiker, „Querschnitt der Schutzpotentialausgleichsleiter“](https://elektropraktiker.de/nachrichten/nachricht/querschnitt-der-schutzpotentialausgleichsleiter?p=all), 09.10.2018, geprüft 09.11.2026, HTTP 200).
- **Netzwerk:** Kommunikationsverteiler je Wohnung, ein Elektro-Installationsrohr vom Hausübergabepunkt [Q18]; Daten und 230 V **getrennt** führen, CAT-Kabel durchgehend im Leerrohr und Biegeradius einhalten (Praxisregel — eine Normstelle dafür wurde hier nicht verifiziert, siehe §11 Nr. 8).

---

## 6. Kosten

**Vorab:** Es gibt keine amtliche Preisstatistik. Die Bänder stammen aus Fachbetriebs-, Preisportal- und Kalkulationsquellen, streuen regional um 30–50 % und sind **Orientierung, kein Angebot**. Drei Angebote sind Pflicht, nicht Kür.

### 6.1 Einzelpositionen (brutto, sofern die Quelle nichts anderes sagt)

| Position | Preis | Quelle |
|---|---|---|
| **Stromkreis verlegen** inkl. Sicherung | **260–455 €** | [Q25] |
| Steckdose installieren | 104–156 € | [Q25] |
| Steckdose nachrüsten, Aufputz | 109–199 € | [Q24] |
| Steckdose UP, vorhandener Kanal | 159–269 € | [Q24] |
| Steckdose UP, neue Leitung | 269–539 € | [Q24] |
| Neue Leitung vom Verteiler | 469–809 € | [Q24] |
| Lichtschalter installieren/tauschen | 91–130 € | [Q25] |
| Wände schlitzen | 20–33 €/m | [Q25] |
| Leitung erneuern (ohne Stemmen) | 15–25 €/m | [Q25] |
| **Unterverteilung einrichten** | **520–1.040 €** | [Q25] |
| FI-Schalter einbauen | 200–400 € | [Q25] |
| Überspannungsschutz nachrüsten | 200–500 € | [Q26] |
| **Sicherungskasten inkl. Zähleranlage, SLS, ÜSS, FI** | **4.000–5.000 €** | [Q26] |
| Zählerschrank/Verteilung bei größeren Änderungen | 1.200–2.500 € | [Q25] |
| Starkstromanschluss (Herd/DLE) | 390–780 € | [Q25] |
| E-Check/Abnahme | 195–390 € | [Q25] |
| **Komplettsanierung Altbau** | **86–127 €/m²** | [Q25] |
| Komplettsanierung Altbau (andere Quelle) | 80–150 €/m² | [Q26] |

**Der Widerspruch bleibt stehen:** 86–127 €/m² [Q25] gegen 80–150 €/m² [Q26] — die Differenz ist die Ausstattung (RAL-Stufe, Smart Home, Zahl der Dosen), nicht die Qualität. Wer Preise vergleicht, vergleicht **Positionen**, nicht Quadratmeterpreise.

### 6.2 Komplettpreise nach Wohnfläche

| Objekt | Preis | Rechnung |
|---|---|---|
| EFH **100 m²** | **8.600–12.700 €** | 86–127 €/m² [Q25] |
| EFH **120 m²** | **10.300–15.200 €** | 86–127 €/m² [Q25] |
| EFH **120 m²** (weite Spanne) | 9.600–18.000 € | 80–150 €/m² × 120 m² [Q26] |
| EFH **150 m²** | **12.900–19.050 €** | 86–127 €/m² [Q25] |
| Zweifamilienhaus 200 m² | 17.200–25.400 € | Altbau-Komplettsanierung [Q25] |
| Wohnung 60 m², nur Steckdosen (12 Stück) | 2.050–3.800 € | Paketpreis [Q24] |

**Zwei durchgerechnete Beispiele der Portale** (nicht addierbar, nur zur Größenordnung): 120 m² mit **65 Arbeitsstunden à 80 €** + 4.500 € Material = **9.700 €** (121 €/m²) [Q26]; dieselbe Fläche mit **98 Stunden à 80 €** + 6.900 € Material = **14.740 €** (113 €/m²) [Q35]. Die Stundenzahl ist der eigentliche Treiber, nicht das Material.

### 6.3 Mit und ohne Eigenleistung

| Variante | Wirkung | Beleg |
|---|---|---|
| Schlitze stemmen, Dosen setzen, Kabel ziehen selbst | „bis zu **40 % der Arbeitskosten**“ | [Q26] |
| Stemmarbeiten sind der größte Einzelposten bei UP | „**40 bis 50 % der Kosten** einer Unterputz-Installation“ | [Q24] |
| Nur Möbel rücken/Aufräumen | 5–10 % | [Q25] |
| Bündelung mehrerer Gewerke | 15–20 % | [Q25] |
| Steuerbonus § 35a EStG | 20 % der Lohnkosten, max. 1.200 €/Jahr | [Q31] |

**Realistische Rechnung für 120 m²:** 10.300–15.200 € komplett [Q25]. Zieht man die in den Quellen genannten 40 % der **Arbeitskosten** für Eigenleistung ab [Q26], landet man grob bei **8.000–12.000 €** — das ist eine **eigene Schätzung** auf Basis der beiden Zahlen, keine belegte Statistik. Die 40-%-Zahl selbst ist eine Verbands-/Portalschätzung [Q26].

### 6.4 Zusatzpositionen, die gern vergessen werden

| Zusatz | Preis | Quelle |
|---|---|---|
| Fußbodenheizung nachrüsten (wasserführt) | **60–130 €/m²** | [Q27] |
| Elektrische Fußbodenheizung | 30–50 €/m² | [Q27] |
| Deckenauslass (neue Leitung + Dose) | Richtwert wie Steckdose mit neuer Leitung: **269–539 €** — eigene Position, kein Listenpreis | [Q24] |
| Rauchmelder vernetzt (je Gerät, Material + Montage) | nicht belegt — separat kalkulieren | — |
| Netzwerkdose / Smart-Home-Vorbereitung | 180–320 € je Anschluss | [Q25] |
| Wallbox installieren (11 kW, inkl. Montage) | 500–2.000 €; eigener 3-phasiger Kreis, Leerrohr vorsehen | [Q26] |

**Wichtig zur Fußbodenheizung:** Die Elektrik dafür sind Stellmotoren, Raumthermostate und die Verdrahtung zum Heizkreisverteiler — sie fällt in derselben Rohinstallation an. Wer sie später nachrüstet, stemmt ein zweites Mal. Die Estrichregel (DIN 18560-2, Mindestdicke 4 cm bei Fußbodenheizung) ist ein Heizungs-, kein Elektrothema [Q27].

---

## 7. Eigenleistung — was geht, was nicht, und warum

### 7.1 Was tatsächlich geht (und Geld spart)

| Aufgabe | Warum erlaubt | Beleg |
|---|---|---|
| Schlitze stemmen/fräsen, Dosenlöcher bohren | Bauleistung, keine Elektroarbeit | [Q1][Q14] |
| Dosen setzen, Hohlwanddosen, Leerrohre, Kanäle | Bauleistung | [Q24] |
| Kabel **nach Vorgabe** einziehen (Weg/Querschnitt/Kreis vom Betrieb festgelegt) | keine Änderung der Anlage | [Q1][Q24] |
| Durchbrüche in **nicht tragenden** Bauteilen | Statik, nicht Elektro | [Q14] |
| Verputzen, Spachteln, Streichen | Bauleistung | [Q24] |
| Fotos jeder Wand mit Maßband, Aufmaß, Raumliste | Dokumentation | [Q24] |
| Entsorgung, Container, Rückbau | Bauleistung | [Q25] |

> **Schadstoff-Vorbehalt:** Bei Baubeginn vor dem 31.10.1993 ist mit Asbest zu rechnen — auch in Spachtelmassen, Fliesenklebern und Bodenbelägen, die beim Stemmen und Schleifen zur Faserquelle werden. Die Regeln (Erkundung, Probe, ASI-Arbeit, Anzeige) stehen im Schwester-Playbook `entkernen-entsorgung.md` und sind **hier nicht erneut geprüft**.

**Der Foto-Standard:** jede Wand **offen** und **mit Maßband im Bild**, je Raum ein Ordner, Dateinamen mit Raumnummer. Ohne diese Bilder findet in zehn Jahren niemand die Leitung wieder — und der Bohrer trifft sie [Q24].

### 7.2 Was ausdrücklich nicht geht

| Aufgabe | Verboten, weil | Beleg |
|---|---|---|
| Adern an Klemmen, Dosen, Verteiler anschließen | Errichten/Ändern nur durch eingetragenes Unternehmen (NAV § 13 Abs. 2) | [Q1] |
| Absichern, FI zuordnen, Stromkreise auflegen | dito | [Q1][Q7] |
| Messen (Isolation, Schleifenimpedanz, RCD), Erstprüfung | nur Elektrofachkraft (DIN VDE 0100-600) | [Q13][Q7] |
| Inbetriebnahme, Zählerantrag | Netzbetreiber/Errichter | [Q1][Q3] |
| Zählerschrank öffnen | Bereich HAK–Messeinrichtung ist von der Instandhaltungs-Ausnahme ausgenommen | [Q1] |
| Änderung „mal eben“ | jede Erweiterung löst aktuelle Regeln aus | [Q9][Q3] |

**Warum das keine Formalie ist:**
1. **Haftung:** Wer selbst anklemmt, haftet für Personen- und Sachschäden — und zwar ohne die Gewährleistung eines Betriebs. Für die eigene Arbeit gibt es keinen Gewährleistungsanspruch gegen sich selbst; der Betrieb, der später die Anlage prüft, wird für Fremdleistung nicht ohne Weiteres geradestehen.
2. **Versicherung:** Führt der Versicherungsnehmer den Versicherungsfall **grob fahrlässig** herbei, ist der Versicherer berechtigt, die Leistung „in einem der Schwere des Verschuldens entsprechenden Verhältnis zu kürzen“ (§ 81 Abs. 2 VVG) [Q29]. Bei Vorsatz entfällt sie ganz (§ 81 Abs. 1) [Q29]. Ein selbst geklemmter Verteiler ohne Messprotokoll ist der Musterfall.
3. **Beweislast:** Ohne Prüfprotokoll fehlt der Nachweis, dass die Anlage den anerkannten Regeln der Technik entspricht — im Streit mit Versicherer, Käufer oder Handwerker [Q13].

**Die Community-Sicht ist strenger als die Norm:** „Außer Leuchtmittel wechseln darf der Laie gar nichts an der elektrischen Anlage“ — Moderator im elektrikforum.de, mit Verweis auf TAB und NAV [Q28]. Das ist die konservative Lesart; die NAV-Ausnahme für Instandhaltung ist enger, als viele denken [Q1].

### 7.3 Die Statik-Grenze beim Stemmen

Ohne statischen Nachweis (DIN EN 1996-1-1, Tabelle NA 19/NA 20) gilt für gemauerte, tragende Wände:
- **senkrechte Schlitze:** max. **30 mm** tief, ungeachtet der Wandstärke;
- **Querschnittsschwächung:** max. **6 %** bezogen auf 1 m Wandlänge;
- **Abstand zu Öffnungen** (Fenster, Türen): mind. **115 mm**;
- **waagerechte/schräge Schlitze:** nur im Bereich **≤ 0,4 m** über oder unter der Rohdecke, nur auf **einer** Wandseite, und in den Installationszonen nach DIN 18015-3 anzuordnen;
- **Langlochziegel:** dort sind Schlitze **gar nicht** erlaubt;
- zulässige Schlitztiefe nach Tabelle: **15–30 mm** (gefräst bis 40 mm). [Q14]

**Der Praxiskonflikt:** Gerätedosen mit **60 mm** Bauhöhe kollidieren mit den 30 mm. In der Vergangenheit wurden Aussparungen > 30 mm toleriert, wenn sie den Dosendurchmesser nicht überschreiten, mit Kreisschneider hergestellt sind und der Abstand mindestens der doppelte Dosendurchmesser ist — „da das aber in der Norm so nicht steht, wird kein Baustatiker diese Absolution schriftlich erteilen“ [Q14]. Konsequenz: Bei dünnen Wänden (115 mm) ist die Aufputz- oder Vorsatzschalen-Lösung keine Notlösung, sondern die statisch saubere.

### 7.4 Was du dem Betrieb vorher geben musst

1. **Raumliste mit Dosenplan** (Möbelplan, Küchenplan, TV-Wand, Arbeitsplätze).
2. **Leitungsweg-Vorgabe** vom Betrieb — schriftlich, mit Querschnitt und Stromkreisnummer.
3. **Baufreiheit** und ein Termin, an dem der Betrieb die Rohinstallation abnimmt.
4. **Fotos** der offenen Wände **vor** dem Verputzen.
5. **Schriftliche Abgrenzung** der Eigenleistung im Angebot — sonst streitet man später über Gewährleistung an genau dieser Stelle [Q24].

---

## 8. Typische Fehler — mit Quelle

### 1. „Bestandsschutz“ als Freibrief
**Symptom:** „Das Haus steht seit 1965, das darf so bleiben, ich mache nur neue Dosen.“
**Warum falsch:** Bestandsschutz gilt für den **unveränderten** Teil und nur unter vier Voraussetzungen (normgerecht errichtet, keine Folgenorm-Anpassung, gleiche Nutzung, keine Gefahr) [Q9]. Jede Erweiterung wird nach aktuellen Regeln ausgeführt [Q3]. Bei 60 Jahren ist außerdem die Lebensdauer („üblicherweise 40 Jahre“) überschritten [Q9].
**Was tun:** Bestand **aufnehmen** und schriftlich trennen: was bleibt, was neu. Ein Satz im Angebot: „Der bestehende Teil verbleibt im Bestand; die neuen Kreise werden nach DIN VDE 0100-410:2018-10 errichtet.“

### 2. Alten Zählerplatz behalten
**Symptom:** Neuer Verteiler im Keller, alte Zählertafel bleibt — „der Zähler läuft doch“.
**Warum falsch:** Zählertafeln nach DIN 43853 sind bei Erweiterungen **nicht zulässig** [Q3]. Ein zeitgemäßer Platz braucht SLS, SPD, AAR 300 mm, RfZ 150 mm [Q5].
**Was tun:** Zählerplatz im Angebot **separat** ausweisen (4.000–5.000 € inkl. SLS/ÜSS/FI) [Q26], Anmeldung durch den Betrieb [Q3].

### 3. RCD nur im Bad
**Symptom:** Ein 30-mA-FI für das Badezimmer, der Rest der Wohnung ohne.
**Warum falsch:** Die Pflicht gilt für **alle** Steckdosenstromkreise bis 32 A, die Laien zugänglich sind, und für Beleuchtungskreise in Wohnungen [Q12]. Ein FI nur im Bad lässt Küche, Kinderzimmer und Außensteckdosen ungeschützt.
**Was tun:** RCD-Gruppen oder RCBO je Kreis, so aufgeteilt, dass ein Fehler nicht alles abschaltet [Q12].

### 4. Kein Potentialausgleich / PEN nicht aufgetrennt
**Symptom:** Neue Verteilung, aber keine Haupterdungsschiene; Wasser-, Gas- und Antennenleitungen nicht angeschlossen.
**Warum falsch:** Der PEN darf für Antennen-, PV-, Blitzschutz- und Kommunikationsanlagen nicht als Erdungsleiter dienen [Q3][Q6]. Ohne Potentialausgleich liegt im Fehlerfall Spannung auf Rohren und Gehäusen; die Sichtprüfung nach DIN VDE 0100-600 prüft genau diesen Punkt (Nr. 12 und 15) [Q13].
**Was tun:** Haupterdungsschiene setzen, alle eingehenden leitfähigen Teile anschließen, Erdungswiderstand messen und protokollieren [Q13].

### 5. Leitungen in der Dämmung ohne Verlegeart-Nachweis
**Symptom:** Nachträglich aufgedoppelte Innendämmung, Kabel liegt darin, gesichert bleibt B16.
**Warum falsch:** Die Strombelastbarkeit hängt an der Verlegeart; zwischen günstigstem und ungünstigstem Fall liegen bei 1,5 mm² 4,5 A [Q15]. Wer die Verlegebedingung ändert, muss die Auslegung neu bewerten (DIN VDE 0298-4 / DIN VDE 0100-520) [Q15][Q33].
**Was tun:** Leitungswege **vor** der Dämmung festlegen; wo Dämmung unvermeidbar ist, Querschnitt erhöhen oder Leitung in der Installationsebene führen.

### 6. Schlitze zu tief oder waagerecht durch die Wand
**Symptom:** 60-mm-Dose in 115-mm-Wand, waagerechter Schlitz über die ganze Wand, Schlitz an der Wandöffnung.
**Warum falsch:** Ohne Nachweis max. 30 mm senkrecht, keine waagerechten Schlitze bis 175 mm Wanddicke, max. 6 % Schwächung, 115 mm Abstand zu Öffnungen, waagerecht nur ≤ 0,4 m über/unter der Rohdecke [Q14].
**Was tun:** Wandaufbau und Statik vor dem Stemmen klären; im Zweifel Aufputz oder Vorsatzschale [Q14].

### 7. Dosen und Leitungen in der Wärmedämmung
**Symptom:** Außenwand wird innen gedämmt, Steckdosen wandern in die Dämmebene, Leitungen liegen in der Dämmung.
**Warum falsch:** Dosen durchbrechen die Dampfbremse/Luftdichtheit und werden zur Wärmebrücke; die Leitung liegt anschließend in der ungünstigsten Verlegeart [Q15]. Für die Luftdichtheit gilt die DIN 4108-7 — **in diesem Playbook nicht geprüft**, deshalb als Planungsauflage: Dose entweder in die Installationsebene oder mit dichten Dosen und Anschluss an die Dampfbremse.
**Was tun:** Installationsebene (Vorsatzschale) vorsehen, wenn innen gedämmt wird; Dosen nicht in die Dämmung setzen.

### 8. Kein Plan, keine Beschriftung
**Symptom:** Verteiler ohne Stromkreisverzeichnis, Sicherungen ohne Nummern, kein Stromlaufplan.
**Warum falsch:** Die Sichtprüfung nach DIN VDE 0100-600 verlangt Schaltungsunterlagen und die Kennzeichnung von Stromkreisen, Überstrom-Schutzeinrichtungen und Klemmen (Nr. 9 und 10) [Q13]. ELEKTRO+ führt „Stromkreise beschriftet / Dokumentation vorhanden“ als Prüfpunkt [Q20].
**Was tun:** Beschriftung als Abnahmebedingung vereinbaren; Stromlaufplan und Prüfprotokoll gehören zur Übergabe [Q13].

### 9. „FI ist eingebaut“ mit 500 mA
**Symptom:** Ein FI ist vorhanden, deshalb gilt die Anlage als sicher.
**Warum falsch:** 500 mA liegt weit über der Grenze, ab der es für Menschen gefährlich wird (50 mA); ein 500-mA-FI ist kein Zusatzschutz im Sinne der Norm [Q23][Q12].
**Was tun:** Gerätetyp und Bemessungsdifferenzstrom ablesen lassen; 30 mA für Steckdosenkreise [Q12].

### 10. Zweiadrige Leitung mit neuer Schuko-Dose
**Symptom:** Neue Dose, alter zweiadriger Kreis ohne PE — die Optik ist neu, der Schutz fehlt.
**Warum falsch:** Ohne Schutzleiter gibt es keinen Fehlerschutz für Geräte der Schutzklasse I; der PEN-Bruch legt 230 V aufs Gehäuse [Q11]. An solche Kreis gehört keine neue Schuko-Dose [Q24].
**Was tun:** Kreis erneuern (3-adrig), Aufputzkanal als Kompromiss, oder den Kreis stilllegen. Dasselbe gilt für die Deckenlampe: Wer die alte **Lampenleitung** weiterbenutzt, weil „sie ja noch geht“, hat an der Decke eine Ader ohne Schutzleiter — der Kreis ist dann **komplett neu** zu legen.

### 11. Zu wenige Stromkreise „weil DIN nur 6 fordert“
**Symptom:** 120 m² mit 6 Kreisen, Küche und Bad teilen sich einen.
**Warum falsch:** Die 6 ist die **Mindest**ausstattung nach DIN 18015-2 [Q17]; jeder Großverbraucher kommt zusätzlich [Q18]. Die Praxis rechnet mit 12–14 Kreisen für ein EFH [Q25].
**Was tun:** Raumplanung vor Elektroplanung; Küche mit eigener Planung (Herd, GS, Kühlgeräte, Dunstabzug) [Q18].

### 12. Roten Schaltdraht weiterverwendet, ohne zu prüfen, wohin er läuft
**Symptom:** Die Lampe brennt, aber beim Abschalten des einen Kreises steht ein anderer unter Spannung.
**Warum falsch:** Der rote Draht wurde in Altinstallationen als **Schaltdraht** für die Lampe zweckentfremdet, ohne zu prüfen, wohin er noch läuft — genau dort entstehen die versteckten Verbindungen zwischen Stromkreisen.
**Was tun:** Adern vor dem Umklemmen durchklingeln und zuordnen lassen; jeder Kreis einzeln abschaltbar, Stromlaufplan nachziehen.

### 13. Klemmdose in der Wand verschwinden lassen
**Symptom:** Nach dem Verputzen ist keine Abzweigdose mehr zu sehen; später findet niemand die Klemmstelle.
**Warum falsch:** Eine **Klemmdose** unter Putz, Tapete oder hinter **Fliesen** ist nicht mehr auffindbar und damit nicht mehr prüfbar.
**Was tun:** Jede Klemmstelle gehört in eine **zugängliche** Dose und in den **Stromlaufplan** — Dokumentation ist Teil der Arbeit, nicht Papierkram.

---

## 9. Prüf- und Abnahmeliste für den Bauherrn

| # | Punkt | Nachweis |
|---|---|---|
| 1 | Stromkreisverzeichnis mit Nummern, Querschnitt, Absicherung, RCD-Zuordnung | Dokument [Q13] |
| 2 | Verteiler beschriftet (jede Sicherung, jeder RCD) | Foto [Q20] |
| 3 | Prüfprotokoll DIN VDE 0100-600 mit allen 10 Messschritten | Protokoll [Q13] |
| 4 | Isolationswiderstand ≥ 1 MΩ | Messwert im Protokoll [Q13] |
| 5 | RCD-Auslösestrom/-zeit je Gruppe gemessen | Messwert im Protokoll [Q13] |
| 6 | Schleifenimpedanz je Stromkreis, Abschaltbedingung erfüllt | Messwert [Q13] |
| 7 | Erdungswiderstand/Haupterdungsschiene | Messwert + Foto [Q13][Q3] |
| 8 | Fotos aller Wände mit Maßband | Ordner je Raum [Q24] |
| 9 | Rauchmelder in Schlafräumen + Rettungswegen, funktionsfähig | Begehung [Q8] |
| 10 | Rechnungen getrennt nach Lohn/Material (für § 35a EStG) | Rechnung [Q31] |
| 11 | Abnahmeprotokoll mit Mängelfristen, unterschrieben | Protokoll [Q32] |
| 12 | RCD-Auslösung bei **≤ I∆N**, Prüfstromart im Protokoll (Typ A: pulsierender DC, 6 mA DC-Offset möglich) | Messwert + Prüfstromart [Q36] |
| 13 | Hauptpotentialausgleich: Mindestquerschnitt **6 mm² Cu / 16 mm² Al / 50 mm² Stahl**, nicht mehr als **25 mm² Cu** nötig | Messwert + Foto [Q37] |

---

## 10. Quellen

**Typ:** G = Gesetz/Verordnung, U = Unfallverhütungsvorschrift, N = Norm/Anwendungsregel (auch über zitierende Fachquelle), F = Fachverlag/Fachartikel, V = Verband/Initiative, H = Hersteller, B = Fachbetrieb, P = Preisportal, C = Community/Referenz, Y = Video.

| # | Quelle | Typ | Geprüft |
|---|---|---|---|
| Q1 | NAV § 13, https://www.gesetze-im-internet.de/nav/__13.html | G | Volltext gelesen; Abs. 2 Sätze 4–5, Abs. 4 wörtlich |
| Q2 | NAV § 19, https://www.gesetze-im-internet.de/nav/__19.html | G | Volltext; Abs. 2 (Mitteilung, 12 kVA) wörtlich |
| Q3 | BDEW, Bundesmusterwortlaut TAB Niederspannung (TAB 2026), Version 1.0, 30.07.2026, PDF: https://bdew.de/media/original_images/2026/07/31/bdew_musterwortlaut_tab_niederspannung_2026_v1_0.pdf | N | PDF geladen, § 1 (3), § 4.1, § 4.4 (1)–(7), § 11 wörtlich gelesen |
| Q4 | VDE FNN, Hinweis „Zählerplätze in Bestandsanlagen“, PDF: https://www.vde.com/resource/blob/2308614/43b92f419c25661679ea337686871b5d/vde-fnn-hinweis-zaehlerplaetze-in-bestandsanlagen-data.pdf | N | PDF gelesen; Abschnitte 5.5, 6.3, 6.5 |
| Q5 | Hager, „VDE-AR-N 4100:2026-04“, https://hager.com/de/wissen/normen/vde-ar-n-4100 | H | Volltext; Maße ZF/RfZ/AAR, SLS, SPD, Hauptschalter 3-Punkt |
| Q6 | DEHN, „VDE-AR-N 4100 (Ausgabe 2026)“, https://www.dehn.de/de/wissen/normen/anwendungsregel-vde-ar-n-4100 | H | Volltext; gilt seit 06.03.2026, Erdung/PEN im Bestand, § 14a |
| Q7 | DGUV Vorschrift 3, PDF: https://publikationen.dguv.de/widgets/pdf/download/article/1052 | U | Volltext; § 2 (3), § 3 (1)/(2), § 5 (1) wörtlich |
| Q8 | LBO Baden-Württemberg § 15, https://www.landesrecht-bw.de/perma?d=jlr-NNLBW00007BCCNN00000000019 | G | Volltext; Abs. 9 wörtlich (Fassung 16.03.2026) |
| Q9 | ELEKTRO+, „Grundlagen“ (Bestandsschutz), https://www.elektro-plus.com/elektroplanung/bestandsschutz/grundlagen | V | Volltext; vier Voraussetzungen, 40 Jahre, Erweiterung/Änderung |
| Q10 | Elektropraktiker, „Bestandsschutz und Anpassung elektrischer Anlagen“, ep 8/2001, https://www.elektropraktiker.de/fachartikel/detail/bestandsschutz-und-anpassung-elektrischer-anlagen | F | Volltext; klassische Nullung mit Bestandsschutz, Zitat „nicht zu erwarten“ |
| Q11 | Wikipedia „Nullung“, https://de.wikipedia.org/wiki/Klassische_Nullung | C | Volltext; 1.5.1973, 31.3.1974, 10 mm²/16 mm², VDE 0105-100 Zitat |
| Q12 | Hager Tipp 36, „DIN VDE 0100-410:2018-10 und -530:2018-6“, PDF: https://www.hager.de/files/download/0/24800499_1/0/22DE0189-tip-h-36-din-vde-0100-4102018-10-web.pdf | N (Hersteller-Fachinfo) | Volltext; 30 mA/32 A (vorher 20 A), Beleuchtungskreise, DIN-18015-2-Zitat, RCBO |
| Q13 | WEKA, „Erstprüfung nach DIN VDE 0100-600 korrekt durchführen“, Stand 28.04.2026, https://www.weka.de/elektrosicherheit/erstpruefung-nach-din-vde-0100-600 | F | Volltext; 16 Sichtpunkte, 10 Messschritte, 1 MΩ, Prüfbericht |
| Q14 | Elektropraktiker, „Statikbetrachtungen für nachträgliches Schlitzen in gemauerten Wänden“, ep 3/2015, https://www.elektropraktiker.de/fachartikel/detail/statikbetrachtungen-fuer-nachtraegliches-schlitzen-in-gemauerten-waenden?p=all | F | Volltext; 30 mm, 6 %, 115 mm, 0,4 m, 60-mm-Dosen |
| Q15 | ElektrikerWissen, „Mindestquerschnitt für Steckdosenstromkreise“, 25.01.2024, https://www.elektrikerwissen.de/leitungsquerschnitt-fuer-steckdosenstromkreise | B | Volltext; Iz-Werte A1/A2/B1/B2/C, 1,5 mm² Minimum, 3 %/18 m, Zs 300 mΩ |
| Q16 | ElektrikerWissen, „DIN VDE 0100-410: FI-Pflicht“, https://www.elektrikerwissen.de/din-vde-0100-410-fi-schutzschalter-pflicht/ | B | Volltext; Schutzebenen, Zs-Berechnung, RCD ≠ Leitungsschutz |
| Q17 | ASVENDO, „DIN 18015-2 Mindestausstattung und RAL-RG 678“, Stand 12.09.2026, PDF: https://asvendo.de/cdn/shop/t/90/assets/asv-din-18015-mindestausstattung.pdf | N (Sekundärauszug) | Volltext; Stromkreis-Tabelle, RAL-Stufen, Abgrenzung DIN/RAL |
| Q18 | elektro.net, „Elektrische Anlagen in Wohngebäuden – Teil 2: Art und Umfang der Mindestausstattung“, 06.10.2021, https://www.elektro.net/120701/teil-2-art-und-umfang-der-mindestausstattung/ | F | Volltext; 4 Kreise bei 50–75 m², 3-/4-reihig, 12 TE, Kommunikationsverteiler |
| Q19 | Gira, „Elektroinstallationszonen … DIN 18015-3“, 15.10.2026, https://gira.de/g-pulse-magazin/bauplanung/installationszonen-elektro | H | Volltext; Zonen 15–45/100–130 cm, 20 cm senkrecht, 10–30 cm, 105 cm |
| Q20 | ELEKTRO+, „Kontrollieren Sie Ihre elektrische Anlage“, https://www.elektro-plus.com/sicherheit/elektroinstallation-in-wohngebaeuden/kontrolle-der-anlage | V | Volltext; Checkliste, Schraubsicherung vor 1979, Bakelit ≥ 50 Jahre, Testtaste 2×/Jahr |
| Q21 | YouTube, ElektroM, „Altbau Elektrosanierung! (Teil 1)“, 11.09.2023, 14:02, https://www.youtube.com/watch?v=_f3LehFAEns | Y | Untertitel geladen; 00:00:31 Zählertafel/Wechselstromzähler, 00:06:32–00:07:00 „alles zweidrahtig“ |
| Q22 | YouTube, Freunde des Stroms, „ZÄHLERSCHRANK IM ALTBAU …“, 06.09.2026, 12:43, https://www.youtube.com/watch?v=GOPAgGtGBro | Y | Untertitel; 00:01:03 SLS/TAB 2007, 00:05:18 VDE-AR-N 4100 § 4.4 zitiert, 00:10:23 Zeitlinie SLS/APZ/ÜSS |
| Q23 | YouTube, Lets-Bastel, „Haussanierung: Muss die Elektrik neu gemacht werden?“, 15.08.2024, 24:13, https://www.youtube.com/watch?v=S47ADjk_WXw | Y | Untertitel; 00:01:22 „30 mA statt 500 mA“, 00:01:47 Bestandsschutz-Grenze, 00:02:44 50-mA-Grenze |
| Q24 | Alboush Elektrotechnik (Elektromeister, HWK Münster), „Steckdosen nachrüsten im Altbau“, 21.01.2026/13.09.2026, https://alboush-elektro.de/blog/steckdosen-nachruesten-altbau-kosten | B | Volltext; Preise, Alu, Nullung, Stemmarbeiten 40–50 % |
| Q25 | BerufExperten, „Elektroinstallation Kosten, Preise 2026“, https://berufexperten.de/preise/elektroinstallation | P | Volltext; 260–455 €/Kreis, 86–127 €/m², 12–14 Kreise EFH |
| Q26 | Wohnen in Südwestfalen, „Elektrik im Haus erneuern“, https://wohnen-in-suedwestfalen.de/wissen/elektrik-im-haus-erneuern | P | Volltext; 4.000–5.000 € Zähleranlage, 80–150 €/m², 40 % Eigenleistung, 65 h/9.700 € |
| Q27 | Vattenfall, „Fußbodenheizung: Kosten für Einbau & Betrieb“, https://www.vattenfall.de/infowelt-energie/nachhaltig-heizen/fussbodenheizung-kosten-fuer-einbau-und-betrieb | H | Volltext; 60–130 €/m² Nachrüstung, 30–50 €/m² elektrisch, DIN 18560-2 |
| Q28 | elektrikforum.de, „Was ist erlaubt, was verboten (für einen Laien)“, https://www.elektrikforum.de/threads/was-ist-erlaubt-was-verboten-fuer-einen-laien.16845/ | C | Thread gelesen; Zitat Moderator, Widerspruch zu 0,5 % |
| Q29 | VVG § 81, https://www.gesetze-im-internet.de/vvg_2008/__81.html | G | Volltext; Abs. 1 und 2 wörtlich |
| Q30 | Grauer-Thomas (Elektrobetrieb), „Elektroinstallation“ (Historie, Verlegearten, Alu), https://www.grauer-thomas.de/elektroinstallation | B | Volltext; Blechrohr bis 1950er, Stegleitung, Alu/DDR, Cu-Al-Klemmen |
| Q31 | EStG § 35a, https://www.gesetze-im-internet.de/estg/__35a.html | G | Volltext; Abs. 3: 20 %, max. 1.200 € |
| Q32 | BGB § 634a, https://www.gesetze-im-internet.de/bgb/__634a.html | G | Volltext; 5 Jahre bei Bauwerk |
| Q33 | Elektropraktiker, „Dimensionierung einer Zuleitung“, https://www.elektropraktiker.de/fachartikel/detail/dimensionierung-einer-zuleitung | F | Volltext; DIN VDE 0100-520:2013-06, Abschnitt 525, Anhang G (3 %/5 %) |
| Q34 | Elektropraktiker, „Prüfung des Spannungsfalls“, https://www.elektropraktiker.de/fachartikel/detail/pruefung-des-spannungsfalls | F | Volltext; DIN 18015-1: 3 % hinter der Messeinrichtung |
| Q35 | Wohnglück, „Elektrik im Haus erneuern: Kosten, Förderung & Tipps“, https://wohnglueck.de/artikel/neue-elektrik-kosten | P | Volltext; 98 h/6.900 € = 14.740 €, 12.000–18.000 € für 120 m², 80–150 €/m² |
| Q36 | Elektropraktiker, „Prüfung von RCDs", https://www.elektropraktiker.de/nachrichten/nachricht/pruefung-von-rcds?p=all (28.01.2020) | F | Volltext; Auslösefenster 0,5–1 / 0,35–1,4 / 0,5–2 × I∆N, 6 mA DC, Stufen < 1/30 I∆N, Bewertung ≤ I∆N |
| Q37 | Elektropraktiker, „Querschnitt der Schutzpotentialausgleichsleiter", https://elektropraktiker.de/nachrichten/nachricht/querschnitt-der-schutzpotentialausgleichsleiter?p=all (09.10.2018) | F | Volltext; DIN VDE 0100-540 Abschn. 544.1: 6/16/50 mm², max. 25 mm² Cu |

**Anzahl geprüfter Quellen: 37.** Verteilung: 7 Gesetz/UVV (Q1, Q2, Q7, Q8, Q29, Q31, Q32), 6 Norm/Anwendungsregel (Q3, Q4, Q5, Q6, Q12, Q17), 8 Fachverlag/Fachartikel (Q10, Q13, Q14, Q18, Q33, Q34, Q36, Q37), 2 Verband/Initiative (Q9, Q20), 2 Hersteller (Q19, Q27), 4 Fachbetrieb/Fachblog (Q15, Q16, Q24, Q30), 3 Preisportal (Q25, Q26, Q35), 2 Community/Referenz (Q11, Q28), 3 Video (Q21, Q22, Q23).

### Prüftiefe — was ich selbst gelesen habe

- **Volltext gelesen und wörtlich zitiert:** Q1, Q2, Q3 (Auszüge § 1, § 4.4, § 11), Q4 (Auszüge), Q5, Q6, Q7, Q8 (§ 15 Abs. 9), Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q24, Q25, Q26, Q27, Q29, Q30, Q31 (Abs. 3), Q33, Q34, Q36, Q37.
- **Untertitel geladen, Zeitmarken aus automatischen Untertiteln (±10 s, ASR-Fehler möglich):** Q21, Q22, Q23. Zitate daraus sind Hörbelege, keine Bildbelege.
- **Nur Thread gelesen, Zitat stichprobenartig:** Q28.
- **Nur Existenz/Ausgabe geprüft:** keine — alle Quellen wurden abgerufen (HTTP 200).
- **Zugriffs-Notiz:** Das Hager-PDF (Q12) liefert Inhalt und HTTP 200, hat aber eine Zertifikatskette, die `curl` ohne `-k` ablehnt; im Browser und über den Extraktor ist es lesbar. Zwei Seiten antworten nur mit Bot-Schutz (de.electrical-installation.org: 403) und wurden deshalb **nicht** als Beleg verwendet.

### Nicht verwendete, aber geprüfte Quellen

- `https://www.my-hammer.de/elektrik/preisradar/was-kostet-elektroinstallation` — 403 (Bot-Schutz), Preise widersprüchlich (90–180 €/m² gegen 60–85 €/m² auf derselben Seite), deshalb nicht zitiert.
- `https://de.electrical-installation.org/dewiki/Maximaler_Spannungsfall` und `.../Bestimmung_des_Leiterquerschnittes_...` — 403, Inhalt nicht erneut verifizierbar; die 3 %/5 %-Tabelle ist über Q33 belegt.

---

## 11. Unbelegt / offen

1. **„Bestandsschutz heißt, ich darf nichts ändern“** und **„Bestandsschutz heißt, alles darf bleiben“** — beides zu einfach. Der unveränderte Teil bleibt unter vier Voraussetzungen [Q9]; jede Erweiterung löst aktuelle Regeln aus [Q3]. Und: Die klassische Nullung hat nach Fachliteratur Bestandsschutz, eine Anpassungsforderung wird „nicht zu erwarten“ sein [Q10] — während eine neue Schuko-Dose daran unzulässig ist [Q24]. Der Widerspruch ist echt und wird hier nicht aufgelöst.
2. **„FI ist seit 2009 Pflicht“** — die Zäsur der DIN VDE 0100-410:2018-10 liegt bei 32 A (vorher 20 A) [Q12]; ältere Daten (2007, 2009) kursieren, sind aber nicht die aktuelle Anforderung. Belegt ist nur: **30 mA, ≤ 32 A**.
3. **Prüffristen für selbst genutzte EFH** — keine gesetzliche Pflicht gefunden. DGUV V3 adressiert Unternehmer [Q7]; ELEKTRO+ empfiehlt die wiederkehrende Prüfung, nennt aber keine Frist [Q20].
4. **Eigenleistungs-Anteil** — „bis zu 40 % der Arbeitskosten“ [Q26] und „Stemmarbeiten 40–50 % der UP-Kosten“ [Q24] sind Schätzungen von Portalen/Betrieben, keine Studie. Eine belastbare Erhebung wurde nicht gefunden.
5. **Kosten** — keine amtliche Statistik; die Bänder streuen bis 100 % (86–127 €/m² gegen 80–150 €/m²). Jede Zahl ist eine Marktbeobachtung, kein Angebot.
6. **Verlegeart-Zuordnung „gedämmte Wand = A1/A2“** — die Iz-Werte je Verlegeart sind belegt [Q15], die Zuordnung der Einbausituation zur Verlegeart konnte in dieser Recherche nicht über eine abrufbare Fachquelle bestätigt werden (Planungskompendium antwortet 403). Deshalb steht im Text nur: Verlegeart ändert sich mit dem Weg und ist neu zu bewerten — die konkrete Zuordnung bleibt Aufgabe des Betriebs.
7. **Dosen in der Wärmedämmung** — die elektrische Seite ist belegt (Verlegeart, [Q15]); die luftdichtheits-/bauphysikalische Seite (DIN 4108-7) wurde **nicht** geprüft. Die Aussage ist deshalb als Planungsauflage formuliert, nicht als Normzitat.
8. **Netzwerk „getrennt von 230 V führen“** — als Praxisempfehlung formuliert; eine Normstelle wurde nicht verifiziert. Belegt ist nur der Kommunikationsverteiler je Wohnung [Q18].
9. **Rauchmelder-Kosten und Deckenauslass-Preise** — keine belastbare Einzelquelle gefunden. Der Deckenauslass ist deshalb nur als Richtwert über den Preis einer Steckdose mit neuer Leitung angegeben [Q24], nicht als Listenpreis.
10. **RCD Typ B für Wallbox/PV/Frequenzumrichter** — die Anforderung ist gängige Praxis, in den hier geprüften Quellen aber nicht wörtlich belegt; Q12 belegt nur die Einführung des Typs F und die Brandschutzschalter. Die Typwahl bleibt dem Betrieb.
11. **VDE-AR-N 4100:2019-04 vs. 2026-04** — die TAB 2026 verweist in § 4.4 noch auf die 2019-04-Fassung (Zitat im VDE-FNN-Hinweis), während Hager/DEHN die Ausgabe 2026-04 mit Gültigkeit ab 06.03.2026 nennen [Q3][Q4][Q5][Q6]. Für die Praxis gilt die beim eigenen Netzbetreiber veröffentlichte Fassung; das ist der Punkt, an dem man **anruft**, statt zu raten.

---

## 12. Die 12 Regeln (zum Mitnehmen)

1. **Nichts anfassen, was unter Spannung steht.** Anklemmen, absichern, messen: Fachbetrieb (NAV § 13 Abs. 2) [Q1].
2. **Erst messen, dann planen.** Isolationswiderstand, Schleifenimpedanz, RCD-Zeit — vor dem ersten Angebot [Q13].
3. **Zweiadern = Stopp.** Keine neue Schuko-Dose an klassischer Nullung [Q24][Q11].
4. **Zählertafel ist kein Zählerplatz.** Bei Erweiterung unzulässig [Q3]; SLS, SPD, AAR 300 mm, RfZ 150 mm [Q5].
5. **30 mA, nicht 500 mA.** Alle Steckdosenkreise bis 32 A, Beleuchtung in Wohnungen [Q12].
6. **RCD-Gruppen statt ein FI für alles.** Ein Fehler darf nicht das Haus dunkel machen [Q12].
7. **1,5 mm² und B16 reichen** — bis 18 m; darüber 2,5 mm² oder kürzerer Weg [Q15].
8. **0,5 % / 3 % / 4 %** — HAK–Zähler, Zähler–Verbraucher, gesamt [Q1][Q34][Q33].
9. **Schlitz nie tiefer als 30 mm** ohne Statiknachweis; 6 %, 115 mm, 0,4 m beachten [Q14].
10. **Fotos, Fotos, Fotos** — jede Wand offen, mit Maßband, je Raum [Q24].
11. **Eigenleistung endet vor der Klemme** — sonst § 81 VVG [Q29].
12. **Prüfprotokoll oder keine Abnahme** — ohne Messung keine Sicherheit, ohne Protokoll keine Gewährleistung [Q13][Q32].
