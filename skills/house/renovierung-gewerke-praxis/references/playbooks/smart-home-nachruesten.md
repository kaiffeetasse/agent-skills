# Smart Home im Bestand nachrüsten — Funk oder Bus, Vorbereitung, Kosten, Datensicherheit

> **Preisstand 09/2026.** Alle Preise sind Orientierungswerte inkl. MwSt. aus den genannten Quellen —
> regional verschieden, keine Angebote. Wer später damit rechnet, prüft sie neu.

## Kurzantwort

- **Funk zuerst, wenn du nicht sanierst**: Homematic IP, Zigbee, Matter — Batterie, keine Leitungen, aber
  Herstellerbindung und Cloud-Zwang prüfen. **Bus (KNX) nur bei Elektrosanierung**, weil die Leitung in die
  Wand muss.
- **Was sich wirklich lohnt**: Heizungsthermostate (2–8 % Ersparnis, belegt), Rauchmelder, Rollos, Licht.
  Reine Komfort- und Alarmtechnik spart nichts.
- **Vorbereitung ist billiger als Nachrüsten**: tiefe Dosen, Leerrohre, Busleitung, Nische für die Zentrale —
  alles, was beim Elektro-Neuaufbau eh offen ist.
- **Sicherheit**: keine Portfreigaben, kein Standardpasswort, lokale Steuerung bevorzugen; Fernzugriff über VPN.


**Zielgruppe:** technisch interessierter Eigenheimbesitzer (Home Assistant), Bestand typisch 1960–2005, kein Neubau.
**Stand:** 09.11.2026. Alle Preise sind Orientierungswerte inkl. MwSt., kein Angebot. Jede Zahlenaussage trägt eine Quellennummer [Q#]; die Quellen stehen mit URL, Typ und Prüftiefe in §9. Eigene Rechnungen sind als **Rechnung** gekennzeichnet, Schätzungen als **Schätzung**.

> **Die eine Grenze, die alles andere bestimmt:** 230-V-Arbeiten hinter der Hausanschlusssicherung darf nur ein eingetragenes Installationsunternehmen ausführen (NAV § 13 Abs. 2), auch im eigenen Haus. Smart Home ändert daran nichts. Was du selbst machen darfst, ist Vorbereitung: Dosen, Schlitze, Leerrohre, Kabel nach Vorgabe, Fotos — Details im Schwester-Playbook `elektro.md`.

---

## 1. In 60 Sekunden

1. **Funk ist die Nachrüstlösung, Bus die Neubaulösung.** Funk kostet „mehrere hundert Euro" als Einstieg, Kabel „mehrere Tausend Euro" — und Kabel lohnt nur bei ohnehin anstehender Renovierung [Q22].
2. **Für ein Bestandshaus ohne Elektrosanierung ist Funk richtig.** 868 MHz (Homematic IP) kommt durch Wände besser als 2,4 GHz (WLAN, Zigbee, Thread) — je höher die Frequenz, desto stärker die Dämpfung [Q13][Q14].
3. **Der größte Fehler ist, mit Geräten anzufangen statt mit dem Verteiler.** Ohne Platz, ohne Neutralleiter in der Dose, ohne PE bleibt jeder Aktor ein Provisorium.
4. **Rollos, Licht und Heizung sind die drei Funktionen mit echtem Nutzen.** Heizungsabsenkung spart belegt 2–8 % Heizkosten [Q22]; „Komfort und Sicherheit" erhöhen dagegen den Stromverbrauch [Q22].
5. **Cloud ist Standard, lokal ist Fleißarbeit.** Bei Shelly ist die Cloud nach dem Einrichten **aktiv** und muss manuell abgeschaltet werden [Q31]; Philips Hue hat die Kontopflicht angekündigt [Q18].

---

## 2. Funk vs. Bus — was man vor der Systemwahl wissen muss

### 2.1 Die Systeme im Vergleich

| System | Medium / Frequenz | Reichweite (Herstellerangabe) | Energie | Störfestigkeit | Herstellerbindung | Cloud |
|---|---|---|---|---|---|---|
| **KNX TP** | 2-Draht-Bus, 30 V DC, 9,6 kbit/s [Q1] | 1.000 m Leitung je Linie, 350 m bis zur Spannungsversorgung, 700 m zwischen Teilnehmern [Q1]; andere Fachquelle nennt 700 m Linie / 300 m zum fernsten Gerät [Q3] | Bus-versorgt, keine Batterien | sehr hoch: verdrillt, geschirmt, keine Funkstörer [Q22] | offener Standard, > 400 Hersteller, aber **eine** Engineering-Software (ETS) [Q1] | keine Cloud nötig; Fernzugriff über IP-Gateway |
| **KNX RF** | 868 MHz [Q1] | Herstellerangabe, nicht geprüft | Batterie oder Netz | wie Funk | KNX-zertifiziert | keine Cloud nötig |
| **Homematic IP** | 868,0–868,6 / 869,4–869,65 MHz [Q8] | 400 m Freifeld (Access Point), 250 m (Thermostat), 200 m (Rauchmelder) [Q8][Q9][Q10] | 2 Jahre (Thermostat), 10 Jahre (Rauchmelder) [Q9][Q10] | gut (Sub-GHz), aber jede Wand dämpft [Q13] | eine Marke (eQ-3), dafür own ecosystem | Access Point: kostenlose Cloud; CCU3: lokal [Q9] |
| **Zigbee** | 2,4 GHz, Mesh [Q14] | „bis 100 m im Innenbereich, 300 m Sichtlinie" [Q14] | Batterie (Sensoren > 2 Jahre) [Q11] | mittel: 2,4-GHz-Band ist geteilt [Q14] | Standard, aber Geräte-Praxis oft herstellerspezifisch | Hub nötig (z. B. Aqara), App/Konto |
| **Z-Wave** | Sub-GHz-Funk (EU), Mesh [Q15] | „bis 300 m" Freifeld (Herstellermarketing) [Q15] | Batterie oder Netz | gut (Sub-GHz), S2-Verschlüsselung [Q15] | Standard mit Zertifizierung, breite Gateway-Auswahl [Q15] | Gateway-abhängig |
| **WLAN (Shelly & Co.)** | 2,4 GHz, 802.11 b/g/n [Q5] | hausübliche WLAN-Abdeckung | **nur Netzbetrieb** (Aktor in der Dose) [Q5] | mittel: 2,4 GHz geteilt, kein Mesh | herstellerübergreifend über HTTP/MQTT, aber Cloud-App | Cloud optional, standardmäßig **an** [Q31] |
| **Matter / Thread** | Thread: 2,4 GHz Mesh, IPv6; Matter: Anwendungsschicht [Q16][Q17] | Thread-Mesh, Reichweite je Knoten wie 2,4 GHz | Batterie oder Netz | mittel (2,4 GHz) | **noch nicht** plug-and-play: Border Router nötig, Plattformen bauen eigene Thread-Netze [Q16][Q17] | lokal gedacht, Cloud je Plattform |

**Was die Tabelle nicht sagt, aber die Praxis:**

- **868 MHz ist der bessere Funk für den Bestand.** Höhere Frequenz wird stärker gedämpft; bei 868 MHz kostet eine Außenwand typisch 60 %, eine Decke 70 %, Stahlbeton 30–90 %, metallbedampftes Glas 40–90 %, Metallgewebe 100 % [Q13]. Das sind Schätzwerte aus der Praxis, keine Absolutwerte [Q13].
- **2,4 GHz teilen sich WLAN, Zigbee und Thread.** Dass daraus Störungen folgen, ist plausibel, aber in keiner der hier geprüften Quellen als Messung belegt → **Unbelegt** (§10).
- **Batterie ist ein Wartungsvertrag.** Ausnahme sind EnOcean-Geräte (Energy Harvesting); sonst müssen Batterien getauscht werden [Q22].
- **Mesh ist kein Ersatz für Planung.** Zigbee und Z-Wave leiten über netzversorgte Knoten weiter [Q14][Q15]; ein Funkaktor in der Dose ist damit auch Repeater — ein batteriebetriebener Sensor nicht.

### 2.2 Die drei ehrlichen Systementscheidungen

**A) „Ich will es einfach, sofort, ohne Wand."** → Homematic IP oder Shelly.
Homematic IP: 868 MHz, eigenes Ökosystem, Access Point mit kostenloser Cloud, alternativ CCU3 lokal [Q9]. Shelly: WLAN, lokale HTTP-API, MQTT, Skripte, Cloud abschaltbar [Q5][Q31]. Beides ist Nachrüstung, beides ist Herstellerbindung — bei Shelly schwächer, weil HTTP/MQTT offen sind.

