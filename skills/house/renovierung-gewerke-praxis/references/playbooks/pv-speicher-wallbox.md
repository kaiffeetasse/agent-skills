# PV + Speicher + Wallbox als Einheit — Auslegung, Anmeldung, Steuern, Kosten

> **Preisstand 09/2026.** Alle Preise sind Orientierungswerte inkl. MwSt. aus den genannten Quellen —
> regional verschieden, keine Angebote. Wer später damit rechnet, prüft sie neu.

**Zielgruppe:** Eigenheimbesitzer im Bestand, die Dach-PV, Batteriespeicher und Ladepunkt in **einem** Zug planen (statt dreimal einzukaufen).
**Stand:** 09.11.2026. Jede Zahl trägt eine Quellennummer [Q#]; die Quellen stehen mit URL, Typ und Prüftiefe in §11. Eigene Rechnungen sind als **eigene Rechnung** gekennzeichnet und ihre Annahmen stehen offen daneben.

> **Die eine Grenze, die alles andere bestimmt:** Der Netzanschluss ist ein einziger Anschlusspunkt. PV, Speicher, Wallbox und Wärmepumpe konkurrieren um dieselbe Leistung, denselben Zählerplatz und dieselbe Steuerbarkeit. Wer nacheinander kauft, zahlt den Zählerschrank zwei- bis dreimal und bekommt für den Speicher keinen § 14a-Rabatt, weil er beim ersten Antrag nicht mitgedacht war. Deshalb: **ein Lastenheft, ein Elektrofachbetrieb, ein Termin beim Netzbetreiber.**

---

## 1. In 60 Sekunden

1. **Die Einspeisevergütung trägt die Anlage nicht mehr.** Für Inbetriebnahme ab 01.08.2026 gibt es **7,70 ct/kWh** bis 10 kWp (Teileinspeisung), bei Volleinspeisung 12,22 ct/kWh [Q5]. Die Rendite kommt aus dem **Eigenverbrauch** — deshalb ist die Frage „wie viel kWp" immer die Frage „wie viel davon esse ich selbst".
2. **Steuerfrei und netto:** 0 % USt auf Lieferung **und** Installation von Modulen, wesentlichen Komponenten und Speichern bis **30 kWp** [Q6]; die Einnahmen sind einkommensteuerfrei bis **30 kWp je Wohn-/Gewerbeeinheit**, insgesamt **100 kWp** je Steuerpflichtigem [Q7].
3. **Der Speicher ist der teuerste Baustein mit dem schlechtesten Wirkungsgrad.** Obergrenze nach HTW Berlin: **1,5 kWh nutzbar je 1.000 kWh Jahresverbrauch** und **1,5 kWh je 1 kWp** [Q19]. Bei 10 kWp und 4.000 kWh Haushaltsstrom sind das **6 kWh** — nicht 15.
4. **Die Wallbox ist der günstigste Baustein** (Gerät 300–2.000 €, Installation 500–3.000 € [Q20]) — und der mit der klarsten Formalie: **jede** Wallbox vor Inbetriebnahme melden, ab **>12 kVA Summen-Bemessungsleistung** zusätzlich **Zustimmung** des Netzbetreibers (NAV § 19 Abs. 2) [Q8].
5. **Alles über 4,2 kW Bezugsleistung wird steuerbar** (§ 14a EnWG): Wallbox, Speicher, Wärmepumpe. Der Netzbetreiber darf auf **4,2 kW** dimmen, dafür gibt es Netzentgeltrabatt — Modul 1 pauschal rund **150 €/a**, 2025 zwischen 124 und 188 € je Region [Q16][Q15].

---

## 2. PV-Anlage: Auslegung in der Reihenfolge, die Geld spart

### 2.1 Zuerst der Verbrauch, dann die kWp

Die Anlagengröße folgt aus dem, was du selbst verbrauchst — nicht aus der Dachfläche und nicht aus dem Angebot des Verkäufers. Zwei Größen müssen zusammenpassen:

| Kenngröße | Was sie sagt | Faustregel |
|---|---|---|
| **Eigenverbrauchsquote** | Anteil der Erzeugung, der im Haus bleibt | steigt mit Speicher und mit Verbrauch am Tag |
| **Autarkiegrad** | Anteil des Verbrauchs, der vom Dach kommt | 25–30 % ohne Speicher, bis ~70 % mit Speicher [Q11] |

Finanztip rechnet für einen 4.000-kWh-Haushalt mit 5 kWp: **32,3 % Autarkie ohne Speicher, 62,8 % mit 5 kWh Speicher** — und gibt die Systemeffizienz des Speichers mit **85 %** an [Q15]. Das ist der belastbarste veröffentlichte Rechenweg, den ich gefunden habe, weil Annahmen und Ergebnis zusammen dastehen.

**Konsequenz für die Auslegung:** Wer 4.000 kWh verbraucht und 10 kWp baut, hat im Sommer mittags Strom im Überfluss und speist ihn für 7,70 ct/kWh ein [Q5]. Wie stark die Angebote für dasselbe Dach auseinanderliegen, zeigt ein Vergleichsvideo aus Oktober 2026: 10 kWp, 15 kWp und „ganzes Dach“ für denselben Kunden — mit dem Fazit, dass mehr Module nicht automatisch mehr Rendite bedeuten [Q31]. Wer zusätzlich ein E-Auto tagsüber lädt, verschiebt die Quote nach oben — das E-Auto ist der billigste „Speicher", den es gibt, weil es ihn schon gibt.

### 2.2 Spezifischer Ertrag: pro Region gemessen, nicht geschätzt

Werte aus **PVGIS v5.2** (EU Joint Research Centre, Strahlungsdatensatz PVGIS-SARAH2), 1 kWp, **35° Neigung, Süd**, 14 % Systemverluste, Dachmontage — über die PVGIS-API abgerufen, also reproduzierbar [Q22]:

| Standort | kWh/kWp·a | Standort | kWh/kWp·a |
|---|---|---|---|
| Hamburg | **952** | Frankfurt/M. | **1.041** |
| Berlin | **1.022** | München | **1.077** |
| Köln | **1.000** | Freiburg | **1.026** |

Die Spanne Nord–Süd beträgt rund **13 %** — deutlich weniger, als der Bauch glaubt. Für Wirtschaftlichkeitsrechnungen ist **1.000 kWh/kWp·a** eine saubere, leicht konservative Annahme für mitteldeutsche Lagen.

### 2.3 Dachausrichtung und Neigung: dieselbe Quelle, echte Zahlen

Ebenfalls PVGIS, Standort Köln [Q22]:

| Ausrichtung (35° Neigung) | kWh/kWp·a | | Neigung (Süd) | kWh/kWp·a |
|---|---|---|---|---|
| Ost | 803 | | 10° | 911 |
| Südost | 949 | | 15° | 940 |
| **Süd** | **1.000** | | **35°** | **1.000** |
| Südwest | 933 | | 45° | 999 |
| West | 783 | | 60° | 955 |
| Nord | 533 | | 70° | 899 |

Drei Dinge folgen daraus, die in Angeboten oft anders dargestellt werden:

- **Ost/West kostet rund 20 %, nicht 40 %.** Und es liefert morgens und abends — für den Eigenverbrauch oft wertvoller als die Mittagsspitze. Die flache Zahl „Süd = 100 %, Ost/West = 80 %" ist als Rechenannahme brauchbar, aber die konkrete Zahl liefert nur eine standortbezogene Simulation.
- **Flachdach ist kein Problem.** 10–15° verlieren gegenüber 35° nur 6–9 %. Bei Ost-West-Aufständerung auf dem Flachdach kommt die Neigung ohnehin selten über 15°.
- **Norddach ist wirtschaftlich tot** (533 kWh/kWp·a = 53 % von Süd): bei 7,70 ct/kWh sind das 41 €/kWp·a Erlös vor Betriebskosten. Wer das Norddach trotzdem belegt, macht es für den Eigenverbrauch (Mittags-/Abendverschiebung) und nicht für die Vergütung.

### 2.4 Verschattung: der Fehler, der erst nach der Montage auffällt

Verschattung ist **standort- und uhrzeitabhängig** und lässt sich nicht pauschal abschlagen. Was zählt:

- **Welche Fläche verschattet wann?** Kamin, Gaube, Nachbargebäude, Baum. Ein Baum wirft im Juni anderen Schatten als im Dezember — und die entscheidenden Monate für den Ertrag sind April bis September.
- **String vs. Modul:** Ein Schatten auf **einem** Modul zieht bei einfacher String-Verschaltung den ganzen String herunter. Abhilfe: **Moduloptimierer** oder **Mikrowechselrichter** an den betroffenen Modulen, oder die betroffene Fläche weglassen.
- **Prüfmittel:** Sonnenstandssonde/Schattenanalyse des Anbieters, nicht „das sieht gut aus". Lass dir die **Simulation mit Uhrzeit und Datum** zeigen und die verschatteten Module benennen.

> **Belegt ist hier nur der Mechanismus, nicht die Prozentzahl.** Welcher Ertragsverlust bei deinem Dach herauskommt, sagt die Simulation — jede Pauschalzahl („10 % für den Kamin") ist eine Vermutung. Siehe §12.

### 2.5 Modultechnik: was die Aufpreise wirklich kaufen

| Variante | Was sie technisch macht | Wann sinnvoll |
|---|---|---|
| **Full Black** (schwarze Rückseitenfolie, schwarzer Rahmen) | Optik; kein Ertragsvorteil | Sichtdach, Gestaltungswunsch, Denkmalumfeld |
| **Glas-Glas** | beidseitig Glas statt Folie: geringere Degradation, längere Garantie, besserer Brandschutz; teurer und schwerer | Anlagen, die 25+ Jahre laufen sollen; Aufdach mit hoher Schneelast |
| **Glas-Folie** (Standard) | leichter, günstiger | Regelfall im Bestand |
| **Bifazial** | Rückseitenertrag nur bei hellem Untergrund/Aufständerung | Freifläche; auf dem Schrägdach ohne Nutzen |

Belegt ist hier nur die **bauartspezifische Unterscheidung** (Glas-Glas vs. Glas-Folie, Zelltechnik LFP bei Speichern) [Q11]; die Preisaufschläge je Variante sind Angebotssache und stehen in §12 als unbelegt.

### 2.6 Wechselrichter: String, Hybrid oder Mikro

- **String-Wechselrichter** — der Regelfall. Ein Gerät für alle Module eines Dachs, ein MPP-Tracker je String. Günstig, robust, gut bei unverschatteten Flächen gleicher Ausrichtung.
- **Hybrid-Wechselrichter** — String-Wechselrichter mit Batterieanschluss auf der **DC-Seite**. Das ist heute der Standard für „PV + Speicher in einem Zug", weil der Speicher ohne zweite Umwandlung geladen wird. Fronius bietet dafür beim GEN24 Plus **PV Point** (Basis-Notstrom für einzelne Verbraucher) und **Full Backup** (ganzes Haus) [Q27]. HTW-Messungen zeigen: die **Umwandlungswirkungsgrade der Hybridwechselrichter** liegen im Labor im Mittel bei **97,6 %**, die Datenblätter behaupten **98,1 %** [Q17].
- **Mikrowechselrichter** — ein Gerät je Modul (oder je zwei). Sinnvoll bei starker Teilverschattung, bei mehreren Dachflächen mit unterschiedlicher Ausrichtung und beim Balkonkraftwerk. Teurer je kWp, dafür kein String-Risiko.
- **Unterdimensionierung:** Der Wechselrichter darf kleiner sein als die Modulleistung (Überbelegung), weil die Module die Nennleistung nur bei Idealbedingungen erreichen — die AC-Grenze ist in Deutschland ohnehin die Einspeisebegrenzung. Wird er zu klein gewählt, verliert man Mittagsspitzen; zu groß gewählt, zahlt man für Leistung, die nie ankommt.

**Merksatz:** Der Wechselrichter ist die Komponente mit der kürzesten Lebensdauer (10–15 Jahre, oft der erste Tausch). Ein Gerät mit **offenen Schnittstellen** (Modbus, API) kostet heute nichts extra und entscheidet später darüber, ob Wallbox und Wärmepumpe den Überschuss sehen.

### 2.7 Einspeisevergütung: Sätze, Degression, Direktvermarktung

Die Vergütung wird nicht jährlich neu verhandelt, sondern **halbjährlich um 1 % gesenkt** — zum 1. Februar und zum 1. August. Die BNetzA: „Seit 2024 werden die Fördersätze halbjährlich unter Verwendung eines festen Degressionssatzes bestimmt" [Q4]; im Tabellenwerk steht dazu der Degressionssatz **0,01** je Periode [Q5].

**Was für eine Inbetriebnahme ab 01.08.2026 gilt** (Teileinspeisung = Überschusseinspeisung; Volleinspeisung = alles ins Netz) [Q5]:

| Inbetriebnahme | ≤10 kWp (TE) | ≤40 kWp (TE) | ≤100 kWp (TE) | ≤10 kWp (VE) | ≤40/≤100 kWp (VE) |
|---|---|---|---|---|---|
| 01.02.–31.07.2025 | 7,94 | 6,88 | 5,62 | 12,60 | 10,56 |
| 01.08.2025–31.01.2026 | 7,86 | 6,80 | 5,56 | 12,47 | 10,45 |
| 01.02.–31.07.2026 | 7,78 | 6,73 | 5,50 | 12,34 | 10,35 |
| **01.08.–31.12.2026** | **7,70** | **6,66** | **5,44** | **12,22** | **10,24** |

**Rechenprobe, damit die Zahl nachvollziehbar ist** (eigene Rechnung auf Basis [Q1][Q2][Q5]):

```
Ausgangswert 2023 (§ 48 Abs. 2)      8,60 ct/kWh
× 0,99^6  (6 Halbjahresschritte bis 08/2026)   =  8,0967 ct/kWh   → "anzulegender Wert"
− 0,40 ct   (§ 53 Abs. 1 Nr. 2 EEG, gilt für Solar)  =  7,6967 ct/kWh
gerundet veröffentlicht (BNetzA)                =  7,70 ct/kWh
```

Deshalb steht im Gesetzestext etwas anderes als in der Veröffentlichung: § 48 Abs. 2 nennt in der konsolidierten Fassung **8,51 / 7,43 / 7,64 ct/kWh** — das ist der Stand nach **einer** Degressionsstufe [Q1]. Maßgeblich für dich ist **nicht** der Gesetzestext, sondern die zum Inbetriebnahmemonat veröffentlichte Tabelle der BNetzA [Q4][Q5]. Wer aus dem Gesetzestext 8,51 ct ableitet, rechnet sich 0,81 ct/kWh zu reich — bei 8.000 kWh Einspeisung sind das **65 €/a**.

**Volleinspeisung** ist die Alternative für Dächer, auf denen du nichts selbst verbrauchst: § 48 Abs. 2a erhöht den anzulegenden Wert um **4,8 ct/kWh** (≤10 kWp) bzw. 3,8 / 5,1 ct (bis 40 / 100 kWp) [Q1]. Bei 10 kWp sind das 12,22 statt 7,70 ct — **+59 %**. Das lohnt nur, wenn der Eigenverbrauch nahe null ist, weil du für Volleinspeisung auf jede Selbstnutzung verzichtest. Zwei Anlagen auf einem Dach (eine je Messung) sind möglich, aber an Bedingungen geknüpft ([Q1] Abs. 2a Satz 2).

**Drei Dinge, die die Vergütung kappen:**

- **Negative Börsenpreise:** „Für Zeiträume, in denen der Spotmarktpreis negativ ist, verringert sich der anzulegende Wert auf null" (§ 51 Abs. 1) [Q3]. **Ausnahme:** Anlagen **unter 100 kW** sind davon ausgenommen, bis zum Ablauf des Kalenderjahres, in dem sie ein **intelligentes Messsystem** bekommen haben (§ 51 Abs. 2 Nr. 1) [Q3]. Praktisch heißt das: Mit dem Smart Meter kommt die Regel — und der Vergütungszeitraum wird um diese Zeiten verlängert [Q13].
- **Kein iMSys, keine volle Einspeisung:** Anlagen ab **7 kWp**, die ab **25.02.2025** in Betrieb gehen, müssen iMSys und Steuerungseinrichtung haben; ohne beides ist die Einspeisung auf **60 %** begrenzt [Q13].
- **Direktvermarktung ab 100 kW:** Die feste Einspeisevergütung gibt es nur bis 100 kW; darüber läuft die Vermarktung über die **Marktprämie** (Direktvermarktung), deren anzulegender Wert ebenfalls halbjährlich degressiert [Q4][Q5]. Für ein Einfamilienhaus ist das irrelevant — relevant wird es bei größeren Dachanlagen auf Mehrfamilienhäusern oder Gewerbehallen, wo die 100-kW-Grenze schnell erreicht ist.

**Dauer:** Die Zahlung läuft **20 Jahre** ab Inbetriebnahme, verlängert bis zum 31. Dezember des 20. Jahres (§ 25 EEG) [Q33]. Danach greift die Ausfallvergütung (§ 53 Abs. 4) — ein Thema für 2046, nicht für die Planung.

> **Rechtslage 2027:** Die Verbraucherzentrale schreibt, die Vergütung sei „zum 1. August 2026 geringfügig gesenkt" worden und wie es ab 2027 weitergehe, sei „noch unklar. Denn ab dann gilt ein neues EEG, das aktuell noch nicht beschlossen ist" [Q13]. Wer **2027** in Betrieb nimmt, plant gegen eine Rechtslage, die noch nicht existiert. Wer 2026 in Betrieb nimmt, hat die 20 Jahre auf dem heutigen Satz fest.

---

## 3. Speicher: Größe, Wirkungsgrad, Notstrom, Aufstellort

### 3.1 Größe: drei Formeln, ein Widerspruch

Die HTW Berlin hat die gängigen Faustregeln geprüft und kommt zu drei Obergrenzen [Q19]:

1. **PV muss groß genug sein:** mindestens **0,5 kWp je 1.000 kWh/a** Verbrauch — sonst gibt es nichts zu speichern.
2. **Speicher nicht größer als die PV:** **max. 1,5 kWh nutzbar je 1 kWp**.
3. **Speicher nicht größer als der Nachtverbrauch:** **max. 1,5 kWh nutzbar je 1.000 kWh/a** Verbrauch.

Rechenbeispiel der HTW: **10 kWp + 4.000 kWh/a → höchstens 6 kWh** nutzbar. Größer steigert den Autarkiegrad nur noch „geringfügig" [Q19].

> **Widerspruch, stehen gelassen:** Die Verbraucherzentrale schreibt auf ihrer Bundes-Seite „etwa **1,5 kWh** Batteriekapazität pro 1.000 kWh Jahresstromverbrauch" und nennt für 5 kWp/5.000 kWh einen Speicher von „rund 7,5 kWh" [Q11]. Die Verbraucherzentrale **Rheinland-Pfalz** schreibt im FaktenCheck „pro 1.000 kWh Haushaltsstromverbrauch etwa **1 kWh** Speicherkapazität" [Q12]. Beide Seiten gehören zum selben Verbund. Die HTW-Formel (1,5 als **Obergrenze**, zusätzlich gedeckelt durch 1,5 × kWp) ist die einzige, die beide Randbedingungen nennt — für die Planung ist sie die brauchbarere. Wer 1,0 ansetzt, liegt wirtschaftlich auf der sicheren Seite.

**Wichtig für dieses Playbook:** Die verbreitete Empfehlung „10 kWp + 8 kWh" ist bei 4.000 kWh Haushaltsstrom **über** der HTW-Obergrenze von 6 kWh. Sie wird erst stimmig, wenn ein E-Auto dazukommt: 12.000 km × 18 kWh/100 km ≈ 2.160 kWh, mit Ladeverlusten rund 2.400 kWh → 6.400 kWh/a → Obergrenze 9,6 kWh. **8 kWh sind dann vertretbar** (eigene Rechnung, Annahmen in §7.1).

### 3.2 Wirkungsgrad: die Zahl, die im Datenblatt nicht steht

- **Round-Trip** ist nicht eine Zahl, sondern eine Kurve. HTW misst Entladewirkungsgrade von **98,0 %** bei guten Systemen oberhalb 900 W [Q18] — aber im Einfamilienhaus wird abends und nachts mit **100–150 W** entladen. Dort bricht die Effizienz ein: bei einem weniger effizienten Hybridwechselrichter müssen **186 W aus der Batterie** kommen, damit **100 W** im Haus ankommen — das sind **54 %** [Q18].
- **Planungszahl:** Finanztip rechnet mit **85 % Gesamteffizienz des Speichersystems** [Q15]. Das ist realistischer als jede Datenblattzahl und Deckungsgleich mit der HTW-Kurve bei realistischer Last.
- **Standby-Verluste** sind ein eigener Posten: HTW beziffert sie bei einem System mit **2,8 Prozentpunkten** — mehr als die Umwandlungsverluste mancher Wettbewerber [Q17].

**Konsequenz:** Jede kWh, die durch den Speicher geht, kostet dich rund **15 %** plus die entgangene Einspeisevergütung. Bei 7,70 ct/kWh Einspeisung und 30 ct/kWh Bezugspreis ist das immer noch ein gutes Geschäft — aber nur, wenn der Speicher nicht zu groß ist und nicht den ganzen Tag im Standby hängt.

### 3.3 Notstrom, Ersatzstrom, Insel — drei verschiedene Dinge

| Begriff | Was geht weiter | Grenze |
|---|---|---|
| **Notstromsteckdose** | einzelne Geräte an einer Dose am Speicher/Wechselrichter | keine Verteilung, kein Hausnetz |
| **Ersatzstrom / Full Backup** | ganzes Hausnetz wird umgeschaltet, PV lädt weiter | nur bis zur Wechselrichterleistung; Großverbraucher (Herd, WP, Wallbox) sprengen sie sofort [Q11][Q27] |
| **Insel** | kein Netzanschluss | mit PV + Speicher in Deutschland nicht autark über den Winter — „keine 100 % Autarkie", auch mit beliebig großem Speicher [Q11] |

- **Saisonspeicherung ist ausgeschlossen:** „eine saisonale Speicherung von Strom … lässt sich auch mit einem sehr großen – unwirtschaftlichen – Batteriespeicher nicht umsetzen" [Q11]. November bis Februar liefert die PV zu wenig [Q11].
- **Ersatzstrom kostet Aufpreis und Planung** (Umschaltbox, getrennter Netzpunkt, Potentialtrennung). Er ist eine **Komfort- und Sicherheitsentscheidung**, keine Wirtschaftlichkeitsentscheidung — und muss beim Kauf des Wechselrichters mitentschieden werden, weil er später oft nicht nachrüstbar ist (bei Fronius per Software-Upgrade „UP.storage" teilweise doch [Q27]).

### 3.4 Garantie, Lebensdauer, Zyklen

- **Lebensdauer:** Module „länger als 20 bis 30 Jahre", Speicher **10 bis 15 Jahre** [Q11]. Finanztip nennt Produktgarantien von typisch **10 Jahren** und dieselbe Lebensdauer-Erwartung [Q15].
- **Alterung ist nicht linear:** „Eine Batterie altert am Anfang also langsam, später aber schneller" [Q11]. Ein Speicher, der nach 12 Jahren 70 % Kapazität hat, ist am Ende seiner Nutzungsdauer — nicht bei 0 %.
- **Zyklenzahlen** sind Marketing, solange die Garantiebedingungen sie mit Restkapazität, Temperaturfenster und Nachweisverfahren verknüpfen. Vergleiche **Garantiedauer + garantierte Restkapazität + Durchsatzkriterium**, nicht die Zyklenzahl im Prospekt. Die geprüften Herstellerdatenblätter (BYD, Huawei) waren zum Prüfzeitpunkt nicht abrufbar bzw. nicht im Volltext lesbar — siehe §12.
- **Hoher Ladezustand schadet:** „ein lang anhaltender hoher Ladezustand" ist ungünstig; ideal ist, dass die Batterie nachmittags voll wird und bis zum Morgen „wieder größtenteils entladen" ist [Q11]. Ein zu großer Speicher erzeugt genau den schädlichen Dauerzustand „zwischen halb voll und voll" [Q11].

### 3.5 Aufstellort und Brandschutz

- **Temperatur ist der Faktor:** Lithiumbatterien mögen weder hohe noch sehr niedrige Umgebungstemperaturen; „in einem trockenen Kellerraum am besten aufgehoben" [Q11]. Garage mit Frost ist schlechter als ein unbeheizter, trockener Keller.
- **Kein Wohnraum, kein Fluchtweg, keine Feuchte.** Praktisch hat sich der Hauswirtschafts-/Technikraum durchgesetzt.
- **Was hier fehlt:** belastbare **Abstände zu brennbaren Bauteilen**, Anforderungen an Feuerwiderstand von Aufstellräumen und die Taktik der Feuerwehr (Trennschnitt) habe ich in dieser Recherche **nicht mit einer prüfbaren Quelle belegen können** — siehe §12. Wer den Speicher in einer Garage mit brennbaren Bauteilen oder unter einem Wohnraum plant, klärt das mit der örtlichen Brandschutzdienststelle, nicht mit dem Verkäufer.

---

## 4. Wallbox: 11 oder 22 kW, Anmeldung, Schutz, Überschuss

### 4.1 11 kW ist der Normalfall — 22 kW ist eine Ausnahme mit Genehmigung

| | 11 kW | 22 kW |
|---|---|---|
| Netzanschluss | 3× 16 A | 3× 32 A |
| Anmeldung | **Pflicht**, vor Inbetriebnahme (NAV § 19 Abs. 2 S. 2) [Q8] | Pflicht **plus Zustimmung** [Q8] |
| Zustimmung Netzbetreiber | nicht erforderlich; „darf der Installation nicht widersprechen" [Q21] | erforderlich, **>12 kVA Summen-Bemessungsleistung** je Anlage (NAV § 19 Abs. 2 S. 3) [Q8]; Antwort binnen **2 Monaten** [Q8][Q21] |
| Ladezeit 60-kWh-Akku (20–80 %) | ca. 3,5 h | ca. 1,8 h |
| Typische Folgekosten | — | Anschlussverstärkung, ggf. Baukostenzuschuss (~500 € bei >30 kW Gesamtbedarf) [Q21] |

**Die 12-kVA-Schwelle ist keine 11-kW-Schwelle.** NAV § 19 Abs. 2 stellt auf die **Summen-Bemessungsleistung** aller Ladeeinrichtungen ab, nicht auf ein einzelnes Gerät: zwei 11-kW-Boxen sind 22 kVA und damit zustimmungspflichtig [Q8]. Eine auf 11 kW **gedrosselte** 22-kW-Box braucht in der Regel keine Genehmigung [Q21] — die Drosselung muss aber dauerhaft und technisch sein, nicht nur eine App-Einstellung.

**Die Wallbox selbst ist immer anmeldepflichtig**, unabhängig von der Leistung, und auch mobile Ladestationen fallen darunter [Q21]. Die Anmeldung ist kostenlos; Geld kostet die Verstärkung des Anschlusses [Q21].

### 4.2 § 14a EnWG: steuerbar, nicht abschaltbar

Seit **1. Januar 2024** gilt die neue Festlegung: Wallboxen, Speicher, Wärmepumpen und Klimaanlagen mit mehr als **4,2 kW** Bezugsleistung sind **steuerbare Verbrauchseinrichtungen** [Q16]. Der Netzbetreiber darf sie „netzorientiert" **dimmen** — auf **4,2 kW Mindestleistung** bei Direktansteuerung [Q9][Q16]. Er darf sie **nicht abschalten** und den Anschluss nicht mehr mit Verweis auf Netzüberlastung verweigern [Q21].

Dafür gibt es Netzentgeltrabatt, drei Module [Q16]:

| Modul | Wirkung | Voraussetzung |
|---|---|---|
| **1** (Standard) | pauschal rund **150 €/a** (2025: 124–188 € je Region) [Q15][Q16] | steuerbare VBE, kein zweiter Zähler |
| **2** | **60 %** Rabatt aufs Netzentgelt | **zweiter Zähler**, lohnt bei hohem Verbrauch [Q16] |
| **3** | zeitvariables Netzentgelt (nach Stunden) | iMSys + flexibler Verbrauch, dazubuchbar zu Modul 1 [Q16] |

**Technisch** läuft die Steuerung über das **intelligente Messsystem (iMSys)** aus moderner Messeinrichtung, Smart-Meter-Gateway und **Steuerbox** — ein alter Rundsteuerempfänger ersetzt das nicht [Q24]. Der Elektriker fordert dafür einen **§ 14a-Klemmblock** („simple Klemmleiste für 15–20 EUR") im Zählerkasten, plus RJ45-Doppelbuchse für EEBUS; bei mehreren steuerbaren Verbrauchern wird das Signal mit Koppelrelais vervielfacht [Q24]. Für den Bauherrn heißt das: **Steuerleitung vorsehen, Klemmen setzen, Inbetriebnahme melden** — wann der Netzbetreiber tatsächlich dimmt, ist nicht seine Baustelle [Q24].

### 4.3 Leitung, Absicherung, Fehlerstromschutz

- **Querschnitt und Länge** sind eine Rechnung aus Strombelastbarkeit (DIN VDE 0298-4), Verlegeart und **Spannungsfall** — keine Tabellenzahl. Als Orientierung: 11 kW = 16 A dreiphasig, 22 kW = 32 A dreiphasig; lange Wege in die Garage (20 m+) oder durch Erdreich brauchen mehr Querschnitt als 5×2,5 mm². Die Entscheidung trifft der Fachbetrieb mit seiner Leitungslänge.
- **Leitungsschutzschalter** ist **nicht** im Gerät: bei der go-e Gemini „muss durch die Elektrofachkraft vorgeschaltet werden", zulässig B oder C mit **16 bzw. 32 A** [Q26].
- **Fehlerstrom:** Wallboxen können **glatte Gleichfehlerströme** erzeugen, die einen Typ-A-RCD „blind" machen. Zwei zulässige Wege: **RCD Typ B**, oder **Typ A plus 6-mA-DC-Erkennung im Gerät**.
  - Die go-e Gemini hat ein eingebautes Fehlerstrom-Schutzmodul mit **20 mA AC und 6 mA DC**; vorgeschaltet werden muss trotzdem mindestens **Typ A (30 mA)** [Q25][Q26].
  - Die Normkette ist **IEC 60364-7-722 / DIN VDE 0100-722** [Q26].
  - **Praktische Folge:** Ein Gerät mit integrierter DC-Erkennung spart den teuren Typ-B-RCD — das senkt die Installationskosten und ist beim Angebotsvergleich ein echtes Kriterium, kein Datenblattfeature [Q20].

### 4.4 PV-Überschussladen und Lastmanagement

- **Überschussladen** heißt: die Wallbox regelt die Ladung auf das, was PV gerade übrig lässt, statt mit voller Leistung ins Netz zu kaufen. Voraussetzung ist, dass die Wallbox den **Zählerstand am Hausanschluss** kennt (Modbus/API/Energy-Manager) — deshalb in §2.6 die Warnung zu geschlossenen Wechselrichtern.
- **Lastmanagement** ist die zweite Aufgabe: mehrere Verbraucher dürfen zusammen die Anschlussleistung nicht überschreiten. Statisch (feste Obergrenze je Gerät) oder dynamisch (misst den Hausanschluss mit).
- **Warum das kein Luxus ist:** Ohne Lastmanagement addieren sich Wallbox (11 kW), Wärmepumpe (3–9 kW), Herd und Speicherladung auf Werte, für die der Hausanschluss nicht ausgelegt ist — die Hauptsicherung fällt, und der Netzbetreiber sieht es. Mit § 14a-Dimmung und Lastmanagement bleibt alles im Rahmen.

### 4.5 Kostenband Wallbox

| Position | Band | Quelle |
|---|---|---|
| Gerät einfach | 300–600 € | [Q20] |
| Gerät Mittelklasse | 600–1.000 € | [Q20] |
| Gerät Premium | 1.000–2.000 € | [Q20] |
| Installation geringer Aufwand (Schrank modern, <5 m, keine Durchbrüche) | 500–800 € | [Q20] |
| Installation mittlerer Aufwand (10–20 m, 1–2 Durchbrüche, FI Typ A-EV) | 800–1.500 € | [Q20] |
| Installation hoher Aufwand (Zählerschrank alt, Erdarbeiten, >30 m) | 1.500–3.000 €+ | [Q20] |
| Standfuß/Montagesäule | 400–1.000 € | [Q20] |
| **Gesamt realistisch EFH** | **1.500–3.000 €** | eigene Addition aus [Q20] |

Abrechnung/Mieterstrom ist ein eigenes Rechtsfeld (Messkonzept, Eichrecht, § 42a EnWG) und **nicht** Gegenstand dieses Playbooks — im selbstgenutzten Einfamilienhaus irrelevant, im Mehrfamilienhaus der teuerste Teil.

---

## 5. Zusammenspiel an einem Hausanschluss

### 5.1 Die Gleichzeitigkeit ist das eigentliche Problem

Nicht die Jahresenergie, sondern die **Lastspitze** entscheidet über die Anschlussgröße:

| Verbraucher | Leistung | Gleichzeitig mit … |
|---|---|---|
| Wallbox 11 kW | 11 kW | abends, wenn gekocht und geduscht wird |
| Wärmepumpe | 3–9 kW (elektrisch) | morgens (Warmwasser), bei Kälte dauerhaft |
| Herd/Backofen | bis 11 kW | abends |
| Speicherladung | 3–10 kW | mittags (PV-Überschuss) oder nachts (Netzladung) |
| Durchlauferhitzer | 18–27 kW | morgens — der Grund, warum manche Häuser keinen 11-kW-Lader vertragen |

Ohne Messung und Steuerung ist die Summe größer als jede Hausanschlusssicherung. Deshalb **zählt** das Lastmanagement doppelt: es verhindert die Auslösung und es ist die Voraussetzung dafür, dass der Netzbetreiber die § 14a-Dimmung überhaupt akzeptiert.

### 5.2 Wer steuert wen

Die Hierarchie, die in der Praxis funktioniert (Erfahrungswissen, nicht Norm — siehe §12):

1. **Energy-Manager / Wechselrichter** kennt PV-Erzeugung, Speicherstand und Hausverbrauch.
2. Er gibt der **Wallbox** einen Leistungs-Sollwert (Überschussladen) und der **Wärmepumpe** ein Signal (Warmwasser bei Überschuss).
3. Der **Netzbetreiber** greift über die **Steuerbox** ein und dimmt auf 4,2 kW (§ 14a) — das übersteuert alles andere.
4. Der **Speicher** ist das Puffer-Glied: er lädt Überschuss und deckt die Spitze, wenn Wallbox und WP gleichzeitig laufen.

**Ein einziger Hersteller für alle drei** ist der bequemste Weg (eine App, ein Support), **offene Schnittstellen** sind der robustere (jeder Baustein bleibt austauschbar). Beides ist vertretbar; geschlossene Systeme ohne API sind es nicht.

### 5.3 Heizstab und Überschuss: meist die schlechteste Verwendung

Ein Heizstab im Warmwasserspeicher ist billig (300–800 €) und wird gern als „Speicher-Ersatz" verkauft. Er wandelt 1 kWh Strom in 1 kWh Wärme — eine Wärmepumpe macht aus 1 kWh Strom **3–4 kWh** Wärme. Wer beides hat, sollte den Überschuss **zuerst** in die Wärmepumpe, dann in die Wallbox, dann in den Speicher und **zuletzt** in den Heizstab schicken. (Reihenfolge = Erfahrungswert; die COP-Zahl 3–4 ist hier **nicht** mit einer eigenen Quelle belegt, siehe §12 — für den WP-spezifischen Nachweis gilt das Playbook `heizung-lueftung.md`.)

### 5.4 Notstrom für die Wärmepumpe

Eine Wärmepumpe im Ersatzstrombetrieb ist ein Sonderfall: Anlaufströme, Solepumpe, Steuerung. „Full Backup" heißt, dass das ganze Hausnetz versorgt wird — aber nur bis zur Leistung des Wechselrichters [Q27]. Eine WP mit 9 kW elektrisch plus Anlaufstrom sprengt einen 10-kW-Hybrid-Wechselrichter im Inselbetrieb. Wer WP-Notstrom will, plant ihn **mit** der WP (Softstarter, Lastmanagement, ggf. eigener Notstromzweig), nicht danach.

---

## 6. Steuern, Anmeldung, Formalien

### 6.1 Umsatzsteuer: 0 % — aber nur bis 30 kWp

§ 12 Abs. 3 UStG lautet (Volltext gelesen) [Q6]:

> „Die Steuer ermäßigt sich auf 0 Prozent für … die Lieferungen von Solarmodulen an den Betreiber einer Photovoltaikanlage, einschließlich der für den Betrieb einer Photovoltaikanlage wesentlichen Komponenten **und der Speicher**, die dazu dienen, den mit Solarmodulen erzeugten Strom zu speichern … **Die Voraussetzungen gelten als erfüllt, wenn die installierte Bruttoleistung … nicht mehr als 30 Kilowatt (peak) beträgt** oder betragen wird."

Wichtig für die Praxis:

- Der Nullsatz gilt für **Lieferung (Nr. 1) und Installation (Nr. 4)** — also auch für die Montageleistung, nicht nur fürs Material.
- **Der Speicher ist ausdrücklich mit drin**, wenn er dem PV-Strom dient.
- **Die Wallbox ist es nicht.** Sie ist keine „für den Betrieb wesentliche Komponente" der PV-Anlage; für sie gilt der Regelsteuersatz. Wer sie in derselben Rechnung mit 0 % ausweist, hat eine Rechnung, die dem Finanzamt nicht gefällt.
- **Über 30 kWp** entfällt der Nullsatz vollständig — dann wird die ganze Lieferung wieder mit 19 % abgerechnet, und die Vorsteuererstattung wird zum Thema.

### 6.2 Einkommensteuer: § 3 Nr. 72 EStG

Volltext (geprüft) [Q7]:

> „die Einnahmen und Entnahmen im Zusammenhang mit dem Betrieb von auf, an oder in Gebäuden … vorhandenen Photovoltaikanlagen, wenn die installierte Bruttoleistung laut Marktstammdatenregister **bis zu 30 Kilowatt (peak) je Wohn- oder Gewerbeeinheit** und insgesamt **höchstens 100 Kilowatt (peak) pro Steuerpflichtigem** oder Mitunternehmerschaft beträgt."

- Gilt **je Wohn-/Gewerbeeinheit** — bei einem Zweifamilienhaus also 2 × 30 kWp, gedeckelt auf 100 kWp je Person.
- Die Anlage muss **auf, an oder in einem Gebäude** sein — Freifläche ist nicht begünstigt.
- Folge: keine Anlage G, keine EÜR, keine Abschreibung für die begünstigten Anlagen. Wer trotzdem eine Steuererklärung mit PV-Einkünften abgibt, macht Arbeit ohne Ertrag.

**Zwei Fallen:** (a) Die Grenzen gelten **pro Steuerpflichtigem**, nicht pro Dach — wer zwei Häuser hat, addiert. (b) Der **Speicher** ist kein eigener Betrieb; er teilt das Schicksal der Anlage.

### 6.3 Marktstammdatenregister: ein Monat, sonst Ordnungswidrigkeit

MaStRV § 5 Abs. 5 (Volltext) [Q10]: Registrierungen müssen „**innerhalb eines Monats nach der Inbetriebnahme**" erfolgen. Zuständig ist der **Anlagenbetreiber**, nicht der Installateur — der macht es üblicherweise, die Pflicht bleibt aber beim Betreiber. Ohne Registrierung gibt es **keine Einspeisevergütung** (die Vergütung setzt die Registrierung voraus) und die 30-kWp-Grenzen von § 12 Abs. 3 UStG / § 3 Nr. 72 EStG werden über die MaStR-Leistung geprüft [Q6][Q7].

### 6.4 Netzanmeldung: VDE-AR-N 4105 in der Fassung 2026-03

**Das ist die Änderung, die 2026 viele Ratgeber noch nicht haben:** Die Anwendungsregel heißt jetzt **VDE-AR-N 4105:2026-03 „Anschluss und Betrieb von Erzeugungsanlagen am Niederspannungsnetz (TAR EZA NS)"**. Sie gilt **seit 01.03.2026**; die Übergangsfrist der Vorgängerausgabe läuft **bis 01.03.2027** [Q23].

- Neu ist ein **vereinfachter Anschlussprozess für Kleinsterzeugungsanlagen, Kleinstspeicher und kombinierte DC-gekoppelte Erzeugungs- und Speichereinheiten bis 800 VA** am Verknüpfungspunkt, Anmeldung über Formular **F.1.2**, das zugleich Inbetriebsetzungserklärung ist [Q23].
- Davon zu unterscheiden sind **Steckersolargeräte nach § 8 Abs. 5a EEG** (max. 2.000 W Modulleistung, max. 800 VA Wechselrichter): dort genügt die **MaStR-Registrierung**, eine Netzanmeldung darf nicht verlangt werden [Q23].
- **Maßgeblich ist das Typenschild/ Einheitenzertifikat**, nicht eine per Software eingestellte Begrenzung [Q23].
- Für die normale Dachanlage (10 kWp) bleibt es beim klassischen Weg: Anmeldung durch den eingetragenen Installationsbetrieb, Netzverträglichkeitsprüfung, Inbetriebsetzungsprotokoll.

### 6.5 Zählerplatz, Steuerbox, Überspannungsschutz

- **Zählerplatz:** Der Zählerschrank ist der Posten, der die Nachrüstung am häufigsten verteuert — ADAC nennt „Zählerschrank ist veraltet und muss komplett erneuert werden" als Grund für die oberste Kostenstufe (1.500–3.000 €+) [Q20]. Wer PV, Speicher und Wallbox plant, plant **einen** neuen Schrank mit Reserven für alle drei, statt dreimal umzubauen.
- **iMSys + Steuerbox** sind für § 14a Pflicht [Q24]; die jährlichen Gebühren liegen bei bis zu **100 €**, der Einbau selbst kostet nichts [Q15].
- **Überspannungsschutz:** Für PV-Anlagen im Wohngebäude ist ein Schutzkonzept auf **DC-Seite (Wechselrichter-Eingang)** und **AC-Seite** Standard; DEHN beschreibt die vier Zonen (Hauptverteilung/HAK, Kommunikation, PV-DC, PV-AC) und liefert Typ-2-Ableiter für die DC-Seite [Q28]. Die normative Herleitung steht in **DIN VDE 0100-443/-534** (kostenpflichtig, hier nicht im Volltext geprüft) — siehe §12.

### 6.6 Gerüst, Absturzsicherung, Denkmalschutz

- **Gerüst:** Für Dacharbeiten an der Traufe ist ein Gerüst oder eine gleichwertige Absturzsicherung nötig — die oft zitierte „Gerüstpflicht ab 3 m" ist **schweizerisch**, nicht deutsch. In Deutschland gilt die DGUV-Regel für Dachdeckerarbeiten und die Landesbauordnung; der Solarteur kalkuliert das Gerüst mit (500–1.500 € je nach Haus, Erfahrungswert — §12).
- **Denkmalschutz:** Solaranlagen auf Denkmalen sind **möglich** — die Deutsche Stiftung Denkmalschutz zeigt Beispiele von der Indach-Anlage in einer Dresdner Kirche bis zur PV auf dem Nürnberger Rathaus [Q29]. Sie sind aber **genehmigungspflichtig** über die Denkmalschutzbehörde, und die Behörde entscheidet über Gestaltung (sichtbare Module, Indach-Lösung, Farbton). **Vor** der Bestellung klären, nicht danach: eine abgelehnte Anlage auf einem bestellten Dach ist ein Totalverlust.
- Für die denkmalrechtliche Seite im Detail gilt das Schwester-Playbook `recht-renovierung.md`.

---

## 7. Wirtschaftlichkeit: 10 kWp + 8 kWh + 11 kW Wallbox

### 7.1 Annahmen (alle offen)

| Größe | Wert | Herkunft |
|---|---|---|
| Anlage | 10 kWp, Süd 35°, 1.000 kWh/kWp·a | PVGIS Köln [Q22] |
| Erzeugung | **10.000 kWh/a** | 10 × 1.000 |
| Haushaltsstrom | 4.000 kWh/a | Annahme (typischer EFH-Haushalt) |
| E-Auto | 12.000 km/a × 18 kWh/100 km = 2.160 kWh, +10 % Ladeverlust = **2.400 kWh/a** | Annahme Verbrauch, Verlustansatz |
| Gesamtverbrauch | **6.400 kWh/a** | Summe |
| Strompreis | **0,30 €/kWh** | Finanztip-Annahme [Q15] |
| Einspeisevergütung | **7,70 ct/kWh**, 20 Jahre fest | [Q5], § 25 EEG [Q33] |
| Autarkie ohne Speicher | 30 % | Anker: 32,3 % bei 5 kWp/4.000 kWh [Q15] |
| Autarkie mit 8 kWh | 65 % | Anker: 62,8 % bei 5 kWh/4.000 kWh [Q15] |
| Speicher-Systemeffizienz | 85 % (in der Autarkie enthalten) | [Q15] |
| Investition PV + Speicher | **17.000 €** (Band 14.000–20.000 €) | [Q14] |
| Investition Wallbox | **2.000 €** | Band [Q20] |

**Eigene Rechnung** — die Autarkiegrade sind von der 5-kWp-Referenz auf 10 kWp/6.400 kWh übertragen, nicht simuliert. Wer es genau will, rechnet mit dem Unabhängigkeitsrechner der HTW Berlin [Q17].

### 7.2 Die Rechnung

**Jahreskosten ohne PV:** 6.400 kWh × 0,30 €/kWh = **1.920 €**

**Variante A — PV ohne Speicher (Autarkie 30 %):**

```
Eigenverbrauch   = 6.400 × 0,30 = 1.920 kWh   → 1.920 × 0,30 =   576 € gespart
Netzbezug        = 6.400 − 1.920 = 4.480 kWh  → 4.480 × 0,30 = 1.344 € bezahlt
Einspeisung      = 10.000 − 1.920 = 8.080 kWh → 8.080 × 0,077 =  622 € erlöst
Saldo            = 1.920 − 1.344 + 622        = 1.198 € Vorteil/a
```

**Variante B — PV + 8 kWh Speicher (Autarkie 65 %):**

```
Eigenverbrauch   = 6.400 × 0,65 = 4.160 kWh   → 4.160 × 0,30 = 1.248 € gespart
Netzbezug        = 6.400 − 4.160 = 2.240 kWh  → 2.240 × 0,30 =   672 € bezahlt
Einspeisung      = 10.000 − 4.160 = 5.840 kWh → 5.840 × 0,077 =   450 € erlöst
Saldo            = 1.920 − 672 + 450          = 1.698 € Vorteil/a
```

**Der Speicher bringt also 1.698 − 1.198 = 500 €/a** — bei 8 kWh und rund 4.000 € Speicherpreis (8 × 500 €/kWh) sind das **8,0 Jahre** Amortisation; bei 600 €/kWh (Finanztip-Obergrenze [Q15]) sind es **9,6 Jahre**. Das deckt sich mit Finanztips Aussage, dass ein Speicher sich „in weniger als zehn Jahren" rechnet, *wenn* er höchstens 600 €/kWh kostet [Q15].

**Amortisation des Gesamtpakets PV + Speicher:**

| Strompreis | Vorteil PV+Speicher | Amortisation 17.000 € | mit 150 € § 14a-Rabatt |
|---|---|---|---|
| 0,25 €/kWh | 1.490 €/a | 11,4 a | 10,4 a |
| **0,30 €/kWh** | **1.698 €/a** | **10,0 a** | **9,2 a** |
| 0,35 €/kWh | 1.906 €/a | 8,9 a | 8,3 a |
| 0,40 €/kWh | 2.114 €/a | 8,0 a | 7,5 a |

**20-Jahre-Betrachtung** (Moduldegradation 0,5 %/a, Preise konstant, ohne Zins und ohne Betriebskosten — eigene Rechnung):

| Jahr | Vorteil | kumuliert | netto nach 17.000 € |
|---|---|---|---|
| 1 | 1.698 € | 1.698 € | −15.302 € |
| 5 | 1.682 € | 8.450 € | −8.550 € |
| **10** | **1.664 €** | **16.806 €** | **−194 €** |
| 15 | 1.645 € | 25.070 € | +8.070 € |
| 20 | 1.628 € | 33.244 € | +16.244 € |

**Die ehrliche Lesart:** Das Paket ist **nach rund 10 Jahren** im Plus — also ziemlich genau dann, wenn der Speicher seine Garantiezeit erreicht und das erste Austauschrisiko beginnt. Die PV-Anlage trägt die Rendite (sie läuft 20–30 Jahre), der Speicher ist die Komponente, die die Rechnung **auf Kante** legt. Das ist kein Argument gegen den Speicher, aber eines gegen den zu großen Speicher und gegen einen Preis über 600 €/kWh.

### 7.3 Sensitivität: was die Rechnung kippt

| Änderung | Wirkung |
|---|---|
| Strompreis 0,25 statt 0,30 €/kWh | Amortisation 10,0 → **11,4 Jahre** (+14 %) |
| Speicherpreis 600 statt 500 €/kWh | Speicher-Amortisation 8,0 → **9,6 Jahre** |
| Autarkie 75 statt 65 % | Vorteil 1.698 → **1.840 €/a** (+142 €/a; je 10 Punkte rund 142 €) |
| Moduldegradation 1 %/a statt 0,5 % | 20-Jahres-Summe 33.244 → **32.575 €** (−669 €) |
| Speicher hält 10 statt 15 Jahre | ein Austausch à 4.000 € frisst 8 Jahre Vorteil |
| Einspeisevergütung sinkt (Degression 1 %/Halbjahr) | nur für **Neu**anlagen relevant; einmal in Betrieb, 20 Jahre fest [Q33] |

**Die drei größten Hebel** sind in dieser Reihenfolge: (1) **Strompreis** — er entscheidet, ob Eigenverbrauch sich lohnt; (2) **Speicherpreis je kWh** — er entscheidet, ob der Speicher sich überhaupt lohnt; (3) **Autarkiegrad** — er entscheidet, wie viel davon ankommt. Die kWp-Zahl ist **nicht** darunter: mehr Module erhöhen die Einspeisung, nicht die Rendite.

### 7.4 Was die Wallbox zur Rechnung beiträgt

**Nichts an der PV-Rechnung — und das ist wichtig.** Die Wallbox verändert weder Erzeugung noch Einspeisevergütung. Ihr wirtschaftlicher Beitrag entsteht nur, wenn die Alternative **öffentliches Laden** wäre: 2.400 kWh/a zu Hause statt an einer öffentlichen AC-Säule. Wie groß diese Differenz ist, hängt vom Tarif vor Ort ab und ist hier **nicht belegt** (§12) — die Wallbox ist deshalb primär eine **Komfort- und Zeitersparnis-Investition**, und sie wird erst durch Überschussladen (§4.4) zum Renditebaustein, weil sie dann teuren Netzbezug durch sonst eingespeisten PV-Strom ersetzt.

---

## 8. Die zehn Fehler, die Geld kosten

1. **Speicher zu groß.** Zwei unabhängige Quellen: HTW begrenzt auf 1,5 kWh je 1.000 kWh/a und 1,5 kWh je kWp [Q19]; die Verbraucherzentrale schreibt, „in der Praxis werden häufig zu große Speicher installiert", was den Ladezustand dauerhaft hoch hält und die Batterie schneller altert [Q11]. Finanztip nennt es „häufiger Fehler: Selbst ein günstiger Speicher lohnt sich nicht unbedingt, wenn er unnötig groß ist" [Q15].
2. **Verschattung nicht simuliert.** Ein Schatten auf einem Modul zieht den ganzen String; ohne Simulation mit Datum/Uhrzeit und ohne Optimierer an den betroffenen Modulen ist der Ertragsverlust erst nach der Montage sichtbar (§2.4). *Mechanismus belegt, Prozentzahl nicht — §12.*
3. **Wechselrichter zu klein (oder zu teuer groß).** Er ist das Bauteil mit der kürzesten Lebensdauer; wer ihn ohne Reserve und ohne offene Schnittstelle kauft, tauscht in 10–15 Jahren und blockiert bis dahin Überschussladen (§2.6).
4. **Wallbox ohne Lastmanagement.** Wallbox (11 kW) + Wärmepumpe + Herd + Speicherladung übersteigen jede Hausanschlusssicherung; ohne Messung und Steuerung fällt die Hauptsicherung, und die § 14a-Dimmung wird nicht akzeptiert (§5.1, §4.4).
5. **Zählerplatz vergessen.** „Zählerschrank ist veraltet und muss komplett erneuert werden" ist die teuerste ADAC-Kostenstufe (1.500–3.000 €+) [Q20] — und sie kommt garantiert, wenn man drei Geräte nacheinander anschließt, statt einmal zu planen (§6.5).
6. **Wallbox nicht angemeldet.** Jede Wallbox ist vor Inbetriebnahme **meldepflichtig**, ab >12 kVA **zustimmungspflichtig** [Q8][Q21]. Wer nachträglich meldet, riskiert den Anschluss und die Vergütung.
7. **Förderung an Bedingungen geknüpft — oder gar nicht mehr da.** Das KfW-Programm **442 „Solarstrom für Elektroautos"** (Zuschuss für PV + Speicher + Ladestation, bis ~9.600 €) wurde am **27.09.2023** nach einem Tag eingestellt: die **300 Mio. €** waren binnen Stunden vergeben, rund **33.000 Anträge** bewilligt [Q30]. Die KfW-Produktseite existiert weiter, trägt aber keinen Förderbetrag mehr und beantwortet nur noch die Frage „Welche Förderungen für E-Mobilität gibt es noch?“ [Q32]. **Es gibt derzeit keine Bundes-Direktförderung für diese Kombination** — wer heute mit „KfW-Zuschuss" rechnet, rechnet mit einem Programm, das es nicht mehr gibt. Prüfe Landes-/Kommunalprogramme aktuell und **vor** der Bestellung, weil sie fast immer Bedingungen an Gerät, Installateur oder Antragsreihenfolge knüpfen.
8. **0 % USt auf die Wallbox anwenden.** § 12 Abs. 3 UStG deckt Module, wesentliche Komponenten, Speicher und deren Installation — die Wallbox nicht [Q6]. Eine Rechnung mit 0 % für die Wallbox ist angreifbar.
9. **Speicher im falschen Raum.** Hohe oder sehr niedrige Temperaturen und langanhaltender hoher Ladezustand schaden; der trockene Kellerraum ist der richtige Ort [Q11] (§3.5).
10. **Denkmalschutz erst nach der Bestellung klären.** PV auf Denkmalen ist möglich, aber genehmigungspflichtig [Q29]; die Ablehnung kommt nach der Bestellung, nicht davor.

---

## 9. Kontrollpunkte

**Vor der Unterschrift (Lastenheft prüfen):**

- [ ] Jahresverbrauch der letzten 12 Monate **und** geplante E-Auto-km in kWh umgerechnet — sonst ist die Auslegung geraten.
- [ ] Verschattungsanalyse mit Datum/Uhrzeit und benannten Modulen.
- [ ] Speichergröße gegen **beide** HTW-Grenzen geprüft (1,5 kWh/1.000 kWh/a **und** 1,5 kWh/kWp) [Q19].
- [ ] Wechselrichter mit **offener Schnittstelle** (Modbus/API) und genug Reserve für Speicher + Wallbox.
- [ ] Zählerplatz: Fotos, Baujahr, freie Teilungseinheiten, Platz für iMSys + Steuerbox + § 14a-Klemmblock [Q24].
- [ ] Wallbox: 11 oder 22 kW, **Summen-Bemessungsleistung** aller Ladepunkte, Drosselung technisch fixiert [Q8].
- [ ] FI-Konzept: Typ A + 6 mA DC im Gerät **oder** Typ B — im Angebot ausdrücklich benannt [Q25][Q26].
- [ ] Steuerbarkeit nach § 14a **im Angebot** (Klemmen, Steuerleitung, Anmeldung), nicht als Nachttrag [Q16].
- [ ] USt-Behandlung getrennt: PV + Speicher 0 %, Wallbox 19 % [Q6].
- [ ] Wer meldet MaStR (Frist 1 Monat) und wer meldet beim Netzbetreiber — mit Namen [Q10].

**Vor Inbetriebnahme:**

- [ ] VDE-AR-N 4105 in der **Fassung 2026-03** zugrunde gelegt, Übergangsfrist bis 01.03.2027 beachtet [Q23].
- [ ] Inbetriebsetzungsprotokoll + Einheitenzertifikat des Wechselrichters liegen vor [Q23].
- [ ] MaStR-Registrierung mit **Bruttoleistung** (nicht nur kWp) — sie entscheidet über 30-kWp-Grenzen [Q6][Q7].
- [ ] Zählerstände vor/nach, Funktionsprotokoll Wallbox (Ladetest), Überschussladen einmal real getestet (nicht nur konfiguriert).
- [ ] § 14a-Anmeldung bestätigt, Netzentgeltmodul gewählt (1/2/3) [Q16].
- [ ] Ersatzstrom/Notstrom einmal **provoziert** (Netz aus, Verbraucher an) — wenn vorhanden [Q27].

---

## 10. Wann Fachbetrieb — und warum hier ausnahmslos

- **Anschluss, Zählerschrank, Absicherung, Inbetriebnahme:** nur eingetragenes Installationsunternehmen (NAV § 13 Abs. 2, siehe `elektro.md`). Das gilt für die PV-Anlage genauso wie für die Wallbox — die Wallbox ist ein Drehstromverbraucher mit 16 oder 32 A, kein Haushaltsgerät.
- **Netzanmeldung:** macht der Installateur, die Pflicht zur MaStR-Registrierung bleibt beim Betreiber [Q10].
- **Dacharbeiten:** Absturzsicherung, Gerüst, Anschlusspunkte, Dichtigkeit der Durchdringungen — Dachdecker/Solarteur, nicht Eigenleistung.
- **Speicher:** Aufstellung, Anschluss, Brandschutzabstimmung mit der örtlichen Dienststelle.
- **Was der Eigentümer beitragen kann:** Verbrauchsdaten sammeln, Zählerstandsfotos, Dachmaße, Verschattungsobjekte fotografieren, Angebote vergleichen, Termine mit dem Netzbetreiber vorbereiten, MaStR-Daten bereithalten. Das ist Vorarbeit, nicht Anschluss.

---

## 11. Quellen

**Typ:** G = Gesetz/Verordnung, B = Behörde, N = Norm/Fachverlag, V = Verbraucherorganisation, F = Fachbetrieb/Fachmedium, H = Hersteller, P = Preisinformationsdienst, C = Community, Y = Video.
Alle URLs am 09.11.2026 einzeln abgerufen; Status je Zeile.

| # | Quelle | Typ | Geprüft |
|---|---|---|---|
| Q1 | EEG 2023 § 48 (Solare Strahlungsenergie), https://www.gesetze-im-internet.de/eeg_2014/__48.html | G | **Volltext gelesen**; Abs. 2 (8,51/7,43/7,64 ct), Abs. 2a (Volleinspeisung +4,8/3,8/5,1), Abs. 3, Fußnoten zu § 100/101. 200 |
| Q2 | EEG 2023 § 53 (Verringerung der Einspeisevergütung), https://www.gesetze-im-internet.de/eeg_2014/__53.html | G | **Volltext**; Abs. 1 Nr. 2: „0,4 Cent pro Kilowattstunde für Strom aus Solaranlagen … abzuziehen". 200 |
| Q3 | EEG 2023 § 51 (negative Preise), https://www.gesetze-im-internet.de/eeg_2014/__51.html | G | **Volltext**; Abs. 1 Wert = null, Abs. 2 Nr. 1 Ausnahme <100 kW bis zum Jahr nach iMSys-Einbau. 200 |
| Q4 | Bundesnetzagentur, „Archivierte EEG-Vergütungssätze" (Übergangsregel + xlsx-Downloads je Halbjahr), https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/ErneuerbareEnergien/EEG_Foerderung/Archiv_VergSaetze/start.html | B | Volltext; maßgebliche Regel „Seit 2024 werden die Fördersätze halbjährlich unter Verwendung eines festen Degressionssatzes bestimmt"; Downloadliste Feb 26–Jul 26 und Aug 26–Dez 26. **Die früher genutzte Übersichtsseite …/EEG_Foerderung/start.html liefert bei Endprüfung 404 und wird nicht mehr zitiert.** 200 |
| Q5 | BNetzA, „Anzulegende Werte für Solaranlagen August 2026 bis Dezember 2026" (xlsx), https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/ErneuerbareEnergien/EEG_Foerderung/Archiv_VergSaetze/_DL/VergSaetzeAug26bisDez26.xlsx?__blob=publicationFile&v=3 | B | **Tabelle geparst** (Zeitreihe seit 01.01.2023, Degressionssatz 0,01, Teileinspeisung/Volleinspeisung/Marktprämie). 200 |
| Q6 | UStG § 12 (Steuersätze), https://www.gesetze-im-internet.de/ustg_1980/__12.html | G | **Volltext Abs. 3**; 0 % für Lieferung (Nr. 1) und Installation (Nr. 4), Speicher eingeschlossen, 30 kWp-Grenze. 200 |
| Q7 | EStG § 3 Nr. 72, https://www.gesetze-im-internet.de/estg/__3.html | G | **Volltext**; 30 kWp je Wohn-/Gewerbeeinheit, 100 kWp je Steuerpflichtigem. 200 |
| Q8 | NAV § 19 (Betrieb von Anlagen, Verbrauchsgeräten und Ladeeinrichtungen), https://www.gesetze-im-internet.de/nav/__19.html | G | **Volltext**; Abs. 2 S. 2 Meldepflicht Ladeeinrichtungen, S. 3 Zustimmung >12 kVA, 2-Monats-Frist. 200 |
| Q9 | EnWG § 14a (netzorientierte Steuerung), https://www.gesetze-im-internet.de/enwg_2005/__14a.html | G | **Volltext** Abs. 1/2; Festlegungskompetenz BNetzA, Netzentgeltreduzierung. 200 |
| Q10 | MaStRV § 5 (Registrierung von Einheiten), https://www.gesetze-im-internet.de/mastrv/__5.html | G | **Volltext**; Abs. 5: „innerhalb eines Monats nach der Inbetriebnahme". 200 |
| Q11 | Verbraucherzentrale, „Lohnen sich Batteriespeicher für Photovoltaik-Anlagen?" (Stand 02.07.2026), https://www.verbraucherzentrale.de/wissen/energie/erneuerbare-energien/lohnen-sich-batteriespeicher-fuer-photovoltaikanlagen-24589 | V | Volltext; 1,5 kWh/1.000 kWh, 10–15 Jahre Lebensdauer, Alterung, Autarkie 25–30 % → 70 %, Notstrom/Ersatzstrom, Kellerraum, keine Saison-speicherung, Solarspitzengesetz-Hinweis. 200 |
| Q12 | Verbraucherzentrale Rheinland-Pfalz, „FaktenCheck Nr. 2: Die richtige Speichergröße" , https://www.verbraucherzentrale-rlp.de/faktencheck-nr-2-die-richtige-speichergroesse-fuer-ihre-photovoltaikanlage-98381 | V | Volltext; **1 kWh/1.000 kWh** (Widerspruch zu Q11), 75 % der Privatanlagen 2023 mit Speicher. 200 |
| Q13 | Verbraucherzentrale, „EEG 2023/24: Was heute für Photovoltaik-Anlagen gilt", https://www.verbraucherzentrale.de/wissen/energie/erneuerbare-energien/eeg-202324-was-heute-fuer-photovoltaikanlagen-gilt-75401 | V | Volltext; Absenkung zum 01.08.2026, Nachfolge-EEG ab 2027 nicht beschlossen, negative Preise + Verlängerung, iMSys/Steuerbox ab 25.02.2025 für ≥7 kWp, sonst 60 %-Begrenzung. 200 |
| Q14 | Finanztip, „Photovoltaik 2026: Lohnt sich eine Solaranlage?", https://www.finanztip.de/photovoltaik/ | P | Volltext; **14.000–20.000 €** für PV+Speicher im EFH (reale Community-Angebote, 2026). 200 |
| Q15 | Finanztip, „PV-Speicher: Wann lohnt sich ein Batteriespeicher?", https://www.finanztip.de/photovoltaik/stromspeicher/ | P | Volltext; Tabelle 5 kWp ohne/mit 5 kWh (32,3 % / 62,8 % Autarkie), Systemeffizienz **85 %**, max. **600 €/kWh**, § 14a-Rabatt 124–188 € (BNetzA 2025), iMSys-Kosten bis 100 €/a. 200 |
| Q16 | Finanztip, „§ 14a EnWG: steuerbare Verbrauchseinrichtungen" (Stand 01.09.2026), https://www.finanztip.de/stromtarife/steuerbare-verbrauchseinrichtungen-14a-enwg/ | P | Volltext; Gerätearten, >4,2 kW, Modul 1 (~150 €/a) / Modul 2 (60 %, zweiter Zähler) / Modul 3 (zeitvariabel), iMSys+Steuerbox. 200 |
| Q17 | HTW Berlin, „Testergebnisse der Stromspeicher-Inspektion 2025", https://solar.htw-berlin.de/publikationen/testergebnisse-stromspeicher-inspektion-2025 | N | Volltext; Datenblatt 98,1 % vs. Labor 97,6 % (Wechselrichter), Standby 2,8 Pp., SPI-Bewertung, Marktzahlen. 200 |
| Q18 | HTW Berlin, „Stromspeicher-Inspektion 2025" (PDF), https://solar.htw-berlin.de/wp-content/uploads/HTW-Stromspeicher-Inspektion-2025.pdf | N | PDF geparst; Entladewirkungsgrad 98,0 % >900 W; **bei 100 W nur 54 %** (186 W aus der Batterie für 100 W im Haus); 100–150 W typische Nachtlast. 200 |
| Q19 | HTW Berlin, „Empfehlungen zur Auslegung von Solarstromspeichern" (Orth/Weniger/Meissner, Sonnenenergie 02/2022), https://solar.htw-berlin.de/publikationen/auslegung-von-solarstromspeichern | N | Volltext; drei Faustformeln (0,5 kWp/1.000 kWh; ≤1,5 kWh/kWp; ≤1,5 kWh/1.000 kWh), Beispiel 10 kWp + 4.000 kWh → 6 kWh. 200 |
| Q20 | ADAC, „Wallbox: Das kosten private Ladestationen plus Installation 2026", https://www.adac.de/rund-ums-fahrzeug/elektromobilitaet/laden/wallbox-kosten/ | P | Volltext; Geräte 300–2.000 €, Installation 500–3.000 €, drei Aufwandsstufen mit Beträgen, Standfuß 400–1.000 €, integrierte DC-Erkennung senkt Kosten. 200 |
| Q21 | ADAC, „Wallbox fürs Elektroauto anmelden", https://www.adac.de/rund-ums-fahrzeug/elektromobilitaet/laden/wallbox-anmelden/ | P | Volltext; Meldepflicht für alle, Genehmigung >11 kW, 2-Monats-Frist, Drosselung auf 11 kW genehmigungsfrei, Baukostenzuschuss ~500 € ab 30 kW. 200 |
| Q22 | PVGIS v5.2 (EU-JRC), PVcalc-API, https://re.jrc.ec.europa.eu/pvg_tools/en/ | B (Modell) | **API abgefragt** für 6 Städte (1 kWp, 35°, Süd, 14 % Verlust, PVGIS-SARAH2) und für Köln in 6 Ausrichtungen + 7 Neigungen. Werte in §2.2/2.3. 200 |
| Q23 | elektrofachkraft.de, „VDE-AR-N 4105:2026-03 – was gilt jetzt?" (04.09.2026), https://www.elektrofachkraft.de/sicheres-arbeiten/vde-ar-n-4105-2026-03 | F | Volltext; **Fassung 2026-03 „TAR EZA NS" gilt seit 01.03.2026**, Übergangsfrist bis 01.03.2027, 800-VA-Klasse/Formular F.1.2, § 8 Abs. 5a EEG (2.000 W/800 VA), Typenschild maßgeblich. 200 |
| Q24 | photovoltaikforum.com, „Steuerung nach § 14a – ENWG (Wallbox plus PV-Anlage)", https://www.photovoltaikforum.com/thread/261802-steuerung-nach-14a-enwg-wallbox-plus-pv-anlage/ | C | Thread gelesen; Steuerung nur über iMSys (mME+SMGw+Steuerbox), kein Rundsteuerempfänger; § 14a-Klemmblock 15–20 €, RJ45/EEBUS, Koppelrelais bei mehreren SteuVE. **Community, keine Rechtsquelle.** 200 |
| Q25 | go-e, „Datenblatt go-e Charger Gemini 11/22 kW" (V1.4), https://go-e.com/fileadmin/Support/Anleitungen/Deutsch/datenblatt-go-e-charger-gemini-11-22-kw.pdf | H | PDF gelesen; DC-Schutzmodul integriert (6 mA DC, 20 mA AC), gebäudeseitig FI **Typ A** + Leitungsschutzschalter, statisches/dynamisches Lastmanagement, IP65. 200 |
| Q26 | go-e, „Installations- und Bedienungsanleitung go-e Charger Gemini", https://go-e.com/fileadmin/Support/Anleitungen/Deutsch/go-e-charger-gemini-installations-und-bedienungsanleitung.pdf | H | PDF gelesen; LS B/C 16 bzw. 32 A, FI mind. Typ A 30 mA, Verweis **IEC 60364-7-722**, integrierte 6-mA-DC-Erkennung. 200 |
| Q27 | Fronius, „Symo GEN24 & GEN24 Plus 3.0–10.0 kW" (Datenblatt DE), https://www.fronius.com/en/~/downloads/Solar%20Energy/Datasheets/SE_DS_Fronius_Symo_GEN24_GEN24Plus_3_to_10_kW_DE.pdf | H | PDF gelesen; **PV Point** (Basisnotstrom) vs. **Full Backup** (ganzes Haus), Nachrüstung per „UP.storage", offene Schnittstellen. 200 |
| Q28 | DEHN, „Überspannungsschutz für PV-Anlagen in Wohngebäuden", https://www.dehn.de/de/loesungen/photovoltaik/wohnbau/ueberspannungsschutz | H | Volltext; Schutzkonzept über vier Zonen (HAK/Hauptverteilung, Kommunikation, PV-DC, PV-AC), Typ-2-Ableiter DC (DEHNcube/DEHNguard YPV), Typ 1+2 im Zählerfeld. 200 |
| Q29 | Deutsche Stiftung Denkmalschutz, „Solaranlagen auf Denkmalen", https://www.denkmalschutz.de/ueber-uns/die-deutsche-stiftung-denkmalschutz/nachhaltigkeit/solaranlagen-auf-denkmalen.html | V | Volltext; Solaranlagen auf Denkmalen „durchaus möglich", Beispiele (Indach-Module Kirche Dresden, Rathaus Nürnberg, Flachdach Gymnasium). 200 |
| Q30 | energie-experten.org, „KfW-Zuschuss ‚Solarstrom für Elektroautos' gestoppt" (27.09.2023), https://www.energie-experten.org/news/kfw-zuschuss-solarstrom-fuer-elektroautos-gestoppt-weitere-foerderung-ab-2024-moeglich | F | Volltext; Programm 442 am ersten Tag eingestellt, **300 Mio. €** ausgeschöpft, **~33.000 Anträge**, Zitat der KfW-Seite. 200 |
| Q31 | PvWelt™, „PV-Anlage zu groß? Warum viele Anbieter Ihnen zu viele Solarmodule verkaufen!" (22.10.2026, 26:39), https://www.youtube.com/watch?v=dRg0B1km4jE | Y | Video existiert (oEmbed geprüft, Titel/Kanal/Datum/Länge), Beschreibung gelesen: Angebote 10 vs. 15 kWp vs. Volldach, „mehr Module bedeuten nicht automatisch mehr Rendite". **Kein Transkript geprüft — keine Zahlen daraus übernommen.** |
| Q32 | KfW, Produktseite „Zuschuss Nr. 442 Solarstrom für Elektroautos", https://www.kfw.de/inlandsfoerderung/Privatpersonen/Bestehende-Immobilie/F%C3%B6rderprodukte/Solarstrom-f%C3%BCr-elektroautos-(442)/ | B | Seite erreichbar, Inhalt JS-gerendert; nur FAQ-Gerüst lesbar („Welche Förderungen für E-Mobilität gibt es noch?"). **Programmstatus daher über Q30 belegt, nicht über diese Seite.** 200 |
| Q33 | EEG 2023 § 25 (Dauer der Zahlung), https://www.gesetze-im-internet.de/eeg_2014/__25.html | G | **Volltext**; „für die Dauer von 20 Jahren zu zahlen", Beginn Inbetriebnahme, Verlängerung bis 31.12. des 20. Jahres. 200 |

**Quellenbilanz:** 33 Einträge, **alle 33 URLs am 09.11.2026 einzeln abgerufen und mit HTTP 200 bestätigt**. Zwei URLs sind im Lauf der Prüfung gestorben und wurden **ersetzt statt stillschweigend gelöscht**: die BNetzA-Übersichtsseite `…/EEG_Foerderung/start.html` (404 → ersetzt durch Archivseite Q4 + xlsx Q5, siehe §12 Nr. 11) und eine BNetzA-§14a-Seite (404 → nicht verwendet; § 14a stützt sich auf EnWG § 14a, Q9, Q16 und Q24). Volltext gelesen: Q1, Q2, Q3, Q6, Q7, Q8, Q9, Q10, Q33 (Gesetze), Q4, Q5 (Behörde, inkl. xlsx-Parsing), Q11–Q21, Q23–Q30. Modell-API abgefragt: Q22.

---

## 12. Unbelegt / offen

Was hier **nicht** steht, weil ich es nicht mit einer prüfbaren Quelle belegen konnte — und was stattdessen gilt:

1. **Verschattungs-Prozentwerte.** Belegt ist der Mechanismus (String vs. Optimierer), nicht der Ertragsverlust je Dach. Es gibt keine seriöse Pauschalzahl; nur eine standortbezogene Simulation (mit Datum/Uhrzeit) liefert sie.
2. **Brandschutz-Anforderungen an den Speicher-Aufstellraum.** Weder Abstände zu brennbaren Bauteilen noch Feuerwiderstand des Aufstellraums oder Vorgaben zum Trennschnitt der Feuerwehr konnte ich in einer belastbaren Quelle verifizieren. Q11 nennt nur „trockener Kellerraum" (Temperatur/Ladezustand), das ist **kein** Brandschutznachweis.
3. **Zyklenfestigkeit und Garantiebedingungen der Speicherhersteller.** Die Datenblätter von BYD (Link 404) und Huawei (Seite JS-gerendert, kein Datenblatt-PDF im Volltext) konnten nicht geprüft werden. **Keine Zyklenzahl in diesem Playbook ist belegt** — wer damit wirbt, muss das Datenblatt des konkreten Modells vorlegen.
4. **Preisaufschläge Full Black / Glas-Glas / bifazial.** Bauartunterschiede sind belegt (Q11), die Aufpreise je m² nicht. Angebotssache.
5. **Gerüstkosten (500–1.500 €).** Erfahrungswert, keine Quelle. Die „Gerüstpflicht ab 3 m" ist schweizerisch und gilt in Deutschland nicht (siehe `SKILL.md`, Abschnitt Normen).
6. **Öffentliche Ladestrompreise** und damit der ROI der Wallbox gegenüber öffentlichem Laden. Fehlt in dieser Recherche; die Wallbox ist deshalb in §7.4 **nicht** in die Amortisation eingerechnet.
7. **COP der Wärmepumpe (3–4).** Die Reihenfolge „WP vor Heizstab" ist Erfahrungswissen; die Zahl gehört in `heizung-lueftung.md` und ist dort zu belegen.
8. **TSG/Zählerplatz-Detailanforderungen.** VDE-AR-N 4100 und die Muster-TAB des BDEW sind kostenpflichtig bzw. nicht im Volltext geprüft; Q24 nennt den § 14a-Klemmblock, das ist ein Teilaspekt.
9. **Normen im Volltext.** DIN VDE 0100-443/-534 (Überspannungsschutz), DIN VDE 0100-722 (Ladeinfrastruktur) und DIN VDE 0298-4 (Strombelastbarkeit) sind kostenpflichtig. Belegt sind hier nur **Nummer, Gegenstand und die zitierende Fachquelle** (Q26, Q28) — **keine Volltextzitate**.
10. **Nachfolge-EEG ab 2027.** Belegt ist nur, dass die Vergütung zum 01.08.2026 gesenkt wurde und das Nachfolge-EEG „aktuell noch nicht beschlossen" ist [Q13]. **Wer 2027 in Betrieb nimmt, plant gegen eine Rechtslage, die es noch nicht gibt.**
11. **Toter Link, offen ausgewiesen:** Die BNetzA-Übersichtsseite `…/EEG_Foerderung/start.html` war während der Recherche abrufbar (Tabelle 7,70/6,66/5,44 und 12,22/10,24) und lieferte bei der Endprüfung am 09.11.2026 **HTTP 404**. Die Sätze in diesem Playbook stammen deshalb aus der **xlsx-Datei** [Q5] und der **Archivseite** [Q4] — beide 200. Die Aussage ist damit weiter belegt, die ursprüngliche Fundstelle ist tot.

---

## Balkonkraftwerk (Steckersolar) — die kleine Schwester der Dachanlage

- **Grenzen seit dem Solarpaket**: Modulleistung bis **2.000 W (2 kW)**, Wechselrichterleistung zusammen
  **maximal 800 VA**; mehrere Geräte werden zusammengerechnet (BNetzA-FAQ, Stand 21.02.2025:
  https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/ErneuerbareEnergien/Solaranlagen/Balkon_table.html).
- **Anmeldung**: im **Marktstammdatenregister** registrieren (Pflicht, kostenlos); die Meldung beim
  Netzbetreiber entfällt für Steckersolargeräte nach der Sonderregelung — der Zähler wird bei
  Rücklaufhemmung getauscht, nicht zwingend gegen einen Zweirichtungszähler.
- **Steckdose**: Betrieb an einer normalen Schuko-Steckdose ist zulässig, aber nur mit den vom
  Wechselrichter geforderten Schutzmaßnahmen; ein eigener Stromkreis mit Absicherung ist die saubere
  Lösung, wenn die Leitung alt ist (siehe `elektro-60er-haus.md`).
- **Wirtschaftlich** ist das Gerät kein Ersatz für eine Dachanlage: 800 W Einspeisegrenze, hoher
  Eigenverbrauchsanteil, aber kleiner Ertrag — für Mietwohnung und kleine Grundlast sinnvoll, für ein
  ganzes Haus nicht.

## 13. Die zehn Regeln zum Mitnehmen

1. **Verbrauch messen, dann kWp wählen.** Ohne Zwölf-Monats-Daten ist jede Auslegung geraten.
2. **1.000 kWh/kWp·a** ist die ehrliche Ertragsannahme für Mittelfeld-Deutschland — standortbezogen rechnen (PVGIS), nicht pauschal abschlagen.
3. **Ost/West kostet 20 %, nicht 40 %** — und liefert, wenn du es brauchst.
4. **Speicher: 1,5 kWh je 1.000 kWh Verbrauch ist die Obergrenze**, nicht das Ziel. Bei 10 kWp/4.000 kWh sind das 6 kWh.
5. **Wirkungsgrad plant man mit 85 %**, nicht mit den 98 % aus dem Datenblatt.
6. **11 kW Wallbox ist der Normalfall**; 22 kW braucht Zustimmung, und die Schwelle ist **12 kVA Summenleistung**, nicht 11 kW Geräteleistung.
7. **Alles über 4,2 kW wird steuerbar** (§ 14a) — Dimmen auf 4,2 kW, dafür 150 €/a. Steuerleitung und Klemmblock von Anfang an vorsehen.
8. **0 % USt und ESt-Freiheit enden bei 30 kWp** — die Wallbox ist nie zu 0 %.
9. **MaStR innerhalb eines Monats**, sonst keine Vergütung.
10. **Der Speicher legt die Rechnung auf Kante, die PV trägt sie.** Amortisation ~10 Jahre bei 30 ct/kWh und 500 €/kWh Speicherpreis — alles darüber ist Verkaufsprosa.

---

*Verwandte Playbooks: `elektro.md` (Zählerschrank, FI, Querschnitt, NAV-Grenze), `heizung-lueftung.md` (Wärmepumpe, Heizstab, GEG), `kosten-bauzeit.md` (Angebotsvergleich, Nachträge), `recht-renovierung.md` (Denkmalschutz, Nachbarrecht, Gerüst).*