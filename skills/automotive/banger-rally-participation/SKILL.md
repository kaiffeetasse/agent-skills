---
name: banger-rally-participation
description: "Use when checking banger-rally rules and car eligibility."
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Rallye, CarbageRun, Rostlaube, Auto, Versicherung, Tickets, Recherche]
    category: automotive
    related_skills: [maps, marketplace-price-research, kleinanzeigen-search, product-price-monitor]
---

# Rostlauben-Rallye: Termine, Regeln, Fahrzeug-Eignung

## When to Use

- „Welche Termine hat der Carbage Run?", „Wann öffnet die Anmeldung?"
- „Erfüllt mein Auto die Voraussetzungen?" (Alter, Wert, TÜV, Versicherung, Ausrüstung)
- Ticket-Lage prüfen (ausverkauft? TicketSwap?), Watchdog für Anmeldefenster planen
- **Nicht** für normale Urlaubs-/Mietwagenreisen → `travel-planning-research`

## Harte Regeln (Carbage Run DE/AT, Stand 2026-10-08, carbagerun.de)

**Fahrzeug:** mindestens **20 Jahre alt** · **Tageswert max. 1.000 €** (Richtwert — keine
Rechnung, kein Gutachten; es gilt der Wert am Starttag) · **TÜV gültig bis mind. 7 Tage nach
der Veranstaltung** · **Haftpflicht- UND Insassenversicherung** · zGG ≤ 3.500 kg · keine
scharfen Teile, keine außenliegenden Hupen/Sirenen/hupenförmigen Lautsprecher, keine nicht
erlaubten Leuchten · **keine Anhänger/Wohnwagen**.

**Winterausgaben zusätzlich:** Winterreifen mit 3PMSF ≥ 4 mm, Schneeketten mitführen,
Wischwasser bis −30 °C, Decken (1/Person).

**Pflichtgepäck:** Feuerlöscher ≥ 1 kg, Erste-Hilfe-Kasten, Warndreieck, Warnweste je Person,
**gültige grüne Versicherungskarte**.

**Versicherung (der Punkt, an dem es real scheitert):** Teilnahme ist der Versicherung
**schriftlich** zu melden (E-Mail genügt). Viele Policen schließen „Rallyes/Tourfahrten" aus →
schriftliche Bestätigung einholen oder Versicherer wechseln. Argumentationshilfe: „Es geht nicht
um Geschwindigkeit und Zeit."

**Team/Dokumente:** alle ≥ 18 J., mind. ein Fahrer mit ≥ 2 Jahren Führerschein, Teamgröße =
zugelassene Sitzplätze, keine Tiere. Beim Start: Ausweise, gültige Versicherungspapiere,
digital unterschriebenes Regeldokument. Stickerpflicht: je 50 × 20 cm auf beiden Vordertüren
freihalten. Anmeldung ohne Auto ist möglich (Fahrzeugdaten später nachreichen).

**Tickets:** Editions sind praktisch immer ausverkauft; Weiterverkauf **nur über TicketSwap**
(bis 4 Wochen vor Start) — nie über Social Media/Kleinanzeigen. 30 Tage kostenloses Storno.
Camping-/Zusatztickets oft noch nachbuchbar.

## Fahrzeug-Eignung prüfen — Reihenfolge zählt

1. **Baujahr → Alter im Eventjahr.** Show-Stopper, deshalb zuerst: Bj. 2010 → 20 Jahre erst
   **2030**. Es zählt das Fahrzeugalter, nicht der Serienstart der Baureihe.
2. **Tageswert ≤ 1.000 €**: als Richtwert behandeln; realistische Marktpreise vergleichen
   (`marketplace-price-research`, Kleinanzeigen), Rost/Unfall/Laufleistung einpreisen.
3. **TÜV-Fenster**: HU muss ≥ 7 Tage nach dem Zieltermin gültig sein → HU-Datum prüfen; bekannte
   Rostmängel (Bremsleitungen, Ankerbleche, Achse) gefährden die HU.
4. **Versicherung**: Haftpflicht + Insassenunfallschutz getrennt prüfen, schriftliche
   Rallye-Meldung, grüne Karte für Nicht-EU-Routen (Balkan, Albanien, Moldau).
5. **Technik vs. Etappen**: 350–500 km/Tag, Schotter, Pässe, kein Abschlepp-/Pannendienst —
   nur gegenseitige Hilfe.
6. **Ausgabeformat (knapp halten):** Tabelle `Anforderung | Ist | ✅/⚠️/❌`, danach ein
   Satz Fazit und 2–3 Optionen (anderes Auto Bj. ≤ Eventjahr−20 / TicketSwap / warten).

## Termine & Verfügbarkeit recherchieren

- **WordPress-Eventseiten finden:** `curl -sL https://<domain>/wp-sitemap.xml | grep -o '<loc>[^<]*</loc>'`
  listet alle Seiten — die Editions stecken als `/event/<slug>/`. Kein Browser nötig.
- Einzelseite per `curl -sL --max-time 30 -A "Mozilla/5.0" <url>` holen, Tags strippen, dann nach
  dem `Wann?`-Block und Datumsmustern (`\d{1,2}\. (bis|-)\s*\d{1,2}\. <Monat> 20\d\d`) greppen.
- **Verfügbarkeit** an Textsignalen ablesen: „ausverkauft", „Uitverkocht", „Teamtickets …
  bereits ausverkauft"; „Anmeldung öffnet am …" heißt: noch offen.
- Fallback, wenn Scraper-Dienste ratenlimitiert sind (429 / „Rate limit exceeded") oder JS-Seiten
  leer zurückkommen: kurz warten und erneut, sonst curl+Regex wie oben.
- Anmeldefenster öffnen typischerweise im **Oktober 20:00** fürs Folgejahr und sind binnen
  Stunden bis Tagen zu → wiederkehrender Watchdog sinnvoll (Cron, `no_agent`-Script).

## Pitfalls

- „20 Jahre" = Fahrzeugalter, nicht Baureihe/Serienstart.
- Promo-/Blogartikel nennen teils andere Grenzen (z. B. „25 Jahre") — es gilt die Editionsseite
  des jeweiligen Landesverbands.
- Kein Pannen-/Abschleppdienst: eigene Pannenhilfe-Versicherung ist freiwillig, aber schlau.
- Spikes nur in Skandinavien erlaubt, in Deutschland verboten.
- Ziel- und Etappenorte stehen erst im Handbuch (4 Wochen vorher) — keine Frühbuchung nötig.

## Referenzen

- `references/carbage-run-de.md` — alle 2027er Ausgaben mit Terminen/Status, Regelliste,
  Recherche-Kommandos und das durchgerechnete Beispiel „VW Polo Bj. 2010".
