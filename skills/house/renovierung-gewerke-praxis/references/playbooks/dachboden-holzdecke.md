# Playbook: Dachboden ausbauen & Holzbalkendecke

Stand: 09.11.2026 · Zielgruppe: Eigenheimbesitzer · Alle Preise brutto, alle Maße in mm, wenn nicht anders
angegeben. Quellen sind mit `[Q1]`…`[Q30]` nummeriert und am Ende mit URL und HTTP-Status geprüft.

## 0. Kurzantwort

**Dachboden ausbauen ist kein Trockenbau-Projekt, sondern zuerst ein Bauamts- und Statik-Projekt.** Drei
Dinge entscheiden, ob es überhaupt Wohnraum wird: **Nutzungsänderung** (fast immer genehmigungspflichtig),
**lichte Höhe** (Bayern z. B. 2,40 m, im Dachgeschoss 2,20 m über der Hälfte der Nutzfläche) und **zweiter
Rettungsweg** (die Einschubtreppe zum Lagerboden ist dann keine zulässige Treppe mehr). Erst danach kommt
Dämmung — und die braucht eine durchgehende Luftdichtheitsschicht, sonst dämmst du Wasser ein.

**Holzbalkendecke:** Trittschall und Schwingung löst man nicht mit Gewicht. Ein Einschub von 0 auf
120 kg/m² bringt nach Messungen am ift Rosenheim **maximal 3 dB** Trittschallverbesserung, zwischen 80 und
120 kg/m² praktisch nichts mehr [Q8]. Was hilft: entkoppelte Metallunterkonstruktion, mehr Beplankungslagen,
möglichst wenige Verbindungspunkte zur Rohdecke [Q8].

**Sichtbare Balken** strahlen kostet 25–80 €/m² Holz [Q17]; **Decke abhängen** 40–70 €/m² [Q7];
**Dachboden komplett ausbauen** 500–2.000 €/m² [Q6]. Eigenleistung ist bei Rückbau, Dämmung, Beplankung und
Anstrich realistisch — nicht bei Statik, Dampfbremse im Steildach, Elektro und Schädlingsbekämpfung.

## 1. Grenze zum Dämm-Playbook (`daemmung.md`)

Dieses Playbook behandelt **nur die Dachboden-spezifische Kopplung**: Nutzung ↔ Baurecht ↔ Höhe ↔
Dampfbremse ↔ Deckenaufbau. Die Dämmstoffwahl, U-Werte, Tauwasserberechnung, Förderung und Fassadendämmung
stehen in `daemmung.md` und werden hier nicht wiederholt.

Die eine Regel, die hierher gehört: **Dämmung ist die halbe Sache, Luftdichtheit die andere Hälfte.** Knauf
formuliert es für den Dachgeschossausbau so: Die Dampfbremse ist gleichzeitig die Luftdichtheitsschicht und
muss an den Folienüberlappungen **und** an den anschließenden Bauteilen dicht sein; sonst gelangt warme,
feuchte Raumluft in die Konstruktion, kühlt ab und bildet Tauwasser — kritisch sind Durchdringungen wie
Steckdoseneinbauten [Q9].

## 2. Baurecht zuerst: Nutzung, Höhe, Rettungsweg, Rauchmelder

### 2.1 Nutzungsänderung — der häufigste teure Irrtum

- **Rechtslage:** „Die Errichtung, Änderung und **Nutzungsänderung** von Anlagen bedürfen der Baugenehmigung,
  soweit in den §§ 60 bis 62, 76 und 77 nichts anderes bestimmt ist." — Musterbauordnung (MBO), Fassung
  November 2002, zuletzt geändert 22.02.2019, **§ 59 Abs. 1** [Q1].
- **Praxis:** Wer einen bisher ungenutzten Dachboden zu Wohnraum umbaut, löst in den meisten Fällen eine
  Nutzungsänderung aus; ob eine Genehmigung nötig ist, hängt von Landesbauordnung und Umfang ab, und bei
  einer eigenständigen Wohnung ist sie es praktisch immer [Q10].
- **Kosten der Genehmigung:** 200–1.500 € je nach Umfang und Bundesland [Q6] (im Fließtext desselben Artikels
  stehen 200–1.000 € — die Tabelle ist die aktuellere Angabe). Das ist die billigste Position
  im ganzen Projekt — und die, die man am ehesten „spart" und später teuer nachzahlt.

**Bestandsschutz-Erleichterung, die man kennen muss (Beispiel Bayern):** Sollen Nutzungseinheiten mit
Aufenthaltsräumen in bestandsgeschützten Gebäuden in Wohnraum umgewandelt werden, „sind auf bestehende
Bauteile Art. 6, 25, 26, 28, 29 und 30 nicht anzuwenden" — BayBO **Art. 46 Abs. 5** [Q3]. Heißt im Klartext:
Der Bestand wird nicht auf Neubau-Niveau hochgerüstet (die Liste umfasst u. a. Abstandsflächen, Brandverhalten
tragender Bauteile, Trennwände, Brandwände und Decken). Das ist **Landesrecht**, nicht
Bundesrecht — die Nummern und der Umfang der Erleichterung sind in jedem Bundesland anders. Deshalb: erst
Landesbauordnung lesen, dann Bauamt anrufen, dann planen.

### 2.2 Höhe — die Zahl, die über „Wohnraum" entscheidet

| Regel | Inhalt | Quelle |
|---|---|---|
| MBO § 47 Abs. 1 | Aufenthaltsräume **2,40 m** lichte Höhe; **gilt nicht** für Aufenthaltsräume im Dachraum | [Q1] |
| BayBO Art. 45 Abs. 1 | **2,40 m**, im Dachgeschoss **2,20 m über der Hälfte der Nutzfläche**; Raumteile unter **1,50 m** bleiben außer Betracht; gilt nicht für Gebäudeklassen 1 und 2 | [Q2] |
| MBO § 47 Abs. 2 | Fensterfläche ≥ **1/8** der Netto-Grundfläche (Tageslicht) | [Q1] |

Zwei Konsequenzen für die Planung:

1. **Die MBO selbst nennt für den Dachraum keine Mindesthöhe** — die Zahl steht in der Landesbauordnung.
   In Bayern ist es die Hälfte der Nutzfläche, in anderen Ländern wird von „zwei Dritteln" gesprochen; ein
   Forumsteilnehmer nennt für seinen Fall „mind. 2,3 m über der Hälfte der Grundfläche mit h > 1,5 m" [Q14].
   **Nicht aus dem Gedächtnis antworten — die eigene Landesbauordnung gilt.**
2. **Die Höhe wird beim Ausbau kleiner, nicht größer.** Auf die Sparren kommt mindestens Unterkonstruktion
   plus Verkleidung, und der Boden braucht eventuell Schüttung zum Ausgleichen — HORNBACH empfiehlt, sich
   vorher einen **Meterriss** im Dach zu setzen (Oberkante Fertigfußboden + 1,00 m) und von dort alle
   Installationen zu planen [Q23].

### 2.3 Rettungswege und Treppe — hier scheitern die meisten Ausbauten

