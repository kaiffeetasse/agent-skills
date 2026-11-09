#!/usr/bin/env python3
"""Fehlercheck: Deckt der Skill die Fehler ab, die Praktiker in Top-Fehler-Videos nennen?

Idee: Aus zehn YouTube-Videos (Transkripte in references/transkripte/) wurde je Fehler ein
Datensatz gebaut: Fehler, Szenario, und die Begriffe/Maße, die eine korrekte Antwort zwingend
enthalten muss ("must_contain"). Dieses Skript prüft, ob diese Begriffe in der Skill-Wissensbasis
(SKILL.md + references/**/*.md) tatsächlich vorkommen.

Scope: pro Fehler wird nur SKILL.md + das zustaendige Playbook geprueft. Sonst findet der Test die
Begriffe in irgendeiner Belegdatei (quellen.md, faktencheck.md, anderen Playbooks) und meldet eine
Abdeckung, die im Ernstfall nicht abgerufen wird. Negativkontrolle: --ablate playbooks/estrich.md
muss alle est-* auf FAIL/TEIL druecken.

Grenze der Aussage: getestet wird die Wissensbasis, nicht das Antwortverhalten eines Modells.
Ein PASS heißt "die Regel steht im Skill", nicht "jede Antwort wendet sie an". Deshalb gibt es
zusätzlich die Szenario-Probes (siehe references/tests/README.md).

Aufruf:
    python3 scripts/fehlercheck.py                 # Tabelle + Zusammenfassung
    python3 scripts/fehlercheck.py --json          # maschinenlesbar
    python3 scripts/fehlercheck.py --gaps          # nur Lücken, nach Playbook gruppiert
Exit-Code 1, wenn ein Fehler nicht (oder nur teilweise) abgedeckt ist.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
CATALOG = SKILL / "references" / "fehlerkatalog.json"
EXCLUDE = {"references/fehlerkatalog.json"}
# Fuellwoerter, die beim Vergleich nur stoeren ("Spannung auf dem PE" == "Spannung auf PE")
STOP = {"der", "die", "das", "dem", "den", "des", "im", "in", "am", "an", "auf", "mit", "und", "oder",
        "je", "zum", "zur", "von", "bei", "fuer", "als", "ist", "sind", "wird", "werden", "eine", "einer",
        "ein", "nicht", "sich", "vor", "nach", "aus", "zu"}


def norm(text: str) -> str:
    """Kleinschreibung, Umlaute transliterieren (ä→ae), Satzzeichen zu Leerzeichen.

    Wichtig: transliterieren statt Umlaute zu entfernen. Sonst findet „waermedaemmung" im
    Katalog den Text „Wärmedämmung" nicht (ä→a ergibt „warmdammung") — der Test meldet dann
    Lücken, die keine sind. Beide Seiten laufen durch dieselbe Funktion, deshalb ist die
    Schreibweise danach egal.
    """
    text = text.lower()
    text = text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-z0-9,./%\s-]", " ", text)
    text = text.replace("-", " ")          # Try-and-error == try and error
    words = [w for w in text.split() if w not in STOP]
    return " ".join(words)


def corpus(ablate: set[str] | None = None) -> dict[str, str]:
    files = [SKILL / "SKILL.md"] + sorted((SKILL / "references").rglob("*.md"))
    out = {}
    for f in files:
        rel = f.relative_to(SKILL).as_posix()
        if rel in EXCLUDE:
            continue
        if ablate and any(a in rel for a in ablate):
            continue
        out[rel] = norm(f.read_text(encoding="utf-8", errors="replace"))
    return out


def scoped_docs(item: dict, docs: dict[str, str]) -> dict[str, str]:
    """Nur SKILL.md + das zustaendige Playbook — das ist der Pfad, der im Gespraech wirklich geladen wird."""
    pb = (item.get("playbook") or "").strip()
    out = {"SKILL.md": docs["SKILL.md"]} if "SKILL.md" in docs else {}
    for rel, text in docs.items():
        if pb and rel.endswith(pb):
            out[rel] = text
    return out or docs


def _alt_found(alt: str, text: str) -> bool:
    """Ein Begriff gilt als belegt, wenn er woertlich vorkommt oder (bei mehreren Woertern) fast
    vollstaendig: alle Woerter ab 4 Zeichen bis auf eines, mindestens 75 % Trefferquote.
    Begriffe mit Ziffern (Masse, Normnummern) muessen woertlich passen — Zahlen raten wir nicht."""
    if alt in text:
        return True
    if re.search(r"\d", alt):
        return False
    toks = [t for t in re.split(r"[\s-]+", alt) if len(t) >= 4]
    if len(toks) < 2:
        return False
    # Reihenfolge egal, Abstand zaehlt: alle Woerter muessen in einem Fenster von 14 Woertern stehen.
    # "an der Wand hochgezogen" soll "hochgezogen an der Wand" treffen, aber nicht quer durchs Dokument.
    words = text.split()
    n = len(toks)
    win = max(6, n + 8)
    need = list(toks)
    for i, w in enumerate(words):
        if w != need[0]:
            continue
        window = set(words[i:i + win])
        if all(t in window for t in need):
            return True
    have = sum(1 for t in toks if t in text)
    return have >= max(2, int(len(toks) * 0.5 + 0.5))


def term_hits(term: str, docs: dict[str, str]) -> list[str]:
    """Welche Dateien decken den Begriff ab? Alternativen mit | erlaubt."""
    alts = [norm(a) for a in term.split("|") if a.strip()]
    hits = []
    for rel, text in docs.items():
        if any(_alt_found(a, text) for a in alts):
            hits.append(rel)
    return hits


def run(show_gaps_only: bool = False, ablate: set[str] | None = None) -> int:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    docs = corpus(ablate)
    rows, fails, skipped = [], [], 0
    for item in data["fehler"]:
        if item.get("scored") is False:
            skipped += 1
            continue
        terms = item["must_contain"]
        found = {t: term_hits(t, scoped_docs(item, docs)) for t in terms}
        missing = [t for t, h in found.items() if not h]
        ratio = (len(terms) - len(missing)) / len(terms) if terms else 1.0
        status = "PASS" if ratio == 1.0 else ("TEIL" if ratio >= 0.5 else "FAIL")
        row = {
            "id": item["id"],
            "video": item.get("video", ""),
            "playbook": item.get("playbook", ""),
            "error": item["error"],
            "status": status,
            "ratio": round(ratio, 2),
            "missing": missing,
            "found_in": sorted({f for h in found.values() for f in h}),
        }
        rows.append(row)
        if status != "PASS":
            fails.append(row)

    if not show_gaps_only:
        print(f"{'ID':<14}{'PB':<22}{'ST':<6}{'%':<6}Fehler")
        for r in rows:
            print(f"{r['id']:<14}{r['playbook'][:21]:<22}{r['status']:<6}{int(r['ratio']*100):<6}{r['error'][:60]}")
    else:
        by_pb: dict[str, list[dict]] = {}
        for r in fails:
            by_pb.setdefault(r["playbook"] or "(ohne)", []).append(r)
        for pb, items in sorted(by_pb.items()):
            print(f"\n## {pb}")
            for r in items:
                print(f"- [{r['status']}] {r['id']}: {r['error']}")
                print(f"    fehlt: {', '.join(r['missing'])}")

    total = len(rows)
    ok = sum(1 for r in rows if r["status"] == "PASS")
    part = sum(1 for r in rows if r["status"] == "TEIL")
    fail = sum(1 for r in rows if r["status"] == "FAIL")
    print(f"\n{total} Fehler geprüft: {ok} vollständig, {part} teilweise, {fail} nicht abgedeckt "
          f"({ok / total * 100:.0f} % Abdeckung)")
    if skipped:
        print(f"{skipped} Fehler nicht bewertet (Projekt-Anekdote aus dem Video, keine übertragbare Regel)")
    return 0 if not fails else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="JSON-Ausgabe")
    ap.add_argument("--gaps", action="store_true", help="nur Lücken anzeigen")
    ap.add_argument("--ablate", default="", help="Pfade (Teilstrings, Komma) aus dem Korpus entfernen — Negativkontrolle")
    args = ap.parse_args()
    if args.json:
        data = json.loads(CATALOG.read_text(encoding="utf-8"))
        docs = corpus()
        out = []
        for item in data["fehler"]:
            if item.get("scored") is False:
                out.append({**item, "missing": [], "status": "SKIP"})
                continue
            found = {t: term_hits(t, scoped_docs(item, docs)) for t in item["must_contain"]}
            missing = [t for t, h in found.items() if not h]
            out.append({**item, "missing": missing,
                        "status": "PASS" if not missing else ("TEIL" if len(missing) < len(item["must_contain"]) else "FAIL")})
        print(json.dumps(out, ensure_ascii=False, indent=2))
        sys.exit(0)
    ablate = {a.strip() for a in args.ablate.split(',') if a.strip()}
    sys.exit(run(show_gaps_only=args.gaps, ablate=ablate))
