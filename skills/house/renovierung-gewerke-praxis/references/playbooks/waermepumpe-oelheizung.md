# Ölheizung raus, Wärmepumpe rein — Playbook für Eigenheimbesitzer

**Stand:** 09.11.2026 · **Zielgruppe:** Eigentümer eines Bestandshauses (typisch 1960er), Ölheizung am Ende, kein SHK-Profi
**Grenze dieses Playbooks:** Du entscheidest, planst, vergleichst Angebote, machst die Eigenleistung außerhalb der Fachbetriebspflicht. Kältemittelkreis, Elektroinstallation, Gas und die Stilllegung der Öltankanlage bleiben Fachbetrieb — mit Rechtsgrundlage unten. Alle Preise sind **Bänder**, keine Punktpreise; jede Zahl mit `[Qnn]` ist belegt, alles andere ist als Schätzung markiert.

> **Die Lage hat sich 2026 zweimal geändert.** Seit **29.07.2026** gilt das **GModG** (Gebäudemodernisierungsgesetz) statt GEG: die 65-%-EE-Pflicht, die Beratungspflicht und die 30-Jahre-Austauschpflicht sind **entfallen** `[Q01][Q02][Q08]`. Seit **21.07.2026** gilt die reformierte Förderung: weniger förderfähige Kosten, weniger Boni, aber ein neuer Familienzuschlag `[Q09][Q11]`. Wer mit Stand 2024 rechnet, rechnet falsch.

---

> **Preisstand 09/2026.** Alle Preise sind Orientierungswerte inkl. MwSt. aus den genannten Quellen —
> regional verschieden, keine Angebote. Wer später damit rechnet, prüft sie neu.

## Kurzantwort

1. **Rechtlich darf deine alte Ölheizung weiterlaufen.** Es gibt seit dem 29.07.2026 keine Austauschpflicht nach 30 Jahren und kein Betriebsverbot mehr `[Q02][Q08][Q12]`. Der Zwang, der bleibt, ist ein wirtschaftlicher: Ölpreis, CO₂-Preis und der Zustand des Kessels.
2. **Wenn du tauschst, ist die Wärmepumpe förderfähig, eine neue Ölheizung nicht** `[Q09][Q11]`. Grundförderung 30 %, Klimageschwindigkeitsbonus 16 %, Einkommensbonus 10/30/40 %, Deckel 80 % von 28.000 € = **max. 22.400 €** `[Q09]`.
3. **Reihenfolge, die Geld spart:** Heizlast und Vorlauftemperatur **messen**, dann Heizflächen anpassen, dann Gerät auslegen. Wer zuerst das Gerät kauft, kauft zu groß `[Q34][Q27]`.
4. **Der Klimageschwindigkeitsbonus verfällt im Sechs-Monats-Takt** (−4 Prozentpunkte ab 01.02.2027, ab 01.08.2028 null) `[Q09][Q11]`. Das ist die einzige echte Frist in diesem Vorhaben — und sie ist eine Förder-, keine Rechtsfrist.
5. **Der Öltank ist der unterschätzte Kostenblock:** Stilllegung nur durch Fachbetrieb nach AwSV `[Q15]`, Entsorgung 400–2.500 € je 1.000 l je nach Bauart `[Q20]`.

---

## 0. Entscheidungsbaum

```
Alte Ölheizung: Baujahr? Zustand?
│
├─ Kessel jünger als ~20 J., dicht, Abgaswerte gut, Tank dicht
│   └─ Weiterbetreiben ist erlaubt [Q02]. Aber: jede Reparatur > 1.500 €
│      verschiebt die Rechnung Richtung Tausch.
│
└─ Tausch geplant
    │
    ├─ 1. Vorlauftemperatur bei Norm-Außentemperatur messen (oder aus
    │      Heizkurve ablesen). Zwei Fälle:
    │      ├─ ≤ 55 °C bei −10 °C AT  → Heizkörper bleiben, WP direkt möglich
    │      └─ > 55 °C               → erst Heizflächen (Typ 33 statt 22,
    │                                  größere Baulänge, einzelne Räume FBH)
    │                                  → dann WP [Q18][Q36][Q27]
    │
    ├─ 2. Wärmequelle verfügbar?
    │      ├─ Garten > 300 m², wasserrechtlich zulässig → Sole/Flachkollektor
    │      ├─ Bohrtiefe machbar, Genehmigung → Sole/Sonde (40.000–50.000 €) [Q22]
    │      └─ nichts davon               → Luft-Wasser (24.000–32.000 €) [Q22]
    │
    ├─ 3. Aufstellort: Abstand zum Nachbarn, Schall, Kondensat, Fundament
    │      → TA-Lärm-Werte prüfen (unten § 3.7)
    │
    └─ 4. Vor Baubeginn: Förderantrag stellen (KfW 458), DANN beauftragen
           → Antrag nach Beginn = kein Zuschuss [Q11][Q37]
```

---

## 1. Fristen & Recht: was gilt, was ist ausgelaufen

### 1.1 Der Stichtag 29.07.2026

| Punkt | Bis 28.07.2026 (GEG 2024) | Seit 29.07.2026 (GModG) | Beleg |
|---|---|---|---|
| 65-%-EE-Pflicht bei neuer Heizung | Pflicht, § 71 GEG | **weggefallen** (§ 71 GEG ist „weggefallen“) | `[Q01][Q02][Q08]` |
| Beratungspflicht beim Heizungstausch | Pflicht | **weggefallen** | `[Q08]` |
| Betriebsverbote bestimmter Heizungen (§ 73 GEG) | vorhanden | **weggefallen** | `[Q08]` |
| Austauschpflicht Kessel ab 30 Jahren (§ 72 GEG) | Pflicht | **ersatzlos gestrichen** | `[Q02][Q12]` |
| Verbot fossiler Brennstoffe ab 2045 | § 72 GEG | **entfallen** | `[Q12]` |
| Kommunale Wärmeplanung | GEG 2024 verwies auf das Wärmeplanungsgesetz | **nicht mehr im Gesetz** (das Wort „Wärmeplan“ kommt im Volltext nicht vor) | `[Q01]` |
| Härtefallregelung | in GEG 2024 vorhanden (§§ 71 ff.) | **nicht mehr im Gesetz** („Härtefall“ kommt im Volltext nicht vor) | `[Q01]` |
| Erfüllungserklärung für Heizungstausch | nötig | nur noch Neubau und Änderung nach § 36 | `[Q01]` (§ 92) |

Prüfstand: Der Volltext auf gesetze-im-internet.de führt das Gesetz jetzt als **„Gebäudemodernisierungsgesetz“**, Fassung „zuletzt geändert durch Art. 4 G v. 23.7.2026 (BGBl. 2026 I Nr. 226)“; §§ 71, 72, 73 sind mit „(weggefallen)“ ausgewiesen `[Q01]`. Das BBSR-Infoportal bestätigt: Bundestag 10.07.2026, Verkündung 28.07.2026, Gültigkeit der Lesefassung „29.07.2026 bis 31.12.2026“ `[Q08]`.

**Konsequenz:** Es gibt 2026 **keine gesetzliche Frist**, die dich zum Tausch zwingt. Wer dir „2026 muss die Ölheizung raus“ erzählt, meint die alte Rechtslage oder verkauft etwas.

### 1.2 Was jetzt beim Einbau gilt: § 42 und § 43 GModG

**§ 42 Abs. 2 — zehn zulässige Optionen**, technologieoffen: Gas/Öl/Flüssiggas, elektrische Wärmepumpe, Solarthermie, Biomasse/Wasserstoff, Wärmepumpen-Hybrid, Solarthermie-Hybrid, KWK, Stromdirektheizung, Fernwärme-Hausübergabestation, „andere innovative Heizungslösung“ `[Q01]`.

**§ 43 — die „Bio-Treppe“** gilt für Gas-, Öl- und Flüssiggasheizungen, die **nach dem 29.07.2026** neu eingebaut werden `[Q01][Q03]`:

| ab 01.01. | Mindestanteil biogen/klimaneutral (Biomethan, Bioöl, biogenes Flüssiggas, H₂) |
|---|---|
| 2029 | 10 % |
| 2030 | 15 % |
| 2035 | 30 % |
| 2040 | 60 % |

- Erfüllbar auch über Solarthermie (bei ≤ 2 Wohnungen: **0,04 m² Aperturfläche je m² Nutzfläche**) oder Lüftung mit Wärmerückgewinnung (≥ 73 % WRG, Leistungszahl ≥ 10, ganze Fläche) `[Q01]` (§ 43 Abs. 3, 4).
- Wärmepumpen-Hybrid: Pflicht gilt als erfüllt, wenn die WP mindestens **30 %** (Teillastpunkt A, DIN EN 14825) bzw. **40 %** (bivalent alternativ) der Spitzenlastleistung bringt `[Q01]` (§ 43 Abs. 5).
- Bei **irreparablem Ausfall** im Jahr 2028: 12 Monate Aufschub; ab 2029 läuft eine bestehende Pflicht 12 Monate fort `[Q01]` (§ 43 Abs. 7).

**§ 42a — Grüngas-/Grünheizölquote:** Ein Gesetz dazu soll die Bundesregierung **bis 01.12.2026** vorlegen; die Inverkehrbringer müssen ihre Brennstoffe **ab 2045 vollständig** auf klimaneutral umstellen `[Q04][Q01][Q08]`. Das ist eine Pflicht der Mineralölwirtschaft, nicht deine — sie ist aber der Grund, warum Öl langfristig teurer wird.

**§ 46 — Stromdirektheizung** (Infrarot, Heizstab) ist in Wohngebäuden nur zulässig, wenn der bauliche Wärmeschutz die Anforderungen der §§ 16, 19 um **mindestens 30 % unterschreitet**; Ausnahme: Gebäude mit ≤ 2 Wohnungen, von denen der Eigentümer eine selbst bewohnt `[Q05]`.

### 1.3 Pflichten, die bleiben