**B) „Ich will es gemischt und selbst steuern."** → Funk-Sensoren + Home Assistant + lokale Zentrale.
Home Assistant kann Zigbee, Z-Wave, Thread, WLAN und Homematic bündeln; die Zentrale läuft lokal. Preis: Du bist dein eigener Administrator. Updates, Backups und Erreichbarkeit sind deine Aufgabe (BSI: keine Updates = Sicherheitsrisiko [Q19]).

**C) „Ich baue neu oder sanieren ohnehin."** → KNX.
KNX ist der einzige hier betrachtete Standard, der Bus, Herstellerunabhängigkeit und 30 Jahre Verfügbarkeit nachweisbar zusammenbringt: offener Standard, > 400 Hersteller, genormt über EN 50090 / ISO/IEC 14543-3 [Q1]. Nachteil: ETS-Software, Planung, Programmierer — und ein Preis, der an der Elektroinstallation hängt, nicht am Gerät.

---

## 3. Was im Bestand wirklich geht — Funktion, Preis, Aufwand

**Vorab:** „Aufwand" ist hier **Schätzung aus der Praxis**, keine Messung. Elektroarbeiten hinter der Dose muss der Fachbetrieb machen; die Stunden sind mit 70 €/h gerechnet (Band 55–85 €/h, siehe `elektro.md`).

