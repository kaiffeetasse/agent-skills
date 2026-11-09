#!/usr/bin/env python3
"""Struktur-Prüfung: hält jedes Playbook auf dem versprochenen Format.

Warum: Der Fehlercheck prüft nur *Inhalt* gegen die Video-Fehlerliste. Er merkt nicht, wenn ein Playbook
seine Quellen- oder „Unbelegt"-Liste verliert, keine Zahlen mehr hat oder Preise ohne Datum nennt. Genau
das passiert beim Zusammenkopieren und beim Delegieren an Subagenten.

Geprüft wird je Playbook:
  * Kopfzeile (H1) vorhanden
  * „Kurzantwort" oder „Kurz"-Abschnitt
  * mindestens ein Zahlenblock (Ziffern) — Playbook ohne Zahlen ist Prosa
  * Quellen: mindestens 8 URLs (Ausnahme: reine Verweis-/Indexdateien)
  * „Unbelegt"-Abschnitt (die Regel des Skills: Unbelegtes wird ausgewiesen, nicht geglättet)
  * Preisbänder: Wo €/m², €/Stück, €/h stehen, muss irgendwo ein Jahr (20xx) im Dokument stehen

Aufruf:
    python3 scripts/strukturcheck.py             # Tabelle + Exit 1 bei Verstößen
    python3 scripts/strukturcheck.py --fix-hints # mit konkreten Reparaturhinweisen
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
PBS = SKILL / "references" / "playbooks"
SKIP = {"README.md"}
MIN_URLS = 8
PRICE = re.compile(r"€\s?/?\s?(m²|m2|Stück|Stk|lfm|h|kWh|t)\b|€/")

CHECKS = [
    ("h1",        lambda t: t.lstrip().startswith("#"),                      "H1-Überschrift fehlt"),
    ("kurz",      lambda t: re.search(r"\bkurz", "\n".join(t.splitlines()[:60]), re.I), "kein Kurz-Abschnitt in den ersten 60 Zeilen"),
    ("zahlen",    lambda t: t.count("§") >= 5 or                      # Rechts-Playbooks zaehlen Paragraphen
                             len(re.findall(r"\d+[.,]?\d*\s?(mm|cm|m²|m2|%|€|kg|h|Tage|Wochen)\b", t)) >= 15,
                  "zu wenige konkrete Zahlen (<15)"),
    ("quellen",   lambda t: len(re.findall(r"https?://", t)) >= MIN_URLS,      f"weniger als {MIN_URLS} Quellen-URLs"),
    ("unbelegt",  lambda t: re.search(r"unbelegt|nicht belegt|Nicht belegt", t, re.I), "„Unbelegt“-Liste fehlt"),
    ("preisdatum",lambda t: not PRICE.search(t) or re.search(r"20\d\d", t),    "Preise ohne Jahresangabe (Preisstand fehlt)"),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix-hints", action="store_true")
    args = ap.parse_args()

    rows, violations = [], 0
    for f in sorted(PBS.glob("*.md")):
        if f.name in SKIP:
            continue
        t = f.read_text(encoding="utf-8", errors="replace")
        bad = [msg for _, fn, msg in CHECKS if not fn(t)]
        rows.append((f.name, len(re.findall(r"https?://", t)), bad))
        violations += len(bad)

    w = max(len(r[0]) for r in rows)
    for name, urls, bad in rows:
        flag = "ok " if not bad else "!! "
        print(f"{flag}{name:<{w}}  {urls:>3} URLs  {'' if not bad else ' | '.join(bad)}")
    print(f"\n{len(rows)} Playbooks, {violations} Verstöße")
    if violations and args.fix_hints:
        print("\nHinweise:")
        print("- „Unbelegt“ fehlt: Abschnitt am Ende anlegen und alles auflisten, was ohne Quelle im Text steht.")
        print("- Preise ohne Jahr: „Preisstand 09/2026“ an die Kostentabelle schreiben.")
        print("- Wenige URLs: Quellen ergänzen oder das Playbook als Verweisdatei kennzeichnen (SKIP).")
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
