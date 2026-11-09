# Elektro im Bestand nachrüsten — Vorbereitung, Kosten, Pfusch-Erkennung

> **Preisstand 09/2026.** Alle Preise sind Orientierungswerte inkl. MwSt. aus den genannten Quellen —
> regional verschieden, keine Angebote. Wer später damit rechnet, prüft sie neu.

## Kurzantwort

- **Grenze zuerst:** 230 V = eingetragenes Installationsunternehmen (NAV § 13 Abs. 2). Eigenleistung endet
  bei Schlitzen, Dosen, Leerrohren und Kabelziehen nach Vorgabe.
- **Bestand prüfen:** zweiadrige Leitungen, klassische Nullung, fehlender PE, „Deko-FI“ — vor jedem Anbau.
- **Kosten:** 80–150 € je Steckdose, Zählerschrank 1.490–2.380 €, E-CHECK 80–660 €.
- **Pflichten:** RCD 30 mA für Steckdosenkreise, Prüfprotokoll nach DIN VDE 0100-600, Kennzeichnung nach
  DIN VDE 0100-510 Abschnitt 514.


**Zielgruppe:** Eigenheimbesitzer, Bestand 1950–1990, die Elektrik modernisieren wollen.
**Stand:** 09.11.2026. Alle Preise sind Orientierungswerte, kein Angebot. Alle Faktenaussagen tragen eine Quellennummer [Q#]; die Quellen stehen mit URL, Typ und Datum in §9.

> **Die eine Grenze, die alles andere bestimmt:** Errichten, Erweitern und Ändern der Anlage hinter der Hausanschlusssicherung darf nur ein in das Installateurverzeichnis eines Netzbetreibers eingetragenes Installationsunternehmen ausführen — auch im eigenen, selbst bewohnten Haus (NAV § 13 Abs. 2 Satz 4) [Q1]. Ausgenommen sind nur **Instandhaltungsarbeiten** (Satz 5), und auch die nicht im Bereich zwischen Hausanschlusssicherung und Messeinrichtung. Dieses Playbook beschreibt deshalb **Vorbereitung, Erkennung, Kosten und Ablauf** — nicht das Anklemmen.

---

## 1. In 60 Sekunden

1. **Erst prüfen, dann planen.** Ein E-CHECK kostet 80–660 € je nach Region und Umfang und entscheidet, ob du einen Verteiler-Tausch brauchst oder eine Vollsanierung [Q11][Q10].
2. **Der billigste große Hebel ist der Verteiler**, nicht die Wand: neuer Kasten mit FI und Reserven kostet 480–2.500 € — aber nur, wenn die Leitungen einen Schutzleiter haben [Q10][Q12].
3. **Zweiadrig ohne PE ist ein K.-o.-Kriterium.** An solche Stromkreise kommt keine neue Schuko-Dose; der Kreis muss neu [Q5][Q2].
4. **Eigenleistung ist erlaubt, solange sie aufhört, bevor es elektrisch wird:** Schlitze, Dosenlöcher, Leerrohre, Kabel einziehen nach Vorgabe, Fotos, Aufmaß [Q1][Q15][Q10].
5. **Wer saniert, plant heute 20 % Reserve** im Zählerschrank und Leerrohre in jedem Raum — beides kostet jetzt wenig und später ein Vermögen [Q9][Q35].

---

## 2. Bestandsaufnahme in 20 Minuten (ohne Werkzeug)

### 2.1 Sichtprüfung — was du selbst sehen darfst

ELEKTRO+ gibt dafür eine Checkliste heraus und schreibt ausdrücklich: am Zählerschrank **nicht arbeiten**, nur sehen [Q8].

| Befund | Was er bedeutet | Konsequenz |
|---|---|---|
| **Schraubsicherungen** (DIAZED) im Verteiler | „deutet auf eine Installation vor 1979 hin" [Q8] | Prüfung, mittelfristig Verteiler neu |
| **Zähler auf Holz- oder schwarzer Bakelit-Tafel** | Anlage „mindestens 50 Jahre alt" [Q8] | Vollsanierung wahrscheinlich |
| **Kein Gerät mit Test-Taste** im Verteiler | kein FI/RCD vorhanden [Q8] | FI-Pflicht bei jeder Erweiterung; Nachrüstung 150–800 € [Q12] |
| **Nur zwei Adern** in der Dose, kein grün-gelber Leiter | Zwei-Leiter-Stromkreis (L + PEN) oder PE nicht aufgelegt [Q2][Q3] | keine neue Schuko-Dose; Kreis erneuern [Q5] |
| **PE und N in der Dose gebrückt** | klassische Nullung (TN-C) [Q2][Q4] | Bestand darf bleiben, aber keine Erweiterung an diesem Kreis; PEN-Bruch legt 230 V aufs Gehäuse [Q2] |
| **Silbrige, weiche Adern** | Aluminiumleitung (v. a. 1960er/70er, DDR) [Q5][Q2] | Alu/Cu nicht ohne Spezialklemme mischen; Fachbetrieb entscheidet über Ersatz [Q5] |
| **Stoff- oder Gummiisolierung** | Leitung muss ersetzt werden, unabhängig vom Baujahr [Q10] | Stromkreis neu |
| **Verteiler unbeschriftet, kein Stromlaufplan** | keine Dokumentation [Q8] | vor Auftrag nachliefern lassen |
| **Dunkel verfärbte Dosen, gebrochene Abdeckungen, lose Schalter** | Überhitzung/Übergangswiderstand [Q8] | sofort prüfen lassen |

**Wichtig zur Farbe:** Fehlendes Grün-Gelb ist ein Warnsignal, aber kein Beweis. Im Fachvideo steckt ein dreiadriges Kabel in der Dose, der Schutzleiter ist trotzdem nicht aufgelegt [Q3, 01:20–01:25 und 03:27–03:48].

### 2.2 Die drei Leiterarten, die man auseinanderhalten muss

- **Zweiadrig (L + PEN):** klassische Nullung, in Deutschland für Neuanlagen seit **1. Mai 1973** verboten (Übergangsfrist bis 31.03.1974); PEN-Verbindungen nur noch ab 10 mm² Cu / 16 mm² Al [Q2].
- **Dreiadrig (L + N + PE):** heutiger Standard für Licht/Steckdosen, 1,5 mm² [Q18].
- **Fünfadrig (3×L + N + PE):** Drehstrom für Herd, Durchlauferhitzer, Wallbox, Wärmepumpe [Q13][Q3].

### 2.3 Messen: wer darf was

- **Du darfst:** sehen, riechen, FI-Testtaste drücken. ELEKTRO+ empfiehlt die Testtaste **zweimal im Jahr** [Q8].
- **Nur Elektrofachkraft:** Isolationswiderstand, Schutzleiterdurchgängigkeit, Schleifenimpedanz, RCD-Auslösezeit, Drehfeld. Die Erstprüfung nach DIN VDE 0100-600 darf „ausschließlich eine befähigte Person (Elektrofachkraft)" durchführen [Q17].
- **Warum das keine Formalie ist:** DGUV Vorschrift 3 definiert die Elektrofachkraft über Ausbildung, Kenntnisse und Erfahrung (§ 2 Abs. 3) und verlangt Errichten/Ändern/Instandhalten „nur von einer Elektrofachkraft oder unter Leitung und Aufsicht" (§ 3 Abs. 1) [Q19]. Adressat ist der Unternehmer — für private Eigentümer gibt es keine gesetzliche Prüfpflicht, aber auch keine Befreiung von den anerkannten Regeln der Technik. Prüfungen bestehen aus **Besichtigen, Messen und Erproben**, und das Ergebnis ist zu dokumentieren [Q16].
- **Folge im Schadensfall:** fehlt das Prüfprotokoll, kann der Versicherer wegen grober Fahrlässigkeit kürzen (§ 81 VVG) [Q14].

**Praxis-Test (10 Minuten, ohne Werkzeug):** Sicherung raus ist **kein** Beweis für Spannungsfreiheit. Wer die Dose öffnen will, lässt sich die Spannungsfreiheit vorher von einer Elektrofachkraft mit zweipoligem Spannungsprüfer bestätigen; sonst bleibt die Dose zu und der E-CHECK liefert die Adernzahl. Fotos macht man in beiden Fällen.

---

## 3. Was der Laie vorbereiten darf — und was nicht

| Erlaubt (Vorbereitung) | Nicht erlaubt (Anlage) |
|---|---|
| Schlitze stemmen/fräsen, Dosenlöcher bohren [Q10][Q15] | Kabel an Klemmen, Dosen oder Verteiler anschließen [Q1][Q15] |
| Leerrohre und Kabelkanäle setzen [Q10] | Absichern, FI zuordnen, Stromkreise auflegen [Q1][Q17] |
| Kabel **nach Vorgabe** einziehen (Leitungsweg, Querschnitt, Zone vom Betrieb festgelegt) [Q1][Q10] | Messen und in Betrieb nehmen [Q17][Q19] |
| Durchbrüche **nicht tragender** Bauteile, Kernlochbohrungen nach Freigabe [Q10] | Durchbruch in tragenden Bauteilen, Statik [Q10] |
| Verputzen der Schlitze, Spachteln, Streichen [Q10] | Zählerschrank öffnen, Zählerantrag stellen [Q1][Q8] |
| Fotos jeder offenen Wand mit Maßband, Aufmaß, Raumliste [Q10] | Änderung/Erweiterung der Anlage „mal eben" [Q1] |

**Was Praktiker dazu sagen (Forum/Community, keine Rechtsquelle):**
- „Ein und Anbauen darfst du alles, nur einschalten bzw. ans Netz bringen darfst du es nicht" — Berufsangabe Elektriker/IT-Systemelektroniker [Q20].
- „you're allowed to ‚prepare' a lot of the work for the electrician … however he is the only one officially allowed to connect anything to the fuse box" [Q15].
- Ein Elektro-Meisterbetrieb formuliert es so: Stemmen und Verputzen könne der Bauherr selbst, „wenn das mit dem Betrieb vorher abgestimmt ist" [Q10].

**Drei Grenzen, die auch der netteste Elektriker nicht wegdiskutieren kann:**
1. **Statik:** senkrechte Schlitze ohne Nachweis max. **30 mm tief**; waagerechte Schlitze bis **175 mm Wanddicke gar nicht** (ohne Nachweis); max. **6 % Querschnittsschwächung je Meter**; mind. **115 mm Abstand** zu Öffnungen; waagerecht nur im Bereich **≤ 0,4 m über/unter der Rohdecke** und nur auf einer Wandseite [Q21]. Eine 60 mm tiefe Schalterdose ist damit in dünner Wand ein Statikthema.
2. **Asbest:** Baubeginn vor 31.10.1993 → begründeter Verdacht (gesetzlicher „Generalverdacht“ seit 5.12.2024 entfallen, Details in `entkernen-entsorgung.md`); Rückbau ist ASI-Arbeit (Details im Schwester-Playbook).
3. **Brandschutz:** Durchdringungen von Brandwänden/-decken nur mit zugelassenen Abschottungen.

---

## 4. Zahlen, die die Planung bestimmen

### 4.1 Querschnitt und Absicherung

| Querschnitt | Belastbarkeit (NYM-J, 2 belastete Adern) | Typische Absicherung | Einsatz |
|---|---|---|---|
| **1,5 mm²** | 16,5 A (Verlegeart A1/A2), 18,5 A (B1), 21 A (C) [Q18] | **B16** | Licht, Steckdosen, Standardstromkreis [Q18] |
| **2,5 mm²** | höher, abhängig von Verlegeart | 16 A, teils 20 A | Küche, Großverbraucher, lange Wege, Unterverteilung [Q5] |
| **5-adrig (3L + N + PE)** | projektiert | 16/32 A | Herd, Durchlauferhitzer, Wallbox — Auslegung durch Fachbetrieb [Q13] |

**Merksatz:** 1,5 mm² ist für einen B16-Steckdosenstromkreis ausreichend — ein pauschales „2,5 mm² ist vorgeschrieben" gibt es nicht [Q18]. Umgekehrt gilt: 2,5 mm² rettet keine 50-A-Absicherung. Genau dieser Fall steht im Pfusch-Video: 6 mm² Zuleitung mit 50 A, dahinter ein Durchlauferhitzer mit 2,5 mm² [Q3, 01:59–02:24].

### 4.2 Stromkreise (DIN 18015-2, Stufe 1)

| Wohnfläche | Stromkreise (allgemein) |
|---|---|
| bis 50 m² | 3 |
| über 50–75 m² | 4 |
| über 75–100 m² | 5 |
| über 100–125 m² | 6 |
| darüber | 7 |

Quelle: HEA/RAL-Planungshilfe, Auszug in [Q7]. **Zusätzlich** bekommt jeder Großverbraucher einen eigenen Stromkreis: Herd, Backofen, Geschirrspüler, Mikrowelle, Waschmaschine, Trockner, Warmwassergerät, Heizung, Rollladen, Sauna [Q22]; Wallbox [Q13].

### 4.3 Steckdosen je Raum (DIN 18015-2 Stufe 1 / RAL-RG 678 Stufe 2 / Stufe 3)

| Raum | Stufe 1 (Norm-Minimum) | Stufe 2 (Standard) | Stufe 3 (Komfort) |
|---|---|---|---|
| Wohnen bis 20 m² | 4 | 8 | 10 |
| Küche | 3 (+ Arbeitsfläche separat) | 3 (+ separat) | 5 (+ separat) |
| Schlafen bis 16 m² | 6 | 8 | 10 |
| Kinderzimmer bis 16 m² | 6 | 8 | 10 |
| Bad | 2 | 4 | 5 |
| Flur bis 4 m | 1 | 2 | 3 |

Auszug aus der HEA-RAL-Planungshilfe 2023, wiedergegeben in [Q7]; die Norm selbst ist kostenpflichtig (DIN 18015-2:2021-10) [Q6].

> **Achtung, verbreiteter Fehler:** „Laut DIN sind im Wohnzimmer mindestens 8 Steckdosen Pflicht" ist falsch. 8 ist **RAL-Stufe 2**, nicht das DIN-Minimum; Stufe 2/3 werden erst verbindlich, wenn sie vertraglich vereinbart sind [Q9][Q7]. Ein Elektro-Meisterbetrieb schreibt diesen Satz trotzdem — ein Beispiel dafür, dass Marketingtexte die Norm überzeichnen [Q5].

### 4.4 Installationszonen (DIN 18015-3:2016-09)

| Zone | Lage | Breite | Vorzug |
|---|---|---|---|
| **waagerecht oben/unten** | 15–45 cm über Fertigfußboden bzw. unter Decke | 30 cm | Mitte = 30 cm über FFOK [Q23][Q24] |
| **waagerecht Mitte (Küche/Arbeitsraum)** | 100–130 cm über FFOK | 30 cm | 115 cm [Q23] |
| **senkrecht** | 10–30 cm neben Rohbaukante/Ecke, beidseits Fenster, Griffseite Tür | 20 cm | 15 cm von der Kante [Q23][Q24] |
| **Schalterhöhe** | — | — | oberste Bedienstelle mittig 105 cm [Q23] |
| **Bad** | eigene Schutzzonen nach DIN VDE 0100-701 | — | Steckdosen erst ab Zone 2 [Q7][Q24] |

Die Norm gilt für **Unterputz**; Aufputz ist frei [Q24]. Im Video (Projektbeispiel, keine Normhöhe): Dosenmitte 1,50 m, 15 cm von der Türkante, waagerechte Linie bei 30 cm über Fertigfußboden [Q25, 10:08–10:54 und 14:07–14:26]; Zonenbreiten 30 cm, Abstand 20 cm bzw. 15 cm an der Türzarge [Q26, 08:20–08:44].

### 4.5 Zeitaufwand (Richtwerte)

| Position | Zeit | Quelle |
|---|---|---|
| Steckdose/Schalter UP setzen | 0,4–0,6 h | [Q11] |
| Gerät tauschen | 0,2–0,3 h | [Q11] |
| Leitung UP je m (inkl. Schlitzen) | 0,15–0,25 h/m | [Q11] |
| Verteilerfeld bestücken (je Reihe) | 1,5–2,5 h | [Q11] |
| FI/LS einbauen + prüfen | 0,2–0,3 h | [Q11] |
| E-Check je Stromkreis | 0,15–0,25 h | [Q11] |
| Komplettsanierung 120 m² EFH | 80–100 h, 5–10 Arbeitstage | [Q10] |

---

## 5. Kosten — mit Quellen und Spannen

**Vorab:** Es gibt keine amtliche Preisstatistik. Die folgenden Bänder stammen aus Fachbetriebs-, Preisportal- und Kalkulationsquellen und weichen regional um 30–50 % ab. Drei Angebote sind Pflicht, nicht Kür.

### 5.1 Einzelpositionen

| Position | Preis (brutto, sofern Quelle nicht anders sagt) | Quelle |
|---|---|---|
| Stundensatz Geselle | 55–85 €/h; Meister Ballungsraum bis 115 €/h | [Q11] |
| **Steckdose nachrüsten**, UP, vorhandener Stromkreis | **80–150 €** | [Q11] |
| Steckdose/Schalter tauschen | 60–120 € | [Q11] |
| Steckdose UP, vorhandener Kanal | 159–269 € | [Q5] |
| Steckdose UP, neue Leitung | 269–539 € | [Q5] |
| Neue Leitung vom Verteiler | 469–809 € | [Q5] |
| Leitung UP je m (inkl. Schlitzen/Verputzen) | 20–45 €/m | [Q11] |
| Leitung Aufputz je m | 8–15 €/m | [Q11] |
| **FI einzeln** nachrüsten (Typ A, freier Platz) | **150–350 €** | [Q12] |
| FI-Gruppen 2–4 im EFH | 400–800 € | [Q12] |
| FI-Gerät Typ A | 20–80 € | [Q12] |
| FI/LS-Kombi je Stromkreis | 30–80 € | [Q12] |
| **Unterverteilung** Standard | **480–960 €** (Rucker) / 500–1.200 € (elektriker.org) | [Q10][Q27] |
| Unterverteilung vollständig neu | 1.200–2.500 €; Altbau mehr | [Q27] |
| Umklemmen je vorhandenem Stromkreis | 40–80 € | [Q27] |
| Prüfung + Prüfprotokoll | 100–300 € | [Q27] |
| **Zählerschrank EFH**, 1 Zählerplatz | **1.490–2.380 €** | [Q10] |
| Zählerschrank + 3-Phasen-Aufrüstung („Stufe 1") | 1.500–3.000 € | [Q14] |
| Überspannungsschutz nachrüsten | 150–600 € | [Q27] |
| E-CHECK Wohnung / EFH | 80–150 € / 100–250 € | [Q11] |
| E-CHECK München (Regionalspanne) | 300–660 € | [Q10] |
| Wallbox 11 kW inkl. Installation | 1.200–2.500 €; Zuleitung 13–40 €/m | [Q28] |
| **Komplettsanierung Elektro** | **90–150 €/m²** (Rucker); 80–130 €/m² (clean-invoice) | [Q10][Q11] |
| EFH 120 m² komplett | 8.000–18.000 € | [Q14][Q10] |

### 5.2 Rechenbeispiel (sourced, nicht geschätzt)

Küchenmodernisierung, 6 neue Steckdosen, 8 m Leitung UP, 2 Lichtauslässe, Herdanschluss prüfen — Beispielrechnung von clean-invoice [Q11]:

- 6 × 0,5 h + 8 × 0,2 h + 2 × 0,4 h + 0,8 h = **6,2 h**
- 6,2 h × 70 €/h = **434 €**
- Material 120 € EK × 1,2 = **144 €**
- Anfahrt **35 €**
- **Summe ca. 613 € netto / ca. 730 € brutto**

### 5.3 Was den Preis wirklich treibt

1. **Zustand der Leitung**, nicht die Anzahl der Dosen: fehlt der PE, ist die Dose kein 100-€-Job, sondern ein neuer Stromkreis [Q10][Q12].
2. **Wandmaterial:** Beton vs. Ziegel vs. Porenbeton; „Leitung UP je m" schwankt um Faktor 1,7 [Q11].
3. **Zugänglichkeit:** ausgeräumte Baustelle vs. bewohnte Wohnung.
4. **Verteilerreserve:** fehlt Platz, kommen 300–800 € für einen neuen Verteiler hinzu [Q12].
5. **Region:** München 70–115 €/h, Ostdeutschland teils 40–55 €/h [Q11].

---

## 6. Ablauf mit dem Elektriker (7 Schritte)

| # | Schritt | Was du vorbereitest | Ergebnis / Nachweis |
|---|---|---|---|
| 1 | **Vorgespräch** (30–60 min, Erfahrungswert) | Baujahr, Fotos vom Verteiler, Raumbedarf, geplante Großverbraucher (WP, Wallbox, PV) | Hausaufgabenliste, Termin für Prüfung |
| 2 | **Bestandsaufnahme / E-CHECK** | Zugang zu allen Räumen, Verteiler frei | Messprotokoll mit Mängelliste [Q8][Q16] |
| 3 | **Plan Raum für Raum** | RAL-Raumplaner, Möbelplan, Anzahl Dosen, Leerrohre | Ausstattungsliste, Stromkreisverzeichnis [Q9] |
| 4 | **Angebot mit Positionen** | Vergleichsangebote, Eigenleistungsabgrenzung schriftlich | Positionen nach Menge × Preis, keine Pauschale [Q10][Q11] |
| 5 | **Rohinstallation** | Schlitze/Dosen nach Vorgabe, Baufreiheit, Strom für Geräte | Fotos jeder Wand, Leitungsweg dokumentiert [Q10] |
| 6 | **Prüfung DIN VDE 0100-600** | Termin vor Inbetriebnahme | Prüfprotokoll: Besichtigen, Erproben, Messen; mind. 1 MΩ Isolation [Q17] |
| 7 | **Abnahme + Doku** | Mängelliste, Restzahlung erst nach Protokoll | Prüfprotokoll, Stromlaufplan, Fotos, Rechnungen; Gewährleistung 5 Jahre bei Bauwerk (BGB § 634a, Frist ab Abnahme) [Q36][Q17] |

**Terminlogik, die Geld spart:**
- **Elektro-Rohinstallation vor Putz und Estrich.** Diese Reihenfolge ist zwingend; „Kabel nach dem Putz" bedeutet stemmen, drecken, zweimal zahlen [Q10].
- **Zählerantrag/Anmeldung** macht der eingetragene Betrieb — nicht du [Q1][Q10].
- **Stromausfall** beim Verteiler-Tausch: Kühlgeräte vorher leeren, Zeitfenster schriftlich zusagen lassen [Q27].
- **Eigenleistung** nur, wenn der Betrieb sie vorher abnimmt und der Leitungsweg von ihm festgelegt ist [Q10][Q15].

**Was du am Ende in der Hand halten musst:**
1. Prüfprotokoll nach DIN VDE 0100-600 [Q17]
2. Stromlaufplan + beschrifteter Verteiler [Q8]
3. Fotos aller Wände mit Maßband
4. Rechnungen getrennt nach Lohn/Material (für § 35a EStG) [Q27]
5. Unterschriebenes Abnahmeprotokoll mit Mängelfristen

---

## 7. Acht Pfusch-Bilder — erkennen, bevor es brennt

### 1. Klassische Nullung weiterbetrieben / Schuko an zweiadriger Leitung
**Symptom:** nur zwei Adern, PE fehlt oder ist in der Dose auf N gebrückt; neue Schuko-Dose am alten Kreis.
**Warum gefährlich:** bricht der PEN, liegen 230 V auf dem Gehäuse [Q2]. Die klassische Nullung ist seit 1973 für Neuanlagen verboten, ein PEN unter 10 mm² Cu ebenfalls; an solchen Stromkreisen dürfen keine neuen Steckdosen angeschlossen werden [Q2][Q5].
**Im Video:** „das sind noch alles alte 2-adrige Leitung, da sind teilweise auch gar keine Schutzleiter verdrahtet" [Q3, 01:20–01:25]; „wer sowas so hinterlässt, dem sollten wir eigentlich den Schein wegnehmen" [Q3, 03:09–03:13].
**Was tun:** Stromkreis erneuern (stemmen), Aufputzkanal als Kompromiss, oder Verteiler/Stromkreis durch Fachbetrieb neu aufbauen [Q5].

### 2. FI eingebaut, aber nicht angeschlossen
**Symptom:** RCD im Verteiler, aber kein Schutz — Testtaste löst nicht aus, oder Gerät ist überbrückt.
**Im Video:** „jeder FI-Schalter ist halt da, aber ist halt nicht angeschlossen" [Q3, 02:24–02:28].
**Was tun:** FI-Testtaste drücken (2×/Jahr) [Q8]; löst nicht aus → Fachbetrieb, Anlage stilllegen lassen.

### 3. Querschnitt oder Absicherung passt nicht zum Verbraucher
**Symptom:** 2,5 mm² an 50 A, 1,5 mm² am Durchlauferhitzer, Herd an einer Sicherung.
**Warum:** 1,5 mm² trägt bei A1/A2 16,5 A — mehr nicht [Q18]. Ein Durchlauferhitzer zieht 20–32 A [Q3, 02:15–02:24].
**Was tun:** Absicherung auf Leitung abstimmen (lassen), nicht umgekehrt.

### 4. Klemmstelle in der Wand statt in einer zugänglichen Dose
**Symptom:** Kabel verschwindet in der Wand, kommt an anderer Stelle wieder, keine Dose dazwischen; Lüsterklemme einbetoniert.
**Warum:** DIN VDE 0100-520, Abschnitt 526.5 verlangt zugängliche bzw. wartungsfreie Verbindungen; der Fachartikel diskutiert genau den Streit, ob eine Klemme „wartungsfrei" ist [Q29].
**Was tun:** Dose setzen lassen; jede unsichtbare Klemmstelle ist ein späterer Fehlersuche-Albtraum.

### 5. Leitung außerhalb der Installationszone / diagonal
**Symptom:** Kabel kreuzt die Wand schräg, liegt 2 m neben der Tür auf 1,10 m Höhe, kein senkrechter Strang zur Dose.
**Warum:** außerhalb der Zonen besteht Bohrgefahr; die Norm existiert genau dafür [Q23][Q24].
**Was tun:** Leitungsweg vor Putz abnehmen, Fotos; nachträglich nur mit Leitungssucher arbeiten.

### 6. Schlitz zu tief oder waagerecht durch die Wand
**Symptom:** 60-mm-Dose in 115-mm-Wand, waagerechter Schlitz über die ganze Wand, Schlitz direkt an der Wandöffnung.
**Warum:** ohne Nachweis max. 30 mm Tiefe, keine waagerechten Schlitze bis 175 mm Wanddicke, max. 6 % Schwächung, 115 mm Abstand zu Öffnungen [Q21].
**Was tun:** vor dem Stemmen Wandaufbau und Statik klären; im Zweifel Aufputz oder Vorsatzschale.

### 7. Aluminiumleitung mit Kupfer verklemmt
**Symptom:** silbrige Adern, weiche Oberfläche, Mischverbindung mit Cu.
**Warum:** Alu verformt sich kalt, Klemmstellen werden locker → Übergangswiderstand, Brand [Q2][Q5]. Alu-Leitungen sind laut Fachbetrieb zu ersetzen [Q10].
**Was tun:** keine Mischklemmen; Stromkreis erneuern.

### 8. Leitung in der Dämmung ohne Neubewertung
**Symptom:** Kabel liegt in der aufgedoppelten Dämmung, zusätzlich in einem Rohr mit anderen Leitungen, und ist weiter mit B16 abgesichert.
**Warum:** Leitungen in wärmegedämmten Wänden fallen in Verlegeart **A1/A2** — das ist der ungünstigste Fall [Q30]. Bei 1,5 mm² bleiben 16,5 A; Häufung und beidseitige Dämmung fressen die Reserve.
**Was tun:** Verlegeart und Häufung durch Fachbetrieb bewerten lassen, ggf. Querschnitt erhöhen.

### Bonus: kein Prüfprotokoll
**Symptom:** „läuft doch", keine Messung, kein Stromlaufplan.
**Warum:** Die Erstprüfung ist bei Neu/Änderung Pflicht und umfasst 16 Sichtprüfungspunkte, Isolationsmessung (min. 1 MΩ), Schutzleiterdurchgängigkeit, RCD-Test, Schleifenimpedanz [Q17]. Ohne Protokoll fehlt der Nachweis gegenüber Versicherung und Käufer [Q14].

---

## 8. Sinnvolle Ausstattung heute

| Thema | Empfehlung | Zahl / Quelle |
|---|---|---|
| **Steckdosen** | RAL-Stufe 2 statt Norm-Minimum; Küche + Arbeitsfläche separat zählen | Tabelle §4.3 [Q7] |
| **Stromkreise** | jeder Großverbraucher separat; 20 % Reserve im Verteiler | [Q22][Q9] |
| **Leerrohre** | in jeden Raum mind. 1 Leerrohr ≥ M25 für Netzwerk; EDV und Starkstrom **nicht** in dasselbe Rohr | [Q26, 06:59]; Kommunikationsverteiler je Wohnung nach DIN 18015-1 [Q35] |
| **Netzwerk** | CAT-Kabel in jeden Wohnraum: dicke Altbauwände sind der WLAN-Killer | [Q15] |
| **Verteiler** | mind. 3-reihig (Einraum) / 4-reihig (Mehrraum), 12 TE je Reihe; beschriftet | [Q35][Q8] |
| **Zählerschrank** | 1,4 m × 1,2 m, **20 % Reserve**; heute oft zu klein für WP/PV/Wallbox | [Q9] |
| **FI** | 30 mA für alle Steckdosenkreise; FI/LS je Kreis für Selektivität | [Q12] |
| **Überspannungsschutz** | Typ 2 im Zählerschrank; Pflicht nach DIN VDE 0100-443, wenn Risikoanalyse es fordert — bei Neu/Erweiterung faktisch Standard | [Q31][Q9] |
| **Wallbox** | eigener 3-phasiger Stromkreis; >4,6 kW dreiphasig; >12 kW Zustimmung Netzbetreiber; Anmeldepflicht besteht | [Q13] |
| **Rauchmelder** | Pflicht in allen 16 Ländern, Details in der Landesbauordnung (Schlafräume + Rettungswege) | [Q32] |

**Wallbox-Vorbereitung konkret:** Leerrohr vom Zählerplatz zum Stellplatz, eigener Stromkreis, Platz im Verteiler, Zuleitung nach Berechnung (13–40 €/m) [Q28]. Anmeldung beim Netzbetreiber ist Pflicht; eine Zustimmung wird erst über 12 kW gebraucht [Q13].

---

## 9. Quellen

**Typ:** G = Gesetz/Verordnung, N = Norm/Fachverlag, V = Verband/Initiative, F = Fachbetrieb/Fachblog, P = Preisportal, C = Community, Y = Video.

| # | Quelle | Typ | Geprüft |
|---|---|---|---|
| Q1 | NAV § 13 (Niederspannungsanschlussverordnung), https://www.gesetze-im-internet.de/nav/__13.html | G | Volltext gelesen; Abs. 2 Satz 4/5 wörtlich |
| Q2 | Wikipedia „Nullung" (Weiterleitung klassische Nullung), https://de.wikipedia.org/wiki/Klassische_Nullung | C | Volltext; 1973, PEN, 10 mm², DDR-Alu |
| Q3 | Step by Step Elektro, „Schwerer Elektro Pfusch Teil 1 – Brandgefährlich", https://www.youtube.com/watch?v=dW-Sf-yaEBQ (25.01.2023) | Y | Auto-Untertitel geladen, Zeitmarken 01:20, 01:59, 02:24, 03:09 |
| Q4 | r/Elektroinstallation, „Altbau Verkabelung", https://www.reddit.com/r/Elektroinstallation/comments/1twh4or/ | C | Thread im Browser gelesen: „klassische Nullung. War bis 1973 erlaubt." |
| Q5 | Alboush Elektrotechnik (Elektromeister, HWK Münster), „Steckdosen nachrüsten im Altbau", https://alboush-elektro.de/blog/steckdosen-nachruesten-altbau-kosten (21.01.2026) | F | Volltext; Preise, Nullung, Alu |
| Q6 | DIN Media, DIN 18015-2:2021-10 (Inhaltsverzeichnis/Pressemitteilung), https://www.din.de/de/din-und-seine-partner/presse/mitteilungen/wie-viele-steckdosen-pro-raum-1230444 | N | Existenz/Ausgabe; Volltext kostenpflichtig |
| Q7 | ASVENDO Fachwissen, „DIN 18015-2 Mindestausstattung und RAL-RG 678", PDF, https://asvendo.de/cdn/shop/t/90/assets/asv-din-18015-mindestausstattung.pdf (Stand 12.09.2026) | N (Sekundärauszug) | Volltext; Raumwerte, Stromkreise, Verteiler |
| Q8 | Initiative ELEKTRO+, „Kontrollieren Sie Ihre elektrische Anlage", https://www.elektro-plus.com/sicherheit/elektroinstallation-in-wohngebaeuden/kontrolle-der-anlage | V | Volltext; Checkliste, Schraubsicherung vor 1979, Bakelit 50 Jahre |
| Q9 | Initiative ELEKTRO+, „Ausstattungsumfang einer zeitgemäßen Elektroinstallation", https://www.elektro-plus.com/elektroplanung/modernisierung-elektroinstallation/ausstattungsumfang | V | Volltext; 1,4 × 1,2 m, 20 % Reserve, RAL-Stufen |
| Q10 | Rucker Elektro (München), „Leitungen im Altbau erneuern", https://rucker-elektro.de/blog/leitungen-im-altbau-erneuern (01.10.2026) | F | Volltext; 90–150 €/m², 80–100 h, Zählerschrank 1.490–2.380 € |
| Q11 | clean-invoice, „Elektriker Kosten & Kalkulation", https://www.clean-invoice.com/elektriker/kosten-und-kalkulation-elektriker (22.07.2026) | P | Volltext; Stundensatz, Positionen, Richtzeiten, Rechenbeispiel |
| Q12 | Listando, „FI-Schalter nachrüsten: Kosten 2026", https://www.listando.com/de-de/elektriker/fi-schalter-nachruesten-kosten | P | Volltext; 150–350 / 400–800 / 800–2.500 €, Gerätepreise |
| Q13 | Initiative ELEKTRO+, „Technische Anforderungen an Elektroinstallationen für Ladeeinrichtungen", https://www.elektro-plus.com/elektromobilitaet/technische-anforderungen | V | Volltext; 4,6 kW, 12 kW, Anmeldepflicht |
| Q14 | Betrivo, „Neue Elektrik Kosten", https://betrivo.de/kosten/neue-elektrik | P | Volltext; 3 Stufen, Prüfprotokoll, § 81 VVG |
| Q15 | r/germany, „Do-it-yourself home renovation work in Germany", https://www.reddit.com/r/germany/comments/1ftp6lx/ | C | Thread gelesen; „prepare … only he is allowed to connect" |
| Q16 | Initiative ELEKTRO+, „Prüfung und Mängelbeseitigung an bestehenden elektrischen Anlagen", https://www.elektro-plus.com/elektroplanung/bestandsschutz/pruefung-und-maengelbeseitigung | V | Volltext; Besichtigen/Messen/Erproben, Prüffristen, Mängelanzeige |
| Q17 | WEKA, „Erstprüfung nach DIN VDE 0100-600 korrekt durchführen", https://www.weka.de/elektrosicherheit/erstpruefung-nach-din-vde-0100-600 (28.04.2026) | N | Volltext; wer prüfen darf, 16 Sichtpunkte, 1 MΩ, Messreihenfolge |
| Q18 | ElektrikerWissen.de, „Mindestquerschnitt für Steckdosenstromkreise", https://www.elektrikerwissen.de/leitungsquerschnitt-fuer-steckdosenstromkreise (25.01.2024) | F | Volltext; 1,5 mm², Iz-Werte, kein 2,5-Zwang |
| Q19 | DGUV Vorschrift 3, PDF, https://publikationen.dguv.de/widgets/pdf/download/article/1052 | G (UVV) | § 2 Abs. 3, § 3 Abs. 1 wörtlich |
| Q20 | elektrikforum.de, „Was ist erlaubt, was verboten (für einen Laien)", https://www.elektrikforum.de/threads/was-ist-erlaubt-was-verboten-fuer-einen-laien.16845/ (02.11.2011) | C | Thread gelesen; Zitat kaffeeruler |
| Q21 | Elektropraktiker, „Statikbetrachtungen für nachträgliches Schlitzen in gemauerten Wänden", https://elektropraktiker.de/fachartikel/detail/statikbetrachtungen-fuer-nachtraegliches-schlitzen-in-gemauerten-waenden?p=all (ep 3/2015) | N | Volltext; 30 mm, 175 mm, 6 %, 115 mm, 0,4 m |
| Q22 | sanier.de, „Wie viele Steckdosen verträgt ein Leitungsschutzschalter?", https://www.sanier.de/elektroinstallation/wie-viele-steckdosen-vertraegt-ein-leitungsschutzschalter (11.07.2024) | F | Volltext; Liste der separat abzusichernden Geräte |
| Q23 | Wikipedia „Installationszone", https://de.wikipedia.org/wiki/Installationszone | C (Normauszug) | Volltext; 15–45 cm, 10–30 cm, 105 cm, 100–130 cm |
| Q24 | Gira, „Elektroinstallationszonen Regeln nach DIN 18015-3", https://gira.de/g-pulse-magazin/bauplanung/installationszonen-elektro | F (Hersteller) | Volltext; 30 cm/20 cm, Unterputz, Bad |
| Q25 | Die Elektromeister, „Elektroinstallation Unterputz … KOMPLETTE Anleitung mit Normenbezug", https://www.youtube.com/watch?v=xHrnbuAn-iY (02.02.2025) | Y | Untertitel; 10:08–10:54 (1,5 m / 15 cm), 14:07–14:26 (30 cm) |
| Q26 | Die Elektromeister, „Leerrohr Installationsrohr richtig verlegen", https://www.youtube.com/watch?v=hM6Cw8XhSgI (20.07.2025) | Y | Untertitel; 08:20–08:44 Zonen, 06:59 EDV/Starkstrom |
| Q27 | elektriker.org, „Sicherungskasten erneuern Kosten", https://www.elektriker.org/magazin/sicherungskasten-erneuern-kosten-202616842 | P | Volltext; 500–1.200 / 1.200–2.500 / 40–80 € je Kreis / Prüfung 100–300 € |
| Q28 | Listando, „Was kostet eine Wallbox?", https://www.listando.com/de-de/elektriker/wallbox-kosten (20.07.2026) | P | Volltext; 1.200–2.500 €, 13–40 €/m |
| Q29 | Elektropraktiker, „Lösbare Verbindungen in Abzweigdosen", https://www.elektropraktiker.de/fachartikel/detail/loesbare-verbindungen-in-abzweigdosen (ep 11/2007) | N | Volltext; Zugänglichkeit/wartungsfreie Klemme, VDE 0100-520 |
| Q30 | Schneider/Planungskompendium, „Bestimmung des Leiterquerschnittes … nach Verlegeart", https://de.electrical-installation.org/dewiki/Bestimmung_des_Leiterquerschnittes_von_Kabeln_und_Leitungen_nach_ihrer_Verlegeart | N (Herstellerfachbuch) | Tabelle gelesen: gedämmte Wand = A1/A2 |
| Q31 | WEKA, „DIN VDE 0100-443: Worauf Sie jetzt achten müssen", https://www.weka.de/elektrosicherheit/din-vde-0100-443/ | N | Volltext; SPD-Pflicht, Typ 2 |
| Q32 | Rauchmelder retten Leben, „Rauchmelderpflicht in allen 16 Bundesländern", https://www.rauchmelder-lebensretter.de/rauchmelderpflicht/ | V | Volltext; Landesbauordnungen |
| Q33 | r/Elektroinstallation, „Kosten Elektrik im Altbau", https://www.reddit.com/r/Elektroinstallation/comments/1txcbt7/ | C | Thread gelesen; 15.000 €/60 m², 20.000 € bei Eigenleistung Schlitzen |
| Q34 | elektro-plus, „Wann Hausbesitzer ihre Elektroanlage modernisieren sollten", https://www.elektro-plus.com/presse/wann-hausbesitzer-ihre-elektroanlage-modernisieren-sollten (28.05.2026) | V | Volltext; Bestandsschutz, Wärmepumpe, E-CHECK |
| Q35 | elektro.net, „Elektrische Anlagen in Wohngebäuden – Teil 2: Art und Umfang der Mindestausstattung", https://www.elektro.net/120701/teil-2-art-und-umfang-der-mindestausstattung/ (06.10.2021) | N | Volltext; 3-/4-reihiger Verteiler, 12 TE, Kommunikationsverteiler |
| Q36 | BGB § 634a (Verjährung), https://www.gesetze-im-internet.de/bgb/__634a.html | G | Volltext; 5 Jahre bei Bauwerk, Fristbeginn Abnahme |

**Anzahl geprüfter Quellen: 36** — 3 Gesetz/UVV (Q1, Q19, Q36), 8 Norm/Fachverlag (Q6, Q7, Q17, Q21, Q29, Q30, Q31, Q35), 6 Verband/Initiative (Q8, Q9, Q13, Q16, Q32, Q34), 5 Fachbetrieb/Fachblog (Q5, Q10, Q18, Q22, Q24), 5 Preisportal (Q11, Q12, Q14, Q27, Q28), 6 Community/Referenz (Q2, Q4, Q15, Q20, Q23, Q33), 3 Video (Q3, Q25, Q26).

### Was ich selbst geprüft habe (Prüftiefe)

- **Volltext gelesen und zitiert:** Q1, Q2, Q3 (Untertitel), Q5, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q16, Q17, Q18, Q19, Q21, Q22, Q23, Q24, Q27, Q28, Q29, Q30, Q31, Q32, Q34, Q35, Q36.
- **Nur Thread/Seite geöffnet, Zitat stichprobenartig:** Q4, Q15, Q20, Q33.
- **Nur Existenz/Ausgabe/TOC geprüft:** Q6 (DIN 18015-2:2021-10; Normtext kostenpflichtig).
- **Video-Zeitmarken** stammen aus automatischen Untertiteln (±10 s) und sind keine frame-genauen Angaben; Zitate können ASR-Fehler enthalten.

---

## 10. Unbelegt / offen

1. **„8 Steckdosen im Wohnzimmer sind DIN-Pflicht"** — falsch. DIN-Stufe 1 nennt 4 (bis 20 m²); 8 ist RAL-Stufe 2 [Q7][Q5]. Die Aussage findet sich trotzdem in einem Meisterbetrieb-Ratgeber.
2. **„Bestandsschutz heißt, ich darf nichts ändern"** und **„Bestandsschutz heißt, alles darf bleiben"** — beides zu einfach. Eine normgerecht errichtete Anlage darf weiterbetrieben werden, aber jede Erweiterung/Änderung löst die aktuellen Regeln aus (NAV § 13; ELEKTRO+) [Q1][Q34].
3. **„Eigenleistung spart 50 %"** — keine Quelle. Ein Reddit-Fall nennt 5.000 € von 15.000 € (33 %) für Vorarbeiten [Q33]; Rucker sagt nur „spürbarer Teil" [Q10]. Belastbare Studie: keine gefunden.
4. **„Neuer Verteiler macht die Anlage sicher"** — nein: fehlt der Schutzleiter, schützt der FI nicht wie vorgesehen; Rucker schreibt das ausdrücklich [Q10].
5. **„FI ist seit 2009 Pflicht"** — Fachbetriebe nennen 1984 (Bad) und 2009 (alle Steckdosen) [Q10]. Die Normzäsuren der DIN VDE 0100-410 werden unterschiedlich datiert (2007 für ≤ 20 A, 2018 für ≤ 32 A); **belegt ist hier nur die aktuelle Anforderung: 30 mA, ≤ 32 A** [Q12].
6. **Prüffristen für selbstgenutzte EFH** — keine gesetzliche Pflicht gefunden; ELEKTRO+ empfiehlt wiederkehrende Prüfung, DIN VDE 0105-100 nennt für Wohnungen „z. B. 10 Jahre" [Q16]. Das ist eine Empfehlung, keine Vorschrift.
7. **Kosten** — es gibt keine amtliche Statistik; alle Bänder sind Marktbeobachtungen von Portalen und Betrieben. Die Streuung zwischen Q10 (München) und Q27 (bundesweit) beträgt bis zu 100 %.
8. **„Asbest nur bei Baujahr vor 1993"** — maßgeblich ist der **Baubeginn**, nicht das Baujahr; Details im Schwester-Playbook.

---

## 11. Die 10 Regeln (zum Mitnehmen)

1. **Nicht anfassen, was unter Spannung steht.** Anschließen, absichern, messen: Fachbetrieb (NAV § 13 Abs. 2).
2. **Erst E-CHECK, dann Angebot.** 80–660 € sparen fünfstellige Fehlentscheidungen.
3. **Zweiadern = Stopp.** Keine neue Schuko-Dose an klassischer Nullung.
4. **Verteiler vor Wand.** Wenn die Leitungen in Ordnung sind, ist der Kasten der günstigste Sicherheitsgewinn.
5. **Fotos, Fotos, Fotos.** Jede offene Wand mit Maßband.
6. **Zonen einhalten.** 15–45 cm waagerecht, 10–30 cm senkrecht, 15 cm von der Kante.
7. **Schlitz nie tiefer als 30 mm** ohne Statiknachweis.
8. **Jeder Großverbraucher ein eigener Stromkreis.**
9. **Leerrohre und 20 % Reserve** jetzt, nicht später.
10. **Prüfprotokoll oder keine Abnahme.** Ohne Messung keine Sicherheit, ohne Protokoll keine Gewährleistung.

## Fehlerkatalog aus der Praxis (10 Videos, Stand 09.11.2026)

Jeder Punkt ist im Video belegt (`references/fehlerkatalog.json`); Zeitmarke = Fundstelle im Transkript
(`references/transkripte/`). Erkannt wird vom Laien — **behoben wird vom eingetragenen Installationsbetrieb**
(NAV § 13 Abs. 2).

**Zuleitung und Netzsystem**
- Zuleitung ohne durchgehenden Schutzleiter (z. B. 6 mm² aus dem Keller, nur L und N): das ist **kein
  TN-S- bzw. TN-C-S-System**, die Anlage hat keinen wirksamen PE. Nicht benutzen, nicht „läuft ja"
  (dW-Sf-yaEBQ 00:00:26).
- Zuleitung darf nicht direkt auf Leitungsschutzschalter und Kammschiene geklemmt werden: definierter
  **Einspeiseklemmenblock**, davor **Hauptleitungsschutz** (Leitungsschutz nach DIN VDE 0100-430)
  (dW-Sf-yaEBQ 00:00:34).
- **PEN-Auftrennung nur einmalig**, danach PE und N durchgehend getrennt; alte zweiadrige Leitungen
  (2-adrig) haben keinen Schutzleiter, daran gehört keine Schutzkontaktsteckdose (dW-Sf-yaEBQ 00:01:00).

**Querschnitt und Absicherung**
- Strombelastbarkeit richtet sich nach Verlegeart (DIN VDE 0298-4): 6 mm² ist nicht mit 50 A
  abgesichert zulässig (dW-Sf-yaEBQ 00:01:46).
- Durchlauferhitzer zieht 20–32 A: eigener Stromkreis, **5×4 mm² oder 5×6 mm²**, RCD 30 mA; 5×2,5 mm²
  nur für einen Boiler, nicht für den Durchlauferhitzer (dW-Sf-yaEBQ 00:02:04).

**RCD/FI**
- „FI ist eingebaut" heißt nichts: nicht angeschlossene oder überbrückte RCDs sind **Deko** — Prüftaste
  und Messung zeigen es, nur der Fachbetrieb (dW-Sf-yaEBQ 00:02:25).
- **RCD 30 mA** für Steckdosenstromkreise; im Bad alle Stromkreise, Schutzbereiche 0–2 nach
  DIN VDE 0100-701 (dW-Sf-yaEBQ 00:02:04).
- RCD nicht nur pro Geschoss: **Aufteilung in mehrere RCD-Gruppen**, sonst legt ein Fehlerstrom ein
  ganzes Geschoss dunkel (eNpMPWvnWiI 00:06:51).

**Dosen, Adern, Klemmstellen**
- Abgeschnittener Schutzleiter: Gerät der **Schutzklasse I** läuft, aber der Körperschluss führt zum
  Stromschlag — Steckdose stilllegen (dW-Sf-yaEBQ 00:02:59).
- **Spannung auf dem PE** in der Dose = akute Gefahr, Anlage freischalten lassen (dW-Sf-yaEBQ 00:04:58).
- Abisolieren nur mit **Abisolierzange**; Seitenschneider kerbt die Seele, bei Litze **Aderendhülse**,
  sonst Bruch- und Erwärmungsstelle (dW-Sf-yaEBQ 00:03:34, 00:03:39).
- Eine **Brücke** ist kein zweiter Stromkreis: Aderzahl zählen, sonst wird der Klemmpunkt falsch
  gedeutet (dW-Sf-yaEBQ 00:03:48).
- **Aderreserve** in der Dose lassen (nachklemmen später), keine **lockere Klemmstelle**, keine Klemme
  in der Wand (eNpMPWvnWiI 00:12:11, 00:12:18).
- Altleitungen: **Isolationswiderstand ≥ 1 MΩ** ist die Prüfgrenze; Serien-/Wechselschaltung nicht
  „irgendwie" zusammenklemmen (dW-Sf-yaEBQ 00:03:20).
- **Try-and-error** ist kein Verfahren — ohne **Grundkenntnisse** und mit **Alleinarbeit (allein nicht zulässig)** endet das im Schaden; Stromlaufplan, Aufstellplan, Durchgangsmaße vorher
  (eNpMPWvnWiI 00:01:18, 00:04:40).

**Verteiler, Reserve, Kanäle**
- **Teilungseinheiten** mit Reserve planen: Platz für 1× dreipolig C16 (400 V Drehstrom) und
  mindestens 3× B16 für später (eNpMPWvnWiI 00:09:46).
- Kabelkanal nicht 20er, sondern **40er Kabelkanal bzw. 60×100** — Nachrüsten im zu kleinen Kanal endet als
  Aufputz-Flickerei (eNpMPWvnWiI 00:10:36).
- Zweite **Unterverteilung** in der **Elektroverteilung** (Garage/Außen) und **Außensteckdosen** und **Dreifachsteckdosen** von Anfang an vorsehen, statt
  Dreifach- auf Zweifachdosen zu reduzieren (sWXyiNADbFk 00:05:20, 00:09:01).
- Netzwerk: durchgehend **Leerrohr**, keine engen Knicke; PoE ersetzt kein Datenkabel (sWXyiNADbFk 00:12:23).

**Messen, prüfen, dokumentieren**
- **Zweipoliger Spannungsprüfer** (Duspol): L gegen N **und** L gegen PE messen, sonst bleibt ein
  PE-Fehler unentdeckt (eNpMPWvnWiI 00:13:59).
- Spannungsprüfer ist **kein Installationsmessgerät**: Isolations-, Schleifen- und RCD-Messung brauchen
  Prüfgeräte, die nur der Fachbetrieb hat (eNpMPWvnWiI 00:16:56).
- Stromkreise **kennzeichnen** (Kennzeichnung nach DIN VDE 0100-510, Abschnitt 514) — im Fehlerfall
  wird sonst der falsche Kreis abgeschaltet (eNpMPWvnWiI 00:15:07).

## Ergänzungen aus dem Video-Katalog (Nachtrag)

- **Lichtsteuerung**: DALI bzw. dimmbare Kreise vorsehen, **beleuchteter Spiegel** und Leuchten auf
  Kompatibilität prüfen — sonst wird die Szene nachträglich verkabelt (sWXyiNADbFk-10).
- **Fenstersensoren** (Fensterhersteller-Systeme) haben Erfahrungswerte mit hoher Ausfallquote im ersten
  Jahr (im Beispiel **30 % Ausschuss**): Dosen/Leitungen vorsehen, Systemwahl nach Erfahrungswerten, nicht
  nach Prospekt (sWXyiNADbFk-14).

## Begriffe und Normbezug (richtige Wortwahl)

- **Netzsysteme**: TN-S (PE und N durchgehend getrennt), TN-C (PEN statt PE+N), **TN-C-S** (PEN wird
  einmalig aufgetrennt, danach PE und N getrennt). Ein Bestand mit PEN ist kein TN-S.
- **Schutzmaßnahmen**: **RCD 30 mA** (umgangssprachlich FI), **Schutzklasse I** (Metallgehäuse braucht PE),
  **Körperschluss**, **Spannung auf dem PE**, Schutzbereiche 0–2 im Bad mit passender **IP-Schutzart**
  (DIN VDE 0100-701).
- **Leitung**: **Strombelastbarkeit** nach Verlegeart (DIN VDE 0298-4), Querschnitt 1,5/2,5/4/6 mm²,
  **Aderendhülse** bei Litze, **Litzenverletzung** durch Seitenschneider, **Kabelreserve**/**Aderreserve**.
- **Prüfen**: **Isolationsmessgerät**, **Isolationswiderstand ≥ 1 MΩ**, zweipoliger Spannungsprüfer
  (Duspol), Prüfung L–N **und** L–PE, Erstprüfung **DIN VDE 0100-600**, Kennzeichnung der Stromkreise
  (DIN VDE 0100-510, Abschnitt 514).
- **Verteiler**: **Teilungseinheiten**, Reserve für 1× dreipolig C16 + 3× B16, **Kammschiene**,
  **Einspeiseklemme**, Hauptleitungsschutz (DIN VDE 0100-430).
- **Verdrahtung**: **Serienschaltung** (zwei Schaltstellungen) vs. Wechselschaltung, **Brücke** statt
  zweitem Stromkreis, **Try-and-error-Verdrahtung** ist kein Verfahren.
- **Kanäle**: 20er Kanal reicht nicht, **40er bzw. 60×100** vorsehen.
### Weitere Video-Fehler (Elektro)

- **Abgerissene Ader in der Klemme** und **Kerben** von der Seitenschneider-Abisolierung: Leiter kürzen
  und mit Abisolierzange neu absetzen, sonst Bruch- und Erwärmungsstelle (dW-Sf-yaEBQ-10).
- **Beschriftung**: jede Sicherung mit **Sicherungsnummer** und Stromkreis kennzeichnen (Kennzeichnung nach
  DIN VDE 0100-510, Abschnitt 514); ohne Beschriftung wird im Fehlerfall der falsche Kreis abgeschaltet
  (eNpMPWvnWiI-14).
- **Netzwerk**: durchgehend **Cat.6/Cat.7** im Leerrohr, **Biegeradius** einhalten — ein geknicktes Kabel
  liefert PoE, aber keine Daten (sWXyiNADbFk-12).
- **Nicht jeder Verbraucher braucht einen eigenen Stromkreis**: „Steckdosen kann man nie genug haben"
  führt zu 14 Sicherungen für 14 Dosen (Werkstattgeräte wie Tischkreissäge/Bandsäge ausgenommen) — mehr
  Kosten und mehr Fehlerquellen statt mehr Sicherheit (eNpMPWvnWiI-06).
## Ergänzungen aus dem Video-Gegencheck (09.11.2026)

- **Lage vor Stückzahl**: Steckdose an jeder Raumecke und neben jeder Tür ist die Praxisregel, die
  Stückzahl-Tabelle ist die Untergrenze. *Erfahrungswert aus der Praxis, nicht belegt.*
- **Lampenauslass nicht direkt neben Schalter oder Steckdose** setzen; Vorhänge, Schränke und Betten
  vorher festlegen — sonst wird nach dem Streichen gespachtelt und neu gestrichen.
- **Bedienstellen planen**: in Räumen mit mehreren Ausgängen Taster an jeder Tür; Flur als ein Raum
  behandeln; Wechselschaltung nur an den Wegen, die wirklich benutzt werden.
- **Deckenventilator**: zwei Kanäle (Licht und Ventilator getrennt) und die Aufhängestelle in der
  Trockenbaudecke verstärken.
- **Schaltbare Steckdose** für LED-Streifen vorsehen — billiger und dauerhafter als jede Funklösung.
- **Schaumstoffstopfen in Gerätedosen** beim Spachteln und Tapezieren, sonst ist die Dose voll Mörtel.
- **LAN-Dose im Technikraum** für Wärmepumpe, Speicher und Wechselrichter — die Geräte werden
  ferngewartet, Funk ist im Keller keine Lösung.
- **Außen-Leerrohre** nicht nur für Garten, Bewässerung und Kamera legen, sondern auch für Rasenroboter,
  Garagentor, Klingel und Pool/Sauna.

## Nachtrag: FI-Aufteilung und Ausfallsicherheit (Kalt/Warm-Test 09.11.2026)

Der Vergleich mit einer Antwort ohne Wissensbasis hat gezeigt: Das Playbook war beim FI zu grob. Ergänzt:

- **Ableitströme summieren sich**: an einen 30-mA-RCD gehören in der Praxis **nicht mehr als etwa sechs
  Stromkreise** (Erfahrungswert, keine Normzahl). Viele Schaltnetzteile, lange Leitungen und alternde
  Elektronik bringen 10–15 mA zusammen — dann löst der RCD ohne Isolationsfehler aus.
- **Gliederung nach Verbraucher, nicht nach Geschoss**: kritische Kreise (Kühl-/Gefriergeräte, Router,
  Heizungssteuerung, Alarmanlage) getrennt führen, Licht/Flur separat. **RCBO (FI/LS) je kritischem Kreis**
  ist die sauberste Lösung — dann fällt nur dieser Kreis.
- **Typ richtig wählen**: Typ A ist Standard; Typ B ist für Wallbox, PV-Wechselrichter und Frequenzumrichter
  mit glattem Gleichfehlerstrom nötig. Bei vorgelagertem selektivem RCD (300 mA Typ S) Selektivität prüfen.
- **RCD ersetzt keinen Leitungsschutz**: Kurzschluss- und Überlastschutz bleiben eigene Aufgabe
  (DIN VDE 0100-430); ein FI schützt Personen, nicht die Leitung.
- **Prüfen statt glauben**: Auslösezeit und Auslösestrom werden gemessen (DIN VDE 0100-600), die Prüftaste
  am Gerät ist nur ein Funktionstest.

- **PEN-Auftrennung nach DIN VDE 0100-540**: Wo aus einem TN-C-System ein TN-S wird, muss der PEN an der
  vorgesehenen Stelle in PE und N getrennt werden — danach nie wieder verbinden. Ohne durchgehenden,
  getrennten Schutzleiter ist die Anlage kein sauberes TN-S-System.