- **Zwei Rettungswege:** Für Nutzungseinheiten mit mindestens einem Aufenthaltsraum müssen in jedem Geschoss
  **zwei voneinander unabhängige Rettungswege** ins Freie vorhanden sein; der **erste** führt über eine
  **notwendige Treppe**, der **zweite** kann eine weitere notwendige Treppe oder eine mit Rettungsgeräten
  der Feuerwehr erreichbare Stelle sein. Liegt die Brüstung eines Anleiterfensters über **8 m** über Gelände,
  braucht die Feuerwehr Hubrettungsfahrzeuge — MBO **§ 33** [Q1], inhaltsgleich BayBO **Art. 31** [Q4].
- **Der Dachraum braucht eine Treppe:** Jedes nicht zu ebener Erde liegende Geschoss **und der benutzbare
  Dachraum** müssen über mindestens eine Treppe zugänglich sein (notwendige Treppe); **einschiebbare Treppen
  und Leitern** sind als notwendige Treppe unzulässig und in Gebäudeklassen 1 und 2 nur als Zugang zu einem
  **Dachraum ohne Aufenthaltsraum** zulässig — MBO **§ 34 Abs. 1 und 2** [Q1].
- **Damit ist die Bodentreppe erledigt, sobald „Wohnraum" draufsteht.** Sie bleibt zulässig für den reinen
  Lagerboden. Der Unterschied ist keine Formalie, sondern der Unterschied zwischen „Nutzung wie bisher" und
  „Aufenthaltsraum".
- **Treppenmaße (DIN 18065:2020-08):** notwendige Treppe **100 cm** nutzbare Laufbreite, Steigung
  **140–190 mm**, Auftritt **260–370 mm**; in Wohngebäuden mit bis zu zwei Wohnungen und innerhalb von
  Wohnungen **80 cm**, Steigung **140–200 mm**, Auftritt **230–370 mm**; Steigungsverhältnis nach
  Schrittmaßregel **2s + a = 59–65 cm** [Q5]. Ein Istmaß darf vom Sollmaß um nicht mehr als 5 mm abweichen
  (Ausnahme Wohngebäude) [Q5].
- **Fenster als zweiter Rettungsweg:** HORNBACH nennt als übliche Mindestgröße **90 × 120 cm** und verweist
  für die Brüstungshöhe auf die jeweilige Landesbauordnung [Q23]. Das ist eine Praxisangabe aus einem
  Hersteller-Video, keine Normzahl — die verbindliche Größe steht in der LBO.

### 2.4 Rauchmelder

In Wohnungen müssen **Schlafräume und Kinderzimmer sowie Flure, die zu Aufenthaltsräumen führen**, jeweils
mindestens einen Rauchwarnmelder haben; Einbau und Betrieb müssen Brandrauch frühzeitig erkennen und melden —
BayBO **Art. 46 Abs. 4** [Q3]. Wird der Dachboden zum Schlaf- oder Kinderzimmer, gehört er dazu. Für den
Lagerboden gilt die Pflicht nicht. Die Details (wer einbaut, welche Bauart, Übertragung auf Dritte) sind
Landesrecht und stehen in der jeweiligen LBO.

### 2.5 Was der Dachboden baurechtlich sonst noch braucht

- **Tageslicht:** Fensterfläche mindestens **1/8** der Netto-Grundfläche [Q1][Q2]. Ein Lagerboden mit einer
  Dachluke erfüllt das nicht.
- **Dachneigung als Realitätscheck:** HORNBACH nennt **mindestens 35°** als Voraussetzung dafür, dass die
  Deckenhöhe überhaupt reicht; über 50° sei sogar zweigeschossiger Ausbau möglich [Q23]. Erfahrungswert aus
  der Praxis, keine Norm — aber ein guter erster Filter, bevor man Geld in die Planung steckt.
- **Nutzung festlegen:** Flur, Schlafzimmer, Wohnraum oder Nassbereich — bei einem Bad kommen Wasserzu- und
  -ableitung und damit ein anderes Gewerk dazu [Q23].

## 3. Ablauf in Tagen (Reihenfolge, die kein Geld zweimal kostet)

| Tag | Schritt | Kontrolle |
|---|---|---|
| 1 | Bestandsaufnahme: Grundfläche, Höhe bis geplante Decke, Sparrenabstand/-tiefe, Fenster, Balkenquerschnitte, Feuchte | Meterriss setzen [Q23]; Fotos mit Maßband |
| 2 | Bauamt/LBO: Nutzungsänderung, Höhe, Rettungsweg, Rauchmelder klären | schriftliche Auskunft oder Aktenvermerk |
| 3 | Statik: Deckenlast, Balkenquerschnitte, Auflager, Schwingung | Tragwerksplaner, nicht Zimmermann nach Gefühl [Q13][Q18] |
| 4–6 | Rückbau: alte Dämmung, Einschub, Schüttung raus; Schadstoffe prüfen (Asbest bei Baubeginn vor 31.10.1993) | siehe `werkzeug-sicherheit.md` |
| 7–9 | Rohinstallation: Elektro, ggf. Sanitär/Lüftung — **vor** Dämmung und Beplankung [Q9] | Leitungen dokumentiert, Dampfbremse noch nicht verletzt |
| 10–12 | Dämmung + Dampfbremse/Luftdichtheit, Anschlüsse und Durchdringungen | Klebungen vollständig, Fotos |
| 13–16 | Unterkonstruktion + Beplankung (Schräge/Decke) | Schraubenabstände, Fugenbild |
| 17–19 | Spachteln, Q2/Q3, Schleifen | Staubabsaugung |
| 20–22 | Bodenaufbau, Trittschalldämmung, Belag | Höhenlage zum Meterriss |
| 23–24 | Treppe, Geländer, Rauchmelder, Elektro-Fertiginstallation | Rettungsweg begehbar, Treppenmaße geprüft |
| 25 | Abnahme, Fotos, Protokolle | Mängelliste, Fristen |

Die Reihenfolge ist nicht Geschmack: Kabel nach der Dampfbremse heißt Folie durchstoßen, Estrich nach Türen
heißt Türen kürzen, Beplankung vor Elektro heißt aufstemmen. HORNBACH nennt dieselbe Logik: erst Dachfenster,
dann Dämmung, dann Trennwände, zuletzt Boden [Q23].

## 4. Dämmung und Dampfbremse im Dachraum

### 4.1 Die drei Fälle, die man auseinanderhalten muss

1. **Schrägdach wird mit ausgebaut (Aufenthaltsraum unter der Schräge):** Dampfbremse unterhalb der Dämmung,
   umlaufend luftdicht, Anschluss an Kehlbalken, Fußpfette, Wand und Fenster [Q9].
2. **Obere Geschossdecke wird gedämmt, Dachraum bleibt kalt (Kaltdach):** Die Luftdichtheitsschicht liegt
   zwischen beheiztem Raum und Dämmung. Hier ist die Dampfbremse besonders wichtig, weil das Temperaturgefälle
   groß ist [Q24].