| Pflicht | Inhalt | Gilt für | Beleg |
|---|---|---|---|
| Heizungsprüfung + Optimierung | Parameter, Pumpe, Rohrdämmung, Vorlauftemperatur prüfen | Anlagen mit Wasser als Wärmeträger in Gebäuden **mit ≥ 6 Wohnungen**; Alt-Anlagen (Einbau vor 01.10.2009) **bis 30.09.2027** | `[Q06]` |
| Hydraulischer Abgleich | raumweise Heizlast (DIN EN 12831), Heizflächenprüfung, Vorlaufregelung; Verfahren B | bei Inbetriebnahme in Gebäuden **mit ≥ 6 Wohnungen** | `[Q07]` |
| Nachrüstung oberste Geschossdecke | U ≤ 0,24 W/(m²K) | Wohngebäude | `[Q01]` (§ 35) |
| Kehrpflicht | entfällt bei dauerhaft stillgelegter Anlage, **wenn** Anschlussöffnungen dichte Verschlüsse aus nicht brennbaren Stoffen haben und Mitteilung erfolgt | alle Feuerstätten | `[Q16]` |

**Für das Einfamilienhaus heißt das:** von den drei „berühmten“ Pflichten (65 %, 30 Jahre, hydraulischer Abgleich) bleibt dir 2026 **keine** als Zwang — der hydraulische Abgleich ist im EFH keine gesetzliche Pflicht, aber **Fördervoraussetzung** und Voraussetzung für eine gute JAZ.

Im BEG-Rahmen ist dafür **Verfahren B** mit raumweiser Berechnung verlangt; als Nachweis verlangen die Förderstellen ein ausgefülltes **VDZ**-Formular.

### 1.4 Widerspruch, der stehen bleibt

Das BBSR schreibt, die 65-%-EE-Anforderung sei für „Neu- und Bestandsgebäude“ entfallen `[Q08]`; für **Neubauten** ist das im Volltext nachvollziehbar (§ 10 verweist auf §§ 42–45) `[Q01]`. Ob ein **vor** dem 29.07.2026 erteilter Förderbescheid mit 65-%-Auflage weiter an seiner Auflage gebunden bleibt, regelt das GModG nicht ausdrücklich — das ist eine Frage des jeweiligen Bescheids, nicht des Gesetzes (siehe „Unbelegt“).

---

## 2. Förderung (Stand 21.07.2026)

### 2.1 Die Bestandteile

| Baustein | Satz | Bedingung | Stand/Quelle |
|---|---|---|---|
| **Grundförderung** | **30 %** | förderfähige Anlage im Bestandswohngebäude (Bauantrag ≥ 5 Jahre her), 65 % EE | `[Q09][Q11]` |
| **Klimageschwindigkeitsbonus (KGB)** | **16 %** | selbstnutzende Eigentümer, die eine **funktionstüchtige fossile** Heizung vorzeitig tauschen | `[Q09]` |
| **Einkommensbonus** | **40 %** (zvE ≤ 30.000 €), **30 %** (≤ 40.000 €), **10 %** (≤ 50.000 €) | nur selbst genutzte Wohneinheit; zu versteuerndes Haushaltsjahreseinkommen | `[Q09][Q11]` |
| **Familienzuschlag** | −10.000 € auf das anzusetzende Einkommen | mind. ein Kind < 18 J. im Haushalt, Nachweis Meldebescheinigung; einmal pro Haushalt | `[Q09][Q11]` |
| **Effizienzbonus** (früher 5 %) | **entfallen** | — | `[Q11]` |
| **Emissionsminderungszuschlag** (früher 2.500 €) | **entfallen** | — | `[Q11]` |
| **Deckel** | **80 %** der förderfähigen Kosten | Kombination der Boni | `[Q09][Q11]` |
| **förderfähige Kosten** | **28.000 €** (1. WE), 15.000 € (2.–6. WE), 8.000 € (ab 7. WE) | sinkt ab 01.02.2027 halbjährlich um **750 €**, ab 01.08.2030 dauerhaft **22.000 €** | `[Q09][Q11]` |
| **Höchstzuschuss EFH** | **22.400 €** | 80 % von 28.000 € | `[Q09]` |

### 2.2 Was das für dich bedeutet (gerechnet, nicht behauptet)

| Einkommenssituation | Fördersatz | Zuschuss bei 28.000 € Kosten | Eigenanteil |
|---|---|---|---|
| ohne KGB (nicht selbstnutzend / Heizung schon defekt) | 30 % | 8.400 € | 19.600 € |
| + KGB 16 % | 46 % | 12.880 € | **15.120 €** |
| + KGB + Einkommensbonus 10 % | 56 % | 15.680 € | 12.320 € |
| + KGB + Einkommensbonus 30 % | 76 % | 21.280 € | 6.720 € |
| + KGB + Einkommensbonus 40 % | 80 % (gedeckelt) | 22.400 € | **5.600 €** |

Rechenweg: Satz = 0,30 + 0,16 + Bonus, gedeckelt auf 0,80; Zuschuss = min(Satz; 0,80) × 28.000 €. Eigene Rechnung aus den belegten Sätzen `[Q09]`.

**Wichtig für den KGB:** Er setzt eine **funktionstüchtige** alte Heizung voraus. Wer wartet, bis der Kessel tot ist, verliert 16 Prozentpunkte = 4.480 € bei 28.000 € Kosten. Das ist die teuerste Frist des ganzen Vorhabens.

### 2.3 Die Verfallsrampe