| Funktion | Lösung im Bestand | Gerätepreis (geprüft 09.11.2026) | Aufwand | Ehrliche Grenze |
|---|---|---|---|---|
| **Licht schalten** | Shelly 1PM Gen3 hinter Schalter/Steckdose, 16 A, Leistungsmessung [Q5] | **14,90 €** [Q5] | 0,5–1 h je Punkt (Schätzung) | Neutralleiter in der Dose nötig; ohne N nur mit Speziallösung |
| **Licht dimmen** | Shelly Dimmer / dimmbare Leuchten | nicht geprüft | 0,5–1 h | Phasenabschnitt, Mindestlast, Brummgeräusche |
| **Rollladen** | Shelly 2PM Gen3 (2 Kanäle, Cover-Modus, Hinderniserkennung) [Q6] | **38,90 € / 2er-Pack** = 19,45 €/Stück [Q6] | 1–2 h je Rollladen | Motor muss vorhanden sein; Tasteranschluss, Laufzeit kalibrieren |
| **Heizung / Thermostat** | Homematic IP eTRV-B-2, M30×1,5, 2 Jahre Batterie [Q9] | **27,99 €** (Preisvergleich) [Q34] | 10 min je Heizkörper, selbst machbar | Kein Ersatz für hydraulischen Abgleich; Ventil muss M30 haben |
| **Rauchmelder** | Homematic IP HmIP-SWSD-2, Q-Label, 10 Jahre Batterie, 200 m Funk [Q10] | **55,34 €/Stück** (Preisvergleich) [Q33] | 10 min je Melder | Rauchmelderpflicht ist Landesbauordnung, nicht Smart Home; Vernetzung ist Zusatznutzen |
| **Türschloss** | Nuki Smart Lock Go/Pro, Montage innen, rückstandslos, für Mietwohnungen [Q29] | **139 €** (Go, Preisvergleich) [Q30] | 30–60 min, selbst machbar | VZ rät von Haustürsteuerung per Handy wegen Missbrauch bei Handyverlust ab [Q22] |
| **Kamera** | Ubiquiti G5 Bullet, 2K, PoE, lokal auf NVR [Q28] | **115 €** Kamera [Q28]; NVR zusätzlich, Preis je Modell nicht geprüft | 2–4 h je Kamera inkl. PoE | Außenkamera = DSGVO-Thema; Nachbar/öffentlicher Raum filmen ist unzulässig |
| **Energiezähler** | Shelly Pro 3EM, Hutschiene, 3-phasig, 45 Tage Daten, lokal/MQTT [Q7] | **273,90 €** [Q7] | 1–2 h durch Elektriker (Zählerkasten!) | Kein MID-Zähler für Abrechnung; Messtoleranz 1 % [Q7] |
| **Wasser / Heizung monitoren** | Funk-Wassersensor + Temperatursensor am Rohr | nicht geprüft | 15 min je Sensor | Batterie-Sensor meldet erst, wenn Wasser da ist — kein Schutz gegen Rohrbruch |
| **Fenster/Türkontakte** | Homematic/Aqara-Kontakte, für Heizungsabsenkung | nicht geprüft; Zigbee braucht einen Hub, z. B. Aqara M1S für **44,36 €** [Q12] | 15 min je Fenster | Nur sinnvoll, wenn die Heizung darauf reagiert |

**Wichtig zur Reihenfolge:** Erst Licht + Heizung (Nutzen sofort, Aufwand klein), dann Rollladen (Nutzen hoch, Aufwand mittel), dann Kamera/Schloss (Sicherheitsversprechen, Datenschutzrisiko), zuletzt Energiezähler (Messung ohne Automatisierung ist nur ein Dashboard).

---

## 4. Elektro-Vorbereitung — das Einzige, was man nicht nachrüsten kann

### 4.1 Die Leitungen und wo sie hingehen

| Leitung | Wohin | Wozu | Zahl |
|---|---|---|---|
| **KNX-Busleitung 2×2×0,8** (J-Y(ST)Y, grün, 7 mm) | von jeder Taster-/Schalterdose und jedem Präsenzmelder stern-/baumförmig zur Verteilung | Bus für Taster, Sensoren, Aktoren | **0,57 €/m**, 100-m-Ring 57,00 € [Q4] |
| **NYM-J 5×1,5** | zu jedem Rollladen, jeder Jalousie, jedem Fensterkontakt | 3 L + N + PE; Reserven für Kontakte | — |
| **NYM-J 3×1,5** | jede Lichtstelle, jede Steckdose | Standardstromkreis | — |
| **Cat.7 / Duplex-LWL** | je Raum 1–2, je Decke ein AP-Punkt, Kameras, Türstation | Netzwerk statt WLAN-Zwang; PoE für Kameras | — |
| **Leerrohr M25** | vom Verteiler in jeden Raum, auf den Dachboden, in die Garage, in den Garten | Nachziehen ohne Stemmen | — |

Zeilen ohne Zahl sind Planungsempfehlungen (Querschnitt, Rohrtyp, Cat-Klasse), keine Normzitate; die einzige bepreiste Position ist die Busleitung [Q4].

**KNX-Topologie, die man nicht verletzen darf:** max. **64 Geräte je Linie**, Gesamtlänge **1.000 m**, **350 m** bis zur Spannungsversorgung, **700 m** zwischen zwei Teilnehmern; Stern, Baum oder Linie erlaubt, **Ringleitung verboten** [Q1][Q32]. Eine zweite Fachquelle rechnet mit 700 m Linie und 300 m zum fernsten Gerät [Q3] — die Werte widersprechen sich, für die Planung gilt der kleinere Wert. Ein 640-mA-Netzteil trägt 64 Geräte bei 9 mA [Q3].

### 4.2 Nischen, Dosen, Verteiler

- **Tiefe Dosen (≥ 60 mm)** statt 45 mm: Busankoppler und Aktoren brauchen Platz. ⚠️ Eigene Empfehlung, keine geprüfte Normzahl.
- **Nische / Technikschrank** für die Verteilung: KNX-Aktoren sitzen auf Hutschiene, nicht in der Wand. Ein 3-reihiger Verteiler mit 12 TE je Reihe ist das Minimum für ein Einfamilienhaus; 20 % Reserve einplanen (Detail in `elektro.md`).
- **Kein Aktor in die gedämmte Fensterlaibung.** Siehe 4.4.
- **Leerrohr-Endpunkt dokumentieren:** Jedes Rohr, das irgendwo endet, wird mit Foto und Maß beschriftet. Ohne das ist es später ein Blindrohr.

### 4.3 Zehn Regeln für den Elektro-Neubau (wenn man schon offen hat)

