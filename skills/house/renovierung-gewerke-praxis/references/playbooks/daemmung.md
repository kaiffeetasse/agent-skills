# Playbook: Dämmung — Stoffe, Bauteile, Bauphysik, Wirtschaftlichkeit

**Stand:** 09.11.2026 · **Zielgruppe:** Eigentümer eines Ein-/Zweifamilienhauses, handwerklich begabt, kein Bauphysiker
**Rechtsstand:** Das GEG heißt seit **29.07.2026 GModG** (BGBl. 2026 I Nr. 226). Zitiert wird GModG; wo eine Quelle
noch „GEG" schreibt, steht das dabei. **Grenze dieses Playbooks:** Es erklärt Auswahl, Aufbau, Physik und Rechnung.
Es ersetzt **keinen** Wärmeschutznachweis: U-Werte, Tauwasser und sommerlicher Wärmeschutz werden am konkreten
Objekt berechnet, nicht aus einer Tabelle abgeschrieben.

Zahlen mit `[Qnn]` sind belegt (Quellenliste unten, alle URLs am 09.11.2026 auf HTTP 200 geprüft). Eigene
Rechnungen sind als **„gerechnet"** markiert, Schätzungen als **„Schätzung"**. Widersprüche zwischen Quellen
stehen als Widerspruch da, nicht als Mittelwert.

---

## 0. Kurzantwort

Dämmen ist Rechnen, nicht Materialkauf. Drei Sätze tragen die ganze Entscheidung:

1. **Dicke schlägt Materialpreis.** Die Arbeit (Gerüst, Anschlüsse, Dampfbremse) kostet ein Vielfaches des
   Dämmstoffs; das Material macht nur etwa **30 %** der Maßnahmenkosten aus `[Q13]`. Deshalb ist die billigste
   Dämmung pro Zentimeter meist die falsche Sparsamkeit.
2. **Fuge schlägt Dicke.** Ein durchgehender Luftspalt oder eine offene Dampfbremse kostet mehr, als 5 cm
   zusätzliche Dämmung einbringen (Erfahrungswert, keine Messreihe) — Konvektion hinter der Dämmung ist kein
   theoretisches Risiko, sondern der häufigste Grund, warum eine fachlich richtige Schicht nicht wirkt `[Q28]`.
3. **Feuchte schlägt alles.** Nasser Dämmstoff dämmt nicht, er schimmelt. Erst Untergrund, Dachhaut und
   Feuchteeintrag klären, dann dämmen `[Q08]`.

**Und die Gegenrede zum Reflex „mehr ist immer besser":** Der Grenznutzen fällt steil. Bei einer ungedämmten
Wand bringen die ersten 16 cm rund **10,20 €/m²·a** Heizkostenersparnis, die nächsten 8 cm nur noch etwa
**0,45 €/m²·a** (gerechnet, § 5.3). Bei einer bereits gedämmten Fassade kann die zweite Dämmebene **über
70 Jahre** Amortisation brauchen `[Q15]`.

**Grenze der Eigenleistung:** Kellerdeckendämmung, oberste Geschossdecke (Massivdecke), Rohrisolierung und
Rollladenkasten-Innendämmung gehen selbst. WDVS, Dachdämmung mit Dampfbremse, Innendämmung ohne Nachweis,
Perimeterdämmung und Kerndämmung gehören in Fachbetriebe (§ 7).

---

## 1. Dämmstoffe im Vergleich

### 1.1 Die Tabelle, auf die es ankommt

λ = Bemessungswert der Wärmeleitfähigkeit (kleiner ist besser). Brandklasse nach DIN 4102-1 (A1 = nicht brennbar,
B1 = schwer entflammbar, B2 = normal entflammbar) `[Q19]`. c = spezifische Wärmekapazität, entscheidend für den
**sommerlichen** Wärmeschutz. Preise: Materialpreis je m², Bezugsdicke = „GEG-Dicke" (siehe Hinweis unter der
Tabelle).

| Dämmstoff | λ [W/(m·K)] | Brandklasse | c [J/(kg·K)] | Preis [€/m²] | Taugt für |
|---|---|---|---|---|---|
| EPS (Polystyrol) | 0,032–0,040 `[Q24]`; 0,037 `[Q13]` | B1 `[Q19]` | 1.500 `[Q19]` | 10 `[Q13]` | AW, Dach, Decke, Innendämmung |
| Glaswolle (KMF) | 0,030–0,050 `[Q24]`; 0,037 `[Q13]` | A1 `[Q19]` | 830–1.000 `[Q19]` | 8 `[Q13]` | universell, Dach, Decke |
| Steinwolle (KMF) | 0,034/0,035 (λD/λB) `[Q22]` | A1 `[Q22]` | 830–1.000 `[Q19]` | 11 `[Q13]` | Dach, Fassade, Brandschutz |
| Holzfaser (Platte/Matte) | 0,037–0,052 `[Q24]`; λB 0,040 `[Q21]` | E nach EN 13501-1 `[Q21]` — **streitig**, siehe 1.4 | 2.100–2.500 `[Q19]` | 21–22 `[Q13]` | Dach, Innendämmung, Schall |
| Zellulose (Flocke) | 0,038–0,042 `[Q19][Q13]` | B2 `[Q19]` | 1.800–2.200 `[Q19]` | 20 `[Q13]` | Einblasen: Decke, Hohlräume |
| PUR/PIR | 0,022–0,029 `[Q24]` | B1 `[Q19]` | 1.400 `[Q19]` | 14 `[Q13]` | wenig Platz, Kellerdecke, Gauben |
| Schaumglas | 0,038–0,070 `[Q24]`; 0,038–0,055 `[Q19]` | A1 `[Q19]` | 850–1.000 `[Q19]` | nicht belegt | Sockel, Perimeter, Flachdach |
| Glasschaum-Schotter (Blähglas) | 0,060–0,120 `[Q24]` | A1 `[Q19]` | 850–1.000 `[Q19]` | nicht belegt | unter Bodenplatte, Kapillarbruch |
| Vakuumpaneel (VIP) | 0,004–0,008; beschädigt 0,02 `[Q24]` | nicht belegt | nicht belegt | nicht belegt | Nischen, Denkmal, Platzmangel |

**Was die Preisspalte wirklich sagt:** `[Q13]` bepreist die Dämmstoffe ausdrücklich „für Dämmstoffe (Dämmdicke
GEG)" und nennt die Dicke nicht je Material. Die GEG-Dicke ist aber genau die Dicke, die für U ≈ 0,24 W/(m²K)
nötig ist — und dafür gibt `[Q19]` eine saubere Zuordnung λ → Dicke:

| λ [W/(m·K)] | 0,025 | 0,030 | 0,032 | 0,035 | 0,040 | 0,045 |
|---|---|---|---|---|---|---|
| Mindestdicke für U ≤ 0,24 [cm] | 10 | 12 | 13 | 14 | 16 | 18 |

Die Preise in 1.1 sind also näherungsweise Preise **bei dieser Dicke** (16 cm bei λ 0,040, 14 cm bei λ 0,035).
Das ist eine Zuordnung zweier Quellen, keine wörtliche Zusage von `[Q13]` — wer einen Punktpreis braucht, nimmt
das Angebot, nicht die Tabelle.

### 1.2 Die Profile dahinter

**EPS** ist der Preisbrecher und der Standard im WDVS. λ 0,032–0,040, B1, hohe Druckfestigkeit, nimmt kaum
Wasser auf, ist aber **dampfsperrend** und nicht kapillaraktiv: Feuchte, die einmal dahinter sitzt, trocknet
schlecht. Deshalb ist die Verklebung (vollflächig, fugenfrei) und der Sockelabschluss kein Detail, sondern die
Haltbarkeitsfrage `[Q28]`.

**Mineralwolle (KMF)** ist der einzige Massenstoff, der **A1 nicht brennbar** ist und gleichzeitig diffusionsoffen
(μ = 1 bei Rockwool `[Q22]`). Sie ist preislich fast unschlagbar (8–11 €/m² `[Q13]`) und im Brandschutz oft die
Bedingung, an der ein Aufbau überhaupt zulässig ist. Zwei Nachteile: geringe Wärmespeicherfähigkeit (c 830–1.000,
sommerlicher Wärmeschutz schwach `[Q19]`) und das Gesundheitsthema KMF: **Glaswolle von vor 1996 gilt als
krebserregend**, neue Wolle ist mit RAL-Gütezeichen unbedenklich, reizt aber Haut und Atemwege — Staubschutz,
Handschuhe, nicht quetschen `[Q13]`.

**Holzfaser** ist der Stoff für Bauherren, die sommerlichen Hitzeschutz und Feuchteregulierung mitkaufen wollen:
c 2.100–2.500, μ = 2, sd-Wert 0,08 m bei 40 mm `[Q21]` — also **diffusionsoffen und kapillaraktiv**, was
Innendämmung und Altbaudach erst verträglich macht. Preis: mehr als das Doppelte von EPS `[Q13]`.

**Zellulose** ist der Einblas-Klassiker: aus Altpapier, λ 0,038–0,042, B2, c 1.800–2.200 `[Q19]`. Ihre Stärke ist
nicht der λ-Wert, sondern dass sie **Hohlräume fugenfrei füllt** und dabei Restfeuchte puffert. Ihre Schwäche
ist die Verarbeitung: zu locker eingeblasen setzt sie sich und lässt oben einen Hohlraum — der klassische
Dämmfehler `[Q28]`.

