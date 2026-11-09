# Dachentwässerung, Regenwasser, Garage — Playbook für Eigenheimbesitzer

**Für wen:** Bestandsbau, Eigenheim, kein Planer im Haus. Ton: Werkstatt, nicht Hörsaal.
**Stand:** 09.11.2026. Alle Zahlen mit Quelle `[Qn]` → Quellenverzeichnis am Ende. Was ich **nicht** belegen konnte, steht ausdrücklich als *unbelegt* da.

> **Preisstand 09/2026.** Alle Preise sind Orientierungswerte inkl. MwSt. aus den genannten Quellen —
> regional verschieden, keine Angebote. Wer später damit rechnet, prüft sie neu.

## Kurzantwort

- **Rinne bemessen, nicht schätzen:** NG 250 trägt bei r = 300 l/(s·ha) rund **86 m²**, NG 333 rund **155 m²**, NG 400 rund **250 m²** Dachgrundfläche — pro Ablauf, nicht pro Haus [Q5]. Marley-Grenzen: RG 100 bis 51 m², RG 125 bis 100 m², RG 150 bis 159 m² (bei 300 l/(s·ha)) [Q6].
- **Gefälle 2–3 mm/m** (2–3 cm auf 10 m), Rinneneisen alle **50–70 cm** [Q6][Q7]. Wer 5 mm/m legt, verliert Höhe am Fallrohr, gewinnt aber Sicherheit bei langen Rinnen — *Einschätzung*.
- **Das Fallrohr ist der Engpass, nicht die Rinne.** Zylindrischer Einlauf ohne Trichter kostet **~30 %** Abflussvermögen [Q5][Q3]; ein eingelöteter Stutzen statt Einhängstutzen erzeugt den „Badewanneneffekt" [Q29].
- **Versickerung ist Gewässerbenutzung** und braucht die wasserrechtliche Erlaubnis, außer NWFreiV + TRENGW greifen [Q11]. Unterirdische Rigolen brauchen **zwingend eine Vorreinigung**, Sickerschächte sind Ausnahme [Q11].
- **Überflutungsnachweis** nach DIN 1986-100: Beispiel-Kommune verlangt ihn ab **800 m²** abflusswirksamer Fläche, Nachweis 30-jähriges minus 2-jähriges Ereignis [Q9].
- **Zisterne:** Speicher = **6 %** des kleineren Werts aus Jahresertrag und Jahresverbrauch (DIN 1989-1), alternativ 4-Wochen-Vorrat = 8,5 % [Q14]. Für einen 4-Personen-Haushalt mit WC, Waschmaschine und Garten landen Sie bei **3,5–6 m³** (eigene Rechnung, §3.1).
- **Garage in Baden-Württemberg:** bis **50 m² Grundfläche** und **3 m mittlerer Wandhöhe** verfahrensfrei — aber „verfahrensfrei heißt nicht rechtsfrei" [Q18][Q19].

**Grenze dieses Dokuments:** Hof, Einfahrt und Terrasse stehen im Playbook `aussen-fassade-terrasse.md` (Aufbau, Pflaster, Gefälle, Sockelanschluss). Hier steht nur, was mit dem **Wasser** passiert, das dort ankommt.

---

## 0. Die Ampel zuerst

| Maßnahme | Ampel | Warum |
|---|---|---|
| Rinne und Fallrohr montieren (Traufhöhe ≤ 2 m) | 🟢 selbst | Stecksystem, Fehler sind sichtbar und korrigierbar [Q6][Q7] |
| Rinne montieren über 2 m Standhöhe | 🟡 selbst mit Gerüst | Leiterregeln siehe `aussen-fassade-terrasse.md` §1.5 |
| Fallrohr-Ableitung, Sockelablauf, Speier | 🟢 selbst | reine Wasserführung, kein Bauteilschutz betroffen |
| Mulde anlegen, Rigole ausheben | 🟡 selbst, nach Freigabe | Erdarbeiten sind Eigenleistung — **aber** Wasserrecht und k-Wert vorher klären [Q11][Q12] |
| Rigole/Mulde an Kanal oder Vorfluter anschließen | 🔴 Fachbetrieb/Behörde | Erlaubnis, Drossel, Überlauf: wasserrechtlich relevante Anlage [Q11] |
| Zisterne setzen (Aushub, Tank, Verfüllung) | 🟡 selbst möglich | Erdaushub spart 500–1.000 € [Q16]; Tankstellen ist körperlich hart |
| Filter, Pumpe, schwimmende Entnahme | 🟢 selbst | Systemteile mit Anleitung |
| Trinkwassernachspeisung anschließen | 🔴 Installateur | Trinkwassernetz: AVBWasserV § 12, freier Auslauf, Anzeige [Q13] |
| Bodenplatte Garage, gemauerte Garage | 🟠 Fachbetrieb | Bewehrung, Frostschutz, Ebenheit, Herstellerfreigabe [Q20] |
| Fertiggarage stellen | 🟠 Hersteller/Fachbetrieb | Fundament nach Herstellerangabe, sonst Tor klemmt [Q20] |
| Torantrieb nachrüsten | 🟡 selbst möglich, 🟠 wenn Tor alt | Kraftbegrenzung und Reversierung müssen passen [Q21] |
| Asbestzement-Dachplatten anfassen | 🔴 ASI-Arbeit | Baujahr vor 31.10.1993 → Erkundung, Probenahme, Fachbetrieb [Q22] |

**Merksatz:** Wasser, das **weg** muss, ist Eigenleistung. Wasser, das **ins Haus oder ins Grundwasser** kann, ist Fachbetrieb oder Behörde.

---

## 1. Dachrinne und Fallrohre

### 1.1 Die Formel, die alles entscheidet

DIN 1986-100 und DIN EN 12056-3 rechnen mit dem Regenwasserabfluss:

```
Q [l/s] = r(5,5) [l/(s·ha)] × C × A [m²] / 10.000
```

- **A** = die **im Grundriss projizierte** Dachfläche, nicht die geneigte Fläche [Q3].
- **C** = Abflussbeiwert: undurchlässiges Dach **1,0**, Kies-/Extensivgrün **0,5**, Intensivgrün **0,3** [Q3]. NedZink führt Extensivgrün pauschal mit 0,3 [Q5] — Widerspruch zwischen den Quellen, im Zweifel den Hersteller des Gründachs fragen.
- **r(5,5)** = örtliche Regenspende für 5 Minuten Dauer, Ereignis einmal in 5 Jahren, aus KOSTRA-DWD [Q3][Q9]. Sie ist **ortsabhängig** — deshalb kann keine Tabelle im Internet Ihre Rinne bestimmen.

**Beispiel, damit die Größenordnung sitzt** (eigene Rechnung mit [Q5]): 120 m² Dachfläche, C = 1,0, r = 300 l/(s·ha) → Q = 3,6 l/s. Eine NG 333 mit DN 100 schafft 4,6 l/s, eine NG 250 mit DN 76 nur 2,6 l/s. Die 250er ist damit **zu klein**, die 333er hat 28 % Reserve.

### 1.2 Rinnengröße → Dachfläche (Bemessungstabelle)

| Rinne (Nennmaß) | Fallrohr | Abfluss Q | Dachfläche bei r = 250 | bei r = 300 | bei r = 350 | bei r = 400 |
|---|---|---|---|---|---|---|
| **250** | 76 mm | 2,6 l/s | 102,5 m² | **85,5 m²** | 73,2 m² | 64,1 m² |
| **333** | 100 mm | 4,6 l/s | 185,9 m² | **154,9 m²** | 132,8 m² | 116,2 m² |
| **400** | 120 mm | 7,6 l/s | 302,4 m² | **252,0 m²** | 216,0 m² | 189,0 m² |

*Werte: NedZink, „Berechnung Dachentwässerung", Tabelle 7 [Q5]. Gilt für trichterförmige Einläufe; bei zylindrischem Stutzen Fläche um ~30 % reduzieren bzw. Fallrohr eine Dimension größer [Q5].*

**Hersteller-Richtgrößen (Marley, bei 300 l/(s·ha))** — praktischer, weil sie die Fallrohr-Nennweite mitliefern [Q6]:

| angeschlossene Dachgrundfläche | Richtgröße | Fallrohr DN |
|---|---|---|
| bis 25 m² | RG 70 / RG 75 | 53 |
| bis 51 m² | RG 100 (= NG 250) | 75 / 90 |
| bis 100 m² | RG 125 (= NG 280) | 105 / 90 |
| bis 159 m² | RG 150 (= NG 333) | 105 |