3. **Dachraum ist beheizt und das Steildach schon gedämmt:** Dann kann die Dampfbremse in der Geschossdecke
   **entfallen** — aber nur, wenn das Temperaturgefälle klein bleibt und die Decke dampfoffen nach oben ist.
   Im Beispiel: 18 °C unten, 12 °C oben, Differenz 6 K, keine Kondensation zu erwarten [Q24].

### 4.2 Der Fehler, der in Fall 3 lauert: zwei Dampfbremsen

Wenn oben auf der Geschossdecke **OSB-Platten** liegen (dampfdicht) und unten Gipskarton (dampfoffen), dann
wandert die Feuchte durch die Decke und wird unter dem OSB eingeschlossen — „das wäre dann auf jeden Fall ein
Feuchtigkeitsproblem" [Q24]. Gleiche Falle: Folie in den Gefachen, aber am Wandbalken nicht anschließbar;
luftdicht „von oben" ist nach Einschätzung im Reddit-Thread realistisch nicht machbar [Q26].

**Regel:** Eine Dampfbremse, ein durchgehendes Bauteil, alle Anschlüsse geklebt. Zwei Dampfbremsen übereinander
sind keine Sicherheit, sondern eine Feuchtefalle.

### 4.3 Durchdringungen

Steckdosen, Kabel, Leuchten, Rauchmelder, Antennen: Jede Durchdringung der Luftdichtheitsschicht ist eine
Leckstelle [Q9]. Deshalb Installationsebene: Dampfbremse **zwischen** zwei Dämmebenen, Leitungen darüber —
dann braucht man die Folie für Steckdosen nicht zu durchstoßen [Q25].

### 4.4 Dampfbremse vs. Dampfsperre

Die Begriffe werden synonym benutzt, sind es aber nicht: „Dampfbremse" ist diffusionsbremsend (variabler
sd-Wert), „Dampfsperre" nahezu diffusionsdicht. Welcher Wert zulässig ist, ergibt sich aus dem
Tauwasser-Nachweis nach **DIN 4108-3:2024-03** (Feuchteschutz) für den konkreten Aufbau — nicht aus dem
Datenblatt allein. Die Norm ist kostenpflichtig; Nummer und Ausgabe sind belegt, der Inhalt nicht zitiert.

## 5. Holzbalkendecke verstehen

### 5.1 Aufbau

Eine klassische Holzbalkendecke besteht von oben nach unten aus: Dielenboden (quer zu den Balken), Balkenlage,
Füllung/Einschub, Untersicht (oft sichtbare Balken, früher mit Hohlkehlen oder Schnitzwerk) [Q19].