1. **Busleitung in jede Schalterdose** — auch wenn heute Funk geplant ist. Kostet 0,57 €/m [Q4], spart später die Wand.
2. **5-adrig zu jedem Fenster** — Rollladen, Kontakt, Reserve.
3. **Cat.7 in jeden Raum und an jede Decke** — WLAN deckt Bestand, aber nicht 4K-Kamera und AP-Backhaul.
4. **Leerrohr vom Verteiler ins Dach, in die Garage, in den Garten** — PV, Wallbox, Bewässerung, Kamera.
5. **Tiefe Dosen und ein 3-reihiger Verteiler mit 20 % Reserve.**
6. **Neutralleiter in jede Schalterdose** — sonst kein Shelly, kein Dimmer, kein Präsenzmelder.
7. **Rollladenaktor im Verteiler, nicht im Rollladenkasten** — Wartbarkeit und Funkreichweite.
8. **Taster statt Schalter** — Smart Home braucht Taster (impuls), nicht Rastschalter.
9. **Alles auf Hutschiene, was Hutschiene kann** — Aktoren, Netzteil, Gateway, Switch.
10. **ETS-Projekt, Stromlaufplan, Fotos und Passwörter dem Bauherrn übergeben** — sonst gehört das Haus dem Integrator.

### 4.4 Warum Funk-Rollos in der Dämmung Probleme machen

Ein Funkaktor im Rollladenkasten sitzt bauartbedingt **außerhalb der Innenwand**, hinter dem Rollladenpanzer und oft in der Dämmebene. Jede Wand dämpft das Signal: Außenwand 60 %, Decke 70 %, Stahlbeton 30–90 %, metallbedampftes Glas 40–90 %, Metallgewebe 100 % [Q13]. Ein heruntergefahrener Panzer aus Alu oder Stahl kommt hinzu. Folge: Der Aktor ist im Mesh schlecht erreichbar, Befehle kommen verzögert oder gar nicht, und die Batterie (bei batteriebetriebenen Funktastern) hält kürzer, weil mehr gesendet wird.

**Was hilft:** Aktor in die Dose **innen** legen (Kabel zum Motor durchführen), Funkgateway zentral statt in der Garage, bei 868 MHz bleiben, Reichweite mit einem zweiten Access Point als eigener Funkzelle erweitern [Q8]. ⚠️ Die Dämmung selbst taucht in der Dämpfungstabelle nicht auf; die Aussage „Dämmung dämpft" ist eine Schlussfolgerung aus Wand-/Metallwerten, kein Messwert [Q13].

---

## 5. Datensicherheit — lokal, aktualisiert, nicht von außen erreichbar

### 5.1 Lokal vs. Cloud

- **Shelly:** Cloud ist nach dem Einrichten **aktiv** und muss in der App manuell deaktiviert werden; danach ist das Gerät per IP im LAN erreichbar, in der Cloud aber „offline" [Q31]. Zugleich ist der lokale Access Point **standardmäßig offen** (kein Passwort) — ein offenes WLAN namens „Shelly…" [Q31]. Wer das nicht abschaltet, betreibt einen unverschlüsselten Zugangspunkt.
- **Homematic IP:** Access Point mit kostenloser Cloud, alternativ CCU3 mit lokaler WebUI [Q9]. Wer ohne Cloud will, braucht die CCU3.
- **Philips Hue:** Wer die App nutzen will, muss laut Ankündigung des Betreibers ein Konto anlegen; die Daten gehen an die Signify-Cloud und können laut Datenschutzbestimmungen an Dritte weitergegeben werden [Q18]. Das ist der belegte Fall angekündigter Kontopflicht im Konsumentenmarkt.
- **Aqara:** Geräte brauchen einen Hub, 2,4-GHz-WLAN, App; lokale Automatisierungen sind möglich; Matter-Unterstützung nennt der Hersteller als OTA-Update, der Stand der Seite ist unklar [Q11].

**Regel:** Wer lokal steuert, verliert nicht die Funktion, sondern nur den Fernzugriff. Wer Cloud will, sollte wissen, welche Daten das Haus verlässt: Video, Anwesenheit, Verbrauch, Türöffnungen lassen Rückschlüsse auf Lebensgewohnheiten zu [Q22][Q23].

### 5.2 Updates

BSI: Vor dem Kauf prüfen, ob der Hersteller Updates über die erwartete Nutzungsdauer liefert; automatische Updates aktivieren; **Geräte ohne Updates sind ein Sicherheitsrisiko und gehören ausgetauscht** [Q19]. In der Praxis heißt das: ein 10 Jahre alter WLAN-Aktor ohne Update ist ein offener Linux-Rechner im Netz.

### 5.3 Zugang von außen

- **Router-Fernzugang deaktivieren**, nicht benötigte Dienste abschalten, Gastnetz für unsichere Geräte [Q20].
- **VPN statt Portfreigabe:** Ein VPN baut einen verschlüsselten Tunnel zum Heimnetz; damit lassen sich schutzwürdige Daten von jedem Ort mit dem lokalen Netz austauschen, ohne den Dienst selbst ins Internet zu stellen [Q21].
- ⚠️ BSI sagt in den geprüften Seiten „Fernzugang deaktivieren" und „VPN nutzen"; das explizite Verbot von Portfreigaben steht dort nicht. Die Empfehlung „keine Portfreigabe" ist die logische Folge, kein wörtliches Zitat.

### 5.4 Die fünf typischen Fehler

1. **Standardpasswort** am Router oder Gerät — BSI nennt „admin"/„1234" ausdrücklich als Angreiferwissen [Q20].
2. **Cloud aktiv gelassen**, obwohl lokal gesteuert wird [Q31].
3. **Offener Access Point** des Aktors nicht abgeschaltet [Q31].
4. **Alles in einem Netz**: Kamera, Türschloss und PC im selben VLAN; BSI empfiehlt Trennung über Gastnetz [Q20].
5. **Keine Updates, kein Backup** der Hausautomation — bei Home Assistant ist der Verlust der Config der eigentliche Ausfall.

