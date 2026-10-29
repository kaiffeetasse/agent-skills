# Versandkosten DE + eigene Verkäufe prüfen (Stand 07/2026)

Belege aus einer Live-Session (2026-10-08, eigener Kleinanzeigen-Verkauf
„Drucksprüher Gartenspritze", Anzeige `3489360495`, 60 € VB): alle Tarife und alle
Fallen unten sind real abgefragt bzw. real aufgetreten.

## 1. Versandtarife Inland — für „Artikel + Versand + Gebühr"

**DHL / Deutsche Post**, Stand 01.07.2026 (`dhl.de/…/preise-national.html`,
`dp-leistungen-und-preise-092026.pdf`):

| Produkt | Max. Maße | Gewicht | Preis |
|---|---|---|---|
| Päckchen S | 35 × 25 × 10 cm | 2 kg | 4,19 € (ohne Tracking/Haftung) |
| Päckchen M | 60 × 30 × 15 cm | 2 kg | 5,19 € (ohne Tracking/Haftung) |
| Paket 2 kg | 60 × 30 × 15 cm | 2 kg | 6,19 € (nur online) |
| Paket 5 kg | 120 × 60 × 60 cm | 5 kg | 7,69 € |
| Paket 10 kg | 120 × 60 × 60 cm | 10 kg | 10,49 € |

Paketpreise inkl. Sendungsverfolgung + Haftung bis 500 €; Päckchen ohne.

**Hermes**, gültig ab 02.03.2026 (`myhermes.de/preise/paeckchen-paket/`): L-Paket
(längste + kürzeste Seite ≤ 120 cm, bis 25 kg, 500 € Haftung) **10,99 € online** /
11,95 € PaketShop; Shop2Shop S 4,40 € / L 10,40 €. Hermes S/M hängen an
„längste + kürzeste Seite zusammen" (S ≤ 50 cm, M ≤ 80 cm) — bei sperrigen Kartons
schnell gerissen.

**Rechenregel:** Leergewicht (Herstellerangabe) + **0,6–1,0 kg** Verpackung; liegt das
Ergebnis über der Grenze, gilt die nächsthöhere Stufe. Praktisch: fast alles über 2 kg
landet in „Paket 5 kg" (7,69 €) oder „Paket 10 kg" (10,49 €). **Päckchen scheiden aus,
sobald das Paket höher als 15 cm ist.**

## 2. Produktidentität aus Anzeigenbildern ohne Browser klären

1. Detail-Endpunkt liefert `value['pictures']['picture']`, je Bild die `link`-Einträge;
   nimm `rel="XXL"`.
2. URL mit **`?rule=$_57.AUTO`** laden (das `.JPG`-Pendant 404t), `curl -A "Mozilla/5.0 …"`.
3. Bilder lokal mit Vision prüfen und Marke/Typenschild/Aufdruck ablesen.

Bringt oft mehr als jeder Anzeigentext: Die Aufschrift „SOLO … 425 MADE IN GERMANY CE"
plus die Deckelprägung ergaben zweifelsfrei eine **SOLO 425 Rückenspritze, 15 l,
Kolbenpumpe, 4,4 kg leer** — und damit direkt die Versandstufe.

**Grenze der Bilder ehrlich benennen:** Fotos beweisen keine Dichtungen, keine Funktion,
keine freie Düse. Bei Geräten mit Druck/Flüssigkeit offen sagen und einen Funktionstest
vor dem Versand empfehlen (hier: aufpumpen, 10 Minuten stehen lassen).

## 3. Verkäufer-Fallen (alle live getroffen)

- **Anzeigen-Attribut vs. Chat können sich widersprechen.** Kategorieabhängiges Attribut
  `versand` (z. B. `garten.versand`, `kueche_esszimmer.versand`) stand auf `nein` =
  **„Nur Abholung"**, während im Chat Versand zugesagt worden war. Zusätzlich war
  `shipping-options` in der Anzeige `null` und in der Conversation
  `shippingType: INDIVIDUAL_SHIPPING` mit Kosten 0 → **kein hinterlegtes Versandprofil**.
  Vor jeder Versandzusage den Anzeigenstatus lesen: bei „Nur Abholung" kann der Käufer den
  Versandweg im Bezahlsystem gar nicht wählen.
- **Flags zu Käuferschutz sind unzuverlässig.** `paymentPossible: false` und
  `adEligibleForPayment: false` im Conversation-Objekt, aber die Probe
  `get_payment_fee(adId, cent)` lieferte eine **gültige Quote** (60 € → 3,20 € Gebühr,
  total 63,20 €, mit Token). Immer probehalber quoten, statt dem Flag zu glauben.
- **Der Namens-Feldwert ≠ Anrede.** Die API führte den Käufer als „Franz", er unterschrieb
  mit „Carsten" — und der bisherige Verlauf hatte ihn „Hallo Carsten" genannt. Anrede
  **aus dem Chatverlauf** nehmen.
- **Kopfzähler sind unzuverlässig.** `numUnread: 9` bei nur **einer** Konversation mit
  `unread: true`. Ungelesen-Status aus den Feldern der einzelnen Chat-Objekte ableiten.
- **Richtung nicht am Feld erkennen.** `authorId` war in allen Nachrichten leer/`None`;
  Richtung aus dem Inhalt ableiten. Eine Nachricht erscheint zudem **zweimal** im JSON
  (`textShort` **und** `unichatMessage.payload.content.text`) — das ist **eine** Nachricht,
  keine Doppelsendung.
- **Benutzte Chemikalien-Geräte** (Pflanzenschutz-Spritzen, Tanks) nur **leer, gespült,
  getrocknet** versenden und in einen Beutel packen: Restchemikalien sind von der
  Beförderung ausgeschlossen, und Pumpen tropfen gern nach.
- **Antwort erst nach ausdrücklicher Freigabe senden.** Vollständigen Verlauf lesen, dann
  Entwurf + Empfehlung vorlegen, senden nur auf OK. Dazu gehören die Plausibilitätschecks:
  Anzeige noch ACTIVE? weitere Interessenten (gleiche Anzeigen-ID über alle Chats suchen)?
  Käufer etabliert (`buyerRegistrationDate`, z. B. seit 2016)?

## 4. Gesamtkosten korrekt ausweisen

Bei Käuferschutz kommt die Gebühr **obendrauf**: 60 € + 10,49 € (DHL Paket 10 kg) =
70,49 €, mit Gebühr grob **~73,70 €**. Wenn man Abholung statt Versand empfiehlt, diesen
Aufschlag nennen — bei einem 60-€-Artikel sind 10,49 € ein spürbarer Anteil und der Grund,
warum Abholung häufig der sauberere Weg ist.
