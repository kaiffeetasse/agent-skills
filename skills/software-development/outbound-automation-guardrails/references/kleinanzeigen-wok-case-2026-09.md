# Fallstudien: Kleinanzeigen-Wok-Verhandlung (09/2026)

Echte Vorfälle aus einem Cron-Watchdog, der Wok-Verhandlungen per LLM führt. Jeder Fall: Symptom →
Ursache → Fix → Gegenprobe. Die Fälle sind als Buchstaben E1–E10 in der Fehlerhistorie des
Domänen-Skills (`kleinanzeigen-toolbox-workflow`, `references/fehlerhistorie-2026-09.md`) verlinkt;
hier stehen die **generalisierten** Lehren.

## Fall 1 — Vierfach dieselbe Absage (Idempotenz)

**Symptom:** Verkäufer schrieb viermal, der Wok habe einen flachen Boden (er koche selbst auf
Ceranfeld). Der Bot antwortete viermal mit derselben statischen Absage. Reaktion: „Was ist los mit
dir."

**Ursache:** Es waren vier **verschiedene** Verkäufer-Nachrichten-IDs, und nur die aktuelle ID wurde
als beantwortet verbucht. Der Text war für diese Konversation schon einmal gesendet worden, das
wurde nirgends geprüft. Zusätzlich lief der Absage-Zweig **vor** der eigentlichen Bewertung.

**Fix:** Zweiter Idempotenz-Schlüssel (`sha256` des normalisierten Textes, pro Konversation) und
„Absage höchstens einmal". Generalisierung: Invariante 1.

**Gegenprobe:** Regressionstest „neue Eingangs-ID + identischer Antworttext → trotzdem nur eine
Nachricht".

## Fall 2 — Rückwärts-Verhandlung nach der Zusage (Betrag aus falscher Quelle)

**Symptom:** Vereinbart waren „15 € plus Versand" (zwei eigene Nachrichten bestätigten es). Bei der
Fixierung schrieb der Bot „dann machen wir es bei **12 €** fest". Der Verkäufer: „Nun schon wieder
handeln? Dann lassen wir es gerne sein."

