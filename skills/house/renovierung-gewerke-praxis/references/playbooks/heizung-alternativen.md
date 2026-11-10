# Heizungsalternativen im Vergleich — Pellet, Holz, Gas-Hybrid, Fernwärme, Solar, Split, Infrarot, Brennstoffzelle

> **Preisstand 09/2026.** Alle Preise sind Orientierungswerte inkl. MwSt. aus den genannten Quellen —
> regional verschieden, keine Angebote. Wer später damit rechnet, prüft sie neu.

**Stand:** 09.11.2026 · **Zielgruppe:** Eigentümer eines Ein-/Zweifamilienhauses, handwerklich begabt, kein SHK-Profi
**Grenze dieses Playbooks:** Es **vergleicht Systeme** — Auslegung, Heizlast, Vorlauftemperatur, JAZ und die Öl→Wärmepumpe-Route stehen im Parallel-Playbook `oelheizung-zu-waermepumpe.md`. Hier geht es um die Frage davor: *welches* System, zu welchem Preis, mit welcher Förderung, unter welchem Recht — und wann welches die falsche Wahl ist. Alle Preise sind **Bänder**, keine Punktpreise. Zahlen mit `[Qnn]` sind belegt; eigene Rechnungen sind als **„gerechnet"** gekennzeichnet, Schätzungen als **„Schätzung"**.

**Kurzantwort (Stand 11/2026):** Die 65-%-Regel ist am 29.07.2026 mit dem **GModG** gefallen — es gibt keine Technologiepflicht und keine Betriebsverbote für Bestandskessel mehr `[Q11][Q12]`. Damit ist die Entscheidung wieder eine Rechenaufgabe statt einer Rechtsfrage. Für ein durchschnittliches Bestandshaus mit 15.000 kWh/a liegt **Pellet** bei den laufenden Kosten vorn (≈ 9,9 ct/kWh Wärme), **Fernwärme** bei der Investition (5.000–15.000 €), **Infrarot** ist die teuerste Dauerlösung (37 ct/kWh) und nur als Insellösung vertretbar. Wer 2026 tauscht, sollte den **Förderantrag 2026 stellen**: Die förderfähigen Kosten sinken ab 01.02.2027 halbjährlich um 750 € und der Klimageschwindigkeitsbonus schmilzt ab dann um 4 Prozentpunkte pro Halbjahr `[Q13][Q36]`.

---

## 0. Was 2026 wirklich gilt (und was nicht mehr)

### 0.1 GEG → GModG: die 65-%-Regel ist weg

| Regel | Bis 28.07.2026 (GEG) | Seit 29.07.2026 (GModG) | Beleg |
|---|---|---|---|
| 65 % erneuerbare Energien bei neuer Heizung | Pflicht | **entfallen** | `[Q11][Q12]` |
| Betriebsverbot alter Kessel | ja (Stufen) | **entfallen** | `[Q12]` |
| Beratungspflicht vor Einbau | ja | **entfallen** | `[Q12]` |
| Technologieauswahl | eingeschränkt | **offen** (Katalog in § 42 Abs. 2) | `[Q01]` |
| Fossile Neuanlagen | faktisch unattraktiv | erlaubt, aber mit **Biotreppe** | `[Q02]` |

Der Gesetzeskatalog in **§ 42 Abs. 2 GModG** nennt als Optionen: Gas/Öl/Flüssiggas, elektrische Wärmepumpe, Solarthermie, Biomasse/Wasserstoff, **Wärmepumpen-Hybrid**, **Solarthermie-Hybrid**, hocheffiziente KWK, **Stromdirektheizung**, **Hausübergabestation ans Wärmenetz**, innovative Lösungen `[Q01]`. Genau diese zehn Optionen sind die acht Systeme unten (Hybrid und Solar-Hybrid zusammengefasst).

**Wichtig für Zitate alter Ratgeber:** Viele Portale schreiben 2026 noch „65 % erneuerbare Energien sind Pflicht". Baurechtlich ist das seit 29.07.2026 falsch `[Q11][Q12]`. Die KfW verlangt für die Förderung nur eine **Verbesserung** des EE-Anteils bzw. der Effizienz, keine 65-%-Schwelle `[Q10]`; einzelne Portale führen die 65 % trotzdem noch als Förderbedingung (z. B. ADAC zur Split-Anlage `[Q20]`) — dieser Widerspruch ist ungeklärt, siehe § 14.

### 0.2 Die Biotreppe für Gas und Öl (§ 43)

Wer **nach dem 29.07.2026** eine neue Gas-, Öl- oder Flüssiggasheizung einbaut, muss ab 2029 steigende Anteile biogener/klimaneutraler Brennstoffe einsetzen `[Q02]`:

| ab 01.01. | 2029 | 2030 | 2035 | 2040 |
|---|---|---|---|---|
| Mindestanteil | **10 %** | **15 %** | **30 %** | **60 %** |

Drei Auswege sind im Gesetz ausdrücklich geregelt:
- **Solarthermie** kann die Pflicht erfüllen, wenn sie 0,04 m² Aperturfläche je m² Nutzfläche hat (bei ≤ 2 Wohnungen; 0,03 m² bei mehr) — für 2029–2034 `[Q02, Abs. 3]`.
- **Wärmepumpen-Hybrid** erfüllt die Pflicht, wenn die WP am Teillastpunkt A mindestens **30 %** (bivalent parallel) bzw. **40 %** (bivalent alternativ) der Spitzenlastleistung bringt `[Q02, Abs. 5]`.
- **Biomasse-Hybrid** erfüllt sie durch den Biomasseanteil `[Q03, Abs. 2]`.

Die Grüngas-/Grünheizölquote selbst kommt erst: § 42a verpflichtet die Bundesregierung, bis **01.12.2026** ein Gesetz vorzulegen, das die Inverkehrbringer ab 2045 vollständig auf klimaneutrale Brennstoffe umstellt `[Q01a]`. Wer heute Gas einbaut, kauft also **keine Bestandsgarantie für den Brennstoffpreis**, sondern eine Technik mit steigendem Bioanteil.

### 0.3 Stromdirektheizung: erlaubt, aber nur unter einer Bedingung (§ 46)

§ 46 GModG ist die einzige echte Einbaubremse, die geblieben ist: Eine **Stromdirektheizung** (dazu zählt die Infrarotheizung) darf in ein bestehendes Wohngebäude nur eingebaut werden, wenn das Gebäude die Anforderungen an den baulichen Wärmeschutz nach §§ 16, 19 **um mindestens 30 % unterschreitet** — also deutlich besser ist als der GModG-Referenzwert. Ausnahme: Gebäude mit **höchstens zwei Wohnungen, von denen der Eigentümer eine selbst bewohnt**; und der **Austausch** einer bestehenden Einzelraum-Stromdirektheizung ist immer zulässig `[Q04]`.

Praktisch: Im eigenen Einfamilienhaus ist Infrarot damit **rechtlich meist möglich** — die Hürde ist nicht das Gesetz, sondern der Strompreis (siehe § 7).

### 0.4 Förderung 2026: 30 % + 16 % + 10–40 %, gedeckelt bei 28.000 €

Seit **21.07.2026** gilt (KfW 458) `[Q10][Q13]`:

| Baustein | Satz | Bedingung |
|---|---|---|
| Grundförderung | **30 %** | Sanierung eines Bestandsgebäudes (Bauantrag ≥ 5 Jahre alt), hydraulischer Abgleich |
| Klimageschwindigkeitsbonus | **16 %** | selbstgenutzt, Austausch einer funktionsfähigen Öl-/Kohle-/Gasetagen-/Nachtspeicherheizung oder ≥ 20 Jahre alten Gas-/Biomasseheizung |
| Einkommensbonus | **10 / 30 / 40 %** | zu versteuerndes Haushaltseinkommen ≤ 50.000 / 40.000 / 30.000 € (Familienzuschlag +10.000 €) |
| Maximum | **80 %** (KfW) bzw. **70 %** ohne Kinderzuschlag (Fachquelle) | Widerspruch siehe § 9 |

**Deckel:** 28.000 € förderfähige Kosten für die erste Wohneinheit, 15.000 € je weiterer (2. WE = 43.000 €; ab 7. WE 8.000 €) `[Q10]`. Der Deckel sinkt ab **01.02.2027** alle sechs Monate um **750 €** bis 22.000 € im Jahr 2030; der Klimageschwindigkeitsbonus sinkt ab dann um **4 Prozentpunkte** pro Halbjahr und läuft voraussichtlich im 2. Halbjahr 2028 aus `[Q13]`.

**Was 2026 außerdem wegfiel:** der Effizienzbonus (5 %) und der Emissionsminderungszuschlag (2.500 € Pauschale für Biomasse ≤ 2,5 mg/m³) `[Q13][Q14]`. Ab **01.10.2027** wird der strenge Staubwert von **2,5 mg/m³** ohnehin Pflicht für neue Biomasseanlagen; aktuell gefördert werden Pelletkessel bis 10 mg/m³, Pelletöfen/Scheitholz bis 15 mg/m³ `[Q14]`.

