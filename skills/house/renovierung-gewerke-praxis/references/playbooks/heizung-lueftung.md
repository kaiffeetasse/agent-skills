# Heizung & Lüftung im Bestand — Playbook für Eigenheimbesitzer

> **Preisstand 09/2026.** Alle Preise sind Orientierungswerte inkl. MwSt. aus den genannten Quellen —
> regional verschieden, keine Angebote. Wer später damit rechnet, prüft sie neu.

## Kurzantwort

- **Heizkörper tauschen und Abgleich sind Eigenleistung** (bis auf Eingriffe an Gas/Öl).
- **Die Zahl, die zählt:** ein Heizkörper für 75/65 liefert bei **55/45 nur etwa die Hälfte** der Leistung —
  deshalb wird bei Wärmepumpe getauscht oder vergrößert.
- **Fußbodenheizung:** Aufbauhöhe 2–10 cm je System, auf Holzbalkendecke nur trocken und mit Statik.
- **Lüften:** Lüftungskonzept nach DIN 1946-6 ist bei dichter Hülle Pflicht, nicht Kür.


**Stand:** 09.11.2026 · **Zielgruppe:** Eigentümer eines Ein-/Zweifamilienhauses, handwerklich begabt, kein SHK-Profi
**Grenze dieses Playbooks:** Du entscheidest, bereitest vor, kaufst, prüfst Angebote und erkennst Pfusch. Gasinstallation, Kesseltausch, KWL-Einbau und alles am Estrich bleiben Fachbetrieb (Begründung unten). Alle Preise sind **Bänder**, keine Punktpreise; alle Zahlen mit `[Qnn]` sind belegt, alle ohne Kürzel sind Erfahrungswerte und als solche gekennzeichnet.

**Kurzantwort:** Der beste Hebel im Bestand ist nicht der Tausch, sondern die Reihenfolge: erst entlüften und Ventile gangbar machen, dann Heizkurve/Vorlauf senken, dann Heizkörpernische und Rohre dämmen, dann hydraulischer Abgleich — und *erst danach* über neue Heizkörper oder Fußbodenheizung nachdenken. Wer zuerst tauscht, kauft oft zu kleine Heizkörper, weil er die Auslegungstemperatur nicht kennt.

---

## 0. Was du selbst darfst — und was nicht

| Aufgabe | Selbst machbar | Warum / Beleg |
|---|---|---|
| Heizkörper streichen, reinigen, entlüften, Thermostatkopf wechseln | **ja** | keine Gas-/Stromberührung; Anleitungen von Herstellern und Verbraucherportalen `[Q17][Q20][Q22][Q39]` |
| Heizkörper tauschen (Wasser ablassen, Verschraubung, neu setzen) | **ja, mit Risiko** | gewerblich nur SHK-Fachbetrieb (HwO Anlage A Nr. 24 `[Q40]`); privat keine ausdrückliche Verbotsnorm wie bei Gas/Strom — aber Undichtigkeit, Gewährleistung und Versicherung sind dein Risiko |
| Ventileinsatz tauschen (nicht nur Kopf) | **eher Fachbetrieb** | Eingriff in den Heizkreis, System muss drucklos; Adapter-/Gewindevielfalt `[Q34]` |
| Hydraulischer Abgleich | **teilweise** | „thermischer Abgleich" als Näherung selbst; Verfahren B braucht raumweise Heizlast und voreinstellbare Ventile `[Q21][Q26]` |
| Estrich fräsen, FBH nass einbauen, Estrich gießen | **nein** | Statik, Höhenlage, Belegreife; danach ist alles zu spät (siehe `estrich.md`) |
| FBH Trockensystem auf Holzbalkendecke | **nur mit Statik-Check** | Gewicht und Aufbauhöhe sind die Knackpunkte `[Q12][Q29]` |
| KWL planen/einbauen | **nein** (Einbau), Konzept lesen: ja | Luftmengen, Schall, Brandschutz, Elektroanschluss `[Q04][Q31]` |
| Gasseitige Arbeiten an Therme/Leitung | **nein, ausnahmslos** | TRGI, Fachbetrieb |
| Absenkung, Heizkurve, Pumpenstufe | **ja** | Bedienung der Regelung, keine Eingriffe in die Hydraulik `[Q02][Q11]` |

Die Grenze verläuft nicht zwischen „schwer" und „leicht", sondern zwischen **Wasser/Statik** und **Gas/Strom**. Heizungswasser ist kein Gas: Wenn du es falsch machst, wird der Boden nass, nicht das Haus explosionsgefährdet. Genau deshalb ist der Heizkörpertausch die beste Eigenleistung im Heizungsbereich — und der Estrich die schlechteste.

**Abgrenzung zur allgemeinen Renovierungslogik:** Der Basisskill `renovierung-gewerke-praxis` zählt „Heizungshydraulik" pauschal zum Fachbetrieb. Dieses Playbook differenziert: **einzelner Heizkörper 1:1 tauschen** ist die Grauzone, in der Eigenleistung vertretbar ist; **Eingriffe in die Verteilung** (Rohre, Strang, Verteiler, Ventileinsätze, Kesselanbindung) bleiben Fachbetrieb — dort entscheidet die Hydraulik über die Funktion des ganzen Hauses, nicht nur eines Raums.

---

## 1. Heizkörper tauschen

### 1.1 Wann tauschen — und wann nicht

Tauschen lohnt, wenn:
- der Heizkörper **zu klein** ist für die tatsächliche Auslegung (Symptom: Raum wird auch bei voll geöffnetem Ventil nicht warm, obwohl die Anlage läuft),
- eine **Wärmepumpe** geplant ist: dann muss die Heizfläche bei niedriger Vorlauftemperatur reichen `[Q10]`,
- der Heizkörper **durchgerostet** ist (Nassstelle unten, braune Suppe beim Entlüften),
- die **Nische** ohnehin geöffnet wird (dann Dämmung mitmachen, siehe §5).

Nicht tauschen, nur weil er „alt aussieht". Ein alter Gliederheizkörper mit sauberem Wasser und funktionierendem Ventil heizt so gut wie ein neuer gleicher Größe; er hat mehr Wasserinhalt und reagiert träger. Der BDH nennt als Argument für den Tausch die **Trägheit und schlechte Regelbarkeit** alter Körper `[Q08]` — ein Verbrauchsvorteil entsteht daraus nur, wenn der alte Körper tatsächlich unterdimensioniert oder verschlammt ist, nicht durch das Baujahr allein.

### 1.2 Die Größe: der teuerste Rechenfehler

Heizkörperleistung im Katalog gilt immer für **Normbedingungen 75/65/20 °C** (Vorlauf/Rücklauf/Raum) `[Q38]`. Deine Anlage läuft aber selten so. Die Leistung skaliert mit der logarithmischen Übertemperatur:

```
ΔT_ln = (VL − RL) / ln((VL − RT) / (RL − RT))
Leistungsfaktor = (ΔT_ln / 49,83)^n        n ≈ 1,3 bei Plattenheizkörpern
```

Daraus ergibt sich (gerechnet, n = 1,3, Raum 20 °C):

| Systemtemperatur | ΔT_ln | Leistung vs. Katalog | Nötige Größe |
|---|---|---|---|
| 75/65 | 49,8 K | 100 % | 1,0 × |
| 70/55 | 42,1 K | 80 % | 1,25 × |
| 55/45 | 29,7 K | **51 %** | **2,0 ×** |
| 50/40 | 24,7 K | **40 %** | **2,5 ×** |
| 45/35 | 19,6 K | **30 %** | **3,3 ×** |
| 40/30 | 14,4 K | 20 % | 5,0 × |

