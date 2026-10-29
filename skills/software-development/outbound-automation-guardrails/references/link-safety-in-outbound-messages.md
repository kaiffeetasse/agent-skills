# Link-Sicherheit in ausgehenden Nachrichten

Klasse von Fehlern: Die Nachricht geht raus (API sagt „ok"), aber der **Inhalt** ist beim Empfänger
kaputt — er klickt und landet falsch. Das ist ein Ausgabe-Fehler der Automation, nicht des Dienstes.

## Fall (2026-10-10): zerschnittene URL durch Markdown, Nutzer landet bei Google

Ein Anmelde-Link (`https://click.edeka.de/f/a/<opaque>~~/AAAHahA~/<opaque>…`) wurde in einer
Markdown-formatierten Telegram-Nachricht verschickt. Der Link enthält `~~` und `_` — Telegram parst
die als Durchstreichen/Kursiv und schneidet die URL. Beim Empfänger kam eine unvollständige URL an;
der Klick-Tracker quittierte den kaputten Aufruf mit einem Fallback-Redirect
(`302 → https://www.google.com/?!=!`). Nutzer-Rückmeldung: „der Link leitet auf google weiter?!"
→ sieht wie ein Angriff aus, ist aber ein Formatierungsfehler des Absenders.

## Regeln

1. **Vor dem Senden selbst auflösen.** Link mit `requests.get(url, allow_redirects=True)` prüfen und
   die Kette (Statuscodes + Ziel-Host) loggen. Steht dort schon ein unbrauchbares Ziel (Google,
   Login-Wall, `localhost`), ist die URL falsch zusammengesetzt — nicht senden.
2. **URLs mit Markdown-Metazeichen (`~~`, `_`, `*`, `[`, `]`) nie in eine Markdown-Nachricht.**
   Entweder `sendMessage` **ohne** `parse_mode` (Telegram verlinkt Klartext automatisch, ohne zu
   parsen) oder als Codeblock/Datei.
3. **Einmal-Links nicht „zur Sicherheit" selbst anklicken.** Bei Tokens/Links, die nur einmal gelten
   (Login-, Reset-, Einladungslinks), zerstört eine eigene Gegenprobe den Link. Dann lieber den
   intakten Link zustellen und dem Nutzer sagen, wo er ihn anklicken soll (z. B. „in der Mail, nicht
   im Chat").
4. **Erwartungshaltung des Nutzers mitliefern:** Gültigkeitsdauer des Links (z. B. 15 Minuten) und
   was passiert, wenn er abgelaufen ist (Aktion im Client neu auslösen).
5. **Wenn der Nutzer „geht nicht" meldet: zuerst den eigenen Ausgabekanal prüfen** (Formatierung,
   Encoding, Truncation), nicht den Dienst beschuldigen. Der Beweis kommt aus der Auflösungskette
   des Links, nicht aus einer Vermutung.

## Gegenprobe (im Erfolgsfall dokumentieren)

Intakter Link der Quelle (z. B. aus der E-Mail gelesen, nicht abgetippt) → `302` auf den erwarteten
Ziel-Host (im Fall: `login.edeka/actions/start-login-edeka-app?...redirect_uri=edeka://main/auth/redirect`,
also Deep-Link in die App. Ein Deep-Link-Ziel bedeutet zusätzlich: der Link funktioniert nur auf dem
Gerät mit installierter App.