**Achtung bei den Bezeichnungen:** „8-teilig / 250 mm", „NG 250", „RG 100" und „25er Rinne" meinen dieselbe Rinne — die Zuordnung Nenngröße ↔ Richtgröße steht bei [Q8]. Wer eine „333er" bestellt und eine „RG 150" bekommt, hat dasselbe Teil; wer RG 125 mit NG 250 verwechselt, kauft **eine Nummer zu klein**.

**Rechenweg für Ihr Haus:**
1. Grundrissfläche des Hauses (Länge × Breite), nicht die Dachfläche.
2. Durch Anzahl der Fallrohre **pro Dachseite** teilen — Marley rechnet das im Beispiel vor: 15 × 10 m = 150 m², zwei Fallrohre → 75 m² je Strang, Ergebnis RG 125 mit DN 105 [Q6].
3. Örtliche Regenspende beim Versorger, Bauamt oder über einen Rinnenrechner mit PLZ holen [Q1][Q5].
4. In der Tabelle nachsehen; bei Sonderformen (Gaube, Kehle, langer Lauf) lieber eine Nummer größer.

### 1.3 Halbrund oder Kasten?

| Form | Stärke | Schwäche |
|---|---|---|
| **Halbrund** | **10–20 % mehr Abflussvermögen** als rechteckig bei gleichem Nennmaß, steigend mit der Größe [Q3] | optisch rund, Ecken als Sonderteile |
| **Kastenrinne** | gerade Ansicht, passt zu modernen Fassaden, viel Volumen bei kleiner Bauhöhe | gleicher Querschnitt schluckt weniger als halbrund [Q3]; häufig geklebt statt gesteckt [Q6] |
| **Duplex / tief-oval** | großes Fassungsvermögen auf kleinem Raum, für Garagen, Pavillons, Gerätehäuser [Q6] | nur DN 53, also kleine Einzugsflächen |

Für ein Einfamilienhaus ist die Halbrundrinne die technisch bessere Wahl, die Kastenrinne die optische. Wer eine Kastenrinne **statt** einer zu kleinen Halbrundrinne setzt, tauscht Optik gegen Leistung — die 10–20 % fehlen dann.

### 1.4 Gefälle, Hängerabstand, Dehnung

- **Gefälle: 2–3 cm auf 10 m** (= 2–3 mm/m) [Q6][Q7]. In der Bemessung gelten Rinnen mit **bis 3 mm/m als „gefällelos"** [Q3] — Sie fahren mit 2–3 mm/m also am unteren Rand des Rechenmodells. Wer Platz hat, legt 5 mm/m; das ist eine **Empfehlung, keine Normzahl**.
- **Rinneneisen alle 50–70 cm** [Q6][Q7]. Bei Schneelast und langen Rinnen den unteren Wert nehmen.
- **Vorderkante der Dachsteine** muss etwa **⅓ in die Rinne** hineinragen; Traufstreifen mit **≥ 4 cm Überlappung** [Q7].
- **Längenausdehnung:** Kunststoffrinnen arbeiten. Marley löst das mit Nocke-Nut in der Verbindungsschale; Schraubverbindungen dürfen die Ausdehnung nicht festklemmen [Q6].
- **Rinnenrand:** Der **vordere Rand muss tiefer liegen** als der hintere, sonst läuft das Wasser beim Überlaufen in die falsche Richtung — also Richtung Fassade [Q29].

### 1.5 Einlauf und Fallrohr: hier verliert man die Reserve

- **Trichterstutzen (Einhängstutzen) statt eingelötetem/ca. 80-mm-Loch:** zylindrische Einläufe ohne Trichter haben nur **80–90 %** des Abflussvermögens; das ZVDH-Merkblatt rechnet sogar mit **−30 %** [Q3][Q5]. Praktisch: Fallrohr eine Nennweite größer.
- **Der „Badewanneneffekt":** Ein zu klein ausgeschnittenes Loch im Rinnenboden lässt das Wasser sich selbst den Ablauf verschließen — im Forum beschrieben als Ursache für Überlaufen trotz ausreichender Rinne [Q29].
- **Fallrohr nicht am Sockel enden lassen.** Ohne Sockelablauf, Speier oder Anschluss an eine Rigole läuft das gesamte Dachwasser an die empfindlichste Stelle der Fassade. Die Folgekosten (Sockelputz, Abdichtung, Kellernässe) sind ein Vielfaches der 30 € für einen Speier — *Erfahrungswert, keine Normzahl*.
- **Fallrohre unten nicht in ein KG-Rohr ohne Geruchsverschluss/Schlammfang** führen, wenn Laub mitkommt; Regenwasserleitungen im Trennsystem brauchen keinen Geruchsverschluss [Q1], verschlammen aber ohne Laubschutz.

### 1.6 Warum Häuser aus den 1960ern oft unterdimensioniert sind

Fünf Mechanismen, in der Reihenfolge ihrer Häufigkeit (Reihenfolge = *Einschätzung*, Einzelbelege je Punkt):

1. **Alte Bemessung war einfacher.** Vorgehängte Rinnen wurden nach **DIN 18460** „stark vereinfacht" bemessen; die Norm wurde mit Erscheinen von DIN EN 12056-3 im **Januar 2001 zurückgezogen** [Q4]. Was 1965 korrekt war, ist heute keine Bemessung mehr.
2. **Ein Ablauf pro Dachseite.** Die Marley-Tabelle zeigt den Hebel: 150 m² auf zwei Stränge = 75 m² je Strang (RG 125), 150 m² auf **einen** Strang = 150 m² (RG 150) [Q6]. Häuser mit einem Fallrohr je Seite haben oft die kleinere Rinne plus den längeren Lauf.
3. **Das Dach ist gewachsen, die Rinne nicht.** Anbau, Gaube, Carport, Dachausbau: die Grundrissfläche steigt, die alte Rinne bleibt. Die Tabelle in §1.2 gilt für die **gesamte** angeschlossene Fläche.
4. **Die Regenspende ist gestiegen.** Am Beispiel Mettmann: r(5,2) = **274**, r(5,5) = **351**, r(5,30) = **550**, r(5,100) = **667** l/(s·ha) [Q9]. Eine Rinne, die nach „300" bemessen wurde, hat bei 351 keine Reserve mehr.
5. **Laub und Wartung.** Im Forumsfall mit 112 m², NG 333 und DN 100 lag es nicht an der Dimension, sondern am **verstopften Laubschutz** — danach lief sie „bei stärkstem Regen nicht mehr über" [Q29].

**Ehrliche Einordnung:** „Die 60er-Jahre-Rinne ist zu klein" ist als Pauschalaussage **unbelegt**. Belegt ist: die damalige Bemessungsgrundlage ist zurückgezogen, die Regenspenden sind gestiegen, und der Engpass ist häufig der **Ablauf** (ein Fallrohr, zylindrischer Stutzen, Laub), nicht die Rinne selbst. Prüfen Sie in dieser Reihenfolge: Laubschutz → Stutzen → zweites Fallrohr → größere Rinne.

### 1.7 Laubschutz

- **Gitter im Rinnenlauf** (z. B. „Poly-Net Laubstop") oder **glatte Abdeckung** über der Rinne („Laubfrei"), die das Laub abrollen lässt [Q6].
- **Konsequenz:** Laubschutz ist Wartungsteil, kein Selbstläufer. Der Forumsfall zeigt: verstopfter Schutz = Überlauf bei Starkregen, obwohl die Rinne reicht [Q29].
- **Kein Laubschutz an der Zisterne vergessen:** Der Filter vor dem Tank ist das zweite Sieb; er muss zugänglich bleiben [Q13][Q16].

---

## 2. Versickerung, Starkregen, Rückstau

### 2.1 Recht zuerst: Versickern ist eine Benutzung