**PUR/PIR** löst das Platzproblem (λ 0,022–0,029 `[Q24]`): 10 cm PUR/PIR ersetzen je nach Produkt **13–17 cm
EPS** (gerechnet). Bezahlt wird das
mit Preis pro R-Wert, B1 statt A1 und einem Material, das bei Brand zu Rauchgasen führt. Sinnvoll an genau zwei
Stellen: Kellerdecke mit begrenzter Höhe und Gauben/Nischen.

**Schaumglas** ist die Antwort auf „darf nass werden": geschlossenzellig, druckfest, A1, nimmt praktisch kein
Wasser auf. Deshalb Sockel, Perimeter, Flachdach, Bodenplatte. λ 0,038–0,055 nach `[Q19]`, nach `[Q24]` bis 0,070
— die Streuung ist Produktqualität, nicht Messfehler.

**Glasschaum-Schotter** ist kein Plattenstoff, sondern eine Schüttung unter der Bodenplatte: kapillarbrechend,
lastabtragend, A1, aus Recyclingglas. λ 0,060–0,120 `[Q24]` ist der schlechteste Wert der ganzen Liste — dafür
ersetzt er Kies **und** Dämmung in einem Arbeitsgang. Beispiel: 17 cm Kerndämmung aus Schaumglasschotter in einer
Stampflehmfassade `[Q19]`.

**Vakuumpaneele** sind die Notlösung für Denkmal und Nischen: λ 0,004–0,008 `[Q24]`, also **1,4 cm für
U = 0,24** (gerechnet, § 5.2). Drei harte Nachteile: nicht zuschneidbar (jeder Schnitt zerstört das Vakuum — dann
λ 0,02), teuer, und Lebensdauer/Garantie sind deutlich kürzer als die eines Bauteils. Ein Panel ist kein
Dämmstoff, sondern ein Einbauteil mit Statik und Anschlussdetail.

### 1.3 Ökologie: GWP und was das GModG dazu sagt

Das GModG bewertet **den Betrieb**, nicht den Baustoff: Anlage 9 nennt Emissionsfaktoren je kWh (Erdgas **240**,
Heizöl **310**, Strom netzbezogen **560**, Holz **20** g CO₂-Äq./kWh) `[Q06]`. Eine Tabelle „GWP je Dämmstoff"
gibt es im GModG **nicht** — die Baustoff-Ökobilanz kommt aus EPDs und der Ökobaudat-Datenbank des Bundes `[Q20]`.

Belegter Ankerwert: Mineralwolle mittlerer Rohdichte (100 kg/m³) hat A1–A3 ein **GWP von 117,4 kg CO₂-Äq./m³**
`[Q20]`. Auf 20 cm umgerechnet sind das **23,5 kg CO₂-Äq./m²** (gerechnet). Zum Vergleich: 20 cm Mineralwolle
sparen an einer Wand mit U 1,5→0,157 rund **87 kWh/m²·a**, also etwa **21 kg CO₂/m²·a** bei Erdgas `[Q06]` — die
Dämmung hat ihre graue Energie nach **etwa 1,1 Jahren** zurückverdient (gerechnet). Diese Rechnung ist der
eigentliche ökologische Kern: fast jeder Dämmstoff amortisiert sich energetisch in Monaten bis wenigen Jahren,
die Unterschiede zwischen den Stoffen sind zweitrangig gegenüber der Frage, **ob** gedämmt wird `[Q23]`.

Für nachwachsende Rohstoffe gilt qualitativ: Holzfaser und Zellulose binden Kohlenstoff und können ein **sehr
niedriges oder sogar negatives** Treibhauspotenzial haben `[Q19]`. Ein belastbarer Zahlenvergleich scheitert
daran, dass biogener Kohlenstoff in den Quellen unterschiedlich verbucht wird (siehe 1.4).

### 1.4 Widersprüche, die man stehen lassen muss

- **Holzfaser-Brandklasse.** `[Q19]` führt Holzfaser als **A2 (nicht brennbar)**, das technische Datenblatt von
  STEICO für die Matte flex 038 nennt **E nach EN 13501-1** `[Q21]` — das entspricht B2. Beides ist nicht
  gleichzeitig richtig für dasselbe Produkt: Es gibt Holzfaserprodukte mit Brandschutzzusatz (B1/A2) und normale
  Matten (B2/E). **Regel: immer das Datenblatt des konkreten Produkts, nie die Materialgruppe.**
- **Schaumglas-λ.** `[Q19]` 0,038–0,055, `[Q24]` 0,038–0,070. Die 0,070 sind Randware/ältere Produkte.
- **GWP-Vergleich.** Eine Hersteller-Tabelle beziffert Holzfaser mit **25–75 kg CO₂-Äq./m² bei R = 5** und
  Glaswolle mit 5–15 `[Q24a]` — Holzfaser also **schlechter** als Mineralwolle. Das widerspricht der
  Ökobaudat-Logik, weil dort die biogene Kohlenstoffspeicherung separat (negativ) verbucht wird. Wer GWP
  vergleicht, muss fragen: **mit oder ohne biogenen Kohlenstoff, welches Modul, welche Rohdichte?**
- **Mineraldämmplatte λ.** `[Q13]` nennt in der Tabelle 0,035, im Text darunter 0,045 W/(m·K) — innerhalb einer
  Quelle. Der Textwert deckt sich mit `[Q24]` (≈ 0,045); die Tabelle ist der Ausreißer.
- **Sommerlicher Wärmeschutz, Normstand.** § 14 GModG verweist auf **DIN 4108-2:2013-02** `[Q04]`; die
  Fachliteratur beschreibt die Novellierung der Norm `[Q07][Q25]`. Wer heute nachweist, muss die im Gesetz
  zitierte Fassung und die vertraglich vereinbarte auseinanderhalten.

---

## 2. Wo dämmen — Bauteile und ihre Regeln

### 2.1 Die gesetzlichen U-Werte (GModG Anlage 7, § 36)

Wer ein Bauteil ersetzt, erstmals einbaut oder außenseitig eine Dämmschicht aufbringt, muss diese Höchstwerte
einhalten `[Q01]`:

| Bauteil | U_max [W/(m²K)] | Nr. in Anlage 7 |
|---|---|---|
| Außenwand (Ersatz, erstmaliger Einbau, Aufbringen von Dämmschichten, Putzerneuerung) | **0,24** | 1a/1b |
| Fenster, Fenstertüren (Uw) | 1,3 | 2a |
| Dachflächen, oberste Geschossdecke gegen unbeheizt, Abseitenwände | **0,24** | 5a/5b |
| Dachfläche mit Abdichtung (Ersatz der Abdichtung) | **0,20** | 5c |
| Wände gegen Erdreich/unbeheizt, Decken nach unten gegen Erdreich/unbeheizt | **0,30** | 6a/6b |
| Decken nach unten gegen Außenluft | 0,24 | 6d/6e |
| Decken nach unten, wenn nur der Fußbodenaufbau erneuert wird | 0,50 | 6c |

**Die wichtigste Fußnote der ganzen Anlage:** Ist die Dämmdicke **aus technischen Gründen begrenzt** (Sparrenhöhe,
Laibung, Deckenhöhe), gilt die Anforderung als erfüllt, wenn die höchstmögliche Dicke eingebaut wird — mit
**λ = 0,035** als Bemessungswert, bei **Einblasdämmung und nachwachsenden Rohstoffen λ = 0,045** `[Q01]`. Das ist
der legale Weg für die Kellergeschossdecke und für jedes Altbaudach: nicht „irgendwie dick", sondern
„nachweislich so dick wie möglich, mit dem richtigen λ".

Der Referenzwert für den Wärmebrückenzuschlag im Nachweis ist **ΔU_WB = 0,05 W/(m²K)** `[Q02]` — die Zahl, gegen
die jeder Detailplaner arbeitet (§ 4).

### 2.2 Dachschräge

Drei Lagen sind zu unterscheiden: **Zwischensparrendämmung** (im Gefach, günstig, durch Sparrenhöhe begrenzt),
**Untersparrendämmung** (darunter, kostet Höhe, bricht die Wärmebrücke Sparren) und **Aufsparrendämmung** (über
den Sparren, dämmt fugenfrei und deckt die Sparren thermisch ab, teuer, Dachhaut muss runter).

Die Reihenfolge von innen nach außen ist bei jeder Variante: **Dampfbremse luftdicht — Dämmung fugenfrei —
Unterdeckbahn/wasserführende Ebene — Hinterlüftung — Deckung**. Fehlt das Unterdach, darf keine Dämmung eingebaut
werden, bevor es hergestellt ist; sonst tropft Flugschnee oder eine defekte Pfanne direkt in die Matte `[Q28]`.
Für die Dampfbremse gilt: Stöße und Durchdringungen verklebt, Anschluss an Mauerwerk und Kehlbalken dauerhaft
luftdicht — „luftdicht" heißt hier **gasdicht**, weil der Wasserdampf sonst mit der Konvektion nach außen wandert
und an der kalten Schicht kondensiert `[Q28][Q08]`.

Dicke: 20 cm zwischen den Sparren sind bei 8×20er Sparren das Maximum; wer auf U = 0,20 will, braucht bei
λ 0,035 rund 15 cm **plus** eine zweite Ebene, weil der Sparren selbst die Wärmebrücke ist (Nadelholz
λ ≈ 0,13 `[Q24]` — der Sparren leitet fast viermal so gut wie die Dämmung).

### 2.3 Oberste Geschossdecke — die billigste Dämmung, die es gibt

Wenn das Dachgeschoss unbeheizt bleibt, ist die Decke der richtige Ort: technisch einfach, keine Dampfbremse
nötig (Beton ist luftdicht), keine Gerüstkosten, in Eigenleistung machbar `[Q16]`. Und es gibt eine **Pflicht**:

