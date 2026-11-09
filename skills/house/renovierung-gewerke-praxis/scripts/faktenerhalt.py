#!/usr/bin/env python3
"""Faktenerhalt prüfen: sind nach einer Umstellung alle Zahlen und URLs noch da?

Zweck: Beim Umsortieren von Text (Anhänge in Hauptabschnitte, Kürzen, Umformulieren) gehen
erfahrungsgemäß Zahlen verloren — und zwar die, die man nicht im Kopf hat. Dieses Skript vergleicht
eine Momentaufnahme mit dem jetzigen Stand und meldet jede Zahl und jede URL, die fehlt.

Es arbeitet auf **Mengen von Zahlen-Tokens** (z. B. "0,24", "28.000", "154/154") und auf der Anzahl
der URLs. Es prüft NICHT, ob der Satz noch stimmt — nur, ob die Ziffer noch vorkommt.

Aufruf:
    python3 scripts/faktenerhalt.py --snapshot            # Momentaufnahme anlegen
    python3 scripts/faktenerhalt.py --compare             # gegen die Momentaufnahme prüfen
    python3 scripts/faktenerhalt.py --compare --fail      # Exit 1, wenn Zahlen fehlen
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
PLAYBOOKS = BASE / "references" / "playbooks"
SNAPSHOT = BASE / "references" / "tests" / "faktenerhalt.json"

NUMBER = re.compile(r"\d+(?:[.,]\d+)?")


def scan(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    return {
        "chars": len(text),
        "numbers": sorted(set(NUMBER.findall(text))),
        "urls": len(re.findall(r"https?://", text)),
        "lines": len(text.splitlines()),
    }


def current() -> dict:
    return {
        p.name: scan(p)
        for p in sorted(PLAYBOOKS.glob("*.md"))
        if p.name != "README.md"
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--snapshot", action="store_true", help="Momentaufnahme schreiben")
    ap.add_argument("--compare", action="store_true", help="gegen Momentaufnahme prüfen")
    ap.add_argument("--fail", action="store_true", help="Exit 1 bei fehlenden Zahlen")
    ap.add_argument("--file", help="nur eine Datei prüfen")
    args = ap.parse_args()

    now = current()
    if args.snapshot:
        SNAPSHOT.parent.mkdir(parents=True, exist_ok=True)
        SNAPSHOT.write_text(json.dumps(now, ensure_ascii=False, indent=1), encoding="utf-8")
        total = sum(len(v["numbers"]) for v in now.values())
        print(f"Momentaufnahme geschrieben: {len(now)} Dateien, {total} eindeutige Zahlen")
        return 0

    if not SNAPSHOT.exists():
        print("Keine Momentaufnahme vorhanden — erst --snapshot laufen lassen.")
        return 2

    old = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    problems = 0
    for name, before in old.items():
        if args.file and name != args.file:
            continue
        after = now.get(name)
        if after is None:
            print(f"FEHLT  {name} (Datei existiert nicht mehr)")
            problems += 1
            continue
        lost = sorted(set(before["numbers"]) - set(after["numbers"]))
        urls_lost = before["urls"] - after["urls"]
        if lost or urls_lost > 0:
            problems += 1
            print(f"\n{name}: Zeilen {before['lines']} → {after['lines']}, Zeichen {before['chars']} → {after['chars']}")
            if lost:
                print(f"  Zahlen nicht mehr im Text ({len(lost)}): {', '.join(lost[:18])}"
                      + (" …" if len(lost) > 18 else ""))
            if urls_lost > 0:
                print(f"  URLs: {before['urls']} → {after['urls']} ({urls_lost} verloren)")
    if problems == 0:
        print(f"Alle Zahlen und URLs aus {len(old)} Dateien noch vorhanden.")
    else:
        print(f"\n{problems} Datei(en) mit Verlust — prüfen, ob beabsichtigt (z. B. Dublette entfernt).")
    return 1 if (problems and args.fail) else 0


if __name__ == "__main__":
    sys.exit(main())
