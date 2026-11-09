# Kalt/Warm-Probe: was der Skill wirklich hinzufügt

## Wozu

Ein Abdeckungstest sagt nur, ob eine Regel **im Text steht**. Die Kalt/Warm-Probe sagt, ob sie in der
**Antwort** ankommt — und ob sie überhaupt nötig war. Sie ist das ehrlichste Maß für den Nutzen eines
Playbooks.

## Vorgehen

1. Szenario aus dem Fehlerkatalog wählen, so wie ein Eigentümer fragen würde („Mein Fliesenleger klebt das
   Dichtband mit Fliesenkleber fest — ist das ok?").
2. **Zwei Läufe parallel**, rund zehn Szenarien pro Runde, je Szenario ein Subagent:
   - **kalt**: „Antworte nur aus Allgemeinwissen, öffne keine Dateien, keine Websuche."
   - **warm**: „Lies zuerst `SKILL.md` und `references/playbooks/<thema>.md` vollständig, dann antworte."
   - Beide: 10–15 Sätze, am Ende eine Zeile „welche Punkte stammen aus den Dateien".
3. Auswerten: Welche der `must_contain`-Kerne stehen in der warmen Antwort und fehlen in der kalten? Wo hat
   die kalte Antwort **mehr** Substanz?
4. Urteil je Szenario: `gleichwertig`, `warm präziser`, `kalt besser`.

## Was daraus folgt (Erfahrungswert aus zehn Szenarien)

- **Allgemeinwissen ist stark.** In rund sieben von zehn Fällen hätte eine kalte Antwort den Videofehler
  verhindert. „Der Skill fängt das ab" ist nur dann eine ehrliche Aussage, wenn die konkrete Zahl, Norm oder
  Reihenfolge in der kalten Antwort fehlt.
- **Der Vorsprung liegt bei Zahlen, Quellen und Vollständigkeit**: 50 mm Estrich über der Rinne, 2 % Gefälle,
  W2-I, „6 mm² ist mit 50 A unzulässig", λ-Wert und Güteklasse im Angebot, CM-Grenzwerte, Fristen.
- **Kalt kann gewinnen.** Bei der FI-Aufteilung (Ableitströme, max. ~6 Kreise pro 30-mA-RCD, RCBO, Typ A/B)
  und beim Werkvertrag (§ 648 BGB, aufschiebende Bedingungen) war die kalte Antwort differenzierter. Beide
  Playbooks wurden daraufhin ergänzt — das Playbook wird korrigiert, nicht verteidigt.
- **Nicht jede Warnung ist Wissen.** Kalte Antworten klangen sicher und nannten Zahlen ohne Quelle
  („16 mm² bei 50 A", „5–7 cm Rinnen"). Der Skill muss deshalb **sagen können, woher** eine Zahl kommt — das
  ist der eigentliche Unterschied, nicht die Menge der Ratschläge.

## Konsequenz für die Pflege

Steht in der warmen Antwort nichts, was die kalte nicht auch hatte, ist das Playbook die Arbeit nicht wert:
entweder Zahlen/Quellen/Prüfgrößen nachlegen oder das Thema mit einem Nachbarn zusammenlegen. Bei jedem
neuen Playbook einmal kalt/warm fahren, bevor es als fertig gilt.

## Grenzen

Zehn Szenarien, ein Modell, eine Sprache — ein Stichprobenbild mit Belegen, keine Statistik. Die
Einzelurteile der letzten Runde stehen in der Sitzungshistorie; hier steht die Methode, damit sie
wiederholbar bleibt.
