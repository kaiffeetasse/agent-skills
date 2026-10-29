# Verbindliche Vorgänge wiederholen oder zurückziehen (Live-Zustand statt Chat-Eindruck)

Fallklasse: Ein Agent soll im Namen des Nutzers einen **verbindlichen Vorgang** (Kleinanzeigen-
„Preisvorschlag"/Sicher-bezahlen-Angebot, Bestellung, Vertragsanfrage) wiederholen, „reparieren"
oder neu abschicken. Zwei echte Fehlerquellen aus 10/2026, beide unabhängig von der Domäne.

## 1. Eine Fehlerantwort beweist nicht, dass nichts passiert ist

`initiate_offer` (Kleinanzeigen, PUT `.../negotiation/{adId}/initiate-offer`) antwortete mit
**422 `OFFER_ALREADY_MADE`** („Du hast bereits eine Anfrage für diesen Artikel gesendet") — und
trotzdem stand der mitgeschickte `messageText` kurz danach **sichtbar als Chatnachricht** im
Verlauf (Zeitstempel im Chat: 11:54, Fehler im Aufruf wenige Minuten später). Zweitbeobachtung
aus 09/2026 in `references/zusagen-widerrufen-und-seiteneffekte-verbuchen.md`: derselbe Effekt.

Konsequenzen:

- **Niemals** einen mutierenden Aufruf als „Probe" formulieren. Auch nicht, um zu prüfen „geht ein
  zweites Angebot?".
- Nach jedem Fehler den **Live-Zustand** lesen, bevor irgendetwas nachgeschoben wird. Sonst stehen
  zwei widersprüchliche Preise im Chat (live: Chattext nannte 27,70 €, gültiges Angebot war
  23,70 €) — der Verkäufer muss dann aufgeklärt werden.
- Nie einen **kleineren** Vorschlag nach einem fehlgeschlagenen Versuch nachschieben; den gleichen
  Betrag wiederholen oder es lassen.

## 2. Chat-Stand ≠ Vorgangsstand — der Vorgang kann „erledigt" aussehen und offen sein

Der sichtbare Chat zeigte „Preisvorschlag zurückgezogen"/„Anfrage abgelehnt", und der Verkäufer bat
ausdrücklich um einen neuen Preisvorschlag. Der Vorgangsstand war trotzdem blockiert bzw. bereits
neu vorhanden. **Der Chat ist die Verhandlungs-, die Vorgangs-API die Buchhaltung.**

Read-only-Rezept (Kleinanzeigen-Client, beide Calls nur lesend):

```python
conv = c.get_conversation(conv_id)
conv["paymentStateSummary"]             # ["OFFER_MADE_BY_BUYER"] = eigenes Angebot offen
conv["paymentStatusBar"]                # {"title": "Angebot ausstehend", "text": "Zahle noch nicht"}
conv["paymentAnalyticsData"]            # offerId, itemPriceInEuroCent, shippingCostInEuroCent,
                                        # buyerFeeInEuroCent, buyerTotalInEuroCent, sellerTotalInEuroCent
conv["paymentPossible"], conv["buyNowPossible"]   # beide False, solange ein Angebot schwebt
conv["sellerName"], conv["adStatus"]

ps = c.get_conversation_payment_status(conv_id)
ps["paymentStateDetails"]["paymentStateTitle"]    # "Bezahlung angefragt" = offen
                                                  # "Anfrage abgelehnt"/"-zurückgezogen" = erledigt
ps["actions"]           # [{"actionType": "CANCEL_OFFER_ACTION", "offerId": ..., "negotiationId": ...}]
                        # -> genau die Argumente für cancel_offer(negotiationId, offerId)
```

Entscheidungsregel: **offener Vorgang → nichts tun** (auf Annahme warten, kein Nachfassen).
Vorgang erledigt **und** ein neuer ist gewünscht → erst `cancel_offer`, dann neu aufsetzen.
Es gibt keinen „Resend"-Endpoint; die Plattform führt pro Anzeige genau eine Negotiation.

⚠️ Der Titel kann **zwischen zwei Reads kippen** (erst „Anfrage abgelehnt", Minuten später
„Bezahlung angefragt") — vor jeder Aktion neu lesen, nie einen Report aus dem Cache wiederholen.
Und `buyNowPossible`/`paymentPossible` der Anzeige sagen nichts über den laufenden Vorgang.

## 3. Der Nutzer handelt parallel im selben Konto

Live 10/2026: Während einer Status-Anfrage waren im Chat bereits frische **Systemzeilen**
(„Bezahlung angefragt", „Preisvorschlag erhalten", „Preisvorschlag zurückgezogen") und eine kurze
**eigene** Nachricht („Lg") — der Nutzer hatte den Vorschlag selbst neu abgeschickt. Der Agent
wollte dasselbe gerade wiederholen.

Vorgehen bei „Status"-Aufträgen auf gemeinsam bedienten Konten:

1. Alle offenen Kanäle **frisch** lesen (Chat + Vorgangsstatus + Anzeigenstatus), nicht die eigene
   Zustandsdatei.
2. Eigene/systemische Zeilen der letzten Stunden suchen → sieht man dort frische Aktivität des
   Nutzers, **nur berichten** und nichts senden.
3. Erst danach genau **eine** Aktion vorschlagen — bei verbindlichen Vorgängen nie zwei parallel,
   auch nicht „nur zum Nachfassen".

## 4. Umkehrschluss für die Meldung an den Menschen

Bei einem Status-Auftrag ist die richtige Antwortreihenfolge: (a) offener Vorgangsstand mit Betrag
und Vorgangs-ID, (b) was daraus folgt (warten / nachfassen / nichts), (c) höchstens ein Vorschlag.
Keine Rückfrage-Kaskade: wenn eine Rückfrage unbeantwortet bleibt, gilt der sichere Lesepfad
(Zustand melden, keine neuen verbindlichen Vorgänge) — der Nutzer bedient das Konto ohnehin selbst.
