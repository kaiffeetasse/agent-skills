# Haus komplett sanieren — Entscheidung, Netzplan, Budget, Steuerung

> **Preisstand 09/2026.** Alle Preise sind Orientierungswerte inkl. MwSt. aus den genannten Quellen —
> regional verschieden, keine Angebote. Wer später damit rechnet, prüft sie neu.

**Für wen:** Eigentümer eines Bestandshauses (typisch 1955–1975), der „alles neu" will und keinen
Generalplaner hat. Ton: Bauleiter zu Bauherr.
**Stand der Quellenprüfung: 09.11.2026.** Jede Zahl trägt eine Quellennummer `[Qn]`, aufgelöst in
Abschnitt 11. Alle URLs wurden am 09.11.2026 einzeln abgerufen; tote Links sind als tot markiert,
nicht gelöscht.

**Drei Etiketten, wie in allen Playbooks dieses Skills:**

| Etikett | Bedeutung |
|---|---|
| `[Qn]` | Zahl oder Aussage steht so in der Quelle (URL, Datum, Zitat in Abschnitt 11) |
| **[Setzung]** | meine Planungsannahme. Begründet, aber nicht belegt — du darfst sie ändern |
| **[Rechnung]** | aus belegten Zahlen gerechnet; Rechenweg steht daneben |

**Die eine Regel vorweg:** Bei einer Komplettsanierung entscheidet nicht der Preis pro Quadratmeter,
sondern die **Reihenfolge**. Jedes Gewerk, das zu früh kommt, wird zweimal bezahlt — Elektro nach dem
Estrich, Fenster vor der Dämmung, Abdichtung nach den Fliesen. Der Netzplan in Abschnitt 2 ist deshalb
der wichtigste Teil dieses Dokuments, nicht das Budget.

**Abgrenzung:** Dieses Playbook steuert das Ganze. Wie man das einzelne Gewerk macht, steht in den
23 Einzel-Playbooks — Zuordnung in Abschnitt 10. Wiederholt wird hier nichts.

---

## 0. Kurzantwort

- **Sanieren oder abreißen** entscheidet man an einer Zahl: kostet die ehrlich kalkulierte Vollsanierung
  **mehr als 75 %** eines vergleichbaren Neubaus auf demselben Grundstück, gehört der Abriss auf den
  Tisch [Q11]. Ein Neubau liegt 2026 grob bei **3.000–4.000 €/m²** ohne Grundstück, eine echte
  Kernsanierung bei **1.800–3.000 €/m²** [Q11].
- **Die Reihenfolge ist nicht verhandelbar:** Entkernen → Rohinstallation → Hülle (Dach/Fenster) →
  Dämmung → Estrich → Abdichtung → Fliesen/Böden → Türen → Küche/Bad → Außenanlagen.
- **120–130 m² Kernsanierung dauern 6–9 Monate netto, mit Puffer 8–11** [Q15]; dazu **2–5 Monate
  Vorlauf** für Planung, Förderantrag und Vergabe. Wer „im Frühjahr anfangen, im Herbst einziehen"
  plant, plant den Umzug zweimal.
- **Bewohnt sanieren ist bei einer Kernsanierung die teuerste Variante** — nicht wegen der Miete,
  sondern wegen der Dauer: Bewohnte Baustellen bremsen jeden Ablauf [Q15], und ein Praktiker rechnet
  mit „ungefähr doppelt so lange wie geplant" [Q23].
- **Erst Antrag, dann Auftrag.** KfW verlangt die Antragstellung **vor Beginn des Vorhabens** [Q4][Q5];
  wer zuerst baggert, verliert die Förderung.
- **Puffer 10–15 % auf die Kosten** ist keine Vorsicht, sondern die Regel: Ein Sanierer nennt
  „15 Prozent Puffer" als Normalwert [Q23], und der Bausachverständige sagt den Grund: „Jeder dieser
  Funde ist ein Nachschlag, der im ursprünglichen Angebot nicht stand" [Q11].

---

## 1. Vorentscheidungen — die fünf Fragen, die vor dem ersten Handwerker geklärt sind

### 1.1 Substanzprüfung: was man vor jeder Zahl prüfen lässt

Bei einem Haus der 1960er ist der Bauablauf der Jahrzehnte das Problem, nicht das Baujahr. BauNetz
beschreibt die Baualtersstufe so: Übergang vom Massivbau zum industriellen Bauen, Stahlbeton,
Aluminium, **großformatige Verglasungen ohne Wärmeschutz**, Zentralheizung fast flächendeckend,
„Anforderungen an den Wärmeschutz spielten dagegen noch eine untergeordnete Rolle" [Q16].

Daraus folgt die Prüfliste, **bevor** ein Angebot geschrieben wird:

| Prüfpunkt | Warum er die Entscheidung ändert | Womit |
|---|---|---|
| **Gründung/Fundament** | Reicht sie für neue Lasten (Aufstockung, Dachausbau)? Der Sachverständige nennt genau diesen Fund: „ich prüfe die Gründung und stelle fest, dass das Fundament für die neuen Lasten nicht ausreicht" [Q11] | Baggerschurf, Sachverständiger |
| **Tragwerk, Decken, Stahlträger** | Bestand ist oft günstiger als Neubau — **wenn** „Tragwerk, Fundament und Dachstuhl in Ordnung sind" [Q11] | Statiker, Sichtprüfung mit Öffnungen |
| **Dachstuhl** | Ein neuer Dachstuhl kostet **50–150 €/m²**, eine Neueindeckung **80–300 €/m²** [Q12] — das ist der Unterschied zwischen „Sanierung" und „Abriss" | Zimmermann |
| **Feuchte im Keller** | Innenabdichtung **50–200 €/m²** Wandfläche, Außenabdichtung **300–600 €/m²** [Q17] | Feuchtemessung, siehe `keller-mauerwerk.md` |
| **Schadstoffe** | Pflichtenlage nach § 5a GefStoffV, gilt **auch für private Haushalte** [Q9] | Abschnitt 6 |
| **Elektro-Bestand** | Zweiadrigkeit ohne Schutzleiter, kein FI — dann ist „Elektro neu" kein Wunsch, sondern Voraussetzung für jede Wohnnutzung | `elektro.md` |
| **Bauakten** | Baujahr, Baubeginn, An- und Umbauten, frühere Feuchteschäden — genau die Informationen, die § 5a Abs. 1 verlangt [Q9] | Bauamt, alte Rechnungen |

**[Setzung]** Ein Substanzgutachten kostet vier- bis fünfstellig. Bei einem Projektumfang von 200.000 €
sind das unter 1 % — und es ist die einzige Position, die den teuersten Fehler verhindert: mitten in
der Sanierung zu merken, dass man hätte abreißen sollen [Q11].

### 1.2 Sanieren vs. abreißen — die 75-Prozent-Regel und ihre Grenzen

Die belastbarste Entscheidungsregel, die ich in den Quellen gefunden habe, stammt von einem
Bausachverständigen: „Wenn die ehrlich kalkulierte Vollsanierung mehr als 75 Prozent dessen kostet,
was ein vergleichbarer Neubau auf demselben Grundstück kosten würde, gehört der Abriss ernsthaft auf
den Tisch" [Q11]. Begründung: „Für die letzten 25 Prozent Ersparnis kaufen Sie sich beim Sanieren ein
altes Haus mit allen Kompromissen: den alten Grundriss, die alte Raumhöhe, die alte Statik" [Q11].

**Abrisskosten (belegt):**

| Position | Zahl | Quelle |
|---|---|---|
| Abriss Einfamilienhaus, komplett mit Entsorgung | **10.000–30.000 €** | [Q13] |
| Faustformel | **50–100 €/m² Wohnfläche**, in Ausnahmefällen bis **250 €/m²** | [Q13] |
| Beispiel 140 m² ohne Keller (Planung, Entrümpelung, Abriss, Entsorgung, Sondermüll) | **12.850 €** | [Q13] |
| Beispiel Stadtvilla 200 m² mit Keller (inkl. Keller verfüllen 5.000 €) | **26.200 €** | [Q13] |
| Bauschutt-Anfall 140-m²-Haus | **300–400 m³** | [Q13] |

**Gegenprobe „wann Abriss":** musterhaus.net schreibt, ein Abriss lohne sich, „wenn die Sanierung über
2.500 €/m² kosten würde" [Q13] — das ist die konservativere Variante derselben 75-%-Logik.