- **Gezieltes Einleiten von gesammeltem Niederschlagswasser ins Grundwasser ist Gewässerbenutzung** und braucht die wasserrechtliche Erlaubnis der Kreisverwaltungsbehörde [Q11].
- **Ausnahme:** wenn die **Niederschlagswasserfreistellungsverordnung (NWFreiV)** und die zugehörige technische Regel **TRENGW** eingehalten sind [Q11]. Das ist Ländersache — in Bayern so, in anderen Ländern anders benannt.
- **Kommunale Satzung** kann zusätzlich Anschlusszwang, Versickerungspflicht, Rückhaltung oder Gebühren regeln. Beispiel (nicht Ihr Ort): Mettmann verlangt den Überflutungsnachweis ab 800 m² abflusswirksamer Fläche [Q9]. **Jede Kommune ist anders — die eigene Satzung beim Bauamt holen, nicht die fremde abschreiben.**

### 2.2 Wo Versickerung überhaupt geht

| Kriterium | Zahl | Quelle |
|---|---|---|
| Durchlässigkeit des Bodens (kf) für Mulden-Rigolen **ohne** Notablauf | **≥ 1 × 10⁻⁶ m/s** | [Q12] |
| bewachsene Oberbodenschicht | **≥ 20 cm** | [Q11] |
| Einstauhöhe Sickermulde | **ca. 30 cm** | [Q11] |
| Abstand Baum (Stammmitte) zur Rigolenkante | **≥ 2,5 m** bzw. halber Kronendurchmesser | [Q12] |
| Mindestabstand zum Grundwasser | *unbelegt — örtlich vorgegeben, meist 1 m zur Sohle* | — |

**Der kf-Wert ist keine Schätzung.** Er kommt aus einem Sickerversuch oder Boden gutachten; ein Blick in die Bodenkarte reicht nicht. Bei kf unter 1 × 10⁻⁶ m/s versickert die Rigole nicht, sondern steht — dann brauchen Sie Rückhaltung mit Drosselablauf statt Versickerung [Q12].

### 2.3 Mulde, Rigole, Schacht — die Rangfolge

1. **Flächenhafte Versickerung über bewachsenen Oberboden** (Mulde, Sickerbecken) ist die beste Lösung: der belebte Boden reinigt mechanisch und biologisch [Q11].
2. **Linienförmige Versickerung** (Rigole, Sickerrohr) nur, wenn flächig nicht geht. **Unterirdische Anlagen brauchen in jedem Fall eine ausreichende Vorreinigung** [Q11].
3. **Sickerschacht** nur, wenn zwingende Gründe Fläche und Linie ausschließen [Q11].
4. **Kein Direktanschluss der Hoffläche an die Rigole.** Der Anschluss von Abflussflächen direkt an Rigole oder Rigolenschacht ist wegen des Wegfalls der Reinigungswirkung **nicht zulässig**; das Wasser muss über die Mulde bzw. den Oberboden [Q12].

**Aufbau einer Rigole (Praxis):** Aushub, **Geotextil/Vlies** als Trennlage rundum, Kies oder Kunststoff-Füllkörper, **Vollsickerrohr** über die ganze Länge, Überdeckung. Kunststoffkörper sind teurer in der Anschaffung, brauchen aber deutlich weniger Platz [Q11]. Das Vlies hält Feinanteile aus dem Kies — ohne Vlies verschlammt die Rigole von innen und versickert nach wenigen Jahren nicht mehr (**Einschätzung**; die Trennlage ist in [Q12] und im Praxisbericht [Q31] Standard).

**Kosten-Anker (Anekdote, keine Kalkulation):** 20 m Rigole (1 m breit, 1 m tief) mit Vlies, Dränrohr und 20 m³ Kies → **2.200 € netto** Angebot, Kies mit **70 €/m³** [Q31]. Das ist die Größenordnung, mit der Sie rechnen können, bevor Sie drei Angebote haben.

### 2.4 Starkregen: der Überflutungsnachweis

- **Auslöser (Beispiel-Kommune):** Grundstücke über **800 m²** abflusswirksame Fläche müssen mit dem Entwässerungsantrag einen Überflutungsnachweis nach DIN 1986-100 vorlegen [Q9].
- **Rechenweg:** Volumendifferenz zwischen **30-jährigem** Ereignis und **2-jährigem** Bemessungsregen; maßgebend ist der größte Wert aus **D = 5, 10 und 15 Minuten** [Q9].
- **Erhöhte Anforderung:** Tiefgarage, Wohnraum im Kellergeschoss, tieferliegende Freisitze mit Fenstern → **100-jähriges** Ereignis [Q9].
- **Wohin mit dem Wasser:** „schadlose Überflutung" auf dem **eigenen** Grundstück, z. B. durch Hochborde oder Mulden, oder in Rückhalteräume; Lageplan beilegen [Q9].
- **Notentwässerung:** Bei vorgehängten Rinnen ist der **vordere Rinnenrand** die Notentwässerung; bei innenliegender Entwässerung braucht es Notabläufe mit freiem Auslauf auf schadlos überflutbare Flächen, **nicht** angeschlossen an die Entwässerungsanlage [Q3][Q1].
- **Die Größenordnung der Notentwässerung** (München, C = 0,5): planmäßig 176,5 l/(s·ha), zusätzlich über Notentwässerung **456,5 l/(s·ha)** — also rund das **2,6-fache** der Regenspende [Q3].

**Was das für Sie heißt:** Eine Rinne ist kein Hochwasserschutz. Sie ist für r(5,5) bemessen und **soll** bei Extremregen überlaufen — nur bitte dahin, wo es nicht ins Haus läuft [Q29].

### 2.5 Rückstau: die Klappe, die im Keller fehlt

- **Rückstauebene** = Höhe, bis zu der Abwasser im Kanal maximal ansteigen kann, in der Regel die **Straßenoberkante** am Anschlusspunkt [Q10].
- **Alle Ablaufstellen darunter** brauchen Schutz. Nach DIN 1986-100 / DIN EN 12056 ist die **automatische Abwasserhebeanlage** mit Rückstauschleife der Regelfall; ein **Rückstauverschluss** (DIN EN 13564) ist nur bei untergeordneter Nutzung, kleinem Nutzerkreis und Gefälle zum Kanal zulässig [Q10].
- **Wartung: zweimal jährlich**, bei motorischen Verschlüssen durch den Fachbetrieb, dokumentiert. Viele Elementartarife machen die funktionsfähige Rückstausicherung zur **Obliegenheit** — ohne Wartungsnachweis kürzt der Versicherer [Q10].
- **Pflicht?** Die Sicherung ist über die anerkannten Regeln der Technik und die kommunale Entwässerungssatzung Sache des **Eigentümers** [Q10]. Es gibt kein Amt, das nachschaut — bis der Keller voll ist.

---

## 3. Zisterne: Größe, Nutzung, Hygiene, Kosten

### 3.1 Größe rechnen — zwei Regeln, ein Band

**Ertrag** = Dachgrundfläche × Jahresniederschlag × **Ertragsbeiwert**
Der Beiwert liegt zwischen **0,3** (intensiv begrünt) und **0,8** (geneigtes Hartdach); typisch **0,75** [Q14]. Die Berliner Regenwasseragentur rechnet im Rechner mit **0,9**, weil sie Filterverluste anders ansetzt [Q15] — beide Werte sind begründet, der Unterschied ist die Frage, ob Sie den Worst Case oder den Rechenwert wollen.

**Bedarf** (DIN 1989-1, zitiert nach [Q14]): WC **24 l/Person/Tag**, Waschmaschine **12 l/Person/Tag** (DIN 1989-1 nennt 10 l), Garten **60 l/m²/Jahr**. Die Berliner Agentur nennt für intensive Bepflanzung **100–200 l/m²/Jahr** [Q15] — bei einem großen Garten ist der höhere Wert realistisch.

**Speichergröße:** **6 %** des Jahresertrags **oder** des Jahresverbrauchs, je nachdem, welcher Wert **kleiner** ist (DIN 1989-1) [Q14]. Alternativ 4-Wochen-Vorrat = **8,5 %** der Jahressumme [Q14].

**Durchgerechnet** (120 m² Dach, 800 mm Niederschlag, 4 Personen, 100 m² Garten — eigene Rechnung mit den Faktoren aus [Q14]):

| Position | Rechnung | Ergebnis |
|---|---|---|
| Ertrag | 120 × 0,8 × 0,75 | **72 m³/a** |
| WC | 4 × 24 × 365 | 35,0 m³/a |
| Waschmaschine | 4 × 12 × 365 | 17,5 m³/a |
| Garten | 100 × 60 | 6,0 m³/a |
| **Bedarf** | Summe | **58,6 m³/a** |
| Speicher nach 6 % | 0,06 × 58,6 | **3,5 m³** |
| Speicher nach 4-Wochen-Regel | 0,085 × 72 | **6,1 m³** |

