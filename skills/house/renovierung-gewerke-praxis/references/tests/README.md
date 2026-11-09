# Tests: halten die Playbooks, was zehn Praktikervideos versprechen?

## Warum überhaupt

Ein Playbook, das sich gut liest, kann trotzdem die falschen Punkte weglassen. Deshalb wird die
Wissensbasis gegen **Fehlerlisten aus zehn Top-Fehler-Videos** getestet (Transkripte in
`../transkripte/`, Katalog in `../fehlerkatalog.json`).

## Test 1 — Abdeckungstest (deterministisch, jederzeit wiederholbar)

```
python3 scripts/fehlercheck.py          # Tabelle
python3 scripts/fehlercheck.py --gaps   # nur Lücken, nach Playbook
```

Für jeden Fehler ist im Katalog hinterlegt, welche Begriffe, Maße oder Regeln eine korrekte Antwort
**zwingend** enthalten muss (`must_contain`). Geprüft wird pro Fehler nur `SKILL.md` + das im
Katalog zugeordnete Playbook — also der Pfad, der im Gespräch wirklich geladen wird. Nicht der
ganze Korpus: sonst findet der Test den Begriff in einer Belegdatei oder einem fremden Playbook und
meldet Abdeckung, die im Ernstfall nie abgerufen wird.

- `PASS` = alle Pflichtbegriffe vorhanden, `TEIL` = mindestens die Hälfte, `FAIL` = weniger.
- Exit-Code 1, sobald irgendetwas nicht vollständig ist — damit als Regressionstest nach jeder
  Änderung am Skill brauchbar.

**Grenze:** getestet wird die Wissensbasis, nicht das Antwortverhalten. Ein PASS heißt „die Regel
steht im Skill", nicht „jede Antwort wendet sie an". Deshalb Test 2.

**Fallstrick, der schon zugeschlagen hat:** Der erste Lauf meldete drei Lücken, die keine waren —
Umlaute. „Wärmedämmung" wurde zu `warmdammung` normalisiert, im Katalog stand `waermedaemmung`.
Seitdem wird transliteriert (ä→ae) statt entfernt, auf beiden Seiten. Lehre: erst den Test testen,
dann dem Testergebnis glauben.

**Negativkontrolle (bei jeder Änderung am Test):**

```
python3 scripts/fehlercheck.py --ablate playbooks/estrich.md   # muss die est-* runterziehen
```