**§ 35 GModG** verlangt, dass oberste Geschossdecken, die den Mindestwärmeschutz nach DIN 4108-2 nicht erfüllen,
so gedämmt werden, dass **U ≤ 0,24** erreicht wird; ersatzweise darf das darüberliegende Dach gedämmt werden `[Q03]`.
Ausnahmen: Bei einem Wohngebäude mit **höchstens zwei Wohnungen**, von denen der Eigentümer eine am **01.02.2002
selbst bewohnt hat**, greift die Pflicht erst beim Eigentümerwechsel, mit **zwei Jahren Frist**; außerdem entfällt
sie, soweit sich die Aufwendungen nicht „innerhalb angemessener Frist" durch Einsparungen erwirtschaften lassen
`[Q03]`. Achtung Quellenlage: Die Verbraucherzentrale (Stand 28.09.2026) beschreibt dieselbe Pflicht, nennt aber
keinen Paragraphen und schreibt weiter „GEG" `[Q16]` — der belastbare Text ist § 35 GModG.

Praxis: Auf einer Betondecke werden Matten oder Platten **lose** verlegt, lückenlos bis zum Rand und um Rohre
herum; die Luftdichtheit kommt vom Beton. Bei Holzbalkendecken ist genau das anders — dort braucht es eine
zusätzliche Dichtigkeitsebene, sonst bläst die warme Luft in die Dämmung `[Q16]`. Einblasdämmung ist hier die
schnellste Lösung und füllt auch die Randbereiche.

### 2.4 Fassade: WDVS oder Vorhangfassade

**WDVS** (Wärmedämmverbundsystem) ist der Standard: Platten vollflächig und fugenfrei kleben, dübeln, Gewebe in
die Armierung einbetten, Putz. Kosten **160–190 €/m²** komplett (Material, Arbeit, Gerüst) `[Q15]`. Fällt das
Gerüst ohnehin an, kostet die Dämmschicht allein nur noch **90–100 €/m²** `[Q15]` — der Grund, warum „Fassade
sanieren" und „Fassade dämmen" zusammen gedacht werden müssen.

**Vorhangfassade** (hinterlüftete Fassade, VHF) ist teurer, aber die konstruktiv ehrliche Lösung: Unterkonstruktion
vor der Dämmung, Hinterlüftungsebene, beliebige Bekleidung. Sie entkoppelt Dämmung und Witterung, ist bei
Holzbau, hohen Gebäuden und Denkmal oft die einzige Option und hat eigene U-Werte im Gesetz (Vorhangfassade
Uc = 1,5 bei Ersatz, Anlage 7 Nr. 2d `[Q01]`).

Die drei Fehler, die ein WDVS ruinieren: **nicht fugenfrei verklebt** (Hohlraum hinter der Dämmung → Konvektion,
Dämmung wirkungslos), **keine Abschlussschiene unten** (Mäuse und Marder graben Gänge in die Platten), **Dübel
ohne thermische Trennung** (im Beispiel 40–50 Wärmebrücken, Folge Schwarzalgen auf der Fassade — Algen, nicht
Schimmel) `[Q28]`.

### 2.5 Kellerdecke

Der Keller ist das am meisten unterschätzte Wärmeleck: **5–10 %** der Heizenergie gehen darüber verloren, eine
Dämmung reduziert diesen Verlust um **mehr als die Hälfte**, was etwa **5 % der Heizkosten** entspricht `[Q14]`.
Kosten: **18–30 €/m²** von unten (auch als Einblasdämmung) `[Q14]`. Dicke: **4–12 cm** von unten, **5 cm** reichen
von oben, weil dort die Raumhöhe limitiert `[Q14]`.