→ Bestellen Sie **4–6 m³**, nicht 10. Wer nur den Garten bewässert, braucht keine Zisterne: 150 m² Garten = 9 m³/a Bedarf, 6 % davon = **0,54 m³** — dafür reicht eine Regentonne [Q16].

### 3.2 Wofür Sie das Wasser nutzen dürfen — und wofür nicht

| Nutzung | Möglich? | Bedingung |
|---|---|---|
| Garten, Hof reinigen, Auto | ja | Filter, keine Trinkwasserleitung betroffen |
| WC-Spülung | ja | **Nichttrinkwasseranlage**: Anzeige, Kennzeichnung, freier Auslauf [Q13] |
| Waschmaschine | ja | wie WC; Hygiene meist unkritisch, aber Keimbelastung möglich [Q14] |
| Trinken, Kochen, Duschen | **nein** | Regenwasser erfüllt die TrinkwV nicht [Q13] |
| Trinkwassernachspeisung | ja, nur mit Sicherung | freier Auslauf Typ AA/AB/AD nach DIN EN 1717 [Q13] |

### 3.3 Die fünf Pflichten, die aus einem Tank eine Anlage machen

1. **Anzeige beim Gesundheitsamt:** Errichtung einer Nichttrinkwasseranlage **spätestens vier Wochen vorher** schriftlich; Stilllegung innerhalb von **drei Tagen** (§ 12 TrinkwV) [Q13].
2. **Mitteilung an den Wasserversorger** vor Errichtung (AVBWasserV § 3) [Q13].
3. **Freier Auslauf** zur Trinkwassernachspeisung: Abstand zwischen höchstem Betriebswasserspiegel und Zulauföffnung = **2 × Rohrdurchmesser, mindestens 20 mm**, nicht überflutbar [Q13].
4. **Kennzeichnung:** Nichttrinkwasserleitungen grün-blau-grün nach DIN 2403 mit Kurzzeichen **„NPW"**, alle Entnahmestellen mit **„Kein Trinkwasser"**, zusätzlich ein Hinweis am Trinkwasser-Hausanschluss [Q13].
5. **Wartung:** freier Auslauf **halbjährlich** durch ein eingetragenes Installationsunternehmen (DIN EN 806-5) [Q13]; Speicher reinigen/inspektionieren **jährlich** empfohlen [Q15].

**Und zwei Verbote:** keine **Querverbindung** zwischen Regen- und Trinkwassernetz, und Leitungen, in denen Nichttrinkwasser floss, dürfen **nie** wieder Trinkwasser führen [Q13].

### 3.4 Technik: Filter, Pumpe, Überlauf

- **Filter** vor dem Tank (170–420 €): selbstreinigende Varianten sind wartungsärmer [Q16]. Der Filter ist auch der Laubschutz — ohne ihn geht der Dreck in den Speicher.
- **Pumpe/Hauswasserwerk** (150–460 €) mit Druckschalter und **Trockenlaufschutz** [Q16].
- **Schwimmende Entnahme** statt Saughahn am Boden: sie zieht das sauberere Wasser unter der Oberfläche, nicht das Sediment [Q13].
- **Überlauf ist Pflicht und muss angeschlossen sein.** Ein realer Fall: Überlauf der Zisterne nie angeschlossen, Wasser versickerte unter dem Garagenboden und drückte gegen die Kellerwand [Q30]. Der Überlauf gehört in eine Versickerung, einen Kanal oder ein Gewässer — mit Rückstausicherung, wenn er am Kanal hängt [Q14].
- **Trinkwassernachspeisemodul** mit freiem Auslauf, nicht als direkte Verbindung [Q13].

### 3.5 Kosten und Förderung

| Position | Kosten | Quelle |
|---|---|---|
| Zisterne 3 m³ (Tank 1.100–2.200 € + Einbau 1.000–2.000 €) | **2.500–4.000 €** | [Q16] |
| Zisterne 5–6 m³ | **3.500–6.000 €** | [Q16] |
| Zisterne 10 m³ | **5.000–8.000 €** | [Q16] |
| Filter | 170–420 € | [Q16] |
| Pumpe/Hauswasserwerk | 150–460 € | [Q16] |
| Steuerung, Nachspeisung, Zubehör | 200–500 € | [Q16] |
| Komplettanlage 4-Personen-Haushalt | **3.500–7.000 €** | [Q16] |
| Erdaushub in Eigenleistung spart | 500–1.000 € | [Q16] |
| Privatwasserzähler, Wechsel alle 6 Jahre | ~90 €/Stück | [Q15] |
| Amortisation mit Förderung / ohne | **7–14 / 12–23 Jahre** | [Q16] |

**Förderung ist kommunal, nicht bundesweit.** Beispiel Barsinghausen (Niedersachsen): Programm ab 1. Juni 2026, Zuschuss **bis 1.000 €**, Antrag **nach** Fertigstellung, Windhundprinzip [Q17]. Hamburg fördert mit **rund 40 %** [Q16]. **Regel: erst Förderrichtlinie lesen, dann bestellen** — viele Programme verlangen bestimmte Normen (DIN 1989-100, DIN EN 16941-1) und den Nachweis der Fertigstellung.

---

## 4. Hof und Einfahrt — nur Querverweis

Pflasteraufbau, Tragschicht, Gefälle (2,5 %), Randeinfassung, Sockelanschluss und die Mengenrechnung (50 m² ≈ 38 t Material) stehen vollständig in **`aussen-fassade-terrasse.md`**, Kapitel 5 und 7. Hier nur die zwei Sätze, die zur Entwässerung gehören:

- **Gefälle weg vom Haus**, nicht zur Garage und nicht zur Kellerwand; die Oberkante Belag bleibt **15 cm unter** dem Wandputz [siehe `aussen-fassade-terrasse.md`].
- **Die versiegelte Fläche ist die Bemessungsgrundlage** für Rigole und Überflutungsnachweis (§2.4). Wer die Einfahrt vergrößert, muss die Versickerung mitrechnen — nicht nur die Optik.

---

## 5. Garage und Carport

### 5.1 Baurecht: verfahrensfrei ist nicht rechtsfrei

- **Baden-Württemberg, LBO Anhang 1 Nr. 1 b** (zu § 50 Abs. 1): verfahrensfrei sind „**Garagen einschließlich überdachter Stellplätze mit einer mittleren Wandhöhe bis zu 3 m und einer Grundfläche bis zu 50 m², außer im Außenbereich**" [Q18]. Carports fallen als „überdachte Stellplätze" darunter, wenn die Maße passen.
- **Andere Länder, andere Zahlen.** Die LBO ist Landesrecht; Bayern, NRW, Niedersachsen haben eigene Grenzen. Die Zahl 50 m² ist ein BW-Wert, kein Bundesrecht.
- **„Verfahrensfrei heißt nicht rechtsfrei":** Sie sparen den Bauantrag, nicht die Prüfung. Abstandsflächen, Bebauungsplan, Ortsgestaltungssatzung und Nachbarrecht gelten weiter, und **Sie** sind für die Einhaltung verantwortlich — die Behörde prüft nicht vorher [Q19].
- **Grenzbebauung:** Garagen sind in den Landesbauordnungen privilegiert, aber an Länge und Höhe gebunden. Die konkrete Zahl aus Ihrer LBO und Ihrem Bebauungsplan nehmen, nicht aus einem Ratgeber.

### 5.2 Statik und Bodenplatte

- **Bodenplatte ≠ Fundament.** Die Bodenplatte nimmt die Lasten der Garage auf und bildet den Boden; das Fundament sorgt für den sicheren Stand auf tragfähigem Untergrund [Q20].
- **Bei Fertiggaragen** ist der Boden oft im Werk integriert — das Fundament muss trotzdem exakt nach Herstellerangabe hergestellt werden (Maße, Ebenheit, Auflagepunkte) [Q20].
- **Bei gemauerten Garagen** wird die Bodenplatte in der Regel vor Ort betoniert: Aushub, **Schottertragschicht**, Schalung, **Bewehrung**, Betonage, Trocknung, Ebenheit [Q20].
- **Frostschutz** ist der Punkt, an dem gespart wird und später das Tor klemmt: nicht tragfähiger Untergrund, fehlender Frostschutz, falsche Maße und schlechte Abdichtung sind laut Hersteller die typischen Fehler [Q20].
- **Streifenfundament** ist nur eine Alternative, wenn das Garagenmodell dafür geeignet ist und der **Hersteller sie freigibt** [Q20]. Bei schweren Dächern (Beton, Begrünung) gehört ein Statiker dazu — *Einschätzung*.