**Und die Gegenposition, die man kennen muss:** FOCUS formuliert sie selbst — unterhalb der Schwelle
ist Sanieren „in den meisten Fällen die richtige Wahl"; **darüber** kann es trotzdem sinnvoll sein, bei
**Denkmal** (erhöhte Abschreibung), bei **Erhaltungssatzung/Milieuschutz** („bekommen Sie ohnehin keine
Abrissgenehmigung") und bei gesunder Substanz [Q11].

**Widerspruch, der stehen bleibt — die Kostenzahlen für „Kernsanierung":**

| Quelle | Band | Anmerkung |
|---|---|---|
| Sparkasse Immobilien [Q14] | **400–1.000 €/m²** Wohnfläche | „große Orientierung", keine Quelle für die Zahl genannt |
| Dr. Klein [Q12] | **400–1.000 €/m²**; 120 m² = 48.000–120.000 € | Seite von 2023 |
| CHECK24 [Q18] | **600–1.000 €/m²** | Schätzungen, ausdrücklich „nicht verbindlich" |
| justhome [Q17] | **500–1.500 €/m²** | Stand Mai 2026 |
| FOCUS/Bausachverständiger [Q11] | **1.800–3.000 €/m²** | „ehrlich kalkulierte Vollsanierung", Juli 2026 |
| Bauexpertenforum, Praktiker [Q19] | **2.500–3.500 €/m²** | Antwort auf genau diese Frage |

Diese Spanne ist kein Recherchefehler, sondern der Kern des Problems. Ein Forenthread von 2024 stellt
die Frage wörtlich: Warum steht überall 400–1.000 €/m², wenn der Architekt für 150 m² **420.000 €**
veranschlagt — „Das sind ja 2.800 € pro qm" [Q19]? Die Antwort eines erfahrenen Forumsteilnehmers:
bei allen Gewerken „kommen eben Preise irgendwo zwischen 2.500 und 3.500 € bei raus. Also ungefähr das,
was dein Architekt gerechnet hat" [Q19].

**[Setzung] Meine Erklärung für die Lücke** (nicht belegt, aber sie passt zu allen Zahlen): Die niedrigen
Bänder beschreiben eine **Innensanierung** — Elektro, Sanitär, Oberflächen — ohne Dach, Fassade,
Fenster und ohne die Nebenkosten. Die hohen Bänder beschreiben die **Vollsanierung inklusive Hülle,
Technik, Planung und Puffer**, also das, was die 75-%-Regel meint. Wer die 400–1.000 €/m² für eine
Komplettsanierung einkalkuliert, plant regelmäßig die Hälfte.

**Entscheidungsmatrix (aus den Quellen, ohne Meinung):**

| Kriterium | spricht für Sanieren | spricht für Abriss + Neubau |
|---|---|---|
| Substanz (Tragwerk, Fundament, Dachstuhl) | gesund [Q11] | Fund reicht für neue Lasten nicht [Q11] |
| Sanierungskosten / Neubaukosten | < 75 % [Q11] | > 75 % [Q11] |
| Grundriss | passt oder ist ohne Statikeingriff änderbar | muss komplett neu (Raumhöhe, Zuschnitt) [Q11] |
| Denkmal | § 7i-AfA schlägt den Neubau steuerlich [Q11][Q8] | — |
| Erhaltungssatzung / Milieuschutz | — | keine Abrissgenehmigung [Q11] |
| Energetisches Endniveau | „guter Altbau", nicht Neubau-Niveau [Q11] | Neubau-Standard erreichbar |

### 1.3 Kauf + Renovierung vs. schlüsselfertig — die Steuerfalle entscheidet mit

Wer ein Bestandshaus **kauft** und dann saniert, hat eine Falle, die in keiner Sanierungsplanung steht:
**anschaffungsnahe Herstellungskosten**. § 6 Abs. 1 Nr. 1a EStG: Instandsetzungs- und
Modernisierungsaufwendungen **innerhalb von drei Jahren** nach der Anschaffung gehören zu den
Herstellungskosten, wenn sie **15 % der Anschaffungskosten des Gebäudes** übersteigen [Q7]. Folge: Sie
sind nicht sofort abziehbar, sondern über die Nutzungsdauer abzuschreiben. FOCUS formuliert die
Wirkung: „Aus einem geplanten Sofortabzug wird dann eine Abschreibung über Jahrzehnte" [Q11].

Das betrifft nur **Vermieter** (Werbungskosten). Wer selbst einzieht, hat keinen Werbungskostenabzug —
für den ist die Regel irrelevant, § 35c bleibt. **[Setzung]** Diese Unterscheidung ist der Punkt, an
dem die Steuerberatung vor dem Kauf steht, nicht danach.

**Schlüsselfertig (Bauträger) vs. Generalunternehmer vs. Einzelvergabe** — die Rollen sind nicht
dasselbe [Q21]:

| Modell | Wer ist Bauherr | Planung | Weisungsrecht an Handwerker | Preisbindung |
|---|---|---|---|---|
| **Einzelvergabe** | du | du/Architekt | ja, je Vertrag | je Gewerk |
| **Generalunternehmer (GU)** | du bleibst Bauherr | separat (oder beim GU) | **nein** — Handwerker sind dem GU verpflichtet | Festpreis möglich |
| **Bauträger** | **der Bauträger**, du bist Käufer | Bauträger | **nein**, im Extremfall Betretungsverbot | Festpreis |

Der Unterschied ist praktisch: Beim Bauträger „dürfen Sie keine direkten Weisungen an die Handwerker
geben" [Q21]. Wenn du selbst steuern willst, ist das das falsche Modell.

### 1.4 Denkmalschutz — zwei Vorteile, eine Pflicht

- **Steuer:** § 7i EStG erlaubt bei Baudenkmalen **9 % in acht Jahren** und **7 % in den vier folgenden
  Jahren** der Herstellungskosten für Erhaltungsmaßnahmen [Q8]. Voraussetzung ist eine **Bescheinigung
  der zuständigen Stelle** (§ 7i Abs. 2) [Q8] — ohne Bescheinigung keine AfA.
- **Förderung:** KfW 261 fördert die Stufe „Effizienzhaus Denkmal EE/NH" ausdrücklich, mit
  Tilgungszuschuss **5 %** (plus 5 Prozentpunkte bei NH-Klasse) [Q4].
- **Pflicht:** Maßnahmen „in Abstimmung mit" der Denkmalbehörde; die KfW verlangt bei Denkmal
  „Abstimmungsnachweise und die Genehmigung der Denkmalschutzbehörde" als Fördervoraussetzung [Q4].
  Wer ohne Abstimmung saniert, verliert AfA und Förderung gleichzeitig.

**[Setzung]** Denkmal heißt nicht „nichts darf sich ändern", sondern „das Erscheinungsbild und die
schützenswerte Substanz bleiben". Fenster, Heizung, Bad und Elektro sind regelmäßig verhandelbar —
aber nur vorher, nicht nach der Lieferung. Praxis und Grenzen: `recht-renovierung.md`.

### 1.5 Energieeffizienz — was 2026 Pflicht ist und was nur Förderung

**Rechtslage hat sich 2026 geändert:** Das **Gebäudemodernisierungsgesetz (GModG)** hat das
Gebäudeenergiegesetz (GEG) abgelöst und gilt **seit 29. Juli 2026** [Q2]. Wer noch mit „GEG 55" oder
„GEG-Novelle" argumentiert, argumentiert mit dem falschen Gesetz.

**Pflichten, die eine Kernsanierung auslösen:**

| Situation | Anforderung | Quelle |
|---|---|---|
| **Umbau von mehr als 10 % der Fläche eines Bauteils** (z. B. Fassade neu verputzen, Fenster tauschen) | Mindest-U-Wert des Bauteils | [Q2] |
| Außenwand | **U = 0,24 W/m²K**, entspricht ca. **12–16 cm** Dämmung | [Q2] |
| Fenster (Uw) | **1,30 W/m²K** (Dachflächenfenster 1,40; Verglasung 1,10) | [Q2] |
| Dachschräge/Steildach | **0,24 W/m²K**, ca. **14–18 cm** | [Q2] |
| Oberste Geschossdecke | **0,24 W/m²K**, ca. **14–18 cm** | [Q2][Q1] |
| Wände/Decken gegen unbeheizten Keller | **0,30 W/m²K**, ca. **10–14 cm** | [Q2] |
| Nur neuer Anstrich | GModG greift **nicht** | [Q2] |
| **Umfassende Modernisierung** | Gesamtbilanz wie Neubau: Primärenergie ≤ **1,4-fach** des Referenzgebäudes, Transmissionswärmeverlust ≤ **1,4-fach** | [Q2] |
| **Nachrüstpflicht oberste Geschossdecke** | U ≤ **0,24 W/m²K**; bei selbstgenutztem Ein-/Zweifamilienhaus, das am 1.2.2002 selbst bewohnt war, greift sie erst bei **Eigentümerwechsel, Frist zwei Jahre**; Ausnahme, wenn die Aufwendungen sich nicht „innerhalb angemessener Frist" amortisieren | [Q1] |
| Heizung: Gas, nach Inkrafttreten eingebaut | **ab 2029: 10 %**, 2030: 15 %, 2035: 30 %, 2040: 60 %, 2045: 100 % erneuerbar | [Q2] |

**[Setzung] Der praktische Merksatz:** Die 10-%-Schwelle macht aus jeder „kleinen" Fassaden- oder
Fensteraktion eine U-Wert-Aufgabe. Wer ohnehin eine Kernsanierung macht, erfüllt sie nebenbei — wer sie
in Etappen macht, zahlt das Gerüst zweimal.

**Effizienzhaus 55/40 — Klarstellung:** Das sind **Förderstufen der KfW**, keine gesetzliche Pflicht.
KfW 261 fördert die Stufen **85, 70, 55, 40** in den Varianten **EE** (Erneuerbare Energien) und **NH**
(Nachhaltigkeit), dazu **EH Denkmal** [Q4]. Voraussetzung für jede Stufe: erneuerbare Energien und/oder
unvermeidbare Abwärme decken **mindestens 65 %** des Wärme- und Kältebedarfs [Q4]. Zur Einordnung:
„Das KfW-Effizienzhaus 40 benötigt höchstens 40 Prozent der Referenz-Primärenergie und muss zusätzlich
erhöhte Anforderungen an die Gebäudehülle erreichen" [Q2]; Stufe 55 ist im **Neubau** nur noch
**befristet bis Ende 2026** förderfähig [Q2] — für die Sanierung gilt die Stufenliste aus [Q4].

**Barrierefreiheit:** [Setzung] Bei einer Kernsanierung ist der einzige Moment, in dem man Türbreiten,
schwellenlose Übergänge und eine bodengleiche Dusche ohne Aufpreis hinbekommt, **vor** dem Estrich.
Förderung: KfW-Programm 455-B (Barrierereduzierung) ist derzeit **nicht beantragbar** (Mittel
ausgeschöpft, Wiederaufnahme 2027 möglich) — Alternative ist der Kredit **159** [Q5, Zitat aus
`kosten-bauzeit.md`, dort geprüft]. Konstruktive Details: `bad.md`, `waende.md`.

### 1.6 Förderfähigkeit — vier Töpfe, drei Regeln

| Programm | Was es gibt | Bedingung, die das Projekt ändert |
|---|---|---|
| **KfW 261** (BEG WG) | Kredit **max. 150.000 € je Wohneinheit**; Tilgungszuschuss **5 %** bei EH 55 EE, **10 %** bei EH 40 EE, **5 %** bei EH Denkmal, **+5 Pp** NH, **+10 Pp** Worst Performing Building, **+15 Pp** serielle Sanierung [Q4] | Bauantrag ≥ **5 Jahre** alt; **Energieeffizienz-Experte** zwingend; **10 Jahre** Nutzungspflicht; Antrag **vor Beginn**; Eigenleistung: **nur Materialkosten** förderfähig [Q4] |
| **KfW 458** (Heizungszuschuss) | Grundförderung **30 %**; Klimageschwindigkeitsbonus **16 %** (sinkt ab 01.02.2027 halbjährlich um 4 Pp, **0 ab 01.08.2028**); Einkommensbonus **40 %** bis 30.000 € zvE (40.000 € mit Kind); Obergrenze **70 %**, mit Einkommensbonus **80 %**; Förderhöchstbetrag **28.000 €** für die erste Wohneinheit [Q5] | nur erneuerbare Wärmeerzeuger; Gas ist **nicht** förderfähig [Q4][Q5] |
| **§ 35c EStG** | **7 % / 7 % / 6 %** in drei Jahren, Deckel 14.000 / 14.000 / 12.000 €, **max. 40.000 €** je Objekt [Q6] | nur die **acht** gelisteten Maßnahmen; Gebäude **älter als 10 Jahre**; **Fachunternehmen** muss ausführen; Bescheinigung nötig [Q6] |
| **§ 7i EStG** (Denkmal) | **9 %** in acht Jahren, **7 %** in vier weiteren [Q8] | Bescheinigung der Denkmalbehörde [Q8] |

**Die drei Regeln, die man nicht verletzen kann:**

1. **Erst Antrag, dann Auftrag.** „Der Antrag ist vor Beginn des Vorhabens bei der KfW über einen
   Finanzierungspartner Ihrer Wahl zu stellen" [Q4]. Ein Handwerkervertrag mit aufschiebender Bedingung
   ist bei 458 ausdrücklich vorgesehen [Q5] — die Förderung überlebt also den Vertrag, nicht den Bagger.
2. **Kumulierungsverbot.** KfW 261 und § 35c schließen sich aus: „Eine Kumulierung mit einer steuerlichen
   Förderung nach diesen Vorschriften ist ausgeschlossen" [Q4]. Ebenso 261 und BEG-Einzelmaßnahmen;
   dazwischen liegen **3 Jahre** Wartezeit [Q4].
3. **Förderung ist kein Preisnachlass.** KfW 261: „Es besteht kein Anspruch auf Förderung" [Q4]. Kalkuliere
   den vollen Preis; der Zuschuss kommt nach der Prüfung.

**[Setzung] Die Förder-Reihenfolge im Projekt:** Energieberater beauftragen → BzA (Bestätigung zum
Antrag) → Finanzierungspartner → KfW-Antrag → **dann** ausschreiben. Wer erst ausschreibt und dann
fördert, findet keinen Experten mehr, der die BzA rückwirkend unterschreibt.

---

## 2. Netzplan — die Reihenfolge und was danach nicht mehr zu ändern ist

### 2.1 Die Kette

```
Bestandsaufnahme + Schadstofferkundung
        │
        ▼
Entkernen / Rückbau ──────────────► Entsorgung, Container
        │
        ▼
Rohinstallation: Elektro · Sanitär · Lüftung · Heizung   ◄── Hülle kann parallel laufen
        │                                                    (Dach/Fenster von außen)
        ▼
Hülle: Dach · Fassade/Dämmung · Fenster
        │
        ▼
Trockenbau / Vorsatzschalen / Putz
        │
        ▼
Estrich  ──►  Trocknung (Zementestrich ca. 4 Wochen)  ──►  Belegreife MESSEN
        │
        ▼
Abdichtung in Feuchträumen (DIN 18534)
        │
        ▼
Fliesen · Böden
        │
        ▼
Türen / Zargen · Treppe
        │
        ▼
Küche · Bad-Endmontage · Elektro-Fertiginstallation
        │
        ▼
Maler (letzte staubige Schicht)  ──►  Außenanlagen  ──►  Abnahme
```

Die Kette stimmt mit dem Bauzeitenplan des Skills überein (`kosten-bauzeit.md`, Abschnitt 2.1) und mit
der Phasenfolge, die Sanierungsanbieter für 120 m² nennen: Entkernung 2–3 Wochen → Rohbau/Hülle 4–8 →
Haustechnik 5–8 → Innenausbau 6–10 Wochen [Q15].

### 2.2 Die vier „Point of no return"

Das ist der eigentliche Gehalt dieses Abschnitts. Nicht „was kommt zuerst", sondern **was man danach
nicht mehr ändert**:

| Entscheidung | Deadline | Was sie danach kostet |
|---|---|---|
| **Grundriss, Wanddurchbrüche, Treppenlage** | vor Rohinstallation | Statik, Leitungsführung und Estrich-Gefälle neu — fünfstellig |
| **Elektro: Anzahl und Lage von Dosen, Stromkreisen, Leerrohren, Verteilerplatz** | **vor** Putz und Estrich | Schlitze in fertigen Wänden, Fliesen wieder auf. Ein Sanierer bereute genau das: die „Ausbaureserve in der Elektroverteilung" war aufgebraucht, obwohl noch Arbeit im Haus anstand [Q24] |
| **Sanitär: Fallrohre, Vorwandtiefe, Bodengleiche Dusche, Gefälle** | **vor** Estrich | Estrich und Abdichtung neu; die Dusche ist dann nicht mehr bodengleich |
| **Estrich-Oberkante / Fußbodenaufbau (Türen!)** | **vor** Bestellung der Türen | Türen kürzen oder neu kaufen. Deshalb: Türen erst nach Estrich aufmaßen |
| **Fenster + Fassade zusammen** | eine Vergabe | Fenster zuerst, Dämmung später heißt: Laibungen und Anschlüsse zweimal, und der U-Wert des Bauteils passt nicht mehr zur GModG-Anforderung [Q2] |
| **Dämmstärke / Aufbauhöhe** | vor Estrich und vor Fenstertausch | Jede cm Aufbauhöhe verschiebt Türstürze, Treppenantritt und Anschlusshöhen |

**Merksatz [Setzung]:** Alles, was **in** der Wand, **unter** dem Estrich oder **hinter** der Fliese
liegt, muss entschieden sein, bevor die Wand geschlossen wird. Alles, was man später abschrauben kann
(Maler, Böden, Möbel, Außenanlagen), ist verschiebbar.

### 2.3 Der kritische Pfad

**Estrich → Trocknung → Belegreife → Abdichtung → Fliesen → Sanitär-Endmontage.**

Der lange Pol ist nicht das Arbeiten, sondern das **Warten**: Zementestrich braucht ca. **4 Wochen** bis
zur ausreichenden Durchhärtung, die Belegreife wird **gemessen** (≤ 2,0 CM-%, beheizt ≤ 1,8) und nicht
am Kalender abgelesen — Details in `estrich.md` und `kosten-bauzeit.md` Abschnitt 2.4.

**Zwei Beschleuniger, die den kritischen Pfad wirklich verkürzen** (aus `kosten-bauzeit.md`, hier nur
verlinkt): Estrich im Bad vermeiden (Gefälleelement statt neuem Estrich, spart 4–5 Wochen), und
Material **vor** dem Rückbau bestellen (Lieferzeit ist die häufigste unsichtbare Verzögerung).

### 2.4 Zeitplan in Wochen (130 m², Kernsanierung, ein Bad neu, ein Bad saniert)

Die Zahlen sind **[Setzung]** aus zwei belegten Phasenrastern [Q14][Q15]; die Spanne ist echt, nicht
Deko.

| Phase | Wochen | Parallel möglich | Fertig, wenn … |
|---|---|---|---|
| **Vorlauf:** Bestandsaufnahme, Energieberater, BzA, KfW-Antrag | 4–8 | — | Förderzusage oder zumindest Antrag gestellt [Q4] |
| **Planung, Ausschreibung, Vergabe** | 6–12 | — | alle Gewerke **terminiert**, nicht nur beauftragt |
| **Materialbestellung** (Fenster, Türen, Sanitär, Fliesen) | 2–6 (Vorlauf) | läuft mit | Liefertermin **schriftlich** vor Rückbau |
| **Baustelle einrichten, Entkernen** | 2–3 | — | Fotos jeder Wand mit Maßband |
| **Rohinstallation** Elektro/Sanitär/Lüftung/Heizung | 5–8 | **Hülle außen** | Druckprobe + Messprotokoll |
| **Dach + Fassade + Fenster** | 4–8 | Rohinstallation | Haus ist dicht, Anschlüsse dokumentiert |
| **Trockenbau, Putz, Spachtel** | 3–5 | — | Wände lotrecht, Schlitze voll verfüllt |
| **Estrich** | 1 | — | Höhe passt zur Tür, Gefälle 2 % |
| **Trocknung + Belegreife** | 4–6 | Malerarbeiten in fertigen Räumen | CM-Protokoll unter Grenzwert |
| **Abdichtung + Fliesen** | 3–4 | — | 2 Lagen, Ecken und Manschetten, Fotos |
| **Türen, Böden, Treppe** | 2–3 | — | Türblatt schleift nicht |
| **Küche, Bad-Endmontage, Elektro-Fertiginstallation** | 2–3 | — | FI geprüft, Messprotokoll da |
| **Maler, Außenanlagen, Endreinigung** | 2–4 | — | Anschlussfugen glatt |
| **Abnahme, Mängelbeseitigung** | 2–3 | — | Protokoll unterschrieben, Fristen je Mangel |

**Summe Bau: 26–40 Wochen netto.** Mit 20–25 % Puffer — der Wert, den ein Sanierungsanbieter für
120 m² selbst nennt [Q15] — sind das **31–50 Wochen**. Plus Vorlauf 8–20 Wochen ergibt das
**10–17 Monate von der Entscheidung bis zum Einzug**; planbar ist die Mitte, nicht der Optimismus.

**Der Gegencheck:** Dr. Klein nennt für eine Kernsanierung „zwischen 3 Monaten und 1 Jahr" [Q12], die
Sparkasse summiert ihre Phasen auf ähnliche Werte [Q14]. Drei Monate sind bei 130 m² mit neuem Estrich,
neuer Hülle und zwei Bädern nicht erreichbar — das ist die Unterkante für eine Wohnung ohne Hülle.

---

## 3. Bewohnt oder unbewohnt — die Entscheidung mit dem größten Zeithebel

### 3.1 Was die Quellen sagen

- **Bewohnte Baustellen bremsen:** „Zugang, Ruhezeiten, Baustellenlogistik und **Bewohnung** bremsen
  Abläufe" [Q15] — das steht in der Phasenaufstellung eines Sanierungsanbieters, also nicht bei einem
  Theoretiker.
- **Dauer:** Ein Sanierer im Rückblick: „Baustellen sind einfach Baustellen und es dauert in der Regel
  auch einfach immer ungefähr **doppelt so lange** als geplant" [Q23, 00:00:50]. Das ist eine
  Praktiker-Aussage, keine Statistik — aber sie deckt sich mit dem Puffer von 20–25 % [Q15] nur dann,
  wenn man sie als Warnung liest, nicht als Rechenfaktor.
- **Dreck ist kein Nebeneffekt, sondern ein Dauerzustand:** Ein selbst sanierender Eigentümer beschreibt
  es so: „wegen unserer Baustelle [wird] um unser Haus permanent Dreck reingeschleppt" [Q24, 00:03:52].
  Bei einer Kernsanierung ist das kein Monatsproblem, sondern ein Halbjahresproblem.
- **Staubschutz ist eine Technik, keine Plane:** Aufbau, Schleusen, Unterdruck und die Regel „nass
  saugen statt fegen" stehen in `entkernen-entsorgung.md` (Abschnitt 1.5) und `werkzeug-sicherheit.md` —
  hier nicht wiederholt.

### 3.2 Der Entscheidungsbaum

| Umfang | Bewohnbar? | Begründung |
|---|---|---|
| **Kernsanierung mit Elektro, Estrich, Heizung, Hülle** | **Nein** | Estrich-Trocknung, Strom weg, Wasser weg, Haus offen. Zwei Bäder gleichzeitig ist kein Provisorium, sondern ein Zustand |
| **Kernsanierung ohne Hülle** (Dach/Fassade bleiben) | eingeschränkt, etagenweise | Rohinstallation und Estrich etagenweise; Bad muss verfügbar bleiben → zwei Bauphasen |
| **Teilsanierung** (Bad + Elektro in 3 Räumen) | ja, mit Schleuse | entspricht dem Szenario in `kosten-bauzeit.md` (11–13 Wochen) |
| **Kosmetisch** (Maler, Böden, Türen) | ja, raumweise | keine Rohinstallation, kein Estrich |

**[Setzung] Die Rechnung, die die Entscheidung trifft:** Miete für 8–10 Monate (130 m², regional
10–14 €/m² kalt → 10.000–18.000 €) gegen die Mehrkosten des bewohnten Bauens: längere Bauzeit,
Provisorien, doppelte Reinigung, Schleusen, und — der eigentliche Posten — die Fehler, die aus Zeitdruck
entstehen. Bei einer echten Kernsanierung ist Ausziehen fast immer billiger als Bleiben. Bei einer
Teilsanierung ist es umgekehrt.

### 3.3 Etappensanierung: was in Etappen geht und was nicht

**Geht in Etappen** (jeweils mit eigenem Abschluss, ohne Folgekosten):
Maler/Spachtel je Raum · Bodenbeläge · Innentüren · Küche · ein Bad komplett · Außenanlagen ·
Dachbodenausbau (wenn die Dämmung der obersten Geschossdecke schon liegt).

**Geht nicht in Etappen, ohne zweimal zu zahlen:**
Elektro (jede Etappe öffnet Wände, die die nächste wieder schließt) · Estrich (Aufbauhöhe und Türen) ·
Heizungstausch mit Verteilleitungen · Fenster + Fassade (Anschlüsse und GModG-U-Wert) ·
Kellerabdichtung (nur einmal zugänglich).

**Die ehrliche Variante der Etappensanierung [Setzung]:** Erst alles Öffnende und alle Leitungen in
**einem** Zug (Entkernen, Elektro, Sanitär, Heizung, Estrich), dann zieht man ein und macht die
Oberflächen raumweise selbst. Das ist die einzige Etappierung, die den Netzplan nicht verletzt.

### 3.4 Provisorien, Winter, Schleusen

- **Winterfenster/Folienverglasung:** [Setzung] Nur als Notlösung bei einzelner Fensteröffnung. Wer im
  Winter die Hülle öffnet, heizt die Baustelle und trocknet Estrich/Putz langsamer — Trocknung ist
  temperaturabhängig, nicht kalenderabhängig.
- **Baustrom/Bauwasser:** [Setzung] eigene Zähler, Pauschale mit dem Betrieb vereinbaren (Position im
  Angebot, siehe `kosten-bauzeit.md` 3.4).
- **Provisorische Küche/Bad:** [Setzung] Wenn bewohnt, ist die Reihenfolge Bad 1 fertig → umziehen →
  Bad 2. Ein Haus ohne funktionierendes Bad ist keine Baustelle, sondern ein Ausnahmezustand.
- **Schleuse:** Tür mit Reißverschluss, Stöße verklebt, Fluchtwege frei — Aufbauanleitung in
  `entkernen-entsorgung.md` 1.5.

---

## 4. Budget

### 4.1 Die Bänder, nach Sanierungstiefe

| Stufe | Was drin ist | Band | Quelle |
|---|---|---|---|
| **Kosmetisch** (Renovierung) | Streichen, Tapezieren, Böden, Kleinreparaturen | kein eigenes Band belegt — Einzelpreise über `bodenbelaege.md`, `waende.md` | — |
| **Teilsanierung** | Bad + Elektro in Teilen + Oberflächen | 400–1.000 €/m² (als „Kernsanierung" deklariert) | [Q12][Q14][Q18] |
| **Kernsanierung, innen** | Entkernen, Elektro, Sanitär, Heizung, Estrich, Oberflächen | **500–1.500 €/m²** | [Q17] |
| **Vollsanierung mit Hülle** | zusätzlich Dach, Fassade/WDVS, Fenster, Planung, Puffer | **1.800–3.000 €/m²** | [Q11] |
| **Praktiker-Realität** | „sämtliche Gewerke betroffen" | **2.500–3.500 €/m²** | [Q19] |

**Der Widerspruch bleibt stehen** (Abschnitt 1.2): Die Bänder beschreiben unterschiedliche
Sanierungstiefen unter demselben Wort. Wer bietet, muss vorher fragen: „Ist das Dach drin? Die Fassade?
Die Fenster? Die Planung? Der Puffer?"

### 4.2 Kostenanteile je Gewerk

Anteile aus dem Rechenbeispiel in Abschnitt 8 (130 m², Vollsanierung), gerechnet aus den Mittelwerten
der belegten Einzelpreise [Q17][Q12][Q18] — **[Rechnung]**, keine Statistik:

| Gewerk | Anteil an der Gewerkesumme |
|---|---|
| Fassade (WDVS + Gerüst) | **19 %** |
| Heizung | **13 %** |
| Dach | **11 %** |
| Keller (Abdichtung, Dämmung) | **10 %** |
| Fenster | **9 %** |
| Elektro | **9 %** |
| Sanitär (2 Bäder + Rohrnetz) | **8 %** |
| Trockenbau/Putz | **5 %** |
| Innentüren | **4 %** |
| Estrich | **4 %** |
| Fliesen | **3 %** |
| Maler | **3 %** |
| Entkernen/Entsorgung | **3 %** |

**Was daran überrascht:** Die **Hülle** (Fassade + Dach + Fenster + Keller) ist mit rund **49 %** der
größte Block — nicht das Bad. Deshalb ist „innen schön, außen alt" die teuerste Zwischenstufe: Sie
bezahlt die Hälfte des Projekts und lässt die andere Hälfte liegen.

**Gegenprobe an den Einzelpreisen der Portale** (alle pro m² Wohnfläche, soweit nicht anders
angegeben) [Q12][Q18]:

| Gewerk | Band | Quelle |
|---|---|---|
| Dacheindeckung | 80–300 €/m² Dachfläche | [Q12] |
| Dachstuhl neu | 50–150 €/m² Dachfläche | [Q12] |
| Fassadendämmung | 60–500 €/m² (CHECK24), 60–200 €/m² (Sparkasse) | [Q18][Q14] |
| Kellerdecke dämmen | 30–100 €/m² | [Q18] |
| Elektro | 110–170 €/m² | [Q18] |
| Fenster | 650–1.000 €/Stück | [Q18] |
| Heizungsanlage | 9.000–35.000 € gesamt | [Q18] |
| Rohrleitungssystem | 200–300 €/m² | [Q18] |
| Lüftung mit WRG | 6.000–9.000 € gesamt | [Q18] |

**Unbelegt bleibt die Einheit** bei CHECK24 „Umbau der Sanitäranlage **1.000–3.500 €/m²**" [Q18] — pro
m² Bad oder pro m² Wohnfläche? Die Seite sagt es nicht. Deshalb rechne ich in Abschnitt 8 mit dem
Bad-Band aus [Q17] (400–1.200 €/m² Bad).

### 4.3 Puffer und Baunebenkosten

| Position | Höhe | Grundlage |
|---|---|---|
| **Unvorhergesehenes im Bestand** | **10–15 %** der Angebotssumme | [Setzung]; Bestätigung als Praktikerwert: „15 Prozent Puffer ganz gut" [Q23, 00:11:35] |
| **Zeitpuffer** | **20–25 %** | [Q15] nennt diesen Wert für 120 m² selbst |
| **Planung/Bauleitung** | **10–15 %** der Gewerkesumme | [Setzung], HOAI-orientiert; bei KfW 261 kommt der Energieeffizienz-Experte **zusätzlich** und ist **gesondert** zu beauftragen [Q4] |
| **Gerüst, Baustrom, Bauwasser, Versicherung, Container** | **5–8 %** | [Setzung]; Containerpreise belegt in `kosten-bauzeit.md` 3.4 |
| **Bauherrenhaftpflicht** | Pflicht | `kosten-bauzeit.md` 3.4 (Finanztip) |
| **Bauleistungsversicherung** | Kür, endet mit Bezugsfertigkeit | ebd. |

**[Setzung] Die Reihenfolge der Puffer ist wichtiger als ihre Höhe:** Erst Unvorhergesehenes (Fund),
dann Termin, dann Ausstattung. Wer den Puffer für die schönere Armatur ausgibt, hat keinen Puffer —
dieselbe Regel wie in `kosten-bauzeit.md` 3.5.

**Die Zahlungsart entscheidet über den Steuerbonus:** § 35c Abs. 4 verlangt eine **Rechnung**, die
Maßnahme, Arbeitsleistung und Objektadresse ausweist und **in deutscher Sprache** ausgefertigt ist, und
die **Zahlung auf das Konto des Leistenden** [Q6]. Wer bar zahlt oder an eine dritte Person überweist,
verliert die 7/7/6 % — unabhängig davon, wie gut die Sanierung ist. Dieselbe Logik gilt für die
KfW-Nachweise („Rechnungen und Nachweise über geleistete Zahlungen (Kontoauszüge)") [Q4].

### 4.4 Finanzierung — was zusammenpasst und was sich ausschließt

| Kombination | möglich? | Beleg |
|---|---|---|
| KfW 261 + KfW 458 | ja, für **verschiedene** Maßnahmen | [Q4][Q5] (getrennte Produkte, getrennte Vorhaben) |
| KfW 261 + BEG-Einzelmaßnahmen (BAFA) | **nein**; 3 Jahre Wartezeit dazwischen | [Q4] |
| KfW 261 + § 35c EStG | **nein** | [Q4] |
| § 35c EStG + § 7i EStG (Denkmal) | [Setzung] steuerlich getrennt prüfen — § 35c greift nicht, wenn „es sich um eine öffentlich geförderte Maßnahme handelt, für die **zinsverbilligte Darlehen oder steuerfreie Zuschüsse** in Anspruch genommen werden" (§ 35c Abs. 3) [Q6]; § 7i ebenso [Q8] |
| KfW 261 + kommunales Programm | ja, grundsätzlich kumulierbar („Kumulierung … mit anderen Fördermitteln … grundsätzlich möglich") | [Q4] |

**Der Satz, der die Finanzierung rettet:** Die Förderung deckt bei einem 270.000-€-Projekt mit
EH-55-Standard höchstens 150.000 € **Kredit** plus 5 % Tilgungszuschuss (7.500 €) [Q4] — sie ersetzt
kein Eigenkapital, sie verbilligt es. Wer die Finanzierung auf den Zuschuss baut, finanziert eine
Lücke.

---

## 5. Steuerung — wer wann ins Haus kommt und wer was unterschreibt

### 5.1 Vergabeform wählen (nicht: „der erstbeste Handwerker")

| Form | Steuerungsaufwand | Preisrisiko | Wann sinnvoll |
|---|---|---|---|
| **Einzelvergabe** (5–10 Gewerke) | hoch — du bist Bauleiter | verteilt, aber Nachträge je Gewerk | wenn du Zeit hast und Preise vergleichen willst; Voraussetzung für Eigenleistung |
| **Generalunternehmer** | niedrig | Festpreis, aber ohne Mitbestimmung bei den Gewerken [Q21] | wenn Termin und ein Ansprechpartner wichtiger sind als 10 % Preis |
| **Bauträger** | minimal | Festpreis | wenn du nicht Bauherr sein willst — dann aber auch kein Weisungsrecht [Q21] |

**Beim GU immer zwei Sicherheiten** (Dr. Klein, aus Verbrauchersicht): eine
**Vertragserfüllungsbürgschaft** von mindestens **5 %**, besser **10 %** der Vergütung, und eine
**Vorauszahlungssicherheit** für geleistete Anzahlungen [Q21]. Ohne Bürgschaft ist die Insolvenz des GU
dein Risiko — „Der Bau stoppt… Eventuell sind Sie auch schon in Vorleistung gegangen" [Q21].

### 5.2 Ausschreibung: was ins Leistungsverzeichnis gehört

Aus `kosten-bauzeit.md` 4.1 (dort vollständig): Positionen mit Menge, Einheit, Einheitspreis;
Material mit Fabrikat; Stundenlohnsatz; Nebenkosten einzeln; Bauzeit mit Terminen; Zahlungsplan;
Nachtragsregel; Abnahme und Gewährleistung; **Ausschlüsse**; USt; Gültigkeit. Die Verbraucherzentrale
fordert „möglichst detaillierte" Kostenvoranschläge mit Stundensätzen und Materialpreisen [Q10].

**Für die Komplettsanierung zusätzlich:**

- **Schnittstellen benennen.** Wer schließt die Fensterlaibung nach dem Fenstertausch — Fensterbauer
  oder Putzer? Wer verfüllt die Elektroschlitze? Diese zwei Fragen erzeugen die meisten Nachträge.
- **Erkundung als eigene Position.** Die technische Erkundung auf Asbest ist laut BG BAU eine
  „besondere Leistung" und damit **kostenpflichtig** [Q3] — sie gehört ins LV, nicht in die
  Überraschungskategorie.
- **Fotos und Protokolle als Leistung.** Messprotokoll Elektro (DIN VDE 0100-600), Druckprobe Wasser,
  Dichtheitsprotokoll Heizung, CM-Protokoll Estrich — als Vertragspflicht, nicht als Gefälligkeit.

### 5.3 Bauleitung: wer sie macht und was sie kostet

Drei Modelle, alle legitim:

1. **Architekt/Ingenieur mit LPH 8** (Objektüberwachung): teuerste, aber vollständigste Variante.
   Honorar und Leistungsbild: Klotzkette-Skill `hoai-leistungsphasen-praxis`
   (`lph8-bauueberwachung-mehrfamilienhaus-effh`).
2. **Freier Bausachverständiger / Bauherrenberater** stunden- oder pauschalweise — sinnvoll bei
   Einzelvergabe.
3. **Eigenbauleitung** — möglich, wenn du drei Dinge hast: Zeit (täglich vor Ort), ein
   Terminplan-Tool und die Fähigkeit, Mängel zu benennen statt zu ahnen.

**[Setzung] Die Grenze der Eigenbauleitung:** Du kannst Koordination, Termine und Optik. Du kannst
nicht Statik, Abdichtung, Elektro-Messung und Schadstoffbewertung beurteilen. Genau diese vier Punkte
sind die, die später Geld kosten.

### 5.4 Meilensteine, an denen man zahlt und prüft

| Meilenstein | Prüfinhalt | Zahlung |
|---|---|---|
| **M0 Förderzusage** | BzA liegt vor, Antrag gestellt, **vor** Auftrag | 0 % |
| **M1 Entkernung fertig** | Fotos jeder Wand mit Maßband, Schadstoffbefund dokumentiert | 10–20 % |
| **M2 Rohinstallation fertig** | Druckprobe, Messprotokoll, Leitungsplan | 20–30 % |
| **M3 Hülle dicht** | Fenster/Anschlüsse, Dach dicht, Dämmstärken | 20 % |
| **M4 Estrich + Belegreife** | CM-Protokoll | 15 % |
| **M5 Fliesen/Böden/Türen** | Fugenbild, Türspalt, Gefälle | 15 % |
| **M6 Endmontage** | FI-Prüfung, Dichtheit, Funktion | 10 % |
| **M7 Abnahme** | Mängelprotokoll, Fristen, Vorbehalt | Rest + Einbehalt |

**Rechtlicher Rahmen des Zahlens** (geprüft in `kosten-bauzeit.md` 5.3): Abschläge nur „in Höhe des
Wertes der erbrachten … Leistungen" (§ 632a BGB) [Q25]; Fälligkeit bei Abnahme (§ 641) [Q26]; bei
Mängeln Zurückbehaltung in der Regel **das Doppelte** der Mängelbeseitigungskosten [Q26]; VOB/B nur,
wenn wirksam vereinbart (`lxgesetze.de/vob-b-2016/13`, 4 Jahre bei Bauwerken) [Q27].

### 5.5 Abnahme je Gewerk — die vier Fehler, die der Handwerker fürchtet

Aus Handwerkssicht (handwerk.com, Fachanwalt für Bau- und Architektenrecht) [Q22]:

1. **Der Bauherr unterschreibt nicht.** „Der Auftraggeber muss unterschreiben, sonst kommt die Abnahme
   nicht zustande" [Q22]. Unterschreibt nur der Architekt oder Bauleiter, braucht er **schriftliche
   Vollmacht** bzw. Prokura — sonst ist das Protokoll „im Streitfall nichts wert" [Q22].
2. **Gewährleistungsfristen im Protokoll weichen vom Vertrag ab** — und die **neuen** Fristen sind
   bindend, auch wenn sie länger sind [Q22]. Also: Protokoll lesen, bevor du unterschreibst.
3. **Mängel nicht benannt.** Unwesentliche Mängel hindern die Abnahme nicht (§ 640 Abs. 1 BGB) [Q26] —
   aber nur, wenn sie im Protokoll stehen.
4. **Kein Vorbehalt.** Bei bekannten Mängeln gilt die Abnahme nur mit Vorbehalt (§ 640 Abs. 3 BGB);
   die Verbraucherzentrale empfiehlt den Satz „Die Geltendmachung von Gewährleistungsansprüchen bleibt
   vorbehalten" [Q10].

**[Setzung] Abnahme je Gewerk, nicht nur am Ende.** Jedes Gewerk bekommt eine eigene Begehung mit
eigener Mängelliste und eigener Frist. Wer erst am Ende abnimmt, nimmt Gewerke ab, die seit vier
Monaten zugedeckt sind.

### 5.6 Nachträge

Aus `kosten-bauzeit.md` 5.1: § 650b Abs. 1 BGB (Änderung: Angebot über Mehr-/Mindervergütung),
§ 650c Abs. 1 (Abrechnung nach tatsächlich erforderlichen Kosten mit Zuschlägen), § 650c Abs. 3 (80 %
in Abschlägen) [Q25]; VOB/B § 2 Abs. 5/6 (neuer Preis, Ankündigung **vor** Ausführung) [Q27].

**Die Sanierungs-Regel dazu:** Bei einem Bestandsobjekt ist der Nachtrag **normal**, nicht böswillig —
„beim Öffnen der Wände besteht Ihr unvermeidliches Kostenrisiko" [Q10]. Was ihn beherrschbar macht, ist
nicht die Ablehnung, sondern das Verfahren: **schriftliche Anordnung mit Menge × Einheitspreis, vor der
Ausführung.** Der Satz „das machen wir später" ist der Anfang des Streits.

**[Setzung] Nachtrags-Budget:** 10–15 % (Abschnitt 4.3) ist kein Misstrauen gegen den Handwerker,
sondern der Preis dafür, dass niemand vorher in die Wand sehen konnte.

### 5.7 Die vier Instrumente (das „Werkzeug" dieses Playbooks)

Bei einer Komplettsanierung ist das Werkzeug kein Stemmhammer, sondern ein Satz Dokumente. Ohne diese
vier ist die Bauleitung nicht vorhanden, egal wer sie übernimmt:

| Instrument | Inhalt | Rhythmus |
|---|---|---|
| **Bauzeitenplan** | Gewerk, Vorgänger, Dauer, Puffer, Verantwortlicher — ein Balkenplan, kein Kalenderzettel | wöchentlich fortschreiben, sichtbar auf der Baustelle |
| **Zahlungsplan** | Abschlag je Meilenstein (5.4), gebunden an Leistungsstand und Prüfprotokoll | je Abschlag, schriftlich |
| **Mängelprotokoll** | je Gewerk: Mangel, Ort, Foto, Frist, Verantwortlicher, Status | Begehung je Gewerk + Nachkontrolle |
| **Fotoprotokoll** | jede Wand offen mit Maßband, je Raum sortiert; Leitungen, Dämmstärken, Abdichtungslagen | täglich, sobald etwas zugedeckt wird |

**[Setzung] Das Fotoprotokoll ist das einzige Instrument, das nach dem Einzug noch Wert hat.** Es
entscheidet, ob der Bohrer für das Regal ein Kabel trifft — und es ist die Beweisgrundlage, wenn ein
Mangel zwei Jahre später sichtbar wird. Die Foto-Regel und die Belegakte sind in `SKILL.md`
(„Dokumentation, Abnahme, Gewährleistung") und `kosten-bauzeit.md` beschrieben.

---

## 6. Schadstoffe und die Überraschungen, die niemand kalkuliert

### 6.1 Die Pflichtenlage (und wer sie hat)

**§ 5a GefStoffV**, wörtlich: „Derjenige, der Tätigkeiten an baulichen oder technischen Anlagen
veranlasst (Veranlasser), hat **vor Beginn** der Tätigkeiten dem ausführenden Unternehmen alle ihm
vorliegenden Informationen zur **Bau- oder Nutzungsgeschichte** über vorhandene oder vermutete
Gefahrstoffe schriftlich oder elektronisch zur Verfügung zu stellen." Und: „**Die Absätze 1 bis 3 gelten
auch für private Haushalte**" (§ 5a Abs. 4) [Q9].

Das heißt: **Du** bist der Veranlasser — auch im eigenen Haus, auch ohne Firma. Du musst nicht
erkunden, aber du musst weitergeben, was du weißt. Abs. 2 verlangt zusätzlich: Bei Objekten mit
**Baujahr zwischen 1993 und 1996** ist das **Datum des Baubeginns** zu übermitteln (oder das Baujahr,
wenn das Datum unbekannt ist); bei Objekten **vor 1993 oder nach 1996** reicht das **Baujahr** [Q9].

**Der Stichtag, an dem die Praxis hängt:** „Entsprechend der Stichtagsregelung muss in allen Gebäuden,
die **vor dem 31. Oktober 1993** errichtet wurden, mit Asbest in den Baustoffen beziehungsweise der
Bausubstanz gerechnet werden" [Q3]; das Verbot gilt seit 1993 [Q20].

**Wer erkundet:** Nicht du. Das **Bauunternehmen** muss laut BG BAU „eine technische Erkundung in den
Gebäuden durchführen lassen, um das Vorhandensein von Asbest zu klären", und die Kosten „gelten als
besondere Leistung" [Q3] — also als vergütungspflichtige Zusatzleistung, nicht als im Preis enthalten.

### 6.2 Das Ampel-Modell (seit 5.12.2024)

Die novellierte GefStoffV (in Kraft **5. Dezember 2024**) hat ein risikobezogenes Maßnahmenkonzept
eingeführt [Q3]:

| Bereich | Faserstaubbelastung | Konsequenz |
|---|---|---|
| **rot** (hohes Risiko) | > **100.000 Fasern/m³** | nur Fachfirmen mit Zulassung; „Handwerksbetriebe werden solche Arbeiten faktisch nicht ausführen" [Q3] |
| **gelb** (mittleres Risiko) | < 100.000 Fasern/m³ | abgestufte Schutzmaßnahmen, Qualifikation |
| **grün** (niedriges Risiko) | < 10.000 Fasern/m³ | abgestufte Schutzmaßnahmen |

**Neu und für die Sanierung wichtig:** Tätigkeiten der „funktionalen Instandhaltung" im niedrigen und
mittleren Risikobereich sind jetzt legalisiert — „beispielsweise Schlitze in asbesthaltigem Putz zur
Verlegung einer Elektroleitung gefräst werden" [Q3]. Vorher war das unzulässig. **Das ändert die
Elektro-Planung im Bestand:** Der Elektriker darf mehr, aber nur mit Schutzmaßnahmen und Qualifikation —
und die Erkundung muss vorher sein.

**Verbote, die bleiben:** Überdeckung, Überbauung und Aufständerung von Asbestzementdächern (z. B.
Photovoltaik) sind verboten; neu hinzugekommen ist ein Überdeckungsverbot für
Asbestzementdeckenverkleidungen und asbesthaltige Bodenbeläge [Q3]. **Für die Planung heißt das:** PV
aufs alte Eternitdach ist keine Option — Dach zuerst.

### 6.3 Die Fundstellen, mit denen man rechnen muss

Aus `entkernen-entsorgung.md` und UBA [Q20] — hier nur die Übersicht, Details dort:

| Stoff | Wo | Stichtag/Erkennung |
|---|---|---|
| **Asbest** | Fassaden-/Dachplatten (Eternit), Putze, Spachtelmassen, Fliesenkleber, Bodenbeläge inkl. Bitumenkleber, Rohrisolierungen, Nachtspeicheröfen, Fensterkitt bis ca. 1990 | Baubeginn **vor 31.10.1993** [Q20] |
| **KMF** (alte Mineralwolle) | Dämmung in Hohlräumen, Zwischensparrendämmung, Trittschalldämmung | **vor 1996 eingebaut = „alte Mineralwolle"** [Q29] |
| **PAK** | Parkettkleber (Teerkork), Schwarzanstrich, Dachpappe | TRGS 551 „Teer und andere Pyrolyseprodukte aus organischem Material" [Q28]; Geruch nach Teer ist ein Indiz **[Setzung]** |
| **Blei** | alte Lacke (Fenster, Türen, Heizkörper), Wasserleitungen | **[Setzung]** vor 1970 fast regelhaft; TRGS 505 nicht separat geprüft |
| **Schimmel/Feuchte** | Keller, Laibungen, nach Wasserschaden | `schimmel-feuchte.md` |
| **Holzwurm** | Dachstuhl, Balken, Dielen | `dachboden-holzdecke.md` |

**[Setzung] Die Reihenfolge, die Geld spart:** Erst Baujahr und Bauakten prüfen (kostenlos), dann
Sichtprüfung an drei Stellen (Dachüberstand, Bad, Heizungsrohre), dann **Materialprobe** — und erst
danach das Angebot finalisieren. Wer das Angebot vor der Probe macht, bekommt einen Preis für ein Haus,
das er nicht hat.

### 6.4 Die typischen Überraschungen (und was sie kosten)

| Überraschung | Erkennbar woran | Wirkung |
|---|---|---|
| **Betondecke statt Holzbalkendecke** (oder umgekehrt) | Baujahr, Klopftest, Öffnung | Leitungsführung, Deckendurchbrüche, Trittschall — `decke.md`, `dachboden-holzdecke.md` |
| **Stahlträger über dem Durchbruch** | Statik, Sichtprüfung | neuer Träger, Brandschutz, Statik-Nachweis |
| **Feuchter Keller** | Salzausblühungen, Geruch, Messung | Außenabdichtung **300–600 €/m²** statt innen **50–200 €/m²** [Q17] |
| **Alte Elektrik ohne Schutzleiter** | Dosen öffnen, zwei Adern | kompletter Neuaufbau statt „erweitern" — `elektro.md` |
| **Asbest im Fliesenkleber** | Baujahr, Probe | Fliesen abschlagen wird ASI-Arbeit: Anzeige, Sachkunde, Fachfirma [Q20] |
| **Holzwurm im Dachstuhl** | Ausfluglöcher, Mehlstaub | Teilersatz oder Insektizid — `dachboden-holzdecke.md` |
| **„Nicht tragende" Wand** | nur die Statik sagt es | Durchbruch wird Statik-Aufgabe, nicht Abbruch |
| **Fundament zu schwach** | Gutachter, Baggerschurf | kippt die Entscheidung Richtung Abriss [Q11] |

**[Setzung] Der Umgang mit Überraschungen ist eine Budgetfrage, keine Nervenfrage:** Jede Öffnung, die
du vor der Vergabe machst (Probefläche, Sondierung, ein Fliesenspiegel ab), kostet dreistellig und
spart vierstellig.

---

## 7. Typische Fehler — mit Quelle

| # | Fehler | Wie er aussieht | Warum er teuer ist | Quelle |
|---|---|---|---|---|
| 1 | **Ohne Plan anfangen** | „Wir fangen im Bad an und sehen dann weiter" | „Die teuerste Variante ist fast immer die, bei der man mitten in der Sanierung merkt, dass man besser abgerissen hätte" | [Q11] |
| 2 | **Gewerke falsch gereiht** | Estrich vor Elektro, Fliesen vor Abdichtung | Jeder Tausch kostet doppelt: Kabel nach Putz = Schlitze wieder auf | `kosten-bauzeit.md` 2.1 |
| 3 | **Elektro nach Estrich/Putz** | „Der Elektriker kommt nächste Woche" | Schlitze in fertigen Wänden, Fliesen wieder ab; Ausbaureserve im Verteiler aufgebraucht | [Q24, 00:06:05] |
| 4 | **Fenster vor Dämmung** (oder umgekehrt, ohne Anschlussplan) | Fenster neu, Fassade „später" | Laibungen und Anschlüsse zweimal; U-Wert passt nicht mehr zur GModG-Anforderung (Uw 1,30) | [Q2] |
| 5 | **Keine Abnahme je Gewerk** | „Zum Schluss schauen wir alles an" | Mängel sind zugedeckt; Gewährleistungsfrist beginnt ohne Mängelliste; ohne Unterschrift des Bauherrn kommt die Abnahme nicht zustande | [Q22] |
| 6 | **Puffer vergessen** | Budget = Summe der Angebote | „15 Prozent Puffer" ist der Praxiswert; jeder Fund ist „ein Nachschlag, der im ursprünglichen Angebot nicht stand" | [Q23, 00:11:35][Q11] |
| 7 | **Bewohner bleiben drin** | „Wir halten es aus" | Bewohnung bremst Abläufe; Dauer „ungefähr doppelt so lange wie geplant"; Dreck als Dauerzustand | [Q15][Q23, 00:00:50][Q24, 00:03:52] |
| 8 | **Förderung nach Beginn beantragt** | Bagger läuft, Antrag kommt später | „Der Antrag ist vor Beginn des Vorhabens … zu stellen" — sonst keine Förderung | [Q4] |
| 9 | **15-%-Falle beim Kauf** | Kaufen, drei Jahre sanieren, sofort absetzen wollen | Über 15 % der Gebäude-Anschaffungskosten in drei Jahren = anschaffungsnahe Herstellungskosten, Abschreibung statt Sofortabzug | [Q11][Q7] |
| 10 | **Angebot ohne Positionen** | „Kernsanierung komplett 180.000 €" | nicht vergleichbar, Nachträge vorprogrammiert | [Q10] |
| 11 | **GU ohne Bürgschaft** | „Der macht das schon" | Insolvenz = Baustopp, Anzahlung weg; mindestens 5 %, besser 10 % Vertragserfüllungsbürgschaft | [Q21] |
| 12 | **Schadstoffe nicht erkundet** | Fliesen trocken abgeschlagen, Putz gefräst | § 5a GefStoffV gilt auch privat; Rückbau wird ASI-Arbeit; Erkundung ist „besondere Leistung" | [Q9][Q3] |
| 13 | **Denkmal ohne Abstimmung** | Eigenmächtig Fenster getauscht | Bescheinigung fehlt → keine § 7i-AfA; KfW verlangt Genehmigung | [Q8][Q4] |
| 14 | **Nur Angebotspreise addiert** | „Die Gewerke kosten 126.000, also kostet es 126.000" | Planung, Gerüst, Versicherung, Puffer fehlen — die Lücke zwischen 400–1.000 und 1.800–3.000 €/m² ist genau diese | [Q11][Q19] |
| 15 | **Etappiert, was nicht etappierbar ist** | Elektro in Etappe 1, Estrich in Etappe 3 | Aufbauhöhe, Türen und Leitungen passen nicht mehr zusammen | [Q15] |

---

## 8. Rechenbeispiel: 130 m², Baujahr 1965, Kernsanierung

### 8.1 Annahmen (alle änderbar, alle benannt)

| Größe | Wert | Herkunft |
|---|---|---|
| Wohnfläche | **130 m²** | Vorgabe |
| Baujahr | **1965** | Vorgabe; damit **vor** dem Asbeststichtag 31.10.1993 [Q3] |
| Gebäude | Einfamilienhaus, 2 Vollgeschosse, Satteldach ~35°, **kein** ausgebauter Dachboden | [Setzung] |
| Dachfläche | **95 m²** | [Setzung], aus Grundfläche ~65 m² und Neigung |
| Fassadenfläche | **170 m²** | [Setzung], Umfang ~33 m × 5,8 m minus Fenster |
| Bäder | **2** (8 m² + 5 m²), eines davon neu | [Setzung] |
| Zustand | Elektro zweiadrig, Ölheizung von 1998, Fenster 1985, kein WDVS, Keller trocken mit Salzausblühungen | [Setzung] — typische 1960er-Konstellation nach [Q16] |
| Standard | EH 55 EE angestrebt (KfW 261) | [Q4] |

### 8.2 Kostenaufstellung je Gewerk

Preise aus [Q17] (Stand Mai 2026) und [Q12], Mengen **[Setzung]**, Summen **[Rechnung]**.

| Gewerk | Menge | Einheit | EP min | EP max | Summe min | Summe max |
|---|---|---|---|---|---|---|
| Entkernen, Entsorgung (Container, Sortierung) | 130 | m² WF | 20 € | 30 € | 2.600 € | 3.900 € |
| Elektro komplett (Zähler, Verteiler, Leitungen, Dosen) | 130 | m² WF | 50 € | 120 € | 6.500 € | 15.600 € |
| Sanitär: 2 Bäder + Rohrnetz | 13 | m² Bad | 400 € | 1.200 € | 5.200 € | 15.600 € |
| Heizung: Wärmepumpe + Verteiler + Heizkörper | 1 | psch | 8.000 € | 25.000 € | 8.000 € | 25.000 € |
| Fenster 12 Stück, 3-fach | 12 | St | 400 € | 1.500 € | 4.800 € | 18.000 € |
| Dach: Dämmung + Neueindeckung | 95 | m² Dachfläche | 80 € | 200 € | 7.600 € | 19.000 € |
| Fassade: WDVS + Gerüst | 170 | m² Fassade | 80 € | 200 € | 13.600 € | 34.000 € |
| Keller: Innenabdichtung + Dämmung | 100 | m² Wandfläche | 50 € | 200 € | 5.000 € | 20.000 € |
| Estrich + Trittschalldämmung | 130 | m² WF | 20 € | 60 € | 2.600 € | 7.800 € |
| Trockenbau, Putz, Spachtel Q3 | 130 | m² WF | 30 € | 60 € | 3.900 € | 7.800 € |
| Fliesen inkl. Material | 45 | m² | 80 € | 80 € | 3.600 € | 3.600 € |
| Innentüren + Zargen | 8 | St | 500 € | 900 € | 4.000 € | 7.200 € |
| Maler Wände/Decken | 130 | m² WF | 20 € | 35 € | 2.600 € | 4.550 € |
| **Gewerkesumme** | | | | | **70.000 €** | **182.050 €** |
| **pro m² Wohnfläche** | | | | | **538 €** | **1.400 €** |

**Mittelwert der Gewerke: 126.025 €** (969 €/m²) — **[Rechnung]** aus den Mittelwerten der
Einzelbänder.

### 8.3 Vom Gewerk zum Projektpreis

| Position | min | max | Rechenweg |
|---|---|---|---|
| Gewerkesumme | 70.000 € | 182.050 € | Tabelle 8.2 |
| + Planung/Bauleitung 10–15 % | 7.000 € | 27.308 € | [Setzung], auf Gewerkesumme |
| + Gerüst/Baustrom/Versicherung/Container 5–8 % | 3.500 € | 14.564 € | [Setzung] |
| + Puffer 10–15 % | 8.050 € | 33.588 € | [Q23] |
| **Projektsumme** | **88.935 €** | **260.022 €** | [Rechnung] |
| **pro m²** | **684 €** | **2.000 €** | [Rechnung] |

**Mittelwert mit Zuschlägen: 169.868 € = 1.307 €/m²** (Gewerke-Mittel 126.025 € × 1,125 × 1,065 ×
1,125) — **[Rechnung]**.

### 8.4 Der Realitätsabgleich — und warum die Rechnung zu niedrig ist

Die Rechnung aus Einzelpreisen landet bei **684–2.000 €/m²**, Mittel **~1.300 €/m²**. Der Markt für eine
Vollsanierung liegt laut Bausachverständigem bei **1.800–3.000 €/m²** [Q11], laut Praktikern bei
**2.500–3.500 €/m²** [Q19].

**Die Lücke hat vier Ursachen, alle belegt oder plausibel:**

1. **Die Bänder sind Mittelwerte aus ausgeschriebenen Projekten.** Die BKI-Preise, auf denen die
   Tabellen beruhen, sind „statistische Mittelwerte aus ausgeschriebenen und abgerechneten Projekten";
   bei Einzelmaßnahmen und direkter Beauftragung durch den Bauherrn ist „mit Preiszuschlägen und
   Mehrkosten zu rechnen" [Q14, Fußnote zur BKI-Tabelle].
2. **Bestand ist kein Neubau.** Aufmaß, Bestandsschutz, Anschlüsse an alte Substanz und Arbeiten im
   bewohnten/geräumten Zustand kosten Zuschläge — `fenster-tueren.md` nennt für Altbau vor 1970
   **50–100 % Zuschlag** auf den Neubau-Richtwert.
3. **Positionen fehlen in jeder Liste:** Baustelleneinrichtung, Entsorgung von Sonderabfall,
   Schadstoffsanierung, Anschlussarbeiten, Statik, Blower-Door, Dokumentation.
4. **Der Bieter kalkuliert sein Risiko.** Wer eine Kernsanierung im Bestand anbietet, weiß, was hinter
   der Wand steckt — und legt es ein.

**[Setzung] Planwert für dieses Haus: 2.080 €/m² = 270.000 €.** Das ist die Mitte zwischen
gerechnetem Mittel (1.307) und Marktband (1.800–3.000), gewichtet nach der Erfahrung, dass
Bestandsangebote am oberen Rand der Bänder liegen. **Planungsband: 235.000–390.000 €.**

### 8.5 Die 75-Prozent-Prüfung

| Größe | Wert | Rechnung |
|---|---|---|
| Neubau vergleichbar, 130 m² × 3.000 €/m² | **390.000 €** | [Q11] Unterkante |
| Neubau vergleichbar, 130 m² × 4.000 €/m² | **520.000 €** | [Q11] Oberkante |
| **75-%-Schwelle** | **292.500 € – 390.000 €** | [Rechnung] |
| Kernsanierung, Planwert | **270.000 €** | Abschnitt 8.4 |
| Kernsanierung, oberes Band | **390.000 €** | Abschnitt 8.4 |

**Ergebnis:** Mit 270.000 € liegst du **unter** der unteren Schwelle (292.500 €) → **sanieren ist
begründet**. Kommt es wie im oberen Band auf 390.000 €, kostet die Sanierung **so viel wie der
billigste vergleichbare Neubau** — dann ist der Abriss keine Niederlage, sondern die wirtschaftlich
klügere Entscheidung [Q11].

**Die Sensitivität, die die Entscheidung kippt** (jeweils +1 Position, [Rechnung]):

| Wenn … | Wirkung | Neue Quote |
|---|---|---|
| Asbest in Fassade + Fliesenkleber (Sanierung 25.000 €) | +25.000 € | 295.000 € = **76 %** der unteren Neubauschätzung → Abriss prüfen |
| Keller muss außen abgedichtet werden statt innen | +20.000 € | 290.000 € = **74 %** → noch sanieren |
| Energieeffizienz EH 40 statt EH 55 (mehr Dämmung, bessere Fenster) | +25.000–40.000 € | 295.000–310.000 € → **Grenzbereich** |
| Grundrissänderung mit Statik (2 Träger, 3 Durchbrüche) | +15.000–30.000 € | 285.000–300.000 € → **Grenzbereich** |

**Das ist der Grund, warum die Substanzprüfung (1.1) vor der Entscheidung steht:** Drei Positionen
entscheiden über 75 % — und keine davon sieht man ohne Öffnung.

### 8.6 Zeitplan in Wochen

| Block | Wochen | Kummuliert |
|---|---|---|
| Entscheidung, Gutachten, Energieberater, BzA, KfW-Antrag | 4–8 | 8 |
| Planung, Ausschreibung, Vergabe, Materialbestellung | 6–12 | 20 |
| Entkernen + Entsorgung | 2–3 | 23 |
| Rohinstallation (Elektro, Sanitär, Lüftung, Heizung) | 5–8 | 31 |
| Dach + Fassade + Fenster (parallel zur Rohinstallation) | 4–8 | 31 (parallel) |
| Trockenbau, Putz, Spachtel | 3–5 | 36 |
| Estrich + Trocknung + Belegreife | 5–7 | 43 |
| Abdichtung + Fliesen | 3–4 | 47 |
| Türen, Böden, Treppe | 2–3 | 50 |
| Küche, Bad, Elektro-Fertiginstallation | 2–3 | 53 |
| Maler, Außenanlagen, Reinigung | 2–4 | 57 |
| Abnahme, Mängel, Restarbeiten | 2–3 | 60 |

**Summe 50–60 Wochen netto** aus den Phasen [Q15] (dort 120 m²: 6–9 Monate = 26–39 Wochen Bauzeit, hier
auf 130 m² und zwei Bäder skaliert). **Mit 20–25 % Puffer: 60–75 Wochen = 14–17 Monate bis zum
Einzug.** Wer 12 Monate plant, plant den Umzug zweimal — und die Miete dreimal.

### 8.7 Break-even gegenüber Neubau und Verkauf

**Variante A — bleiben (Vergleich gegen Neubau):**

| Position | Sanierung | Abriss + Neubau |
|---|---|---|
| Baukosten | 270.000 € | 390.000–520.000 € |
| Abriss + Entsorgung | — | 10.000–30.000 € [Q13] |
| Grundstück | vorhanden | vorhanden (kein Ansatz) |
| Förderung (EH 55, KfW 261) | −7.500 € Tilgungszuschuss (5 % von 150.000 €) [Q4] | ggf. Neubauförderung, hier nicht angesetzt |
| **Einsatz** | **~262.500 €** | **~400.000–550.000 €** |
| Ergebnis | „guter Altbau", nicht Neubau-Niveau [Q11] | Neubaustandard, neuer Grundriss |

**Break-even:** Die Sanierung ist günstiger, solange die Mehrkosten des Neubaus (**130.000–290.000 €**)
nicht durch den höheren Endwert und die niedrigeren Betriebskosten aufgezehrt werden. **[Setzung]** Bei
einem Zins von 3,5 % und 25 Jahren entspricht jede 100.000 € Mehrinvestition etwa **500 €/Monat** Rate —
dafür müsste der Neubau mindestens diese Differenz an Wert und Nebenkosten zurückholen.

**Variante B — verkaufen statt sanieren:**

| Weg | Rechnung |
|---|---|
| unsaniert verkaufen | Erlös = Verkehrswert im Ist-Zustand; Käufer zieht die Sanierungskosten ab (Marktpreis) |
| sanieren und verkaufen | Erlös = Verkehrswert saniert **minus** 270.000 € Einsatz **minus** Zins während der Bauzeit |

**[Setzung] Die Faustregel:** Sanieren und dann verkaufen lohnt nur, wenn der Erlöszuwachs **größer** ist
als Sanierungskosten + Finanzierungskosten + 12–17 Monate Kapitalbindung. In den meisten Lagen ist der
Erlöszuwachs kleiner — Sanierung rechnet sich für den **eigenen** Einzug, nicht für den Wiederverkauf.
Die belastbare Zahl dafür kommt aus dem Bodenrichtwert und dem lokalen Vergleichswert: dafür ist
`german-property-valuation` zuständig, nicht dieses Playbook.

---

## 9. Kontrollpunkte (ausdrucken und abhaken)

**Vor dem ersten Handwerker**

- [ ] Bauakten besorgt (Baujahr, Baubeginn, An-/Umbauten) — Pflichtangabe nach § 5a GefStoffV [Q9]
- [ ] Substanzprüfung: Gründung, Tragwerk, Dachstuhl, Feuchte, Elektro
- [ ] Schadstoffsichtprüfung + Materialprobe bei begründetem Verdacht (Baujahr vor 1993)
- [ ] Neubaukosten für ein vergleichbares Haus auf demselben Grundstück ermittelt (75-%-Regel) [Q11]
- [ ] Zwei Kalkulationen: Sanierung mit Risikoaufschlag, Abriss + Neubau [Q11]
- [ ] Energieberater beauftragt, Zielstufe festgelegt (EH 55 / 70 / 40) [Q4]
- [ ] KfW-Antrag **vor** Vergabe gestellt, BzA liegt vor [Q4]
- [ ] Steuerfolge geprüft (bei Kauf: 15-%-Falle; bei Denkmal: § 7i-Bescheinigung) [Q7][Q8]

**Vor dem Rückbau**

- [ ] Bauzeitenplan mit Trocknungszeiten und Puffer, von allen Gewerken bestätigt
- [ ] Alle Gewerke **terminiert**, nicht nur beauftragt
- [ ] Material bestellt, Liefertermine schriftlich
- [ ] Fotos jeder Wand mit Maßband, Grundriss mit Leitungsführung
- [ ] Nachbarinformationsschreiben, Halteverbotszone, Containerstellplatz geklärt

**Während des Baus**

- [ ] Nach jedem Gewerk: Begehung + Mängelliste + Frist, nicht „am Ende"
- [ ] Messprotokolle einsammeln: Elektro (DIN VDE 0100-600), Druckprobe Wasser, Dichtheit Heizung,
      CM-Messung Estrich (Liste in `SKILL.md`, „Dokumentation, Abnahme, Gewährleistung")
- [ ] Nachträge nur schriftlich, Menge × Preis, **vor** Ausführung (§ 650b/c BGB) [Q25]
- [ ] Zahlungen an Leistungsstände gebunden (§ 632a BGB), Einbehalt vereinbart [Q25]
- [ ] **Jede Rechnung per Überweisung auf das Konto des Leistenden** — Barzahlung kostet den
      § 35c-Bonus (§ 35c Abs. 4 Nr. 2) [Q6]
- [ ] Bei GU: Bürgschaft über mindestens 5 %, besser 10 % [Q21]
- [ ] Fotodokumentation je Bauphase, digital und gesichert

**Bei der Abnahme**

- [ ] Abnahme **je Gewerk**, mit eigenem Protokoll [Q22]
- [ ] Der **Bauherr** unterschreibt (oder ein Bevollmächtigter mit schriftlicher Vollmacht) [Q22]
- [ ] Gewährleistungsfristen im Protokoll gegen den Vertrag geprüft (Änderung ist bindend) [Q22]
- [ ] Vorbehaltssatz bei bekannten Mängeln: „Die Geltendmachung von Gewährleistungsansprüchen bleibt
      vorbehalten" [Q10]
- [ ] Fristen je Mangel, Verantwortlicher, Nachbesserungstermin

**Nach dem Einzug**

- [ ] Bauwerksbuch: Angebote, Rechnungen, Protokolle, Fotos, Herstellerunterlagen, Garantien
- [ ] Förder-Nachweise: BnD, Rechnungen, Kontoauszüge, bei 261 zusätzlich 10 Jahre Nutzungspflicht
      beachten [Q4]
- [ ] Wartungsvertrag Heizung/Lüftung, Einregulierung protokolliert [Q15]

---

## 10. Wo das Detail steht

| Frage | Playbook |
|---|---|
| Entkernen, Container, Entsorgung, Staubschutz, Schleuse | `entkernen-entsorgung.md` |
| Elektro: Bestand, Normen, Pfusch, Vorbereitung | `elektro.md` |
| Sanitär, Vorwand, Wasser/Abwasser | `sanitaer.md` |
| Heizung, Fußbodenheizung, Lüftung, GEG/GModG-Anforderungen | `heizung-lueftung.md` |
| Dämmung: Dach, Fassade, Keller, Innendämmung, Dampfbremse | `daemmung.md` |
| Fenster/Türen: Tausch, Anschluss, Aufarbeitung | `fenster-tueren.md` |
| Fassade außen, Terrasse, Pflaster, Gerüst | `aussen-fassade-terrasse.md` |
| Estrich, Aufbauhöhen, Belegreife | `estrich.md` |
| Abdichtung, Fliesen, Gefälle | `fliesen.md`, `bad.md` |
| Böden, Trittschall, Sockelleisten | `bodenbelaege.md` |
| Trockenbau, Vorsatzschale, Brandschutz | `trockenbau.md` |
| Keller, Mauerwerk, Salzausblühungen | `keller-mauerwerk.md` |
| Schimmel, Lüftungszahlen | `schimmel-feuchte.md` |
| Dachboden, Holzbalkendecke, Holzwurm | `dachboden-holzdecke.md` |
| Treppe, Geländer, DIN 18065 | `treppe.md` |
| Küche, Anschlüsse, Arbeitshöhe | `kueche.md` |
| Bauzeitenplan, Angebotscheck, Nachträge, Zahlungsplan | `kosten-bauzeit.md` |
| Werkzeug, Absaugung, Asbest-Entsorgung | `werkzeug-sicherheit.md` |
| Genehmigung, Nachbar, Denkmal, Versicherung | `recht-renovierung.md` |
| Baufirma, Werkvertrag, Abnahme | `hausbau-baufirma.md` |
| HOAI-Leistungsphasen, Bauüberwachung, DIN 276 | Klotzkette-Skill `hoai-leistungsphasen-praxis` |
| Wert, Bodenrichtwert, Verkauf | `german-property-valuation` |

---

## 11. Quellen

Alle URLs am **09.11.2026** abgerufen und im Text geprüft (nicht nur Statuscode). Wo eine Seite
automatisierte Abrufe blockt, steht das dabei — der Inhalt wurde dann über den Browser bzw. das PDF
geprüft.

**[Q1] BBSR / GModG-Infoportal — „Nachträgliche Dämmpflicht bei obersten Geschossdecken".**
https://www.gmodg.bund.de/GModG/DE/GModGRegelungen/Gebaeudebestand/Nachruestungspflichten/obersteGeschossdecke/OGD-node.html
Belegt: § 35 GModG, U-Wert **0,24 W/m²K**, Pflicht unmittelbar ohne Übergangsfrist; Ausnahme für
selbstgenutzte Ein-/Zweifamilienhäuser, die am **1. Februar 2002** selbst bewohnt waren — Anforderungen
erst bei **Eigentümerwechsel, Frist zwei Jahre**; Ausnahme nach Abs. 4, wenn sich die Aufwendungen nicht
„innerhalb angemessener Frist" amortisieren. Betreiber: Bundesamt für Bauwesen und Raumordnung.

**[Q2] Verbraucherzentrale — „GModG: Was steht im Gebäudemodernisierungs-Gesetz?"**, Stand
**21. August 2026.**
https://verbraucherzentrale.de/wissen/energie/energetische-sanierung/gmodg-was-steht-im-gebaeudemodernisierungsgesetz-13886
Belegt: GModG löst GEG ab, gilt **seit 29. Juli 2026**; Pflichten bei > **10 %** Flächenänderung eines
Bauteils; U-Wert-Tabelle (Außenwand 0,24 / Fenster Uw 1,30 / Dachschräge 0,24 / oberste Geschossdecke
0,24 / Keller 0,30 / Flachdach 0,20) mit Dämmstärken; bei umfassender Modernisierung Primärenergie und
Transmissionswärmeverlust **≤ 1,4-fach** des Referenzgebäudes, Endenergie ≤ 1,5-fach; Gasheizung
stufenweise 2029: 10 % … 2045: 100 %; EH 40 = „höchstens 40 Prozent der Referenz-Primärenergie";
EH 55 im Neubau **befristet bis Ende 2026**.

**[Q3] BG BAU, Bauportal — „Novellierung der Gefahrstoffverordnung mit neuen Regeln für den Umgang mit
Asbest".** https://bauportal.bgbau.de/bauportal-12025/rund-um-die-bg-bau/novellierung-gefahrstoffverordnung-umgang-mit-asbest
Belegt: novellierte GefStoffV in Kraft **5.12.2024**; Ampel-Modell mit **> 100.000 / < 100.000 /
< 10.000 Fasern/m³**; Mitwirkungspflicht des Veranlassers; **Erkundungspflicht des Bauunternehmens**,
Kosten „gelten als besondere Leistung"; Stichtag **31. Oktober 1993**; funktionale Instandhaltung im
niedrigen/mittleren Risiko legalisiert („Schlitze in asbesthaltigem Putz … gefräst"); Überdeckungsverbot
für Asbestzementdächer (PV) und neu für Asbestzementdeckenverkleidungen und asbesthaltige Bodenbeläge.

**[Q4] KfW — Merkblatt „BEG Wohngebäude Kredit Effizienzhaus" (Produkt 261), gültig ab 24.09.2026,**
Bestellnummer 600 000 4854 (PDF).
https://www.kfw.de/PDF/Download-Center/F%C3%B6rderprogramme-(Inlandsf%C3%B6rderung)/PDF-Dokumente/6000004854_M_261.pdf
Belegt: Kredit **max. 150.000 € je Wohneinheit**; Stufen **EH Denkmal, 85, 70, 55, 40** in EE/NH;
**≥ 65 %** erneuerbare Energien; Tilgungszuschuss **5 %** (EH 55 EE), **10 %** (EH 40 EE), **5 %**
(Denkmal EE), **0 %** (70/85 EE), **+5 Pp** NH, **+10 Pp** WPB, **+15 Pp** SerSan; Bauantrag ≥ **5
Jahre**; **10 Jahre** Nutzungspflicht; Energieeffizienz-Experte zwingend und gesondert zu beauftragen;
Eigenleistung: **nur Materialkosten**; „Der Antrag ist **vor Beginn des Vorhabens** … zu stellen";
keine Kombination mit BEG-EM (3 Jahre Wartezeit), **keine Kumulierung mit § 35c EStG**; „Es besteht
kein Anspruch auf Förderung."
*(kfw.de blockt automatisierte Abrufe: Produktseiten und PDFs liefern über curl HTTP 000
(Zertifikatsfehler im Proxy); beide Merkblätter wurden über einen echten Browserabruf im Volltext
gelesen und geprüft.)*

**[Q5] KfW — Merkblatt „BEG Heizungsförderung für Privatpersonen – Wohngebäude" (Produkt 458), gültig
ab 24.09.2026** (PDF).
https://www.kfw.de/PDF/Download-Center/F%C3%B6rderprogramme-(Inlandsf%C3%B6rderung)/PDF-Dokumente/6000005131_M_458.pdf
Belegt: Grundförderung **30 %**; **Klimageschwindigkeitsbonus 16 %**, sinkt ab **01.02.2027**
halbjährlich um **4 Prozentpunkte**, **0 ab 01.08.2028**; **Einkommensbonus 40 %** bis **30.000 €**
zvE (40.000 € mit Kind); Obergrenze **70 %**, mit Einkommensbonus **80 %**; Förderhöchstbetrag
**28.000 €** für die erste Wohneinheit; Grundlage BEG-EM-Richtlinie in Kraft **21.07.2026**;
Liefer-/Leistungsvertrag mit aufschiebender Bedingung ausdrücklich vorgesehen.

**[Q6] § 35c EStG — Steuerermäßigung für energetische Maßnahmen.**
https://www.gesetze-im-internet.de/estg/__35c.html
Wörtlich geprüft: **7 % / 7 % / 6 %** in drei Jahren, Deckel **14.000 / 14.000 / 12.000 €**,
Höchstbetrag **40.000 €** je Objekt; Gebäude **älter als 10 Jahre** (Beginn der Herstellung); **acht**
abschließend gelistete Maßnahmen (Dämmung Wände/Dach/Geschossdecken, Fenster/Außentüren, Lüftung,
Heizung, digitale Systeme, Heizungsoptimierung); „von einem **Fachunternehmen** ausgeführt";
Bescheinigung nach amtlichem Muster.

**[Q7] § 6 EStG — anschaffungsnahe Herstellungskosten.**
https://www.gesetze-im-internet.de/estg/__6.html
Wörtlich geprüft: Aufwendungen für Instandsetzungs-/Modernisierungsmaßnahmen „innerhalb von **drei
Jahren** nach der Anschaffung", wenn sie „**15 Prozent** der Anschaffungskosten des Gebäudes
übersteigen", gehören zu den Herstellungskosten; ausgenommen Erweiterungen und jährlich üblich
anfallende Erhaltungsarbeiten.

**[Q8] § 7i EStG — erhöhte Absetzungen bei Baudenkmalen.**
https://www.gesetze-im-internet.de/estg/__7i.html
Wörtlich geprüft: „im Jahr der Herstellung und in den folgenden **sieben Jahren** jeweils bis zu **9
Prozent** und in den folgenden **vier Jahren** jeweils bis zu **7 Prozent**"; Bescheinigung der
zuständigen Stelle nach Abs. 2; keine Absetzung, soweit öffentliche Zuschüsse die Kosten decken.

**[Q9] § 5a GefStoffV — Mitwirkungs- und Informationspflichten des Veranlassers.**
https://www.gesetze-im-internet.de/gefstoffv_2010/__5a.html
Wörtlich geprüft: Abs. 1 Veranlasser muss **vor Beginn** alle Informationen zur **Bau- oder
Nutzungsgeschichte** über vorhandene oder vermutete Gefahrstoffe schriftlich/elektronisch übermitteln;
Abs. 2 bei Baujahr **1993–1996** Datum des Baubeginns, bei **vor 1993 oder nach 1996** genügt das
Baujahr; **Abs. 4: „Die Absätze 1 bis 3 gelten auch für private Haushalte."**

**[Q10] Verbraucherzentrale — „Handwerker: Was bei einem Auftrag zu beachten ist".**
https://verbraucherzentrale.de/wissen/vertraege-reklamation/kundenrechte/handwerker-was-bei-einem-auftrag-zu-beachten-ist-12762
Belegt: detaillierte Kostenvoranschläge mit Stundensätzen und Materialpreisen; Kostensteigerung „mehr
als 15 bis 20 Prozent" unverzüglich mitteilen; Festpreis darf nicht überschritten werden; Abnahme mit
Vorbehaltssatz; Gewährleistung 5 Jahre bei Bauwerken; „beim Öffnen der Wände besteht Ihr unvermeidliches
Kostenrisiko".

**[Q11] FOCUS online — „Ab 75 Prozent der Neubaukosten spricht vieles für Abriss"**, Tobias Beuler
(Bausachverständiger), **14.07.2026**.
https://www.focus.de/immobilien/kaufen/ab-75-prozent-der-neubaukosten-spricht-vieles-fuer-abriss_bda3502b-ebdd-471e-b420-955c8ccf35d7.html
Belegt: 75-%-Regel im Wortlaut; Neubau EH-Standard „grob **3.000 bis 4.000 Euro pro Quadratmeter**,
Grundstück nicht eingerechnet"; „echte Kernsanierung … schnell bei **1.800 bis 3.000 Euro pro
Quadratmeter**, und das sind die Zahlen vor den Überraschungen"; anschaffungsnahe Herstellungskosten
**15 % in drei Jahren**; Denkmal-AfA schlägt Neubau; Erhaltungssatzung/Milieuschutz verhindert
Abrissgenehmigung; „Die teuerste Variante ist fast immer die, bei der man mitten in der Sanierung merkt,
dass man besser abgerissen hätte."

**[Q12] Dr. Klein — „Kernsanierung: Checkliste, Ablauf, Kosten, Dauer"**, 15.06.2023.
https://www.drklein.de/kernsanierung.html
Belegt: **400–1.000 €/m²**; 120 m² = **48.000–120.000 €**; Dauer „zwischen 3 Monaten und 1 Jahr";
Kernsanierung = Rückbau bis auf tragende Strukturen.

**[Q13] musterhaus.net — „Abrisskosten: Was kostet es, ein Haus abzureißen?"**, 14.10.2025.
https://www.musterhaus.net/ratgeber/haus-abreissen-kosten
Belegt: **10.000–30.000 €** für ein Einfamilienhaus mit Entsorgung; Faustformel **50–100 €/m²**, in
der Praxis meist **50–250 €/m²**; Beispielrechnung 140 m² = **12.850 €**, Stadtvilla 200 m² mit Keller
= **26.200 €**; **300–400 m³** Bauschutt bei 140 m²; „Ein Abriss lohnt sich, wenn die Sanierung über
**2.500 €/m²** kosten würde."

**[Q14] Sparkasse Immobilien — „Kernsanierung: Kosten, Ablauf & Dauer".**
https://immobilien.sparkasse.de/modernisieren/massnahmen/kernsanieren.html
Belegt: **400–1.000 €/m²**; Zeitplan je Phase (Bestandsaufnahme 1–2 Wochen, Planung 2–4, Vergabe 3–6,
Baustelle 1, Entkernung 2–4, Dach/Fassade 3–6, TGA 4–8, Innenarbeiten 6–12, Endausbau 2–4, Abnahme
1–2); Kostenbeispiele je Gewerk; Fußnote zu den BKI-Preisen: „statistische Mittelwerte aus
ausgeschriebenen und abgerechneten Projekten", „Bei Einzelmaßnahmen und direkter Beauftragung durch den
Bauherren ist mit Preiszuschlägen und Mehrkosten zu rechnen."

**[Q15] SO Innenausbau — „Kernsanierung Dauer: Realistische Zeitpläne, Phasen & Beispiele".**
https://www.so-innenausbau.de/kernsanierung-dauer
Belegt: Phasenrichtwerte (Bestandsaufnahme 2–6 Wochen, Planung 4–12, Beschaffung 2–6, Entkernung 1–3,
Rohbau/Hülle 2–8, Haustechnik 3–8, Innenausbau 4–12, Abnahme 1–2); **120 m² Einfamilienhaus: 6–9
Monate plus 20–25 % Puffer**; 60 m² Wohnung 4–6 Monate plus 15–20 %; „Zugang, Ruhezeiten,
Baustellenlogistik und **Bewohnung** bremsen Abläufe"; „15–25 % Zeitpuffer für Befunde".
*Interessenkonflikt: Der Anbieter wirbt auf derselben Seite für Generalunternehmer-Vergabe — die
Phasenzahlen sind brauchbar, die Empfehlung ist Verkauf.*

**[Q16] BauNetz Wissen — „Baualtersstufe: Bauten der 1960er-Jahre".**
https://baunetzwissen.de/bauen-im-bestand/fachwissen/baualtersstufen/baualtersstufe-bauten-der-1960er-jahre-148200
Belegt: Übergang vom traditionellen Massivbau zum industriellen Bauen; Stahlbeton, Aluminium,
großformatige Verglasungen „meist noch nicht über Wärmeschutzverglasung"; Zentralheizung „nahezu
flächendeckend"; „Anforderungen an den Wärmeschutz spielten dagegen noch eine untergeordnete Rolle";
im Wohnungsbau verputzte Mauerwerksfassaden und Betonfertigteile.

**[Q17] justhome — „Sanierungskosten pro qm: Alle Gewerke"**, Stand **Mai 2026**.
https://justhome.com/learning-center/article/sanierungskosten-pro-qm
Belegt: Kernsanierung **500–1.500 €/m²**; Gewerketabelle (Dachdämmung 30–80 €/m² Dachfläche,
Dacheindeckung 50–120, WDVS 80–200 €/m² Fassade, Fenster 400–1.500 €/Stück, Heizung 8.000–25.000 €,
Bad 400–1.200 €/m², Keller 50–200 €/m², Elektro 50–120 €/m² WF, Laminat 15–40, Parkett 60–150);
Keller-Außenabdichtung **300–600 €/m²**; Ballungsraum-Zuschlag **20–30 %**.

**[Q18] CHECK24 — „Kosten für Kernsanierung eines Hauses pro m²".**
https://www.check24.de/wohngebaeudeversicherung/kosten-kernsanierung/
Belegt: **600–1.000 €/m²**; Beispieltabelle je Maßnahme (Dach 80–300 €/m², Dachstuhl 50–150 €/m²,
Fassadendämmung 60–500 €/m², Kellerdecke 30–100 €/m², Elektro 110–170 €/m², Fenster 650–1.000 €/Stück,
Heizung 9.000–35.000 €, Sanitäranlage 1.000–3.500 €/m², Rohrleitung 200–300 €/m², Lüftung mit WRG
6.000–9.000 €); ausdrücklicher Hinweis: „Es handelt sich hierbei nicht um verbindliche Angaben, sondern
um Schätzungen."

**[Q19] Bauexpertenforum — Thread „Kosten Kernsanierung"**, ab 27.05.2024.
https://www.bauexpertenforum.de/threads/kosten-kernsanierung.137840/
Belegt: Ausgangsfrage, warum überall „400–1000 € pro qm" stehe, während ein Architekt für 150 m²
**420.000 €** veranschlagt (= **2.800 €/m²**); Antwort eines Vielposters: bei allen Gewerken „kommen
eben Preise irgendwo zwischen **2.500 und 3.500 €** bei raus. Also ungefähr das, was dein Architekt
gerechnet hat"; ein weiterer Beitrag: Kernsanierung bis KfW-55-Niveau „tatsächlich nicht viel günstiger,
als der Neubau". *Forum = Erfahrungswerte, keine Statistik.*

**[Q20] Umweltbundesamt — Asbest** (Stand 30.07.2024).
https://www.umweltbundesamt.de/themen/gesundheit/umwelteinfluesse-auf-den-menschen/chemische-stoffe/asbest
Belegt: Verbot seit **31.10.1993**; Bitumenkleber können asbesthaltig sein; Nachtspeicheröfen können
schwach gebundenen Asbest enthalten; Rückbau als ASI-Arbeit mit Anzeige.

**[Q21] Dr. Klein — „Hausbau mit Generalunternehmer: Die Vor- und Nachteile".**
https://www.drklein.de/generalunternehmer.html
Belegt: Abgrenzung GU / Bauträger / Einzelvergabe; beim Bauträger „dürfen Sie keine direkten Weisungen
an die Handwerker geben", „Bauherr ist hier der Bauträger"; Nachteile des GU: kein Mitbestimmungsrecht
bei den Gewerken, keine Weisung an Handwerker, Insolvenzrisiko; **Vertragserfüllungsbürgschaft
mindestens 5 %, besser 10 %**; Vorauszahlungssicherheit.

**[Q22] handwerk.com (Deutscher Handwerkskammertag) — „Abnahmeprotokoll: Das sind die 3 größten
Stolperfallen"**, aktualisiert 08.09.2026.
https://handwerk.com/recht/abnahmeprotokoll-das-sind-die-3-groessten-stolperfallen
Belegt (Fachanwalt Florian Herbst): „Der Auftraggeber muss unterschreiben, sonst kommt die Abnahme nicht
zustande"; Architekt braucht schriftliche Vollmacht, Bauleiter Prokura, sonst ist das Protokoll „im
Streitfall nichts wert"; im Abnahmeprotokoll geänderte Gewährleistungsfristen sind **bindend**, auch
wenn länger als im Bauvertrag.

**[Q23] YouTube — „FEHLER BEIM RENOVIEREN – Das würde ich nie wieder machen"**, Kanal Johannes /
Flipper Immo, 16:09, 19.01.2025. https://www.youtube.com/watch?v=k3q49IW19KU
Aus den Untertiteln (Transkript `references/transkripte/k3q49IW19KU.txt`, geprüft 09.11.2026):
**00:00:50** „Baustellen sind einfach Baustellen und es dauert in der Regel auch einfach immer ungefähr
doppelt so lange als geplant"; **00:11:35** „dafür ist normalerweise so ein 15prozentiger Puffer ganz
gut". *Praktiker-Aussage eines Flippers, keine Statistik.*

**[Q24] YouTube — „Unsere Haussanierung: 12 Fehler, die ich bereue"**, Kanal Spiel und Zeug, 17:55,
30.05.2026. https://www.youtube.com/watch?v=sWXyiNADbFk
Aus den Untertiteln (Transkript `references/transkripte/sWXyiNADbFk.txt`): **00:03:52** „wegen unserer
Baustelle [wird] um unser Haus permanent Dreck reingeschleppt"; **00:06:05** die „Ausbaureserve" in der
Elektroverteilung war „mehr oder weniger aufgebraucht", obwohl noch Arbeiten anstanden; **00:15:03**
Fenstersensoren mit „relativ hohe[r] Ausfallquote im ersten Jahr".

**[Q25] BGB § 632a (Abschlagszahlungen), § 641 (Fälligkeit), § 650b (Vertragsänderung), § 650c
(Vergütungsanpassung).** https://www.gesetze-im-internet.de/bgb/__632a.html ·
https://www.gesetze-im-internet.de/bgb/__641.html · https://www.gesetze-im-internet.de/bgb/__650b.html ·
https://www.gesetze-im-internet.de/bgb/__650c.html
Geprüft (Volltext in `kosten-bauzeit.md` zitiert): Abschlag „in Höhe des Wertes der … erbrachten
Leistungen"; Vergütung bei Abnahme fällig; Zurückbehaltung „in der Regel das Doppelte" der
Mängelbeseitigungskosten; § 650b Abs. 1 Angebot über Mehr-/Mindervergütung; § 650c Abs. 1 tatsächlich
erforderliche Kosten mit Zuschlägen, Abs. 3 80 % in Abschlägen.

**[Q26] BGB § 640 (Abnahme), § 634a (Verjährung).**
https://www.gesetze-im-internet.de/bgb/__640.html · https://www.gesetze-im-internet.de/bgb/__634a.html
Geprüft: Abnahmepflicht, „Wegen unwesentlicher Mängel kann die Abnahme nicht verweigert werden"
(Abs. 1); fiktive Abnahme nur mit Hinweis in Textform (Abs. 2); bekannte Mängel nur mit Vorbehalt
(Abs. 3); Verjährung **5 Jahre** bei Bauwerk, Beginn mit Abnahme.

**[Q27] VOB/B § 13 (Mängelansprüche), § 2 (Vergütung), § 16 (Zahlung), § 17 (Sicherheit)** —
VOB/B 2016, über lxgesetze.de geprüft: https://lxgesetze.de/vob-b-2016/13
**VOB/B ist kein Gesetz**, sondern Vertragsbestandteil; sie gilt nur, wenn wirksam einbezogen. 4 Jahre
Verjährung bei Bauwerken (§ 13 Abs. 4); § 2 Abs. 5/6 Ankündigung vor Ausführung; § 16 Abs. 3 Nr. 2
vorbehaltlose Schlusszahlung; § 17 Einbehalt max. 10 %.

**[Q28] BG BAU — Umsetzungshilfe zur TRGS 551 „Teer und andere Pyrolyseprodukte aus organischem
Material", Nr. 5 Schutzmaßnahmen.**
https://www.bgbau-medien.de/handlungshilfen_gb/daten/tr/trgs551/5.htm
Belegt: TRGS 551 regelt Tätigkeiten mit Pyrolyseprodukten (Teer/PAK); Rangfolge der Schutzmaßnahmen nach
STOP-Prinzip, branchenübergreifende und spezielle Schutzmaßnahmen. *Die TRGS 551 selbst liegt bei der
BAuA (baua.de blockt automatisierte Abrufe: HTTP 403) — zitiert ist die Umsetzungshilfe der BG BAU.*

**[Q29] DGUV — TRGS 521 „Abbruch-, Sanierungs- und Instandhaltungsarbeiten mit alter Mineralwolle"**
(PDF). https://dguv.de/medien/fb-bildungseinrichtungen/fb_bildung_neu/pikto-nicht-freigegeben/trgs-521-1.pdf
Belegt: „Bei Mineralwolle die vor **1996** eingebaute wurde, ist davon auszugehen, dass es sich um alte
Mineralwolle im Sinne dieser TRGS handelt"; seit **Juni 2000** Herstellungs- und Verwendungsverbot nach
Anhang IV Nr. 22 GefStoffV; seit 1996 hergestellte Mineralwollen gelten als nicht biopersistent.

---

## 12. Unbelegt / offen (bitte nicht als Tatsache weitergeben)

1. **Alle Mengen im Rechenbeispiel** (Dachfläche 95 m², Fassade 170 m², 12 Fenster, 13 m² Bad,
   100 m² Kellerwand) sind **[Setzung]**. Sie ersetzen kein Aufmaß. Ein Aufmaß kann das Ergebnis um
   20–30 % verschieben — in beide Richtungen.
2. **Der Planwert 2.080 €/m² (270.000 €)** ist eine gewichtete Setzung zwischen gerechnetem Mittel
   (1.307 €/m²) und Marktband (1.800–3.000 €/m²). Es gibt **keine** Statistik, die für „130 m², Baujahr
   1965, Kernsanierung" einen belastbaren Mittelwert liefert. Die belegten Anker stehen in 8.2–8.4.
3. **Die Erklärung für die Lücke zwischen 400–1.000 und 1.800–3.000 €/m²** (Sanierungstiefe,
   Bestandszuschläge, fehlende Nebenkosten) ist meine Interpretation **[Setzung]**. Belegt ist nur, dass
   die Lücke existiert — und dass ein Praktiker sie mit „2.500 bis 3.500 €" beziffert [Q19].
4. **„Bewohnt sanieren dauert doppelt so lange"** stammt aus einem YouTube-Video eines Flippers
   [Q23, 00:00:50], nicht aus einer Studie. Belegt ist außerdem, dass Bewohnung Abläufe bremst [Q15].
   Eine Prozentzahl gibt es nicht.
5. **Pufferhöhen** (10–15 % Kosten, 20–25 % Zeit) sind Erfahrungswerte. Der einzige belegte Pufferwert
   ist der des Sanierungsanbieters (20–25 % für 120 m²) [Q15] und die Praktiker-Angabe „15 Prozent"
   [Q23]. Die 15–20 % aus der Verbraucherzentrale [Q10] sind eine **rechtliche Meldeschwelle** beim
   Kostenvoranschlag, kein Pufferwert.
6. **Kostenanteile je Gewerk** (Abschnitt 4.2) sind aus den Mittelwerten der Einzelbänder gerechnet
   **[Rechnung]**, nicht aus einer Projektstatistik. Sie sagen, wo das Geld relativ hingeht, nicht, was
   dein Haus kostet.
7. **Mietkosten im Vergleich „ausziehen vs. bleiben"** (10–14 €/m² kalt) sind **[Setzung]** ohne
   Quellenprüfung; regionale Mietspiegel sind dafür die richtige Quelle, nicht dieses Playbook.
8. **Barrierefreiheit** wird hier nur als Zeitpunkt behandelt (vor Estrich). Normmaße (DIN 18040),
   Förderdetails und Konstruktionen stehen **nicht** in diesem Playbook; KfW 455-B ist derzeit nicht
   beantragbar [Zitat aus `kosten-bauzeit.md`, dort geprüft].
9. **KfW-Konditionen und Zinssätze ändern sich.** Alle Zahlen [Q4][Q5] sind Stand **09.11.2026**
   (Merkblätter gültig ab 24.09.2026). Vor jeder Finanzierung tagesaktuell prüfen.
10. **Die 75-%-Regel ist eine Faustregel eines Sachverständigen** [Q11], keine Norm und keine
    betriebswirtschaftliche Methode. Sie ist brauchbar als Gesprächsgrundlage mit dem Gutachter, nicht
    als alleinige Entscheidung.
11. **Nicht geprüft, weil nicht vorhanden:** eine belastbare Statistik „Sanierungsquote 2025/2026" des
    BBSR, die man als Kontext zitieren könnte. Die gefundenen Meldungen zur Sanierungsquote stammen von
    Verbänden, nicht vom BBSR; sie sind hier deshalb **nicht** verwendet.
12. **§ 7i und § 35c gleichzeitig** ist steuerlich nicht in diesem Playbook geklärt. Beide setzen voraus,
    dass keine öffentlichen Zuschüsse die Kosten decken [Q6][Q8]; die Kombination gehört zum
    Steuerberater, nicht in ein Bau-Playbook.