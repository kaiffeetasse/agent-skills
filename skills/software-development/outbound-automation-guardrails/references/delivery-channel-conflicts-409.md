# Zustellkanal-Besitz: Konflikte, wenn zwei Konsumenten denselben Kanal abfragen

Für Automation, die über einen **eigenen Bot/Token/Kanal** sendet und empfängt, gilt eine
Voraussetzung, die leicht übersehen wird: **Du musst der einzige Konsument sein.** Zwei Poller am
selben Token → Telegram antwortet `409 Conflict: terminated by other getUpdates request`; der eine
Dienst stirbt in einer Neustartschleife, oder — schlimmer — die Nachrichten des Nutzers werden still
vom anderen Konsumenten abgeholt und deine Automation sieht sie nie.

**Iron rule:** Kein Code-Fix am Opfer, solange nicht geklärt ist, **wer sonst** den Kanal abfragt.
Erst Konsumenten identifizieren oder den Token rotieren, dann am Dienst schrauben.

## Diskriminator (messen, nicht vermuten)

1. **Eigene Instanzen ausschließen:** `systemctl show <svc> -p ActiveState,SubState,NRestarts,MainPID`
   und `ps -eo pid,lstart,etime,cmd | grep <script>` → genau EIN Prozess, kein Restart-Loop.
2. **Dienst stoppen, 20–30 s Ruhe abwarten** (die Gegenseite hält eine Lease kurz nach).
3. **Blindprobe beim gestoppten Dienst:** ~15 × `getUpdates?timeout=3` (1 s Pause), Statuscodes zählen.
   - **Weiter 409** ⇒ fremder Konsument existiert → lokal suchen (siehe unten).
   - **Nur 200** ⇒ hausgemachte Überlappung: zwei eigene Starts (Dienst + manueller Testlauf) oder
     eine Bibliotheks-Retry-Schleife, die zwei Anfragen gleichzeitig offen hält.
4. **Fundstellen abarbeiten:**
   - `sudo ss -tnp | grep 149.154` — welche PIDs halten Telegram-Verbindungen (mehrere
     `hermes gateway run`-Prozesse sind normal, meist mit *anderen* Tokens)
   - `sudo tr '\0' '\n' < /proc/<pid>/environ | grep -iE 'telegram|bot_token'`
   - `docker inspect <container> --format '{{range .Config.Env}}{{println .}}{{end}}' | grep -i token`
   - `grep -rl <bot-id> ~/.hermes/scripts /etc/systemd/system ~/.config/systemd/user` — **alte
     Skriptversionen** (`*_v4.py` o. ä.) halten oft noch denselben Token
   - Cronjobs (`cronjob list`, `crontab -l`) und User-Units (`ls ~/.config/systemd/user`)
5. **Token rotieren** (@BotFather `/mybots` → Bot → API Token → Revoke), neuen Token in die `.env`,
   Dienst neu starten → jede Alt-Instanz ist automatisch ungültig. Schneller und sicherer als jede
   weitere Suche; der einzige wirklich endgültige Fix.
6. **Wenn die Funktion aktuell nicht gebraucht wird:** Dienst `stop` **und** `disable`, Nutzer
   informieren (mit dem Ein-Zeiler für später). Ein halb funktionierender Verbraucher, der
   Nachrichten stiehlt, ist schlechter als kein Verbraucher.

## Single-Flight-Polling (gegen Overlap der Bibliothek)

```python
offset = None
while True:
    try:
        updates = await app.bot.get_updates(offset=offset, timeout=10,
                                           allowed_updates=Update.ALL_TYPES)
    except Conflict:
        await app.bot.delete_webhook(drop_pending_updates=True)
        offset = None
        await asyncio.sleep(6)
        continue
    for u in updates:
        offset = u.update_id + 1
        await app.process_update(u)
    await asyncio.sleep(1)          # kleine Pause gegen Lease-Überlappung
```

Ergebnis im Fall: stabil (3× HTTP 200, 2× 409 in 90 s, kein Crash) statt Restart-Loop. Ein
`drop_pending_updates=True`/Queue-Reset beim Start räumt Altlasten weg, ersetzt aber dieses Muster nicht.

## Pitfalls beim Dienst-Handling

- `pgrep -f bot_v` / `pkill -f bot_v` matcht die **eigene Kommandozeile** und killt die aufrufende
  Shell (`exit -9`). Eindeutiges Muster (`pgrep -f 'bot_v[0-9]'`) oder separates Kill-Skript nutzen.
- Dienst muss mit dem passenden Interpreter/venv starten (eigenes venv im `ExecStart`), sonst
  `ModuleNotFoundError` — was wie ein Token-Problem aussieht.
- Nach jedem Start **Belege sammeln**: `journalctl -u <svc> --since "-1min"` + Erfolgs-/Fehlerzähler.
  `active` ist kein Beweis für „pollt und verarbeitet".
- Token nie hardcoden; aus `~/.secrets/<bot>.env` lesen. Verlorene Tokens lassen sich aus
  Session-DBs/Backups rekonstruieren und per `getMe` verifizieren.