---

## 6. Kosten — drei Pakete, nachgerechnet

**Vorab:** Es gibt keine amtliche Preisstatistik. Gerätepreise sind Herstellershop- oder Preisvergleichspreise vom 09.11.2026; Lohn ist mit 70 €/h gerechnet (Band 55–85 €/h). Alle Summen sind **Rechnung**, keine Angebote.

### 6.1 Einsteiger (3 Zimmer, Funk, ohne Elektrosanierung)

| Position | Menge | Einzel | Summe |
|---|---|---|---|
| Shelly 1PM Gen3 (Licht) [Q5] | 6 | 14,90 € | 89,40 € |
| Heizkörperthermostat eTRV-B-2 [Q34] | 3 | 27,99 € | 83,97 € |
| Rauchmelder HmIP-SWSD-2 [Q33] | 2 | 55,34 € | 110,68 € |
| **Geräte** | | | **284,05 €** |
| Elektriker 6 h (Aktoren setzen) | 6 | 70 € | 420,00 € |
| **Gesamt** | | | **≈ 700 €** |

### 6.2 Mittelklasse (EFH 140 m², Funk, mit Netzwerk)

| Position | Menge | Einzel | Summe |
|---|---|---|---|
| Shelly 1PM Gen3 [Q5] | 12 | 14,90 € | 178,80 € |
| Shelly 2PM Gen3, 2er-Pack [Q6] | 3 Pakete | 38,90 € | 116,70 € |
| Heizkörperthermostat eTRV-B-2 [Q34] | 8 | 27,99 € | 223,92 € |
| Rauchmelder HmIP-SWSD-2 [Q33] | 8 | 55,34 € | 442,72 € |
| Nuki Smart Lock Go [Q30] | 1 | 139,00 € | 139,00 € |
| Ubiquiti G5 Bullet [Q28] | 2 | 115,00 € | 230,00 € |
| Shelly Pro 3EM [Q7] | 1 | 273,90 € | 273,90 € |
| **Geräte** | | | **1.605,04 €** |
| Elektriker 20 h | 20 | 70 € | 1.400,00 € |
| **Gesamt** | | | **≈ 3.000 €** |

Nicht enthalten: NVR für die Kameras (Preis je Modell nicht geprüft), Netzwerkkabel, Patchpanel, Steckdosen.

### 6.3 KNX-Vollausbau

- **60–150 €/m²** Wohnfläche für die KNX-Automation, bei 200 m² also **10.000–25.000 €** [Q26].
- Ein Praxisbeispiel mit 250 m² nennt **130.000 €** für die **komplette Elektroinstallation inkl. KNX** = **155 €/m²** [Q27]. Das ist nicht der Aufpreis für KNX, sondern der Preis der ganzen Elektrik — die Zahl wird oft falsch zitiert.
- Ein zweites Beispiel nennt 260 €/m² mit viel Eigenleistung und gehobener Ausstattung [Q27]; ein drittes 357 €/m² bei 1 Mio. € Bausumme [Q27]. Die Spanne ist so groß, dass nur ein Angebot hilft.
- **Je Raum** (8 Räume, 140 m²): **1.050–2.600 €/Raum** (Rechnung aus 60–150 €/m²).

**Der ehrliche Vergleich:** Funk-Mittelklasse kostet ~3.000 € für ein ganzes Haus, KNX beginnt bei ~8.400 € für 140 m² und endet offen. Dafür kann KNX bei Auszug bleiben, funkende Geräte wandern mit oder in den Elektroschrott.

---

## 7. Wann Smart Home Unsinn ist

### 7.1 Mietwohnung

Funk ist hier tatsächlich die richtige Wahl: „Sie bieten sich auch in Mietwohnungen an, da sie problemlos wieder demontiert werden und Umzüge mitmachen können" [Q22]. Nuki wirbt ausdrücklich mit Montage ohne Bohren und rückstandsloser Entfernung [Q29]. **Aber:** 230-V-Einbau (Shelly hinter dem Schalter) ist eine Änderung der Elektroanlage und braucht die Zustimmung des Vermieters; beim Auszug muss sie zurückgebaut werden. Für Mietwohnungen gilt deshalb: Steckdosen-Zwischenstecker, Thermostat aufschrauben, Schloss tauschen — nichts, was Kabel oder Dosen verändert.

### 7.2 Kein Nutzen

Der belegte Nutzen ist schmal: **2–8 % Heizkosteneinsparung** durch Absenkung bei Abwesenheit [Q22]. Alles andere ist Komfort oder Sicherheitsgefühl. Für Komfort und Sicherheit gilt laut Verbraucherzentrale das Gegenteil des Marketings: „Gerade auf Komfort und Sicherheit ausgelegte Smart-Home-Lösungen erhöhen den Stromverbrauch statt ihn zu senken" — gestützt auf eine Öko-Institut-Untersuchung im Auftrag der VZ NRW [Q22]. Wer nur „Licht per App statt per Schalter" will, kauft sich ein Batterie- und Cloud-Problem, keinen Mehrwert.

### 7.3 Förderung — die Vorgabe „gibt es nicht" ist falsch

Das war die Vorgabe, und sie hält der Prüfung nicht stand:

- **KfW** bewirbt Smart Home ausdrücklich als „staatlich gefördert", aber nur **im Rahmen** eines BEG-Kredits (261/262) oder des Produkts „Altersgerecht Umbauen" (159) — es gibt keine eigenständige Smart-Home-Förderung [Q24].
- **BAFA/BEG Einzelmaßnahmen** fördert unter „Efficiency Smart Home" konkret: Smart-Meter, MSR-Technik, elektronische Heizkörperthermostate, Fensterkontakte, Präsenzsensoren, Beleuchtungsaktoren, Jalousie-/Rollladenantriebe, Energiemanagementsysteme, notwendige Verkabelung inkl. **Leerrohre und Cat.7** [Q25].
- **Nicht förderfähig** sind reine Komfort- und Sicherheitsfunktionen; Einbruchmelde-/Gefahrenwarnanlagen nur über KfW 159 [Q25].
- **Satz widersprüchlich:** VZ NRW nennt „bis zu 20 Prozent der Kosten" [Q22], elektriker.org „bis zu 15 Prozent" [Q26]. Beides steht nebeneinander; maßgeblich ist die Förderrichtlinie zum Antragszeitpunkt, nicht der Ratgeber.

**Fazit:** Förderung gibt es — aber nur für die energetisch begründbaren Teile und nur im Förderverfahren, nicht für Licht, Schloss und Kamera. Wer wegen der Förderung saniert, saniert für die Förderung.

### 7.4 Die drei Fälle, in denen du es lassen solltest

1. **Elektrik ist alt (zweiadrig, kein PE, klassische Nullung).** Erst Elektro sanieren, dann smart machen. Ein Aktor an einer Nullung ist eine Gefahr, kein Fortschritt (Details `elektro.md`).
2. **Kein Koordinierungsaufwand gewünscht.** Funk braucht Batterien, Apps, Updates und ein Gateway; wer das nicht pflegen will, kauft sich eine teure Baustelle.
3. **Nur ein Gerät, nur ein Raum.** Ein einzelner smarter Zwischenstecker ist billiger als jedes System — und genauso nützlich.

---

## 8. Ablauf in sieben Schritten

| # | Schritt | Ergebnis |
|---|---|---|
| 1 | **Nutzenliste** schreiben: Was soll automatisch passieren? (nicht: welche Geräte) | 5–10 Szenen, priorisiert |
| 2 | **Elektro-Check**: PE vorhanden? Neutralleiter in der Dose? Platz im Verteiler? | Entscheidung Funk vs. Bus, Sanierungsbedarf |
| 3 | **Funksystem wählen** nach Frequenz, Cloud, Gateway-Lebensdauer | ein System, nicht fünf |
| 4 | **Gateway und Netzwerk** planen: zentrale Lage, LAN, VPN, VLAN/Gastnetz | erreichbares, getrenntes Netz |
| 5 | **Geräte in Stufen** kaufen: Licht + Heizung zuerst, dann Rollladen | lauffähige erste Stufe |
| 6 | **Lokal betreiben**: Cloud aus, Konten prüfen, Updates automatisch | Funktion ohne Internet |
| 7 | **Dokumentieren**: IP-Liste, Passwörter, Fotos, Config-Backup | Wiederherstellbarkeit |

---

## 9. Quellen

**Typ:** G = Gesetz/Verordnung/Norm, V = Verband/Behörde, H = Hersteller, F = Fachmedium/Fachbetrieb, P = Preisportal/Preisvergleich, C = Community, Y = Video.

