#!/usr/bin/env python3
"""YouTube-Auto-Untertitel (VTT) → lesbares Transkript mit Zeitmarken.

Warum das Skript existiert: Auto-Untertitel sind *rollierend* — jede Zeile enthaelt das Ende der
vorigen Zeile plus neuen Text. Naives Zusammenfuegen erzeugt Dreifach-Wiederholungen und macht das
Transkript als Quelle unbrauchbar. Hier wird wortweise entdoppelt (laengster Ueberlapp: Suffix des
bisherigen Textes == Praefix des neuen Cues, 3-30 Woerter) und danach in Absaetze à ~20 s mit
[hh:mm:ss] geschnitten.

Aufruf (im Verzeichnis mit den .vtt-Dateien):

    yt-dlp --skip-download --write-auto-subs --sub-langs "de.*" --sub-format vtt \
           -o "<videoid>.%(ext)s" "https://www.youtube.com/watch?v=<videoid>"
    python3 vtt2txt.py            # schreibt <videoid>.txt neben die VTTs

Danach: Datei nach references/transkripte/ legen, mit Kanal, Titel, Laenge, Datum und URL in
references/transkripte/README.md eintragen — die Zeitmarken sind die Fundstelle jedes Fehlers im
Fehlerkatalog. Video vorher per oEmbed pruefen (Kanal + Titel), nicht per Suchtreffer.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

KEEP_LAST = 30          # so viele Woerter Kontext fuer die Ueberlapp-Erkennung
MIN_OVERLAP = 3         # kuerzere Ueberlappungen sind Zufall
PARAGRAPH_SECONDS = 20


def parse_vtt(path: Path) -> list[tuple[str, str]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    cues: list[tuple[str, str]] = []
    for block in re.split(r"\n\s*\n", text):
        m = re.search(r"(\d{1,2}:\d{2}:\d{2})\.\d{3}\s*-->", block)
        if not m:
            continue
        body = "\n".join(line for line in block.splitlines() if "-->" not in line)
        body = re.sub(r"<[^>]+>", "", body)
        body = re.sub(r"^\s*(align|position|line):.*$", "", body, flags=re.M)
        body = " ".join(body.split())
        if body:
            cues.append((m.group(1), body))
    return cues


def _tokens(s: str) -> list[str]:
    return re.findall(r"\S+", s)


def _norm(word: str) -> str:
    return word.lower().strip(",.!?;:\"'()")


def merge_rolling(cues: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """Entfernt die rollenden Wiederholungen der Auto-Untertitel."""
    out: list[tuple[str, str]] = []
    tail: list[str] = []
    for ts, text in cues:
        words = _tokens(text)
        overlap = 0
        for k in range(min(KEEP_LAST, len(tail), len(words)), MIN_OVERLAP - 1, -1):
            if [_norm(w) for w in tail[-k:]] == [_norm(w) for w in words[:k]]:
                overlap = k
                break
        fresh = words[overlap:]
        if not fresh:
            continue
        out.append((ts, " ".join(fresh)))
        tail = (tail + fresh)[-KEEP_LAST:]
    return out


def to_paragraphs(items: list[tuple[str, str]], span: int = PARAGRAPH_SECONDS) -> str:
    def secs(t: str) -> int:
        h, m, s = t.split(":")
        return int(h) * 3600 + int(m) * 60 + int(s)

    lines: list[str] = []
    buf: list[str] = []
    start: str | None = None
    for ts, text in items:
        if start is None:
            start = ts
        buf.append(text)
        if secs(ts) - secs(start) >= span:
            lines.append("[%s] %s" % (start, " ".join(buf)))
            buf, start = [], None
    if buf:
        lines.append("[%s] %s" % (start or "00:00:00", " ".join(buf)))
    return "\n\n".join(lines)


def main(argv: list[str]) -> int:
    folder = Path(argv[1]) if len(argv) > 1 else Path(".")
    best: dict[str, tuple[int, Path]] = {}
    for vtt in sorted(folder.glob("*.vtt")):
        base = re.sub(r"\.(de|de-DE|de-orig|en|en-US)$", "", vtt.stem)
        # pro Video nur eine Quelle: .de.vtt vor .de-DE vor .de-orig
        prio = 0 if vtt.stem.endswith(".de") else (1 if "-DE" in vtt.stem else 2)
        if base in best and best[base][0] <= prio:
            continue
        best[base] = (prio, vtt)

    if not best:
        print("keine .vtt-Dateien gefunden", file=sys.stderr)
        return 1

    for base, (_, vtt) in sorted(best.items()):
        body = to_paragraphs(merge_rolling(parse_vtt(vtt)))
        dest = folder / (base + ".txt")
        dest.write_text(body, encoding="utf-8")
        words = len(re.findall(r"\w+", body))
        print(f"{dest.name:<24} {words:>6} Wörter")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
