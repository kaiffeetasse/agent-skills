# Verifikation von Sends, die keinen Response-Body liefern

Gilt für jede Automatik, die Nachrichten an Dritte schickt — nicht nur für Marktplätze.

## Das Problem

Manche Sende-Endpunkte antworten mit `None`/leerem Body, **obwohl** die Nachricht zugestellt wurde.
Beobachtet 09/2026: `send_message_in_conversation(conv_id, text)` (Nachricht in einem bestehenden Chat)
gibt `None` zurück; derselbe Chat enthielt danach nachweislich den gesendeten Volltext.

Wer den Response als Erfolgssignal behandelt, macht daraus zwei Fehler:

1. **Falsch-negativ:** „nicht gesendet" wird gemeldet, obwohl es raus ist → Eskalation/Alarm ohne Grund.
2. **Doppelnachricht:** der Retry schickt denselben Text ein zweites Mal an einen echten Menschen.

## Die Regel

> Ein leerer/fehlender Response ist **kein** Fehlerbeweis. Erfolg wird am **Zustand der Gegenseite**
> verifiziert, nicht am Rückgabewert des Sendecalls.

## Verifikationsmuster (read-back)

1. Vor dem Send den **Threadzustand** erfassen: Nachrichtenzahl (rekursiv alle `text`-Knoten zählen,
   nicht nach fester Pfadtiefe) und/oder die letzte Nachrichten-ID.
2. Senden — den Call **nicht** in Retry-Schleifen hängen, solange das Ergebnis unbekannt ist.
3. Thread erneut laden und prüfen: Zahl **+1**, eigener Volltext vorhanden, eigene Nachricht als letzte.
4. Erst danach `ok=True` in der Ergebnisdatei / der Outbound-Historie verbuchen.
5. Schlägt der Read-back **fehl** (Zahl unverändert, Text fehlt), dann — und nur dann — ist es ein echter
   Fehler: dokumentieren und die Ursache melden, nicht blind wiederholen.

## Kopplung an die Freigabe-Invariante

- Bleibt eine **Freigabeanfrage an den Menschen unbeantwortet** (Timeout, keine Rückmeldung), wird
  **nicht committet**: kein Geld, keine verbindliche Zusage, keine Bestellung. Der nicht-mutierende Pfad
  läuft weiter (Rückfrage bei der Gegenseite, Umfang/Betrag/Zahlungsweg klären); committet wird erst nach
  ausdrücklicher Freigabe. Der sichere Default bei Schweigen ist die unverbindliche Variante.
- Das ist die read-back-Variante derselben Idee: **Zustand von außen prüfen, nie aus dem eigenen
  Sendeversuch ableiten.**

## Pitfalls

- Nicht „gesendet" behaupten und nicht „fehlgeschlagen" behaupten, solange kein Read-back vorliegt — beides
  ist geraten.
- Nachrichten-Zählung nicht über die Konversationsliste (`get_conversations`) prüfen: die liefert
  Summaries ohne Threadinhalt. Immer die Einzelkonversation laden.
- Bei mehrteiligen Texten nicht nur „Anzahl stimmt" prüfen, sondern den **eigenen Volltext** im Verlauf
  lesen — sonst zählt eine System-/Automatiknachricht als Bestätigung.
