# Terminal-Aktionen gehören nicht ins Modell — Fallstudie Sprachagent (2026-10-08)

Fall aus einem **eingehenden KI-Anrufbeantworter** (OpenAI Realtime + pyVoIP-SIP).
Die Lehren sind kanalunabhängig und gelten für jeden Agenten, der eine unumkehrbare
oder zustandsbeendende Aktion ausführt (Senden, Auflegen, Festschreiben, Session-Ende).

## Der Fall

Ein Anrufbeantworter-Agent bekam — wie beim Auswärts-Telefonieren bewährt — ein
Werkzeug `auflegen` ("beende den Anruf") in den Werkzeugkatalog.

Beobachtungen aus den Logs (jeweils reproduziert):

| Beobachtung | Log-Beweis |
|---|---|
| Agent **sagte**, er lege auf — tat es aber nicht | `KI: "… Ich verabschiede mich, aufgelegt."` — **kein** `TOOL-Aufruf: auflegen`; Leitung blieb 24 s offen, bis der Mensch selbst auflegte |
| Agent legte **mitten in einer offenen Frage** auf | erst Anrufer-Frage, dann `AUFLEGEN (Werkzeug auflegen)` — die Frage blieb unbeantwortet (2× an einem Nachmittag) |
| Doppelter Werkzeugaufruf | `TOOL-Aufruf #2: auflegen` und `#3: auflegen` in einem Gespräch |

## Ursache

1. **„Fertig?" ist eine Dialog-Bewertung** — genau die Frage, die ein LLM nicht zuverlässig
   und nicht zur richtigen Zeit beantwortet. Mit einem Aktions-Werkzeug bekommt es die
   Erlaubnis, das Gespräch abzuwürgen, sobald es *glaubt*, fertig zu sein (auch während der
   Gegenpart noch eine Frage offen hat).
2. **Gesprochene Absicht ≠ ausgeführte Aktion.** Der Agent verbalisiert den Abschluss
   („ich lege jetzt auf"), der Werkzeugaufruf unterbleibt. Wer den Text/die Ansage als
   Beleg nimmt, hält einen offenen Kanal für geschlossen.

## Gegenmittel (verifiziert)

- **Terminal-Aktion deterministisch aus Code-Bedingungen ableiten**, nicht vom Modell
  anfordern: Ende des Anrufs = Gegenpart hat aufgelegt (`state == ENDED`) **oder**
  Stille `HANGUP_SILENCE_S` (12 s) **oder** Zeitlimit (`MAX_CALL_S`).
- **Gestaffelte Stille:** enthielt die letzte Agenten-Antwort einen Abschied
  („wiederhören", „tschüss", „ciao", „bis dann"), reicht eine kurze Schwelle (5 s);
  sonst die lange (12 s). `last_act` bei `speech_started` (Gegenpart) und
  `response.created` / `response.done` (Agent) aktualisieren — sonst wird ein
  nachdenkender Gegenpart abgeschnitten.
- **Werkzeuge mit harmlosem Fehlgebrauch bevorzugen.** Lesende Werkzeuge (Suche, Abfrage)
  können im Gespräch bleiben; Aktionen, die den Kanal beenden oder Zusagen erzeugen,
  gehören in Code-Bedingungen.
- **Prompt-Verbot zusätzlich im Code absichern.** Auch mit klarem Verbot
  („sage nie, dass du auflegst, ohne das Werkzeug aufzurufen") hielt sich das kleine
  Realtime-Modell nicht daran; ebenso rutschten verbotene Floskeln („Alles klar",
  „ich schaue kurz nach") weiter durch. Kleine Modelle befolgen Verbote nur teilweise —
  die Regel in den Code, nicht in die Hoffnung.

## Verifikationslehren (Harness)

- **Der Simulator muss die Zeitachse der Realität haben.** Ein Mock-Call, dessen
  „Gegenpart" ohne **Pausen** durchspricht, lässt die Voice-Activity-Erkennung jede
  Agenten-Antwort abbrechen — das Ergebnis ist ein Artefakt der Attrappe, nicht des
  Systems. Erst der Vergleich mit realistischen Pausen ergab die echten Fehler.
- **Pro Fixture genau ein Ereignis.** Enthielt eine TTS-Datei zwei Aussagen, wurde die
  zweite doppelt verarbeitet → Fehldiagnose „Agent kündigt Werkzeuge doppelt an".
- **Behauptung gegen Log-Beweis prüfen:** für jede zugesagte Aktion die Ereigniszeile
  suchen (Werkzeugaufruf, Auflege-Grund, Sendezeile), nicht den gesprochenen Abschied
  oder die Zusammenfassung des Modells.
- **Ohne echten Kanal testbar machen:** Der Transportweg (hier SIP) ließ sich ohne
  Fremdanrufer prüfen, indem eine zweite Instanz dieselbe Nebenstelle anrief — Persona,
  Werkzeuge, Aufnahme und Kanalende sind damit vollständig belegbar.
