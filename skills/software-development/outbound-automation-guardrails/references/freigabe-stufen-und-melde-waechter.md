# Freigabe-Stufen und Melde-Wächter

Ergänzung zu den Invarianten in `SKILL.md`: Automatik, die **Dritten schreibt**, wird nicht von
selbst scharf. Solange der Mensch den nächsten Schritt nicht ausdrücklich freigegeben hat (Frage
bleibt unbeantwortet, er ist offline), gilt die **kleinste wirksame Stufe** — gewählt, nicht geraten.

| Stufe | Erlaubt | Wann |
|---|---|---|
| 1 Melden | nur lesen, neue Ereignisse genau einmal melden | Default, immer zulässig |
| 2 Vorschlagen | Nachricht entwerfen, der Mensch sendet | keine Auto-Freigabe |
| 3 Verhandeln | automatische Antworten im vereinbarten Rahmen | ausdrückliche Freigabe |
| 4 Abschließen | verbindliche Angebote/Käufe | Einzelfreigabe, nie parallel |

## Regeln

* **Ein pausiertes Automatik-Skript nie „einfach wieder anwerfen".** Erst prüfen, ob die Kriterien
  noch gelten und die Freigabe vorliegt, dann `cronjob action=resume`. Andernfalls handelt der Job
  nach Regeln, die der Mensch gerade geändert oder gelöscht hat.
* **Übergang 1 → 3 im Klartext benennen** („auf ein Wort schalte ich um"), damit der Mensch weiß,
  dass gerade nichts von selbst passiert. Real 10/2026: Nach zwei Erstanfragen auf dem Marktplatz kam
  keine Antwort auf die Frage „automatisch weiterverhandeln?" → eingerichtet wurde Stufe 1.
* **Ein Melde-Wächter liest nur.** Er darf den Kanal nicht verändern, keine Antwort entwerfen und
  nichts senden. Meldung je Ereignis-ID genau einmal (State-Feld „reported"/`replied[]`, **nicht**
  Zeitstempel), leerer stdout = still.
* **Lesefehler vor dem Alarm wiederholen.** Transiente Netzfehler sind kein Befund — real:
  `_ssl.c:999: The handshake operation timed out` beim Laden eines Chats. 3 Versuche mit Backoff,
  erst danach melden; sonst erzeugt der Wächter Fehlalarme.
* **Endgültige Lesefehler müssen sichtbar rausgehen.** Ein still verschluckter Fehler lässt den
  Menschen „Ruhe" annehmen, obwohl der Wächter kaputt ist.

## Muster (bewährt, 10/2026)

```python
# no_agent-Cron, every 10m, deliver: telegram:<chat_id>
for item in WATCHED:
    data = _fetch(item, attempts=3)            # Retry mit Backoff 3s/7s/11s
    inbound = [m for m in data["messages"]
               if m.get("boundness") == "INBOUND"      # Feldname je API prüfen
               and m.get("type") == "MESSAGE"]         # Systemereignisse aussortieren
    last = inbound[-1] if inbound else None
    if not last or last["messageId"] in state.get(item, []):
        continue
    out.append(...); state[item].append(last["messageId"])   # genau einmal melden
if out: print(REPORT)          # nicht leer -> Zustellung
elif errors: print(ERRORS)     # endgültige Lesefehler sichtbar machen
# nichts von beidem -> still
```

Merksatz: Der Wächter darf **nur** beobachten — die Entscheidung, ihn auf Stufe 3 zu heben, trifft
der Mensch, nie die Automatik selbst.