**Konsequenz:** Ein Heizkörper, der bei 75/65 „passt", liefert bei 55/45 nur die Hälfte. Wer für eine Wärmepumpe tauscht und „die gleiche Größe" wieder einbaut, hat Geld ausgegeben und nichts gewonnen. Der BWP empfiehlt, die Vorlauftemperatur auf **maximal 50 °C** zu begrenzen und dafür zu prüfen, ob die vorhandenen Radiatoren die Räume noch versorgen — oft reicht es, **nur einzelne** Radiatoren zu vergrößern `[Q10]`.

**Was du wirklich brauchst:** eine **raumweise Heizlastberechnung nach DIN EN 12831**, nicht die Quadratmeter-Faustformel. Im Fachforum ist der Satz dazu eindeutig: „Heizlastberechnung machen! Alles andere kommt nur von der Glaskugel" `[Q28]`. Die Heizlast kannst du von einem Energieberater rechnen lassen (Erfahrungswert: ~100–300 €) — das ist billiger als ein falsch gekaufter Heizkörper und die Grundlage für jeden Förderantrag.

**Typen (Plattenheizkörper):** Die Zahl bezeichnet **Platten + Konvektorlamellen**: Typ 22 = 2 Platten, 2 Lamellen; Typ 33 = 3 Platten, 3 Lamellen `[Q38]`. Bei gleicher Baulänge und -höhe liefert Typ 33 mehr Leistung als Typ 22, ist aber tiefer (mehr Wandabstand, mehr Staubfläche). Im Zweifel: **größerer Typ statt höherer Vorlauf** `[Q28]`.

**Anschluss:** Entscheidend sind drei Maße — **Anschlussabstand** (Nabenabstand der beiden unteren Anschlüsse), **Bauhöhe**, **Baulänge** — plus die Anschlussart (Seiten- oder Untenanschluss, 2-Rohr). Passt der Neue millimetergenau auf die vorhandenen Anschlüsse, entfallen Rohr- und Stemmarbeiten `[Q08]`. Miss **vor** der Bestellung am alten Körper: Nabenabstand Mitte-Mitte, Höhe, Länge, Tiefe, Lage des Thermostatventils (links/rechts), Vor-/Rücklauf.

### 1.3 Ablauf in sechs Schritten (BDH)

