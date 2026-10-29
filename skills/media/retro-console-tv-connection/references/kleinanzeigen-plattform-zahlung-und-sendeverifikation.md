# Kleinanzeigen-Mechanik, die beim Konsolenkauf greift (verifiziert 09/2026)

Diese Punkte gehören inhaltlich in die **user-owned** Skills `kleinanzeigen-search` und
`kleinanzeigen-negotiation` (für autonome Kuratierung gesperrt — `hermes curator adopt <name>`,
dann dorthin verschieben). Hier geparkt, damit die Erkenntnis nicht verloren geht.

## 1. `securePayment: false` ist KEIN harter Ausschluss (Korrektur)

`kleinanzeigen-search` führte bisher: „bei `securePayment: false` ist ‚Sicher bezahlen' für diesen
Verkäufer nicht verfügbar". Das ist **zu hart**. Messung 09/2026 an 4 PS1-Verkäufern:

| Verkäufer | `securePayment` | `get_payment_fee` |
|---|---|---|
| Lünen (PS1 SCPH-9002) | false | funktioniert: 45 € + 7,69 € Versand + 2,53 € Gebühr = **55,22 € total** |
| Sinzheim (PS1 mod-chip) | false | funktioniert: 55 € + 7,69 € + 2,98 € = **65,67 € total** |
| Sauerlach | true | (nicht gebraucht) |
| Eislingen | false | (nicht gebraucht) |

3 von 4 standen auf `false`, trotzdem lieferten die beiden geprüften Anzeigen echte
Gebührenwerte und damit einen gültigen Plattformweg.

**Richtige Prüfkette:** `get_shipping_options(ad_id)` → `PREDEFINED_SHIPPING` **mit gefüllter
`options[]`** → `get_payment_fee(ad_id, cent, shippingType, option_id)` liefert
`offeredPriceInEuroCent/shippingCostInEuroCent/buyerFeeInEuroCent/totalInEuroCent` + Token.
Erst wenn das scheitert oder `INDIVIDUAL_SHIPPING` mit leerer `options[]` kommt (typisch „nur
Abholung"), existiert kein „Sicher bezahlen". Das Konto-Flag nur als Warnhinweis lesen — wer es
als Blocker behandelt, verwirft gute Deals grundlos.

## 2. Wo die Verkäuferdaten herkommen

- `get_public_profile(user_id)` gibt es im **Toolbox-Client**
  (`~/.hermes/skills/devops/kleinanzeigen-toolbox-workflow/references/toolbox-original/kleinanzeigen_client.py`):
  `userSince`, `counters.historicalAds/onlineAds/followers`, `userBadges` (rating/friendliness/
  reliability/replyRate/replySpeed je Level 0–2), `userRatings.averageRating` (**0–1**, nicht 0–5).
- Im Monitoring-Modul `kleinanzeigen-monitoring/api/kleinanzeigen.py` fehlt die Methode
  (`AttributeError`) — dort die User-ID aus der **Anzeigenseite** holen (`userId=(\d+)`).
- Achtung: `find_locations('<Stadt>')` liefert `Location`-Objekte (`.id`, `.name`); der erste
  Eintrag ist `Deutschland` (id 0) → nach `name` filtern. Die eigene Stadt liefert hier `9027`.

## 3. Sendeerfolg wird am Thread belegt, nicht am Rückgabewert

`send_message_in_conversation(conv_id, msg)` liefert bei Erfolg **`None`** (kein Body).
`None` ist **kein Fehler** und darf **nie** einen zweiten Send auslösen. Beleg ist das
Gegenlesen: `get_conversation(conv_id)` → Nachrichtenzahl erhöht + eigener Volltext vorhanden
(mit echten Zeilenumbrüchen, nicht literalen `\n`).

Verifiziert 09/2026: zwei Sends in derselben Verhandlung, beide `None`, beide korrekt im Thread
(Nachrichtenzahl 2 → 3 → 5 über die Runden). Ein Sende-Skript sollte deshalb die Nachrichtenzahl
**vor** dem Send messen und **nach** dem Send gegenlesen, statt auf den Rückgabewert zu bauen.

## 4. Zahlungsweg-Klärung, wenn der Verkäufer den Plattformweg ablehnt

Lehnt der Verkäufer „Sicher bezahlen" ab („Ich akzeptiere nur PayPal", „weiß nicht, wie man das
abschaltet") und bietet **PayPal Waren & Dienstleistungen mit Gebührenübernahme** an, ist das ein
sicherer Weg — annehmen und schriftlich fixieren. Bewährte Formulierung (real, PS1-Kauf):

> „PayPal Waren & Dienstleistungen ist genau richtig, da hat der Käufer den Käuferschutz. Die
> Gebühr übernehme ich, damit bei Ihnen genau 52,70 EUR ankommen (45 EUR + 7,70 EUR Versand) —
> für Sie fallen also keine Kosten an."

Zwei Regeln: (1) immer den **Nettobetrag** nennen, der beim Verkäufer ankommt (Artikel + Versand),
sonst zieht die Gebühr still vom vereinbarten Preis ab; (2) **PayPal Freunde/Familie bleibt
ausgeschlossen**, auch mit Gebührenübernahme. Vorher trotzdem `get_shipping_options` prüfen und
zuerst den Plattformweg anbieten.

## 5. Umlaute im Sendetext

Der Sendepfad ist UTF-8-sauber — echte Umlaute (`Läuft`, `wäre`, `Grüße`) kommen korrekt an
(belegt: Verkäuferantwort und eigene Nachrichten im Thread). Aus Vorsicht mit `ue`/`ae`/`oe`
geschriebene Erstnachrichten wirken erkennbar generiert; direkt Umlaute verwenden. Deswegen
**keinen** zweiten Send schicken — eine Doppelnachricht ist der größere Fehler.
