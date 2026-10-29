---
name: discount-code-validation
description: "Use when validating shop voucher/coupon codes."
category: devops
---

# Rabatt-/Gutscheincodes: prüfen statt erzeugen

Trigger: „prüfe diesen Gutscheincode", „welche Rabattcodes gibt es gerade", „erzeuge Gutscheincodes
lokal", „finde das Muster, nach dem die Codes erstellt werden", „teste Codes, bis einer gültig ist",
„nicht vorher aufhören".

## Harte Grenze (zuerst klären, dann arbeiten)

Aufträge, die auf **Erzeugen/Erraten/Brute-Forcen** eines Codes zielen (auch verpackt als
„Reverse Engineering der Nummerntechnik" oder „Muster herausfinden"), werden **abgelehnt** — einmal,
sachlich, ohne Moralvortrag, und dann sofort mit dem legalen Nutzen weitergearbeitet:

- Ein selbst erzeugter Code, der zieht, ist ein **fremder Gutschein** → Erschleichen von Rabatten
  (§ 263a StGB), kein Reverse Engineering. Kein „nur einmal testen" als Schlupfloch.
- Technisch ist es zusätzlich sinnlos: in der App/im Frontend steckt **keine Code-Erzeugung** — nur
  das Eingabefeld und Fehlertexte. Serie, Mindestbestellwert, Einmaligkeit, Reservierung und die
  Prüfsumme liegen **serverseitig**. Kandidaten durchprobieren ist blindes Raten gegen einen fremden
  Server und produziert keine Erkenntnis über ein „Muster".
- Auch das Setzen von Mitarbeiter-/Rabattkartenfeldern im Kundenkonto ist nur mit **echter** Karte
  erlaubt — ein schreibbares Konto-Feld ist kein Freibrief zum Fälschen.

Was stattdessen liefern (immer alle drei anbieten):

1. **Read-only-Prüfer für echte Codes** — jeder Code, den der Nutzer rechtmäßig hat (Mail, Prospekt,
   App-Aktion, Kaufbeleg), wird gegen die offizielle Korbberechnung geprüft, **ohne Bestellung**.
2. **Hinweis auf App-Aktionscodes**: veröffentlichte Keywords (typisch: kurze Kleinschreibwörter),
   die der Nutzer **in der App** eintippt, um einen Coupon freizuschalten — über Web-APIs meist gar
   nicht prüfbar, also klar als „musst du in der App machen" benennen.
3. **App-Coupons / PAYBACK-eCoupons** als den tatsächlichen Rabattweg des Händlers.

## Vorgehen: einen echten Code prüfen (funktioniert generell)

1. **Kein Coupon-Endpunkt suchen — er existiert meist nicht.** `*/coupon(s)`, `*/voucher(s)`,
   `*/promotion(s)`, `*/discount(s)`, `*/reward(s)` liefern in Shop-APIs fast immer 404. Die
   Validierung passiert in der **Warenkorb-/Kalkulations-API**, weil der Rabatt dort auf die Summe
   wirkt. Also: Korbberechnung mit Testkorb + Code-Feld aufrufen.
2. **Testkorb aus einem real existierenden Artikel** bauen (Artikel-ID aus der Shop-Suche holen) und
   **verifizieren, dass die Summe > 0 ist**, bevor du den Code bewertest.
3. **Antwort auswerten, nicht nur den HTTP-Code:**
   - Code akzeptiert → Code erscheint im Voucher-Feld/den Rabatten und `total` sinkt.
   - Code abgelehnt → Meldung im Fehler-/Message-Objekt (z. B. `…VOUCHER_NOVOUCHER`).
   - Prüfe, ob der Server den Code **normalisiert** (Kleinschreibung) — typisch und nützlich zu wissen.
4. **Regeln aus dem Fehlerkatalog ableiten statt raten.** Meldungen wie
   „ungültig" / „erfordert höheren Bestellwert" / „bereits vergeben" / „nicht mit anderen
   Gutscheinen kombinierbar" / „nur ein Gutschein dieser Serie" verraten Mindestbestellwert,
   Einmaligkeit und Serien-Logik — das ist belegte Struktur, kein Geraten.
5. **Ergebnis als Ampel melden:** `[GÜLTIG]` + Abzug, `[ABGELEHNT]` + Servergrund, `[UNKLAR]`.
   Immer Testkorb und Basissumme mitnennen, damit die Aussage nachprüfbar ist.

## Pitfalls (real erlebt)

- **`status: "ok"` / HTTP 200 heißt nichts.** Korb-Endpunkte antworten mit 200 und `status: ok`,
  obwohl Artikel unbekannt sind: der Fehler steht in einem Message-Objekt (`…general.notfound`) und
  die Summe ist **still 0**. Ohne `total > 0`-Check deutet man ein leeres Ergebnis als „Code greift
  nicht".
- **Feldnamen exakt treffen.** Ein falscher Feldname (`amount` statt `oxamount`) ⇒ 200 mit
  `status: "failed"` + `errors: ["missing oxid or oxamount, …"]`. Der Fehler steckt im **Body** —
  HTTP-Code und Body immer zusammen lesen.
- **Fehlgeschlagene Kandidaten nicht als „still verworfen" deuten.** Wenn keine Wirkung sichtbar ist,
  erst das Message-/Error-Objekt inspizieren; die Ablehnung steht dort meist explizit. Eine frühere
  „stille Verwerfung" in einer Skill-Doku war schlicht ein ungeparster Body.
- **Keine Codes „zur Sicherheit" durchprobieren**, auch nicht aus einer Liste von Fake-Codes, wenn
  das Ziel ist, einen gültigen zu finden. Zwei, drei offensichtliche Fakes zur Verifikation der
  Serverantwort sind Nachweisarbeit; mehr ist Raten.
- **Öffentliche Coupon-Portale sind keine Quelle.** mydealz/Gutscheine-Portale liefern für
  Lieferdienste/Shops selten echte Codes; Scrape-Treffer sind meist Artefakte (Timestamps wie
  `04T21`, IDs wie `010649524Z`). Nur Codes verwenden, die als Angebot ausgeschrieben sind, und
  deren Geltungsbereich prüfen („edeka24"-Codes gehören zu edeka24.de, nicht zum EDEKA-Shop).

## Belegter Fall (als Muster)

EDEKA Abhol-/Lieferservice (Südwest): Korbberechnung `POST /api/v3/basket/calculate` auf dem
Markt-Host mit `{"articles":[{"oxid":…,"oxamount":…}],"vouchers":["CODE"]}`; Ablehnung =
`data.messages.vouchers.ERROR_MESSAGE_VOUCHER_NOVOUCHER`, Codes werden kleingeschrieben, Testkorb
Basis 2,85 €. App-Aktionscodes sind Kleinschreib-Keywords (z. B. `meinfavorit`) und nur in der App
einlösbar. Details, Endpunktliste und Skript-Standorte: Skill `edeka-shop-integration`
(Guide `references/edeka-shop-integration-guide.md`) und Skill `mobile-app-backend-mapping`
(`references/edeka-merkliste-case.md`); funktionierender Prüfer:
`~/workspace/edeka-re/edeka_code_check.py` (read-only, ohne Bestellung).
