---
name: retro-console-tv-connection
description: "Use when connecting a retro console to a modern TV."
---

# Retro-Konsole an modernen TV / Monitor anschließen

Beantwortet „wie schließe ich die <Konsole> an meinen modernen Fernseher an?" — Kabel-Wahl,
Upscaler, Preisstufen und die Fallen, die man sonst erst live am Gerät entdeckt.

## When to Use

- „Wie schließe ich PS1 / PS2 / N64 / SNES / GameCube / Dreamcast / Xbox an meinen Smart-TV an?"
- „Welcher Adapter deckt Konsole A **und** B ab?"
- Kaufberatung Kabel / Konverter / Scaler für Retro-Hardware, TV-Einstellungen danach.
- Nicht nötig für Konsolen mit HDMI (PS3 Slim, PS4/PS5, Switch) — dort reicht ein HDMI-Kabel.

## Schritt 0 — Bestandsaufnahme (immer zuerst fragen)

1. **Modellnummer** vom Typenschild (z. B. PS1 `SCPH-9002`). Sie entscheidet über den Ausgang.
2. **Welche Buchsen hat der TV?**
   - nur HDMI → Wandler nötig (Standardfall)
   - 3,5-mm-Buchse „AV In" (manche Samsung/LG/Philips) → Composite reicht per Adapterkabel
   - SCART → bei aktuellen Geräten praktisch ausgestorben
3. **PAL/NTSC**: PAL-Geräte geben 50 Hz und 240p/288p aus — genau der Modus, den moderne
   Skalierer per Line-Doubling verarbeiten. TV-eigene Scaler können 240p meist **nicht**.

## Was welche Konsole ausgibt

| Konsole | Anschluss | Auflösungen | 480p/Progressive | Besonderheit |
|---|---|---|---|---|
| PS1 (SCPH-xxxx) | AV Multi Out (Composite **und** RGBs) | 240p/288p @ 50 Hz | nein — Hardware kann kein YPbPr | RGB ist sichtbar besser als Composite |
| PS2 (SCPH-xxxxx) | **derselbe** AV Multi Out | 240p (PS1-Discs) / 480i / 480p | nur über Component (YPbPr) oder RGB mit Sync-on-Green | DVD-Wiedergabe über RGB/SCART meist gesperrt (grünes Bild) |
| PS3 Fat | Multi Out + HDMI | — | — | HDMI direkt nutzen |
| PS3 Slim / PS4 / PS5 | HDMI | — | — | kein Wandler nötig |

→ **PS1 und PS2 haben denselben Stecker**, deshalb deckt ein Multi-Out-HDMI-Adapter beide ab.
Ein PS2/PS3-**Component**-Kabel funktioniert **nicht** an der PS1 (sie kann kein YPbPr).

## Lösungsstufen (Werte live prüfen; Stand 09/2026)

| Stufe | Lösung | Preis | Bild |
|---|---|---|---|
| 1 billig | Multi-AV → 3× Cinch-Kabel + Cinch→HDMI-Konverter mit Upscaler (USB-Strom, PAL/NTSC- und 4:3/16:9-Schalter) | ~15–25 € gesamt | weich, ~30–60 ms Lag |
| 2 Plug & Play | fertiger „PS1 & PS2 HDMI"-Adapter **mit RGB** (z. B. Kaico, Micro-USB-Strom) | 28–35 € | gut |
| 2b Referenz | RAD2X für PlayStation (RetroTINK) | ~65–70 € (Import) | sehr gut, **aber nur PS1-Auflösungen** (240p/480i) → kein PS2-480p |
| 3 Scaler | RetroTINK-2X-Mini/5X oder GBS-C + konsoleigenes Kabel | 130–200 € + Kabel | bestmöglich; einziger Weg zu PS2-480p (Component) und Referenz-RGB für PS1 |
| 4 Mod | HDMI-Mod (PS1Digital & Co., Löten) | ~150–200 € | top, aber invasiv |

**Kernaussage für „ein Adapter für beide":** Kein einzelnes Kabel gibt PS1 **und** PS2 in
Bestqualität. Beide laufen über einen Multi-Out-HDMI-Adapter (Stufe 2) mit 240p/480i problemlos;
PS2-480p und DVD brauchen den Component-Weg, also Stufe 3 mit zwei verschiedenen Kabeln.

Verifizierte Quellen, Preise und Produktdetails: `references/ps1-ps2-hdmi-options-2026-09.md`.

## Nach dem Anschließen (TV-Einstellungen)

1. Bildmodus **Spiel/Game** → deutlich weniger Input-Lag.
2. Format **4:3** erzwingen, sonst wird das Bild gestreckt.
3. Ton kommt über HDMI mit; Regelung im Spiel.
4. Bei schwarzem Bild der Reihe nach: Stromversorgung des Konverters → PAL/NTSC-Schalter an
   Billig-Boxen → anderes HDMI-Kabel → anderer TV-Eingang.