1. Heizkörper mit passender **Anschlussvariante** auswählen `[Q08]`.
2. **Wasserzufuhr stoppen** (Vor- und Rücklauf schließen; bei alten Anlagen Rücklaufverschraubung prüfen — sie ist oft die Ursache, wenn später „nur oben warm", siehe §6.3) `[Q08][Q27]`.
3. **Verschraubung lösen**, Heizkörper abnehmen (Wasser in Wanne/Bottich, Lappen, Boden abdecken) `[Q08]`.
4. Neuen Körper einhängen, **neue Dichtungen** verwenden, Verschraubung anziehen.
5. **Wasserzufuhr öffnen**, Dichtheit an beiden Anschlüssen prüfen (Zewa-Test, 10 Minuten).
6. **Entlüften** `[Q08]`, Druck prüfen, ggf. nachfüllen.

Praxisergänzungen (Erfahrungswerte, nicht belegt):
- Vor dem Abnehmen Anlage **drucklos** machen und Heizkörper abkühlen lassen — sonst 60 °C Wasser auf dem Parkett.
- Zwei Personen, ein Rollbrett und ein flacher Bottich; ein 1,2-m-Körper wiegt 30–60 kg nass.
- Bei Fußbodenheizung im selben Kreis: Ventil am Verteiler zusätzlich schließen.

### 1.4 Entlüften — und die Verwechslung, die fast jeder macht

**Luft im Heizkörper** erkennst du daran: der Körper wird **vorne am Thermostatventil heiß und hinten kalt**, und es **gluckert** `[Q20, 00:00:48–00:01:02]`.

**Kein Luftproblem** ist: **oben warm, unten kühler**. Das ist die normale Abkühlung des Wassers im Kreis, bis zu **20 K Differenz** `[Q20, 00:02:21–00:03:06]`. Wer das für Luft hält, entlüftet endlos und wundert sich.

Vorgehen `[Q22][Q39]`:
1. **Umwälzpumpe aus** (sonst zieht sie Luft nach) `[Q22]`.
2. **Alle Heizkörper voll aufdrehen** `[Q22]`.
3. Beim **obersten/letzten** Heizkörper anfangen, dann abwärts `[Q22]`.
4. Entlüftungsschlüssel (Vierkant) ansetzen, eine Vierteldrehung öffnen, Gefäß darunter, Lappen an die Wand.
5. Warten, **bis Wasser kommt** (nicht nur bis es zischt), dann schließen `[Q20][Q39]`.
6. **Druck prüfen**: Faustformel Einfamilienhaus **1–2 bar**, danach ggf. nachfüllen `[Q22]`. Viessmann: nach dem Entlüften mindestens **eine Stunde** laufen lassen und den entferntesten Heizkörper erneut prüfen `[Q39]`.
7. **Nie mit Zange am Vierkant** drehen — rundgedrehtes Ventil kostet mehr als der Schlüssel `[Q39]`.

Wenn du **mehrfach** entlüften musst, ist es kein Luftpolster, sondern ein **tieferliegendes Problem**: Undichtigkeit, falsch eingestellte Pumpe, Sauerstoffeintrag über diffusionsoffene Rohre `[Q39]`. Im US-Fachforum wird genau dieser Fall diskutiert: ein Heizkörper, der nach Entleeren zwei Tage läuft und dann wieder kalt ist — Antwort: Luft steigt nach oben, sie muss am höchsten Punkt raus; automatische Entlüfter sind bequem, aber ein bekanntes Leckrisiko `[Q36]`.

---

## 2. Heizkörper aufarbeiten: streichen, entkalken, nachrüsten

### 2.1 Streichen (Eigenleistung, 1–2 h pro Körper)

Vier Schritte `[Q17]`:
1. **Abkleben und abdecken**: Folie/Vlies auf Boden, Ventile und Anschlüsse mit Kreppband.
2. **Untergrund**: abblätternde Farbe und oberflächlichen Rost entfernen, anschleifen, entfetten.
3. **Grundieren** (Rostschutz), dann **Heizkörperlack** (hitzebeständig) dünn in zwei Gängen.
4. **Trocknen lassen**, bevor geheizt wird.

Wichtig: Du musst den Heizkörper dafür **nicht abbauen** `[Q17]`. Wandfarbe hält auf Heizkörpern nicht — es braucht Heizkörperlack. Das ist der einzige „Trick", der wirklich zählt.

### 2.2 Entkalken — die ehrliche Antwort

In einem **geschlossenen Heizkreis** verdampft kein Wasser, deshalb fällt Kalk nicht wie im Wasserkocher als Belag aus. Kesselstein bildet sich punktuell an den heißesten Flächen (Wärmetauscher/Kessel), nicht als Schicht im Heizkörper. Was Heizkörper tatsächlich zusetzt, sind **Schlamm, Magnetit und Luft** — und das ist **Spülen/Entschlammen**, keine Entkalkung. Das macht der Fachbetrieb mit Spülgerät und Wasserqualitätskontrolle; selbst „mal eben Essig rein" schädigt Dichtungen und Alu-freie Komponenten.

Kalk **außen** (Badsockel, Armaturen, Fliesen) ist ein Reinigungsthema, kein Heizungsthema.

Für das Playbook heißt das: **„Heizkörper entkalken" ist bei wassergeführten Heizungen meist die falsche Diagnose.** Richtig ist: entlüften (§1.4), Ventil gangbar machen (§2.3), spülen lassen (Fachbetrieb), Wasserqualität prüfen.

### 2.3 Thermostatventile nachrüsten

Alte Anlagen haben oft **Handventile** („auf/zu", kein Thermostatkopf). Nachrüsten heißt: **Thermostatkopf auf vorhandenes Ventilunterteil** — oder, wenn das Unterteil alt/defekt ist, **Ventileinsatz tauschen**.

Was du wissen musst:
- **Gewinde/Adapter sind der Knackpunkt.** Standard ist M30 × 1,5; alte Fabrikate (z. B. MMA) haben M28 × 1,5 und brauchen einen Adapter. Im Forum sucht jemand für Heizkörper von ~1985 genau diesen Einsatz und findet ihn nicht auf Anhieb — Antwort: „Das mit den Einsätzen ist ziemlich ärgerlich, wenn man das nicht täglich macht, kann man es eigentlich nur herausfinden, wenn man alt und neu nebeneinander in der Hand hält" `[Q34]`. PraxistiAlten Kopf abschrauben, Gewinde messen, Foto machen, beim Hersteller/Händler mit Baujahr und Ventilhersteller anfragen.
- **Klemmender Ventilstift** ist der häufigste Defekt: Kopf ab, Stift mit Zange vorsichtig bewegen, WD40, mehrfach hin und her `[Q34][Q19]`. Hilft das nicht, ist der Einsatz hin.
- **Alte Handventile vs. Thermostat:** Der Energiesparkommissar zeigt den Unterschied im Schnittmodell: Handventil = „Ventil auf, mehr Wärme, Ventil zu, keine Wärme"; Thermostatventil regelt über den Stift und die Raumtemperatur `[Q19, 00:05:06–00:15:59]`. Ein Thermostatkopf spart nicht durch Magie, sondern weil er **nicht dauerhaft volle Leistung** durchlässt.
- **Kosten** (Fachforum, keine Rechnung): „nicht mehr als 500 €" für 6 Ventile, wenn es Heimeier-Ventile sind und nur die Einsätze getauscht werden, 1–2 Stunden bei vorhandener Absperrung; eine andere Schätzung: 2 Monteurstunden + **30 € pro Ventileinsatz** `[Q37]`.

### 2.4 Hydraulischer Abgleich — einfach erklärt

**Das Problem:** Jeder Heizkörper bekommt so viel Wasser, wie der Weg des geringsten Widerstands zulässt. Der nahe, kleine Heizkörper im Flur wird überflutet und überheizt; der große im kalten Eckzimmer bekommt zu wenig. Der Thermostatkopf regelt zwar die Raumtemperatur, aber nur durch **Zudrehen** — die Pumpe arbeitet dann gegen geschlossene Ventile, und die Rücklauftemperatur steigt, was den Kessel/Wärmepumpe unwirtschaftlich macht.

**Die Lösung:** Am Ventil wird ein **Grunddurchfluss** voreingestellt, der zur Heizlast des Raums passt. Dann ist bei voll geöffnetem Thermostat jeder Raum versorgt, und die Pumpe kann kleiner laufen.

Drei Stufen, aufsteigend im Aufwand:

| Verfahren | Was passiert | Wer | Beleg |
|---|---|---|---|
| **Thermischer Abgleich** (Näherung) | Alle Köpfe ab, Heizkurve so weit runter, bis der erste Raum zu kalt wird, dann überheizte Räume über die Ventile drosseln; 24-h-Schritte, wolkiger Tag | geübter Laie | `[Q26]` |
| **Verfahren A** | pauschale Tabellenwerte, Ventile nach Heizkörperleistung eingestellt — „sehr pauschal", Heizlast wird nicht genau geprüft | Fachbetrieb | `[Q21, 00:02:15]` |
| **Verfahren B** | raumweise Heizlast nach DIN EN 12831, daraus Volumenstrom je Heizkörper, Einstellung an voreinstellbaren Ventilen, schriftliches Protokoll | Fachbetrieb | `[Q21, 00:02:35–00:03:51]` |
| **Verfahren B+** | wie B, zusätzlich Absenkung der Systemtemperatur | Fachbetrieb | `[Q21, 00:04:22–00:04:45]` |

**Rechtlich:** Der hydraulische Abgleich ist beim Einbau/der Inbetriebnahme **gesetzlich Pflicht in Gebäuden mit mindestens sechs Wohnungen oder Nutzungseinheiten** (GEG § 60c Abs. 1) `[Q01]`. Im Einfamilienhaus ist er **nicht gesetzlich erzwungen** — aber:
- die Verbraucherzentrale nennt ihn „wichtig" für die Optimierung `[Q02]`,
- die Förderung verlangt seit **1.1.2023** ein Verfahren A oder B `[Q21, 00:02:35]`,
- ohne ihn bleibt jede Vorlaufabsenkung Stückwerk.

**Kosten:** Einfamilienhaus **ca. 925 €**, Spanne **650–1.250 €**; Mehrfamilienhaus 500 m²/5 WE ca. 5.000 €; BAFA-Zuschuss 15 % `[Q13]`.

**Kann ich das selbst?** Den thermischen Abgleich ja — mit Geduld und einem Thermometer. Das „richtige" Verfahren B nein: Es braucht die raumweise Heizlast und **voreinstellbare Ventile**. Wer alte, nicht voreinstellbare Ventile hat, kann nur thermisch arbeiten oder muss Ventile tauschen lassen. Im Forum wird genau das diskutiert — inklusive der Warnung, dass Smart-Home-Ventile, die alle gleichzeitig öffnen, „das komplette Gegenteil von hydraulischem Abgleich" sind `[Q26]`.

---

## 3. Fußbodenheizung nachrüsten

### 3.1 Systeme und Aufbauhöhe

| System | Aufbauhöhe | Gewicht | Kosten/m² | Geeignet für |
|---|---|---|---|---|
| **Nass** (Estrich) | **5–10 cm** `[Q12]` | hoch | **45–130 €** `[Q12]` | Kernsanierung, Neubau, Räume mit Fliesen |
| **Trocken** (Gipsfaser/Kunststoff, Wärmeleitbleche) | **4–5 cm ohne Dämmung** `[Q12]` | gering | **65–135 €** `[Q12]` | Altbau, Holzbalkendecke, schnelle Belegreife |
| **Dünnschicht** (Matten + Nivellierestrich) | **ca. 2 cm** `[Q12]` | gering | **30–100 €** `[Q12]` | wenn Höhe knapp, Estrich aber nass möglich |
| **Fräsen** (Kanäle in vorhandenen Estrich) | **0 bis wenige mm** `[Q12]` | unverändert | **30–120 €** `[Q12]` | massiver Estrich ≥ 40 mm, kein Holz |
| **Elektrisch** | sehr gering | sehr gering | **20–90 €** `[Q12]` | nur Bad/Teilfläche, hohe Betriebskosten |

Der BDH beschreibt die Systeme genauso: Trockensysteme mit vorgeformten Rillen und Wärmeleitblechen, Lastverteilung über zweilagigen Trockenestrich; Estrichfräsen nur bei **Zement- oder Anhydritestrich mit Mindeststärke 40 mm**, tragfähig und stabil `[Q06, Kap. 2.4.2–2.4.3]`.

**Fräsen** ist für viele Bestandsbauten die erste Wahl: kein Höhenaufbau, keine Türblattkürzung, kein Estrich-Abbruch. Die NDR-Reportage zeigt es: Belag raus, Fräse fräst Bahn für Bahn Kanäle, Rohr rein, Ausgleichsestrich drüber — „typischerweise nach zwei Tagen fertig" und „in der Regel sogar deutlich günstiger als der konventionelle Einbau" `[Q23, 00:01:06–00:02:38]`.

### 3.2 Holzbalkendecke: geht — aber nur trocken und nur mit Statik

Auf einer Holzbalkendecke ist **Nassestrich meist ausgeschlossen** (Gewicht, Feuchte). Der belegte Weg im Fachforum: alte Dielen runter, **Schutt/Schlacke aus den Balkenzwischenräumen raus**, dämmen, Balken nivellieren, **Folie als Gleitschicht** auf die Balken, dann **Dünnschicht-FBH mit 10–12 mm Rohr** darauf `[Q29]`. Das ist ein Trockenaufbau, kein Estrich.

Zwei harte Randbedingungen:
- **Statik**: Punktlasten und Gesamtgewicht der neuen Schichten müssen die Decke tragen. Das prüft der Zimmerer/Statiker, nicht der Heizungsbauer.
- **Höhe**: Im zitierten Fall lag 10 cm Gefälle im Raum — „ohne Schwellen" war der Aufbau nicht lösbar; am Ende blieb nur, die Balkenlage tiefer zu legen oder den Aufbau zu begrenzen `[Q29]`. Rechne damit, dass die Türblätter gekürzt oder die Türschwellen angepasst werden müssen.

### 3.3 Was es real kostet

- **Bandbreite:** 20–135 €/m² je nach System und Eigenleistung; für ein **130-m²-Einfamilienhaus 2.500–17.500 €** `[Q12]`. Die Spanne ist so groß, weil „Material bis Komplettpreis" enthalten ist — vergleiche nie eine Materialzahl mit einem Komplettangebot.
- **Realbeispiel aus einem Sanierungsforum (Österreich):** FBH im Bestand mit nur **2,5 cm Auftrag** möglich, „deswegen so teuer, weil wir aufgrund des Bestands nur 2,5 cm auftragen können" — Angebote für Heizkörper EG + FBH OG: **23.000 €**, FBH auch im EG: **30.000 €**, zusätzlich Luftwärmepumpe: **35.000 €** (vor Förderung) `[Q33]`. Das ist kein Preisvergleich, sondern ein Beleg dafür, wie stark die Randbedingungen den Preis treiben.
- **Dämmung ist kein Extra, sondern Norm:** Die Mindest-Wärmedurchlasswiderstände unter den Rohren fordert **DIN EN 1264-4**: Rλ **0,75 bis 2,00 m²K/W**, je nach angrenzendem Raum und Auslegungs-Außentemperatur `[Q06, Kap. 3.2.3]`. Wer die Dämmung weglässt, heizt die Kellerdecke.

### 3.4 Wann FBH nachrüsten sinnvoll ist — und wann nicht

**Sinnvoll, wenn:**
- ohnehin ein neuer Bodenaufbau ansteht (Kernsanierung, neuer Estrich, Fliesen),
- eine Wärmepumpe kommt und du die Vorlauftemperatur auf 35–45 °C drücken willst (`[Q11]`: gut gedämmte Häuser mit FBH „oft sehr effizient mit etwa 35 °C"),
- das Bad oder einzelne Räume ohnehin geöffnet werden.

**Nicht sinnvoll, wenn:**
- nur „Energie sparen" das Ziel ist und der Boden bleibt — dann ist der Heizkörper-/Abgleich-Pfad billiger,
- die Aufbauhöhe Türen, Treppe oder Steckdosen zerstört,
- die Decke die Last nicht trägt und ein Verstärken der Balken nicht in Frage kommt.

---

## 4. Lüften: Fenster, dezentral, zentral

### 4.1 Fensterlüftung — die Zahlen, die zählen

- Winter, niedrige Außentemperatur/Wind: **3–5 Minuten** Stoß-/Querlüften `[Q03]`.
- Frühjahr/Herbst: **10–20 Minuten** für den kompletten Luftaustausch `[Q03]`.
- Mindestens **3–4 Mal pro Tag** die Luft komplett austauschen `[Q03]`.
- Nach Duschen, Baden, Kochen, Schlafen **sofort** lüften `[Q03]`.
- Ziel: Luftfeuchte **dauerhaft unter 50 %** `[Q03]`.
- Ein **Vier-Personen-Haushalt** gibt **6–12 Liter Wasser pro Tag** an die Raumluft ab `[Q05]`.

Das ist die Baseline. Alles Weitere ist Komfort, Feuchteschutz bei Abwesenheit — oder teuer.

### 4.2 Die drei Systeme im Vergleich

| System | Aufbau | Kosten EFH | Wärmerückgewinnung | Nachrüstbar | Wartung |
|---|---|---|---|---|---|
| **Abluft** (Bad/Küche) | Ventilator + Außenluftdurchlässe | gering (nicht separat belegt) | nein | einfach | Filter |
| **Dezentral** (je Raum ein Gerät, paarweise Pendellüfter) | Kernbohrung + Strom, kein Rohrnetz | Geräte ab **250 €**, komplette Ausstattung **5.000–10.000 €** `[Q16]` | ja | **am einfachsten** `[Q04]` | Filter, mehr Aufwand `[Q04]` |
| **Zentral** (Zu-/Abluft mit Kanälen) | Gerät + Verteilsystem | **8.000–15.000 €** inkl. Einbau `[Q16]`; Material 6.000–9.000 €, Einbau 2.500–6.000 € `[Q14]` | **bis 90 % und mehr** `[Q04]` | aufwendig, im Bestand schwer `[Q04]` | Filter **40–90 €/a**, Kanalreinigung **400–800 €** alle ~10 Jahre `[Q04]` |

Betriebskosten: Strom **ca. 300 kWh/a ≈ 90 €/a** bei 30 ct/kWh `[Q04]`; eine andere Quelle nennt **60–120 €/a Strom + 100–300 €/a Filter/Wartung** `[Q16]`. Beides sind Schätzungen für ein EFH, keine Messwerte.

Planungsdetails, die man später nicht mehr korrigiert `[Q04]`:
- Ventilator- und Strömungsgeräusche **unter 25 dB** auslegen.
- Zentralgerät **nicht an Schlafräume angrenzen** lassen.
- **Revisionsöffnungen** für alle Kanäle vorsehen — sonst wird nie gereinigt.
- Bei innenliegenden Bädern ohne Fenster gilt **DIN 18017-3**, nicht DIN 1946-6 `[Q04]`.

### 4.3 Lüftungskonzept nach DIN 1946-6

**Wann:** „Für Neubauten und sanierte Altbauten ist ein Lüftungskonzept erforderlich. Das gilt für alle Sanierungen, bei denen **mehr als ein Drittel der Fensterfläche** erneuert wird und für sanierte Einfamilienhäuser und Dachgeschosswohnungen, wenn das **Dach saniert** wird" `[Q04]`. Norm: **DIN 1946-6:2019-12** `[Q04]`.

**Was es leistet:** Es weist nach, dass die Wohnung auch bei Abwesenheit und geschlossenen Fenstern genug Luftwechsel für den **Feuchteschutz** hat — oder dass technische Lüftung nötig ist. Die Norm kennt vier Stufen: Lüftung zum Feuchteschutz, reduzierte Lüftung, Nennlüftung, Intensivlüftung `[Q04]`.

**Kosten:** **300–400 €** für Ein-/Zweifamilienhaus `[Q04]`.

**Der Streitpunkt, den du kennen musst:** Die DIN 1946-6 ist **keine baurechtlich eingeführte Norm** — sagt ein Energieberater im Video ausdrücklich: „das bedeutet, sie ist nicht verpflichtend" `[Q25, 00:03:19–00:03:25]`. Die Verbraucherzentrale formuliert dagegen „erforderlich" `[Q04]`. Beides ist vereinbar: **Unmittelbar erzwingt sie keine Behörde; geschuldet ist der Nachweis über die anerkannten Regeln der Technik und über den Werkvertrag.** Praktisch heißt das: Verlange das Konzept vom ausführenden Betrieb oder von einem Energieberater — die Verantwortung für den Nachweis und für die Feuchte im Haus bleibt bei dir als Bauherrn.

**Warum das kein Papier ist:** Im Forum schildert ein Bauherr genau den Fall — Energieberater warnt, dass nach Einbau dichter Fenster (Ug 1,1) die **Wand der kälteste Punkt** wird und Kondensat/Schimmel droht; der Fensterbauer sagt, das Risiko bestehe „nur bei noch stärker dämmenden Fenstern" `[Q32]`. Der Konflikt ist typisch: Der eine verkauft Fenster, der andere haftet für die Feuchte. Ohne Lüftungskonzept fehlt die Instanz, die das entscheidet.

### 4.4 KWL einregulieren (der „pneumatische Abgleich")

Ohne Einregulierung ist eine KWL eine teure Zufallslüftung: Bad bekommt zu viel, Schlafzimmer zu wenig. So wird es gemacht `[Q31]`:
- **Gesamtvolumenstrom am Gerät** einstellen (Stufe/Prozent).
- **Raumvolumenströme an den Tellerventilen** in den Räumen — nicht am Verteiler („die Einstellungen am Verteiler sind eher selten anzutreffen") `[Q31]`.
- Messen mit Flügelrad-Anemometer oder Balometer; Sollwerte aus dem Lüftungskonzept.
- **Filter** jährlich, bei Bedarf halbjährlich; Kanäle nach Inspektion.

Ohne Messgerät keine Einregulierung. Wer „nach Gefühl" dreht, stellt nur die Geräusche anders ein.

---

## 5. Optimieren ohne Tausch — die Reihenfolge

| # | Maßnahme | Aufwand | Wirkung | Beleg |
|---|---|---|---|---|
| 1 | **Alle Thermostatköpfe prüfen** (Stift gangbar, Kopf nicht überdreht, nicht durch Möbel blockiert) | 30 min | hoch, kostenlos | `[Q19]` |
| 2 | **Heizkurve/Vorlauf absenken** in 1–2-K-Schritten, je 2–3 Tage, bis der kälteste Raum nicht mehr mitkommt, dann einen Schritt zurück | 1–2 Wochen | hoch | `[Q02][Q11]` |
| 3 | **Pumpe** auf hocheffiziente Pumpe / niedrigste ausreichende Stufe; keine Rauschgeräusche, keine voll geöffneten Ventile nötig | 1 h (Fachbetrieb) | mittel | `[Q02]` |
| 4 | **Heizkörpernische dämmen** (Dämmplatte + Alu-Folie) | 1–2 h/Körper | mittel, lokal | `[Q18]` |
| 5 | **Rohrleitungen in unbeheizten Räumen dämmen** | 1–2 h | mittel | `[Q02]` |
| 6 | **Hydraulischer Abgleich** | 1 Tag Fachbetrieb | hoch | `[Q13][Q21]` |
| 7 | **Nachtabsenkung** — nur bei Kessel + Heizkörpern sinnvoll | 10 min | gering bis mittel | `[Q02]` |

**Wichtig zur Nachtabsenkung:** Die Verbraucherzentrale schreibt ausdrücklich, dass bei **Wärmepumpen oder Fußbodenheizung** eine starke Absenkung oder Abschaltung wenig bringt, den Komfort senkt „und meistens sogar der Effizienz" schadet `[Q02]`. Wer mit FBH nachts 5 K absenkt, heizt morgens mit schlechterem COP nach.

**Heizkörpernische — die Zahlen:** Der Energiesparkommissar misst an einem ~55 °C warmen Heizkörper in einer Nische: Der Wärmeverlust sinkt **ohne Alu-Beschichtung um etwa ein Drittel**, **mit Beschichtung um über 41 %** `[Q18, 00:03:56–00:04:11]`. Mit zwei Dämm-Lagen und Folie kommt er auf **~44 %** Verlustreduktion, ohne Nische (flache Wand) auf **~35 %**, mit nur **einer** Lage nur **~25 %** `[Q18, 00:07:39–00:14:17]`. Das sind Kanal-Messungen, keine unabhängige Studie — die Größenordnung ist aber plausibel und deckt sich mit dem physikalischen Mechanismus (Strahlung + Konvektion hinter dem Körper).

**Merksatz:** Nische dämmen wirkt nur **mit** Reflexionsfolie richtig; Luftpolsterfolie ohne Kaschierung bringt deutlich weniger `[Q18, 00:02:21–00:03:30]`.

---

## 6. Typische Fehler — Symptom, Ursache, Beleg, Abhilfe

### 6.1 Heizkörper zu klein ausgelegt
**Symptom:** Raum wird bei Volllast nicht warm, Rücklauf kalt, Ventil voll offen.
**Ursache:** Leistung bei 75/65/20 gekauft, Anlage läuft 55/45 oder tiefer → nur 51 % bzw. 40 % der Nennleistung (Tabelle §1.2) `[Q38][Q10]`.
**Abhilfe:** raumweise Heizlast `[Q28]`, größerer Typ (33 statt 22) oder mehr Baulänge; nicht die Vorlauftemperatur hochdrehen, wenn eine Wärmepumpe geplant ist `[Q10]`.

### 6.2 Luft im System — aber falsch entlüftet
**Symptom:** Gluckern, vorne heiß/hinten kalt `[Q20]`.
**Ursache:** Pumpe läuft beim Entlüften, nur der oberste Heizkörper wird entlüftet, Druck danach nicht geprüft `[Q22]`.
**Abhilfe:** Pumpe aus, alle Köpfe auf, von oben nach unten, bis Wasser kommt, Druck 1–2 bar `[Q22][Q39]`. Wiederholt sich das → Undichtigkeit/Sauerstoffeintrag suchen `[Q39][Q36]`.

### 6.3 Falsche oder falsch eingestellte Ventile nach dem Tausch
**Symptom:** Nach Ventiltausch wird ein großer Heizkörper nur **oben** warm; alle anderen Heizkörper sind zu.
**Ursache (laut Fachforum, in dieser Reihenfolge prüfen):** Rücklaufverschraubung noch (fast) zu; **Voreinstellung** am neuen Ventil zu niedrig; Ventilstößel schwergängig `[Q27]`. Der Installateur im Thread argumentierte mit „Pumpe zu schwach" — im geschlossenen Kreis ist die Höhe irrelevant, die Pumpe überwindet nur Reibung; ein zusätzlicher Widerstand durch das neue Ventil ist die plausiblere Erklärung `[Q27]`.
**Abhilfe:** Rücklauf öffnen, Voreinstellung auf max. Durchfluss, Stößel prüfen; notfalls Ventil eine Nummer größer.

### 6.4 FBH ohne (ausreichende) Dämmung
**Symptom:** Räume werden träge warm, Heizkosten hoch, Kellerdecke warm.
**Ursache:** Dämmung gespart; die Wärme geht nach unten.
**Beleg:** DIN EN 1264-4 fordert Mindest-Wärmedurchlasswiderstände **0,75–2,00 m²K/W** unter den Rohren, je nach angrenzendem Raum `[Q06, Kap. 3.2.3]`. co2online nennt als Nachteil des Nasssystems ausdrücklich das hohe Gewicht und die Notwendigkeit, im Altbau zu dämmen `[Q12]`.

### 6.5 KWL ohne Einregulierung
**Symptom:** Bad trocknet nicht, Schlafzimmer riecht „abgestanden", Anlage rauscht in einem Raum.
**Ursache:** Nur Gesamtvolumen am Gerät eingestellt, Tellerventile nie gemessen `[Q31]`.
**Abhilfe:** Luftmengenprotokoll verlangen (Soll/Ist je Raum), mit Anemometer nachmessen.

### 6.6 Lüftungskonzept fehlt nach Fenstertausch
**Symptom:** Nach neuen Fenstern Schimmel in Ecken/Laibungen, Fenster „schwitzen".
**Ursache:** Gebäude wird dicht, der Luftwechsel bricht weg, die Wand wird kältester Punkt `[Q32][Q04]`.
**Abhilfe:** Konzept nach DIN 1946-6 (300–400 €) `[Q04]`; technische Lüftung oder definierte Außenluftdurchlässe; Feuchte messen.

### 6.7 „Abgleich" nur durch Pumpendrosseln
**Symptom:** Anlage wird leiser, aber einzelne Räume bleiben kalt.
**Ursache:** Pumpenstufe ist kein Abgleich — die Verteilung ändert sich nicht `[Q26]`.
**Abhilfe:** thermischer Abgleich oder Verfahren B `[Q21][Q26]`.

### 6.8 Nachtabsenkung bei FBH/Wärmepumpe
**Symptom:** Morgens lange Aufheizzeit, Verbrauch steigt.
**Ursache:** Träge Masse, schlechterer COP beim Wiederaufheizen `[Q02]`.
**Abhilfe:** Absenkung klein halten (1–2 K) oder ausschalten.

### 6.9 Nur Folie in die Nische kleben
**Symptom:** Kaum messbare Wirkung.
**Ursache:** Reflexion allein reicht nicht; Dämmung + Folie zusammen `[Q18]`.
**Abhilfe:** Dämmplatte plus kaschierte Folie, zwei Lagen, sauber absaugen und staubfrei verkleben `[Q18, 00:08:13–00:09:42]`.

---

## 7. Kosten und Zeit — Tabelle mit Quellen

| Position | Bandbreite | Quelle | Anmerkung |
|---|---|---|---|
| Heizkörper (Material) | **100–1.000 €/Stk** | `[Q15]` | Platten 100–300 €, Glieder 250–400 €, Design/Bad höher |
| Heizkörper tauschen inkl. Einbau | **300–700 €/Stk** | `[Q15]` | kompletter Austausch, nicht nur Material |
| Ventileinsatz | **~30 €/Stk** + 1–2 h | `[Q37]` | Forumsschätzung, Heimeier-Beispiel |
| Hydraulischer Abgleich EFH | **650–1.250 €**, Mittel **~925 €** | `[Q13]` | BAFA 15 % Zuschuss |
| Hydraulischer Abgleich MFH 500 m²/5 WE | **~5.000 €** | `[Q13]` | vor Förderung |
| FBH nachrüsten | **20–135 €/m²** | `[Q12]` | Systemabhängig, Tabelle §3.1 |
| FBH EFH 130 m² | **2.500–17.500 €** | `[Q12]` | Material bis Komplettpreis |
| Lüftungskonzept DIN 1946-6 | **300–400 €** | `[Q04]` | EFH/ZFH |
| KWL zentral EFH | **8.000–15.000 €** | `[Q16]` | inkl. Installation; 50–70 €/m² Wohnfläche |
| KWL dezentral EFH | **5.000–10.000 €** | `[Q16]` | Geräte ab 250 € |
| KWL Betrieb | **60–120 €/a Strom**, **100–300 €/a Wartung** | `[Q16]` | andere Quelle: 90 €/a Strom, 40–90 €/a Filter `[Q04]` |
| Kanalreinigung | **400–800 €** alle ~10 Jahre | `[Q04]` | nach Inspektion |

**Zeit:**
- Heizkörpertausch: **1–2 h pro Stück** (Erfahrungswert; BDH zeigt den Ablauf ohne Zeitangabe `[Q08]`).
- FBH fräsen: **~2 Tage** für eine Wohnung `[Q23]`.
- Hydraulischer Abgleich: **~1 Tag** (Erfahrungswert; Verfahren B inkl. Protokoll).
- KWL-Einbau: **mehrere Tage** (Erfahrungswert; im Bestand deutlich länger als Neubau).

**Rechenregel:** Immer **Band** kommunizieren, nie Punktpreis. Ein Angebot ohne Positionen („Heizung komplett 12.000") ist nicht vergleichbar — nach Material, Stunden und Nebenpositionen aufschlüsseln lassen.

---

## 8. Angebots- und Pfusch-Checkliste (10 Fragen an den Fachbetrieb)

1. **Raumweise Heizlast** nach DIN EN 12831 — liegt sie vor, oder wird nach m² geschätzt? `[Q10][Q28]`
2. **Auslegungstemperatur** (VL/RL) und **Leistung bei dieser Temperatur** — nicht nur Katalogwert 75/65 `[Q38]`.
3. **Heizkörpertyp, Bauhöhe, Länge, Nabenabstand** — passt er auf die vorhandenen Anschlüsse ohne Stemmarbeiten? `[Q08]`
4. **Voreinstellwerte** je Ventil und **Abgleich-Protokoll** (Verfahren A oder B) `[Q21]`.
5. **Druckprobe/Dichtheitsprüfung** und Protokoll nach Abschluss.
6. **Entlüftung + Druck** nach Inbetriebnahme, schriftlich `[Q22][Q39]`.
7. Bei FBH: **Dämmung nach DIN EN 1264-4** mit Rλ-Wert im Angebot `[Q06]`.
8. Bei KWL: **Lüftungskonzept** und **Luftmengenprotokoll** je Raum `[Q04][Q31]`.
9. **Schallschutz** (< 25 dB) und **Revisionsöffnungen** bei KWL `[Q04]`.
10. **Gewährleistung**: 5 Jahre bei Bauwerk (BGB § 634a Abs. 1 Nr. 2 `[Q41]`), bei VOB/B 4 Jahre — nicht „2 Jahre Garantie" akzeptieren.

**Pfusch-Signale:** „brauchen wir nicht", „machen wir immer so", kein Protokoll, kein Messgerät im Auto, Pauschalpreis ohne Positionen, Heizkörper „gleiche Größe" ohne Heizlast, KWL „läuft doch".

---

## 9. Quellen (alle am 09.11.2026 abgerufen und geprüft)

**Gesetz / Norm**
- `[Q01]` **GEG § 60c** — Hydraulischer Abgleich und weitere Maßnahmen zur Heizungsoptimierung, Abs. 1: Gebäude mit mindestens sechs Wohnungen/Nutzungseinheiten. https://www.gesetze-im-internet.de/geg/__60c.html (Volltext geprüft; Fassung mit Stand 2026)
- `[Q40]` **HwO Anlage A Nr. 24** — „Installateur und Heizungsbauer" als zulassungspflichtiges Handwerk. https://www.gesetze-im-internet.de/hwo/anlage_a.html (Volltext geprüft)
- `[Q41]` **BGB § 634a Abs. 1 Nr. 2** — Verjährung „in fünf Jahren bei einem Bauwerk". https://www.gesetze-im-internet.de/bgb/__634a.html (Volltext geprüft)

**Verbraucherzentrale**
- `[Q02]` Verbraucherzentrale, „Heizung optimieren und Heizkosten sparen – so geht's", Stand 08.10.2026. https://www.verbraucherzentrale.de/wissen/energie/heizen-und-warmwasser/heizung-optimieren-und-heizkosten-sparen-so-gehts-30096 — Hydraulischer Abgleich „wichtig", Pumpe/Regelung, Nachtabsenkung bei WP/FBH kontraproduktiv, Rohrdämmung DIY.
- `[Q03]` Verbraucherzentrale, „Heizen und Lüften: So geht's richtig". https://verbraucherzentrale.de/wissen/energie/strom-sparen/heizen-und-lueften-so-gehts-richtig-10426 — 3–5 min (Winter), 10–20 min (Übergang), 3–4×/Tag, < 50 % rF.
- `[Q04]` Verbraucherzentrale, „Was müssen Sie für die Planung einer Lüftungsanlage wissen?" https://verbraucherzentrale.de/wissen/energie/energetische-sanierung/was-muessen-sie-fuer-die-planung-einer-lueftungsanlage-wissen-5411 — Lüftungskonzept > 1/3 Fensterfläche, DIN 1946-6:2019-12, 4 Lüftungsstufen, 90 % WRG, < 25 dB, Kosten 300–400 €, Filter 40–90 €/a, Reinigung 400–800 €/10 a.
- `[Q05]` Verbraucherzentrale, „Richtiges Heizen und Lüften – die beste Strategie gegen Schimmel". https://verbraucherzentrale.de/energiebildung-fuer-ukrainerinnen/heizen-lueften-schimmel — 4-Personen-Haushalt 6–12 L Wasser/Tag.

**Verbände / Hersteller**
- `[Q06]` BDH, Informationsblatt Nr. 51, Teil 2 „Fußbodenheizung/-kühlung – Modernisierung", Oktober 2024. https://www.bdh-industrie.de/fileadmin/user_upload/Downloads/Infoblaetter/Infoblatt_Nr_51_2_10-2024_Fussbodenheizung_-kuehlung.pdf — Trockensysteme mit Wärmeleitblechen, Estrichfräsen nur ≥ 40 mm, DIN EN 1264-4 Mindest-Rλ 0,75–2,00 m²K/W.
- `[Q08]` BDH (Bundesverband der Deutschen Heizungsindustrie), „Heizkörpertausch – Einfacher Austausch in 6 Schritten", 05.03.2015. https://www.youtube.com/watch?v=O9NBXhXhF4g — 6 Schritte, passende Anschlussvariante, keine Stemmarbeiten bei maßgleichem Körper, Entlüften am Ende.
- `[Q10]` BWP, „Gehört zu einer Wärmepumpe immer auch eine Fußbodenheizung?" (FAQ der Experten), 23.08.2023. https://www.waermepumpe.de/verbraucher/darum-waermepumpe/fragen-sie-die-experten/antwort-der-experten/gehoert-zu-einer-waermepumpe-immer-auch-eine-fussbodenheizung/ — Vorlauf ≤ 50 °C, Radiatoren prüfen, oft reicht Tausch einzelner Radiatoren, Heizlast nach DIN EN 12831.
- `[Q11]` Vaillant, „Vorlauftemperatur: Die Heizung optimal einstellen". https://vaillant.de/ratgeber/heizungstipps/vorlauftemperatur — FBH ~35 °C in gut gedämmten Häusern; ältere, schlecht gedämmte Gebäude mit kleinen Heizkörpern 55–90 °C.
- `[Q39]` Viessmann, „Heizung entlüften – Anleitung und Tipps". https://viessmann.de/de/wissen/anleitungen-und-tipps/heizung-entlueften.html — Vierkantschlüssel, keine Zange (Runddrehen), Druck prüfen, 1 h laufen lassen, wiederholtes Entlüften = tieferliegendes Problem.

**Verbraucherportale / Fachbetriebe**
- `[Q12]` co2online, „Fußbodenheizung nachrüsten: Kosten & Methoden", 09.09.2026. https://co2online.de/modernisieren-und-bauen/heizung/fussbodenheizung/fussbodenheizung-nachruesten — Kostentabelle je System, Aufbauhöhen Nass 5–10 cm / Trocken 4–5 cm / Dünnschicht ~2 cm / Fräsen 0–mm, 130 m² = 2.500–17.500 €, Statik bei Holzbalkendecken.
- `[Q13]` co2online, „Hydraulischer Abgleich: Kosten, Nutzen & Förderung". https://www.co2online.de/energie-sparen/heizenergie-sparen/hydraulischer-abgleich/ — EFH ~925 € (650–1.250 €), MFH 500 m²/5 WE ~5.000 €, BAFA 15 %.
- `[Q14]` co2online, „Lüftungsanlagen: Arten, Kosten, Vor- & Nachteile". https://www.co2online.de/energie-sparen/heizenergie-sparen/lueften-lueftungsanlagen-fenster/lueftungsanlagen/ — Planung 400–600 €, Material 6.000–9.000 €, Einbau 2.500–6.000 €, Wartung 50–100 €/a, Reinigung 150–400 € alle 2–5 Jahre.
- `[Q15]` heizsparer, „Heizkörper Kosten – damit sollten Sie rechnen". https://www.heizsparer.de/heizung/heizkorper/heizkoerper-kosten — 100–1.000 € Material, 300–700 € komplett inkl. Einbau, Typenpreise.
- `[Q16]` heizsparer, „Wohnraumlüftung Kosten". https://www.heizsparer.de/lueftungsanlage/kosten-einer-wohnraumlueftung — zentral 8.000–15.000 €, dezentral 5.000–10.000 €, Geräte ab 250 €, Strom 60–120 €/a, Wartung 100–300 €/a.
- `[Q17]` heizung.de, „Heizkörper streichen in 4 Schritten". https://www.heizung.de/ratgeber/heizkoerper/in-4-schritten-die-heizkoerper-streichen.html — 4 Schritte, Abbau nicht nötig, Untergrund vorbehandeln.
- `[Q38]` Kolboske (SHK-Fachbetrieb), „Dimensionierung von Platten- und Kompakt-Heizkörpern", 16.10.2015 (PDF). http://www.kolboske.de/joomla/files/ue/hz/hz_auslegung_von_platten_und_kompacktheizkoerpern_kurz_und_knapp.pdf — Typ 22 = 2 Platten + 2 Lamellen, Leistungstabellen 75/65, 70/55, 55/45, Korrekturfaktor bei abweichender Raumtemperatur.

**YouTube (deutsch, Untertitel selbst ausgewertet)**
- `[Q18]` ENERGIESPARKOMMISSAR, „DIY – Heizkörpernische dämmen", 18.07.2022. https://www.youtube.com/watch?v=lXi1KO4XOZc — bei ~55 °C: Verlust −1/3 ohne Alu, > 41 % mit Alu; 2 Lagen ~44 %, ohne Nische ~35 %, eine Lage ~25 % (Auto-Untertitel, Minutenangaben ±10 s).
- `[Q19]` ENERGIESPARKOMMISSAR, „Dumme und Smarte Heizkörper Thermostate", 17.05.2025. https://www.youtube.com/watch?v=kpzwJ8QA8GI — Aufbau Handventil vs. Thermostatventil, Stift klemmt, Kopf ab, Stift gangbar machen.
- `[Q20]` SHK Info, „Heizkörper entlüften – so geht's richtig", 30.11.2018. https://www.youtube.com/watch?v=l6vwmYvfg0I — Luft: vorne heiß/hinten kalt + Gluckern; oben warm/unten kühler ist normal bis 20 K.
- `[Q21]` SHK Info, „Hydraulischer Abgleich für die Heizungsförderung", 26.03.2023. https://www.youtube.com/watch?v=6d6hTbtFdJs — Verfahren A pauschal, B nach DIN EN 12831, B+ mit Temperaturabsenkung, Förderung seit 1.1.2023.
- `[Q22]` Mac Paverick, „Heizkörper richtig entlüften – Oft wird ein wichtiges Detail vergessen!", 21.09.2022. https://www.youtube.com/watch?v=O1V83XMTG3Q — Pumpe aus, alle auf, oben anfangen, Druck 1–2 bar; Kanal behauptet „bis zu 15 % Einsparung" (unbelegt).
- `[Q23]` NDR Info, „Heizung im Altbau: Fußbodenheizung einfräsen lassen?", 02.01.2026. https://www.youtube.com/watch?v=7xq4pUOX4l8 — Fräsen in vorhandenen Estrich, gleiche Höhe, ~2 Tage, meist günstiger als konventionell.
- `[Q24]` Bauhelden, „Fußbodenheizung nachrüsten im Trockenbau – Schritt für Schritt", 07.12.2025. https://www.youtube.com/watch?v=wRJOrHfH65E — Trockenaufbau, Höhenlage ~18 mm im gezeigten Fall (DIY-Kanal, keine Normaussage).
- `[Q25]` ARCenergie (Energieberater), „Lüftungskonzept DIN 1946-6: Ist das Pflicht oder nur Kür?", 07.03.2025. https://www.youtube.com/watch?v=cIDLFtLBeMc — 1/3 der Fenster bzw. 2/3 Dachfläche; DIN 1946-6 „keine baurechtlich eingeführte Norm", Verantwortung beim Ausführenden.

**Foren**
- `[Q26]` HaustechnikDialog, „Ist ein hydraulischer Abgleich in Eigenregie für Laien zu bewältigen?", 21.–26.11.2018. https://www.haustechnikdialog.de/Forum/t/212501/ — thermischer Abgleich als Näherung (Köpfe ab, Heizkurve runter, 24-h-Schritte), Smart-Home-Ventile kontraproduktiv.
- `[Q27]` HaustechnikDialog, „Heizkörper wird nach Ventilaustausch nicht warm genug", 08.–11.11.2024. https://www.haustechnikdialog.de/Forum/t/281579/ — nur obere Hälfte warm; Prüfreihenfolge Rücklaufverschraubung, Voreinstellung, Stößel; „Pumpe zu schwach" als Fehldiagnose.
- `[Q28]` HaustechnikDialog, „Heizkörper TYP 22 oder 33", 26.–29.03.2025. https://www.haustechnikdialog.de/Forum/t/285831/ — „Heizlastberechnung machen! Alles andere kommt nur von der Glaskugel"; größerer Typ für WP.
- `[Q29]` HaustechnikDialog, „FH auf schiefem Holzboden", 03.07.–16.08.2007. https://www.haustechnikdialog.de/Forum/t/67836/ — Holzbalkendecke: Dielen raus, Schüttung raus, dämmen, nivellieren, Folie, Dünnschicht-FBH 10–12 mm; 10 cm Gefälle.
- `[Q30]` HaustechnikDialog, „60er Jahre Altbau, quo vadis? Oder: Brennwert vs. WP", 12.–20.03.2024. https://www.haustechnikdialog.de/Forum/t/275879/ — realer Aufbau FBH EG/OG „ca. 9–10 cm" (EPS-Schüttung 2–4 cm, Noppenplatte, Estrich, Vinyl).
- `[Q31]` HaustechnikDialog, „KWL – pneumatischer Abgleich – wo Luftmengen einstellen?", 22.–28.03.2019. https://www.haustechnikdialog.de/Forum/t/216394/ — Gesamtmenge am Gerät, Raummenge an Tellerventilen, Verteiler selten.
- `[Q32]` HaustechnikDialog, „Neue Fenster im Altbau – Schimmelgefahr", 06.05.2010 ff. https://www.haustechnikdialog.de/forum/t/119651/ — Energieberater warnt vor Schimmel, weil die Wand kältester Punkt wird; Fensterbauer widerspricht.
- `[Q33]` energiesparhaus.at, „Radiatoren tauschen? FBH? Vielleicht sogar LWP?", 02.–04.09.2020. https://www.energiesparhaus.at/forum-radiatoren-tauschen-fbh-vielleicht-sogar-lwp/58980 — im Bestand nur 2,5 cm Aufbau möglich, Angebote 23.000/30.000/35.000 € (AT, vor Förderung).
- `[Q34]` energiesparhaus.at, „Ventileinsatz für Heizkörper BJ ~1985 (alte MMA Ventile)", 12.01.–29.11.2022. https://www.energiesparhaus.at/forum/66102 — Adapterproblem M28×1,5/MMA, Stift gangbar machen mit WD40, Einsatz nur durch Vergleich alt/neu bestimmbar.
- `[Q37]` r/handwerk, „Austausch Heizkörper Ventile". https://www.reddit.com/r/handwerk/comments/1xkz2ul/ — Kostenschätzung < 500 € für 6 Ventile bei Heimeier, 1–2 h, 30 €/Einsatz (Nutzerangaben, keine Rechnung).

**Reddit (Vergleich)**
- `[Q35]` r/Handwerker, „Entlüftungsventil tauschen", 19.10.2023. https://www.reddit.com/r/Handwerker/comments/17bq41b/ — DIY-Versuch: Vor-/Rücklauf abgesperrt, trotzdem Druck auf dem Körper; Antwort: eines der Ventile ist defekt, Heizkörper abkühlen lassen und prüfen, welches warm wird.
- `[Q36]` r/HVAC, „Single radiator works for 2 days if I drain it and then stops", 2018. https://www.reddit.com/r/HVAC/comments/7vhf8s/ — nur als Vergleich: Luft steigt nach oben, manuelles Entlüften am höchsten Punkt; automatische Entlüfter = Leckrisiko; diffusionsoffene PEX als Ursache für Lufteintrag.

---

## Ergänzungen aus dem Video-Gegencheck (09.11.2026)

- **Jeder Raum braucht eine eigene Heizfläche**, auch Ankleide, Abstellraum und Hauswirtschaftsraum:
  **GEG § 63** verlangt raumweise Regelung; die Ausnahme gilt nur für kleine Flächen mit
  Flächenheizung (< 6 m²). Wer die Ankleide an einen Nachbarraum hängt, heizt sie im Winter nicht —
  und der Schimmel kommt zuerst in der Ecke.

## 10. Unbelegt / offen (bewusst nicht als Fakt verkauft)

- **„15 % Heizenergie durch Entlüften"** stammt aus dem Mac-Paverick-Video `[Q22]` und ist dort nicht belegt. Plausibel ist ein Effekt nur, wenn die Anlage tatsächlich Luft hat — nicht als Dauerersparnis.
- **Nischen-Prozente (25/35/41/44 %)** sind Messungen des Kanals Energiesparkommissar `[Q18]`, keine unabhängige Studie; die Randbedingungen (55 °C, spezielle Folie, zwei Lagen) sind nicht auf jede Nische übertragbar.
- **Kostenbänder** von co2online, heizsparer und Verbraucherzentrale sind Marktbeobachtungen, keine Rechnungen. Regionale Unterschiede ±30 % sind normal.
- **r/Selbstbau**: Die Recherche ergab keinen belastbaren Thread zum Thema Heizung/Lüftung; deshalb wird das Subreddit hier nicht zitiert. r/Handwerker und r/handwerk decken die deutsche DIY-Perspektive ab.
- **„Heizkörper entkalken"**: Für geschlossene Heizkreise gibt es keine belastbare Quelle, dass Kalk die Ursache ist; die belegten Themen sind Luft, Schlamm und Ventile. Deshalb steht in §2.2 bewusst die Gegenaussage.
- **DIN-Volltexte** (1946-6, EN 1264-4, EN 12831) sind kostenpflichtig. Belegt sind Nummer, Titel, Ausgabe und die zitierte Sekundärstelle — nicht der Normtext selbst.
- **Zeitangaben** (1–2 h/Heizkörper, 1 Tag Abgleich) sind Erfahrungswerte ohne Quelle.