| # | Quelle | Typ | Geprüft |
|---|---|---|---|
| Q1 | Wikipedia „KNX-Standard", https://de.wikipedia.org/wiki/KNX-Standard | C (Normauszug) | Volltext; 64 Geräte, 1.000/350/700 m, 9,6 kbit/s, 30 V, ETS, EN 50090 |
| Q2 | KNX Association, https://www.knx.org/de | V | Volltext; offener Standard, 180 Länder, ETS |
| Q3 | tgb-automation, „KNX-Liniensegment am 64-Geräte-Limit", https://tgb-automation.de/smarthome/knx-netzteil/knx-mehrere-linien-koppler | F | Volltext; 64 Geräte, 700 m Linie, 300 m zum fernsten Gerät, 9 mA |
| Q4 | HORNBACH, „EIB Busleitung J-Y(ST)-Y 2x2x0,8 grün 100 m", https://www.hornbach.de/p/eib-busleitung-j-yst-y-2x2-x-0-8-gruen-100-m/10358810 | H (Handel) | Preis 57,00 €/100 m, 0,57 €/m, Ø 7 mm |
| Q5 | Shelly, „Shelly 1PM Gen3", https://www.shelly.com/products/shelly-1pm-gen3 | H | Preis 14,90 €, WLAN 802.11 b/g/n, Einbau in Standarddose, lokal + Cloud |
| Q6 | Shelly, „Shelly 2PM Gen3 2-pack", https://www.shelly.com/products/shelly-2pm-gen3 | H | Preis 38,90 €/2er-Pack, Cover-Modus, Hinderniserkennung |
| Q7 | Shelly, „Shelly Pro 3EM", https://www.shelly.com/de/products/shelly-pro-3em-1 | H | Preis 273,90 €, Hutschiene, 3-phasig, 45 Tage Daten, 1 % Toleranz |
| Q8 | Homematic IP, „Access Point 2", https://homematic-ip.com/de/produkt/access-point-2 | H | 868 MHz, 400 m Freifeld, < 1 W |
| Q9 | Homematic IP, „Heizkörperthermostat basic", https://homematic-ip.com/de/produkt/heizkoerperthermostat-basic | H | 250 m, 2 Jahre Batterie, M30×1,5, Access Point **oder** CCU3 |
| Q10 | Homematic IP, „Rauchwarnmelder", https://homematic-ip.com/de/produkt/rauchwarnmelder | H | 200 m, 10 Jahre Batterie, > 85 dB, Access Point nötig |
| Q11 | Aqara, „Hub M1S Gen 2", https://www.aqara.com/de/product/hub-m1s-gen-2 | H | Zigbee 3.0, 128 Geräte, 2,4 GHz, lokale Automatisierungen, Matter per OTA |
| Q12 | Geizhals, „Aqara Hub M1S Gen2", https://geizhals.at/aqara-hub-m1s-gen2-hm1s-g02-a2767678.html | P | Preis 44,36 € |
| Q13 | ELV Journal, „Reichweitenverlängerung im Homematic IP System", — *ELV-Journal „Homematic IP Reichweite erhöhen“: HTTP 404 am 09.11.2026, Link entfernt; Reichweiten als Herstellerangabe markiert.* | H (Fachbeitrag) | Volltext; Dämpfungstabelle: Außenwand 60 %, Decke 70 %, Stahlbeton 30–90 %, Metallgewebe 100 % |
| Q14 | Wikipedia „ZigBee", https://de.wikipedia.org/wiki/Zigbee | C | Volltext; 2,4 GHz, Mesh, bis 100 m innen / 300 m Sichtlinie |
| Q15 | Aeotec, „What is Z-Wave?", https://aeotec.com/zwave/ | H | Volltext; Mesh, „bis 300 m", S2-Sicherheit, 868 MHz |
| Q16 | heise online, „Matter 1.4 …", https://www.heise.de/news/Matter-1-4-eint-konkurrierende-Funknetze-und-hilft-bei-der-Energiewende-10007636.html | F | Volltext; Border Router, konkurrierende Thread-Netze, HRAP, Multi-Admin |
| Q17 | matter-smarthome.de, „Geteilte Thread-Netzwerke …", https://matter-smarthome.de/entwicklung/geteilte-thread-netzwerke-jetzt-auch-mit-smartthings | F | Volltext; Thread 1.4 (Sept. 2024) Credential Sharing, vorher parallele Netze |
| Q18 | heise online, „Account-Pflicht bei Philips Hue", https://www.heise.de/news/Philips-Hue-Signify-zwingt-Nutzer-einen-Account-anzulegen-9316508.html | F | Volltext; Kontozwang, Cloud, Weitergabe an Dritte |
| Q19 | BSI, „Smarthome sicher einrichten", https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Internet-der-Dinge-Smart-leben/Smart-Home/smart-home_node.html | V (Behörde) | Volltext; Updates, Geräte ohne Updates austauschen, Standardpasswörter |
| Q20 | BSI, „Router und WLAN sicher einrichten", https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/Router-WLAN-VPN/router-wlan-vpn.html | V | Volltext; Fernzugang deaktivieren, Gastnetz, Standardpasswörter |
| Q21 | BSI, „Virtual Private Networks (VPN)", https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/Router-WLAN-VPN/Virtual-Private-Networks-VPN/virtual-private-networks-vpn.html | V | Volltext; verschlüsselter Tunnel, sicherer Zugriff aufs lokale Netz |
| Q22 | Verbraucherzentrale, „Smart Home – Das intelligente Zuhause", Stand 24.02.2026, https://www.verbraucherzentrale.de/wissen/umwelt-haushalt/wohnen/smart-home-das-intelligente-zuhause-6882 | V | Volltext; 2–8 % Heizkosten, „mehrere hundert Euro" vs. „mehrere Tausend", Störanfälligkeit, Cloud, Handy-Türsteuerung, Förderung bis 20 % |
| Q23 | Verbraucherzentrale Bayern, „Smart Home: Mehr Komfort, neue Risiken", 30.10.2024, https://verbraucherzentrale.bayern/pressemitteilungen/smart-home-mehr-komfort-neue-risiken-100678 | V | Volltext; Datenarten, Router als Schwachstelle, starke Passwörter |
| Q24 | KfW, „Smart Home … staatlich gefördert", https://www.kfw.de/inlandsfoerderung/Privatpersonen/Bestandsimmobilie/Smart-Home/ | V (Bank) | Volltext; Förderung nur über BEG-Kredit 261/262 oder 159 |
| Q25 | BAFA, „BEG Infoblatt förderfähige Maßnahmen", PDF, https://www.bafa.de/SharedDocs/Downloads/DE/Energie/beg_infoblatt_foerderfaehige_kosten.pdf?__blob=publicationFile&v=25 | V (Behörde) | Volltext; Nr. 3.5 „Efficiency Smart Home", Liste; Nr. 9.4 Alarmtechnik nur KfW 159 |
| Q26 | elektriker.org, „KNX-Kosten", 30.10.2026, https://www.elektriker.org/magazin/knx-kosten-202617371 | F | Volltext; 60–150 €/m², 10.000–25.000 €/200 m², Förderung 15 % |
| Q27 | smarthome-exklusiv, „Was kostet ein Smart Home?", https://smarthome-exklusiv.de/blog-wissen/was-kostet-ein-smart-home/ | F | Volltext; 155 €/m², 260 €/m², 357 €/m² (jeweils Elektro + Smart Home) |
| Q28 | Ubiquiti Store Europe, „G5 Bullet", https://eu.store.ui.com/eu/en/products/uvc-g5-bullet | H | Preis 115,00 €, 2K, PoE |
| Q29 | Nuki, „Smart Lock Pro (5. Gen.)", https://nuki.io/de-de/produkte/smart-lock-pro-5-gen/ | H | Volltext; Montage innen, rückstandslos, Mietwohnung, E2E-Verschlüsselung |
| Q30 | Geizhals, „Nuki Smart Lock Go weiß", https://geizhals.de/nuki-smart-lock-go-weiss-a3444702.html | P | Preis ab 139,00 € |
| Q31 | Draeger-IT, „Shelly ohne Cloud nutzen – lokal & sicher", https://www.youtube.com/watch?v=TeNLKiBsqTQ (06.01.2026, 9:23) | Y | Untertitel geladen; 01:50–02:03 Cloud standardmäßig aktiv; 02:35–02:53 lokal per IP; 03:51–04:04 offener Access Point |
| Q32 | KNX-User-Forum, „TP-64 vs. TP-256 Geräte", https://knx-user-forum.de/forum/%C3%B6ffentlicher-bereich/knx-eib-forum/902401-tp-64-vs-tp-256-ger%C3%A4te | C | Thread gelesen; 64 Geräte/TP-64, 1.000 m Linie, KNX Association im Thread |
| Q33 | idealo, „Homematic IP HmIP-SWSD-2", https://www.idealo.de/preisvergleich/OffersOfProduct/205946994_-hmip-swsd-2-homematic-ip.html | P | Preis ab 55,34 € |
| Q34 | idealo, „Homematic IP eTRV-B Heizkörperthermostat basic", https://www.idealo.de/preisvergleich/OffersOfProduct/6778192_-etrv-b-heizkoerperthermostat-basic-153412a0-homematic-ip.html | P | Preis ab 27,99 €, 51 Angebote |