### 5.3 Entwässerung der Garage

- **Gefälle 1–2 %** zum Tor oder zu einem Ablaufgitter/einer Linienentwässerung; **1 %** ist das Minimum, viele Praktiker fordern 1,5 % [Q24].
- **Richtung:** in Richtung Tor (Wasser läuft raus), zu einem Punktablauf in der Mitte (kuvertförmig) oder zu einer Linienentwässerung — die Wahl bestimmt die Höhenplanung der Bodenplatte [Q24].
- **Ohne Gefälle** bleibt Wasser stehen, besonders im Winter bei Schneematsch; die Bodenplatte durchfeuchtet, Werkzeug und Reifen stehen im Nassen [Q20][Q24].
- **Ölabscheider:** Für private Pkw-Garagen ist ein Abscheider **nicht generell** gefordert — das regelt die örtliche Entwässerungssatzung, und wer selbst Öl wechselt, braucht eine Auffangwanne. **Unbelegt** in dieser Recherche: eine belastbare bundesweite Pflicht für die private Einzelgarage. Vor dem Anschluss an den Kanal beim Bauamt fragen.

### 5.4 Elektro

- **Steckdosenstromkreise** in der Garage fallen unter die RCD-Pflicht: **FI ≤ 30 mA** für Steckdosen bis 32 A (DIN VDE 0100-410:2018-10) [Q25]. Ein eigener Stromkreis für Garage/Wallbox ist Praxisstandard — und die Wallbox ist ein eigener Fall (Anmeldung beim Netzbetreiber).
- **Erdkabel: 60 cm tief** im Garten, **80 cm** unter Wegen, Einfahrten und Stellplätzen [Q26].
- **Anschluss an die Hausverteilung** ist Installationsarbeit hinter der Hausanschlusssicherung — dafür gilt die Grenze aus dem Haupt-Skill (NAV § 13 Abs. 2, eingetragenes Installationsunternehmen). Eigenleistung ist das **Graben** und das Einziehen nach Vorgabe, nicht das Anklemmen.

### 5.5 Torantrieb

- **Kraftbegrenzung:** Automatische Tore dürfen mit maximal **ca. 40 kg** auf ein Hindernis treffen und müssen **in unter 1 Sekunde** wieder öffnen [Q21]. Veraltete Anlagen erfüllen das oft nicht — genau darin liegt das Unfallrisiko für Kinder [Q21].
- **Lichtschranke** in geringer Höhe als zusätzliche Sicherung: Das Tor stoppt und öffnet, **bevor** es auf das Hindernis trifft [Q21].
- **Quetschstellen** sind nicht nur der Antrieb: unverkleidete Seitenzargen, zu geringer Abstand zwischen Hebelarm und Zarge, zu große Abstände in alten Federn [Q21].
- **Nachrüstung:** Antrieb und Tor sollten vom **gleichen Hersteller** sein, damit die Sicherheitsmechanismen zusammenpassen [Q21]. Die Normenkette (EN 12453 Kraftbetätigte Tore, EN 12978 Schutzeinrichtungen) ist hier **nicht im Volltext geprüft** — die Zahlen oben sind Herstellerangaben.

### 5.6 Schadstoffe in alten Garagen

- **Baujahr vor dem 31.10.1993 → mit Asbest rechnen.** Asbesthaltige Produkte durften ab diesem Datum nicht mehr hergestellt, in Verkehr gebracht oder verwendet werden [Q22].
- **Betroffen sind genau die Garagendächer:** „**Dach- und Fassadenplatten**, Sanitärrohre, Blumenkübel und andere Asbestzement-Erzeugnisse", dazu Dachpappe/Asbestpappen [Q22]. Wellplatten auf Garage und Carport sind der Klassiker.
- **Solange die Faser gebunden ist, geht keine Gefahr aus** — kritisch wird es beim **Bearbeiten oder Zerstören**: Rückbau von Asbestzement-Produkten, Abbruch, Schleifen [Q22].
- **Ihre Pflichten als Auftraggeber:** Sie müssen dem Handwerksbetrieb **schon bei der Vertragsanbahnung** alle Informationen zur Bau- und Nutzungsgeschichte geben; bei Baujahr 1993–1996 zusätzlich das Datum des Baubeginns [Q22]. Reichen die Informationen nicht, muss der Betrieb erkunden und beproben — oder so arbeiten, als läge Belastung vor [Q22].
- **Entsorgung:** asbesthaltige Baustoffe sind **gefährlicher Abfall**, nur in zugelassenen Anlagen; über den Restmüll entsorgen ist strafbar [Q22].
- **Öl im Boden** alter Garagen (Tropfverluste, Altölwechsel) ist ein realistischer Verdacht, aber in dieser Recherche **nicht belegt** — bei Aushub oder Verkauf Bodenprobe einplanen.

---

## 6. Typische Fehler — und woran Sie sie erkennen

| # | Fehler | Folge | Erkennen / Abhilfe |
|---|---|---|---|
| 1 | **Rinne zu klein** für die Grundrissfläche | Überlauf bei Starkregen, Wasser an der Fassade | Fläche je Fallrohr rechnen (§1.2); zweites Fallrohr ist oft billiger als neue Rinne [Q29] |
| 2 | **Nur ein Ablauf** für 150 m² und mehr | Überlauf am Ende der Rinne | Marley-Beispiel: 150 m² auf zwei Stränge = RG 125 statt RG 150 [Q6] |
| 3 | **Zylindrischer Stutzen / zu kleines Loch** | −30 % Abfluss, „Badewanneneffekt" | Einhängstutzen mit Trichter, Fallrohr eine Nummer größer [Q3][Q5][Q29] |
| 4 | **Fallrohr endet am Sockel** ohne Ableitung | Sockelputz durchfeuchtet, Ausspülung, Kellernässe | Sockelablauf/Speier, Anschluss an Rigole oder Zisterne |
| 5 | **Rigole ohne Vlies** | Kies verschlammt, Versickerung bricht zusammen | Geotextil als Trennlage rundum, Vollsickerrohr [Q12][Q31] |
| 6 | **Rigole ohne Vorreinigung / Direktanschluss der Fläche** | Verockerung, Grundwassereintrag; unzulässig | Wasser über Mulde/Oberboden führen [Q11][Q12] |
| 7 | **Zisterne ohne (angeschlossenen) Überlauf** | Wasser versickert unkontrolliert, drückt gegen Kellerwand | Überlaufleitung planen und abnehmen; realer Schadensfall [Q30] |
| 8 | **Rückstauklappe fehlt** im Keller | Abwasser aus dem Kanal im Keller | Rückstauebene prüfen, Hebeanlage statt Klappe bei Wohnraum [Q10] |
| 9 | **Garage ohne Gefälle** | Pfützen, Frostschäden, feuchte Bodenplatte | 1–2 % zum Tor oder Ablauf, vor dem Betonieren festlegen [Q24][Q20] |
| 10 | **Trinkwassernachspeisung ohne freien Auslauf** | Trinkwasserverunreinigung, Anzeigepflicht verletzt | Typ AA/AB/AD, 2×D ≥ 20 mm, Anzeige 4 Wochen vorher [Q13] |
| 11 | **Laubschutz nie gereinigt** | Überlauf trotz ausreichender Rinne | zweimal im Jahr, vor allem nach dem Laubfall [Q29] |
| 12 | **Asbestplatten selbst abgeschlagen** | Faserfreisetzung, Bußgeld/Strafbarkeit, Entsorgung unzulässig | Baujahr prüfen, erkunden lassen, ASI-Betrieb [Q22] |

---

## 7. Ablauf in der Reihenfolge, die kein Geld zweimal kostet

