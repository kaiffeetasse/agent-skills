# Zusagen zurücknehmen & Seiteneffekte korrekt verbuchen (verifiziert 2026-10-11)

Zwei Lektionen aus Automatisierungen, die **verbindliche Zusagen** verschicken (Kaufangebot,
Kaufzusage, Bestellung). Beide betreffen dieselbe Frage: ab wann darf sich die Automation
als „erledigt" betrachten, und wie wird eine Zusage wieder los, wenn der Plan des Nutzers
sich ändert?

## A. Eine verbindliche Zusage muss widerrufbar sein — und der Widerruf verifiziert werden

Fall: Ein plattformgebundenes Kaufangebot („Sicher bezahlen") war bereits beim Verkäufer.
Der Nutzer meldete kurz darauf „könnte auch heute abholen kommen" — also ändert sich die
Abmachung. Ein offenes Angebot ist **Zahlungspflicht bei Annahme**, deshalb gilt:

1. **Vorher den Verlauf lesen** (hat die Gegenseite schon geantwortet/angenommen?). Keine
   Antwort = gefahrlos umstellbar.
2. **Erst zurückziehen, dann neu verhandeln** — nicht beides parallel stehen lassen.
3. **Rückgabe der API ist kein Beweis.** Der Widerruf wurde erst als erledigt betrachtet,
   nachdem ihn *zwei* unabhängige Ansichten zeigten: die Systemnachricht im Chat-Verlauf
   („Anfrage zurückgezogen") und das Zahlungsstatus-Objekt der Gegenseite-Ansicht
   (`paymentStateTitle`). Merksatz: nach einem Widerruf immer beim Gegenüber/Status
   nachlesen, nicht beim eigenen Call.
4. **Neue Abmachung im SELBEN Thread** (bestehende Conversation-ID) — ein zweiter Thread
   zur selben Sache erzeugt Doppelnachrichten, die die Regeln dieses Nutzers verbieten.
5. **Zahlungsstatus-Titel als Zustandsmaschine** dokumentieren, z. B.: „Zahlung angefragt"
   = eigenes verbindliches Angebot offen → „Anfrage zurückgezogen" = keine Verpflichtung
   mehr. Wer diese Titel kennt, kann den Automationszustand ohne DB prüfen.
6. **Kosten ehrlich benennen:** nicht den Angebotspreis nennen, sondern das Total inkl.
   Versand + Käuferschutzgebühr aus dem Fee-Objekt (real: 70 € + 7,69 € + 3,65 € = 81,34 €).

## B. Erfolg eines Seiteneffekts erst nach Bestätigung persistieren

Fall: ein Job trug einen versendeten Artikel in seine State-Liste ein, **bevor** die
Telegram-Zustellung geprüft war (`requests.post(...)` ohne Response-Auswertung). Ein
fehlgeschlagener Versand galt damit dauerhaft als „gesendet" — die Arbeit war verloren,
ohne dass irgendwo ein Fehler auftauchte. Patch:

```python
try:
    r = requests.post(url, json=payload)
    ok = bool(r.json().get("ok"))       # nur echte Zustellung ist Erfolg
except Exception:
    ok = False
if not ok:
    continue                            # NICHT als gesendet merken -> nächster Lauf retry
state.append(item_id)
```

Verallgemeinert:
- **State erst nach bestätigtem Seiteneffekt schreiben** — „fire and forget + Buchhaltung"
  ist die häufigste Ursache für still verlorene Arbeit.
- Für Zustands-Automationen heißt das auch: eine **Zählung über die State-Datei**
  (vorher/nachher) ist nur so ehrlich wie diese Regel. Ist sie verletzt, lügt der Zähler.
- Zwei Lügen, die in „stillen" Automationsjobs leicht übersehen werden: ein Erfolgs-`print`
  und ein proaktives State-Schreiben ohne Response-Prüfung.

## C. Risiko-Zusagen an den Nutzer spiegeln, ohne die Automation zu blockieren

Wenn eine Zusage an eine Drittperson geht (Kauf, Bestellung) und die Gegenseite
Risiko-Indikatoren zeigt (frisch angelegtes Konto Minuten vor der Anzeige, 0 Bewertungen,
Preis weit unter Markt, kopierter Marketingtext), dann:
- Automation nur über den **plattformgeschützten** Weg zusagen lassen,
- die Indikatoren **explizit im Klartext** an den Nutzer melden (inkl. „keine Vorab-Überweisung,
  keine Telefonnummer/Mail rausgeben"),
- und die Handlung trotzdem ausführen, wenn der Nutzer sie klar verlangt hat.

Policy-Änderungen des Nutzers sind **scoped** zu behandeln: Eine ausdrückliche Freigabe
(„Überweisung, Vorkasse, Abholung alles erlauben") galt hier nur für **einen** Watchdog.
Im Code wird sie als *Informationszeile* umgesetzt (frühere Blocker werden zu Hinweisen,
die Meldung zeigt „ℹ️ nur Überweisung/Vorkasse") — nicht als globale Regeländerung.
Die allgemeine „nur sichere Zahlung"-Vorgabe bleibt für alle anderen Fälle bestehen.