**Anzahl geprüfter Quellen: 34** — 3 Community/Normauszug (Q1, Q14, Q32), 6 Verband/Behörde (Q2, Q19, Q20, Q21, Q22, Q23), 1 Bank (Q24), 1 Behörde BAFA (Q25), 12 Hersteller/Handel (Q4–Q11, Q13, Q15, Q28, Q29), 6 Fachmedium/Fachbetrieb (Q3, Q16, Q17, Q18, Q26, Q27), 4 Preisportal (Q12, Q30, Q33, Q34), 1 Video (Q31).

### Prüftiefe

- **Volltext gelesen und zitiert:** Q1–Q11, Q13–Q29, Q31, Q32.
- **Nur Preis/Existenz geprüft:** Q12, Q30, Q33, Q34.
- **Video-Zeitmarken** stammen aus automatischen Untertiteln (± 5 s), keine frame-genauen Angaben; Zitate können ASR-Fehler enthalten.
- **Nicht geprüft, nicht verwendet:** NVR-Preise, KNX-ETS-Lizenzpreise, Preise für Wassersensoren.

---

## 10. Unbelegt / offen

1. **„Funk-Rollos in der Dämmung funktionieren nicht."** So pauschal falsch. Belegt sind Dämpfungswerte für Außenwand (60 %), Decke (70 %), Stahlbeton (30–90 %) und Metall (100 %) [Q13]; die Dämmung selbst steht nicht in der Tabelle. Die Aussage ist eine begründete Schlussfolgerung, kein Messwert.
2. **Arbeitszeiten je Gerät** (0,5–1 h Licht, 1–2 h Rollladen, 2–4 h Kamera) — Erfahrungswerte, keine Quelle.
3. **„Portfreigaben sind unsicher."** BSI empfiehlt Fernzugang deaktivieren und VPN nutzen [Q20][Q21]; ein wörtliches Portfreigabe-Verbot steht dort nicht.
4. **Fördersatz 15 % vs. 20 %** — elektriker.org [Q26] und VZ NRW [Q22] widersprechen sich. Beide Zahlen stehen gelassen; die Richtlinie entscheidet.
5. **KNX-Leitungslänge 700 m/300 m vs. 1.000 m/350 m/700 m** — tgb-automation [Q3] und Wikipedia [Q1] widersprechen sich. Für die Planung gilt der kleinere Wert.
6. **„Smart Home spart Energie."** Nur für Heizungsabsenkung belegt (2–8 %) [Q22]; für Komfort/Sicherheit gilt das Gegenteil [Q22].
7. **2,4-GHz-Störungen durch WLAN/Zigbee/Thread** — plausibel, aber in den geprüften Quellen nicht als Messung belegt.
8. **Anzahl der Hersteller** — Wikipedia nennt „> 400" [Q1], KNX selbst nennt 180 Länder und 140.000 Installateure [Q2]; die Zahlen messen Verschiedenes und wurden nicht gegeneinander geprüft.

---

## 11. Die 10 Regeln (zum Mitnehmen)

1. **Erst Nutzen, dann Geräte.** Wer mit dem Aktor anfängt, kauft zweimal.
2. **Bestand ohne PE saniert zuerst die Elektrik** — nicht das Smart Home.
3. **Funk für den Bestand, Bus für den Neubau** — und Busleitung trotzdem in jede Dose legen, solange offen ist.
4. **868 MHz vor 2,4 GHz**, wenn Wände im Spiel sind.
5. **Kein Aktor in die gedämmte Laibung.** Kabel nach innen, Aktor in die Dose.
6. **Cloud nach dem Einrichten abschalten** und den offenen Access Point schließen [Q31].
7. **Updates und Hersteller-Lebensdauer sind Kaufkriterium**, nicht Feature-Liste [Q19].
8. **Fernzugriff nur per VPN**, Router-Fernzugang aus [Q20][Q21].
9. **Förderung nur für energetische Teile** — und nur, wenn die Sanierung ohnehin ansteht [Q25].
10. **Dokumentieren und Backup:** Fotos, IP-Liste, Passwörter, Config. Sonst gehört das Haus der App.
