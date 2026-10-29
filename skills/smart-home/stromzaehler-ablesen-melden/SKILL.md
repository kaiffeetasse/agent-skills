---
name: stromzaehler-ablesen-melden
description: "Zählerstand ablesen und beim Netzbetreiber melden."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [strom, zaehler, ablesung, tibber, messstelle]
    related_skills: [home-assistant, energy-price-history]
---

# Stromzähler ablesen, melden und gegenprüfen

## When to Use

- Der Nutzer schickt ein Foto des Stromzählers oder einen Ablesebrief des Netzbetreibers
  („Zählerstand ablesen und online melden“).
- Frage „was steht da“, „muss ich das melden“, „macht der Verbrauch Sinn“.
- Tibber Pulse meldet nichts / Batterie verdächtig.

## 1. Ablesen (mME, z. B. ISKRA MT175)

- Die große Zahl ist der **Gesamtbezug** (OBIS **1.8.0**, Symbol „+A“ mit Pfeil ins Netz).
  Beim MT175 steht sie **sechsstellig ohne Nachkommastelle mit führenden Nullen** —
  `010791` heißt **10.791 kWh**, nicht 1.079,1. Der Punkt in der Anzeige ist kein Dezimaltrennzeichen;
  ihn als Komma zu lesen ist der klassische Zehnfach-Fehler.
- Weiterschalten mit der optischen Taste (Sensorfläche kurz abdecken) oder der mechanischen Taste:
  `1.8.0` Gesamt → `1.8.1` HT → `1.8.2` NT → `2.8.0` Einspeisung → Momentanleistung in W.
- Die zweite Zeile (z. B. „2102 W“) ist **kein** Zählerstand, sondern die aktuelle Leistung.
- Gegenprobe vor dem Melden: der **letzte Stand** aus dem Portal/Brief. Ein Wert, der kleiner ist,
  kann nicht stimmen (Zählertausch ausgenommen, siehe unten).

## 2. Melden — beim Netzbetreiber, nicht beim Lieferanten

Der Netzbetreiber (Messstellenbetreiber) fragt jährlich ab und gibt die Werte an den Lieferanten
weiter; eine zweite Meldung an den Lieferanten ist freiwillig. Frist im Brief beachten
(typisch drei Wochen) — danach wird geschätzt.

Ablauf am Beispiel E-Werk Netze (Überlandwerk Mittelbaden):
1. **Der QR-Link im Brief kann kaputt sein.** `ablesung.ew-netze.de` liefert in diesem Fall
   `ERR_CERT_COMMON_NAME_INVALID` (Zertifikat auf `*.webspaceconfig.de`). Nicht wegklicken — über
   `https://www.ew-netze.de/ablesung` gehen, das leitet auf
   `https://webportal.uewm.de/kundenportal/gast/zaehlerstaende` weiter.
2. Login = **Zählernummer** (z. B. `1ISK…`) + **Ableseauftrag** aus dem roten Kasten des Briefes.
3. Das Eingabefeld akzeptiert **nur Ziffern** und setzt selbst Tausenderpunkte — Komma und Punkt
   werden geschluckt: `1079,1` getippt ergibt `10.791`. Also die Ziffernfolge ohne Trennzeichen
   eingeben und den formatierten Wert gegen die Anzeige prüfen.
4. Validierung: „Der minimal zulässige Wert lautet …“ → der Wert muss ≥ der letzten Ablesung sein.
   Kommt der Fehler, ist entweder die Zahl falsch gelesen oder der Zähler wurde getauscht.
5. Bild-Upload ist optional; der Schritt „E-Mail-Adresse für künftige Zustellung“ ist eine
   **Einwilligung** — ohne Rückfrage überspringen.
6. Bestätigung („Die Zählerstände wurden erfolgreich übermittelt“) als Screenshot sichern und dem
   Nutzer mitschicken.

**Zählertausch:** Stand springt auf 0, das Portal kennt aber noch den Endstand des alten Zählers und
lehnt jeden kleineren Wert ab. Dann nicht raten und nicht „aufrunden“ — Hotline des Netzbetreibers
anrufen und den Tausch melden.

## 3. Gegenprüfen, ob der Verbrauch plausibel ist

- Delta aus zwei Ablesungen gegen die Verbrauchshistorie des Lieferanten stellen (Tibber-App:
  Zählerstandshistorie; sonst Jahresverbrauch aus Rechnungen).
- Weicht es um Faktor 2–3 ab, ist meist **nicht** die Ablesung falsch, sondern: andere Messstelle,
  alter/neuer Zähler, geschätzter Wert des Lieferanten oder ein Pulse, der an einem anderen Zähler
  hängt. Das prüfen, bevor ein Wert „korrigiert“ wird.
- Rechenprobe: kWh-Delta / Tage = kWh/Tag; × 1000/24 = mittlere Wattzahl. Passt die Momentanleistung
  im Foto grob dazu, ist die Lesung konsistent.

## 4. Tibber Pulse (IR-Lesekopf)

**LED-Codes (Pulse, nicht Bridge):**
| LED | Bedeutung |
|---|---|
| 1× alle 10 s | normal, Batterie ok |
| 2×/s | sucht den Zähler (Sitz auf der IR-Schnittstelle prüfen) |
| 3× alle 10 s | keine Verbindung zur Bridge |
| 4× alle 10 s | keine Daten vom Zähler (Sitz, entsperrt, INF=Ein) |
| Dauerlicht | bereit zum Koppeln |
| keine LED | kein Strom → Batterien |

Kurzes weißes Aufblitzen beim Einlegen der Zellen ist normal und der beste Funktionstest.
Die **Bridge** ist das Steckdosenteil und meldet in **Farben** (grün/blau ok, rot/violett kein WLAN,
rot/gelb kein Tibber-Server) — ihre LED sagt nichts über die Pulse-Batterie.

**Batterietest mit Voltmeter (2× AA, Tibber empfiehlt Lithium):** jede Zelle einzeln im Leerlauf
(Lithium frisch 1,7–1,8 V, Alkaline 1,55–1,6 V), dann **unter Last** (100 Ω parallel): bricht sie
unter 1,2 V ein, ist sie hin — auch wenn sie leer 1,5 V zeigt. In Reihe zusammen ≥ 2,8 V.
Immer beide Zellen gleichzeitig und gleicher Typ.

**Keine LED trotz neuer Zellen:** Batterie-Lasche vollständig gezogen? Zellen gegenläufig eingelegt?
Kontakte korrodiert/federnd? Spannung **am Fach** messen — liegen dort ~3 V an, ist das Gerät defekt
→ Tibber-Support-Chat (Gerät wird getauscht).

## Pitfalls

- **Nie eine Portal-Ablesung erzwingen, die gegen die Physik spricht.** Lehnt das Portal einen Wert ab,
  erst Ziffernlesung, Zählertausch und Messstelle klären — nicht die nächsthöhere Zahl eintragen.
- **Zeigt Home Assistant für Tibber `unavailable` bzw. „restored“, sind die Monatswerte Schätzungen.**
  Nicht als Messwerte gegen den Zähler rechnen.
- **Die Vertragsbezeichnung im Portal ist kein Beweis für den Netztyp.** Ein Eintrag „AUSSPEISUNG“
  kann aus einem alten Vertrag stammen; maßgeblich ist, welches Zählwerk (1.8.0 vs. 2.8.0) das Portal
  abfragt.