Der Vorteil ist die λ-Freiheit: Weil nur wenig Höhe da ist, nimmt man einen Stoff mit besserem λ (PUR/PIR,
Mineralwolle hoher Güte) statt mehr Dicke — genau der Fall, für den die Fußnote in § 2.1 („technisch begrenzt,
höchstmögliche Dicke") geschrieben wurde. Zwingend: Platten **fugenlos und ohne Hohlräume** an die Decke, Rohre
zuerst dämmen, dann die Fläche; die Kellerwände müssen trocken sein, sonst dämmt man Feuchte ein `[Q14]`.

**Die Rechnung, die man kennen sollte** (gerechnet): 100 m² Kellerdecke kosten 1.800–3.000 €. Bei 15.000 kWh
Gasverbrauch und 12 ct/kWh sind 5 % Einsparung **90 €/a** — Amortisation **20–33 Jahre**. Die Maßnahme ist
trotzdem sinnvoll (Behaglichkeit, kein kalter Boden, Gebäudehülle geschlossen), aber sie ist **keine**
Goldgrube. Wer mit „rentabelste Maßnahme" wirbt, meint meist die niedrigen Kosten, nicht die lange Laufzeit.

### 2.6 Kellerwand außen (Perimeter)

Erdberührte Bauteile sind ein anderes Klima: ständig feucht, kein Frost, dafür Salz und Druck. Zulässig sind
deshalb nur **feuchteresistente Stoffe — XPS, PUR, Schaumglas** `[Q19]`; Mineralwolle und Holzfaser scheiden aus.
Der Aufbau ist von außen nach innen: Abdichtung nach DIN 18533, **Schutzlage/Perimeterdämmung**, Drainage,
wiederverfüllter Boden. Die Dämmung sitzt **außerhalb** der Abdichtung und schützt sie gleichzeitig mechanisch.

Wer nur die Kellerdecke dämmt, lässt die Kellerwand als „Kühlrippe" stehen. Die Verbraucherzentrale nennt den
pragmatischen Kompromiss: die **oberen 50 cm der Kellerwand** mitdämmen, etwa **6 cm** Dicke, weil dort der
Übergang zur Außenwand liegt `[Q16]`.

### 2.7 Innendämmung — die riskanteste Variante

Innendämmung ist die einzige Dämmung, die den Taupunkt **in die Wand verschiebt** und damit Feuchte erzeugt, die
vorher nicht da war `[Q28]`. Sie ist trotzdem richtig — aber nur unter Bedingungen: denkmalgeschützte Fassade,
einzelne Wohnung, keine außenseitige Möglichkeit.

Bautechnisch gilt: **kapillaraktiv** dämmen (Holzfaser, Calciumsilikat, Mineralschaum) und raumseitig eine
Dampfbremse mit definiertem sd-Wert, die Anschlüsse luftdicht. Calciumsilikat hat λ 0,05–0,07 und wird wegen
seines hohen pH-Werts und der Kapillarität für genau diese Fälle eingesetzt `[Q19]`. Ein Luftspalt zwischen
Dämmung und Wand ist ein Fehler, keine Entkopplung: dort zirkuliert Raumluft und kondensiert `[Q28]`.

**Wichtig gegen ein verbreitetes Missverständnis:** DIN 4108-3 führt „Wände mit Innendämmung ohne
Schlagregenbeanspruchung" ausdrücklich unter den **nachweisfreien Konstruktionen** `[Q08]`. „Ohne Feuchtenachweis"
ist also nicht automatisch ein Pfusch — es ist der Normalfall für diese Konstruktion, **sofern** der Mindestwärmeschutz
und die luftdichte Ausführung nach DIN 4108-7 eingehalten sind. Ein Nachweis ist Pflicht, sobald die Konstruktion
nicht in dieser Liste steht (Schlagregen, Holz, Sonderaufbau).

### 2.8 Sockel

Der Sockel ist die Zone, in der drei Probleme zusammenkommen: Spritzwasser, Erdfeuchte, und der Übergang von
der außen liegenden WDVS-Ebene zur Perimeterdämmung. Deshalb: im Spritzwasserbereich **Schaumglas oder XPS**
(Schaumglas ist dampfdicht und frostfest), keine saugende Dämmung, keine Mineralwolle. Und die schon genannte
**Abschlussschiene** an der Unterkante des WDVS — sie ist der Unterschied zwischen einer Fassade und einem
Mäusebau `[Q28]`.

### 2.9 Rollladenkästen

Ein ungedämmter Rollladenkasten im Altbau hat **U ≈ 2,0 W/(m²K) oder schlechter** — über dieses eine Bauteil
geht ähnlich viel Wärme verloren wie über eine schlecht gedämmte Außenwand. Zielwert: **≤ 0,5 bis 1,0**, ab
**1,5** gilt der Kasten als sanierungsbedürftig `[Q26]`. Moderne Aufsatzkästen erreichen 0,5–0,9 `[Q26]`.

Der Fehler ist fast nie die Dämmstärke, sondern die **Luftdichtheit**: die Öffnung für den Panzer und der
Anschluss an Fensterrahmen und Wand sind die Wege, über die Kaltluft einfällt. Deshalb: Kasten innen dämmen
(Platten zuschneiden, fugenfrei), Panzeröffnung mit Bürstendichtung, Anschlüsse luftdicht — und wenn ohnehin
Fenster getauscht werden, den Kasten mitmachen `[Q26]`.

### 2.10 Rohrleitungen — die Zahlen stehen im Gesetz

Anlage 8 GModG schreibt Mindestdicken vor, bezogen auf **λ = 0,035 bei 40 °C Mitteltemperatur** `[Q05]`:

| Innendurchmesser | Mindestdicke |
|---|---|
| bis 22 mm | **20 mm** |
| > 22 bis 35 mm | **30 mm** |
| > 35 bis 100 mm | **gleich dem Innendurchmesser** |
| > 100 mm | **100 mm** |

Halbiert wird die Dicke in Wand- und Deckendurchbrüchen, an Kreuzungen, Verbindungsstellen und zentralen
Verteilern; verdoppelt, wenn die Leitung an Außenluft grenzt. Für Kälte-/Kaltwasserleitungen gilt 9 mm (bis
22 mm) bzw. 19 mm, bezogen auf 10 °C `[Q05]`. Heizungsrohre im unbeheizten Keller sind damit nicht „Kür", sondern
Pflicht — und die billigste Einzelmaßnahme im ganzen Haus (Material zweistellig pro Meter, Arbeit in Stunden).

---

## 3. Bauphysik — das Handwerkszeug

### 3.1 U-Wert, R-Werte, Rechenweg

Der Wärmedurchgangskoeffizient ist der Kehrwert der Summe aller Widerstände:

```
U = 1 / (Rsi + Σ d_i/λ_i + Rse)          [W/(m²K)]
```

- **Rsi** (innen) = **0,13**, **Rse** (außen) = **0,04** m²K/W bei Wänden (horizontaler Wärmestrom)
  `[Q27][Q12]`; bei Decken/Böden gegen Außenluft andere Werte (Rsi 0,10 bzw. 0,17) `[Q27]`.
- **d/λ** ist der Wärmedurchlasswiderstand jeder Schicht. 10 cm bei λ 0,035 ergeben **R = 2,86** `[Q27]`.
- **Nur der Bemessungswert λB darf verwendet werden**, nicht der Nennwert λD: Bei einer Steinwollplatte stehen
  0,037 (Nennwert) gegen **0,038** (Bemessungswert) — der Bemessungswert enthält Feuchte und Alterung `[Q09]`.
  Wer mit dem Nennwert rechnet, rechnet sich die Wand schön.

**Beispiel (gerechnet):** 24 cm Kalksandstein λ 0,8 → R = 0,30; 16 cm EPS λB 0,035 → R = 4,57; plus 0,13 + 0,04
= **R_ges 5,04** → **U = 0,198 W/(m²K)**. Ohne Dämmung wäre dieselbe Wand bei U = 2,13 — Faktor 10.

### 3.2 Tauwasser: das Glaser-Verfahren und seine Grenzen

DIN 4108-3 ist die Norm für den klimabedingten Feuchteschutz; ihr rechnerisches Kernstück ist das
**Glaser-Verfahren**: es vergleicht den Dampfdruckverlauf mit dem Sättigungsdampfdruck im Bauteil und ermittelt,
wo und wie viel Tauwasser im Winter ausfällt `[Q08]`.

Tauwasser ist **nicht grundsätzlich verboten**. Unschädlich ist es, wenn `[Q08]`:

- das Wasser in der Tauperiode (Winter) anfällt und in der Verdunstungsperiode (Sommer) wieder abgegeben wird,
- die Baustoffe nicht geschädigt werden (kein Pilz, keine Korrosion),
- die Tauwassermasse in Dach- und Wandkonstruktionen **≤ 1,0 kg/m²** bleibt — und **≤ 0,5 kg/m²**, wenn
  nicht kapillar aufnehmende Schichten beteiligt sind (Folien, Metalle, Normalbeton, Mineralwolle, EPS, XPS, PU),
- bei Holzkonstruktionen zusätzlich der massebezogene Feuchtegehalt **≤ 5 %** (Holz) bzw. **≤ 3 %**
  (Holzwerkstoffe) bleibt.

Für beidseitig eingeschlossene Holzbauteile fordert DIN 68800-2 zusätzliche **Trocknungsreserven**: ≥ 250 g/(m²·a)
bei Dächern, ≥ 100 g/(m²·a) bei Decken und Wänden `[Q08]`. Das ist die Zahl, die man in der Diskussion „diffusionsoffen
oder Dampfsperre" selten hört — sie sagt: es geht nicht um dicht oder offen, sondern um **Trocknungsreserve**.

**Nachweisfrei** sind laut DIN 4108-3 u. a. einige Massivwände, Wände mit Innendämmung ohne Schlagregen,
Holzwände nach DIN 68800-2, erdberührte Wände mit Bauwerksabdichtung/Perimeterdämmung, Bodenplatten mit
Perimeterdämmung, Außenwände mit zugelassenem WDVS und Warmdächer mit raumseitigem sd ≥ 100 m (ohne Holzbauteile
dazwischen) `[Q08]`. Wer eine dieser Konstruktionen baut, braucht keinen Glaser-Nachweis — aber die
Randbedingungen müssen exakt passen.

### 3.3 sd-Wert und die Richtung der Dampfbremse

Der sd-Wert ist die **diffusionsäquivalente Luftschichtdicke**: `sd = d · μ` in Metern `[Q11]`. Er ist die
praktischere Größe als μ, weil er die Dicke mitrechnet. Beispiel: Holzfaser μ = 2, 40 mm dick → sd = 0,08 m `[Q21]`.

Die eine Regel, die zählt: **Die sd-Werte müssen von innen nach außen abnehmen** `[Q11]`. Wird außen dichter
gebaut als innen, kann die Feuchte nicht raus. Daraus folgt für die Praxis:

- Dampfsperre (sd ≫ 100 m) nur, wenn außen eine dampfdichte Schicht liegt (Flachdach, Warmdach).
- Dampfbremse (sd einige Meter) bei diffusionsoffenem Aufbau, Dimensionierung nach DIN 4108-3.
- Bei Innendämmung liegt die Bremse **raumseitig**, direkt hinter der Bekleidung — nicht in der Mitte.

### 3.4 Luftdichtheit

Luftdichtheit ist keine Dämmung, sondern die **Voraussetzung** dafür. Die winddichte Ebene liegt raumseitig
(meist die Dampfbremse), die winddichte Ebene außen ist die Unterspannbahn. Jede Durchdringung — Kabel, Rohr,
Dachfenster, Kehlbalken, Mauerwerksauflager — wird verklebt oder mit einer Manschette angeschlossen. Ein
durchgehender Spalt macht die Fläche wertlos, weil dort mehr Wärme transportiert wird als durch die ganze
Dämmfläche diffundiert `[Q28]`.

Der Nachweis läuft über den **n₅₀-Wert** (Luftwechsel bei 50 Pa); das GModG-Referenzgebäude setzt eine
Dichtheitsprüfung an `[Q02]`. Für die Praxis: Blower-Door-Test **vor** dem Schließen der Bekleidung, nicht
danach.

### 3.5 Sommerlicher Wärmeschutz — das komplett fehlende Thema

§ 14 GModG verlangt, dass der Sonneneintrag durch ausreichenden baulichen sommerlichen Wärmeschutz begrenzt wird
`[Q04]`. Zwei Wege sind zugelassen:

1. **Sonneneintragskennwert** (S_vorh ≤ S_zul) nach DIN 4108-2 Abschnitt 8.3 — das vereinfachte Verfahren `[Q04][Q07]`.
2. **Simulation** nach Abschnitt 8.4, wenn der Nachweis zeigt, dass die **Übertemperatur-Gradstunden** nach
   Tabelle 9 nicht überschritten werden `[Q04]`.

Die Zahlen, die man kennen muss: **≤ 1.200 Kh/a für Wohngebäude**, **≤ 500 Kh/a für Nichtwohngebäude** `[Q25]`.
Ein Nachweis ist überhaupt erst zu führen, wenn der Fensterflächenanteil die Grenzwerte überschreitet — bei
vertikalen Fenstern liegt die Schwelle bei **mehr als 35 % der Grundfläche** des Raumes `[Q07]`. Dazu kommen die
drei **Sommer-Klimaregionen** (Karte in der Norm), die Wärmespeicherfähigkeit der Bauart (leicht/mittel/schwer),
Nachtlüftung, Sonnenschutzverglasung, Fensterneigung und Orientierung `[Q07]`.

**Warum das ein Dämmthema ist:** Dämmung wirkt im Sommer anders als im Winter. Entscheidend ist nicht λ, sondern
die **Wärmespeicherfähigkeit c** der Schichten innen: Holzfaser (c 2.100–2.500) und Zellulose (1.800–2.200)
puffern Temperaturspitzen, EPS (1.500) und Mineralwolle (830–1.000) tun das kaum `[Q19]`. Eine außen liegende
Dämmung mit hoher Speicherfähigkeit plus innen liegende schwere Bauteile (Massivdecke, Estrich) sind der
physikalisch richtige Aufbau; eine Leichtbaukonstruktion mit Südverglasung ohne außenliegenden Sonnenschutz
überhitzt trotz 30 cm Dämmung.

**Der Fehler, der teuer wird:** sommerlichen Wärmeschutz erst zu prüfen, wenn die Fenster bestellt sind. Der
wirksamste Hebel ist der **außenliegende** Sonnenschutz (Fc-Wert), nicht die Verglasung — und er muss im
Schnittstellendetail der Fassade mitgeplant sein. Das GModG fördert ihn als eigene Maßnahme, wenn er im Zuge
der Fassadendämmung eingebaut wird `[Q18]`.

---

## 4. Wärmebrücken

**Definition:** Eine Wärmebrücke ist eine Stelle der Gebäudehülle, an der der Wärmestrom pro Fläche größer ist als
in der ungestörten Fläche — wegen Geometrie (Ecke, Laibung), Materialwechsel (Beton ins Mauerwerk, Stahlträger)
oder Luftzug (Spalt). Folge: kältere Innenoberfläche, höheres Schimmelrisiko, mehr Verbrauch.

**Bilanzierung** — drei Stufen, alle in DIN 4108 Beiblatt 2 `[Q10]`:

| Nachweis | Wärmebrückenzuschlag ΔU_WB |
|---|---|
| pauschal, ohne Nachweis | **0,10 W/(m²K)** |
| Gleichwertigkeit Kategorie A (Details aus Bildvorlagen) | **0,05 W/(m²K)** |
| Gleichwertigkeit Kategorie B (vollständig) | **0,03 W/(m²K)** |

Bei 200 m² Hüllfläche ist der Unterschied zwischen 0,10 und 0,03 **14 W/K**. Über 65 kKh/a sind das rund
**910 kWh/a** (gerechnet) — mehr als der halbe Heizwärmebedarf eines Effizienzhauses. Wärmebrücken sind deshalb kein
Akademikerproblem, sondern die zweite große Verlustquelle nach der undichten Dampfbremse.

**Typische Stellen** (alle aus den Video-Fällen und der Fachliteratur):

- **Fensterleibung**, wenn sie nicht in die Dämmebene gezogen wird → Schimmel in der Laibung `[Q28]`
- **Deckenauflager** und **Balkonplatten**, die durch die Dämmung stoßen (der Klassiker: Stahlbeton λ ≈ 2,1)
- **Ecken** (geometrisch bedingt, auch ohne Materialfehler)
- **Dübel** im WDVS ohne thermische Trennung — 40–50 Stück pro Fassade `[Q28]`
- **Rollladenkästen** und **Heizkörpernischen**, die nicht mitgedämmt werden `[Q26]`
- **Sparren** im Dach (Holz λ ≈ 0,13 gegen Dämmung 0,035) `[Q24]`
- **Übergang Sockel/Perimeter** und **Kellerdecke zur Außenwand** `[Q16]`

**Vermeiden** heißt fast immer dasselbe: die Dämmebene **durchlaufen lassen**, nicht unterbrechen. Konkret:
Laibung dämmen, Fenster in die Dämmebene setzen, Balkon thermisch trennen (Isokorb), Rollladenkasten in die
Dämmung einbinden, obere 50 cm der Kellerwand mitdämmen `[Q16]`, Dübel mit Kunststoffteller oder
thermisch getrennte Befestiger. Was man nicht durchlaufen lassen kann (Kerndämmung im zweischaligen Mauerwerk),
wird raumseitig mit kapillaraktivem Material (Calciumsilikat) entschärft `[Q28]`.

---

## 5. Dämmstärken und Wirtschaftlichkeit

### 5.1 Was „richtig dick" heißt

Die gesetzlichen U_max-Werte (§ 2.1) sind **Mindestanforderungen**, keine Zielwerte. Die übliche Sanierungspraxis
liegt bei **20–30 cm** Dämmdicke `[Q13]`. Für U = 0,20 braucht man bei λ 0,035 rund **15 cm**, bei λ 0,040 rund
**17 cm**, bei λ 0,025 rund **11 cm** — gerechnet mit der Formel aus 3.1 und einem Wand-R von **0,50 m²K/W**
(die Wand aus Fall A in 5.2). Bei einer besser gedämmten Bestandswand entsprechend weniger.

Merksatz: **U = 0,24 ist die Pflicht, U = 0,20 ist die Vernunft, U = 0,15 ist das Passivhaus-Niveau** — und
unterhalb von 0,15 ändert sich am Verbrauch fast nichts mehr, weil dann Fenster, Lüftung und Wärmebrücken
dominieren.

### 5.2 Der Grenznutzen — warum „mehr ist besser" falsch ist

Die Verbraucherzentrale rechnet zwei Fälle, die zusammen die ganze Ökonomie erklären `[Q15]`:

**Fall A — ungedämmte Wand, 110 m², U 1,5:** 16 cm Dämmung senken U auf **0,19** (−87 %). Bei 65 kKh/a und
12 ct/kWh ergibt das **9.370 kWh/a** und **1.120 €/a**. Die Maßnahme kostet 110 m² × 175 €/m² − 15 % Förderung =
**16.360 €** → Amortisation **14–15 Jahre**. Fällt das Gerüst ohnehin an, kostet die Dämmung nur 90–100 €/m² und
die Amortisation sinkt auf **etwa 8 Jahre** `[Q15]`.

**Fall B — Wand mit 6 cm Dämmung aus den 1980ern, 90 m², U 0,50:** Weitere 12 cm senken U auf **0,18** (−64 %).
Ersparnis: 1.870 kWh/a × 8,9 ct/kWh (Wärmepumpe, JAZ 2,8) = **170 €/a**. Kosten: 14.900 € − 15 % = **12.655 €**
→ **über 70 Jahre** Amortisation. Fazit der Quelle: „Unter diesen Voraussetzungen rechnet sich eine zusätzliche
Dämmung also nicht" `[Q15]`.

Das ist der belastbare Kern der Grenznutzen-Debatte: **nicht die Dicke an sich ist das Problem, sondern die
zweite Dämmebene auf einer schon gedämmten Fläche.** Die erste Schicht holt 87 % des Potenzials, die zweite
vielleicht 5 % — kostet aber wieder Gerüst, Anschlüsse und Fensterlaibungen.

**Die Rechnung in kleinen Schritten** (gerechnet, gleiche Wand wie Fall A, 65 kKh, 12 ct/kWh):

| Dämmung | U | Ersparnis gesamt | Zuwachs gegenüber vorher |
|---|---|---|---|
| 16 cm | 0,191 | 10,21 €/m²·a | — |
| 20 cm | 0,157 | 10,48 €/m²·a | +0,27 €/m²·a für 4 cm |
| 24 cm | 0,133 | 10,66 €/m²·a | +0,19 €/m²·a für 4 cm |
| 30 cm | 0,108 | 10,86 €/m²·a | +0,19 €/m²·a für 6 cm |

Der erste Zentimeter bringt am meisten, der zwanzigste fast nichts. **Aber:** Bei EPS kostet ein Zentimeter
Material etwa 0,63 €/m² (abgeleitet aus 10 €/m² bei 16 cm `[Q13]`) — 4 cm kosten also rund 2,50 €/m² und
sparen 0,27 €/m²·a, Amortisation **etwa 9 Jahre** (gerechnet). Bei billigem Material und ohnehin laufender
Baustelle ist „dicker" also **ökonomisch richtig**. Falsch wird es bei teuren Stoffen (VIP, Schaumglas), bei
begrenztem Platz und bei der zweiten Lage auf einer gedämmten Wand. Die Regel lautet deshalb nicht „mehr ist
besser", sondern: **jede zusätzliche Schicht muss ihre eigene Amortisation tragen.**

### 5.3 Förderung 2026 (BAFA, BEG EM)

Stand 09.11.2026, geprüft auf der BAFA-Seite `[Q18]`:

- **Grundfördersatz 15 %** der förderfähigen Ausgaben (nicht 20 % — der alte Merksatz „15 + 5 iSFP" gilt nur
  oberhalb einer Schwelle).
- **iSFP-Bonus 5 %** erst ab **30.000 €** förderfähigem Mindestinvestitionsvolumen bei einer Wohneinheit; der
  Bonus gilt nur für den Betrag **über** dieser Schwelle.
- **Höchstgrenze 30.000 €** förderfähige Ausgaben für die erste Wohneinheit (60.000 €, wenn der iSFP-Bonus
  greift oder der Eigentümer nicht iSFP-antragsberechtigt ist); 15.000 € je weiterer WE (2.–6.), 8.000 € ab der 7.
- **Mindestinvestition 300 €** brutto.
- **WPB-Bonus** (Worst Performing Building) für Dämmmaßnahmen voraussichtlich **ab Q1 2027**, nur im Zusammenhang
  mit einer geförderten Energieberatung, maximal drei Anträge.
- **Antrag nur mit Energieeffizienz-Experten (EEE)**; gefördert werden u. a. Dämmung der Gebäudehülle
  (Außenwände, Dachflächen, Geschossdecken, Bodenflächen) und **außenliegender Sonnenschutz** `[Q18]`.

Wichtig für die Rechnung: Die Förderung bemisst sich an **Ausgaben**, nicht an U-Werten — sie senkt die
Investition, nicht den Verbrauch. Und sie ist der Grund, warum die Verbraucherzentrale in beiden Beispielen mit
15 % rechnet `[Q15]`.

### 5.4 Was eine Dämmmaßnahme wirklich kostet

| Maßnahme | Kosten | Quelle |
|---|---|---|
| WDVS komplett (Material, Arbeit, Gerüst) | 160–190 €/m² | `[Q15]` |
| Dämmschicht allein, Gerüst steht schon | 90–100 €/m² | `[Q15]` |
| Kellerdecke von unten / Einblasdämmung | 18–30 €/m² | `[Q14]` |
| Dämmstoff EPS / Glaswolle / Steinwolle (Material) | 10 / 8 / 11 €/m² | `[Q13]` |
| Dämmstoff Holzfaser / Zellulose (Material) | 21–22 / 20 €/m² | `[Q13]` |

Die Schere zwischen 10 €/m² Material und 175 €/m² Gesamtkosten ist die eigentliche Botschaft: **Dämmung ist zu
85 % Handwerk und Logistik.** Wer Kosten sparen will, spart an der Zahl der Gewerke und am Gerüst — nicht am
Dämmstoff.

---

## 6. Die Fehler, die Geld kosten

Alle mit Quelle; die Video-Fälle mit Zeitmarke im Transkript (`references/transkripte/TszegjPc69w.txt`).

1. **Zu dünn gedämmt, „weil billig".** Obere Geschossdecke mit 20 cm statt 40–50 cm: Materialkosten sind der
   kleine Anteil, die Arbeit dominiert `[Q28, 00:01:08]`. *Gegenposition:* bei technisch begrenzter Dicke ist
   „höchstmögliche Dicke" die normative Erfüllung `[Q01]`.
2. **WDVS nicht fugenfrei verklebt** (kein Punkt-/Wulst-Batzen-Verfahren): Luft strömt hinter der Dämmung von
   unten nach oben, die Außendämmung ist wirkungslos `[Q28, 00:02:41]`.
3. **Hohlraum nicht erkannt:** 2–3 cm Luft rund ums Haus sind bei 7 m³ Füllvolumen eine Größenordnung, die man
   **vor** dem Verputzen kontrolliert und schließt `[Q28, 00:03:50]`.
4. **Innendämmung mit Luftspalt** erzeugt einen Taupunkt in der Wand; nur vollflächig, fugenfrei verklebt, mit
   Dampfbremse und luftdichten Anschlüssen `[Q28, 00:04:37]`. Muffiger Geruch ist das Indiz.
5. **Tiere im WDVS:** ohne **Abschlussschiene unten** graben Mäuse und Marder Gänge in die Platten, Kot im
   Hohlraum; kein Gift in der Dämmebene `[Q28, 00:05:22]`.
6. **Dachdämmung innen ohne wasserführendes Unterdach und ohne Dampfbremse:** Wasser darf nie in den Dämmstoff
   tropfen; im Altbau fehlt das Unterdach häufig `[Q28, 00:06:07]`.
7. **Fensterleibung nicht in die Dämmung gezogen** → Wärmebrücke, Schimmel in der Laibung. Bei Kerndämmung im
   zweischaligen Mauerwerk ist die Wärmebrücke nicht beseitigbar; dann Calciumsilikat raumseitig `[Q28, 00:08:00]`.
8. **Dämmstoff zusammengepresst:** gequetschte Matten haben keine Lufteinschlüsse mehr, Glasfaser liegt an
   Glasfaser, die Dämmwirkung bricht ein — trotzdem fugenfrei anliegen `[Q28, 00:11:03]`.
9. **Fugen mit Mörtel oder Putz verfüllt:** Mörtel leitet Wärme, die Fuge bleibt Wärmebrücke `[Q28, 00:14:30]`.
10. **Plattenware im Dach/Leichtbau:** starre Platten lassen sich zwischen Sparren nicht fugenfrei einbauen →
    Matten oder Einblasdämmung `[Q28, 00:15:18]`.
11. **Fehlende Dampfbremse im Leichtbau** und **Dübel-Wärmebrücken** (40–50 Stück) `[Q28, 00:16:27, 00:12:11]`.
12. **Sommerlichen Hitzeschutz ignoriert.** Wer nur auf λ schaut, kauft eine Dämmung, die im Winter gut und im
    Sommer nutzlos ist; c und außenliegender Sonnenschutz entscheiden `[Q19][Q04]`.
13. **Innendämmung ohne Prüfung der Nachweisfreiheit.** Zulässig ist der Verzicht auf den Glaser-Nachweis nur
    für die in DIN 4108-3 genannten Konstruktionen; bei Schlagregen oder Holzbauteilen ist er Pflicht `[Q08]`.
14. **Dämmung unter der Bodenplatte vergessen.** Wer im Neubau oder bei komplettem Fußbodenaufbau die
    Dämmung unter der Platte (Perimeterdämmung, Schaumglas-Schotter) weglässt, kann sie später nur mit
    Aufbauhöhe nachholen `[Q19][Q14]`.
15. **Rohrleitungen nicht gedämmt**, obwohl Anlage 8 Mindestdicken vorschreibt (20/30/DN/100 mm) `[Q05]`.
16. **KMF ohne Schutz verarbeitet.** Alte Glaswolle (vor 1996) gilt als krebserregend; neue Wolle reizt Haut und
    Atemwege — Handschuhe, Atemschutz, keine offene Haut `[Q13]`.
17. **U-Wert mit dem Nennwert gerechnet** statt mit dem Bemessungswert: 0,037 vs. 0,038 klingt nach nichts,
    ist aber ein systematischer Fehler in jedem Nachweis `[Q09]`.

---

## 7. Eigenleistung — was geht und was nicht

**Geht selbst (mit Plan und Zeit):**

- **Kellerdeckendämmung von unten.** Der dankbarste Einstieg: 18–30 €/m² Material `[Q14]`, keine Statik, keine
  Dampfbremse, überschaubare Fläche. Reihenfolge: Rohre zuerst dämmen, Decke säubern, Platten kleben/dübeln,
  fugenlos, Abschlüsse an den Wänden.
- **Oberste Geschossdecke (Massivdecke).** Matten oder Platten lose verlegen, Randanschlüsse lückenlos `[Q17]`; bei
  Betondecke ist die Luftdichtheit geschenkt `[Q16]`. Achtung: Begehbarkeit und Lasten klären, sonst
  Laufsteg planen.
- **Rohrisolierung.** Die gesetzlichen Dicken stehen in Anlage 8 `[Q05]`; Schalen zuschneiden, kleben, an
  Armaturen und Bögen sauber anschließen. Materialkosten zweistellig, Wirkung sofort.
- **Rollladenkasten innen dämmen.** Zuschnitt, fugenfrei, Panzeröffnung abdichten `[Q26]` — solange der Kasten
  zugänglich ist und die Fenster nicht getauscht werden.
- **Einblasdämmung der obersten Geschossdecke** — prinzipiell machbar mit Leihmaschine, **aber** der Fehler ist
  programmiert: zu locker eingeblasen setzt sich die Zellulose, oben bleibt ein Hohlraum `[Q28]`. Wer es selbst
  macht, muss die Einblasdichte und die Kontrolle der Randbereiche beherrschen.

**Geht nicht selbst (und warum):**

- **WDVS.** Gerüst, Verklebung, Gewebe, Putzsystem mit Gewährleistung — und die Haftung für Abplatzungen liegt
  beim Verarbeiter `[Q15][Q28]`.
- **Dachdämmung mit Dampfbremse.** Die luftdichte Ebene ist unsichtbar und die häufigste Schadensursache; ein
  Fehler zeigt sich erst nach Jahren als Holzfäule `[Q28]`.
- **Innendämmung** ohne bauphysikalische Prüfung (siehe 2.7) `[Q08]`.
- **Perimeterdämmung/Kellerabdichtung.** Abdichtung nach DIN 18533 ist Fachbetriebsarbeit; die Dämmung ist nur
  die Schutzlage darauf `[Q19]`.
- **Kerndämmung** im zweischaligen Mauerwerk: Ausbau der Vorsatzschale, Einblasen, Wiederherstellen der
  Schale — inklusive Wärmebrückenproblem in der Laibung `[Q28]`.
- **Alles, was gefördert werden soll:** Der BAFA-Antrag setzt einen Energieeffizienz-Experten voraus `[Q18]`;
  reine Eigenleistung hat keine Fachunternehmerrechnung und damit keine förderfähige Ausgabe.

**Realistische Zeitplanung:** Kellerdecke 100 m² = 2–3 Tage für zwei Personen (Schätzung). Oberste Geschossdecke
100 m² mit Einblasmaschine = 1 Tag (Schätzung). Rohrleitungen im Keller = 1 Tag (Schätzung).

---

## 8. Kontrollpunkte

Vor dem Dämmen:

- [ ] Ist die Fläche wirklich die **thermische Hülle**? (Kellerdecke ja, Kellerwand nur wenn unbeheizt)
- [ ] Sind Dachhaut, Unterdach und Anschlüsse **dicht**, bevor gedämmt wird `[Q28]`?
- [ ] Ist der Untergrund trocken, tragfähig, frei von Schimmel `[Q14]`?
- [ ] Welcher **U-Wert** ist heute da, welcher wird erreicht — mit **λB**, nicht λD `[Q09]`?
- [ ] Welche Bauteile sind **technisch begrenzt** (Sparrenhöhe, Deckenhöhe, Laibung) → höchstmögliche Dicke
      dokumentieren `[Q01]`.
- [ ] Ist der **sommerliche Wärmeschutz** mitgedacht (c, Sonnenschutz, Fensterflächenanteil) `[Q04][Q07]`?
- [ ] Ist die **Förderfähigkeit** vor der Bestellung geklärt (EEE, Antrag vor Vorhabenbeginn) `[Q18]`?

Während der Ausführung:

- [ ] Verklebung **vollflächig/fugenfrei**, Kontrolle vor dem Verputzen `[Q28]`.
- [ ] Dampfbremse: Stöße verklebt, Durchdringungen manschettiert, Anschlüsse an Mauerwerk/Kehlbalken dicht.
- [ ] Dämmung **nicht gequetscht**, keine Hohlräume an Sparren, Rohren, Laibungen `[Q28]`.
- [ ] Abschlussschiene am Sockel montiert `[Q28]`.
- [ ] Dübel thermisch getrennt, Anzahl minimiert `[Q28]`.

Nach der Ausführung:

- [ ] Blower-Door-Test **vor** der Bekleidung `[Q02]`.
- [ ] U-Werte je Bauteil dokumentiert (für Förderung und Energieausweis) `[Q18]`.
- [ ] Fotos von jeder Schicht, jede Durchdringung, jedes Detail — die einzige Beweislage bei Feuchteschäden.

---

## 9. Wann Fachbetrieb

| Maßnahme | Warum Fachbetrieb |
|---|---|
| WDVS/Fassade | Gerüst, Systemzulassung, Gewährleistung, Absturzsicherung |
| Dachdämmung mit Dampfbremse | luftdichte Ebene, Tauwasser, Holzfäule-Risiko |
| Innendämmung | Feuchtenachweis, Anschlüsse, kapillaraktives System |
| Perimeterdämmung / Kellerabdichtung | DIN 18533, Erddruck, Drainage |
| Kerndämmung | Ausbau/Wiederherstellung der Schale, Statik |
| KfW/BAFA-Förderung | EEE + Fachunternehmererklärung `[Q18]` |
| Statisch relevante Aufbauten (Aufsparrendämmung, Dachgauben) | Lastabtrag, Befestigung |

Der Unterschied zwischen „selbst gemacht" und „fachgerecht" ist bei Dämmung fast nie sichtbar — er zeigt sich
in der **Luftdichtheit** und in den **Anschlüssen**. Genau dort entstehen die Schäden, und genau dort ist die
Gewährleistung des Handwerkers (§ 634a BGB, 5 Jahre) das eigentliche Produkt.

---

## 10. Quellen

Alle URLs am **09.11.2026** geprüft (HTTP 200, sofern nicht anders vermerkt).

**[Q01]** GModG (vormals GEG), **Anlage 7** (zu § 36) — Höchstwerte der Wärmedurchgangskoeffizienten von
Außenbauteilen bei Änderung an bestehenden Gebäuden. https://www.gesetze-im-internet.de/geg/anlage_7.html
*(Volltext selbst gelesen; U_max-Werte und Fußnote λ 0,035/0,045 wörtlich übernommen.)*

**[Q02]** GModG, **Anlage 1** (zu § 15 Abs. 1) — Technische Ausführung des Referenzgebäudes (Wohngebäude):
U-Werte 0,28/0,35/0,20/1,3, **ΔU_WB = 0,05 W/(m²K)**, n₅₀ mit Dichtheitsprüfung.
https://www.gesetze-im-internet.de/geg/anlage_1.html

**[Q03]** GModG, **§ 35** — Nachrüstung eines bestehenden Gebäudes (oberste Geschossdecke U ≤ 0,24, Ausnahmen,
Zwei-Jahres-Frist). https://www.gesetze-im-internet.de/geg/__35.html

**[Q04]** GModG, **§ 14** — Sommerlicher Wärmeschutz (Verweis auf DIN 4108-2:2013-02, Abschnitte 8.3/8.4).
https://www.gesetze-im-internet.de/geg/__14.html

**[Q05]** GModG, **Anlage 8** (zu §§ 69, 70) — Anforderungen an die Wärmedämmung von Rohrleitungen und
Armaturen. https://www.gesetze-im-internet.de/geg/anlage_8.html

**[Q06]** GModG, **Anlage 9** (zu § 85 Abs. 6) — Umrechnung in Treibhausgasemissionen (Emissionsfaktoren
g CO₂-Äq./kWh). https://www.gesetze-im-internet.de/geg/anlage_9.html

**[Q07]** BauNetz Wissen — *Sommerlicher Wärmeschutz nach DIN 4108-2* (Sonneneintragskennwert, 35 %-Schwelle,
drei Klimaregionen, Simulationsverfahren).
https://www.baunetzwissen.de/fassade/fachwissen/normen-verordnungen/sommerlicher-waermeschutz-nach-din-4108-2-1471925

**[Q08]** BauNetz Wissen — *Tauwasser und Glaser-Verfahren* (DIN 4108-3; 1,0/0,5 kg/m², 5 %/3 % Holzfeuchte,
sd ≥ 100 m, Trocknungsreserven 250/100 g/(m²·a), nachweisfreie Konstruktionen).
https://www.baunetzwissen.de/bauphysik/fachwissen/feuchteschutz/tauwasser-und-glaser-verfahren-4421843

**[Q09]** BauNetz Wissen — *Wärmeleitfähigkeit – Nennwert oder Bemessungswert?* (λD 0,037 vs. λB 0,038;
nur λB für den U-Wert).
https://www.baunetzwissen.de/daemmstoffe/fachwissen/richtlinien-verordnungen/waermeleitfaehigkeit--nennwert-oder-bemessungswert-3394755

**[Q10]** BauNetz Wissen — *Wärmebrückenbilanzierung nach DIN 4108 Beiblatt 2* (ΔU_WB 0,10 / 0,05 / 0,03).
https://www.baunetzwissen.de/bauphysik/fachwissen/waermeschutz/waermebrueckenbilanzierung-nach-din-4108-beiblatt-2-7496857

**[Q11]** BauNetz Wissen — *sd-Wert* (sd = d · μ; sd-Werte müssen von innen nach außen abnehmen).
https://www.baunetzwissen.de/bauphysik/fachwissen/feuchteschutz/sd-wert-4384605

**[Q12]** BauNetz Wissen — *Der U-Wert als bauphysikalische Kenngröße* (Definition, Bewertung von Außenbauteilen).
https://www.baunetzwissen.de/bauphysik/fachwissen/waermeschutz/der-u-wert-als-bauphysikalische-kenngroesse-4339151

**[Q13]** co2online — *Alle konventionellen Dämmstoffe im direkten Vergleich* (λ-Werte, Preise €/m²,
Marktanteile 48/43/9 %, Materialanteil ≈ 30 %, Glaswolle vor 1996).
https://www.co2online.de/modernisieren-und-bauen/daemmung/konventionelle-daemmstoffe/

**[Q14]** co2online — *Kellerdeckendämmung: Umsetzung, Kosten & Förderung* (5–10 % Verluste, > 50 % Reduktion,
≈ 5 % Heizkosten, 18–30 €/m², 4–12 cm / 5 cm).
https://www.co2online.de/modernisieren-und-bauen/daemmung/kellerdeckendaemmung/

**[Q15]** Verbraucherzentrale — *Rechenbeispiele für eine Fassadendämmung* (Fall A: 110 m², U 1,5→0,19, 16 cm,
65 kKh, 12 ct/kWh, 9.370 kWh, 1.120 €/a, 175 €/m², 15 %, 16.360 €, 14–15 Jahre; Fall B: 90 m², U 0,50→0,18,
12 cm, 8,9 ct/kWh, 170 €/a, 12.655 €, > 70 Jahre; 90–100 €/m² bei stehendem Gerüst; 40 Jahre Nutzung).
Stand 22.10.2025. https://www.verbraucherzentrale.de/wissen/energie/energetische-sanierung/rechenbeispiele-fuer-eine-fassadendaemmung-8192

**[Q16]** Verbraucherzentrale — *Wärmedämmung für Dach, Fassade und Keller spart Energie* (Kellerdecke,
oberste Geschossdecke, obere 50 cm der Kellerwand mit ≈ 6 cm, Nachrüstpflicht). Stand 28.09.2026.
https://www.verbraucherzentrale.de/wissen/energie/energetische-sanierung/waermedaemmung-fuer-dach-fassade-und-keller-spart-energie-39851

**[Q17]** Verbraucherzentrale — *Tipps: So packen Sie die Wärmedämmung richtig an* (Dachboden/Kellerdecke
teilweise selbst machbar; Luftdichtheit und Wärmebrücken als Kernpunkte).
https://www.verbraucherzentrale.de/wissen/energie/energetische-sanierung/tipps-so-packen-sie-die-waermedaemmung-richtig-an-40001

**[Q18]** BAFA — *Einzelmaßnahmen an der Gebäudehülle* (15 % Grundfördersatz, iSFP-Bonus 5 % ab 30.000 €,
Höchstgrenzen 30.000/60.000 €, Mindestinvestition 300 €, WPB-Bonus ab Q1 2027, EEE-Pflicht, außenliegender
Sonnenschutz förderfähig). https://www.bafa.de/DE/Energie/Effiziente_Gebaeude/Sanierung_Wohngebaeude/Gebaeudehuelle/gebaeudehuelle_node.html

**[Q19]** ThEGA / ibqs (Hrsg.) — *Dämmstoffe*, Faktenblatt (λ-Bereiche, Brandklassen nach DIN 4102-1,
c-Werte, Tabelle „Mindestdämmstärke für U ≤ 0,24", Nutzungsdauer WDVS 40 Jahre / Kerndämmung ≥ 50 Jahre,
Alnatura-Beispiel 17 cm Schaumglasschotter).
https://www.thega.de/fileadmin/user_upload/Publikationen/Ressourceneffizienz/Fachinfos_Faktenbl%C3%A4tter/ThEGA-Faktenblatt-Daemmstoffe.pdf

**[Q20]** Ökobaudat (Bundesinstitut für Bau-, Stadt- und Raumforschung) — *Mineral wool insulation (medium bulk
density range)*, GWP A1–A3 = 117,4 kg CO₂-Äq./m³ bei 100 kg/m³, Bezugsjahr 2021.
https://oekobaudat.de/OEKOBAU.DAT/datasetdetail/process.xhtml?lang=en&uuid=89b4bfdf-8587-48ae-9178-33194f6d1314&version=00.02.000

**[Q21]** STEICO — *Technisches Merkblatt STEICOflex 038* (λD 0,038; λB 0,040; Brandverhalten E nach
EN 13501-1; μ = 2; c 2.100 J/(kg·K); sd 0,08 m bei 40 mm). Version 8, 21.09.2026.
https://www.steico.com/fileadmin/user_upload/importer/downloads/produktinformationen_holzfaser-dmmstoffe/STEICO_technical-data-sheet_flex-038_DEU-AUT-CHE_de_i.pdf

**[Q22]** ROCKWOOL — *Technisches Datenblatt Klemmrock 035* (λD 0,034; λB 0,035; A1; μ = 1; R 5,70 bei 200 mm;
Verlegehinweis Übermaß 1–2 cm).
https://www.rockwool.com/siteassets/rw-d/datenblatter/schragdach/db-klemmrock-035-rockwool.pdf

**[Q23]** Umweltbundesamt — *Wärmedämmung. Fragen und Antworten*, Hintergrundpapier, März 2016 (Sanierung senkt
Primärenergiebedarf um bis zu 90 %; Heizung ≈ 70 % des Endenergieverbrauchs Wohnen; Raumwärme 132 kWh/m²·a 2013).
https://www.umweltbundesamt.de/publikationen/waermedaemmung

**[Q24]** Baulinks — *Wärmeleitzahlen / λ-Werte* (VIP 0,004–0,008, beschädigt 0,02; Aerogel 0,013–0,018;
PUR/PIR 0,022–0,029; EPS 0,032–0,040; Mineralwolle 0,030–0,050; Holzfaser 0,037–0,052; Schaumglas 0,038–0,070;
Blähglas 0,060–0,120; Holz ≈ 0,13).
https://www.baulinks.de/baumaterial/lambda-werte-waermeleitzahl-waermeleitfaehigkeit-waermedaemmung.php

**[Q24a]** FIXOLITE — *Kohlenstoff-Fußabdruck von Dämmstoffen* (Vergleichstabelle kg CO₂-Äq./m² bei R = 5:
Glaswolle 5–15, EPS 10–25, Steinwolle 5–25, Holzfaser 25–75, Zellulose 10–40). Herstellerquelle, nur als
Beispiel für die fehlende Vergleichbarkeit zitiert. https://fixolite.fr/de/co2-fusabdruck-von-dammstoffen/

**[Q25]** Das Ingenieurbüro (R. Krause) — *Sommerlicher Wärmeschutz nach DIN 4108-2* (Gradstunden-Kriterium
≤ 1.200 Kh/a WG, ≤ 500 Kh/a NWG; § 14 GModG). Redaktionsstand 19.10.2026.
https://www.das-ingenieurbuero.com/rechner/sommerlicher-waermeschutz/

**[Q26]** Leipfinger-Bader — *Welchen U-Wert sollte ein gedämmter Rollladenkasten haben?* (Altbau ≥ 2,0;
Ziel ≤ 0,5–1,0; ab 1,5 sanierungsbedürftig; Aufsatzkästen 0,5–0,9).
https://leipfinger-bader.de/blog/welchen-u-wert-sollte-ein-gedaemmter-rollladenkasten-haben/

**[Q27]** Energie-Experten — *Wärmewiderstände: R, Rsi und Rse* (Rsi 0,13 / Rse 0,04 bei Wänden; 10 cm λ 0,035
→ R 2,86; abweichende Werte für Decken). Stand 30.06.2026.
https://www.energie-experten.org/bauen-und-sanieren/daemmung/waermedaemmung/r-wert

**[Q28]** YouTube — *9 teure Dämm-Fehler und wie du sie vermeidest* (schlau energiesparen, Arnold Drewer),
https://www.youtube.com/watch?v=TszegjPc69w — Transkript in `references/transkripte/TszegjPc69w.txt`,
Zeitmarken oben. ASR-Text; Zahlen aus dem gesprochenen Wort, nicht aus einer Schriftquelle.
Zwei weitere Videos wurden nur auf Existenz/Titel geprüft (oEmbed), **nicht inhaltlich ausgewertet**:
*Dachdämmung richtig verstehen in nur 15 min* (https://www.youtube.com/watch?v=b84FyffRoRY) und
*Welche Dämmung schützt am besten vor HITZE?* (https://www.youtube.com/watch?v=9cTUFoRMQd0).

**Normen (Nummer/Ausgabe belegt, Volltext kostenpflichtig):** DIN 4108-2:2013-02 (vom GModG in § 14 zitiert),
DIN 4108-3 (klimabedingter Feuchteschutz; Ausgabe 2024-03 nach `references/quellen.md`), DIN 4108-4:2020-11
(Bemessungswerte), DIN 4108-7 (Luftdichtheit), DIN 4108 Beiblatt 2:2019 (Wärmebrücken), DIN 4102-1
(Baustoffklassen), DIN 68800-2 (Holzschutz), DIN 18533 (Bauwerksabdichtung), DIN EN 13501-1 (Euroklassen),
DIN EN 13162/13171 (Mineralwolle/Holzfaser), DIN EN ISO 6946 (U-Wert).

---

## Fehler aus den Video-Quellen (Praxis, mit Zeitmarke im Transkript)

- **Hohlraum hinter der Außendämmung**: Luft hinter den Platten strömt (Konvektion), die Dämmwirkung ist
  weg, obwohl die Dicke stimmt. Vor dem Verputzen abklopfen und Hohlstellen nachkleben (TszegjPc69w-03).
- **Innendämmung mit Luftspalt zur Außenwand**: der Taupunkt wandert in die Wand, es kommt zu Schimmel und
  Frostschäden. Platten vollflächig verklebt, kein Luftspalt (TszegjPc69w-04).
- **Plattendämmung ohne unteren Abschluss**: unten offen wirkt wie ein Kamin, kalte Luft zieht hinter die
  Dämmung. Abschlussprofil bzw. Sockelanschluss vorsehen (TszegjPc69w-05).
- **Dämmung endet stumpf vor der Fensterleibung**: die Leibung bleibt Wärmebrücke und schimmelt. Dämmung
  in die Leibung hineinziehen (TszegjPc69w-07).
- **Dämmstoff zusammengepresst**: gequetschte Matten verlieren Luftporen, der λ-Wert steigt messbar. Nie
  in Hohlräume pressen, lieber passend schneiden (TszegjPc69w-09).
- **Durchgehende Metalldübel im WDVS**: 40–50 Wärmebrücken, sichtbar als Algenflecken. Thermisch getrennte
  Tellerdübel verwenden (TszegjPc69w-10).
- **Plattenware in der Dachdämmung / im Leichtbau**: zwischen den Platten bleiben Fugen und Hohlräume.
  Bei Dachschräge und Leichtbau einblasen (Zellulose) oder zweite Lage versetzt (TszegjPc69w-12).
- **Split-Klimaanlage vergessen**: Leerrohr bzw. Kabelkanal für die Kältemittelleitung muss vor der
  Dämmung liegen, sonst bleibt nur Aufputz (sWXyiNADbFk-11).

## Ergänzungen aus dem Fehlerkatalog

- **Größenordnung Hohlraum**: bei einem Einfamilienhaus kommen schnell **7 m³ Schüttgut als Größenordnung** zusammen, wenn hinter der Dämmung Luft bleibt (TszegjPc69w-03).
- **Vollflächige, fugenfreie Verklebung** ist die Regel — Punktverklebung nur, wo der Untergrund es zulässt, sonst Konvektion (TszegjPc69w-04).
- **„Stockflecken" ist Schimmel, nicht harmlos**: braune Flecken an der Leibung sind ein Feuchteindiz, kein Schönheitsfehler (TszegjPc69w-07).
- **40–50 Wärmebrücken im Beispiel** durch durchgehende Metalldübel — thermisch getrennte Tellerdübel (TszegjPc69w-10).
- **Plattendämmstoffe im Dach ungeeignet**: bei Leichtbau und Dachschräge **Matten- oder Einblasdämmstoff wählen**, sonst bleiben Fugen (TszegjPc69w-12).

## 11. Unbelegt

Diese Punkte sind bewusst **nicht** mit Zahl in den Text gewandert:

- **Preis je m² bei exakt definierter Dicke** für Schaumglas, Glasschaum-Schotter und VIP — keine geprüfte
  Quelle gefunden. Die Preise in 1.1 gelten für die „GEG-Dicke", die `[Q13]` nicht je Material ausweist.
- **GWP je m² für EPS, PUR/PIR, Holzfaser und Zellulose.** Ökobaudat führt Datensätze, die Indikator-Tabellen
  waren über die abgerufenen Seiten nicht auslesbar. Belegt ist nur Mineralwolle (117,4 kg CO₂-Äq./m³) `[Q20]`.
- **ψ-Werte einzelner Detailpunkte** (W/(m·K)) für Laibung, Deckenauflager, Sockel. Belegt sind nur die
  pauschalen Zuschläge 0,10/0,05/0,03 `[Q10]`; die Detailwerte stehen in DIN 4108 Beiblatt 2, die
  kostenpflichtig ist.
- **Brandklasse von VIP** und **c-Wert von VIP/Schaumglas-Schüttung** — in den geprüften Quellen nicht genannt.
- **Amortisationszeiten für Dach-, Kellerwand- und Perimeterdämmung** — nur für die Fassade sind Rechenbeispiele
  belegt `[Q15]`. Die Kellerdecken-Rechnung in 2.5 ist eine eigene Überschlagsrechnung und als solche markiert.
- **Eigenleistungs-Anteil an den Kosten** und **Zeitbedarf** — nur Schätzungen, keine belastbare Quelle.
- **Ob Eigenleistung förderfähig ist**: `[Q18]` verlangt einen EEE, sagt aber nichts über die Ausführung durch
  den Eigentümer. In der Praxis fehlt die Fachunternehmerrechnung; als Rechtsaussage nicht geprüft.
- **Zahlen zu HBCD und Bioziden in WDVS** — nicht recherchiert, obwohl das UBA dazu publiziert.
- **Sommerlicher Wärmeschutz für Nichtwohngebäude** (500 Kh/a) ist belegt `[Q25]`, die Systematik der
  DIN 4108-2 Tabelle 9 (Zuordnung Klimaregion → Grenzwert) nicht im Detail geprüft.
- **Wirtschaftlichkeit von Aufsparren- vs. Zwischensparrendämmung** — keine geprüfte Kostenquelle; die
  Aussagen in 2.2 sind konstruktiv, nicht kaufmännisch.
