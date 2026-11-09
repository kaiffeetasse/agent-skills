#!/usr/bin/env python3
"""Router-Test: landet eine Alltagsfrage in der richtigen Playbook-Datei?

Was hier geprüft wird — und was nicht:
Getestet wird die **Router-Tabelle in SKILL.md**, also ob die Stichworte einer Zeile zu einer
typischen Frage passen und ob genau eine Zeile gewinnt. NICHT getestet wird, welches Playbook
ein Sprachmodell tatsächlich öffnet — dafür braucht es einen Lauf durch das Modell.

Trotzdem nützlich: wenn zwei Zeilen fast gleich gut passen, ist die Tabelle mehrdeutig, und
dann greift auch ein Modell daneben.

Aufruf:
    python3 router_test.py            # Tabelle
    python3 router_test.py --json
    python3 router_test.py --fail     # Exit 1 bei Fehlgriff oder Mehrdeutigkeit
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SKILL = BASE / "SKILL.md"
CASES = BASE / "references" / "router-test.json"

STOP = {
    "und", "oder", "der", "die", "das", "den", "dem", "ein", "eine", "einen", "einer", "im", "in",
    "an", "am", "auf", "aus", "bei", "für", "mit", "von", "zu", "zum", "zur", "ist", "sind", "wird",
    "werden", "kann", "können", "muss", "müssen", "soll", "sollen", "ich", "wir", "mein", "meine",
    "unser", "unsere", "es", "sich", "nicht", "noch", "auch", "schon", "wie", "was", "welche",
    "welcher", "wann", "wo", "geht", "gehen", "habe", "haben", "brauche", "brauchen", "will",
    "wollen", "macht", "machen", "gibt", "lohnt", "reicht", "kostet", "kosten", "dauert",
}


def stem(word: str) -> str:
    """Grober Stamm: deutsche Endungen abschneiden reicht für Stichwortvergleich."""
    word = word.lower().strip(".,;:!?()\"'„“")
    # Kein "s"-Abschnitt bei Woertern auf -is/-us/-os/-ss ("Stromkreis" darf nicht zu "Stromkrei" werden)
    if len(word) > 5 and word.endswith("s") and not word.endswith(("is", "us", "os", "ss")):
        word = word[:-1]
    for suffix in ("ungen", "ung", "en", "er", "es", "em", "e", "n"):
        if len(word) > 5 and word.endswith(suffix):
            return word[: -len(suffix)]
    return word


def tokens(text: str) -> set[str]:
    words = re.findall(r"[A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß\-]+", text)
    return {stem(w) for w in words if w.lower() not in STOP and len(w) > 2}


def parse_router() -> list[tuple[str, str]]:
    text = SKILL.read_text(encoding="utf-8", errors="replace")
    block = text.split("### Router: Frage → Playbook", 1)[1].split("\n## ", 1)[0]
    rows = []
    for line in block.splitlines():
        if not line.startswith("|") or line.startswith("|---") or "So fragt man" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        file_match = re.search(r"`([a-z0-9\-]+\.md)`", cells[1])
        if file_match:
            rows.append((cells[0], file_match.group(1)))
    return rows


def score(question_tokens: set[str], row_text: str) -> float:
    """Anteil der FRAGE-Stichworte, die die Zeile abdeckt.

    Bewusst nicht durch die Zeilenlaenge geteilt: sonst gewinnt die kuerzeste Zeile, und eine
    ausfuehrliche Zeile wird fuer ihre Genauigkeit bestraft. Laengere Zeilen bekommen nur einen
    minimalen Abzug als Tie-Break.
    """
    row_tokens = tokens(row_text)
    if not row_tokens or not question_tokens:
        return 0.0
    hit = question_tokens & row_tokens
    return len(hit) / len(question_tokens) - 0.001 * len(row_tokens)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--fail", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    rows = parse_router()
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    results = []
    for case in cases:
        qt = tokens(case["frage"])
        ranked = sorted(((score(qt, text), file, text) for text, file in rows), reverse=True)
        top_score, top_file, top_text = ranked[0]
        second_score = ranked[1][0] if len(ranked) > 1 else 0.0
        ambiguous = second_score > 0 and (top_score - second_score) < 0.15
        results.append(
            {
                "frage": case["frage"],
                "erwartet": case["erwartet"],
                "getroffen": top_file,
                "richtig": top_file == case["erwartet"],
                "score": round(top_score, 2),
                "zweitbeste": ranked[1][1] if len(ranked) > 1 else None,
                "mehrdeutig": ambiguous,
            }
        )

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        ok = sum(1 for r in results if r["richtig"])
        print(f"{ok}/{len(results)} Fragen landen in der erwarteten Datei\n")
        for r in results:
            if r["richtig"] and not r["mehrdeutig"] and not args.verbose:
                continue
            flag = "OK  " if r["richtig"] else "FALSCH"
            extra = " (mehrdeutig)" if r["mehrdeutig"] else ""
            print(f"{flag} {r['score']:.2f}{extra}  {r['frage'][:70]}")
            print(f"        erwartet {r['erwartet']}, getroffen {r['getroffen']} "
                  f"(zweitbeste: {r['zweitbeste']})")
        bad = [r for r in results if not r["richtig"]]
        amb = [r for r in results if r["mehrdeutig"]]
        print(f"\n{len(bad)} Fehlgriffe, {len(amb)} mehrdeutige Fragen (Abstand < 0,15).")
        print("Grenze des Tests: geprüft wird die Router-Tabelle, nicht die Wahl eines Modells.")
    bad = [r for r in results if not r["richtig"]]
    amb = [r for r in results if r["mehrdeutig"]]
    return 1 if (args.fail and (bad or amb)) else 0


if __name__ == "__main__":
    sys.exit(main())
