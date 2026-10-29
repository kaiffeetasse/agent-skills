---
name: outbound-automation-guardrails
description: "Use when automation sends messages or commits actions."
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Automatisierung, Watchdog, LLM-Guardrails, Idempotenz, Cron]
    related_skills: [kleinanzeigen-negotiation, cronjob-silent-output, kleinanzeigen-toolbox-workflow]
---

# Outbound Automation Guardrails

Invarianten für Automatik, die **mit Dritten kommuniziert** und dabei **unumkehrbare Dinge tut**
(Nachrichten senden, Angebote abgeben, Zusagen machen, Bestellungen auslösen) oder **wiederkehrend
an den Nutzer meldet**.

## When to Use

- Ein Skript/Agent sendet auf einem Zeitplan Nachrichten an Dritte (Marktplatz-Verhandlung,
  Support-Chat-Autoresponder, Kunden-Follow-ups, Bot-zu-Bot).
- Ein Job trifft **verbindliche** Entscheidungen (Preis zusagen, Kauf auslösen, Vertrag abschließen).
- Ein Job meldet sich wiederholt beim Nutzer (Watchdogs, Cron-Benachrichtigungen).
- Ein LLM entscheidet im Loop und der Code muss es begrenzen.

Nicht die Domäne ist hier das Thema, sondern die Sicherheitsmechanik — Domänenwissen gehört in das
jeweilige Fach-Skill (z. B. `kleinanzeigen-negotiation`).

## Die neun Invarianten

1. **Idempotenz braucht ZWEI Schlüssel.** `replied[event_id]` verhindert die Antwort auf dasselbe
   Ereignis; `sent_fingerprints[normalisierter_text]` verhindert, dass derselbe Text bei *neuen*
   Ereignissen erneut rausgeht. Beide Prüfungen stehen **vor** dem mutierenden Aufruf.
2. **Am-Zug-Regel (Turn-Taking).** Es wird nur gesendet, wenn die Gegenseite seit unserem letzten
   Send **neu** geschrieben hat. Ohne neue Nachricht ist genau **EIN** Nachfassen erlaubt — und erst
   nach einer Funkstille (Standard 24 h); danach nie wieder zum selben Ereignis. Zusätzlich eine
   Mindestpause zwischen zwei Sendungen.
   Vor jedem Send `turn_state(...)`, nach jedem Send `record_outbound(...)` — auf **allen**
   Sendestellen, nicht nur auf dem Hauptpfad.
3. **Wiederkehrende Meldungen an den Menschen brauchen eine Einmal-Sperre**, die an der **Ursache**
   hängt (`escalated_for = <event_id>`), nicht an einem Zeitstempel. Sonst wandert der
   Doppel-Nachrichten-Fehler nur vom Kanal des Dritten in den Benachrichtigungskanal.
4. **Eine fertige Zusage wird nie eigenmächtig zurückgenommen.** Wenn das Aufgeben einer Zusage
   nötig scheint, wird **eskaliert** und der Mensch entscheidet. Automatische Rücknahme nur mit
   ausdrücklicher Freigabe *und* klarem Vorteil (Marge **und** nicht teurer).
