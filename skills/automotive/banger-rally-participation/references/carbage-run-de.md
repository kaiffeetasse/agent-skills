# Carbage Run — Ausgaben, Regeln, Rechercheprotokoll (Stand 2026-10-08)

Quelle: carbagerun.de (DE/AT-Verband), carbagerun.com (Dachorganisation CRUM eventravel).
Erfasst am 08.10.2026 per curl/Extraktor; jede Zahl ist belegt, nicht geschätzt.

## Ausgaben 2027 (alle ausverkauft)

| Ausgabe | Termin | Status |
|---|---|---|
| Winterausgabe → Helsinki | 10.–15. Januar 2027 | ausverkauft |
| Winterausgabe → Rumänien | 25.–29. Januar 2027 | ausverkauft |
| Winterausgabe → Arctic Circle | 22.–26. Februar 2027 | ausverkauft |
| Sommerausgabe → Highway to Helsinki (Schweden/Finnland, über den Polarkreis, ~2.500 km) | 20.–24. Juni 2027 | ausverkauft |
| Sommerausgabe → „durch 15 Länder in 5 Tagen" | 29. Aug – 2. Sep 2027 | Teamtickets **bereits ausverkauft** (Anmeldefenster 06.10.2026, 20:00) |

Sommerausgabe 2026 → Albanien lief 21.–25. Juni 2026 (vorbei).

Struktur pro Jahr: DE/AT fährt **3–4 Ausgaben** (2 Sommer, 2 Winter). Campingplatz der Sommer-
Ausgaben ist jeweils das Etappenziel; Winter-Ausgaben übernachten im Hotel (Tagesziel-Adressen
stehen im Handbuch).

## Fahrzeug-Anforderungen (Wortlaut der Editionsseiten)

- mindestens 20 Jahre alt
- maximaler Tageswert 1.000 Euro (Richtwert, kein Nachweis: „Du brauchst weder eine Rechnung noch
  ein Gutachten"; es gilt der Wert am Starttag; „Pimpen" ist erlaubt, ein Tauschmotor nicht)
- gültiger TÜV, gültig bis mindestens 7 Tage nach der Veranstaltung
- Haftpflichtversicherung + Insassenversicherung
- zGG max. 3.500 kg
- keine scharfen/hervorstehenden Teile, keine Hupen/Sirenen/hupenförmigen Lautsprecher außen
- keine unzulässige Beleuchtung, keine Anhänger/Wohnwagen
- Winter zusätzlich: 3PMSF-Winterreifen ≥ 4 mm, Schneeketten, −30 °C Wischwasser, Decken
- Pflichtgepäck: Feuerlöscher ≥ 1 kg, Erste-Hilfe-Kasten, Warndreieck, Warnwesten (1/Person),
  gültige grüne Versicherungskarte

## Teilnahme-Regeln (FAQ)

- 18+; mind. ein Teammitglied mit 2 Jahren Führerschein (sonst nur Mitfahren)
- Teamgröße = zugelassene Sitzplätze; keine (Haus-)Tiere
- Beim Start: Ausweis für alle, gültige Versicherungspapiere, digital unterschriebenes Regeldokument
- Versicherung muss die Teilnahme **schriftlich** kennen (E-Mail genügt); „Rallyes/Tourfahrten"
  sind bei vielen Policen ausgeschlossen → bestätigen lassen oder Versicherer wechseln
- Stickerset Pflicht (50 × 20 cm je Vordertür freihalten), Navi erlaubt, Sponsoring erlaubt
- 30 Tage Storno nach Anmeldung; Weiterverkauf nur über TicketSwap, bis 4 Wochen vor Start
- kein Abschlepp-, Pannen- oder technischer Dienst; gegenseitige Hilfe ist Teil des Konzepts
- Campingplatz-Regeln: Schrittgeschwindigkeit, kein offenes Feuer, Ruhe ab 23:00, Unterlegkeile

## Recherche-Rezept (bewährt, ohne Browser-Automatik)

```bash
# 1) Alle Seiten inkl. Editions finden
curl -sL https://carbagerun.de/wp-sitemap.xml | grep -o '<loc>[^<]*</loc>' | sed 's/<[^>]*>//g'
#    -> https://carbagerun.de/event/<slug>/  je Ausgabe

# 2) Einzelseite holen und auf den "Wann?"-Block + Datumsmuster prüfen
curl -sL --max-time 30 -A "Mozilla/5.0" https://carbagerun.de/event/<slug>/ \
  | python3 -c "import sys,re,html; t=re.sub(r'<(script|style)[^>]*>.*?</\1>',' ',sys.stdin.read(),flags=re.S|re.I); \
t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t); \
m=re.search(r'Wann\?\s*(.{0,400})',t); print(m.group(1) if m else 'kein Wann?-Block')"
```

Verfügbarkeitssignale: „ausverkauft", „Uitverkocht!", „Teamtickets … bereits ausverkauft"
(vs. „Die Anmeldung öffnet am <Datum>"). Ticketübersicht: carbagerun.de/tickets/.

## Durchgerechnetes Beispiel: VW Polo (2010)

Fakten (aus Sessions): VW Polo 6R, **Bj. 2010**, FIN VWZZZ9NZ9B007814, **LR DY 362**, ~250.000 km,
Ankerblech durchgerostet (Empfehlung: Bremsleitungen/Achse mitprüfen), Takata-Rückruf 69EJ offen.

| Anforderung | Ist | Bewertung |
|---|---|---|
| ≥ 20 Jahre | 17 Jahre (2027) | ❌ nicht zugelassen — 20 Jahre erst 2030 |
| Tageswert ≤ 1.000 € | rostiger 250k-km-Polo 6R: Markt eher 1.500–2.500 € | ⚠️ knapp drüber (Richtwert) |
| TÜV bis +7 Tage | HU-Stand unbekannt, Rostmängel | ⚠️ prüfen |
| Haftpflicht | vorhanden | ✅ |
| Insassenversicherung | unbekannt | ⚠️ prüfen (meist Zusatzbaustein) |
| Grüne Versicherungskarte | unbekannt | ⚠️ anfordern |
| Versicherung schriftlich informieren | nicht erfolgt | ⚠️ Pflicht |

Fazit-Muster: „Fahrzeugkonzept passt, Baujahr passt nicht." → Optionen: anderes Fahrzeug
(Bj. ≤ Eventjahr−20, Tageswert ≤ 1.000 €, gültiger TÜV), auf 2030 warten und den Polo bis dahin
technisch sanieren, oder TicketSwap (löst das Auto-Problem nicht).