**Dachrinne erneuern:**
1. Grundrissfläche und Fallrohranzahl aufnehmen, örtliche Regenspende holen [Q3][Q5].
2. Rinnengröße und Fallrohr-DN bestimmen (§1.2), Reserve für Anbauten einplanen.
3. Höhenlage festlegen: Gefälle 2–3 mm/m, Rinnenrand vorn tiefer [Q6][Q29].
4. Rinneneisen 50–70 cm, an der Richtschnur ausrichten, Traufstreifen [Q7].
5. Rinne montieren, Dehnungsausgleich beachten, Einhängstutzen mit Trichter [Q6][Q3].
6. Fallrohr mit ausreichend Rohrschellen, unten **nicht** am Sockel enden lassen.
7. Ableitung bauen: Speier, Sockelablauf, Rigole oder Zisterne — **vor** dem nächsten Regen.
8. Laubschutz montieren und in den Wartungskalender eintragen [Q6].

**Rigole/Mulde:**
1. Satzung und Wasserrecht klären (NWFreiV/TRENGW? Erlaubnis?) [Q11].
2. kf-Wert bestimmen lassen, Grundwasserabstand prüfen [Q12].
3. Fläche je Fallrohr und Q nach §1.1 rechnen, Speichervolumen aus DWA-A 138 [Q12].
4. Mulde ausheben, Oberboden ≥ 20 cm andecken, Einstau ≤ 30 cm [Q11].
5. Rigole: Vlies, Kies/Füllkörper, Vollsickerrohr, Überlauf [Q12][Q31].
6. Einlauf gestalten (Vorreinigung, kein Direktanschluss) [Q12].
7. Nach Regen prüfen: steht Wasser länger als 24 h, ist die Anlage zu klein oder der Boden zu dicht.

**Zisterne:**
1. Bedarf und Ertrag rechnen (§3.1), Speicher 6 % bzw. 4-Wochen-Vorrat [Q14].
2. Aufstellort: Abstand zum Haus, Zufahrt für Aushub, Überlaufziel [Q30].
3. Anzeige beim Gesundheitsamt **vier Wochen vorher**, Mitteilung an den Versorger [Q13].
4. Aushub, Sandbett, Tank, Verfüllung; Auftrieb bei hohem Grundwasser beachten (*unbelegt, Herstellerangabe*).
5. Filter, schwimmende Entnahme, Überlauf, Rückstausicherung [Q13][Q14].
6. Trinkwassernachspeisung mit freiem Auslauf durch den Installateur [Q13].
7. Kennzeichnen, einweisen, Wartungsplan (halbjährlich freier Auslauf, jährlich Speicher) [Q13][Q15].

**Garage:**
1. Verfahrensfreiheit und Abstandsflächen in **Ihrer** LBO prüfen, Bebauungsplan lesen [Q18][Q19].
2. Baujahr-Aspekt: alte Garage → Dachplatten beproben lassen, bevor jemand sie anfasst [Q22].
3. Bodenplatte/Fundament nach Herstellerangabe, Frostschutz, Bewehrung, Ebenheit [Q20].
4. Gefälle 1–2 % und Ablauf **vor** dem Betonieren festlegen [Q24].
5. Strom: eigener Kreis, FI 30 mA, Erdkabel 60/80 cm [Q25][Q26].
6. Tor und Antrieb aufeinander abstimmen, Kraftbegrenzung und Reversierung prüfen [Q21].
7. Entwässerung: kein Wasser in die Garage leiten, das vom Hof kommt (*Einschätzung*).

---

## 8. Kostenband auf einen Blick

| Maßnahme | Kosten | Quelle |
|---|---|---|
| Dachrinne Kunststoff erneuern | **40–90 €/m** inkl. Montage, Rückbau, Entsorgung | [Q23] |
| Dachrinne Titanzink | **50–100 €/m** | [Q23] |
| Dachrinne Kupfer | **80–150 €/m** | [Q23] |
| Fahrgerüst | ~**200 €/Projekt** | [Q23] |
| Fassadengerüst 100 m² | **1.700–2.000 €** | [Q23] |
| Rigole 20 m³ (Anekdote) | ~**2.200 € netto** | [Q31] |
| Kies für Rigole | ~**70 €/m³** | [Q31] |
| Zisterne komplett 3 / 5–6 / 10 m³ | **2.500–4.000 / 3.500–6.000 / 5.000–8.000 €** | [Q16] |
| Förderung (Beispiel) | bis **1.000 €** (Barsinghausen), ~**40 %** (Hamburg) | [Q17][Q16] |

**Einordnung:** Die Spannen sind Material- und Regionsunterschiede, keine Unsauberkeit. Drei Angebote, 10–15 % Puffer für Aushub und Entsorgung — und beim Gerüst länger mieten als geplant.

---

## Quellenverzeichnis

### Normen (nur Nummer, Titel, Ausgabe geprüft — kein Volltext gekauft)

| Nr. | Norm | Ausgabe | Belegte Aussage |
|---|---|---|---|
| Q1 | **DIN 1986-100** Entwässerungsanlagen für Gebäude und Grundstücke | **2016-12**; Baunormenlexikon listet inzwischen eine Ausgabe **2026-11** | Geltungsbereich, Notentwässerung mit freiem Auslauf, Regenwasserleitungen ohne Geruchsverschluss. *Achtung: Die 2026-11-Ausgabe ist brandneu — Änderungen vor Planung prüfen.* https://www.baunormenlexikon.de/norm/din-1986-100/e9ee17a0-7205-4112-93c4-c33e6069db5d |
| Q2 | **DIN EN 12056-3** Schwerkraftentwässerungsanlagen, Dächer | **2001-01** | Bemessungsnorm für vorgehängte und innenliegende Rinnen. https://www.baunormenlexikon.de/norm/din-en-12056-3/ae6fbe2a-a52b-40b0-9892-e4a25941b808 |
| Q27 | **DIN 1989-100** Regenwassernutzungsanlagen | **2022-07** | aktuelle deutsche Norm für RWNA. https://www.baunormenlexikon.de/norm/din-1989-100/1367fec8-3e6e-4957-a260-0e4458ad5b02 |
| Q28 | **DIN EN 16941-1** Vor-Ort-Anlagen für Nicht-Trinkwasser | **2024-05** | europäische Norm, in [Q13] als technische Grundlage genannt. https://www.baunormenlexikon.de/norm/din-en-16941-1/806844b9-d7b6-4e1f-a4f6-9f8e523463fb |

### Behörden, Kammern, Verbände

