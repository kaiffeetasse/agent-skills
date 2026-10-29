# Zweiphasiger Markt-Wächter: erst Lernwoche, dann Schnäppchen-Alarme

Auftragsmuster: **„beobachte ~1 Woche, was angeboten wird, und richte danach Alarme für gute
Schnäppchen ein."** Die Alarmschwelle ist vorher unbekannt → sie wird aus den gesammelten Daten
berechnet, nicht geraten. Ein Job mit zwei Phasen statt Blind-Alarm.

## Daten & Zustand

| Datei | Rolle |
|---|---|
| `~/workspace/<topic>/monitor/listings.jsonl` | Append-Log jeder passenden Anzeige (`id, title, price, Klasse, km, zip, link, ts`) |
| `~/workspace/<topic>/monitor/baseline.json` | nach jedem Lauf neu: `{Klasse: {n, median, p25, min}}` über alle Zeilen |
| `~/.hermes/cron/state/<topic>_watch.json` | `seen` (id → Ablehnungsgrund/Preis), `learn_until`, Alarme pro Tag, `learn_report_sent` |
| `~/workspace/<topic>/monitor/watch.log` | Fehler/Diagnose — **nie** stdout, das ist der Telegram-Kanal |

Tick (stündlich, `no_agent`): sammeln → Basis neu rechnen → `now < learn_until` ⇒ **still** →
danach einmalig Lernauswertung, dann Alarme.

## Alarmschwelle (bewährt)

```
Preis <= 0.62 * Median(Klasse)     # echter Abschlag, nicht „günstigster Treffer"
Preis <= HARD_CAP[Klasse]          # absolute Obergrenze, z. B. 80 € (1 TB), 150 € (2 TB)
Preis/Einheit <= EUR_PER_UNIT_MAX  # z. B. 85 €/TB
```

plus `MAX_ALERTS_PER_DAY` (4), Dedup über die Anzeigen-ID und ein eigener Trigger für Preisrückgänge
bekannter Anzeigen. Vorher den **Neupreis-Anker** holen: liegt der Gebraucht-Median über dem
Neupreis, sind die unteren ~5 % die Deals — dann ist ein harter Prozent-Abschlag richtig.

## Trennschärfe: Kapazität nur aus dem Titel, nur EINE Angabe

```python
CAPTOK_RE = re.compile(r"(?<![\d,.])(?:(\d{3,4})\s?GB\b|([1248])\s?TB(?!\s?[BW]))", re.I)
toks = [int(gb) if gb else int(tb) * 1000 for gb, tb in CAPTOK_RE.findall(title)]
if len(toks) != 1: reject("Kapazität unklar/mehrfach")   # Sammelanzeige „256GB für 39€ oder 2TB…"
if toks[0] < 1000: reject("kleiner als 1 TB")            # 250-GB-Platte …
if toks[0] > 2048: reject("zu groß")
```

Lookbehind `(?<![\d,.])` tötet Dezimalwerte („7,2 TB" = **TBW**, nicht Kapazität), `(?!\s?[BW])`
tötet „TBW". Ohne diese Regel kamen 10/2026 „2 TB für 39 €" (zwei Platten in einer Anzeige) und
„2 TB für 49 €" (250-GB-Platte mit TBW-Angabe) als Top-Deals durch.

Weitere Pflicht-Ausschlüsse bei Speicher/Hardware: `sata` **ohne** `nvme|pcie` im Text
(`Intenso M.2 SSD TOP` = SATA-M.2, B+M-Key), `2[.,]5\s?"`-Zeilen, extern/Gehäuse/Adapter/Kabel,
`defekt|Bastler|ungetestet|läuft nicht`, Gesuche/Tausch, „oder"-Anzeigen mit mehreren Preisen.
**Vorher klären, was ins Zielsystem passt** (`lsblk` / `nvme list` / `lspci` am eigenen Rechner) —
sonst empfiehlt man den falschen Formfaktor.

## Verifikation ohne echte Alarme

1. **Filter-Selbsttest** mit synthetischen Anzeigen-Objekten → „erwartet OK/REJ" je Fall.
2. **Alarmpfad-Test**: `learn_until`/Tageszähler im State manipulieren, im Vordergrund laufen lassen,
   Ausgabe prüfen, State zurücksetzen.
3. **Stiller Normalzustand**: zweimal ohne Stateänderung → beide Male leerer stdout.

## Referenzzahlen (M.2-NVMe, 10/2026, 373 passende Anzeigen)

1 TB NVMe: Median **140 €**, 25 %-Quantil 115 €, Minimum 69 € · 2 TB: Median **242 €** ·
Neupreis-Anker 1 TB ≈ 115–135 €. Skript-Vorbild: `~/.hermes/scripts/ssd_deal_watch.py`.

## Verwandt: Kauf-/Angebotsseite (frische Konten = Betrugsmuster)

Beim Kauf frisch inserierter, auffällig billiger Elektronik die Verkäuferseite technisch prüfen statt
auf den Anzeigentext zu hören: `get_public_profile(userId)` (`userSince`, `counters.onlineAds`,
`userBadges.badges`, **`securePayment`**) plus das Feld `user-since-date-time` der Anzeige selbst.
Muster (verifiziert 10/2026, UDR7 für 70 € statt ~230 €): **Konto am selben Tag angelegt** wie die
Anzeige, 0 Bewertungen, keine Badges, Marketing-Text im Werbe-Deutsch, falsche Kategorie.
Konsequenz: nur über „Sicher bezahlen" kaufen (Geld liegt treuhänderisch), niemals Überweisung/
Vorkasse/PayPal-Freunde, keine Rufnummer/Mail herausgeben — und ein verbindliches Angebot vorher
zurückziehen (`cancel_offer(negotiation_id, offer_id)`), wenn stattdessen Abholung vereinbart wird.