## Pitfalls

- **240p ist der Knackpunkt.** Ohne Wandler gibt der TV oft gar kein Bild; der TV-Scaler ist
  nicht die Lösung.
- **Composite (gelb/weiß/rot) ist billiger, aber matschig** — bei Retro immer RGB bevorzugen und
  im Produktnamen auf „RGB"/„True RGB" achten.
- Fertige Billig-HDMI-Kabel sind qualitativ ungleich: **LevelHike** wird in Tests als inkonsistent
  beschrieben, **Kaico** und **RAD2X** gelten als die verlässlichen.
- **Lightgun-Spiele** (Time Crisis, Duck Hunt …) laufen über LCD + Wandler **nicht** — die brauchen
  einen CRT. Vorher ansprechen, sonst ist die Enttäuschung vorprogrammiert.
- **PS2-DVDs** sind über RGB/SCART meist blockiert → nur Composite/Component.
- **PS2-Slim-Modelle** haben bei einigen PS1-Titeln reduzierte Kompatibilität; zum PS1-Zocken ist
  die Original-Konsole die sichere Wahl.
- Ein **Modchip** ändert am Anschluss nichts — er betrifft nur Import-/Sicherungskopien.
- Fehlt das Original-Kabel (z. B. Sony `SCPH-1052`), gebraucht für ein paar Euro nachkaufen statt
  inkompatibles Zubehör zu raten.

## Preis-Verifikation (echte Quellen, keine Schätzungen)

- **eBay.de-Suche** liefert EUR-Preise inkl. Versand serverseitig auslesbar (`web_extract` auf
  `https://www.ebay.de/sch/i.html?_nkw=<begriff>`); im Cache stehen Titel und „EUR x,xx" im selben
  Block → mit `grep -o -E '^.{0,200}'` filtern statt schätzen.
- **Amazon.de-Produktseiten** können in der Browser-Sitzung auf US-Lieferung stehen und dann nur
  USD / „cannot be dispatched to your selected delivery location" zeigen (`#corePrice_feature_div`
  und `.priceToPay` bleiben leer). Dann Amazon nur als Existenz-/Bewertungsnachweis nutzen
  (Titel, ASIN, Bewertungszahl) und den **EUR-Preis** von eBay.de oder einem deutschen Händler nehmen.
- Preise immer mit Stand-Datum nennen und als schwankend markieren.

## Gebrauchtkauf der Konsole (Kurzfassung)

Die vollständige Such-/Verhandlungsmaschinerie liegt in `kleinanzeigen-search` (user-owned) und
`kleinanzeigen-negotiation` (user-owned). Retro-spezifisch gilt zusätzlich:

- **Der Suchtreffer-Text ist abgeschnitten und verschweigt den Zustand.** Immer die Anzeigenseite
  lesen (`#viewad-description-text`): verifizierter Fall 09/2026 — ein 39-€-PS1-Set wirkte top,
  stand im Volltext aber als „wird ausdrücklich als defekt abgegeben" (Bastlerware).
- **Modellnummern kollidieren zwischen den Generationen.** `SCPH-3000x/5000x/7000x/9000x` gibt es
  bei PS1 **und** PS2 → die SCPH-Regex allein zieht PS2-Treffer ins PS1-Ergebnis. Zusätzlich im
  **Titel** auf `ps ?[2-5]|playstation ?[2-5]` prüfen und Zubehör-/Doku-Wörter ausschließen
  (Controller, Memory Card, Netzteil, Kabel, Bedienungsanleitung, Abschirmblech, Laser, Ersatzteil).
- **„Konsole" steht auch in Spiel-Anzeigen** („für die PlayStation 1 Konsole") → Konsolen-Filter
  auf den **Titel** legen, nicht auf die Beschreibung.
- **Retail-Anker fürs Preisgefühl:** generalüberholte PS1 mit Controller + Zubehör ~140 €
  (Konsolenkost.de, 09/2026), gewerblich getestet auf eBay ~58 € + ~25 € Versand; der
  Kleinanzeigen-Markt lag im Median bei ~70 € (n=272 Konsolen). Guter Deal = komplett und
  funktionsfähig ≤ 60 €.
- **Lokale Märkte können dünn sein:** im 60-km-Umkreis um die Suchstadt gab es gerade 3 PS1-Angebote
  (davon eines defekt, eines 180 € Sammler-OVP) → Versand-Deals mitprüfen statt nur Umkreis.
- **„Nur Abholung" ist der Ausschluss bei Ferne:** steht in der Anzeige `INDIVIDUAL_SHIPPING` mit
  leerer Optionsliste und „nur Abholung", gibt es keinen Plattform-Zahlungsweg → nicht anschreiben,
  sondern dem Nutzer als nicht handelbar melden.

## Related

- `kleinanzeigen-search` — Gebrauchtkauf der Konsole(n); die Anschlussfrage kommt oft direkt danach.