- **KGB:** ab 01.02.2027 halbjährlich −4 Prozentpunkte; **ab Antragstellung 01.08.2028 = 0** `[Q09]`.
- **förderfähige Kosten:** ab 01.02.2027 halbjährlich −750 €, Ende 2030 bei 22.000 € `[Q09][Q11]`.
- **Ab Q1 2027 (jetzt belegt, nicht mehr strittig):** Die Grundförderung für Wärmepumpen sinkt von
  **30 % auf 15 %**, gleichzeitig kommt ein **Wertschöpfungsbonus von 15 %** für Geräte aus **EU-Fertigung**
  — in Summe bleiben 30 % also nur für EU-Geräte (Verbraucherzentrale, am 09.11.2026 im Volltext geprüft:
  „Ab dem 1. Quartal 2027 wird die Grundförderung … von bisher 30 Prozent auf 15 Prozent reduziert").
  Das **KfW-Merkblatt 458 (Stand 09/2026)** weist folgerichtig noch die 30 % aus — es beschreibt den Stand
  vor dieser Änderung. Das ist eine **Zeitachse, kein Widerspruch**; wer 2027 antragt, rechnet mit 15 %
  plus 15 % nur bei EU-Gerät.
- **Austausch einer bestehenden Wärmepumpe:** bis 31.12.2026 regulär förderfähig; ab Q1 2027 nur noch für Anlagen mit Einbau **vor 2008**, dann 25 % gedeckelt `[Q11]`.

### 2.4 Antragsweg und die Falle, die Geld kostet

1. **Vorhabenbeginn ist der Feind.** Erst Antrag, dann beauftragen: Für Anträge vor dem 21.07.2026 galten die alten Regeln, das Portal war bis 20.07.2026 geschlossen `[Q11]`.
2. Zuschuss **KfW 458** (Privatpersonen, Wohngebäude). Fossile Heizungen werden **nicht** bezuschusst, auch wenn das GModG sie wieder erlaubt `[Q11]`.
3. **Kredit obendrauf:** KfW **358 („Ergänzungskredit Plus“, bis 120.000 € für die selbstbewohnte Wohneinheit)** und **359 (bis 120.000 €/WE, Haushaltsjahreseinkommen ≤ 90.000 €)** — nur zusätzlich zu einer bereits zugesagten Zuschussförderung, die nicht älter als 12 Monate ist; Zins marktbezogen, aus Bundesmitteln bezuschusst; Merkblatt gültig ab 24.09.2026 `[Q10]`.
4. **Steuerbonus § 35c EStG** als Alternative ohne KfW: **7 % + 7 % + 6 % = 20 %** der Aufwendungen über drei Jahre, **max. 40.000 € pro Objekt**; Gebäude muss älter als 10 Jahre sein, Fachunternehmen, Rechnung + Überweisung `[Q13]`. **Nicht kombinierbar** mit Zuschüssen oder zinsverbilligten Darlehen `[Q13]`.
   - Für Wärmepumpen fordert die ESanMV eine **JAZ ≥ 3,0 nach VDI 4650 Blatt 1:2019-03**, einen hydraulischen Abgleich nach Verfahren B und **ab 01.01.2028 natürliche Kältemittel** (R290, R600a) `[Q14]`.
5. **BAFA** ist für die Gebäudehülle und die Heizungsoptimierung zuständig (15 %), nicht mehr für den Heizungstausch `[Q11]`.

---

## 3. Technik: was die Anlage können muss

### 3.1 Jahresarbeitszahl (JAZ)

Die JAZ ist der Jahresmittelwert aus erzeugter Wärme geteilt durch eingesetzten Strom. **Ab 3,0 gilt eine Wärmepumpe als effizient**; Luftwärmepumpen liegen typisch bei **3–4**, Grundwasseranlagen oft **5 und mehr** `[Q18]`. Für den Steuerbonus ist die JAZ 3,0 rechnerisch nachzuweisen `[Q14]`.

**Feldwerte statt Prospektwerte:** Luft-Wasser-Wärmepumpen erreichen im Feld im Mittel **3,4**; damit rechnet sich die Anlage besser als mit 3,0 — mit einer 5,0 aus dem Datenblatt nie. (Zahl aus dem Video-Gegencheck, ohne eigene Quelle — siehe §12.)

**Messbar machen:** Wärmemengenzähler plus Stromzähler für die WP — die JAZ ist sonst eine Behauptung des Verkäufers `[Q18]`.

### 3.2 Vorlauftemperatur: die eine Zahl, die zählt

- Effizientester Betrieb bei **30–50 °C** Vorlauf `[Q18]`.
- Im Fachforum gilt: „Wenn du im Kernwinter mit 60 °C heizen musst, dann ist das nichts für eine Wärmepumpe“ `[Q27]`.
- Faustregel aus demselben Forum: **2–2,5 % Wirkungsgradverlust je Grad** mehr Vorlauf `[Q27]`. (Die im Thread zusätzlich genannte Aussage „65° braucht doppelt so viel Strom wie 40°“ ist mit dieser Regel nicht vereinbar — Widerspruch, nicht Mittelwert.)
- **Messen statt schätzen:** an einem kalten Tag Vorlauf und Rücklauf am Kessel ablesen und mit der Heizkurve vergleichen. Wer nur „gefühlte 50 °C“ hat, kauft zu klein oder zu groß.

**Heizkurve einstellen, nicht Thermostat aufreißen.** Die Heizkurve legt fest, wie viel Vorlauf das Gerät je Außentemperatur fährt; sie ist der einzige Hebel, der die JAZ dauerhaft verschiebt. Vorgehen: Heizkurve so weit absenken, bis die Räume an einem kalten Tag gerade noch warm werden, dann einen Schritt zurück. Jedes Grad weniger Raumtemperatur spart nach Verbraucherzentrale **etwa 6 % Heizenergie** — unter **16 °C** sollte kein Raum fallen, sonst droht Feuchte und Schimmel [VZ Heizung optimieren](https://www.verbraucherzentrale.de/wissen/energie/heizen-und-warmwasser/heizung-optimieren-und-heizkosten-sparen-so-gehts-30096) (geprüft 09.11.2026, Stand 08.10.2026).

**Absenkung ist kein Sparen um jeden Preis.** Bei einer Wärmepumpe mit Fußbodenheizung kostet jede Nachtauskühlung am Morgen Wiederaufheizleistung (§ 3.4, Φ_RH) und damit Geräteleistung. 1–2 K Absenkung sind sinnvoll, 5 K nicht — die Anlage müsste dafür größer ausgelegt werden, und genau das ist der teuerste Fehler bei der Auslegung.

### 3.3 Heizkörper: tauschen oder nicht

Die Leistung eines Heizkörpers hängt an der logarithmischen Übertemperatur, nicht an der Katalogangabe (75/65/20 °C). Details, Formel und Umrechnungstabelle stehen im Playbook `heizung-lueftung.md` (§ 1.2). Kurz: bei 55/45 liefert ein Heizkörper rund **50 %** der Katalogwerte, bei 50/40 rund **40 %**. Wer „die gleiche Größe“ wieder einbaut, gewinnt nichts.

**Optionen, in dieser Reihenfolge:**
1. **Nichts tun**, wenn die Vorlauftemperatur schon ≤ 50–55 °C liegt.
2. **Einzelne** Heizkörper vergrößern (Typ 33 statt Typ 22, größere Baulänge) — günstigste Variante, häufig reicht das Wohnzimmer und ein Eckraum.
3. **Lüfter-Heizkörper** nachrüsten (magnetisch aufgesetzt) — im Projektbeispiel wurden damit 22 °C erreicht `[Q34, 04:15–04:27]`.
4. **Flächenheizung** (Fußboden, Wand, Decke) nur, wenn ohnehin Estrich/Fußboden rauskommt — sonst ist das der teuerste Weg zum gleichen Ziel (siehe `estrich.md`).

### 3.4 Heizlast: der Überschlag und seine Grenzen

**Überschlag aus dem Verbrauch** (belastbarer als jede Quadratmeterformel):

```
Heizlast [kW] ≈ Jahresverbrauch [kWh] / 2.000 h        (Vollbenutzungsstunden, Erfahrungswert)
1 l Heizöl EL = 10,0 kWh Heizwert (Hu)                 [Q31]
```

Beispiel: 2.500 l → 25.000 kWh → **12,5 kW** (ohne Wirkungsgradabzug). Mit 85 % Kesselwirkungsgrad sind es
**10,6 kW** — beide Werte sind Überschläge, die Spanne ist ehrlicher als eine Zahl. Für die Auslegung gilt
**DIN EN 12831 raumweise**; `scripts/material.py heizlast --oel-liter 2500` rechnet beide Varianten vor.
Im Fachforum wird für 3.500 l „grob 16 kW" genannt `[Q27]` — dieselbe Größenordnung.

**Der Widerspruch:** Die Baujahrstabelle von heizung.de nennt für Gebäude **bis 1977 rund 160 W/m²** `[Q19]`; bei 150 m² wären das **24 kW** — fast das Doppelte des Verbrauchswerts. Beide Zahlen sind veröffentlicht, beide sind grob. Deshalb gilt: **raumweise Heizlast nach DIN EN 12831** ist die Entscheidungsgrundlage, der Überschlag nur die Plausibilitätsprüfung `[Q19][Q01]` (§ 60c verlangt genau dieses Verfahren). Ein zu groß gewähltes Gerät taktet, verschleißt und erreicht die JAZ nicht `[Q18]`.

**Das Typenschild ist keine Heizlast.** Der kW-Wert auf dem alten Kessel ist eine historische Geräteziffer, kein Beleg für den heutigen Wärmebedarf; wer ihn übernimmt und noch einen **Sicherheitszuschlag** drauflegt, kauft doppelt zu groß. Grundlage bleibt die raumweise Heizlast nach DIN EN 12831.

**Zweites Auswahlkriterium ist die Modulationsgrenze.** Eine Vaillant VWL 75/6 regelt nur bis etwa **4,6 kW** herunter, eine Stiebel Eltron 07.2 Plus bis rund **3 kW**. Liegt der Bedarf an einem Herbsttag darunter, taktet das Gerät — deshalb gehört die **Modulationsgrenze** neben die Heizlast ins Angebot.

**Was die Norm wirklich verlangt.** Die raumweise Heizlast nach DIN EN 12831 ist eine Summe dreier Posten:

```
Φ_HL = Σ Φ_T (Transmission durch die Hüllfläche)
     + Σ Φ_V (Lüftung, Infiltration oder Anlage)
     + Σ Φ_RH (Wiederaufheizzuschlag nach Absenkphasen)
```

U-Werte nach DIN EN ISO 6946, Erdkontakt nach DIN EN ISO 13370, Wärmebrücken nach DIN V 18599-2 (detailliert: DIN 4108 Beiblatt 2) — das sind die Rechenwege, die im Energieausweis und in der Förderung wieder auftauchen [BauNetz Heizlast](https://www.baunetzwissen.de/heizung/fachwissen/waermebedarf/berechnung-der-heizlast-161074) (geprüft 09.11.2026). Zwei Konsequenzen für den Altbau:

- Die früher übliche Pauschale von **100 W/m²** führt nach derselben Quelle regelmäßig zur **Überdimensionierung** — sie ist der Grund, warum im sanierten Altbau 20-kW-Geräte stehen, die dann takten.
- Der **Wiederaufheizzuschlag** ist der Posten, den Laien gern vergessen: Wer nachts um 4 K absenkt und morgens in zwei Stunden warm haben will, braucht dafür Leistung. Wer die Absenkung auf 1–2 K begrenzt, kann das Gerät kleiner kaufen — dieselbe Wärme, weniger Kilowatt.

**Der Aufwand lohnt.** Die raumweise Berechnung ist zugleich die Grundlage für den hydraulischen Abgleich nach § 60c GModG `[Q07]` und für die Auslegung der Heizkörper (§ 3.3). Wer sie überspringt, spart an der falschen Stelle.

### 3.5 Pufferspeicher und Warmwasser

- **Die Aufgabe hat sich verschoben.** Inverter-Wärmepumpen modulieren ihre Leistung und takten deutlich weniger; der Puffer dient heute vor allem dazu, den **Mindestvolumenstrom** des Erzeugers in jeder Betriebslage zu sichern, und bei Luft-Wasser-Anlagen die **Abtauenergie** bereitzustellen. Reicht der Durchsatz nicht, sinkt nicht nur die Betriebssicherheit — es drohen Störungen bis zum Geräteschaden [IKZ Pufferspeicher](https://www.ikz.de/detail/news/detail/die-dimensionierung-von-pufferspeichern/) (geprüft 09.11.2026).
- **Wann er entfallen kann:** wenn das umgewälzte Heizungswasser in *allen* Betriebszuständen den geforderten Volumenstrom liefert. Die in Deutschland übliche **Einzelraumregelung** verlangt dagegen einen Puffer, solange kein anderes Verfahren die gleiche Regelwirkung bringt [IKZ Pufferspeicher](https://www.ikz.de/detail/news/detail/die-dimensionierung-von-pufferspeichern/) (geprüft 09.11.2026).
- **Größe, jetzt belegt.** Richtwert **10 % des stündlichen Heizwasserdurchsatzes**; bei zweistufigen Geräten genügen **8 %**, bei leistungsgeregelten Geräten im monoenergetischen Betrieb **bis 5 %**. Der Praxisrichtwert **30 l/kW** ist etabliert, bei Invertern aber nicht mehr das alleinige Kriterium: Eine pauschale Überdimensionierung kostet Wärmeverluste, Platz und Effizienz [IKZ Pufferspeicher](https://www.ikz.de/detail/news/detail/die-dimensionierung-von-pufferspeichern/) (geprüft 09.11.2026).
- **Reihen- oder Parallelpuffer.** Der **Reihenpuffer** vergrößert das Anlagenvolumen, wird gerichtet durchströmt und mischt kaum; die hydraulische Entkopplung sitzt außerhalb (etwa ein doppelt differenzdruckloser Verteiler). Der **Parallelpuffer** übernimmt zusätzlich die Entkopplung, kann Vermischung und Rücklaufanhebung aber nicht vermeiden — das kostet Effizienz und erschwert die Platzierung des Anforderungsfühlers. Entscheidung nach Herstellervorgabe, nicht nach Katalogbild [IKZ Pufferspeicher](https://www.ikz.de/detail/news/detail/die-dimensionierung-von-pufferspeichern/) (geprüft 09.11.2026).
- **Seriell einbinden, wo die Hydraulik es zulässt.** Wird der Puffer in den **Rücklauf** gelegt, entladen ihn die Heizkreispumpen selbst — keine Entladepumpe, keine eigene Regelung, und im Bestand ohne Eingriff in die vorhandene Regelung machbar. Eine Simulation an einem 500-kW-Objekt ergab rund **1 % höheren Gasverbrauch** (ca. **450 €/a**) gegen rund **380 €/a** Strom für die Entladepumpe der parallelen Variante; der Saldo von etwa **80 €/a** liegt unterhalb der Messbarkeit [IKZ Puffer-Einbindung](https://www.ikz.de/detail/news/detail/parallele-oder-serielle-einbindung/) (geprüft 09.11.2026, Artikel von 2016 — die Hydraulik gilt, der Preisstand nicht).
- **Was im Angebot stehen muss:** Puffergröße mit Herstellerbezug (Mindestvolumenstrom aus dem Datenblatt), Einbindung (Reihen/parallel/seriell), **Spreizung** im Auslegungspunkt und die **Mindestlaufzeit des Verdichters**. „Viel Puffervolumen für lange Laufzeiten“ ist eine Videoaussage `[Q34, 02:36–02:42]`, keine Auslegungsnorm — die Zahl kommt aus dem Gerätedatenblatt.
- **Warmwasser:** Speicher mit Heizwasserumspülung (Multifunktionsspeicher) löst das Legionellen-Thema konstruktiv, weil kein stehendes Trinkwasserreservoir existiert `[Q34, 02:42–02:47]`. Frischwasserstation (Durchflussprinzip) ist die Alternative mit weniger Speichervolumen, aber mehr Technik im Fließweg. Beides ist zulässig; die Entscheidung hängt am Platz.

### 3.6 Kältemittel

| Kältemittel | GWP | Vorkommen | Beleg |
|---|---|---|---|
| R410A | **2.088** | viele Bestandsgeräte (Buderus-Katalog) | `[Q32]` |
| R32 | **675** | Split-Klimageräte | `[Q32]` |
| R290 (Propan) | natürliches Kältemittel, Größenordnung „Brennstoff statt Treibhausgas“ | zunehmend Monoblock-Geräte | `[Q14]` (Nennung), GWP-Zahl siehe Unbelegt |

Zwei praktische Konsequenzen: (1) Für den **Steuerbonus** müssen ab 01.01.2028 neu installierte Wärmepumpen **natürliche Kältemittel** einsetzen — wer 2027 kauft, plant das gleich mit `[Q14]`. (2) Arbeiten am Kältemittelkreis darf nur, wer eine **Sachkundebescheinigung nach § 6 ChemKlimaschutzV** hat `[Q17]`.

**Füllmenge und Rechtsrahmen.** Eine Heizungswärmepumpe fürs Einfamilienhaus enthält üblicherweise **rund 2 kg** Kältemittel; im Normbetrieb bleibt es über die Lebensdauer im Kältekreis und wird anschließend recycelt. Die neueren chemischen Kältemittel liegen bei **GWP 150–700** und sind meist brennbar — deshalb müssen alle elektrischen Komponenten zündquellenfrei ausgeführt werden, was eine echte Neuentwicklung des Geräts bedeutet, kein Produktupdate [SBZ Kältemittel](https://www.sbz-online.de/heizung/waermepumpen-neu-denken-was-bringen-die-neuen-kaeltemittel) (geprüft 09.11.2026, Artikelstand 12/2021).

**Zeitachse statt Widerspruch:** Der SBZ-Artikel nennt die F-Gase-Verordnung von 2012/2014. Heute gilt die Verordnung **(EU) 2024/573**, angenommen am 07.02.2024, anwendbar seit **11.03.2024** — sie führt den Phase-down fort und verschärft ihn [EU F-Gase-VO](https://climate.ec.europa.eu/areas-action/fluorinated-greenhouse-gases/f-gas-legislation_en) (geprüft 09.11.2026, englische Fassung). Wer heute ein Gerät kauft, plant gegen diese Fassung, nicht gegen den Artikelstand 2021.

**R290 ist nicht „kostenlos besser“.** Propan gehört zu den natürlichen Kältemitteln mit „wenigen bis keinen Treibhausgas-Eigenschaften“, ist aber brennbar und verlangt deshalb Aufstellungs- und Lüftungsvorgaben, die im Datenblatt und in der Planung stehen müssen — die Geräte sind nicht beliebig austauschbar. Die Zahl „GWP 3“ bleibt in diesem Playbook unbelegt (siehe § 12).

### 3.7 Schall: TA Lärm, nicht Bauchgefühl

TA Lärm, Nr. 6.1 — Immissionsrichtwerte außerhalb von Gebäuden `[Q19a]`:

| Gebiet | tags | nachts |
|---|---|---|
| allgemeines Wohngebiet / Kleinsiedlung | **55 dB(A)** | **40 dB(A)** |
| reines Wohngebiet | 50 dB(A) | 35 dB(A) |
| Misch-/Dorfgebiet | 60 dB(A) | 45 dB(A) |

Kurzzeitige Spitzen dürfen tags um 30 dB(A), nachts um 20 dB(A) überschritten werden `[Q19a]`. **Achtung:** Die oft zitierte „50/35“-Regel gilt für **reines** Wohngebiet — im normalen Wohngebiet sind es 55/40. Wer mit dem falschen Wert plant, stellt zu nah auf oder zahlt ein Gutachten umsonst.

**Was die TA Lärm nicht liefert: Meter.** Sie regelt Pegel, keine Abstände. Für die Praxis braucht man die zweite Hälfte der Rechnung — und die besteht aus drei Zahlen, die man nicht verwechseln darf: **Schallleistungspegel** (am Gerät, Datenblatt), **Schalldruckpegel** (am Ohr, Messung) und der **Immissionspegel** am maßgeblichen Ort (Nachbarfenster), der aus Abstand, Abschirmung und Reflexion folgt. Der bwp-Leitfaden Schall (24 Seiten, kostenlos) behandelt Aufstellarten, Abtaugeräusche, Entkopplung vom Gebäude und die Körperschalleinleitung über Rohr- und Elektroleitungen [BauNetz Leitfaden Schall](https://www.baunetzwissen.de/heizung/tipps/planungshilfen/leitfaden-schall-4685992) (geprüft 09.11.2026).

**Körperschall ist die unterschätzte Hälfte.** Ein zusätzliches Gehäuse senkt den Luftschall; gegen Körperschall helfen nur Dämpfer oder ein eigenes Fundament. Eine vollständige Trennung ist wegen der Anschlussleitungen nicht möglich — deshalb entscheidet die **lärmarme Auslegung** und nicht die Nachrüstung [BauNetz Schall Gebäudetechnik](https://www.baunetzwissen.de/bauphysik/fachwissen/schallschutz/schutz-gegen-laerm-aus-gebaeudetechnischen-anlagen-4408801) (geprüft 09.11.2026).

**Praktische Prüfliste vor dem Kauf:** Schallleistungspegel im Datenblatt (nicht „leise“), Nachtabsenkung des Ventilators, Aufstellort mit Abstand zum nächsten schutzbedürftigen Fenster, elastische Entkopplung und eine schallentkoppelte Rohrdurchführung. Wer die Werte nicht schriftlich hat, kann sie später nicht beweisen.

### 3.8 Aufstellort, Kondensat, Fundament

- **Aufstellort:** außen an der Wand, auf dem Dach oder im Freien; Abstand zum Nachbarfenster und zur Grundstücksgrenze ist eine Schallfrage, keine feste Meterzahl (siehe Unbelegt).
- **Kondensat:** fällt bei Luft-Wasser-Anlagen ganzjährig an und muss **gefällefähig** abgeführt werden (Siphon, Frostschutz) — sonst Eisfläche vor der Tür.
- **Fundament:** lastabtragend, frostfrei, schwingungsentkoppelt; bei Aufstellung auf dem Boden ist ein Streifenfundament/Platte üblich. Maße kommen aus dem Gerätedatenblatt, nicht aus dem Kopf.

---

## 4. Ölheizung ausbauen

### 4.1 Rechtlicher Rahmen: AwSV, nicht Handwerkergusto

| Vorgang | Regel | Beleg |
|---|---|---|
| Stilllegung, Innenreinigung, Instandsetzung, Errichtung von Heizölverbraucheranlagen | **nur Fachbetrieb** (§ 45 Abs. 1 Nr. 4 AwSV) | `[Q15]` |
| Bei Stilllegung: alle wassergefährdenden Stoffe „soweit technisch möglich“ entfernen, Anlage gegen missbräuchliche Nutzung sichern | § 17 Abs. 4 AwSV | `[Q15]` |
| Prüfpflichten/Prüfzeitpunkte bei Stilllegung | Anlage 5/6 AwSV | `[Q15]` |

Praktisch heißt das: **Tank entleeren, reinigen, stilllegen und entsorgen ist Fachbetriebsarbeit** — unabhängig davon, ob es ein 1.000-l-Kunststofftank oder ein geschweißter Stahltank ist. Die häufig zitierte 1.000-l-Schwelle stammt aus einer **anderen** Regel: Auf ein Rückhaltevolumen kann bei oberirdischen Anlagen der Wassergefährdungsklasse 1 bis 1.000 l unter Bedingungen verzichtet werden (AwSV, Anforderungen an die Rückhaltung) — über die Fachbetriebspflicht sagt sie nichts `[Q15]`.

### 4.2 Ablauf in sieben Schritten

1. **Restöl abpumpen** und – wenn sauber – verkaufen/abgeben; sonst fachgerecht entsorgen `[Q20]`.
2. **Tank innen reinigen** (Öl-Wasser-Gemisch, Schlamm) — Fachbetrieb `[Q35, 01:16–01:22]`.
3. **Stilllegen oder demontieren.** Stilllegen = Tank bleibt, ist entleert, gereinigt, verschlossen; Demontage = Tank wird zerschnitten und ausgetragen `[Q35, 01:33–01:56]`.
4. **Ölleitungen spülen** und tot legen (beide Enden trennen, spülen, verschließen) — Leitungen sind Teil der Anlage.
5. **Kessel demontieren**, Kesselwasser vorher ablassen, Anschlüsse trennen.
6. **Entsorgung mit Nachweis**: Altöl, ölbehaftete Bauteile, Kessel, Tankteile. Bescheinigung des Fachbetriebs zur Stilllegung/Beseitigung aufbewahren.
7. **Schornstein**: siehe 4.4.

Ein Praxisbeispiel (Video, 15.000-l-Tank): Provisorium für Starkstrom, Durchbruch durch die Betonwand, Restöl pumpen, Reinigung, Zerschneiden, Ausbau, provisorische Warmwasserversorgung, Tankraum wird Kellerraum `[Q35, 00:25–02:28]`.

### 4.3 Kosten (Band, je 1.000 l Tankvolumen)

| Bauart | Kosten Entsorgung | Beleg |
|---|---|---|
| Kunststofftank | 400–700 € | `[Q20]` |
| modularer Stahltank | 700–1.000 € | `[Q20]` |
| im Haus geschweißter Stahltank | 1.000–1.500 € | `[Q20]` |
| unterirdischer Tank | 1.500–2.500 € | `[Q20]` |

Dazu kommen Demontage des Kessels, Leitungsarbeiten und Entsorgung des Kessels — im Projektbeispiel waren Rückbau + Entsorgung + Tanks im Pauschalpreis von 52.000 € enthalten `[Q34, 03:13–03:20]`.

### 4.4 Schornstein

- **Kehrpflicht entfällt**, wenn die Anlage **dauerhaft stillgelegt** ist, die Anschlussöffnungen **dichte Verschlüsse aus nicht brennbaren Stoffen** haben und die Stilllegung **mitgeteilt** wurde (KÜO § 1 Abs. 3 Nr. 1) `[Q16]`.
- Der Schornstein bleibt als Baukörper stehen und kann weiter genutzt werden (Zuluft für Kaminofen, Kabel, Leitungen) — die Nutzungsänderung ist mit dem Bezirksschornsteinfeger abzustimmen, weil er die Feuerstättenschau macht.
- **Nicht** einfach „zumauern“: Verschluss muss dicht, nicht brennbar und dokumentiert sein `[Q16]`.

### 4.5 Tankraum weiternutzen

Der Raum ist nach Ausbau ein normaler Kellerraum — im Video „steht als neuer Kellerraum zur Verfügung“ `[Q35, 02:25–02:28]`. Vorher prüfen: Ölgeruch (Bodenaufbau kann getränkt sein), Feuchte, Bodenschutz. Bei Verdacht auf Durchtränkung: Probe und Sanierung, nicht überstreichen.

---

## 5. Elektro und Gewerke

### 5.1 Wer macht was

| Aufgabe | Wer | Rechtsgrundlage/Beleg |
|---|---|---|
| Kältemittelkreis, Inbetriebnahme der WP | Fachbetrieb mit Sachkunde | § 6 ChemKlimaschutzV `[Q17]` |
| Öltankanlage stilllegen/reinigen | Fachbetrieb AwSV | § 45 AwSV `[Q15]` |
| 230/400-V-Anlage errichten/ändern | eingetragenes Elektro-Installationsunternehmen | NAV § 13 Abs. 2 (Beleg im Basisskill `references/quellen.md`) |
| Netzanschluss anmelden | Elektrofachbetrieb beim Netzbetreiber | VDE-AR-N 4100 / TAB `[Q21]` |
| Kernbohrung durch Fassade | Bohr-Fachbetrieb (Statik, Dichtheit, Gefälle) | Praxisbeispiel `[Q37, 06:57–09:01]` |
| Heizungsrohre, Speicher, Heizkörper | SHK-Fachbetrieb | HwO Anlage A (Basisskill) |
| Fundament, Graben, Dämmung Leitungen | Eigenleistung möglich | § 8 unten |
| Dachdurchdringung (Aufstellung auf Dach) | Dachdecker | DachAusbV (Basisskill) |

### 5.2 Stromkreis und Zählerplatz

- Die Wärmepumpe ist eine **Dauerstrom-Anwendung**. In der VDE-AR-N 4100 gilt: Die Forderung nach 63 A Strombelastbarkeit greift **nicht** für die Abgangsleitung zu einer Anwendung mit Dauerstromverhalten „z. B. einer Wärmepumpe“, solange in der Unterverteilung keine weiteren Endstromkreise davon abgezweigt werden `[Q21]`.
- **Zählerplatzbelastung:** bei interner Verdrahtung mit 10-mm²-Leitungen max. **32 A** `[Q21]`. Wer WP + Wallbox + Durchlauferhitzer gleichzeitig plant, kommt hier an die Grenze — dann braucht es einen eigenen Zählerplatz oder Lastmanagement.
- **Eigener Zähler** ist die Voraussetzung für einen Wärmepumpen-Tarif `[Q18]`.
- **Netzdienliche Steuerung:** Für steuerbare Verbrauchseinrichtungen sind Vereinbarungen über netzorientierte Steuerung im Gegenzug für Netzentgelt-Reduzierungen vorgesehen (§ 14a EnWG) `[Q33]`. Der Netzbetreiber verlangt das im Anmeldeformular — vor Beauftragung des Elektrikers klären, sonst wird zweimal gebaut.
- **Wer steuerbar wird und was das heißt:** alle Wärmepumpen mit mehr als **4,2 kW** Bezugsleistung — ebenso nicht öffentliche Wallboxen, Klimageräte und Batteriespeicher. Die Steuerung erfolgt über das **Smart Meter Gateway**, nicht mehr über Zeitschaltuhr oder Rundsteuerempfänger; der Netzbetreiber darf den Anschluss seit **01.01.2024** nicht mehr mit dem Argument drohender Netzüberlastung ablehnen, auch wenn er noch gar nicht dimmt [Elektropraktiker § 14a](https://www.elektropraktiker.de/nachrichten/nachricht/waermepumpen-co-muessen-ab-januar-2024-aus-dem-netz-steuerbar-sein) (geprüft 09.11.2026). Praktische Folge: Steuerleitung, Klemmblock und Platz im Zählerkasten von Anfang an vorsehen — die Details stehen in `pv-speicher-wallbox.md` § 4.2.
- **Alte Sperrzeiten-Denke:** Starre Sperrzeiten sind mit der netzorientierten Steuerung abgelöst; gedimmt wird auf eine Mindestleistung, nicht abgeschaltet. Wer eine Anlage aus der Zeit davor übernimmt, prüft, ob die Steuerung noch über einen alten Empfänger läuft — der erfüllt die Anforderung nicht [Elektropraktiker § 14a](https://www.elektropraktiker.de/nachrichten/nachricht/waermepumpen-co-muessen-ab-januar-2024-aus-dem-netz-steuerbar-sein) (geprüft 09.11.2026).

### 5.3 Wallbox-Anbindung

Wallbox und Wärmepumpe teilen sich oft denselben Hausanschluss. Der Elektriker rechnet die **Gleichzeitigkeit** (DIN 18015-1 / TAB) und entscheidet, ob ein Lastmanagementsystem nötig ist. Eigenleistung: Kabelweg und Leerrohre vorbereiten, nicht anschließen.

---

## 6. Kosten und Rechenbeispiele

### 6.1 Investition (brutto, inkl. Installation, vor Förderung)

| System | Kosten EFH | Beleg |
|---|---|---|
| **Luft-Wasser-Wärmepumpe** | **24.000–32.000 €** (Gerät 12.000–15.900 €, Installation 12.000–16.000 €) | `[Q22]` |
| Luft-Wasser (Herstellerangabe mit weiter Spanne) | 18.000–54.000 € | `[Q21a]` |
| Erdwärmepumpe, Flachkollektor | 29.000–39.000 € | `[Q22]` |
| Erdwärmepumpe, Erdsonden | 40.000–50.000 € | `[Q22]` |
| Luft-Luft (Klima-Split, Multi) | 12.500–17.500 € | `[Q23]` |
| Pelletheizung | 20.000–50.000 € | `[Q24]` |
| Gasheizung (Vergleichslinie) | 9.000–15.500 € | `[Q25]` |
| Fernwärme-Anschluss | 5.000–20.000 € (Tabellenspalte im selben Text: 5.000–15.000 €) | `[Q26]` |

**Widerspruch, der stehen bleibt:** Stiebel nennt 24.000–32.000 €, Viessmann 18.000–54.000 € für dieselbe Gerätegattung `[Q22][Q21a]`. Die Spanne ist keine Ungenauigkeit, sondern der Unterschied zwischen „Kesseltausch mit WP“ und „Sanierung mit Heizkörpertausch, Elektro, Kernbohrung, Fundament“.

### 6.2 Preise, mit denen gerechnet wird (09.11.2026)

| Größe | Wert | Beleg |
|---|---|---|
| Heizöl EL, DE-Mittel, 3.000 l, inkl. MwSt. | **1,738 €/l** | `[Q28]` |
| Strom, Neukunde, inkl. Steuern/Abgaben | **34,6 ct/kWh** (Bestandskunden 35,7; Grundversorgung 42,83) | `[Q29]` |
| CO₂-Preis 2026/2027 | **55–65 €/t** (2025 fix 55 €; ETS2-Start auf 2028 verschoben) | `[Q30]` |
| Heizöl EL Heizwert | **10,0 kWh/l** | `[Q31]` |
| CO₂ je Liter Heizöl | **2,66 kg** (266 g/kWh × 10 kWh) | `[Q31]` |

### 6.3 Beispielhaus (1965, 150 m², 2.500 l/Jahr)

**Ausgangslage:** 2.500 l × 10 kWh/l = **25.000 kWh** Endenergie; bei angenommenen 85 % Kesselwirkungsgrad (Annahme, nicht belegt) **21.250 kWh** Nutzwärme.

```
Ölkosten     = 2.500 l × 1,738 €/l                      = 4.345 €/Jahr
WP-Strom     = 21.250 kWh / JAZ 3,0  = 7.083 kWh
WP-Kosten    = 7.083 kWh × 0,346 €/kWh                  = 2.451 €/Jahr
Ersparnis    = 4.345 − 2.451                            = 1.894 €/Jahr
```

**Investition und Förderung** (Luft-Wasser, 28.000 €, KGB 16 %, kein Einkommensbonus):

```
Zuschuss  = 0,46 × 28.000 €                             = 12.880 €
Eigenanteil = 28.000 − 12.880                           = 15.120 €
Amortisation = 15.120 / 1.894                           ≈ 8,0 Jahre
```

**Ehrlicher zweiter Blick — Mehrinvestition:** Eine neue Gasheizung kostet 9.000–15.500 € (Mittel 12.000 €) und bekommt **0 % Förderung** `[Q25]`. Die Wärmepumpe kostet dich nach Förderung 15.120 €, also **3.120 € mehr**. Diese Mehrinvestition amortisiert sich in **1,6 Jahren** — das ist die Zahl, die die Entscheidung trägt, nicht die 8 Jahre.

**Jahreskostenvergleich (Annuität 3 %, 20 Jahre):**

```
Annuität = I × (q−1)/(1−q^−n),  q = 1,03, n = 20  → Faktor 0,0672
WP:  15.120 × 0,0672 = 1.016 €/a  + 2.451 Betrieb + 250 Wartung  = 3.717 €/a
Öl:                       4.345 €/a + 300 Wartung + 150 Schornstein = 4.795 €/a   (Wartung/Schornstein: Schätzwerte)
Vorteil WP: 1.078 €/Jahr
```

**Gegenrechnung aus einem Video (Widerspruch, nicht gemittelt):** dort werden „mindestens **24.000 €** Eigenanteil nach Förderung“ bei **20 Jahren** Haltbarkeit angesetzt (= 1.000 €/Jahr). Dieses Rechenbeispiel kommt mit **15.120 €** aus, weil andere Gerätepreise angenommen werden. Beide Annahmen offenlegen, statt eine Zahl zu wählen.

### 6.4 Sensitivität (dieselbe Anlage)

| Variable | Wert | Ersparnis/Jahr | Amortisation 15.120 € |
|---|---|---|---|
| Ölpreis | 1,00 €/l | 49 € | **308 Jahre** |
| Ölpreis | 1,30 €/l | 799 € | 18,9 Jahre |
| Ölpreis | **1,738 €/l** | **1.894 €** | **8,0 Jahre** |
| Ölpreis | 2,00 €/l | 2.549 € | 5,9 Jahre |
| Strompreis | 25 ct/kWh | 2.574 € | 5,9 Jahre |
| Strompreis | **34,6 ct/kWh** | **1.894 €** | **8,0 Jahre** |
| Strompreis | 45 ct/kWh | 1.158 € | 13,1 Jahre |
| JAZ | 2,5 | 1.404 € | 10,8 Jahre |
| JAZ | 4,0 | 2.507 € | 6,0 Jahre |

**CO₂-Preis-Sensitivität:** 2.500 l = 6,65 t CO₂. Bei 65 €/t sind das 432 €/Jahr (im Ölpreis enthalten), bei 100 €/t 665 €/a (+233 €/a), bei 150 €/t 998 €/a (+565 €/a) `[Q30][Q31]` — eigene Rechnung, Faktoren belegt.

**Die unbequeme Wahrheit aus der Tabelle:** Die Null-Linie liegt bei **0,98 €/l** Öl (2.451 € WP-Betriebskosten ÷ 2.500 l). Darunter spart die Wärmepumpe über die Brennstoffkosten **nichts**; unter 1,30 €/l liegt die Amortisation jenseits von 18 Jahren. Dann tragen nur drei Argumente: CO₂-Preis-Steigerung, Komfort/Wartungsfreiheit und das Risiko, in 10 Jahren ohnehin tauschen zu müssen. Wer mit 1,00 €/l kalkuliert, kalkuliert gegen den Markt — der Preis stand am 09.11.2026 bei 1,738 €/l `[Q28]`.

### 6.5 Projektbeispiel aus der Praxis (Herstellervideo, nicht neutrale Quelle)

Zweifamilienhaus 290 m², Bj. 1935, teilsaniert, überwiegend Heizkörper:
- 52.000 € für Installation, WP, Rückbau, Entsorgung, Öltanks; **23.600 € Förderung** → **28.400 € Eigenanteil** `[Q34, 03:05–03:20]`
- Öl vorher 3.000 €/Jahr, WP ~2.500 €/Jahr → 500 €/Jahr; Amortisation „zehn, fünfzehn Jahre“ `[Q34, 03:47–04:03]`
- Zwei Räume mussten mit Lüfter-Heizkörpern nachgerüstet werden `[Q34, 04:15–04:27]`

Das ist eine Herstellerdarstellung (alpha innotec) — die Zahlen sind plausibel, aber nicht unabhängig geprüft. Sie zeigt außerdem die ehrliche Größenordnung: **52.000 €** ist realistisch, wenn Rückbau und Tanks enthalten sind.

---

## 7. Alternativen im Vergleich

| System | Investition | Betrieb | Eignung im 1960er-Bestand | Beleg |
|---|---|---|---|---|
| **Luft-Wasser-WP** | 24.000–32.000 € | Strom, JAZ 3–4 | Standardlösung; braucht Fläche für Außengerät + Schallabstand | `[Q22][Q18]` |
| **Sole-Wasser-WP** | 29.000–50.000 € | Strom, höhere JAZ | beste Effizienz; braucht Garten/Bohrung + Genehmigung | `[Q22]` |
| **Gas-Hybrid** (§ 42 Nr. 5) | 9.000–15.500 € + WP-Teil | Gas + Strom | nur sinnvoll, wenn Gasanschluss liegt und Heizflächen knapp sind; Bio-Treppe gilt | `[Q25][Q01]` |
| **Pellets** | 20.000–50.000 € | Pelletpreis, Brennstofflager, Asche | braucht Lagerraum + Schornstein; Förderung ja, aber keine 65-%-Pflicht mehr | `[Q24]` |
| **Fernwärme** | 5.000–20.000 € Anschluss | 10–18 ct/kWh + 200–800 €/a Grundpreis | nur wo Netz liegt; kein Kessel, keine Wartung | `[Q26]` |
| **Solarthermie** | (nicht separat belegt) | sonnenabhängig | Heizungsunterstützung/Warmwasser, kein Ersatz für Kessel | `[Q01]` (§ 44) |
| **Klima-Split (Luft-Luft)** | 12.500–17.500 € | Strom, weniger effizient | günstig, schnell, aber Raumluft-Wärme; als Übergangslösung oder für einzelne Räume | `[Q23]` |
| **Infrarot/Stromdirekt** | 65–650 € je Paneel | Strom 1:1, Betriebskosten „mehrere Tausend Euro pro Jahr“ | nur für einzelne Räume; § 46 GModG begrenzt den Einbau | `[Q27a][Q01]` |

**Einordnung:** Wer einen Gasanschluss hat und die Heizflächen nicht anfassen will, kann mit einer Wärmepumpen-Hybridlösung starten (§ 42 Nr. 5, § 43 Abs. 5) — er erfüllt die Bio-Treppe über den WP-Anteil `[Q01]`. Wer keinen Gasanschluss hat, für den ist die Kombination aus Luft-Wasser-WP und Heizkörpertausch fast immer der günstigste Weg.

---

## 8. Was du selbst machen kannst — und was nicht

| Aufgabe | Selbst? | Warum / Rechtsgrundlage |
|---|---|---|
| Kessel entleeren, Anschlüsse trennen, Kessel zerlegen | **ja, nach Absprache** | für den Abbau eines stillgelegten Kessels gibt es keine ausdrückliche Fachbetriebspflicht (anders als für die Öltankanlage); der Ölkreislauf muss vorher leer sein |
| Öltank entleeren/reinigen/stilllegen/entsorgen | **nein** | § 45 Abs. 1 Nr. 4 AwSV `[Q15]` |
| Ölleitungen spülen und tot legen | **nein** (Teil der Anlage) | AwSV-Anlage; Praxis: Fachbetrieb `[Q15]` |
| Graben für Erdkollektor/Leitungen | **ja** (Aushub), Verlegung nein | Erdarbeiten sind keine Fachbetriebsarbeit; Kollektorverlegung + Anschluss Fachbetrieb |
| Kernbohrung durch die Fassade | **nein** | Statik, Dichtheit, Gefälle, Bohrkrone nass; Praxisbeispiel lässt bohren `[Q37, 06:57]` |
| Fundament/Platte für Außengerät gießen | **ja** | Maurer-/Betonarbeit, Maße aus Datenblatt |
| Rohrleitungen dämmen (Heizung) | **ja** | Dämmung ist keine Anlagenänderung; Anlage 8 GModG nennt die Anforderungen `[Q01]` |
| Heizkörper tauschen (1:1) | **ja, mit Risiko** | siehe `heizung-lueftung.md` § 0 — Grauzone, Gewährleistung geht verloren |
| Kältemittelkreis öffnen, evakuieren, füllen | **nein** | § 6 ChemKlimaschutzV (Sachkunde) `[Q17]` |
| Elektroanschluss, Zähler, Netzanschluss | **nein** | NAV § 13 Abs. 2 (Basisskill); VDE-AR-N 4100 `[Q21]` |
| Gasleitungen | **nein** | TRGI, Fachbetrieb |
| Inbetriebnahme/Regelung einstellen | **teilweise** | Heizkurve und Absenkung sind Bedienung; Auslegung ist Planung |
| Fördermittelantrag | **ja** | KfW-Portal, Antrag vor Vorhabenbeginn `[Q11]` |

**Der Förderschock:** Wer selbst einbaut und den Antrag erst danach stellt, bekommt nichts — genau das passiert im Selbstbau-Video, wo der Autor die Förderung „nachträglich einreichen“ will, nachdem er rund 7.000 € Material verbaut hat `[Q37, 25:51–26:30]`. Förderfähig ist nur ein Antrag **vor** Beginn `[Q11]`. Eigenleistung im förderfähigen Gewerk ist zudem oft ausgeschlossen, weil die KfW eine Fachunternehmererklärung verlangt.

---

## 9. Die Fehler, die Geld kosten

1. **Förderantrag nach Baubeginn** → 0 €. Antrag zuerst, dann Bestellung `[Q11][Q37, 25:51]`.
2. **KGB verschenkt, weil die Heizung erst repariert wurde, bis sie tot war** → 16 Prozentpunkte = 4.480 € bei 28.000 € `[Q09]`.
3. **Gerät nach Quadratmeterformel oder Typenschild ausgelegt** → 24 kW statt 12,5 kW, Takten, JAZ unter 3 `[Q19][Q27][Q18]`; dasselbe passiert, wer den kW-Wert des alten Kessels plus Sicherheitszuschlag übernimmt (§3.4).
4. **Heizkörper „in gleicher Größe“ getauscht** → bei 55/45 nur ~50 % Leistung, Raum wird nicht warm (Formel in `heizung-lueftung.md`).
5. **Schall mit 50/35 dB(A) gerechnet** → das ist reines Wohngebiet; im allgemeinen Wohngebiet gelten 55/40 `[Q19a]`.
6. **Öltank selbst „stillgelegt“** → AwSV-Verstoß, keine Bescheinigung, späterer Hausverkauf wird zum Problem `[Q15]`.
7. **Kondensatablauf vergessen** → Eisplatte, Feuchteschaden an der Fassade.
8. **Zählerplatz überlastet** (WP + Wallbox + Durchlauferhitzer) → 32-A-Grenze bei 10 mm² `[Q21]`.
9. **Steuerbonus und KfW-Zuschuss gleichzeitig angesetzt** → § 35c Abs. 3 verbietet die Doppelförderung `[Q13]`.
10. **Steuerbonus ohne JAZ-Nachweis** → ESanMV fordert JAZ ≥ 3,0 `[Q14]`.
11. **Pufferspeicher nach Gefühl** → kein belegter Richtwert; Auslegung gehört ins Angebot.
12. **Angebot ohne Positionen** („Wärmepumpe komplett 28.000 €“) → nicht vergleichbar; nach Gerät, Montage, Elektro, Kernbohrung, Rückbau, Entsorgung, Inbetriebnahme aufschlüsseln.

---

## 10. Kontrollpunkte

**Vor der Entscheidung**
- [ ] Vorlauftemperatur bei Kälte gemessen (nicht geschätzt)
- [ ] Jahresverbrauch der letzten 3 Jahre in Litern
- [ ] Heizlast überschlagen (kWh/2.000 h) und mit W/m²-Tabelle plausibilisiert
- [ ] Aufstellort: Schall zum Nachbarn, Kondensat, Fundament, Stromweg
- [ ] Wärmequelle geprüft (Garten, Bohrung, Wasserrecht)
- [ ] Förderfähigkeit: Bauantrag ≥ 5 Jahre, selbstgenutzt?, Einkommen, Kinder

**Vor der Beauftragung**
- [ ] Förderantrag gestellt und bestätigt (vor Vorhabenbeginn!)
- [ ] Angebot positionenweise, inkl. Elektro, Kernbohrung, Rückbau, Entsorgung
- [ ] Fachbetriebe für AwSV-Stilllegung und Kältemittel benannt
- [ ] Netzbetreiber-Anmeldung und § 14a-Klärung terminiert

**Vor der Abnahme**
- [ ] Hydraulischer Abgleich nach Verfahren B dokumentiert (Einstellwerte, raumweise Heizlast)
- [ ] Wärmemengenzähler + Stromzähler für die JAZ eingebaut
- [ ] Heizkurve eingestellt; **keine tiefe Nachtabsenkung** (die Wärmepumpe arbeitet am effizientesten im Halten der Temperatur; kurzes Absenken spart nichts, weil morgens mit schlechterem COP wieder aufgeheizt wird — der Effekt steht in keinem Verhältnis zum Komfortverlust)
- [ ] Dichtheitsprotokoll Heizung, Elektro-Messprotokoll (DIN VDE 0100-600)
- [ ] Stilllegungs-/Entsorgungsbescheinigung Öltank im Ordner
- [ ] Schornsteinverschluss dokumentiert und mitgeteilt `[Q16]`

---

## 11. Quellen

| Nr. | Quelle | URL | Stand/Abruf |
|---|---|---|---|
| Q01 | GModG Volltext (gesetze-im-internet.de), §§ 1, 10, 35, 42, 42a, 43, 44, 45, 46, 60b, 60c, 92, 107 | https://www.gesetze-im-internet.de/geg/ | Fassung 29.07.2026, abgerufen 09.11.2026 |
| Q02 | § 72 GModG (weggefallen) | https://www.gesetze-im-internet.de/geg/__72.html | 09.11.2026 |
| Q03 | § 43 GModG (Bio-Treppe) | https://www.gesetze-im-internet.de/geg/__43.html | 09.11.2026 |
| Q04 | § 42a GModG (Grüngasquote) | https://www.gesetze-im-internet.de/geg/__42a.html | 09.11.2026 |
| Q05 | § 46 GModG (Stromdirektheizung) | https://www.gesetze-im-internet.de/geg/__46.html | 09.11.2026 |
| Q06 | § 60b GModG (Heizungsprüfung) | https://www.gesetze-im-internet.de/geg/__60b.html | 09.11.2026 |
| Q07 | § 60c GModG (hydraulischer Abgleich) | https://www.gesetze-im-internet.de/geg/__60c.html | 09.11.2026 |
| Q08 | BBSR/Bund: „Neuregelungen mit dem GModG“ (Inkrafttreten, §§ 71–73 entfallen, Bio-Treppe, 2027 EPBD) | https://gmodg.bund.de/GModG/DE/GModGRegelungen/GModG_neu/GModG_neu-node.html | abgerufen 09.11.2026 |
| Q09 | KfW, Infografik „Neue Bedingungen der Heizungsförderung“ (30 %, 16 %, 40/30/10 %, 28.000 €, 22.400 €) | https://www.kfw.de/PDF/Download-Center/F%C3%B6rderprogramme-(Inlandsf%C3%B6rderung)/PDF-Dokumente/Infografik_Heizungsf%C3%B6rderung_Anpassungen_Juli_2026.pdf | Stand 21.07.2026 |
| Q10 | KfW Merkblatt 358/359 Ergänzungskredit (120.000 €, 90.000 € Einkommen, Laufzeiten) | https://kfw.de/PDF/Download-Center/F%C3%B6rderprogramme-(Inlandsf%C3%B6rderung)/PDF-Dokumente/6000005135_M_358_359.pdf | gültig ab 24.09.2026 |
| Q11 | ADAC: KfW-Heizungsförderung 2026 (Neustart 21.07.2026, Bonusentfall, Wertschöpfungsbonus ab Q1 2027 genannt — steht im Widerspruch zum KfW-Merkblatt 458, das 30 % Grundförderung ausweist) | https://www.adac.de/rund-ums-haus/energie/spartipps/foerderung-heizung/ | abgerufen 09.11.2026 — die dort genannte 15-%-Stufe ab Q1 2027 ist durch die Verbraucherzentrale bestätigt (09.11.2026) |
| Q12 | Heid Energieberatung: „Austauschpflicht abgeschafft“ (30-Jahre-Regel, 2045-Verbot, Gasetagenheizung) | https://www.heid-energieberatung.de/ratgeber/heizung-austauschpflicht/ | aktualisiert 29.08.2026 |
| Q13 | § 35c EStG Volltext (7/7/6 %, 40.000 €, Doppelförderungsverbot) | https://www.gesetze-im-internet.de/estg/__35c.html | 09.11.2026 |
| Q14 | ESanMV Volltext (Anlage 6: JAZ ≥ 3,0 nach VDI 4650; natürliche Kältemittel ab 01.01.2028) | https://www.gesetze-im-internet.de/esanmv/BJNR000300020.html | 09.11.2026 |
| Q15 | AwSV Volltext § 45 (Fachbetriebspflicht, auch Stilllegung) und § 17 Abs. 4 | https://www.gesetze-im-internet.de/awsv/__45.html · https://www.gesetze-im-internet.de/awsv/__17.html | 09.11.2026 |
| Q16 | KÜO § 1 (Ausnahme von der Kehrpflicht bei dauerhafter Stilllegung) | https://www.gesetze-im-internet.de/k_o/__1.html | 09.11.2026 |
| Q17 | § 6 ChemKlimaschutzV (Sachkundebescheinigungen für Kältemittelarbeiten) | https://www.gesetze-im-internet.de/chemklimaschutzv_2026/__6.html | 09.11.2026 |
| Q18 | Verbraucherzentrale: Wärmepumpe (JAZ ≥ 3, Luft 3–4, Vorlauf 30–50 °C, Zähler) | https://www.verbraucherzentrale.de/wissen/energie/heizen-und-warmwasser/waermepumpe-alles-was-sie-wissen-muessen-5439 | 09.11.2026 |
| Q19 | heizung.de: Heizlastberechnung, W/m²-Tabelle nach Baujahr, Überschlagsformel | https://www.heizung.de/ratgeber/diverses/heizlastberechnung-zur-bestimmung-der-heizleistung.html | 09.11.2026 |
| Q19a | TA Lärm, Nr. 6.1 (Immissionsrichtwerte 55/40, 50/35 dB(A)) | https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_26081998_IG19980826.htm | 09.11.2026 |
| Q20 | heizung.de: Öltank entsorgen (AwSV, Ablauf, Kosten je Bauart) | https://heizung.de/oelheizung/wissen/oeltank-entsorgen-ablauf-zeitpunkt-kosten.html | 09.11.2026 |
| Q21 | VDE FNN: TAR Niederspannung VDE-AR-N 4100 (63-A-Ausnahme für WP, 32-A-Grenze 10 mm²) | https://www.vde.com/de/fnn/themen/tar/tar-niederspannung/tar-niederspannung-vde-ar-n-4100 | 09.11.2026 |
| Q21a | Viessmann: Wärmepumpe Kosten (18.000–54.000 €, Rechenbeispiele 30 %/80 %) | https://www.viessmann.de/de/wissen/technik-und-systeme/waermepumpe/waermepumpe-kosten.ext.html | 09.11.2026 |
| Q22 | Stiebel Eltron: Wärmepumpe Kosten 2026 (24.000–32.000 €, Sole 29–39 T€, Sonde 40–50 T€) | https://stiebel-eltron.de/de/waermepumpen-ratgeber/kosten-foerderung/waermepumpe-kosten.html | Stand 09/2026 |
| Q23 | co2online: Luft-Luft-Wärmepumpe (12.500–17.500 € EFH) | https://co2online.de/modernisieren-und-bauen/waermepumpe/luft-luft-waermepumpe | 09.11.2026 |
| Q24 | Thermondo: Kosten Pelletheizung (20.000–50.000 €) | https://www.thermondo.de/info/rat/erneuerbare-energie/kosten-pelletheizung | aktualisiert 27.09.2026 |
| Q25 | Thermondo: Gasheizung Kosten (9.000–15.500 €, 0 % Förderung) | https://www.thermondo.de/info/rat/gas/gasheizung-kosten/ | aktualisiert 27.09.2026 |
| Q26 | Enpal: Fernwärme Kosten (Anschluss 5.000–20.000 €, Arbeitspreis 10–18 ct/kWh) | https://www.enpal.de/waermepumpe/fernwaerme | 09.11.2026 |
| Q27 | haustechnikdialog, Thread 223679 „Ölheizung durch Wärmepumpe ersetzen, EFH 1988“ (3.500 l ≈ 16 kW; 60 °C = nicht WP-geeignet; 2–2,5 %/K) | https://www.haustechnikdialog.de/Forum/t/223679/Oelheizung-durch-Waermepumpe-ersetzen-EFH-Baujahr-1988 | 09.11.2026 |
| Q27a | ADAC: Infrarotheizung (65–650 €/Paneel, hohe Betriebskosten) | https://adac.de/rund-ums-haus/energie/versorgung/infrarotheizung | 09.11.2026 |
| Q28 | Tecson: Heizölpreise, DE-Mittel 173,8 ct/l am 09.11.2026 | https://www.tecson.de/de/heizoelpreise.html | 09.11.2026 |
| Q29 | Strom Report: Strompreise 09.11.2026 (34,6 / 35,7 / 42,83 ct/kWh) | https://strom-report.com/strompreise/ | 09.11.2026 |
| Q30 | Clean Energy Wire: CO₂-Preis 2025 fix 55 €/t, Korridor 55–65 €/t, ETS2-Start 2028 | https://www.cleanenergywire.org/news/germany-freeze-national-co2-price-2027-eu-delays-emissions-trading | 09.11.2026 |
| Q31 | heizwert.info: Heizöl EL 10,0 kWh/l (Hu), 10,6 kWh/l (Ho), 346 g CO₂/kWh Wärme | https://heizwert.info/heizoel/ | 09.11.2026 |
| Q32 | Buderus: F-Gase-Tabelle (R410A GWP 2.088, R32 GWP 675, CO₂-Äquivalente je Gerät) | https://www.buderus.de/de/foerderungen/verordnungen-gesetze/f-gas-kaeltemittel-66652 | 09.11.2026 |
| Q33 | § 14a EnWG (netzorientierte Steuerung steuerbarer Verbrauchseinrichtungen) | https://www.gesetze-im-internet.de/enwg_2005/__14a.html | 09.11.2026 |
| Q34 | YouTube alpha innotec: „Wärmepumpe statt Ölheizung im Altbau (BJ 1935)“, 5:42 — 52.000 €, 23.600 € Förderung, 28.400 € Eigenanteil (03:05), Öl 3.000 €/WP 2.500 € (03:47), Lüfter-Heizkörper (04:15) | https://www.youtube.com/watch?v=YM__P4KLptI | 09.11.2026 |
| Q35 | YouTube Heizungsmacher: „Öltank Demontage“, 3:09 — Restöl pumpen (01:16), zerschneiden (01:33), Tankraum wird Kellerraum (02:25) | https://www.youtube.com/watch?v=_VWgfktt8b0 | 09.11.2026 |
| Q36 | YouTube schlau energiesparen: „Wärmepumpe ohne Fußbodenheizung im Altbau“, 14:56 — 35 °C ohne Neubau (00:00), Leistungsverlust bei niedriger Temperatur (08:05) | https://www.youtube.com/watch?v=AeUmuCiPcXI | 09.11.2026 |
| Q37 | YouTube „Mission Erneuerbar“: „Wärmepumpe EINFACH selber einbauen“, 28:16 — Kernbohrung (06:57), Gas-Rückbau vom Profi (10:02), ~7.000 € Material (25:51), Förderung nachträglich = Problem (26:19) | https://www.youtube.com/watch?v=HlEKW_MYBJQ | 09.11.2026 |
| Q38 | BauNetz Wissen: Berechnung der Heizlast (DIN EN 12831, Φ_HL = ΣΦ_T + ΣΦ_V + ΣΦ_RH, U-Werte DIN EN ISO 6946, Erdreich DIN EN ISO 13370, Wärmebrücken DIN V 18599-2; 100 W/m² als Überdimensionierungs-Fehler) | https://www.baunetzwissen.de/heizung/fachwissen/waermebedarf/berechnung-der-heizlast-161074 | 09.11.2026 |
| Q39 | IKZ: „Die Dimensionierung von Pufferspeichern“ (Mindestvolumenstrom, Abtauung, 10 / 8 / bis 5 % des stündlichen Heizwasserdurchsatzes, 30 l/kW, Reihen- vs. Parallelpuffer) | https://www.ikz.de/detail/news/detail/die-dimensionierung-von-pufferspeichern/ | 09.10.2026 |
| Q40 | IKZ: „Parallele oder serielle Einbindung?“ (Puffer im Rücklauf, Pufferbypass, 1 % Gasmehrverbrauch ≈ 450 €/a gegen 380 €/a Pumpenstrom) | https://www.ikz.de/detail/news/detail/parallele-oder-serielle-einbindung/ | 22.12.2016 |
| Q41 | SBZ: „Was bringen die neuen Kältemittel?“ (Füllmenge ≈ 2 kg, neue chemische Kältemittel GWP 150–700, Zündquellenfreiheit, Brennbarkeit) | https://www.sbz-online.de/heizung/waermepumpen-neu-denken-was-bringen-die-neuen-kaeltemittel | 01.12.2021 |
| Q42 | EU-Kommission: F-Gas Regulation (EU) 2024/573, angenommen 07.02.2024, anwendbar seit 11.03.2024 | https://climate.ec.europa.eu/areas-action/fluorinated-greenhouse-gases/f-gas-legislation_en | 09.11.2026 |
| Q43 | BauNetz Wissen: Leitfaden Schall des bwp (24 Seiten; Schallleistungs- und Schalldruckpegel, Abtaugeräusche, Entkopplung, Körperschall über Rohr-/Elektroleitungen) | https://www.baunetzwissen.de/heizung/tipps/planungshilfen/leitfaden-schall-4685992 | 09.11.2026 |
| Q44 | BauNetz Wissen: Schutz gegen Lärm aus gebäudetechnischen Anlagen (Gehäuse senkt Luftschall, Dämpfer/Fundament gegen Körperschall, keine vollständige Trennung) | https://www.baunetzwissen.de/bauphysik/fachwissen/schallschutz/schutz-gegen-laerm-aus-gebaeudetechnischen-anlagen-4408801 | 09.11.2026 |
| Q45 | Elektropraktiker: SteuVE ab 01.01.2024 (alle Wärmepumpen > 4,2 kW, Steuerung über Smart Meter Gateway, keine Ablehnung wegen Netzüberlastung) | https://www.elektropraktiker.de/nachrichten/nachricht/waermepumpen-co-muessen-ab-januar-2024-aus-dem-netz-steuerbar-sein | 20.12.2023 |
| Q46 | Verbraucherzentrale: Heizung optimieren (≈ 6 % Heizenergie je Grad, 16-°C-Untergrenze) | https://www.verbraucherzentrale.de/wissen/energie/heizen-und-warmwasser/heizung-optimieren-und-heizkosten-sparen-so-gehts-30096 | Stand 08.10.2026 |

**Quellenprüfung:** 49 Quellen, 63 einzelne URLs. Die 2026 ergänzten Fachportal-Quellen **Q38–Q46** wurden am 09.11.2026 einzeln mit Browser-Headern per GET abgerufen (alle HTTP 200, Titel gegengeprüft); die übrigen stammen aus dem Lauf vom 09.11.2026 ohne 404.

---

## 12. Unbelegt / offen

1. **GWP von R290 (Propan).** Die ESanMV nennt R290 und R600a als natürliche Kältemittel `[Q14]`, die Buderus-Tabelle enthält sie nicht `[Q32]`. Die verbreitete Zahl „GWP 3“ ist hier **nicht** belegt.
2. **Puffervolumen je kW als alleiniges Kriterium.** Der Praxisrichtwert **30 l/kW** ist jetzt belegt [Q39]; dieselbe Quelle sagt aber, dass er bei leistungsgeregelten Geräten nicht mehr ausreicht, weil der **Mindestvolumenstrom des konkreten Geräts** die Größe bestimmt. Diese Gerätedatenblätter wurden hier nicht geprüft — die Zahl kommt aus dem Angebot, nicht aus diesem Playbook. Die Videoaussage „viel Puffer = lange Laufzeit“ bleibt ein Zitat `[Q34]`, keine Auslegungsnorm.
3. **Mindestabstand zur Nachbargrenze in Metern.** Es gibt keinen bundesweit festen Meterwert; die TA Lärm regelt Pegel, nicht Abstände `[Q19a]`. Kommunale Merkblätter nennen unterschiedliche Werte — nicht geprüft.
4. **Kosten für Kernbohrung, Fundament, Elektroanschluss als Einzelposition.** In den herangezogenen Quellen nur im Gesamtpreis enthalten `[Q22][Q34]`; keine belastbare Einzelbandbreite.
5. **Behandlung von Erfüllungserklärungen aus der GEG-2024-Zeit** (65-%-Auflage in Altbescheiden). Das GModG regelt das nicht ausdrücklich `[Q01]`.
6. **Wärmepumpen-Stromtarif.** Es wurde mit dem Haushaltsstrompreis gerechnet `[Q29]`; ein belegter durchschnittlicher WP-Tarif lag nicht vor.
7. **Solarthermie-Investitionskosten** im Bestand: keine geprüfte Zahl in dieser Recherche.
8. **„Wärmeplanung“ als kommunale Pflicht.** Sie ist aus dem GModG entfernt `[Q01]`; ob Landesgesetze (z. B. Wärmeplanungsgesetze der Länder) eigenständige Fristen setzen, wurde nicht geprüft.
9. **Langfristige Ölpreisprognose.** Die Sensitivitätsrechnung nutzt nur belegte Tagespreise `[Q28]`; jede Prognose wäre Spekulation.
10. **Erfahrungswerte für Eigenleistungs-Stunden** (Graben, Dämmung) — bewusst weggelassen, weil keine Quelle.
11. **Feld-Jahresarbeitszahl 3,4** (Luft-Wasser) stammt aus dem Video-Gegencheck und hat in dieser Recherche keine eigene Quelle; belegt ist nur die Spanne 3–4 `[Q18]`. Die Rechenbeispiele in §6 arbeiten deshalb weiter mit 3,0.
12. **Modulationsgrenzen einzelner Geräte** (VWL 75/6 ≈ 4,6 kW, Stiebel 07.2 Plus ≈ 3 kW) sind Herstellerangaben aus dem Video-Gegencheck, nicht aus einem geprüften Datenblatt.

---

*Verwandte Playbooks: `heizung-lueftung.md` (Heizkörper, Vorlauf, Hydraulik), `elektro.md` (Zählerplatz, Leitungen), `daemmung.md` (Hüllfläche vor Heizungstausch), `kosten-bauzeit.md` (Angebotsvergleich, Nachträge), `entkernen-entsorgung.md` (Rückbau, Entsorgung).*