**Förderfähig sind** ausdrücklich: Solarthermie, Biomasseheizungen, elektrische Wärmepumpen, Brennstoffzellenheizungen, wasserstofffähige Heizungen, Anschluss an ein Gebäude-/Wärmenetz, provisorische Heiztechnik bei Defekt, Fachplanung, akustische Planung, Umfeldmaßnahmen `[Q10]`. **Nicht** förderfähig: reine Gas-/Ölheizung ohne EE-Anteil, reine Kaminöfen ohne Wassertasche (KfW listet „Pelletöfen mit Wassertasche") `[Q10][Q33]`.

### 0.5 Die drei Fristen, die 2026 zählen

1. **31.12.2026:** Antrag noch 2026 stellen sichert 28.000 € Deckel + 16 % Klimabonus. Nach Antrag hat man **drei Jahre** Zeit für die Umsetzung `[Q36]`.
2. **01.02.2027:** erster Abschlag beim Deckel (−750 €) und beim Klimabonus (−4 pp) `[Q13]`.
3. **01.10.2027:** 2,5 mg/m³ Staubgrenzwert für neue Biomasseanlagen — betrifft die Produktauswahl, nicht den Bestand `[Q14]`.

---

## 1. Pelletheizung

**Wie es funktioniert.** Holzpellets (ENplus A1) werden per Schnecke oder Saugsystem aus einem Lager in den Kessel gefördert, dort automatisch gezündet und verbrannt; ein Pufferspeicher entkoppelt Kessel und Heizkreis, die Asche landet in einem Behälter, der je nach Anlage alle paar Wochen geleert wird `[Q18][Q26]`. Wirkungsgrad moderner Kessel: **bis 95 %** (Heizwert), Brennwertkessel nach Herstellerangaben darüber `[Q18][Q35]`.

**Für wen.** Bestand mit mittlerer bis hoher Heizlast (15.000 kWh/a und mehr), Keller oder Nebenraum mit **3–10 m²** Lagerfläche, Zufahrt für einen Silowagen (Einblasen), kein Gasnetz oder kein Fernwärmeanschluss `[Q26][Q18]`. Nicht für Passivhaus, nicht für Innenstadt-Reihenhaus ohne Lieferweg.

**Investition.** **15.000–25.000 €** inkl. Montage und Lager `[Q18]`; eine zweite Marktquelle nennt **25.000–30.000 €** `[Q16]` — die Spanne ist echt, sie hängt an Kessel (4.000–14.000 €), Lager (2.000–9.000 €) und Puffer (700–2.000 €) `[Q18]`.

**Betriebskosten je kWh Wärme.** Pellets kosteten am 09.11.2026 **436,09 €/t** (6-t-Abnahme, inkl. MwSt. und Lieferung) `[Q16]`. Bei 4,9 kWh/kg Heizwert `[Q34]` sind das **8,9 ct/kWh** Brennstoff; bei 90 % Kesselwirkungsgrad **9,9 ct/kWh Wärme** (gerechnet), bei 85 % 10,5 ct. ADAC nennt **7–9 ct/kWh** (Stand 2025) `[Q18]` — der Unterschied ist der Pelletpreis, nicht die Physik (siehe § 9).

**Jahresbedarf/Lager.** Für 15.000 kWh: **3,4 t** Pellets, rund **5,1 m³** Schüttvolumen (1,5 m³/t `[Q34]`) — praktisch 6–9 m³, wenn man eine Lieferung pro Jahr plus Reserve will.

**Wie die Pellets aus dem Lager in den Kessel kommen.** Zwei Systeme, zwei Grenzen: Die **Förderschnecke** ist das mechanische System für kurze Wege — geräuscharm, wenig Strom, aber je gerader und kürzer, desto weniger Abrieb. Das **pneumatische Saugsystem** überbrückt bis zu **30 m** Entfernung und schafft **Steigungen bis 6 m**, ist dafür lauter und stromhungriger; Abhilfe ist ein größerer Vorratsbehälter am Kessel, der nur außerhalb der Ruhezeiten gefüllt wird. Entscheidend ist in beiden Fällen wenig **Feinabrieb**: Er verstopft Förderwege und führt zu Betriebsstörungen am Kessel [BauNetz Pellet-Austragung](https://www.baunetzwissen.de/heizung/fachwissen/brennstofflagerung/austragungssysteme-fuer-pelletheizungen-5385903) (geprüft 09.11.2026).

**Was das für den Lagerraum bedeutet.** Das Lager muss nicht nur groß genug sein (§ oben), sondern zur Austragung passen: Schrägboden mit Entnahmeschnecke am tiefsten Punkt oder ebener Boden mit Bodenrührwerk oder Saugsonden. Wer den Raum später umnutzen will, plant die Entnahmetechnik an der Wand, nicht in der Raummitte.

**Förderung 2026.** 30 % Grundförderung; mit Klimabonus 16 % und Einkommensbonus 10–40 % sind **56–80 %** möglich, bezogen auf max. 28.000 € `[Q10][Q13]`. Voraussetzung: Staub ≤ 10 mg/m³ (Pelletkessel) `[Q14]`, Pufferspeicher, hydraulischer Abgleich `[Q10][Q18]`.

**Rechtliche Hürden.**
- § 45 GModG: Nur **Biomassekessel oder Biomasseofen mit Wasser** als Wärmeträger; Brennstoff nur nach § 3 Abs. 1 Nr. 4, 5, 5a, 6, 7, 8, 13 der 1. BImSchV `[Q03]`.
- 1. BImSchV § 5 Abs. 1 Stufe 2 (Anlagen nach 31.12.2014): **20 mg/m³ Staub, 0,4 g/m³ CO** (bezogen auf 13 % O₂) `[Q07]`.
- 1. BImSchV § 5 Abs. 4: **Pufferspeicher mindestens 55 l/kW** bei handbeschickten Anlagen, **20 l/kW** bei automatisch beschickten `[Q07]`.
- 1. BImSchV § 15 Abs. 1: Der Schornsteinfeger misst **alle zwei Kalenderjahre** `[Q08]`.
- Schornstein und Feuerstättenschau sind Pflicht; ein bestehender Schornstein muss meist saniert oder ein Edelstahlrohr eingezogen werden (Erfahrungswert, keine Quelle).

**Wartung/Aufwand.** **150–300 €/a** Wartung plus **50–100 €/a** Strom für Schnecke/Steuerung `[Q18]`; dazu Schornsteinfeger und Asche. Wer im Urlaub ist, braucht jemanden, der im Notfall den Kessel quittiert.

**Wann es die falsche Wahl ist.**
- Kleiner Wärmebedarf oder sehr gut gedämmtes Haus: Dann ist die Investition nicht amortisierbar, und die Wärmepumpe gewinnt bei den Vollkosten.
- Kein trockener Lagerraum und kein Einblasweg: Ein Erdtank im Garten kostet zusätzlich und braucht Genehmigung/Platz (Erfahrungswert).
- Enge Nachbarschaft: Feinstaub und Geruch sind der soziale Sprengstoff; das **UBA bewertet Holzheizungen 2025 insgesamt als klimaschädlicher als Öl- und Gasheizungen**, weil es die Verbrennungsemissionen mitrechnet `[Q33]` (via `[Q34]`-Umfeld; siehe § 9).

---

## 2. Scheitholz / Kaminofen

**Wie es funktioniert.** Zwei verschiedene Dinge, die oft verwechselt werden: Der **Holzvergaser-Kessel** (zentral, wassergeführt) verbrennt Scheitholz in Chargen, gibt die Wärme an einen Pufferspeicher und versorgt das ganze Haus `[Q27]`. Der **Kaminofen** heizt einen Raum, ein **wasserführender Ofen** zusätzlich den Heizkreis `[Q27]`. Beides braucht Handarbeit: Holzen, Spalten, Trocknen, Nachlegen.

**Für wen.** Eigene Holzquelle (Wald, Restholz, Nachbarschaft), körperlich fit, trockener Lagerplatz für 10–15 m³, Pufferplatz im Heizraum. Nicht für Menschen, die im Winter verreisen oder keine Lust auf tägliches Nachlegen haben.

**Investition.** Holzvergaser-Kessel **5.000–8.000 €** für ein typisches EFH (Kessel allein) `[Q27]`; mit Puffer, Hydraulik, Schornstein und Montage realistisch **15.000–25.000 €** (**Schätzung**, keine Quelle für das Komplettpaket). Kaminofen **ab ~500 €**, Kachelofen **> 5.000 €**, wasserführender Ofen **2.500–3.000 €** `[Q27]`.

**Betriebskosten je kWh Wärme.** TFZ Bayern, Juli 2026: **Buche 144,70 €/Rm** (33 cm, inkl. MwSt., Lieferung ≤ 10 km) bzw. **Fichte 109,80 €/Rm**; umgerechnet **9,40 ct/kWh** (Buche) und **9,64 ct/kWh** (Fichte) **bezogen auf den Heizwert** `[Q17]`. Bei 85 % Kesselwirkungsgrad sind das **11,1 ct/kWh Wärme** (gerechnet); ein Kaminofen mit 70–75 % liegt höher.

**Jahresbedarf/Lager.** 15.000 kWh ÷ (1.540 kWh/Rm × 0,85) ≈ **11,5 Rm** Buche (gerechnet aus `[Q17]`). Das sind je nach Scheitlänge **12–18 m³** Lagerraum, überdacht und belüftet — der größte Platzbedarf aller Systeme hier.

**Förderung 2026.** Kessel: 30 % + 16 % + 10–40 % wie bei Pellet `[Q10][Q13]`. **Reiner Kaminofen: keine Förderung** — die KfW-Liste führt Biomasseheizungen und **Pelletöfen mit Wassertasche** `[Q10][Q33]`.

**Rechtliche Hürden.**
- § 45 GModG: nur Kessel oder **Biomasseofen mit Wasser**; reine Raumheizgeräte erfüllen die Anforderung nicht `[Q03]`.
- 1. BImSchV § 4 Abs. 3: Einzelraumfeuerungen müssen typgeprüft sein; § 4 Abs. 8: Betreiber handbeschickter Anlagen müssen sich **innerhalb eines Jahres nach Errichtung oder Betreiberwechsel** von der Schornsteinfegerin/dem Schornsteinfeger **beraten lassen** `[Q07]`.
- 1. BImSchV § 15 Abs. 2: Feuerstättenschau für Einzelraumfeuerungen `[Q08]`.
- 1. BImSchV § 25: Übergangsregeln für alte Kessel — Bestandsanlagen mit Errichtungsdatum bis 1994 mussten Stufe 1 ab 2015 einhalten, 1995–2004 ab 2019, 2005–2010 ab 2025 `[Q09]`.
- Pufferspeicher: **55 l/kW** bei handbeschickten Anlagen `[Q07]` — bei 15 kW also **825 l**.

**Wartung/Aufwand.** Schornsteinfeger, Asche täglich, Kesselreinigung wöchentlich, Holzlogistik 2–4 Wochen Arbeit pro Jahr (Erfahrungswert). Kein Komfortanspruch: Wer morgens duschen will, heizt abends vorher.

**Wann es die falsche Wahl ist.**
- Keine eigene, günstige Holzquelle: Dann ist der Preisvorteil gegenüber Pellets (9,4 vs. 8,9 ct/kWh) weg und die Arbeit bleibt.
- Platzmangel für Puffer und Holz.
- Luftreinhaltegebiet/Feinstaubhotspot: Das UBA nennt für **Kaminöfen im Mittel 0,31 g/kWh Staub und 7,4 g/kWh CO**, für Scheitholzkessel 0,117 g/kWh Staub `[Q33]` — Kaminöfen sind die schmutzigste Option.
- Mietwohnung/Denkmal: Ofen anschließen und Schornstein sanieren ist oft unverhältnismäßig.

---

## 3. Gas-Brennwert und Gas-Hybrid

**Wie es funktioniert.** Gas-Brennwert nutzt zusätzlich die Kondensationswärme des Abgases, moduliert die Leistung und braucht nur einen Gasanschluss, 1–2 m² Wandfläche und einen Luft-/Abgasanschluss `[Q23]`. **Hybrid** kombiniert eine kleine Luft-Wasser-Wärmepumpe mit dem Gaskessel; eine Regelung entscheidet nach Außentemperatur, wer heizt `[Q22]`.

**Für wen.** Gas-Brennwert: Gebäude mit vorhandenem Gasanschluss, knappem Budget und unsicherer Perspektive (Verkauf, Altersteilzeit). Hybrid: Bestand mit Heizkörpern, die bei 45–55 °C nicht mehr reichen, aber eine WP als Grundlastträger sinnvoll ist — und ein großer Heizraum.

**Investition.** Gas-Brennwert inkl. Installation **9.000–15.500 €** `[Q23]` (Basismodelle ab 3.000 € + Einbau). Hybrid komplett **36.000–65.000 €**, weil zwei vollwertige Systeme bezahlt werden `[Q22]`.

**Betriebskosten je kWh Wärme.** Erdgas kostete im August 2026 **12,45 ct/kWh** (BDEW, inkl. Grundpreisanteil), im Jahresschnitt 2026 bisher 11,93 ct `[Q15]`. Bei 90 % Wirkungsgrad: **13,8 ct/kWh Wärme** (gerechnet). Hybrid: bei 70 % WP-Anteil (JAZ 3,0, WP-Strom 27,44 ct) und 30 % Gas **10,6 ct/kWh** (gerechnet) `[Q15]`.

**Platz.** Gas-Brennwert 1–2 m², Hybrid zusätzlich Außengerät und großer Puffer `[Q22]`.

**Förderung 2026.** **Gas-Brennwert allein: 0 %** `[Q23]`. Hybrid: gefördert wird **nur der Wärmepumpenteil**, nicht der Gaskessel — dadurch ist der Förderanteil auf die Gesamtinvestition deutlich niedriger als bei einer reinen WP `[Q22]`.

**Rechtliche Hürden.**
- **Biotreppe** § 43: 10 % ab 2029, 15 % ab 2030, 30 % ab 2035, 60 % ab 2040 `[Q02]`.
- **Hybrid-Ausnahme** § 43 Abs. 5: WP ≥ 30 % (bivalent parallel) bzw. 40 % (bivalent alternativ) der Spitzenlast `[Q02]`.
- **Grüngasquote** kommt bis 01.12.2026 als Gesetz `[Q01a]`.
- 1. BImSchV § 15 Abs. 3: Schornsteinfegermessung alle **3 Jahre** (Anlage < 12 Jahre alt), sonst alle **2 Jahre** `[Q08]`.
- Kein Betriebsverbot mehr für alte Kessel `[Q12]` — aber der Netzausbau und die CO₂-Kosten bleiben ein Risiko.

**Wartung.** **150–250 €/a** Wartung plus Schornsteinfeger; Hybrid: **doppelte Wartung** (WP + Gas) `[Q22]`.

**Wann es die falsche Wahl ist.**
- Gut gedämmtes Haus/Neubau: Die WP ist bei gleicher Förderung günstiger im Betrieb, der Gasteil ist totes Kapital `[Q22]`.
- Hybrid als „Sicherheitsnetz": 36.000–65.000 € Investition für ein Backup, das man mit einem Heizstab oder einer größeren WP billiger haben kann `[Q22]`.
- Wenn die Biotreppe ab 2029 teure Biomethan-Anteile erzwingt und kein Solarthermie-/Hybrid-Ausweg vorhanden ist `[Q02]`.

---

## 4. Fernwärme

**Wie es funktioniert.** Kein Kessel im Haus: Eine **Hausübergabestation** mit Wärmetauscher, Regelung und Wärmemengenzähler übernimmt die Wärme aus dem Netz; im Haus gibt es keine Verbrennung und keinen Abgasweg `[Q28]`.

**Für wen.** Grundstücke im Netzgebiet, dichte Bebauung, kein Platz für Kessel/Lager, kein Interesse an Brennstofflogistik. Nicht für Grundstücke ohne Netz — ein Anschluss „auf Vorrat" gibt es nicht.

**Investition.** Hausanschluss/Hausstation **5.000–15.000 €** `[Q29]`; eine andere Quelle nennt **7.500–20.000 €** plus Montage für den Wärmeübertrager `[Q28]`.

**Betriebskosten je kWh Wärme.** AGFW, mengengewichtet zum 01.01.2026: **15,7 ct/kWh** `[Q30]`; VZBV-Median für Einfamilienhäuser **~17 ct/kWh** `[Q30]`; Marktband **8–22 ct/kWh**, typisch 12–18 ct `[Q29]`. Dazu **Grundpreis 200–800 €/a** `[Q29]` bzw. **50–150 €/kW und Jahr** (bei 15 kW: 750–2.250 €/a) `[Q28]`. Für das Rechenbeispiel: 16,5 ct/kWh + 500 €/a Grundpreis.

**Platz.** 1–2 m² für die Station, kein Lager, kein Schornstein `[Q28]`.

**Förderung 2026.** Anschluss an ein Wärmenetz ist förderfähig: 30 % Grundförderung, mit Boni bis 70/80 % `[Q10][Q29]`.

**Rechtliche Hürden.**
- **Anschluss- und Benutzungszwang**: Gemeinden können ihn über Landesrecht auch zum Klimaschutz begründen — § 109 GModG `[Q05]`. Wer im Zwangsgebiet liegt, hat keine Wahl `[Q28]`.
- **Kein Anbieterwechsel**: pro Netzgebiet ein regionales Monopol — Planung und Betrieb von Kraftwerk und Netz liegen beim selben Unternehmen, ein Wechsel ist nicht möglich [VZ Fernwärme](https://www.verbraucherzentrale.de/wissen/energie/heizen-und-warmwasser/fernwaerme-kosten-sparen-und-gleichzeitig-das-klima-schonen-34038) (geprüft 09.11.2026, Stand 09.07.2025) `[Q29]`.
- **Vertragslaufzeit** bis 10 Jahre, automatische Verlängerung um 5 Jahre, Kündigung 9 Monate vor Ablauf (§ 32 AVBFernwärmeV) `[Q29]`; die Verbraucherzentrale nennt dieselbe Obergrenze von **zehn Jahren** [VZ Fernwärme](https://www.verbraucherzentrale.de/wissen/energie/heizen-und-warmwasser/fernwaerme-kosten-sparen-und-gleichzeitig-das-klima-schonen-34038) (geprüft 09.11.2026).
- **Preisänderungsklauseln sind an Indexe gekoppelt** und werden jährlich angepasst `[Q28]`. Was sie dürfen, steht in § 24 Abs. 4 AVBFernwärmeV: Sie müssen **Kostenentwicklung bei Erzeugung und Bereitstellung** *und* die **Verhältnisse auf dem Wärmemarkt** angemessen berücksichtigen, die maßgeblichen Berechnungsfaktoren **vollständig und allgemein verständlich** ausweisen und den **Brennstoffkostenanteil** an der Änderung gesondert nennen; einseitig per öffentlicher Bekanntgabe darf die Klausel nicht geändert werden [AVBFernwärmeV § 24](https://www.gesetze-im-internet.de/avbfernw_rmev/__24.html) (geprüft 09.11.2026)`. Für die Vertragsprüfung heißt das: Index, Gewichtung und Basisjahr müssen im Vertrag stehen — fehlt der Brennstoffanteil, ist die Klausel angreifbar.
- **Woher die Wärme kommt:** Bundesweit rund **zwei Drittel fossil**, **20 % erneuerbar**, **9 % Abwärme**, **5 % nicht biogener Abfall** — der CO₂-Faktor ist damit eine Frage des Netzes, nicht der Technik [VZ Fernwärme](https://www.verbraucherzentrale.de/wissen/energie/heizen-und-warmwasser/fernwaerme-kosten-sparen-und-gleichzeitig-das-klima-schonen-34038) (geprüft 09.11.2026).

**Wartung.** Minimal — die Station gehört dem Versorger; Wartung/Reparatur sind eingepreist (Erfahrungswert).

**Wann es die falsche Wahl ist.**
- Hoher Arbeitspreis bei hohem Verbrauch: Bei 16,5 ct/kWh zahlt das Musterhaus **2.475 €/a** nur für Wärme — mehr als Gas (2.075 €) und deutlich mehr als Pellets (1.483 €) `[Q15][Q30]` (gerechnet).
- Netz mit hohem fossilen Anteil: Die CO₂-Belastung ist netzabhängig und liegt **teils über 300 g/kWh** `[Q29]` — dann ist die Wärme klimatisch nicht besser als Gas.
- Wenn man Wert auf Wechselmöglichkeit legt: Es gibt sie nicht `[Q29]`.

---

## 5. Solarthermie

**Wie es funktioniert.** Flach- oder Röhrenkollektoren auf Dach/Fassade erwärmen eine Trägerflüssigkeit; über Pumpe und Wärmetauscher geht die Wärme in einen Pufferspeicher. Im Sommer deckt die Anlage oft das Warmwasser komplett, im Winter unterstützt sie die Heizung `[Q19][Q24]`.

**Für wen.** Südlage mit 3–6 m² (nur Warmwasser) bzw. 9–20 m² (Warmwasser + Heizung), ausreichend Puffervolumen (250–350 l bzw. 500–1.500 l) `[Q24]`. Immer **als Ergänzung**, nie als alleinige Heizung `[Q19]`.

**Der Deckungsgrad entscheidet über die Wirtschaftlichkeit**, nicht die Kollektorfläche allein. Drei Bänder, drei Charaktere [BauNetz Solardeckungsgrad](https://www.baunetzwissen.de/solar/fachwissen/solarwaerme/kollektorflaeche-und-solarer-deckungsgrad-165858) (geprüft 09.11.2026):

| solarer Deckungsgrad | Charakter | Folge |
|---|---|---|
| **unter 40 %** | klein, günstig | Kollektorwärme im Sommer voll genutzt, Defizit aus dem Kessel; bei Mehrfamilienhäusern üblich (30–45 %) |
| **40–60 %** | Kompromiss fürs Einfamilienhaus | bei **60 %** ist der Warmwasserbedarf im Sommer gedeckt, der Kessel bleibt aus |
| **über 70 %** | maximale Abdeckung | große Flächen, hohe Sommerüberschüsse, **niedrigerer Nutzungsgrad**, aufwendig und teuer |

Für die **Heizungsunterstützung** gibt es keinen Standardwert: Der Deckungsgrad hängt an der energetischen Qualität des Gebäudes — im Passivhaus sind rund **50 %** erreichbar [BauNetz Solardeckungsgrad](https://www.baunetzwissen.de/solar/fachwissen/solarwaerme/kollektorflaeche-und-solarer-deckungsgrad-165858) (geprüft 09.11.2026). Wer mit „70 % Deckung“ wirbt, verkauft Sommerüberschüsse als Ertrag.

**Investition.** Verbraucherzentrale (Stand 2025): **6.000–10.000 €** nur Warmwasser, **9.000–17.000 €** Warmwasser + Heizung `[Q24]`. ADAC (Juli 2026): **3.000–6.000 €** bzw. **7.000–10.000 €**, Kombianlage 7.000–17.000 € `[Q19]`. Pro m² Kollektor 250–600 € (Flach) bzw. 350–800 € (Röhre) `[Q19]`.

**Betriebskosten je kWh Wärme.** Kein Brennstoff; laufende Kosten **100–200 €/a** `[Q19]`. Vollkosten gerechnet: 13.000 € Investition, 300 kWh/m²·a bei 15 m² = 4.500 kWh/a, 20 Jahre → **~14 ct/kWh** (gerechnet, ohne Kapitalkosten und ohne Förderung); mit 56 % Förderung ~6–7 ct/kWh. Das ist eine ** eigene Rechnung**, keine Marktzahl.

**Platz.** Dachfläche 3–6 m² bzw. 9–20 m²; Speicher 250–350 l bzw. 500–1.500 l im Haus `[Q24]`.

**Förderung 2026.** 30 % + Boni über KfW 458 `[Q10]`. Technische Voraussetzungen: **Solar-Keymark**-Zertifizierung, Mindestertrag **525 kWh/m²·a**, Funktionskontrollgerät, Wärmemengenzähler bei Vakuumkollektoren, Listung in der BAFA-Liste `[Q19]`. § 44 GModG verlangt die Keymark-Zertifizierung auch baurechtlich `[Q06a]`.

**Rechtliche Hürden.** Keine Feuerstätte, kein Schornstein, keine BImSchV. Aber: **Dachflächenkonkurrenz zur PV** — die Verbraucherzentrale sagt ausdrücklich, dass bei kleinen Dächern vieles für PV spricht `[Q24]`. Bei Denkmal: Gestaltungssatzung prüfen (Erfahrungswert).

**Wartung.** **100–200 €/a** `[Q19]`, plus Sichtprüfung, Druck, Frostschutz; Stagnation im Sommer ist normal und muss konstruktiv beherrscht werden (Erfahrungswert).

**Wann es die falsche Wahl ist.**
- Kleines Dach und hoher Strombedarf: PV + Wärmepumpe ist wirtschaftlicher `[Q24]`.
- Sehr geringer Warmwasserverbrauch (1–2 Personen): Die Anlage amortisiert sich nicht.
- Wenn sie als „Heizungsersatz" verkauft wird: Sie liefert im Dezember/Januar nur einen Bruchteil `[Q19]`.

---

## 6. Luft-Luft-Wärmepumpe / Split-Klimaanlage

**Wie es funktioniert.** Ein umkehrbarer Kältemittelkreislauf: Das Außengerät entzieht der Luft Wärme, das Innengerät gibt sie an den Raum ab. Technisch ist die Split-Anlage eine **Luft-Luft-Wärmepumpe** `[Q20]`. Kennzahlen: **SCOP 4–5** bei guten Geräten, reale **Jahresarbeitszahl 2,5–3,5** `[Q20]`.

**Für wen.** Gut gedämmte Häuser, einzelne Räume, Übergangszeit-Heizen, Kühlbedarf im Sommer. **Keine Warmwasserbereitung** — das ist die entscheidende Grenze `[Q20]`.

**Investition.** Mono-Split inkl. Montage **1.500–3.500 €**, Multi-Split mit 2–3 Innengeräten **3.500–7.000 €** `[Q20]`; ein ganzes Haus ist deutlich teurer.

**Betriebskosten je kWh Wärme.** Bei JAZ 3,0 und Haushaltsstrom 37,0 ct/kWh: **12,3 ct/kWh** (gerechnet); mit separatem Wärmepumpentarif 27,44 ct/kWh `[Q15]` und JAZ 3,0: **9,1 ct/kWh**. Bei SCOP 4 und 37 ct: 9,25 ct/kWh.

**Platz.** Innengerät an der Wand, Außengerät ca. 0,5–1 m² mit Abstand zur Nachbarwand; Kältemittelleitung durch die Wand `[Q20]`.

**Förderung 2026.** Nur **fest installierte** Anlagen, die **primär für den Heizbetrieb** ausgelegt sind, sind über KfW 458 förderfähig; reine Kühlgeräte und Monoblöcke nicht `[Q20]`. ADAC nennt zusätzlich die 65-%-EE-Bedingung `[Q20]` — siehe Widerspruch § 9.

**Rechtliche Hürden.** Keine BImSchV, kein Schornstein. Relevant sind **Lärmschutz** (TA Lärm, Abstand zum Nachbarfenster) und bei Mietwohnung die Zustimmung des Eigentümers `[Q20]`. Bei ganzjähriger Nutzung als Hauptheizung greift § 42 Abs. 2 Nr. 2 GModG (Wärmepumpe) — kein Stromdirektheizungs-Verbot.

**Wartung.** Jährliche Fachwartung empfohlen, **ca. 100–200 €/a** (Erfahrungswert; ADAC nennt nur die Empfehlung) `[Q20]`.

**Wann es die falsche Wahl ist.**
- Als **alleinige** Hausheizung: keine Warmwasserbereitung, in kalten Nächten schlechterer COP, Luftzug und Geräusche `[Q20]`.
- Schlecht gedämmtes Haus: Dann heizt sie teurer als Gas.
- Schlafzimmer/Homeoffice mit Geräuschempfindlichkeit: Außengerät und Luftstrom sind der Kompromiss `[Q20]`.

---

## 7. Infrarot / Elektro-Direktheizung

**Wie es funktioniert.** Heizpaneele oder Deckenstrahler wandeln Strom direkt in Wärme und Strahlung: **1 kWh Strom = 1 kWh Wärme**, physikalisch ohne Verlust, aber auch ohne Gewinn `[Q25][Q37]`. Kein Kessel, kein Wasser, kein Schornstein.

**Für wen.** Einzelne Räume (Bad, Gästezimmer, Werkstatt), selten genutzte Räume, Häuser mit sehr niedrigem Wärmebedarf, PV-Überschuss im Winter. **Nicht** für die Grundversorgung eines normalen Einfamilienhauses `[Q25][Q37]`.

**Investition.** Wandpaneel 300–600 W: **100–250 €**; 800–1.200 W: **150–400 €**; Deckenheizung 250–500 €; komplette 50-m²-Wohnung **1.500–2.500 €** `[Q40]`. Fest angeschlossene Geräte (Bad) gehören in Elektrikerhand `[Q40]`.

**Betriebskosten je kWh Wärme.** **37,0 ct/kWh** (BDEW-Haushaltsstrom August 2026) `[Q15]` — bei COP 1 also **37 ct/kWh Wärme**. Für 15.000 kWh: **5.550 €/a**. Ein günstiger Heizstromtarif existiert oft nicht, die Verbraucherzentrale warnt ausdrücklich `[Q25]`.

**Platz.** Null — das ist der einzige echte Vorteil neben dem Preis `[Q40]`.

**Förderung 2026.** **Keine.** Stromdirektheizungen sind nicht in der KfW-Liste `[Q10]`.

**Rechtliche Hürden.** § 46 GModG: Einbau in bestehende Wohngebäude nur, wenn der bauliche Wärmeschutz die Anforderungen um **≥ 30 % unterschreitet**; Ausnahme für selbstgenutzte Gebäude mit **≤ 2 Wohnungen** und für den **Austausch** einer bestehenden Einzelraum-Stromdirektheizung `[Q04]`. Im eigenen EFH ist die Ausnahme der Regelfall — man sollte sie aber kennen, bevor man ein Mehrfamilienhaus umrüstet.

**Wartung.** Keine. Kein Schornsteinfeger, keine Brennstofflogistik `[Q40]`.

**Wann es die falsche Wahl ist.**
- Immer, wenn es die **Hauptheizung** eines Hauses mit mehr als Passivhaus-Standard ist: 37 ct/kWh gegen 9,9 ct (Pellet) oder 13,8 ct (Gas) ist kein knapper Unterschied, sondern der Faktor 3–4 `[Q15][Q25]`.
- Wenn jemand mit „50 €/Monat" wirbt: Im Fachforum wird genau das zerlegt — „1 kWh elektrische Energie ergibt 1 kWh Wärmeenergie. Einfache Physik, aber immer gültig" `[Q37]`.
- Als Ersatz für eine funktionierende Zentralheizung: Die Verbraucherzentrale nennt sie eine **„kostenintensive Notlösung"** `[Q25]`.

---

## 8. Brennstoffzelle

**Wie es funktioniert.** Gas (Erdgas/Biomethan) wird reformiert, der Wasserstoff reagiert in der Zelle mit Sauerstoff zu Wasser — dabei entstehen Strom und Wärme, ohne offene Flamme. Zwei Zelltypen im EFH: **PEM** (niedrige Temperatur, schneller Start, Reformer; z. B. Viessmann Vitovalor) und **SOFC** (Hochtemperatur, höherer elektrischer Wirkungsgrad; BlueGen, Dachs InnoGen). Gesamtwirkungsgrad **bis ~90 %** `[Q21]`.

**Für wen.** Große Häuser mit **hohem, gleichmäßigem Strom- und Wärmebedarf** (Pool, Gewerbe im Haus, Elektroauto, mehrere Personen dauerhaft zu Hause). Nicht für ein normales EFH mit 15.000 kWh — dort ist die Zelle unterfordert und der Stromüberschuss wird schlecht vergütet `[Q21]`.

**Investition.** PEM **25.000–30.000 €**, SOFC **30.000–35.000 €**, jeweils inkl. Einbau `[Q21]`.

**Betriebskosten je kWh Wärme.** Gas 2026 ~12 ct/kWh `[Q21]`. Weil die Zelle Strom und Wärme koppelt, hängt der Wärmepreis am **Eigenverbrauch des Stroms**: Wer den Strom zu 37 ct/kWh selbst verbraucht, rechnet ihn gegen und landet bei grob **10–15 ct/kWh Wärme**; wer einspeist (wenige Cent), bei **20–25 ct** (**gerechnet**, keine Marktquelle — siehe § 9).

**Platz.** 1–2 m², Gasanschluss, Abgasführung, Kondensatablauf `[Q21]`.

**Förderung 2026.** Über KfW 458 förderfähig — **aber nur bei Betrieb mit Biomethan oder grünem/blauem Wasserstoff**; **Erdgas-Brennstoffzellen sind nicht förderfähig** `[Q21]`. Das ist die harte Bedingung, an der die meisten Projekte scheitern.

**Rechtliche Hürden.** Gilt als Gasheizung → **Biotreppe** § 43 gilt `[Q02]`; Schornsteinfeger nach 1. BImSchV § 15 Abs. 3 `[Q08]`.

**Wartung.** **200–400 €/a** (PEM) bzw. **300–500 €/a** (SOFC); Lebensdauer **~80.000 Betriebsstunden = 10–15 Jahre** `[Q21]`.

**Wann es die falsche Wahl ist.**
- Fast immer im normalen EFH: „Eine Neuinstallation ist 2026 wirtschaftlich selten die beste Wahl" `[Q21]`.
- Wenn kein Biomethan-/Wasserstoffvertrag vorliegt: Dann gibt es keine Förderung und die Biotreppe läuft trotzdem `[Q21][Q02]`.
- Wenn der Strom nicht selbst verbraucht wird: Die Einspeisung trägt die Investition nicht `[Q21]`.

---

## 9. Vergleichstabelle (alle Systeme)

Preisbasis: Gas 12,45 ct/kWh, Öl 14,1 ct/kWh, Pellets 436,09 €/t, Buche 144,70 €/Rm, Fernwärme 16,5 ct/kWh, WP-Strom 27,44 ct/kWh, Haushaltsstrom 37,0 ct/kWh (alle 2026, Quellen `[Q15][Q16][Q17][Q30]`). Wirkungsgrade: Gas/Öl 90 %, Pellet 90 %, Scheitholz 85 %, Split JAZ 3,0, Infrarot 1,0. **€/kWh Wärme sind gerechnet**, nicht zitiert.

| System | Investition | €/kWh Wärme | CO₂ g/kWh Wärme | Platz | Förderung 2026 | Wartung/a | Hauptrisiko |
|---|---|---|---|---|---|---|---|
| **Pellet** | 15.000–25.000 € `[Q18]` | **9,9–10,5** | ~0 fossil (biogen, UBA kritisch `[Q33]`) | 3–10 m² Lager `[Q26]` | 30 + 16 + 10–40 % `[Q10]` | 150–300 € `[Q18]` | Feinstaub, Pelletpreis, Lager |
| **Scheitholz/Kamin** | 15.000–25.000 € (Kessel 5–8k) `[Q27]` | **11,1–11,8** | ~0 fossil (biogen) | 12–18 m³ Holz + 825 l Puffer | 30 + 16 + 10–40 % (nur Kessel) `[Q10]` | Schornsteinfeger + Eigenarbeit | Arbeit, Feinstaub, Holzlogistik |
| **Gas-Brennwert** | 9.000–15.500 € `[Q23]` | **13,8** | **223–244** | 1–2 m² | **0 %** `[Q23]` | 150–250 € | Biotreppe, CO₂-Preis, Netz |
| **Gas+WP-Hybrid** | 36.000–65.000 € `[Q22]` | **10,6** | ~150 (gerechnet) | 2 Geräte + Puffer | nur WP-Teil `[Q22]` | 400 € (doppelt) `[Q22]` | Investitionshöhe, Komplexität |
| **Fernwärme** | 5.000–15.000 € `[Q29]` | **15,7–17,0** + Grundpreis | netzabhängig, **teils > 300** `[Q29]` | 1–2 m² | 30 + Boni `[Q10]` | ~0 | Monopol, Anschlusszwang `[Q05]` |
| **Solarthermie** | 6.000–17.000 € `[Q24]` | ~6–14 (gerechnet) | ~0 | 3–20 m² Dach | 30 + Boni `[Q10]` | 100–200 € `[Q19]` | kein Alleinbetrieb, PV-Konkurrenz |
| **Split/Luft-Luft** | 1.500–7.000 € `[Q20]` | **9,1–12,3** | **115** | Außengerät ~0,5 m² | nur heizungsprimär `[Q20]` | 100–200 € | kein Warmwasser, Kälte, Lärm |
| **Infrarot** | 1.500–2.500 € (50 m²) `[Q40]` | **37,0** | **344** `[Q32]` | 0 | **0 %** | 0 | Strompreis, § 46 `[Q04]` |
| **Brennstoffzelle** | 25.000–35.000 € `[Q21]` | 10–25 (gerechnet) | 120–244 (gerechnet) | 1–2 m² | nur Biomethan/H₂ `[Q21]` | 200–500 € `[Q21]` | Brennstoffbedingung, Lebensdauer |

**Lesart:** Die Tabelle sortiert nach *laufenden* Kosten, nicht nach Wirtschaftlichkeit. Pellet und Scheitholz sind pro kWh am billigsten, kosten aber 15.000–25.000 € und Arbeit. Fernwärme ist bei der Investition unschlagbar, beim Arbeitspreis die zweitteuerste Option. Infrarot ist nur dann sinnvoll, wenn die Alternative „gar keine Heizung" wäre.

---

## 10. Rechenbeispiel: 15.000 kWh Wärmebedarf pro Jahr, 15 Jahre

Annahmen: Einfamilienhaus, 15.000 kWh/a, Austausch einer 20 Jahre alten Gasheizung, selbstgenutzt, zu versteuerndes Haushaltseinkommen 45.000 € (Einkommensbonus **10 %**), Förderquote 30 + 16 + 10 = **56 %** auf den Deckel von 28.000 €. Ohne Preissteigerung, ohne Kapitalkosten, ohne CO₂-Steigerung. **Alle Zahlen gerechnet** aus den Quellen oben.

| System | Investition | Förderung | Netto-Invest | Energie/a | Wartung/a | Gesamt/a | 15 Jahre |
|---|---|---|---|---|---|---|---|
| Pellet | 20.000 € | 11.200 € | **8.800 €** | 1.483 € | 475 € | 1.958 € | **38.200 €** |
| Scheitholz | 18.000 € | 10.080 € | **7.920 €** | 1.659 € | 350 € | 2.009 € | **38.100 €** |
| Split (nur Heizung) | 6.000 € | 0 € | **6.000 €** | 1.850 € | 150 € | 2.000 € | **36.000 €** |
| Gas-Brennwert | 12.000 € | 0 € | **12.000 €** | 2.075 € | 250 € | 2.325 € | **46.900 €** |
| Fernwärme | 10.000 € | 5.600 € | **4.400 €** | 2.975 € | 100 € | 3.075 € | **50.500 €** |
| Hybrid | 45.000 € | 11.200 € | **33.800 €** | 1.583 € | 400 € | 1.983 € | **63.500 €** |
| Infrarot | 3.000 € | 0 € | **3.000 €** | 5.550 € | 0 € | 5.550 € | **86.250 €** |

**Was die Tabelle nicht zeigt:**
- **Split** deckt kein Warmwasser — die 36.000 € sind eine Heizung ohne Dusche. Fair wäre ein Zuschlag für eine Brauchwasser-Wärmepumpe (ca. 3.000–5.000 €, Schätzung).
- **Scheitholz** enthält keine Arbeitszeit. 11,5 Rm Holz machen, spalten, stapeln sind realistisch 2–4 Wochen — bei 25 €/h Gegenwert sind das 2.000–4.000 €/a, die die Bilanz kippen.
- **Gas** hat die niedrigste Investition, aber die höchste Preissensitivität: Die Biotreppe ab 2029 und der EU-ETS2 ab 2028 verteuern den Brennstoff `[Q02][Q23]`.
- **Pellet** ist nur dann vorn, wenn der Pelletpreis hält. 2026 lag er bei 436 €/t; 2022 waren es kurzzeitig über 700 €/t (Markterinnerung, keine geprüfte Quelle in diesem Lauf).
- **Infrarot** ist nach 15 Jahren doppelt so teuer wie Pellet — bei einem Drittel der Investition. Das ist die ganze Geschichte dieses Systems.
- **Fernwärme** enthält im Rechenbeispiel **500 €/a Grundpreis** zusätzlich zu 16,5 ct/kWh; reine Arbeitskosten wären 2.475 €/a. Ohne Grundpreis sähe die 15-Jahres-Summe 7.500 € besser aus — er ist aber Realität `[Q29][Q28]`.

---

## 11. Entscheidungsbaum

```
Liegt das Haus in einem Fernwärmenetz (oder kommt es in den Wärmeplan)?
├─ ja, Arbeitspreis ≤ 15 ct/kWh → FERN WÄRME prüfen (Anschlusszwang § 109 beachten)
└─ nein / Preis > 17 ct → weiter

Gibt es einen Gasanschluss und ist das Budget < 15.000 €?
├─ ja → GAS-BRENNWERT (0 % Förderung, Biotreppe ab 2029 einkalkulieren)
└─ nein → weiter

Ist Platz für 6–9 m³ Lager und ein Silo-Fahrzeug kommt ans Haus?
├─ ja → PELLET (beste laufende Kosten, 56–80 % Förderung)
└─ nein → weiter

Hast du eigene Holzquelle und Zeit für 11–12 Rm/Jahr?
├─ ja → SCHEITHOLZ (nur mit Puffer 55 l/kW)
└─ nein → weiter

Ist das Dach südlich und ≥ 20 m² frei (und keine PV geplant)?
├─ ja → SOLARTHERMIE als Ergänzung zum gewählten System
└─ nein → weiter

Brauchst du nur einzelne Räume / Übergangszeit / Kühlung?
├─ ja → SPLIT (kein Warmwasser!)
└─ nein → WÄRMEPUMPE (siehe Parallel-Playbook) — nicht Infrarot

Sonderfälle:
- Dauerhaft hoher Strom- UND Wärmebedarf + Biomethanvertrag → BRENNSTOFFZELLE
- Bad/Gästezimmer, kein Anspruch auf Komfort → INFRAROT (max. Einzelraum)
- MFH > 2 Wohnungen, Infrarot geplant → § 46 prüfen: nur bei 30 % besserem Wärmeschutz
```

**Die drei Fragen, die jede Entscheidung vorweg entscheiden:**
1. **Kommt ein Silowagen ans Haus?** (Pellet steht und fällt damit.)
2. **Ist der Heizraum groß genug für Puffer + Kessel + Lager?** (Scheitholz/Pellet/Hybrid)
3. **Bleibst du 15 Jahre?** (Amortisation; bei Verkauf in < 8 Jahren ist die Investition oft verloren.)

---

## 12. Typische Fehler

1. **„65 % sind Pflicht"** — seit 29.07.2026 falsch `[Q11][Q12]`. Richtig ist: Förderung verlangt EE-Verbesserung, Baurecht nicht.
2. **Pellet ohne Lieferweg planen.** Ein 3-t-Silo wird nicht durch den Kellerflur getragen; der Schlauch braucht 20–30 m und eine gerade Zufahrt (Erfahrungswert).
3. **Pufferspeicher weglassen.** § 5 Abs. 4 1. BImSchV fordert **55 l/kW** bei handbeschickten Anlagen — bei 15 kW 825 l `[Q07]`. Wer kleiner baut, riskiert Taktbetrieb und Ärger mit dem Schornsteinfeger.
4. **Kaminofen mit Zentralheizung verwechseln.** Ein Ofen heizt einen Raum; § 45 GModG verlangt für die Heizungsanlage einen Kessel oder Ofen **mit Wasser** `[Q03]`.
5. **Förderantrag nach der Bestellung.** Die KfW verlangt den Antrag **vor Beginn der Arbeiten vor Ort**; schon der **Vertragsabschluss** gilt als „schädlicher Vorhabenbeginn" `[Q10]`. Wer zuerst bestellt, verliert den Zuschuss.
6. **Deckel ignoriert.** 28.000 € förderfähige Kosten, nicht 28.000 € Zuschuss. Bei 56 % sind das max. **15.680 €** `[Q10]`.
7. **Hybrid als „Förder-Trick".** Gefördert wird nur der WP-Teil; der Gaskessel bleibt zu 100 % privat `[Q22]`.
8. **Fernwärme ohne Preisblattvergleich.** Arbeitspreis 8–22 ct und Grundpreis 200–2.250 €/a sind eine Spanne von Faktor 3 `[Q29][Q28]`.
9. **Split als Vollheizung.** Keine Warmwasserbereitung, JAZ 2,5–3,5, Luftzug `[Q20]`.
10. **Infrarot mit PV schönrechnen.** Im Dezember liefert PV fast nichts; die 37 ct/kWh bleiben `[Q15][Q37]`.
11. **Brennstoffzelle mit Erdgas.** Keine Förderung, Biomethan kostet 2–3× so viel wie Erdgas `[Q21]`.
12. **Schornsteinfeger-Termine vergessen.** Feste Brennstoffe: alle 2 Jahre Messung `[Q08]`.

---

## 13. Quellen (alle am 09.11.2026 abgerufen, HTTP 200)

**Gesetz / Verordnung**
- `[Q01]` GModG § 42 — Grundsatz, Optionskatalog. https://www.gesetze-im-internet.de/geg/__42.html (Volltext geprüft; die URL führt weiterhin auf „geg", das Gesetz heißt GModG)
- `[Q01a]` GModG § 42a — Grüngas-/Grünheizölquote, Gesetz bis 01.12.2026. https://www.gesetze-im-internet.de/geg/__42a.html
- `[Q02]` GModG § 43 — Biotreppe 10/15/30/60 %, Abs. 3 Solar-Fläche, Abs. 5 Hybrid-Leistung. https://www.gesetze-im-internet.de/geg/__43.html
- `[Q03]` GModG § 45 — Biomasse: nur Kessel/Ofen mit Wasser. https://www.gesetze-im-internet.de/geg/__45.html
- `[Q04]` GModG § 46 — Stromdirektheizung: 30-%-Wärmeschutz, Ausnahme ≤ 2 WE. https://www.gesetze-im-internet.de/geg/__46.html
- `[Q05]` GModG § 109 — Anschluss- und Benutzungszwang Fernwärme. https://www.gesetze-im-internet.de/geg/__109.html
- `[Q06]` GModG § 71 — **(weggefallen)**: die frühere 65-%-Regel. https://www.gesetze-im-internet.de/geg/__71.html
- `[Q06a]` GModG § 44 — Solarthermie: Solar-Keymark. https://www.gesetze-im-internet.de/geg/__44.html
- `[Q07]` 1. BImSchV § 5 — Grenzwerte 20 mg/m³ Staub / 0,4 g/m³ CO, Puffer 55/20 l/kW. https://www.gesetze-im-internet.de/bimschv_1_2010/__5.html
- `[Q08]` 1. BImSchV § 15 — wiederkehrende Überwachung (2 Jahre fest, 2–3 Jahre Gas/Öl). https://www.gesetze-im-internet.de/bimschv_1_2010/__15.html
- `[Q09]` 1. BImSchV § 25 — Übergangsregelung Bestandskessel. https://www.gesetze-im-internet.de/bimschv_1_2010/__25.html
- `[Q43]` § 24 Abs. 4 AVBFernwärmeV — Preisänderungsklausel: Kostenentwicklung **und** Wärmemarkt, Faktoren vollständig ausweisen, Brennstoffanteil gesondert, keine einseitige Änderung per Bekanntgabe. https://www.gesetze-im-internet.de/avbfernw_rmev/__24.html

**Behörde / Förderbank**
- `[Q10]` KfW, Zuschuss 458 „Heizungsförderung für Privatpersonen – Wohngebäude", Stand 07/2026. https://www.kfw.de/inlandsfoerderung/Privatpersonen/Bestehende-Immobilie/F%C3%B6rderprodukte/Heizungsf%C3%B6rderung-f%C3%BCr-Privatpersonen-Wohngeb%C3%A4ude-(458)/ — 30–80 %, Deckel 28.000/15.000/8.000 €, förderfähige Techniken.
- `[Q11]` BMWE, Dossier „GModG ersetzt GEG", Beschluss 10.07.2026. https://www.energiewechsel.de/KAENEF/Redaktion/DE/Dossier/gmodg.html — 65-%-Vorgabe und Betriebsverbote entfallen, Biotreppe, Förderung bis mind. 2029.
- `[Q32]` Umweltbundesamt, „CO₂-Emissionen pro Kilowattstunde Strom 2025", 23.03.2026. https://umweltbundesamt.de/themen/co2-emissionen-pro-kilowattstunde-strom-2025-nur — **344 g CO₂/kWh** (2024: 353, 2023: 379).
- `[Q33]` Umweltbundesamt, FAQ Holzheizungen (Stand 21.04.2023). https://www.umweltbundesamt.de/en/node/101321 — Kaminofen 0,31 g/kWh Staub, 7,4 g/kWh CO; Scheitholzkessel 0,117 g/kWh; Holzverbrennung nicht automatisch klimaneutral.

**Fachpresse / Verbände**
- `[Q12]` HeizungsJournal, „GModG in Kraft getreten", 06.08.2026. https://www.heizungsjournal.de/gmodg-in-kraft-getreten_114420 — 65 % entfällt, Betriebsverbote entfallen, Biotreppe.
- `[Q13]` ELCO, „BEG 2026 – die neuen Förderungen", 2026. https://elco.de/blog/waermerecht/beg-foerderung.html — 30 % Grundförderung, 16 % Klimabonus, −4 pp halbjährlich, Deckel −750 € halbjährlich, Effizienz-/Emissionsbonus gestrichen, 15+15 % Wertschöpfungsbonus ab 2027.
- `[Q30]` ZfK, „Fernwärmepreise 2026: Klarer Trend erkennbar", 06.03.2026. https://zfk.de/energie/waermewende/fernwaermepreise-2026-klarer-trend-erkennbar — AGFW 15,7 ct/kWh (01.01.2026), VZBV-Median ~17 ct (EFH).
- `[Q41]` BauNetz Wissen, „Austragungssysteme für Pelletheizungen" — Schnecke (kurze Wege, wenig Abrieb), pneumatisch bis **30 m** und **Steigungen bis 6 m**, Feinabrieb als Störungsursache. https://www.baunetzwissen.de/heizung/fachwissen/brennstofflagerung/austragungssysteme-fuer-pelletheizungen-5385903
- `[Q44]` BauNetz Wissen, „Kollektorfläche und solarer Deckungsgrad" — Bänder < 40 % / 40–60 % / > 70 %, 30–45 % bei MFH, 60 % deckt Warmwasser im Sommer, Passivhaus ≈ 50 % bei Heizungsunterstützung. https://www.baunetzwissen.de/solar/fachwissen/solarwaerme/kollektorflaeche-und-solarer-deckungsgrad-165858
- `[Q31]` BDEW, „Fernwärmepreise bleiben stabil, Marktabdeckung wächst", 22.07.2026. https://www.bdew.de/presse/die-marktabdeckung-waechst-weiter-und-die-preise-bleiben-stabil — 710 Netze, > 50 % des Absatzes.

**Verbraucherportale / Verbraucherzentrale**
- `[Q15]` cleanthinking, „Heizkostenvergleich 2026/27", 04.10.2026. https://cleanthinking.de/heizkosten-vergleich — Gas 12,45 ct (BDEW 08/2026), Öl 14,1 ct (Destatis 07/2026), WP-Strom 27,44 ct, Fernwärme 15,6 ct, Haushaltsstrom 37,0 ct.
- `[Q16]` HeizPellets24, Pelletpreise, 09.11.2026. https://www.heizpellets24.de/pelletpreise — **436,09 €/t** (6 t, inkl. MwSt./Lieferung).
- `[Q17]` TFZ Bayern, Scheitholzpreise Juli 2026. https://tfz.bayern.de/biogenefestbrennstoffe/scheitholz/380613?fontsize=1 — Buche 144,70 €/Rm = 9,40 ct/kWh, Fichte 109,80 €/Rm = 9,64 ct/kWh.
- `[Q18]` ADAC, „Pelletheizung: Kosten, Förderung, Vor- und Nachteile", 22.07.2026. https://www.adac.de/rund-ums-haus/energie/versorgung/pelletheizung — 15.000–25.000 €, 7–9 ct/kWh (2025), 4–6 t/a, 150–300 € Wartung, 95 % Wirkungsgrad.
- `[Q19]` ADAC, „Solarthermie: Kosten und Förderung 2026", 22.07.2026. https://www.adac.de/rund-ums-haus/energie/versorgung/solarthermie-kosten-foerderung — 3.000–6.000 / 7.000–17.000 €, 250–800 €/m², 100–200 €/a, Keymark, 525 kWh/m²·a.
- `[Q20]` ADAC, „Heizen mit Klimaanlage". https://www.adac.de/rund-ums-haus/energie/versorgung/heizen-mit-klimaanlage — 1.500–3.500 € mono, 3.500–7.000 € multi, SCOP 4, JAZ, keine WW, Förderung nur heizungsprimär.
- `[Q42]` Verbraucherzentrale, „Fernwärme: Kosten sparen und gleichzeitig das Klima schonen" (Stand 09.07.2025) — lokales Monopol ohne Wechsel, Verträge bis 10 Jahre, Erzeugungsmix 2/3 fossil / 20 % EE / 9 % Abwärme / 5 % Abfall. https://www.verbraucherzentrale.de/wissen/energie/heizen-und-warmwasser/fernwaerme-kosten-sparen-und-gleichzeitig-das-klima-schonen-34038
- `[Q24]` Verbraucherzentrale, „Solarthermie: So nutzen Sie Solarenergie". https://verbraucherzentrale.de/wissen/energie/erneuerbare-energien/solarthermie-so-nutzen-sie-solarenergie-fuer-heizung-und-warmwasser-5568 — 3–6 m²/250–350 l, 9–20 m²/500–1.500 l, 300–400 kWh/m²·a, 6.000–17.000 € (2025), PV-Konkurrenz.
- `[Q25]` Verbraucherzentrale Energieberatung, „Elektrische Direktheizung". https://verbraucherzentrale-energieberatung.de/heizen/neue-heiztechnik/elektrische-direktheizung — „kostenintensive Notlösung", 1 kWh Strom = 1 kWh Wärme.
- `[Q26]` co2online, „Pelletheizung: Kosten, Förderung & Arten" (29.01.2025). https://www.co2online.de/modernisieren-und-bauen/heizung/pelletheizung — Lagerraum 3–10 m², Puffer, Asche, Nachteile.
- `[Q34]` heizsparer, „Heizwert von Pellets", 10.09.2026. https://heizsparer.de/energie/holzpellets/heizwert-von-pellets — 4,9 kWh/kg, 1,5 m³/t, 1 kg Scheitholz ≈ 4 kWh.
- `[Q40]` Infrarot-Guide, „Infrarotheizung Kosten 2026", 21.09.2026. https://www.infrarot-guide.de/infrarotheizung-kosten-stromverbrauch-betriebskosten/ — Paneelpreise, 1.500–2.500 € für 50 m².

**Heizungsbau / Hersteller**
- `[Q21]` thermondo, „Brennstoffzellenheizung: Funktion, Kosten und Förderung 2026", 27.09.2026. https://www.thermondo.de/info/rat/erneuerbare-energie/brennstoffzellenheizung/ — 25.000–35.000 €, 90 %, nur Biomethan/H₂ förderfähig, 200–500 €/a, 80.000 h.
- `[Q22]` thermondo, „Hybridheizung: Gas und Wärmepumpe", 27.09.2026. https://www.thermondo.de/info/rat/waermepumpe/hybridheizung-gas-und-waermepumpe/ — 36.000–65.000 €, Förderung nur WP-Teil, doppelte Wartung, GModG-Konformität.
- `[Q23]` thermondo, „Gasheizung Kosten 2026", 27.09.2026. https://www.thermondo.de/info/rat/gas/gasheizung-kosten/ — 9.000–15.500 €, 0 % Förderung, 0,22 kg CO₂/kWh Gas, 0,28 Öl.
- `[Q27]` heizung.de, „Die Preise der Holzheizung im Überblick". https://www.heizung.de/holzheizung/wissen/die-preise-der-holzheizung-im-ueberblick.html — Holzvergaser 5.000–8.000 €, Kamin ab 500 €, Kachelofen > 5.000 €, wasserführend 2.500–3.000 €.
- `[Q28]` heizung.de, „Typische Fernwärme-Kosten", 14.08.2026. https://heizung.de/finanzielles/wissen/typische-fernwaerme-kosten-im-ueberblick.html — Hausstation 7.500–20.000 €, Grundpreis 50–150 €/kW·a, Arbeitspreis 12–20 ct, § 109 GModG.
- `[Q29]` 42watt, „Fernwärme Kosten 2026", 01.09.2026. https://42watt.de/magazin/fernwaerme-kosten — 5.000–15.000 € Anschluss, 8–22 ct/kWh, Grundpreis 200–800 €/a, § 32 AVBFernwärmeV, CO₂ teils > 300 g/kWh.
- `[Q35]` ÖkoFEN, Pellematic Condens (10–32 kW). https://www.oekofen.com/de-de/pellematic-condens/ — 1 m² Stellfläche, Brennwert, ZeroFlame.

**Fachforum / YouTube**
- `[Q36]` HaustechnikDialog (News), „Letzte Chance für Pellet-Pioniere: Volle Heizungsförderung nur noch 2026", 27.08.2026. https://www.haustechnikdialog.de/News/31803/Letzte-Chance-fuer-Pellet-Pioniere-Volle-Heizungsfoerderung-nur-noch-2026-moeglich — Deckel 30.000 → 28.000, dann −750 €/Halbjahr; drei Jahre Umsetzungsfrist.
- `[Q37]` HaustechnikDialog (Forum), „Erfahrungen mit Infrarotheizung?", 04.02.–18.06.2026. https://www.haustechnikdialog.de/Forum/t/291482/Erfahrungen-mit-Infrarotheizung- — „1 kWh elektrische Energie ergibt 1 kWh Wärmeenergie"; IR nur Bad/selten genutzte Räume; Passivhaus-Voraussetzung.
- `[Q38]` Prof. Dr. Volker Quaschning, „Wärmepumpe, Gas oder Pellets? Faktencheck zu Kosten, Klima & Komfort", 09.01.2026. https://www.youtube.com/watch?v=DHVr4lhDzDg — Kapitelmarken aus der Beschreibung: 06:08 Pelletheizung/Lager, 11:25 Kostenvergleich, 19:50 „Ist mit Holz heizen klimaneutral?" (Transkript nicht abrufbar, siehe § 14).
- `[Q39]` Haus-Garten-Solar, „Achtung vor der Pelletheizung! Meine Erfahrung nach 1 Jahr im Altbau", 24.02.2026. https://www.youtube.com/watch?v=2tEtpYF8REc — Titel/Kanal/Datum per oEmbed geprüft; nicht als Zahlenbeleg verwendet.
- `[Q14]` t-online, „Neuer Grenzwert bei Holzheizungen: Diese Änderungen gelten ab 2027", 27.07.2026. https://www.t-online.de/heim-garten/aktuelles/id_101357152/neuer-grenzwert-bei-holzheizungen-diese-aenderungen-gelten-ab-2027.html — 2,5 mg/m³ ab 10/2027, Fördergrenzen 10/15 mg/m³.


---

## 14. Unbelegt, offen, widersprüchlich

**Widersprüche (stehen gelassen, nicht geglättet):**
1. **Pellet-Investition:** 15.000–25.000 € `[Q18]` vs. 25.000–30.000 € `[Q16]`. Erklärung: `[Q18]` rechnet „inkl. Montage und Lager", `[Q16]` offenbar mit hochwertigerem Kessel — die Wahrheit liegt dazwischen, regionale Spreizung ±20 %.
2. **Pellet-Betriebskosten:** 7–9 ct/kWh `[Q18]` (Stand 2025) vs. 9,9–10,5 ct (gerechnet aus 436 €/t, 11/2026). Kein Fehler, sondern Preisentwicklung — `[Q18]` ist mit „Stand 2025" datiert.
3. **Solarthermie-Kosten:** 6.000–10.000 / 9.000–17.000 € `[Q24]` (2025) vs. 3.000–6.000 / 7.000–10.000 € `[Q19]` (2026). `[Q19]` ist neuer und günstiger; vermutlich unterschiedlicher Lieferumfang (Speicher, Montage). Für die Kalkulation die höhere Zahl nehmen.
4. **Fernwärme-Grundpreis:** 200–800 €/a `[Q29]` vs. 50–150 €/kW·a, bei 15 kW also 750–2.250 €/a `[Q28]`. Beides kann stimmen (kleine vs. große Anschlussleistung), aber die Planung muss den eigenen Wert beim Versorger erfragen.
5. **Förder-Obergrenze:** KfW nennt „bis zu 80 %" `[Q10]`, die Fachquelle „Obergrenze 70 % mit Ausnahme Kinderzuschlag" `[Q13]`. Auflösung: 70 % ist der Regelfall, 80 % nur mit Kinderzuschlag/Sozialstaffel.
6. **65 % EE bei der Förderung:** ADAC schreibt sie 2026 noch für Split-Anlagen und Pellet `[Q18][Q20]`, obwohl das GModG sie baurechtlich abgeschafft hat `[Q11][Q12]`. Vermutlich Förderrichtlinien-Rest — **ungeklärt**, vor Antragstellung bei der KfW klären.
7. **CO₂-Faktor Gas:** 0,22 kg/kWh `[Q23]` vs. 0,201 kg/kWh (UBA-Standardwert, hier nicht separat abgerufen). Die Tabelle rechnet mit 0,201–0,22 als Band.
8. **ETS2-Start:** 2028 `[Q23]` — frühere Planungen nannten 2027. Für die Wirtschaftlichkeit ändert das nur das Tempo, nicht die Richtung.

**Unbelegt / Schätzung (so gekennzeichnet):**
- **Komplettpreis Scheitholz 15.000–25.000 €** — Kesselpreis ist belegt `[Q27]`, der Rest (Puffer, Hydraulik, Schornstein, Montage) ist Schätzung.
- **Wirkungsgrad Scheitholzkessel 85 %** — Erfahrungswert, keine Quelle in diesem Lauf.
- **Wärmepreis Brennstoffzelle 10–25 ct/kWh** — eigene Rechnung; die Allokation zwischen Strom und Wärme ist eine Annahme.
- **Solarthermie-Vollkosten 6–14 ct/kWh** — eigene Rechnung mit 300 kWh/m²·a `[Q24]`, 20 Jahren, ohne Kapitalkosten.
- **Alle 15-Jahres-Summen** — eigene Rechnung, keine Preissteigerung, keine Diskontierung, keine CO₂-Steigerung. Reale Zahlen weichen ab.
- **Lagerraum-Brandschutz** (Abstand zu brennbaren Bauteilen, Feuerwiderstand) — nicht geprüft; steht in Landesbauordnung/Feuerungsverordnung, muss der Bezirksschornsteinfeger abnehmen.
- **Abstand/Genehmigung Außengerät Split** — TA Lärm und Landesrecht nicht im Volltext geprüft.
- **YouTube-Transkripte:** Für `[Q38][Q39]` war kein Transkript abrufbar (YouTube liefert die timedtext-URL nur mit gültigem Token). Zitiert sind **Titel, Kanal, Datum** (oEmbed) und bei `[Q38]` die **Kapitelmarken aus der Videobeschreibung** — keine Transkriptzitate, keine erfundenen Zeitmarken.
- **Pelletpreis-Historie 2022 (700 €/t)** — Markterinnerung, in diesem Lauf nicht belegt; deshalb im Text als solche gekennzeichnet.

**Nicht geprüft, weil außerhalb des Auftrags:** Ölheizung→Wärmepumpe (Parallel-Playbook), Wasserstofffähigkeit (§ 71k GEG), KWK-Zuschlag, steuerliche Behandlung (§ 35c EStG), Mietrecht/Umlage.