- **Blindboden / Fehlboden / Einschub:** Die Füllmaterialien liegen auf einem Blind- oder Fehlboden auf;
  wird der Fehlboden zwischen den Brettern eingebracht, heißt er **Einschub**. Traditionell Strohlehmwickel,
  heute kurze Holz-/Schwartenbretter („Einschieblinge") [Q19].
- **Füllung:** Hochofenschlacke, Sand/Brennsand, Lehm, Perlite, Vermiculite, Blähton, Zelluloseflocken,
  Holzfasern; auch Gipsdielen, Tonhohlplatten (Hourdis), Betonplatten oder Gipskartonreste als Beschwerung
  [Q19].
- **Warum überhaupt Füllung?** Wikipedia begründet sie mit Schwingungsdämpfung und Trittschall: „Zur Dämpfung
  der Schwingungen des Trittschalls muss die Decke beschwert werden" [Q19].

**Widerspruch, der stehen bleibt:** Diese Begründung ist baupraktisch richtig für alte Decken, wird aber von
den Messungen in [Q8] relativiert — der Einschub bringt höchstens 3 dB Trittschall, und oberhalb von
80 kg/m² fast nichts mehr. Beides gilt: Masse dämpft ein Stück weit, aber sie ist kein Ersatz für Entkopplung.
Wer nur Schüttung nachfüllt, gibt Geld für 1–2 dB aus.

### 5.2 Schwingung — die Decke, die „lebt"

Das WTA-Merkblatt **8-13-13/D** „Ertüchtigung von Holzbalkendecken nach WTA I: Schwingungen, Durchbiegungen,
Tragfähigkeit" ist die Referenz für den Bestand [Q18]. Kernaussagen:

- Schwingungen werden von Nutzern deutlich wahrgenommen; klirrende Gläser im Schrank oder ein als unangenehm
  empfundenes Schwingen können Hinweise auf **nicht ausreichende Tragfähigkeit, zu große Verformungen oder ein
  ungünstiges dynamisches Verhalten** sein [Q18].
- Das Schwingungsverhalten hängt von **Stützweite, Steifigkeit und Masse** der Decke ab [Q18].
- Bei Umnutzung oder wesentlichen Änderungen werden **neue Standsicherheitsnachweise** erforderlich; die
  Gebrauchstauglichkeitskriterien **Durchbiegung und Schwingung** müssen mit dem Auftraggeber vereinbart und
  **schriftlich fixiert** werden [Q18].
- Der Bestand erreicht häufig nicht die Eigenschaften eines Neubaus; Ziel ist eine substanzschonende
  Ertüchtigung, keine Neubau-Decke [Q18].

**Praxisfall (Forum, 2023):** Decke EG/OG, Baujahr 1956, Balken 20 cm hoch, 8,5 m lang, mittig auf einer Wand,
Spannweite also ca. 4 m je Feld, Balkenabstand 55–65 cm; die Decke schwingt beim normalen Gehen deutlich.
Nach Ausbau der Schlacke wurde es etwas besser. Der Fragesteller will mit seitlich angeschraubten Latten
6 × 10 cm und 22 mm OSB „versteifen" [Q15]. Was daran falsch ist, steht im selben Thread: Masse kann man
nicht „wegdiskutieren", und ein Querschnitt „20 cm" ohne Breite sagt nichts [Q15]. Der richtige Weg ist der
Tragwerksnachweis, nicht der Bauchladen.

**Vergleichsfall aus den USA (r/Carpentry):** 2x4-Sparrenpfetten, die gleichzeitig als Deckenbalken dienen,
24 Zoll (61 cm) Achsabstand, 20 Fuß (6,10 m) Spannweite — im Thread als klar unterdimensioniert bewertet
(„2x4's 24 Zoll OC can only span 13 Fuß"), Lösung nur über Unterzug oder Ingenieur [Q27]. Das ist kein deutsches
Recht, zeigt aber die Größenordnung: **Spannweite und Querschnitt gehören zusammen, und beides ist nicht
schätzbar.**

**Was tatsächlich gegen Schwingung hilft** (in dieser Reihenfolge prüfen):

1. **Auflager und Verbindungen** prüfen (Balkenköpfe, Mauerwerk, Verankerung) — locker ist schlimmer als dünn.
2. **Steifigkeit erhöhen**, nicht nur Gewicht: Querschnitt, Nebenträger/Unterzug, Verbund (z. B. Aufdopplung
   mit Verschraubung/Verklebung) — statisch nachweisen lassen [Q13][Q18].
3. **Entkoppelte Unterdecke** mit möglichst wenigen Verbindungspunkten zur Rohdecke; freitragende Unterdecke
   als beste Variante [Q8].
4. **Erst dann** Masse/Beplankungslagen — als Schall-, nicht als Schwingungsmaßnahme [Q8].

### 5.3 Trittschall: die Zahlen, die zählen

Anforderungen für Wohnungstrenndecken nach **DIN 4109-1:2018-01** (Mindestwerte) und **DIN 4109-5:2020-08**
(erhöhter Schallschutz), zitiert nach der Übersichtstabelle bei Rigips [Q8][Q30]:

| Bauteil | R'w min | L'n,w max | erhöht R'w | erhöht L'n,w |
|---|---|---|---|---|
| Wohnungstrenndecken | ≥ 54 dB | ≤ 50 dB* | ≥ 57 dB | ≤ 45 dB |

\* Bei Neubau mit Deckenkonstruktionen nach **DIN 4109-33:2016-07** (Holz-, Leicht- und Trockenbau) liegt die
Anforderung bei **L'n,w ≤ 53 dB** [Q8].

*Anmerkung zur Ausgabe:* Rigips nennt im Fließtext die DIN 4109-1:2016-07, in der Tabelle 2018-01. Gültig ist
die **2018-01** (so auch in `references/quellen.md` geführt).

**Realitätscheck Altbau:** Für eine Referenzdecke in Altbauweise nennt Rigips **L'n,w = 74 dB** ohne
Ertüchtigung — also rund 20 dB über der Anforderung. Das ist der Grund, warum „Decke abhängen" im Altbau
mehr ist als Optik [Q8].

**Was wie viel bringt** (Messungen ift Rosenheim, zitiert bei Rigips) [Q8]:

- Austausch Holz- gegen **schallentkoppelte Metallunterkonstruktion**: deutliche Verbesserung.
- **Zusätzliche Beplankungslagen** (Masse der Unterdecke): deutliche Verbesserung.
- **So wenige Verbindungspunkte wie möglich** bzw. **freitragende Unterdecke**: deutliche Verbesserung.
- **Einschub** von 0 auf 20/80/120 kg/m²: L'n,w 74 → 72 → 71 → 71 dB, also **maximal 3 dB**, zwischen 80 und
  120 kg/m² nur noch marginal; Luftschall bis **7 dB** Verbesserung [Q8].

### 5.4 Decke abhängen — und was man dabei nicht durchbohrt

**Aufbau unter einer Holzbalkendecke, der funktioniert:**

- **Variante 1 (direkt):** UD-Profil oder Konterlattung quer unter die Balken, darauf CD-Profile im Abstand
  ≤ 50 cm, darauf 12,5 mm Gipsplatten [Q12].
- **Variante 2 (entkoppelt):** Direktabhänger mit entkoppelter Aufnahme oder freitragende Unterkonstruktion —
  schalltechnisch die bessere Variante [Q8].
- **Beplankung:** Schraubenabstände nach Hersteller; Knauf nennt für Dachschrägen **< 25 cm**, für Decken
  **< 17 cm** [Q9].

**Die Praxisnummer aus dem Forum:** 9,5 mm Platten auf 70 cm Lattenabstand sind „schon sehr sportlich, außer
man mag nach unten ragendes Tonnengewölbe"; die Empfehlung des Trockenbaumeisters: seitlich UD 27/28
verschrauben, dazwischen im Abstand von **max. 50 cm** ein CD-Profil (oder Dachlatte 28/50), dann Platten
[Q12]. Heißt: **Der Plattenabstand wird von der Unterkonstruktion bestimmt, nicht vom Balkenabstand.**

**Nicht durchbohren — die Regel und ihre Begründung:**

- Ein tragender Holzbalken wird **nicht** quer durchbohrt, schon gar nicht mehrfach hintereinander. Im
  Forumsthread „Elektriker hat Holzbalken mehrfach durchbohrt": fünf nebeneinanderliegende Balken, 12 cm
  breit, im 50er-Jahre-Altbau, mehrfach durchbohrt; der Elektriker sagte „das machen wir immer so". Antwort
  des Moderators: „Das ist aber schon ein alter Balken … da macht man das erst recht nicht. Bei einem Loch OK,
  aber gleich ne Flöte bauen? Murks" [Q11].
- **Was zulässig ist, entscheidet der Tragwerksplaner**, nicht der Elektriker und nicht das Internet. Bohrungen
  liegen im Idealfall in der Nähe der Nulllinie (mittleres Drittel der Höhe), mit Randabstand, nicht im
  Auflagerbereich und nicht in Zugzone mit Rissen. Diese geometrischen Regeln sind Fachwissen der
  Tragwerksplanung; im vorliegenden Playbook sind sie **nicht primär belegt** (siehe „Unbelegt").
- **Was ohne Statiker geht:** Aufputz, Kabelkanal, Befestigung **seitlich** am Balken (Schraube in die Flanke),
  Abhängung mit Klemmverbindern. Was nicht geht: Stemmen, Schlitzen, Ausklinken, Durchbohren der Untersicht in
  Feldmitte, Kürzen von Balkenenden.

### 5.5 Lastreserven — rechnen, nicht schätzen

- **Bestand war oft nur „Speicher":** Ein Tragwerksplaner im Forum zu einer 7,5 × 7,5 m Decke mit 10 × 16 cm
  Balken im Abstand 70–80 cm: „Es ist ja nicht so, dass die Decke ‚schwach geworden' ist. Die sollte nie etwas
  tragen — außer sich selbst. Also Umnutzung." [Q13]
- **Zahlen:** Für einen Spitzboden, der von Anfang an als solcher geplant war, wurde die Decke für eine
  Verkehrslast von **1,0 kN/m² (= 100 kg/m²)** nachgewiesen; für einen Hobbyraum hält der Forumsexperte
  **mindestens 1,5 kN/m², eventuell 2,0 kN/m²** für nötig [Q14].
- **Wohnnutzung nach heutiger Norm:** DIN EN 1991-1-1, Kategorie A (Wohn- und Aufenthaltsräume, Flure,
  Treppen) = **2,0 kN/m²** [Q20]. Damit ist die Lücke benannt: 1,0 → 2,0 kN/m² ist **das Doppelte**.
- **Was das praktisch heißt:** Ein 1.000-Liter-Aquarium wiegt mit Glas, Kies und Technik grob 1,3 t. Auf
  2 m² Standfläche sind das ca. **6,5 kN/m²** — mehr als das Dreifache der Wohnlast. Das ist kein
  „schweres Möbelstück", das ist eine Sonderlast, die gerechnet werden muss. (Eigene Rechnung, keine Quelle.)
- Gleiches gilt für **Waschmaschine im OG** (Unwucht + 60–80 kg + Wasser), **Klavier/Flügel**,
  **Wasserbett**, **Hantelbank** und **Kaminofen** — alles Fälle für den Tragwerksplaner, nicht für den
  Bauch [Q14][Q18].

## 6. Rauspund oder Trockenbau?

| Kriterium | Rauspund (Nut und Feder) | Gipskarton/Gipsfaser |
|---|---|---|
| Materialpreis | Fichte **16,80–22,00 €/m²**, Lärche **28,10 €/m²** (Restposten/Lagerware, Stand 2026) [Q28] | ab **3 €/m²** [Q7] |
| Optik | warm, sichtbare Holzdecke, Fugenbild gewollt | glatt, streichfertig |
| Dampfverhalten | je nach Dicke/Aufbau mäßig diffusionsbremsend — bei zwei Lagen schnell zu dicht [Q24] | dampfoffen, aber nur mit Dampfbremse darunter [Q9] |
| Spachteln | Fugen bleiben sichtbar (gewollt) | Q2/Q3 nötig, 8–15 €/lfm Fuge [Q7] |
| Typischer Fehler | zu dünn bei weitem Lattenabstand | zu dünne Platte bei weitem Balkenabstand [Q12] |

**Entscheidungsregel:** Rauspund ist die **sichtbare** Decke (Dachboden-Charakter, Balken bleiben sichtbar),
Gipskarton die **glatte** Decke (Wohnraum, Streichen, Einbauleuchten). Beides ist Eigenleistung — aber
Rauspund verzeiht keine schiefe Unterkonstruktion, Gipskarton verzeiht sie mit Spachtel.

**Wenn Balken sichtbar bleiben sollen:** Dann wird **zwischen** den Balken beplankt (Einschub-Optik) oder die
Decke bleibt offen und die Balken werden aufgearbeitet. Die Variante „Balken sichtbar + glatte Fläche
dazwischen" ist die aufwendigste, weil jedes Gefach ein eigenes Maß hat.

## 7. Sichtbare Balken: strahlen, bürsten, lasieren

### 7.1 Was die Verfahren kosten und leisten

| Verfahren | Preis | Wirkung / Grenze | Quelle |
|---|---|---|---|
| Sandstrahlen (Holz) | **25–80 €/m²** brutto | trägt Altbeschichtung und oberste Holzschicht ab; Struktur wird freigelegt | [Q17] |
| Strahlstunde (Werkstatt) | **70–155 €/h** brutto | Kalkulation nach Zeit, wenn Fläche/Geometrie unklar | [Q17] |
| Mobile Strahlarbeiten | Zuschlag | Anfahrt, Einhausung, Absaugung, Rüstzeit, Entsorgung | [Q17] |

**Wichtig für alte Balken:** Sandstrahlen ist kein „Reinigen", sondern **Materialabtrag**. Bei dünnen,
gerissenen oder angefaulten Balken kann das die Tragfähigkeit weiter schwächen. Vorher ein **Probefeld** an
einer unauffälligen Stelle, danach entscheiden [Q17].

### 7.2 Arbeitsschutz — der Punkt, an dem Eigenleistung endet

- Strahlmittel dürfen nach den DGUV-Regeln grundsätzlich **höchstens 2 Masse-% freie kristalline Kieselsäure**
  (Quarz, Cristobalit, Tridymit) enthalten — Grund ist die Silikose- und Krebsgefahr durch alveolengängigen
  Quarzstaub [Q17].
- Daraus folgt: **Einhausung, Absaugung, Atemschutz, Entsorgung** sind Teil des Preises, nicht Deko. Wer im
  bewohnten Dachboden „mal eben" strahlt, verteilt Quarzstaub im ganzen Haus.

### 7.3 Die günstigen Alternativen (Reihenfolge nach Aufwand)

1. **Bürsten/Schleifen** (Nylonbürste, Schleifmittel) — entfernt lose Farbe, kein Abtrag der Struktur. Staub
   absaugen, nicht kehren.
2. **Beizen/Abbeizer** — nur bei löslichen Anstrichen; Laugen greifen Holz und Haut an.
3. **Lasur** (dünnschichtig, dampfoffen) statt Deckfarbe: lässt Maserung stehen, betont aber auch Risse und
   Astlöcher. Deckende Farbe auf alten Balken ist meist die falsche Entscheidung, weil sie die Struktur
   zuschmiert und später wieder ab muss.
4. **Ölen/Wachsen** — für Wohnräume angenehm, aber nicht in Feuchträumen.

**Unbelegt:** konkrete Preise für Bürsten/Schleifen und Lasur je m², sowie die Frage, ob alte Anstriche Blei
enthalten (Baujahr-abhängig). Vor dem Schleifen alter Lacke: Probe auf Blei, nicht annehmen.

## 8. Holzwurm und andere Holzschädlinge

### 8.1 Erkennen — die harten Merkmale

Nach Umweltbundesamt (Stand 16.10.2026) [Q16]:

- **Käfer:** 3–5 mm lang, dunkelbraun bis schwärzlich, gedrungener Körper, Halsschild kapuzenartig über dem
  Kopf, parallele Punktreihen auf den Flügeldecken.
- **Befall:** **Schlupflöcher ca. 1–2 mm** Durchmesser, aus denen **Bohrmehl** austritt; **Fraßgänge bis 2 mm**
  breit, teils mit festen Kotpartikeln verstopft; tote Käfer in den Schlupflöchern möglich.
- **Larvenentwicklung:** im Mittel **zwei Jahre**, abhängig von Nährstoffgehalt, Holzfeuchte und Temperatur.
- **Befallen wird meist nur Splintholz**, Kernholz wird gemieden; auch altes Holz wird befallen.
- **Der Gemeine Nagekäfer ist ein Materialschädling, kein Gesundheitsrisiko** — aber an tragenden Teilen kann
  er die **Tragfähigkeit gefährden** [Q16].

### 8.2 Was daraus folgt

- **Schadbild allein reicht nicht.** Das UBA schreibt ausdrücklich: Bei Verdacht „sollte grundsätzlich eine
  umfassende Bestimmung und Einordnung der holzzerstörenden Insekten mittels makroskopischer und
  mikroskopischer Untersuchung durch einen Sachverständigen erfolgen" — Grundlage sind Larven, Puppen oder
  geschlüpfte Käfer [Q16].
- **Tragende Teile:** Sachverständiger zur Prüfung auf statische Mängel hinzuziehen [Q16].
- **Bekämpfung:** „sollte durch eine Fachfirma nach **DIN 68800 Teil 4** durchgeführt werden" [Q16]. Die
  allgemeinen Grundlagen des Holzschutzes stehen in **DIN 68800-1:2019-06** [Q22].
- **Was man selbst tun kann:** befallene Möbel/Kleinteile warm und trocken stellen (Larven sterben durch
  Trocknung ab), kleine Teile mehrstündig auf **55 °C** erhitzen, Schlupflöcher anschließend mit Wachs
  verschließen [Q16]. Das gilt für **Möbel**, nicht für die Deckenbalken des Hauses.
- **Vorbeugend:** Der Käfer bevorzugt kühle Orte mit hoher relativer Luftfeuchte; Nutzen und Heizen verschlechtert
  seine Bedingungen; Holzbalken regelmäßig kontrollieren [Q16]. Ein ausgebauter, beheizter Dachboden ist
  deshalb biologisch kein „Neubau", sondern eine **Nutzungsänderung der Randbedingungen** — auch für den
  Schädling.

### 8.3 Wo man nachsieht (Praxis, unbelegt)

Balkenköpfe im Mauerwerk, Auflager, Fußpunkte der Schrägen, Bereiche unter undichten Fenstern, alte
Wasserflecken. Ein Endoskop durch eine Bohrluke (dann mit Statiker!) oder ein Blick von oben nach dem
Ausräumen des Einschubs bringt mehr als das Abklopfen der Untersicht.

## 9. Werkzeug und Material

**Kaufen (Eigenleistung):** Akkuschrauber mit Tiefenanschlag, Trockenbau-Bit, Cuttermesser, Wasserwaage
1,5 m, Schlagklatsche, Fuchsschwanz, Schutzbrille, Staubmaske FFP2/FFP3, Absaugung, Folienklebeband
(dampfdicht), Dampfbremse, CD-/UD-Profile, Direktabhänger, 12,5 mm Gipsplatten, Mineralwolle, Schüttung,
Trittschalldämmung, Schrauben (Trockenbauschrauben), Rauchmelder.

**Mieten statt kaufen:** Stemmhammer, Baustellenabsaugung mit Zyklon, Nivellierlaser, Plattenheber,
Gerüst/Turm, ggf. Strahlgerät (nur mit Einhausung und Absaugung).

**Materialpreise als Anker:** Gipsplatten ab 3 €/m², Holzplatten 7–18 €/m², Metallprofile 7–9 €/m² [Q7];
Rauspund Fichte 16,80–22,00 €/m² [Q28].

## 10. Kosten mit Quelle

### 10.1 Dachboden komplett ausbauen

MyHammer (aktualisiert 01.09.2026) nennt **500–2.000 €/m²** Gesamtkosten und folgende Beispielrechnung für
ca. 100 m² Dachfläche [Q6]. Die Zahlen sind laut Fußnote im Artikel „Schätzungen … mit Hilfe von KI
zusammengetragen" — also Marktbeobachtung, keine Angebotspreise:

| Posten | Menge | Kosten |
|---|---|---|
| Dachdämmung | 100 m² | 4.700–12.000 € |
| Dachfenster/Rolladen | 1 Stück | 1.200–2.000 € |
| Gauben | 2 Stück | 6.400–14.000 € |
| Trockenbauwände | 50 m² | 3.300–4.800 € |
| Trittschalldämmung | 60 m² | 1.200–1.800 € |
| Bodenbelag | 50 m² | 900–2.100 € |
| Tapezieren | 100 m² | 400–1.500 € |
| Sanitärmöbel | pauschal | 200–1.000 € |
| Heizung | 3 Stück | 200–500 € |
| Installationsmaterial | 60 m² | 800–1.900 € |
| **Summe** | | **19.800–42.000 €** |

Dazu nennt derselbe Artikel Materialkosten von **12.100–27.300 €** und Handwerkerkosten von
**9.400–13.000 €**, Stundensätze **30–80 €** (Zimmermann 30–60, Elektriker 50–70, Installateur 40–60, Maler
20–40) und Genehmigungskosten **200–1.500 €** [Q6].

**Einordnung:** 2.000 €/m² ist ein Ausbau mit Gauben, Bad und neuer Treppe. Wer nur dämmt, beplankt und
streicht, liegt deutlich darunter — dafür fehlen in der Tabelle die Eigenleistungs-Anteile. Die Spanne ist
deshalb ein **Band**, kein Preis.

### 10.2 Decke abhängen

MyHammer nennt **40–70 €/m²** im Durchschnitt, **38–50 €/m²** für Direktabhängung mit Gipskarton und
**40–70 €/m²** für Holzunterbau mit Holzdecke; Zusatz: Fugen spachteln **8–15 €/lfm**, Verputzen
**10–20 €/m²**, LED-Beleuchtung **30–40 €/Element** [Q7].

**Widerspruch in der Quelle:** Im Einleitungstext stehen „45 bis 150 Euro pro Quadratmeter", in der
Zusammenfassung „40 bis 70". Beide Zahlen stehen lassen, nicht mitteln — die 150 dürfte Sonderfälle
(Akustik, Brandschutz, hohe Räume) abdecken. Für die Kalkulation die engere Spanne nehmen und im Angebot
nach Positionen fragen.

### 10.3 Sichtbare Balken aufarbeiten

Holz sandstrahlen **25–80 €/m²** brutto; Werkstattstunde **70–155 €** brutto; mobile Arbeiten mit Zuschlag
[Q17]. Bei 30 lfm Balken mit 20 cm Breite (6 m² sichtbare Fläche) sind das grob **150–480 €** Strahlkosten —
plus Einhausung, Absaugung, Entsorgung. (Eigene Rechnung aus [Q17], keine Angebotszahl.)

### 10.4 Was die Zahlen nicht enthalten

Gerüst, Container/Entsorgung, Baustrom, Werkzeugmiete, Versicherung, Puffer. Für die Vollkostenrechnung
`kosten-bauzeit.md` nehmen; hier stehen nur die bauteilbezogenen Sätze.

## 11. Die teuren Fehler (mit Quelle)

1. **Dämmung ohne durchgehende Dampfbremse/Luftdichtheit.** Folge: Raumluft diffundiert in die Dämmung,
   kühlt ab, Tauwasser, nasse Mineralwolle dämmt nicht mehr, Schimmel an Gipskarton/Deckenbekleidung möglich
   [Q9][Q24]. Besonders tückisch: Die Folie ist da, aber am Wandbalken oder an der Einschubtreppe nicht
   angeschlossen [Q14][Q26].
2. **Zwei Dampfbremsen übereinander** (OSB oben, Gipskarton unten, Folie dazwischen): Feuchte wird
   eingeschlossen, „auf jeden Fall ein Feuchtigkeitsproblem" [Q24].
3. **Sparren/Balken durchbohrt, „das machen wir immer so".** Fünf 12-cm-Balken mehrfach durchbohrt; fachlich
   „Murks", bei alten Balken erst recht [Q11]. Querschnittsschwächung in Feldmitte ist ein Statikthema, kein
   Elektrothema.
4. **Last an der Decke überschritten.** Speicherdecke 1,0 kN/m², Wohnnutzung 2,0 kN/m², Aquarium >6 kN/m²
   [Q14][Q20]. Der Fehler passiert nicht beim Ausbau, sondern zwei Jahre später beim Einzug.
5. **Holzwurm ignoriert.** „Ein Befall mit dem Gemeinen Nagekäfer an tragenden Holzteilen im Haus ist ernst zu
   nehmen, da dieser mitunter die Tragfähigkeit dieser Bauteile gefährden kann" [Q16]. Schadbild allein
   genügt nicht; Bestimmung durch Sachverständigen, Bekämpfung nach DIN 68800-4 [Q16].
6. **Rettungsweg fehlt / Einschubtreppe bleibt.** Einschiebbare Treppen sind als notwendige Treppe unzulässig
   und nur für Dachräume **ohne** Aufenthaltsraum zulässig [Q1, § 34 Abs. 2]. Wer den Ausbau ohne Treppe
   plant, plant am Bauamt vorbei.
7. **Nutzungsänderung nicht angemeldet.** Genehmigungspflicht nach MBO § 59 Abs. 1 [Q1]; in der Praxis fast
   immer, sobald Wohnraum entsteht [Q10]. Kosten der Genehmigung sind klein gegen den Ärger.
8. **9,5-mm-Platten auf 70 cm Balkenabstand.** „Sehr sportlich", Durchhang sichtbar; UD 27/28 + CD im
   Abstand ≤ 50 cm ist die Lösung [Q12].
9. **Masse als Allheilmittel.** Einschub 0 → 120 kg/m² bringt max. 3 dB Trittschall [Q8]. Wer 5 t Schüttung
   einbringt, hat 1–2 dB gewonnen und die Deckenlast erhöht.
10. **Strahlen ohne Probfeld und ohne Einhausung.** Materialabtrag an dünnen Balken, Quarzstaub im Haus
    (DGUV: max. 2 Masse-% kristalline Kieselsäure im Strahlmittel) [Q17].

## 12. Kontrollpunkte vor dem nächsten Gewerk

- [ ] Nutzungsänderung schriftlich geklärt, LBO-Auszug zur Höhe im Ordner.
- [ ] Meterriss gesetzt, lichte Höhe nach Abzug von Unterkonstruktion + Beplankung + Bodenaufbau nachgemessen.
- [ ] Rettungsweg begehbar, Treppenmaße (Laufbreite, Steigung, Auftritt) geprüft, Geländer vorhanden.
- [ ] Rauchmelder in Schlafräumen/Kinderzimmern und Fluren eingeplant (LBO).
- [ ] Statik: Deckenlast, Balkenquerschnitte, Auflager, Schwingung bewertet; Bohrungen/Schlitze freigegeben.
- [ ] Dampfbremse: alle Überlappungen geklebt, alle Anschlüsse (Wand, Fußpfette, Kehlbalken, Fenster,
      Durchdringungen) dicht; Fotos vor der Beplankung.
- [ ] Dämmung lückenlos, nicht gequetscht, hinterlüftungstauglich nach Hersteller.
- [ ] Unterkonstruktion: Abstände, Befestigung, Entkopplung; keine Schraube in die Zugzone des Balkens.
- [ ] Beplankung: Plattenstöße versetzt, Schraubenabstände nach Hersteller, Fugenbild dokumentiert.
- [ ] Holzwurm: Befall ausgeschlossen oder saniert, Protokoll des Sachverständigen.
- [ ] Fotos von jeder offenen Decke mit Maßband — das ist das Baudokument, das später zählt.

## 13. Wann Fachbetrieb

| Aufgabe | Warum nicht selbst |
|---|---|
| Nutzungsänderung/Bauantrag | Bauvorlageberechtigung, LBO-Kenntnis |
| Statik, Verstärkung, neue Träger, Deckenausschnitt | Tragwerksplanung; falsche Annahme = Versagen |
| Dampfbremse im Steildach, Anschlüsse Traufe/Kehle | Dachdecker-/Zimmererausbildung: Dampfsperr-/Luftdichtheitsschichten [Skill: Ausbildungsordnungen] |
| Elektro hinter der Dampfbremse | NAV § 13 Abs. 2, siehe `elektro.md` |
| Treppe mit Absturzhöhe, Geländer | Statik, DIN 18065, Bauordnungsrecht |
| Schädlingsbekämpfung an tragenden Teilen | Sachverständiger + Fachfirma nach DIN 68800-4 [Q16] |
| Sandstrahlen im bewohnten Haus | Staub, DGUV, Entsorgung [Q17] |

**Eigenleistung bleibt sinnvoll:** Rückbau, Einschub ausräumen, Dämmung einbringen (nach Vorgabe),
Unterkonstruktion, Beplankung, Spachteln, Streichen, Rauchmelder montieren, Bodenbelag.

## 14. Quellen (alle am 09.11.2026 auf HTTP-Status geprüft)

| Nr. | Quelle | URL | Status |
|---|---|---|---|
| Q1 | Musterbauordnung (MBO), Fassung November 2002, zuletzt geändert 22.02.2019 — §§ 33, 34, 47, 59 | https://bauministerkonferenz.de/Dokumente/42323066.pdf | 200 |
| Q2 | Bayerische Bauordnung, Art. 45 Aufenthaltsräume (2,40 m / Dachgeschoss 2,20 m / 1,50 m) | https://www.gesetze-bayern.de/Content/Document/BayBO-45 | 200 |
| Q3 | Bayerische Bauordnung, Art. 46 Wohnungen (Rauchwarnmelder Abs. 4; Bestandsschutz Abs. 5) | https://www.gesetze-bayern.de/Content/Document/BayBO-46 | 200 |
| Q4 | Bayerische Bauordnung, Art. 31 Rettungswege | https://www.gesetze-bayern.de/Content/Document/BayBO-31 | 200 |
| Q5 | DIN 18065:2020-08, Treppenmaße — Tabellenwerte und Schrittmaßregel, zusammengestellt bei treppauf.de | https://treppauf.de/din18065-treppenmasse.htm | 200 |
| Q6 | MyHammer, „Dachboden ausbauen: Was kostet es?", aktualisiert 01.09.2026 | https://www.my-hammer.de/bauen-renovieren/preisradar/was-kostet-dachboden-ausbauen | 403 (Bot-Schutz) |
| Q7 | MyHammer, „Decke abhängen: Kosten" (40–70 €/m², Zusatzpositionen) | https://www.my-hammer.de/trockenbau-verputzen/preisradar/was-kostet-decke-abhaengen | 403 (Bot-Schutz) |
| Q8 | Saint-Gobain Rigips, Technik Aktuell Nr. 64 (06/18), „Schallschutz von Holzbalkendecken", 28 S. PDF | https://www.rigips.de/Dokumente/technik-aktuell/ta-schall-holzbalkendecken.pdf | 200 |
| Q9 | Knauf, DIY-Anleitung „Dachgeschossausbau: Dämmen und Beplanken" | https://knauf.com/de-DE/kunden-gruppe/diy/anleitungen/dachgeschossausbau/daemmen-und-beplanken | 403 (Bot-Schutz) |
| Q10 | VELUX Magazin, „Dachausbau-Genehmigung — In welchem Fall ist sie notwendig?" | https://www.velux.de/magazin/dachausbau-genehmigung | 200 |
| Q11 | bauexpertenforum.de, „Elektriker hat Holzbalken mehrfach durchbohrt" | https://www.bauexpertenforum.de/threads/elektriker-hat-holzbalken-mehrfach-durchbohrt.115835/ | 200 |
| Q12 | bauexpertenforum.de, „Holzbalkendecke und Gipskartonverkleidung" (9,5 mm bei 70 cm) | https://www.bauexpertenforum.de/threads/holzbalkendecke-und-gipskartonverkleidung.106500 | 200 |
| Q13 | bauexpertenforum.de, „Holzbalkendecke 7,5 m Spannweite von oben stabilisieren, WIE?" | https://www.bauexpertenforum.de/threads/holzbalkendecke-7-5m-spannweite-von-oben-stabilisieren-wie.72967 | 200 |
| Q14 | expertenforum-bau.de, „Nachträglicher Ausbau und Dämmung des Spitzboden" (1,0 kN/m², Raumhöhe) | https://expertenforum-bau.de/forum?diskussion/5577-nachtr%C3%A4glicher-ausbau-und-d%C3%A4mmung-des-spitzboden/= | 200 |
| Q15 | fachwerk.de, „Holzbalkendecke schwingt" (BJ 1956, 20 cm Balken, 8,5 m) | https://www.fachwerk.de/threads/holzbalkendecke-schwingt.309032 | 200 |
| Q16 | Umweltbundesamt, „Gemeiner Nagekäfer (Holzwurm)", aktualisiert 16.10.2026 | https://www.umweltbundesamt.de/gemeiner-nagekaefer-holzwurm | 200 |
| Q17 | listando, „Sandstrahlen: Kosten pro m² und Stunde 2026" (Holz 25–80 €/m², DGUV 2 Masse-%) | https://listando.com/de-de/maler/sandstrahlen-kosten | 200 |
| Q18 | WTA-Merkblatt 8-13-13/D „Ertüchtigung von Holzbalkendecken nach WTA I", Fachbeitrag Bausubstanz 4/2013 (PDF) | https://www.irbnet.de/daten/rswb/14039011579.pdf | 200 |
| Q19 | Wikipedia, „Holzbalkendecke" (Aufbau, Einschub, Blindboden, Füllung) | https://de.wikipedia.org/wiki/Holzbalkendecke | 200 |
| Q20 | Wikipedia, „Nutzlast (Bauwesen)" — Kategorie A (Wohn-/Aufenthaltsräume) 2,0 kN/m² nach DIN EN 1991-1-1 | https://de.wikipedia.org/wiki/Nutzlast_(Bauwesen) | 200 |
| Q21 | Bischoff & Schäfer, „Sortierhilfen und Erläuterungen zur Anwendung der DIN 4074-1" (Sortierklassen S7/S10/S13) | https://www.bischoff-schaefer.de/fileadmin/editor/PDF/DE/Datenblaetter/erlaeuterungen_zur_din_4074_1.pdf | 200 |
| Q22 | DIN 68800-1:2019-06 „Holzschutz — Teil 1: Allgemeines", Produktseite DIN Media | https://www.dinmedia.de/en/standard/din-68800-1/302767659 | 200 |
| Q23 | YouTube, HORNBACH Meisterschmiede, „Dachboden ausbauen: Planung" (Transkript, ASR) | https://www.youtube.com/watch?v=aWViNIS6Uo0 | 200 |
| Q24 | YouTube, Homealex, „Holzbalkendecke dämmen: Mineralwolle richtig einbauen" (Transkript, ASR) | https://www.youtube.com/watch?v=ENuzEV2Pg4c | 200 |
| Q25 | Reddit r/Handwerker, „Dachausbau Reihenfolge Dampfbremse" (Installationsebene) | https://www.reddit.com/r/Handwerker/comments/1reoc1m/dachausbau_reihenfolge_dampfbremse/ | 200 |
| Q26 | Reddit r/selbermachen, „Holzbalkendecke dämmen" (Luftdichtheit von oben, Zellulose) | https://www.reddit.com/r/selbermachen/comments/1hp9c62/holzbalkendecke_d%C3%A4mmen/ | 200 |
| Q27 | Reddit r/Carpentry, „Fixing sagging rafter ties/ceiling joists" (2x4 auf 20 ft, undersized) | https://www.reddit.com/r/Carpentry/comments/tntr1g/fixing_sagging_rafter_tiesceiling_joists/ | 200 |
| Q28 | meinholz24, „Nut-und-Feder-Bretter: Stärken, Holzarten, Preise" (16,80–28,10 €/m²) | https://www.meinholz24.de/magazin/nut-und-feder-bretter/ | 200 |
| Q29 | dachdeckerforum.de — **nicht erreichbar** (HTTP 000, Domain antwortet nicht) | — *dachdeckerforum.de: keine Antwort am 09.11.2026 (Domain tot), Link entfernt.* | 000 (tot) |
| Q30 | DIN 4109-1:2018-01 / DIN 4109-5:2020-08 / DIN 4109-33:2016-07 — Nummer, Titel und Ausgabe belegt über die Tabellen in [Q8] und `references/quellen.md`; Volltexte kostenpflichtig, nicht zitiert | (Beuth/DIN Media) | — |

**Quellenlage, ehrlich:** Von 29 Quellen mit URL antworten **25 mit HTTP 200**, **drei mit 403**
(Bot-Schutz, Inhalt über den Extractor gelesen: Q6, Q7, Q9), **eine ist tot** (Q29, HTTP 000). Q30 ist eine
Normreferenz ohne eigene URL (Beuth/DIN Media, kostenpflichtig). Das ursprünglich vorgesehene **dachdeckerforum** existiert nicht mehr;
als Forum-Ersatz stehen bauexpertenforum (3 Threads), expertenforum-bau und fachwerk.de. Die YouTube-Quellen
sind **automatische Untertitel (ASR)** — Zahlen daraus sind gegen die Herstellerangaben geprüft, nicht
gegen ein Skript.

## 15. Unbelegt / Schätzung

Diese Punkte sind **nicht** durch eine der obigen Quellen gedeckt und werden als Vermutung gekennzeichnet:

- **Bohrgeometrie in Holzbalken** (zulässiger Durchmesser, Abstand zum Auflager, Lage im Querschnitt): Die
  Regel „mittleres Drittel, Randabstand, nicht im Auflager" ist Fachwissen der Tragwerksplanung. Im Playbook
  steht sie als **Orientierung ohne Primärquelle** — verbindlich ist der Statiker.
- **Mindestholzfeuchte / Messverfahren** vor dem Beplanken (Gerät, Zielwert): keine Quelle geprüft.
- **Preise für Bürsten, Schleifen, Beizen, Lasur je m²**: keine belastbare Quelle gefunden.
- **Bleigehalt alter Anstriche** und Entsorgung: Baujahr-abhängig, ohne Probe nicht beantwortbar.
- **U-Werte und Dämmstärken nach GEG** für den konkreten Dachaufbau: gehören in die Energieberatung
  (`daemmung.md`), nicht hierher.
- **Schallwerte für den konkreten Bestandsaufbau**: Die Zahlen aus [Q8] gelten für die dort geprüften
  Referenzaufbauten, nicht für jedes Haus. Eine Messung vor Ort (ift/Prüfstelle) ersetzt die Tabelle.
- **Genehmigungsfreie Fälle je Bundesland**: hängt von LBO und Vorhabenbegriff ab; ohne Bauamtsauskunft keine
  Aussage.
- **Tragfähigkeit bestehender Balken** ohne Freilegung: nicht schätzbar. Wer „das hält schon" sagt, ohne
  Querschnitt, Holzart, Sortierklasse [Q21] und Auflager gesehen zu haben, rät.
- **Kostenband 500–2.000 €/m²**: Marktbeobachtung mit KI-erzeugten Schätzungen [Q6], kein Angebot. Für die
  eigene Kalkulation drei Angebote pro Gewerk.
