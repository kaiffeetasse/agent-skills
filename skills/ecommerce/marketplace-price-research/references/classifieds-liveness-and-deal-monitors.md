# Classifieds: Anzeigen-Liveness, Kapazitätsparsing & „Lern-dann-Alarm"-Wächter

Verifizierte Lektionen aus einer 1-TB-M.2-NVMe-Suche + Schnäppchen-Wächter (Kleinanzeigen, 10/2026).
Gilt für jede Klasse „gebrauchte Hardware/Technik auf Kleinanzeigen bewerten + Deals überwachen".

## 1. „Reserviert"/„Gelöscht" im Seitentext sind Template-Platzhalter

**Messung:** Ein Seiten-Rendering (`web_extract`) zeigte bei einer Anzeige prominent
„Reserviert • Gelöscht". Gleichzeitig führten
* der echte Browser (sichtbarer Text **ohne** Statusbanner),
* der Suchindex **und**
* die App-API (`api/ads/{id}.json` → `ad-status: ACTIVE`)

dieselbe Anzeige als **aktiv**. Die Labels sind also Markup-Zustände, die der Renderer
linearisiert hat — analog zum bekannten `data-soldlabel="Verkauft"`-Rauschen.

**Regel:** Status **nie** aus gerendertem Seitentext ableiten. Verlässlich sind:
1. `ad-status` aus der App-API (`kleinanzeigen_public.get_ad(id)`): `ACTIVE` = live,
   `PAUSED` = reserviert bzw. deaktiviert (verschwindet dann aus der Suche).
2. `<link rel="canonical">` / `og:url` + `<h1 id="viewad-title">` zur ID/Titel-Gegenprobe.
3. `viewad-price` (+ `boxedarticle--old-price`) für den **aktuellen** Preis — der Suchindex
   ist träge und zeigt teils den alten Preis.
Der Suchindex ist **kein** Liveness-Beweis; die Anzeigenseite im echten Browser ist der
beste „sieht der Nutzer es so?"-Test.

## 2. Kapazität/Bauart bei Speicher-Suchen hart parsen

Zwei Fehltreffer-Klassen, die billige „Schnäppchen" vortäuschen (real gemessen):

| Anzeige | Fehler | Regel |
|---|---|---|
| „M.2 SSD NVMe 256GB für 39 € **oder** 2TB Samsung 990 … für 239 €" | Sammelanzeige, Preis gilt für die kleine Platte | Kapazität nur aus dem **Titel**, und nur wenn dort **genau eine** Angabe steht |
| „Samsung SSD 980 250GB … **7,2 TB**, 97 %" | „7,2 TB" = TBW (Endurance), keine Kapazität | Dezimal-Lookbehind: `(?<![\d,.])(\d{3,4})\s?GB\b` bzw. `([1248])\s?TB(?!\s?[BW])` |
| „Intenso M.2 SSD **TOP** 1TB" | SATA-M.2 (B+M-Key), kein NVMe | Bus aus Titel **und** Volltext: `sata` ohne `nvme` ⇒ ablehnen |
| „1TB SATA M.2 — läuft auf SATA und auch NVMe" | Werbetext, technisch falsch | NVMe muss aktiv belegt sein (`nvme|pcie`), sonst Bus unklar ⇒ ablehnen |

Zusätzlich ausschließen: `extern|Gehäuse|Enclosure|Adapter|Dock|Lesegerät|USB|SD-Karte|Hülle|Kabel`,
`defekt|Bastler|Ersatzteil|ungetestet|kann nicht testen|läuft nicht`, `Gesuch|Tausch|Ankauf`,
Mehrfach-Bundles (`2x`, `Konvolut`) und Platten < 1 TB / > 2 TB.

## 3. Muster: „erst ~1 Woche lernen, dann alarmieren"

Für „beobachte X eine Woche und richte dann Alarme ein" (Implementierung:
`~/.hermes/scripts/ssd_deal_watch.py`, no_agent-Cron, stündlich):

* **Phase 1 (Lernphase, still):** jede Stunde alle Suchbegriffe abfragen, jeden passenden
  Treffer mit Preis/Titel/PLZ/Koordinaten in `listings.jsonl` anhängen und daraus
  **Median + p25 pro Klasse** (Kapazität/Formfaktor) in `baseline.json` rechnen.
  Ein cron-`no_agent`-Job ist in dieser Phase komplett still (leerer stdout).
* **Phase 2 (Alarme):** nur bei ≤ 62 % des Lern-Medians **und** unter einem harten Cap
  (z. B. 80 €/1 TB, 150 €/2 TB) **und** ≤ 85 €/TB; max. 4 Meldungen/Tag, Dedup per
  Anzeigen-ID, **Live-Status-Check vor jeder Meldung** (Abschnitt 1). Am Ende der Lernwoche
  einmalig eine kurze Marktauswertung senden.
* **Anzeigentext für die Meldung:** Preis, €/TB, Abweichung zum Median, Entfernung ab
  Wohnort, Link und der Prüfhinweis (bei SSDs: CrystalDiskInfo-Screenshot mit Health/TBW/
  Betriebsstunden anfordern; Zahlung nur „Sicher bezahlen" oder Barzahlung bei Abholung).

## 4. Bewertung: Neupreis-Anker und Nebenkosten entscheiden

* **Neupreis-Anker vor jeder Kaufempfehlung** (Geizhals-Direktzugriff per `curl` = 403;
  `web_extract` auf `https://geizhals.de/?fs=<produkt>&in=&sort=p&v=l&pagesize=100&hloc=de`
  funktioniert). Beispiel 10/2026: 1-TB-NVMe gebraucht Median **140 €** / p25 115 €
  (nur 2 von 229 Anzeigen < 80 €), neu ~110 € (Verbatim Vi3000) bis **155 €**
  (WD Blue SN5100 1 TB) ⇒ der Gebrauchtmarkt liegt *über* Neupreis-Niveau; nur echte
  Ausreißer sind Deals.
* **Nebenkosten immer mitrechnen.** „Nur Abholung" 122 km ≈ 1,5 h pro Strecke und
  25–30 € Sprit — ein 70-€-Angebot wird damit teurer als ein 89-€-Angebot in 83 km
  Entfernung mit Versand. Verkäuferprofil prüfen: `securePayment: false` bedeutet
  **kein** „Sicher bezahlen" ⇒ bei Versand nur Überweisung (Risiko) oder Abholung.
* Technik-Kontext mitgeben, wenn er die Entscheidung dreht: QLC/DRAM-less vs. TLC mit
  DRAM-Cache (PM9A1/PC801/PM981a) und „Gen4-Platte im Gen3-Slot läuft nur mit Gen3-Tempo".
