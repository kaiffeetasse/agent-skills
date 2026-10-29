# PS1 / PS2 an HDMI — verifizierte Optionen (Stand 29.09.2026)

Alle Preise live gelesen, nicht aus dem Gedächtnis. Preise schwanken; vor einer Empfehlung erneut prüfen.

## Geprüfte Angebote (EUR, eBay.de)

| Produkt | Preis | Versand | Anmerkung |
|---|---|---|---|
| Kaico HDMI-Adapter Plug & Play für Sony PlayStation 1 & 2 (PS1/PS2) | 28,00 € | +6,19 €, 2–3 Tage | günstigster gefundener Original-Kaico |
| Kaico HDMI Adapter für PS1 PS2 Playstation 1 & 2 (Plug & Play) | 34,90 € | — | zweites Listing, gleiche Klasse |
| Kaico PS1 & PS2 HDMI Adapter mit **RGB Switch** (silber) | 69,48 € | +36,10 € | Import; nur nötig, wenn YPbPr gebraucht wird |
| „Retro PS1/PS2 HDMI Konverter – Plug & Play, 150 cm Kabel" | 24,95 € | — | No-Name-Alternative |
| AV zu HDMI Adapter (Cinch/RCA → HDMI) für PS1/PS2/PS3/Wii/Xbox/N64/GameCube | 7,99 € | — | nur der Composite-Wandler, Kabel fehlt |
| RCA auf HDMI Konverter 1080P (Composite → HDMI) | ~12–14 € | — | Klasse der Billig-Boxen mit PAL/NTSC-Schalter |

Amazon.de-Nachweis (EUR-Preis dort nicht lesbar, weil die Sitzung auf US-Lieferung stand):
**ASIN B083RY5NZH** — „Kaico PS1 & PS2 HDMI Adapter for PlayStation 1 and 2 with RGB Switch",
4,2★, ~1.590 Bewertungen. Produktbeschreibung nennt „RGB and YPbPr component modes".

Retail-Anker für gebrauchte Original-Hardware (nicht HDMI-relevant, aber Preisgefühl):
Konsolenkost.de verkauft „PS1 Konsole + Original Controller + Zubehör (generalüberholt)" für
139,99 €, mit 2 DualShock 189,99 €. eBay.de gewerblich: getestete PS1 ~58 € + ~25 € Versand.

## Recherche-Ergebnisse zu Kompatibilität und Grenzen

- **Multi-Out = gemeinsame Basis.** PS1 und PS2 nutzen denselben AV-Multi-Out; deshalb funktionieren
  „PS1 & PS2"-HDMI-Adapter an beiden (und an der PS3 Fat).
- **RAD2X für PlayStation** läuft laut Hersteller/Community auch an PS2 und PS3, ist aber auf die
  **PS1-Auflösungen (240p/480i)** begrenzt → kein PS2-480p-Progressive.
- **PS2-480p nur über Component (YPbPr) oder RGB mit Sync-on-Green.** Composite kann kein
  Progressive-Signal tragen. Component-Kabel für PS2/PS3 sind **nicht** PS1-tauglich.
- **PS2-DVD-Wiedergabe** ist über RGB/SCART in der Regel gesperrt (grünes Bild); nur
  Composite/Component geben DVDs wieder.
- **Kritik an der Billig-Klasse:** Ein Nutzerbericht zum Kaico nennt unscharfen Text/Menü bei
  PS2-Spielen; LevelHike wird in Vergleichen als inkonsistent bezeichnet. Für minimale Reibung ist
  RAD2X die verlässlichste Plug-&-Play-Wahl, für maximale Qualität ein Scaler (RetroTINK-2X-Mini/5X,
  GBS-C) mit konsoleigenem Kabel.
- **Lightgun-Spiele** brauchen einen CRT-Röhrenfernseher; über LCD + Wandler funktionieren sie nicht.

## Prüfpfad, der sich bewährt hat

1. `web_search` für die Produktklasse („PS1 HDMI adapter", „PS2 480p progressive component").
2. `web_extract` auf die **eBay.de-Suchseite** → Cache-Datei, dann mit `grep -o -E '^.{0,200}'` nach
   Titel-/Preiszeilen filtern (Titel und „EUR x,xx" stehen dort im selben Block).
3. Amazon.de nur für Produkt-/ASIN-/Bewertungsnachweis nutzen, wenn die Sitzung USD zeigt
   (`#corePrice_feature_div` / `.priceToPay` bleiben leer, `#availability` enthält
   „cannot be dispatched to your selected delivery location").

## Nicht verifizierte Behauptungen (nicht als Fakt weitergeben)

- Konkrete Amazon.de-EUR-Preise für den Kaico — von dieser Maschine nicht lesbar, weil die
  Amazon-Sitzung auf US-Lieferung stand. Wenn ein Preis genannt wird, live prüfen.
- Dass ein bestimmter Billig-Adapter PS2-480p könne: Die Stufe-2-Klasse (Kaico/LevelHike/Pound)
  gibt 480i/240p aus; 480p ist nur über den Component-Zweig belegt.