5. **Entscheide mit den autoritativen Fakten aus dem Kanal**, nicht mit lokalen Schätzungen. Was die
   Gegenseite tatsächlich genannt hat („das wären 21,09 €"), schlägt jede Versand-/Kostenschätzung.
6. **Der bestätigte Betrag kommt aus unserer eigenen Zusage-Nachricht**, nie aus einer
   Default-/Zielliste. Ein einmal zugesagter Betrag wird nie gesenkt (Maximum bilden).
7. **Neue Zustandsfelder brauchen eine Migration.** Führt man Gate-Felder ein, müssen bestehende
   Datensätze einmalig nachgezogen werden — sonst ist das Gate für alle Altfälle ein No-Op und jeder
   Lauf hält das alte Ereignis für neu.
8. **Das LLM entscheidet, der Code begrenzt.** Modellvorschläge laufen durch deterministische
   Guardrails; bei Modellausfall gibt es nur weiche/sichere Aktionen, **niemals** eine verbindliche
   Zusage. Ausdrückliches „keine Antwort nötig" des Modells darf nicht in einen Regel-Fallback
   laufen (klassische Doppelnachricht).
9. **Bei echter Unklarheit eskalieren statt raten** (widersprüchliche Belege, fehlender Zustand,
   unklare Herkunft einer Nachricht). Fehlt ein Pflichtfeld in der Modellantwort, gilt der Fall als
   unsicher.

## Zustandsfelder (Referenz)

```
replied[event_id]                 # Ereignis beantwortet
sent_fingerprints[text_hash]      # Text bereits gesendet
last_outbound_at                  # Zeitpunkt unseres letzten Sends
awaiting_reply_for                # Ereignis-ID, auf die wir zuletzt geantwortet haben
awaiting_since                    # seit wann wir auf Antwort warten
followup_for                      # Ereignis-ID, für die das einmalige Nachfassen raus ist
escalated_for[event_id]           # Eskalation an den Menschen bereits gemeldet
committed_amount / agreed_total   # der zugesagte Betrag (niemals senken)
```

Kopiervorlage: `templates/turn_gate.py`.

## Reihenfolge der Prüfungen (wichtig)

Beim Senden gilt diese Ordnung — die Reihenfolge ist selbst eine Fehlerquelle:

1. **Zug** (`turn_state`) — darf überhaupt gesendet werden?
2. **Idempotenz** — identischer Text / dasselbe Ereignis schon bedient?
3. **Ereignis** (`event_id` schon beantwortet **und kein fälliges Nachfassen**) → überspringen.
4. Guardrails auf Inhalt (Grenzen, verbotene Inhalte, erfundene Daten).
5. Senden, danach `record_outbound(...)`.

Punkt 3 muss **zug-bewusst** sein: eine reine „schon beantwortet"-Abkürzung blockiert sonst das
erlaubte Nachfassen — real aufgetreten, nur durch einen Test gefunden.

## Kostenschutz bei teuren Modellaufrufen im Loop

- **Ergebnis am Artefakt cachen:** Schlüssel = `hash(Inhalt) + Modell + Prompt-Version`; Treffer
  kostet nichts. Prompt-Version erhöhen invalidiert den Cache genau einmal kontrolliert.
- **Nur handlungsrelevante Datensätze bewerten** (offene/aktive Fälle), abgeschlossene nicht.
- **Antwort-Version mitspeichern:** ein Urteil aus einer älteren Prompt-Fassung verwerfen, sonst
  mischen sich zwei Vokabulare (z. B. „gewölbt" alt vs. „deutlich_gewoelbt" neu) und Entscheidungen
  werden still falsch.
- **Strukturierte Extraktion:** Denk-/Reasoning-Budget abschalten, wo unterstützt, und das
  Token-Limit hochsetzen — sonst kommt JSON abgeschnitten zurück.

## Verifikation

- **Replay echter Transkripte** gegen die aktuelle Logik: Erwartungen auf die **effektive**
  Entscheidung beziehen (Modell → Guardrails → Code-Fallback) — nicht nur auf eine Schicht. Sonst
  meldet die Prüfung „send=False", obwohl der Fallback sehr wohl sendet.
- **Offline-Fixture-Tests** mit gefälschtem Transport; gezählt wird, nicht geschaut:
  höchstens eine Nachricht, keine zweite bei schweigender Gegenseite, Nachfassen genau einmal nach
  der Funkstille, keine automatische Rücknahme, keine wiederholte Eskalation.
- **Uhr/Zustände in Tests altern.** Zwei Läufe in derselben Sekunde treffen Sperren wie „nicht im
  selben Lauf senden" und produzieren Scheinfehler. Zeitstempel im Test künstlich zurücksetzen.
- Jeden echten Vorfall als **Fall in der Fehlerhistorie + Regressionstest** festhalten, mit Ursache,
  Fix und Gegenprobe — nie nur im Einzelfall beheben.

## Pitfalls

- **Ein Guard nur auf dem Hauptpfad leckt.** Alle Sendestellen prüfen: Antwort, Absage, Nachfassen,
  Ausspielen/Playoff, Fixierung, Rücknahme, Benachrichtigung.
- **Fingerprint blockt zurecht identische Texte** — deshalb muss das Modell Nachfassen *neu
  formulieren*; ein Regel-Fallback liefert sonst wortgleich und wird blockiert (im Test einplanen).
- **Berichte an den Menschen sind auch Nachrichten:** Einmal-Sperre, sonst 5-Minuten-Spam.
- **Bild-/LLM-Heuristiken brauchen präzise Fragen:** Bei Produkten den *relevanten Teil* erfragen
  (Auflagefläche statt Gesamtform), Medien nur aus dem eigenen Bereich des Objekts ziehen (Galerie,
  nicht die ganze Seite) und die **Beweisbasis** mitführen („Urteil beruht auf 1 Foto").
- **Verbindliche Nachrichten nie doppelt:** Eine Zusage/ein Abschluss darf nicht zweimal
  rausgehen, auch wenn das Modell zweimal formuliert.

## References

- `references/kleinanzeigen-wok-case-2026-09.md` — Fallstudien mit Ursachen, Fixes und Gegenproben
  (vierfach wiederholte Absage, Rückwärts-Verhandlung nach Zusage, eigenmächtige Rücknahme einer
  fertigen Zusage, doppelte Eskalationen).
- `templates/turn_gate.py` — kopierbare Implementierung von `turn_state()` / `record_outbound()`.