| Nr. | Quelle | Belegte Zahlen |
|---|---|---|
| Q3 | Bayerische Architektenkammer, **Merkblatt M1: Regenentwässerungsanlagen nach DIN 1986-100** (PDF) | Q = r·C·A/10.000; C = 1,0/0,5/0,3; r(5,5) aus KOSTRA; **Halbrund 10–20 % leistungsfähiger**; **≤ 3 mm/m = gefällelos**; **−15 %** je Richtungsänderung > 10°; Rinne 250 → Ablauf Ø 60–80, Rinne 333 → Ø 100–120; **−30 %** bei zylindrischem Einlauf; Notentwässerung über Rinnenrand; QNot-Formel; München r(5,5) 353 / r(5,100) 633. https://www.byak.de/data/pdfs/Recht/Merkblaetter/Merkblatt-1-Regenentwaesserungsanlagen.pdf |
| Q9 | Stadt Mettmann, **Infoblatt Überflutungsnachweis nach DIN 1986-100** (25.07.2018, PDF) | Nachweis ab **800 m²** abflusswirksamer Fläche; 30-jährig minus 2-jährig; D = 5/10/15 min; T = 100 bei Tiefgarage/Wohnraum im KG; r(5,2)=274, r(5,5)=351, r(5,30)=550, r(5,100)=667 l/(s·ha). **Kommunales Beispiel, nicht allgemeinverbindlich.** https://www.mettmann.de/web/download/ueberflutungsnachweis_info.pdf |
| Q11 | Bayerisches **LfU**, „Versickerung von gesammeltem Niederschlagswasser" | Versickerung = Gewässerbenutzung mit **Erlaubnis**; Ausnahme NWFreiV + TRENGW; bewachsener Oberboden **≥ 20 cm**; Einstau **ca. 30 cm**; Rigole nur mit **Vorreinigung**; Sickerschacht nur bei zwingendem Grund; Kunststoffkörper teurer, aber platzsparend. https://www.lfu.bayern.de/wasser/umgang_mit_niederschlagswasser/versickerung/index.htm |
| Q12 | **Berliner Wasserbetriebe, Regelblatt 600** „Mulden-Rigolen-System" (PDF, 11/2012) | kf **≥ 1 × 10⁻⁶ m/s** ohne Notablauf; **Geotextil** als Trennlage; Baumabstand **≥ 2,5 m** bzw. halber Kronendurchmesser; **Direktanschluss der Flächen an die Rigole unzulässig**; DWA-A 138. https://www.bwb.de/regelblaetter/rgbl600_11-2012.pdf |
| Q13 | **DVGW-Kompaktinfo** „Regenwassernutzungsanlagen" (TWIN, 07/2025, PDF) | § 12 TrinkwV: Anzeige **4 Wochen vorher**, Stilllegung **3 Tage**; § 13 Abs. 3 + DIN 1988-100: **freier Auslauf Typ AA/AB/AD** nach DIN EN 1717, Abstand **2 × D, min. 20 mm**; Kennzeichnung grün-blau-grün „NPW" + „Kein Trinkwasser"; Wartung freier Auslauf **halbjährlich** (DIN EN 806-5); AVBWasserV § 3 Mitteilung; keine Querverbindung, keine Umnutzung. https://www.wvr.de/images/Bauen_und_Planen/twin/twin_2025-07-Regenwassernutzungsanlagen.pdf |
| Q18 | **LBO Baden-Württemberg, Anhang 1** (zu § 50 Abs. 1), Nr. 1 b | Garagen inkl. überdachter Stellplätze, **mittlere Wandhöhe ≤ 3 m**, **Grundfläche ≤ 50 m²**, außer im Außenbereich → verfahrensfrei. https://dejure.org/gesetze/LBO/Anhang_1.html |
| Q19 | Bayerisches Staatsministerium für Wohnen, Bau und Verkehr, „Verfahrensfreie Bauvorhaben" | Zitat: **„Verfahrensfrei heißt nicht rechtsfrei!"** — keine Prüfung vorab, Eigentümer verantwortlich für Abstandsflächen, Bebauungsplan, Satzungen. https://www.bauen.bayern.de/buw/bauherreninfo/bauaufsichtliches_verfahren/verfahrensfreiebauvorhaben/index.php |
| Q22 | Ministerium für Umwelt, Klima und Energiewirtschaft **Baden-Württemberg**, „Asbest in Gebäuden – die versteckte Gefahr" (PDF) | Verbot seit **31.10.1993**; betroffen u. a. **Dach- und Fassadenplatten**, Dachpappe; Gefahr beim Bearbeiten/Zerstören; **Informationspflicht des Auftraggebers** bei Vertragsanbahnung (Baujahr 1993–1996: Baubeginn); Erkundung/Probenahme; Entsorgung nur als gefährlicher Abfall. https://um.baden-wuerttemberg.de/Asbest-Flyer.pdf |
| Q25 | elektrikerwissen.de, „DIN VDE 0100-410: FI-Pflicht" | RCD **≤ 30 mA** für Steckdosen bis **32 A** und Beleuchtungsstromkreise in Wohnungen (DIN VDE 0100-410:2018-10). https://elektrikerwissen.de/din-vde-0100-410-fi-schutzschalter-pflicht |

### Hersteller und Fachquellen

| Nr. | Quelle | Belegte Zahlen |
|---|---|---|
| Q4 | **IKZ-Haustechnik**, W. Heinl, „Dachrinnen und Fallrohre dimensionieren" | DIN EN 12056-3 gilt seit **Juni 2001** als Bemessungsnorm; **DIN 18460 im Januar 2001 zurückgezogen**; vorgehängte Rinnen waren zuvor „stark vereinfacht" bemessen; hydraulischer Nachweis mit örtlicher Regenspende. https://www.ikz.de/ikz-archiv/2004/08/0408098.php |
| Q5 | **NedZink**, „Berechnung Dachentwässerung" | Q = r × ψ × A / 10.000; Tabelle 7: NG 250/DN 76 = **2,6 l/s** → 102,5/85,5/73,2/64,1 m²; NG 333/DN 100 = **4,6 l/s** → 185,9/154,9/132,8/116,2 m²; NG 400/DN 120 = **7,6 l/s** → 302,4/252,0/216,0/189,0 m²; zylindrischer Einlauf: Fläche **−30 %**; Mindest-Regenspende **300 l/(s·ha)**. https://www.nedzink.com/de/berechnung-dachentwasserung/ |
| Q6 | **Marley**, Prospekt „Dachrinnensysteme" (PDF, 08/21) | RG 70/75 bis **25 m²**, RG 100 bis **51 m²**, RG 125 bis **100 m²**, RG 150 bis **159 m²** (bei 300 l/(s·ha)); DN 53/75/90/105; **Rinneneisen 50–70 cm**; **2–3 cm Gefälle auf 10 m**; Nocke-Nut-System; Laubschutz „Laubfrei"/„Poly-Net Laubstop"; Beispiel 150 m² → 2 × 75 m² → RG 125 + DN 105. https://www.dachrinnenrechner.de/fileadmin/media/029443_Prosp._Dachrinnen_08_21_-DE-.pdf |
| Q7 | **Marley**, Montageanleitung Kasten-/Duplex-/Halbrundrinne | Schrittfolge; Rinneneisen **50–70 cm**; **2–3 cm auf 10 m**; Dachstein **⅓** in der Rinne; Traufstreifen **≥ 4 cm** Überlappung; Rinnenstutzen einhängen. https://marley.de/pages/montage-kasten-duplex-und-halbrunde-dachrinne |
| Q8 | **DAS HAUS**, „Dachrinnen: Maße und Größen" | Nenngrößen 200/250/280/333/400/500 ↔ RG 75/100/125/150/190/250; Fallrohr DN 50–150; „teilig" = Zuschnittbreite (6-teilig ≈ 33,3 cm). https://www.haus.de/bauen/dachrinnen-groessenberechnung-und-masse-28300 |
| Q10 | **starkregen.de**, „Rückstauklappe: Pflicht, Funktion und Wartung" (17.08.2026) | Rückstauebene = Straßenoberkante; **Hebeanlage** Regelfall, **Rückstauverschluss** (DIN EN 13564) nur bei untergeordneter Nutzung, kleinem Nutzerkreis, Gefälle; Wartung **2×/Jahr**, dokumentiert; Elementartarife verlangen funktionsfähige Sicherung. https://www.starkregen.de/starkregen/ratgeber/rueckstauklappe |
| Q14 | **Mall GmbH**, „Regenwassernutzung von A–Z" (Handbuch-Auszug, Stand 2017, PDF) | Ertragsbeiwert **0,3–0,8** (0,75 typisch); WC **24 l/P/d**, Waschmaschine **12 l/P/d**; Garten **60 l/m²/Jahr**; Speicher **6 %** des kleineren Werts (DIN 1989-1) bzw. **8,5 %** für 4-Wochen-Vorrat; Beispiel 6,0 / 6,8 m³; Rechenbeispiele A–F. https://www.mall.info/fileadmin/user_upload/produkte/fachbuchreihe-oekologie-aktuell/regenwassernutzung-a-z-grundlagen.pdf |
| Q15 | **Berliner Regenwasseragentur**, „Zisternengröße berechnen" | Rechenwert Abflussbeiwert **0,9**; Garten **60 l/m²/Jahr** (intensiv 100–200); Vorhaltezeit **30 Tage**; Berliner Trinkwassergebühr **1,81 €/m³**; Privatwasserzähler Wechsel alle **6 Jahre ~90 €**; jährliche Inspektion empfohlen. https://regenwasseragentur.berlin/planen-und-umsetzen/zisternengroesse-berechnen/ |
| Q16 | regenwasser-haushalt.de, „Was kostet eine Zisterne?" (18.08.2026) | Tank **1.100–4.500 €**; 3 m³ komplett **2.500–4.000 €**; 5–6 m³ **3.500–6.000 €**; 10 m³ **5.000–8.000 €**; Filter **170–420 €**; Pumpe **150–460 €**; Steuerung **200–500 €**; Einbau **1.000–2.500 €**; Amortisation **7–14 / 12–23 Jahre**; Hamburg ~**40 %** Förderung. https://www.regenwasser-haushalt.de/kosten/ |
| Q17 | Stadt **Barsinghausen**, „Förderung von Regenwasserzisternen" (2026) | Programm ab **01.06.2026**, Zuschuss **bis 1.000 €**, Antrag **nach** Fertigstellung, Windhundprinzip. **Kommunales Beispiel.** https://www.barsinghausen.de/portal/seiten/foerderung-von-regenwasserzisternen-jetzt-bis-zu-1000-euro-im-jahr-2026-1846016338-20002.html |
| Q20 | **ZAPF Garagen**, „Bodenplatte für die Garage" | Bodenplatte vs. Fundament; Fertiggarage: Boden im Werk, Fundament nach Herstellerangabe; Aufbau Aushub–Tragschicht–Schalung–Bewehrung–Betonage; typische Fehler: nicht tragfähiger Untergrund, fehlender Frostschutz, falsche Maße, schlechte Abdichtung; Streifenfundament nur mit Herstellerfreigabe. https://www.zapf-garagen.de/entdecken/bodenplatte-fuer-die-garage-kosten-aufbau-planung |
| Q21 | **Hörmann**, „Sicheres Garagentor – was muss ich beachten?" | Automatische Tore: max. **ca. 40 kg** Auftreffkraft, **Rücklauf in unter 1 Sekunde**; veraltete Anlagen erfüllen das oft nicht; Lichtschranke als Zusatzschutz; Quetschstellen an Zargen, Hebelarm, Federn; Tor und Antrieb vom gleichen Hersteller. https://hoermann.de/tipps/privates-bauen/detail/sichere-garagentore |
| Q23 | dachdecker.com, „Dachrinne erneuern Kosten [2026]" (14.10.2026) | Kunststoff **40–90 €/m**, Titanzink **50–100 €/m**, Kupfer **80–150 €/m** (inkl. Montage, Rückbau, Entsorgung); Fahrgerüst **~200 €**, Fassadengerüst 100 m² **1.700–2.000 €**. https://www.dachdecker.com/magazin/dachrinne-erneuern-kosten-202638169 |
| Q24 | nordictec, „Gefälle des Bodens in der Garage" | Gefälle **1–2 %**, Minimum **1 %**, viele Praktiker **1,5 %**; Richtung Tor, Punktablauf (kuvertförmig) oder Linienentwässerung; typische Fehler: kein Gefälle, zu großes Gefälle, ungleichmäßig. **Herstellerangabe, keine Norm.** https://nordictec-shop.eu/blog/post/gefaelle-des-bodens-in-der-garage-welche-groesse |
| Q26 | Kabelkaufhaus, „Erdkabel verlegen: Tiefe & Vorschriften" (2026) | **60 cm** im Garten, **80 cm** unter Wegen, Einfahrten, Stellplätzen; Anschluss an die Hausverteilung nur durch Fachkraft. https://kabelkaufhaus.de/blogs/gut-zu-wissen/erdkabel-verlegen-tiefe-vorschriften |

