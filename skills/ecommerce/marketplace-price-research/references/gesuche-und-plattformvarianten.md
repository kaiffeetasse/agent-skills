# Gesuche (Wanted-Ads) bepreisen + Plattform-Varianten sauber trennen

Verifizierte Lektionen 10/2026 aus einer Anfrage „ich würde dieses Gesuch gern befriedigen"
(Kleinanzeigen-Gesuch: PS2 + Simpsons Hit & Run, Goslar, Budget 150 €).
Gilt für jede Klasse „auf ein Gesuch antworten" / „Preis für eine bestimmte Plattform-Variante".

## 1. Gesuche leben in einem eigenen Index

Ein Gesuch ist **nicht** über die Standard-Suche erreichbar. `api.search()` ist per Default
`OFFERED`; Gesuche erscheinen **nur** mit:

```python
res = api.search(q="…", size=100, count=100,
                 ad_type="WANTED", poster_type="PRIVATE", include_top_ads=True)
hit = [i for i in res if i.get_id() == "<adId>"]
```

Ein ID-Abgleich in der `OFFERED`-Suche liefert `False` und sieht damit wie „gelöscht" aus —
genau der Fehlalarm aus `classifieds-liveness-and-deal-monitors.md` Abschnitt 1, nur anders
getriggert. **Erst den Status beweisen, dann etwas behaupten.**

Felder des Gesuch-Treffers (verifiziert):

| Feld | Bedeutung |
|---|---|
| `get_ad_status()` | `ACTIVE` = live (Statusbeweis) |
| `get_ad_type()` | `WANTED` |
| `get_price_amount()` | **Wunsch-/Budgetpreis des Suchenden**, kein Marktpreis |
| `get_zip_code()` / `get_state()` | Ort des Suchenden (hier 38640 Goslar) |
| `get_start_date_time()` | Alter des Gesuchs |
| `get_ad(adId)` | **unbrauchbar** — `KeyError: 'title'` |

`data-soldlabel` trägt bei Gesuchen `"Gefunden"`, bei Angeboten `"Verkauft"` — in beiden Fällen
Template-Rauschen und **kein** Statusbeleg.

## 2. Status NIE aus gerendertem Seitentext ableiten

`web_extract` auf eine `s-anzeige/…`-URL stellte der H1-Zeile „**Reserviert • Gelöscht** • <Titel>"
voran, obwohl die Anzeige per API `ACTIVE` war und das Roh-HTML (per `curl`) **kein**
`reserviert|gelöscht` enthielt. Die Zustands-Labels liegen als ausgeblendete Template-Varianten
vor. Verlässlich sind nur: API-`adStatus`, `canonical`/`og:url` für die ID-Prüfung, und ein
wirklich gerendertes Badge. Eine Status-Behauptung ohne Verifikation erzeugt verärgerte Rückfragen.

## 3. Recherche-Rezept vor der Antwort auf ein Gesuch

1. Gesuch-Status + Budget per `ad_type="WANTED"` holen (Abschnitt 1).
2. Beide Bestandteile **einzeln** bepreisen (nicht als Bundle) — hier PS2-Konsole und das Spiel
   getrennt, je mit Median/Q1/Q3 und n.
3. Median-Summe gegen das Budget des Suchenden stellen → zeigt, ob das Geschäft trägt.
4. Versand ergänzen, wenn der Suchende weit weg wohnt (Anbieter ↔ Suchender ≈ 500 km,
   DHL-Paket 5 kg ≈ 7 €). Gesuche tragen oft „Versand möglich" — das ist das Signal dafür.
5. Im Antworttext klar sagen, ob man die Teile **hat** oder erst beschaffen müsste. Bei
   Beschaffung zählt nur die Marge nach Einkauf + Versand — ein knapper Aufschlag ist kein Geschäft.

Gemessen (Kleinanzeigen, 10/2026, ~440 Konsolen- + 15 Spiel-Angebote):

| Position | n | günstig | Median | teuer |
|---|---|---|---|---|
| PS2-Konsole solo (mit Controller/Kabel) | 197 | 10 € | **70 €** | 92 €+ |
| PS2 im Set mit Spielen/Zubehör | 246 | 20 € | 99 € | 125 €+ |
| Simpsons Hit & Run — **PS2** | 15 | 30 € | **45 €** | 80 € |
| Simpsons Hit & Run — PC | 32 | 4 € | 20 € | 30 € |

Summe Einzelkauf ≈ 105–115 € gegen ein Budget von 150 € ⇒ trägt, Puffer ~35–50 €.

## 4. Plattform-/Geschwister-Filter bei Varianten-Preisen

Zieltoken **fordern**, Geschwister **hart ausschließen** — sonst kontaminieren Nachbarmodelle die
Statistik. Gemessen: die Suchbegriffe zogen PS1/PS3/PS4 mit herein, weil Zusatzwörter wie
„Slim"/„Konsole"/„Fat" auch auf Fremdmodelle matchen („Sony Play-Station 4 Slim",
„PlayStation 3 und PlayStation 4 Konsolen") — der Median stieg dadurch von real ~70 € auf ~100 €.

* **Fordern:** `(?:\bps2\b|playstation\s*2\b)`
* **Ausschließen:** `\bps[1345]\b|playstation\s*[1345]\b|psp|vita|nintendo|xbox|gamecube|\bwii\b`
* **Bei Spielen die Ports trennen:** derselbe Titel kostet als PS2-Fassung Median 45 €, als
  PC-Fassung 4–20 € — ein ungefilterter Titel-Median ist um Faktor 2–3 falsch.
* **Populationen getrennt ausweisen:** Solo-Konsole vs. Bundle „Konsole + N Spiele"; 1-€-Platzhalter
  und „nur Gehäuse / ungeprüft / defekt" herausfiltern. Bei Konsolen < 30 € steht fast immer
  „ungeprüft"/„defekt"/nur Gehäuse im Text.
* **Gegenprobe:** 3–5 Kandidaten live prüfen (`viewad-price`) — der Suchindex war bei mehreren
  Anzeigen bereits reduziert.