Gemessene Kontrolle (09.11.2026, 12 Fehler): voll 100 %, ohne `estrich.md` 58 %, ohne `elektro.md`
75 %. Kommt beim Ablieren kaum etwas weg, sind die `must_contain`-Begriffe zu allgemein — dann
spezifische Regeln eintragen („zwei Gänge", „Dichtschlämme", „2,5 mm² bei 50 A") statt Oberbegriffe
wie „Schutzleiter".

## Test 2 — Szenario-Probe (Verhalten, mit und ohne Skill)

Für ein Szenario aus dem Katalog („Ich habe ein Angebot per WhatsApp: Estrich für 3.000 € …") wird
die Frage zweimal gestellt:

1. **kalt** — ohne Skill-Inhalt, nur die Frage (Basislinie: was ein Modell aus Allgemeinwissen sagt)
2. **warm** — mit `SKILL.md` + dem zuständigen Playbook im Kontext

Bewertet wird, ob die konkrete Warnung (der `must_contain`-Kern) in der warmen Antwort vorkommt und in
der kalten fehlt. Fehlt sie in beiden, ist das Playbook zu schwach oder die Frage zu allgemein.

Beispiel-Ergebnis (09.11.2026, Szenario Estrich-Angebot): Die **kalte** Antwort warnt bereits vor
fehlender Leistungsbeschreibung, Dämmung, Trennlage, Randdämmstreifen, Bewehrung und fehlender
Belegreife — sie hätte den Fehler also **teilweise abgefangen**. Der Unterschied liegt nicht in der
Existenz der Warnung, sondern in der Prüfbarkeit: mit Playbook kamen Preisbänder je Estrichart,
2 % Gefälle nur mit Verbundestrich, CM-Grenzwerte, 45 mm + Dämmung = 75 mm Aufbau, Türkürzungsmaße,
Reihenfolge Rohinstallation → Estrich → Abdichtung → Fliesen und Asbest-Verdacht vor
31.10.1993. Konsequenz für die Bewertung: „Skill fängt den Fehler ab" nur behaupten, wenn die
konkrete Zahl/Regel in der kalten Antwort fehlt — sonst ist es Präzision, nicht Abdeckung.

Ergebnis-Dokument: `kalt-warm.md` (Methode und Erfahrungswerte; die Einzelurteile je Szenario stehen in der
Sitzungshistorie). Kurzfassung: das Allgemeinwissen war in 7 von 10 Fällen ausreichend, um den Videofehler zu
vermeiden; der Skill gewinnt über Zahlen, Belegbarkeit und Vollständigkeit — bei zwei Szenarien (FI-Aufteilung,
Werkvertrag) war die kalte Antwort sogar differenzierter, was zu Nachträgen in `elektro.md` und
`hausbau-baufirma.md` geführt hat.

## Werkzeuge

- `scripts/fehlercheck.py` — Abdeckung gegen den Fehlerkatalog (128 bewertete Fehler), `--gaps`, `--json`,
  `--ablate` als Negativkontrolle.
- `scripts/linkcheck.py` — alle URLs im Skill (736), HEAD zuerst, Retry bei 000, Klammern in Pfaden
  balanciert; Bot-Blocker (kfw.de, landesrecht-bw.de) werden separat gezählt statt als tot gemeldet.
- `scripts/strukturcheck.py` — Formvertrag je Playbook: Kurzantwort, ≥ 15 konkrete Zahlen (Rechts-Playbooks
  stattdessen ≥ 5 Paragraphen), ≥ 8 Quellen-URLs, „Unbelegt“-Abschnitt, Preisbänder mit Jahresangabe.
- `~/.hermes/scripts/renov_skill_health.py` — Cron-Wächter, kombiniert Abdeckung und Links, schweigt im
  Normalfall.
- **GitHub Actions** (`.github/workflows/skills-checks.yml` in der veröffentlichten Kopie): zwei Jobs.
  `schnell` läuft bei jedem Push (strukturcheck + fehlercheck, Sekunden); `links` läuft monatlich und per
  `workflow_dispatch`, weil 1.100+ URLs den Runner sonst in den Timeout treiben und der Push rot wird,
  ohne dass der Inhalt schuld ist. Schlägt `schnell` fehl, ist es ein echter Befund — nicht ignorieren.

### Fallstricke der Linkprüfung (alle aufgetreten, alle im Skript behoben)

- **Klammern im Pfad**: Wikipedia-URLs wie `…/Nutzlast_(Bauwesen)` wurden am `)` abgeschnitten und als 404
  gemeldet. Die Regex bricht dort ab — das Skript schließt jetzt balancierend wieder, sonst entstehen
  Scheinlücken und jemand „repariert" eine intakte Quelle.
- **Drosselung**: `gesetze-im-internet.de` beantwortet 12 parallele Anfragen teils mit 000. Deshalb Retry
  nach 2 s und **6 Threads** statt 12 — 000 heißt erst nach dem zweiten Versuch „tot".
- **Dauerhaft blockende Hosts** (kfw.de, landesrecht-bw.de, service-bw.de) liefern grundsätzlich 000/403:
  als „bekannt blockiert" zählen, nicht als tot. Der Inhalt ist über Browser bzw. amtliche PDFs geprüft.
- **200 ≠ Inhalt**: bei JS-Portalen liefert jede Dokument-URL eine Hülle mit 200. Vor dem Zitieren den
  Text tatsächlich lesen, sonst wandert eine leere Seite als Beleg in den Skill. Dasselbe gilt für
  PDF-Links: `file x.pdf` prüfen — kommt HTML zurück, ist das Dokument verschwunden, obwohl der Status 200 ist.
- **000 trotz lebender Seite = Zertifikatskette**: kfw.de und mehrere Behörden-PDFs antworten ohne `-k`
  mit 000, mit `curl -k` mit 200. Solche Links als erreichbar führen (im Skript `200*`), nicht löschen —
  sonst verliert der Skill eine gültige Primärquelle. Vor dem Löschen immer erst `-k` probieren.
- **URLs aus Markdown nicht raten**: erst prüfen, dann als tot markieren *und* die URL entfernen — bleibt sie
  stehen, meldet der Wächter sie jeden Montag erneut und man gewöhnt sich an die Meldung.

## Test 3 — Quellen-Gegenprobe

Stichprobe der Playbook-Zahlen gegen die Originalquelle (Herstellerdatenblatt, Normenportal, Video-
Transkript). Wird bei jeder Änderung an Zahlen wiederholt; Ergebnisse stehen in
`../../references/quellen.md`.

**Geld und Fristen nur aus der Primärquelle.** Fördersätze, Deckel, Stichtage und Paragraphen gegen
Merkblatt, Richtlinie oder Gesetz prüfen — nicht gegen Portalartikel, ADAC/Verbraucherportale oder
Herstellerblogs. Ablauf für PDF-Primärquellen:

```bash
curl -skL -m 60 -o m.pdf "<merkblatt-url>" -w "%{http_code}\n"
file m.pdf                      # 200 + HTML statt PDF = Dokument ist weg, nicht „vorhanden“
pdftotext -layout m.pdf m.txt   # dann im Text suchen, nicht im Kopf
 grep -n -E "Prozent|2027|Höchstbetrag" m.txt
```

Belegter Fall: zwei Fachportale schrieben „15 % Grundförderung ab 2027 plus Wertschöpfungsbonus“; das
**KfW-Merkblatt 458 (Stand 09/2026)** sagt im Volltext **30 % Grundförderung, kein Bonus**, Deckel 70 %
(80 % nur bei zvE ≤ 30.000 €), Höchstbetrag 28.000 € mit −750 € je Halbjahr ab 01.02.2027. Der Fehler
stand in **zwei** Playbooks und wurde vom Warm-Lauf brav weitergegeben — ein Skill mit Sekundärquelle
verstärkt einen Fehler, statt ihn abzufangen. Konsequenz: bei jedem Kalt/Warm-Lauf die warme Antwort
zusätzlich gegen die Primärquelle prüfen, sonst misst man nur, ob das Modell den Skill wiederholt.

## Test 3b — Themenweise Kalt/Warm-Probe (mehrere Fragen je Lauf)

Für einen ganzen Themenblock (z. B. Wärmepumpe, PV, Elektro-Altbau, Kabel, Förderung, Komplettsanierung):

1. **Paare bilden**: gleiche Frage zweimal, einmal „nur Allgemeinwissen, keine Dateien/Skills“, einmal
   „lies SKILL.md + zuständiges Playbook“. Beide Läufe ohne Kenntnis des anderen.
2. **Beide Läufe parallel** starten (je ein Subagent pro Frage), damit keine Absprache entsteht.
3. **Bewertung in drei Spalten**: was kalt richtig war, was kalt falsch war (mit Paragraph/Datum), was
   warm zusätzlich liefert. Struktur und Ablauf sind meist schon kalt gut — der Unterschied zeigt sich
   bei Zahlen, Fristen, Ausschlussregeln.
4. **Warm mitprüfen**: jede warme Zahl, die aus dem Skill stammt, gegen die Primärquelle (Test 3).
   Sonst dokumentiert man die Skill-Fehler als Erfolg.

Erfahrungswert: kalte Antworten sind bei Struktur inzwischen stark und fallen vor allem bei
Rechts-/Fördersätzen durch (weggefallene Pflichten, alte Deckel). Diese Fehler sind der eigentliche
Nutzen des Playbooks — sie gehören in die Antwort, nicht nur in die Belegliste.

## Test 4 — Katalog-Pflege: Regel oder Anekdote?
Der Katalog wird aus Videos gebaut und ist damit voll von Projekt-Details. Wird jedes Detail als
Pflichtbegriff eingetragen, misst der Test nicht mehr Wissen, sondern Zitierfreude. Deshalb pro Fehler:

- **`must_contain` = die übertragbare Regel**, 1–3 Begriffe, keine Euro-Beträge, keine Produktnamen,
  keine Zahlen aus dem konkreten Projekt („15 cm Estrich", „1200 € für 7 Türen", „7 m³ Schüttgut").
- **Anekdote** bleibt im Datensatz (`error`, `scenario`, `quote`) stehen, wird aber `scored:false` gesetzt
  und zählt in keiner Quote mit.
- Faustregel für die Triage: enthält der Begriff einen Preis, einen Markennamen oder eine Aufzählung
  („4–5 Mann, 2 Wochen") → Anekdote. Nennt er ein Material, Maß, Verfahren oder eine Norm → Regel.

Nach jeder Triage die Zahl neu messen. Eine gestiegene Quote durch Umetikettieren ist kein Fortschritt.

## Matcher-Regeln (sonst lügt die Quote)

Vier Fallen, alle schon aufgetreten:

1. **Umlaute transliterieren, nicht entfernen** — `ä→ae` auf beiden Seiten. Entfernen macht aus
   „Wärmedämmung" `warmdammung` und aus dem Katalogbegriff `waermedaemmung`; der Test meldet dann Lücken,
   die keine sind.
2. **Bindestriche zu Leerzeichen** — sonst findet `try and error` das Wort „Try-and-error" nicht.
3. **Füllwörter entfernen** (der/die/das/dem/den/auf/im/…), sonst matcht „Spannung auf PE" nicht
   „Spannung auf dem PE".
4. **Begriffe mit Ziffern wörtlich prüfen** (Maße, Normnummern, Prozentwerte) — Zahlen werden nicht
   „ungefähr" gematcht.
5. **Wortstellung ist keine Bedeutung** — mehrwortige Begriffe werden über ein **Fenster von ~14 Wörtern**
   gesucht: alle Bestandteile müssen nah beieinander stehen, die Reihenfolge ist egal. Grund: „an der Wand
   hochgezogen" stand im Playbook, der Katalog fragte „hochgezogen an der Wand" — die Phrasensuche meldete
   eine Lücke, die keine war, und drückte die Quote um 11 Fehler. Das Fenster darf **nicht** dokumentweit
   suchen, sonst trifft „Wand … hochgezogen" zwei verschiedene Absätze und der Test wird beliebig.

Nach jeder Änderung am Matcher: `--ablate` gegenprüfen. Ein Matcher, der nach einer Lockerung plötzlich
100 % meldet, ist kaputt, nicht großzügig.

## Quelle beschaffen: Video-Transkripte (der Katalog beginnt hier)

```bash
yt-dlp --skip-download --write-auto-subs --sub-langs "de.*" --sub-format vtt \
       -o "<id>.%(ext)s" "https://www.youtube.com/watch?v=<id>"
```

- **Video vor dem Zitieren verifizieren:** `https://www.youtube.com/oembed?url=...&format=json` gibt Kanal
  und Titel zurück. Ein Treffer in der Suche ist kein Beleg, dass das Video noch existiert.
- **Auto-Untertitel sind rollierend**: jede Zeile enthält das Ende der vorigen. Naives Zusammenfügen
  erzeugt Dreifach-Wiederholungen. Entdoppeln über den längsten Wort-Überlapp (Suffix der alten Zeile =
  Präfix der neuen, 3–30 Wörter), dann Absätze à 20 s mit `[hh:mm:ss]`.
- **ASR-Fehler einplanen** („Bartsanierung" = Badsanierung, „Strich" = Estrich, „Dichtschlemme" =
  Dichtschlämme): beim Zitieren behutsam glätten und als ASR kennzeichnen.
- **Zeitmarken sind ±10 s und können zwischen zwei Abrufen wandern.** Vor dem Zitat die Stelle im
  aktuellen Transkript erneut suchen; eine alte Minutenangabe aus einer früheren Sitzung ist keine Quelle.

## Test 5 — Strukturvertrag (Form, nicht Inhalt)

Der Abdeckungstest merkt nicht, wenn ein Playbook seine Quellenliste verliert oder Preise ohne Datum nennt.
Deshalb prüft `scripts/strukturcheck.py` je Datei sechs Dinge: H1, Kurzantwort in den ersten 60 Zeilen,
mindestens 15 konkrete Zahlen (Rechts-Playbooks: ≥ 5 `§`), mindestens 8 Quellen-URLs, einen
„Unbelegt“-Abschnitt und — falls €-Beträge vorkommen — irgendwo eine Jahresangabe („Preisstand“).

Beim ersten Lauf waren 22 von 23 Playbooks im Verstoß, überwiegend wegen fehlender Kurzantwort (13×) und
fehlender Unbelegt-Liste (3×) — beides Zusagen aus dem README, die beim Delegieren verloren gingen. Zwei
Dauerfälle bleiben inhaltlich zu dünn statt nur formal: ein Playbook mit 1 Quelle und eines mit 5.

Lehre: **Form prüfen lassen, nicht erinnern.** Ein Playbook ohne Kurzantwort ist im Gespräch doppelt so
teuer, weil der Agent die ersten 200 Zeilen lesen muss, um zu wissen, ob es passt.

## Test 6 — Themeninventur: was fehlt überhaupt?

Die Abdeckung sagt nur, was die zehn Videos verlangen. Ob ein ganzes Thema fehlt, zeigt sie nie. Dafür eine
Liste von Begriffen quer über den Lebenszyklus eines Hauses bilden (Recht, Technik, Geld, Betrieb) und je
Begriff die Trefferzahl im Korpus zählen — Sätze mit `grep -rIic "<begriff>" . | awk -F: '{s+=$2}'`.

Null Treffer heißt: Thema fehlt. Weniger als vier Treffer heißt: erwähnt, nicht erklärt — nachziehen oder
bewusst abgrenzen. Und: **Teilstring-Treffer prüfen**, bevor man sie als Abdeckung zählt („WEG“ traf 44×,
weil „weg“ in „Weg“ und „wegen“ steckt; „Blei“ traf 202×, weil „bleiben“ mitgezählt wurde). Beim ersten
Inventar waren 12 von 61 Themen blind — darunter Energieausweis, Radon, Batteriespeicher, Kabel-Internet,
Fernwärme, sommerlicher Wärmeschutz.

## Was hier nicht getestet wird

- Ob eine Antwort im echten Gespräch freundlich/verständlich ist.
- Ob die Preise in einem konkreten Jahr noch stimmen (Kostenbänder sind datiert).
- DIN-Inhalte (kostenpflichtig) — nur Nummer, Titel und Ausgabe sind belegt.