### Foren (Praxisberichte, keine Normen)

| Nr. | Quelle | Beleg |
|---|---|---|
| Q29 | bauexpertenforum.de, „Dimensionierung Dachrinne und Starkregen" | 30°-Satteldach, **112 m² je Seite** über NG 333 + **Fallrohr 100 mm**, läuft bei Starkregen über; Ursache im Thread: **verstopfter Laubschutz**, zu kleines Loch/kein Einhängstutzen („Badewanneneffekt"); „Rinnen sollen planmäßig bei extremen Starkregen überlaufen"; vorderer Rinnenrand muss tiefer liegen. https://www.bauexpertenforum.de/threads/dimensionierung-dachrinne-und-starkregen.17848/ |
| Q30 | bauexpertenforum.de, „Zisterne Überlauf nicht angeschlossen – Regreß?" | Überlauf der Zisterne nie angeschlossen; Wasser versickert unter dem Garagenboden und „sorgt ggf. für drückendes Wasser gegen meine Kellerwand"; Skimmerfunktion fehlt. https://www.bauexpertenforum.de/threads/zisterne-ueberlauf-nicht-angeschlossen-regress.56925/ |
| Q31 | bauexpertenforum.de, „Rigole?" | Rigole 20 m × 1 m × 1 m = **20 m³** Aushub und Kies, mit **Vlies und Dränrohren**, Angebot **2.200 € netto**; Kies **70 €/m³**. https://www.bauexpertenforum.de/threads/rigole.81760/ |

### YouTube (deutsch, geprüft: Titel, Kanal, Länge, Aufrufe, Datum)

| Nr. | Video | Kanal / Länge / Aufrufe | URL |
|---|---|---|---|
| Y1 | „Dachrinne montieren \| HORNBACH Meisterschmiede" | HORNBACH, **8:48**, ~1.091.600 Aufrufe (29.08.2017) | https://www.youtube.com/watch?v=Je9RGOgGHlo |
| Y2 | „Rigole \| Entwässerung auf dem Grundstück \| Vor- & Nachteile \| Arenz erklärt" | ARCenergie, **11:07**, ~24.900 Aufrufe (13.04.2023) | https://www.youtube.com/watch?v=dRwjmuf7oXk |
| Y3 | „Rigofill ST: Einbau von Rigolenfüllkörpern \| FRÄNKISCHE" | FRÄNKISCHE Deutschland, **5:42**, ~40.700 Aufrufe (28.11.2014) | https://www.youtube.com/watch?v=uxkyDLab1ng |

*YouTube-Angaben aus den Seitendaten von YouTube (lengthSeconds, viewCount, uploadDate), abgerufen 09.11.2026. Aufrufzahlen sind Momentaufnahmen. Alle 34 URLs dieses Dokuments wurden am 09.11.2026 einzeln abgerufen: durchgehend HTTP 200, keine 404.*

---

## Was ich nicht belegen konnte

1. **„Häuser aus den 60ern sind unterdimensioniert"** — als statistische Aussage unbelegt. Belegt sind nur die Mechanismen (§1.6): zurückgezogene DIN 18460, gestiegene Regenspenden, ein Ablauf pro Seite, Laub. Wer die Rinne tauscht, ohne Laubschutz und Stutzen zu prüfen, tauscht möglicherweise das falsche Teil.
2. **Eine exakte Rigolen-Dimensionierungsformel** (DWA-A 138) steht hier nicht — das Arbeitsblatt ist kostenpflichtig. Belegt sind die Randbedingungen (kf ≥ 1 × 10⁻⁶ m/s, Vorreinigung, Oberboden ≥ 20 cm, Einstau ≤ 30 cm) [Q11][Q12]. Volumen muss gerechnet werden, nicht geschätzt.
3. **Mindestabstand der Rigole zum Grundwasser** (oft „1 m zur Sohle") ließ sich in dieser Recherche nicht aus einer belastbaren Quelle belegen. Örtliche Vorgabe erfragen.
4. **Ölabscheider für private Pkw-Garagen** — keine belastbare bundesweite Pflicht gefunden. Das ist Entwässerungssatzung, nicht Bundesrecht. Wer Öl wechselt, braucht eine Auffangwanne; alles andere wäre geraten.
5. **Gefälle 5 mm/m für Dachrinnen** ist eine Empfehlung, keine Normzahl. Belegt sind 2–3 mm/m [Q6][Q7] und die Bemessungsgrenze „≤ 3 mm/m = gefällelos" [Q3].
6. **Kosten für Garage, Bodenplatte und Torantrieb** fehlen bewusst: Die Spannen hängen zu stark von Größe, Boden und Region ab, und ich hatte keine Quelle, die ich für belastbar halte. Ein Angebot ist hier die einzige Zahl mit Wert.
7. **Die Änderungen der DIN 1986-100:2026-11** konnte ich nicht prüfen (Norm kostenpflichtig, Ausgabe erst diesen Monat gelistet). Alle Zahlen dieses Dokuments stützen sich auf die 2016-12-Fassung bzw. auf Fachquellen, die diese zitieren.
8. **DIN 1989-1:2002 vs. DIN 1989-100:2022** — die 6-%-Regel stammt aus DIN 1989-1, zitiert nach [Q14] (Stand 2017). Die aktuelle Normenlage ist DIN 1989-100:2022-07 und DIN EN 16941-1:2024-05 [Q27][Q28]; ob die Prozentregel unverändert gilt, habe ich **nicht** im Volltext geprüft.
9. **Widerspruch, den ich stehen lasse:** Abflussbeiwert für Extensivgrün 0,5 [Q3] gegen 0,3 [Q5]; Ertragsbeiwert für die Zisternenbemessung 0,75 [Q14] gegen Rechenwert 0,9 [Q15]. Beide Paare sind methodisch begründbar — wer es genau braucht, rechnet mit dem Hersteller seines Systems.