**Ursache:** Der Preisleser erkannte Zusage-Formulierungen („Ich nehme den Wok für 15 €", „15 € plus
Versand sind so in Ordnung") **nicht** und fiel auf den Startwert der Zielliste zurück (12 €). Der
Zusage-Zweig überschrieb den echten Wert bei jedem Lauf erneut.

**Fix:** Eigener Zusagepreis-Leser: erste Preisangabe je Zusage-Nachricht, Grenzformulierungen wie
„knapp unter 25 €" ignorieren, über Nachrichten das Maximum; Zusage- und Fixierungszweig bilden
immer das Maximum (nie senken). Generalisierung: Invariante 6.

**Reparatur am Kunden:** Ehrliche Korrektur senden („die 12 € waren ein Versehen, es bleibt bei
15 € plus Versand"), Daten im Zustand korrigieren, Skill + Fehlerhistorie ergänzen.

## Fall 3 — Eigenmächtige Rücknahme einer fertigen Zusage (schwerster Fall)

**Symptom:** Der Job fixierte automatisch Kandidat A (15 € + Versand ≈ 22 €) und sagte **im selben
Moment** Kandidat B ab („ich habe mich für eine andere Pfanne entschieden") — obwohl B fertig
zugesagt hatte, seine Zahlungsdaten schon geschickt hatte (20 € + 1,09 € Gebühr = 21,09 €) und
A noch nicht einmal bestätigt war.

**Ursachen (drei gleichzeitig):**

1. Für den Vergleich wurden **Schätzwerte** benutzt statt der im Chat genannten Gesamtbeträge
   (B: 27 € geschätzt statt 21,09 €; A: 19 € statt 22 €, weil der falsche 12-€-Preis noch im
   Zustand stand).
2. Es gab **keine Sperre** gegen das Aufgeben einer fertigen Zusage.
3. Die 24-h-Wartefrist lief genau in dieser Minute ab.

**Fix:** (a) Vergleich nutzt die im Chat **genannten** Gesamtbeträge; nennt die Gegenseite nur den
Artikelpreis („15 € plus Versand"), wird gerechnet (Artikel + Versand + Gebühr). (b) Fertige Zusage
wird **nie** eigenmächtig abgesagt: bei mehreren Zusagen Eskalation an den Menschen; automatische
Rücknahme nur mit Freigabe (`WOK_AUTO_CANCEL_OTHERS=1`) **und** klarem Sieger (Score-Marge **und**
nicht teurer). Generalisierung: Invarianten 4 und 5.

**Reparatur am Kunden:** Rücknahme-Zustand aufheben, Zusage beim Verkäufer ehrlich wiederherstellen
(Fehler eingestehen, vereinbarten Betrag bestätigen), beide Kandidaten offen halten, Vergleich dem
Menschen überlassen.

## Fall 4 — Doppelte Eskalation an den Nutzer (Meldung ohne Einmal-Sperre)

**Symptom:** Nach dem Umbau meldete der Job denselben unklaren Fall bei **jedem** Lauf erneut an
Telegram — also alle 5 Minuten.

**Ursachen:**

1. Der LLM-Zweig `needs_human` hatte keine Einmal-Sperre (nur der Beweislage-Zweig hatte eine).
2. **Alt-Zustände ohne die neuen Gate-Felder:** Für Fälle, die vor dem Am-Zug-Umbau beantwortet
   wurden, war `awaiting_reply_for` leer → das alte Ereignis galt bei jedem Lauf als neu.

**Fix:** `escalated_for = <event_id>` auch im LLM-Zweig, und wenn dieselbe Ursache schon eskaliert
ist: still bleiben und **keinen** weiteren Modellaufruf machen (spart Kosten). Dazu eine einmalige
Migration beim Laden: `replied` gefüllt + `awaiting_reply_for` leer → zuletzt beantworteten Eintrag
übernehmen. Generalisierung: Invarianten 3 und 7.

**Merksatz:** Jede wiederkehrende Meldung braucht eine Sperre, die an der *Ursache* hängt
(Ereignis-ID) — nicht an einem Zeitstempel und nicht an nichts.

## Fall 5 — Doppelnachricht durch Fallback

**Symptom:** Das Modell antwortete „keine Antwort nötig", der Regel-Fallback schrieb trotzdem.

**Fix:** `needs_reply=false` beendet den Vorgang explizit, ohne Ersatztext. Eine endgültige Absage
wird dagegen **immer** höflich verabschiedet (`action=close`) — der Unterschied gehört in den
Prompt-Vertrag. Generalisierung: Invariante 8.

## Fall 6 — Teure Modellaufrufe: Cache und Beweisbasis (Vision)

**Symptom/Lerne:**

- Fremde Bilder wurden bewertet, weil die ganze HTML-Seite nach Bild-URLs durchsucht wurde statt nur
  der Galerie des Objekts.
- Das Modell verwechselte die **immer gewölbte Wandung** eines Woks mit der **Auflagefläche** und
  urteilte „gewölbt, ungeeignet", obwohl der Boden flach war.
- Zwei Urteile kamen als abgeschnittenes JSON zurück.
- Ein hartes Urteil stützte sich auf ein **einziges** Foto.

**Fix:** Nur den Galerie-Bereich parsen; Prompt ausschließlich auf die **Kontaktfläche** richten und
`view` + `bottom_visible` erzwingen („nicht sichtbar" ⇒ `unklar`, niemals „gewölbt");
Reasoning-Budget abschalten + Token-Limit erhöhen; Beweisbasis (Anzahl auswertbarer Fotos) im Urteil
mitführen; Ergebnis-Cache `hash(Bild) + Modell + Prompt-Version`, nur offene Fälle bewerten.

## Prüfmethodik, die diese Fälle gefunden hat

- Ein **Replay-Skript** spielt echte Chat-Transkripte gegen die aktuelle Logik und prüft die
  **effektive** Wirkung (Modell → Guardrails → Code-Fallback). Vorher prüfte es nur die LLM-Schicht
  und meldete Abweichungen, die im echten Ablauf gar nicht auftraten (und umgekehrt).
- **Offline-Fixture-Tests** mit gefälschtem Transport zählen Sendungen; jeder echte Vorfall wurde zu
  einem Test.
- Zwei Fehler wurden **erst durch die Tests** gefunden: die nicht zug-bewusste
  „schon beantwortet"-Abkürzung (blockierte das erlaubte Nachfassen) und ein Grenzfall in der
  Preisleser-Heuristik.
