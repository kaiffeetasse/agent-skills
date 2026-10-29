---
name: shipment-tracking
description: "Use when tracking a parcel or answering where-is-my-package."
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [DHL, Hermes, Paket, tracking, Kleinanzeigen]
    related_skills: [kleinanzeigen-search, cron-silent-watchdog]
---

# Shipment Tracking

Für „Wo ist mein Paket?", „Ist heute etwas abzuholen?" und Statusprüfungen zu
Kleinanzeigen-Käufen. Immer **live** abfragen; ein Watchdog-State kann veraltet
sein und ist keine Antwort auf eine aktuelle Frage.

## When to Use

- Der Nutzer fragt nach dem Status, Ort oder Abholzeitpunkt eines Pakets.
- Eine Kleinanzeigen-Bestellung soll nachverfolgt werden.
- Ein Paket-Watchdog soll gebaut oder geprüft werden.

Nicht für Retouren-/Reklamationsbearbeitung oder Adressänderungen beim Händler.

## 1. Sendungsnummer besorgen

- Bei Kleinanzeigen: `get_conversation_payment_status(conv_id)` liefert
  `trackingNumber`, `carrierId` und einen Tracking-Link. Dieselbe Nummer steht
  im Chat; nicht raten und nicht aus dem Gedächtnis einsetzen.
- Bei Hermes: die Nummer aus der Versandmail/App; das bestehende
  `~/.hermes/scripts/paket_ankunft_watchdog.py` deckt Hermes-Sendungen ab.
- Immer die **exakte** Nummer aus der Quelle verwenden; eine falsche Nummer
  liefert bei DHL eine fremde oder keine Sendung.

## 2. DHL-Status abfragen

Öffentlicher JSON-Endpunkt (die Website nutzt denselben):

```bash
curl -sS 'https://www.dhl.de/int-verfolgen/data/search?piececode=<NR>&language=de' \
  -H 'User-Agent: Mozilla/5.0' -o /tmp/dhl.json
```

Parsen:

- `sendungen[0].sendungsdetails.sendungsverlauf.status` — Kurzstatus
- `.datumAktuellerStatus` — Zeitpunkt
- `.events[]` — `datum`, `status`, `ort` (chronologisch)
- `sendungsdetails.zustellung.empfaenger.name` — z. B. „Briefkasten"
- `sendungsdetails.zustellung.zugestelltAnBriefkasten` — true bei Briefkastenzustellung
- `sendungsdetails.zustellung.abholcodeAvailable` / `benachrichtigtInFiliale`

Statusdeutung:

- „in das Zustellfahrzeug geladen" = **in Zustellung**, noch nicht da.
- „Zustellung erfolgreich" + `zugestelltAnBriefkasten: true` = im Briefkasten,
  kein Abholcode nötig.
- Packstation: erst wenn ein Event „in die Packstation gelegt" nennt und
  `abholcodeAvailable: true` ist, gibt es einen Abholcode.

**Adresse:** Die öffentliche DHL-API liefert **keine Empfängeradresse** — auch
nicht mit `postalCode`, `plz`, `zip` oder `postCode` (Antwort bleibt identisch).
`isNoPackstation` allein ist kein Adressbeweis. Für die genaue Anschrift nur
DHL-App/Konto oder das Versandlabel nennen; nicht aus dem Status raten und keine
Adresse behaupten, die die API nicht hergibt.

## 3. Antworten

- Zuerst den **aktuellen** Status und den letzten Event mit Zeit nennen.
- Bei „zugestellt" den Ort aus `zustellung` ableiten (Briefkasten, Nachbar,
  Filiale) und klar sagen, ob etwas abzuholen ist.
- Bei „in Zustellung" kein Abholcode versprechen; nur Zeitfenster/Tendenz.
- Wenn der Nutzer die Adresse wissen will: offen sagen, dass die API sie nicht
  ausgibt, und die zwei echten Quellen nennen (DHL-App, Label/Bestellung).

## 4. Watchdog

Für dauerhaftes Beobachten einen stillen Cronjob bauen (`cron-silent-watchdog`):
Status-Hash + Events in einer State-Datei speichern, nur bei Änderung melden,
transiente Fetch-Fehler still schlucken. Der Watchdog ersetzt **nicht** die
Live-Abfrage auf eine direkte Nutzerfrage.

## Pitfalls

- **Status „Zustellung erfolgreich" ist die Wahrheit, nicht die Ankündigung
  „voraussichtlich heute".** Immer den neuesten Event lesen.
- **Nicht zwei Quellen vermischen:** Die Sendungsnummer aus Kleinanzeigen und
  die DHL-Antwort gehören zusammen; eine PLZ-Suche ist kein Ersatz.
- **Keine Adresse aus `isNoPackstation` ableiten.** Das Flag ist mehrdeutig; die
  Zustellart steht in `zustellung` und im Event-Text.
- **Kein „Paket ist da", solange nur „in Zustellung" steht.**
