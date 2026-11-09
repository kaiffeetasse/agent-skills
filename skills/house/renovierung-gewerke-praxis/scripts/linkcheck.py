#!/usr/bin/env python3
"""Prüft alle URLs in der Skill-Wissensbasis auf Erreichbarkeit.

Hintergrund: Beim ersten Durchlauf standen fünf tote Links im Skill (vier OBI-Anleitungen mit HTTP 404,
fredsbauanleitungen.de ohne Antwort) und eine falsche Amtsquelle (VOB/B auf gesetze-im-internet.de, HTTP
404 — VOB/B ist keine Rechtsnorm). Ohne Prüfung fällt so etwas erst auf, wenn jemand die Quelle braucht.

Aufruf:
    python3 scripts/linkcheck.py             # Zusammenfassung + tote Links
    python3 scripts/linkcheck.py --all       # jeden Link einzeln
    python3 scripts/linkcheck.py --timeout 8 --jobs 8

Bewertung:
    200/301/302/303/307/308 = ok
    401/403/429             = ok (Bot-Schutz, Seite existiert)
    404/410                 = tot  -> Exit 1
    000                     = keine Antwort (DNS/TLS/Blockade) -> Warnung, Exit 1
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import re
import subprocess
import sys
import time
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
URL_RE = re.compile(r"https?://[^\s)|\]>\"']+")
OK = {200, 301, 302, 303, 307, 308, 401, 403, 429}
# Diese Hosts blocken automatisierte Abrufe dauerhaft (000) — Inhalt ist über den Browser geprueft.
BLOCKED_HOSTS = ("kfw.de", "kfw.com", "landesrecht-bw.de", "service-bw.de")


def urls() -> dict[str, set[str]]:
    found: dict[str, set[str]] = {}
    for f in [SKILL / "SKILL.md", *sorted((SKILL / "references").rglob("*.md"))]:
        raw = f.read_text(encoding="utf-8", errors="replace")
        for m in URL_RE.finditer(raw):
            u = m.group(0).rstrip(".,;:`")
            # Klammern im Pfad (z. B. Wikipedia "Nutzlast_(Bauwesen)") wieder schliessen:
            # die Regex bricht an ")" ab, deshalb hier balancieren.
            while u.count("(") > u.count(")") and raw[m.start() + len(u):][:1] == ")":
                u += ")"
            if "..." in u or "…" in u:      # Platzhalter aus Doku-Beispielen
                continue
            found.setdefault(u, set()).add(f.relative_to(SKILL).as_posix())
    return found


def check(url: str, timeout: int) -> tuple[str, str]:
    base = ["curl", "-s", "-o", "/dev/null", "-m", str(timeout), "-g",
            "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "-H", "Accept-Language: de-DE,de;q=0.9,en;q=0.8",
            "-w", "%{http_code}"]
    for attempt in range(2):           # zweiter Versuch nach Pause: Hosts drosseln gern
        for mode in (["-I"], []):      # erst HEAD (schnell, auch bei großen PDFs), dann GET
            try:
                r = subprocess.run(base[:1] + mode + base[1:] + [url],
                                   capture_output=True, text=True, timeout=timeout + 5)
                code = r.stdout.strip()
                if code and code != "000":
                    # HEAD luegt bei manchen Seiten: OBI und bau.net antworten auf HEAD mit 404,
                    # auf GET mit 200. Deshalb bei 4xx/5xx aus dem HEAD weiter mit GET probieren.
                    if mode and code.startswith(("4", "5")):
                        continue
                    return url, code
            except Exception:
                pass
        if attempt == 1:
            # Letzter Versuch ohne Zertifikatspruefung: manche Behoerden-PDFs liefern eine unvollstaendige
            # Kette. Reachable aber TLS-kaputt ist ein Hinweis, kein toter Link.
            for mode in (["-I"], []):
                try:
                    r = subprocess.run(base[:1] + ["-k"] + mode + base[1:] + [url],
                                       capture_output=True, text=True, timeout=timeout + 5)
                    code = r.stdout.strip()
                    if code and code != "000":
                        return url, "200*"
                except Exception:
                    pass
        if attempt == 0:
            time.sleep(2)
    return url, "000"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=12)
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    found = urls()
    print(f"{len(found)} eindeutige URLs in {len({f for s in found.values() for f in s})} Dateien")
    results: dict[str, str] = {}
    with cf.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for url, code in pool.map(lambda u: check(u, args.timeout), found):
            results[url] = code

    dead = {u: c for u, c in results.items() if c in {"404", "410"}}
    blocked = {u: c for u, c in results.items()
               if c == "000" and not any(h in u for h in BLOCKED_HOSTS)}
    tls = {u: c for u, c in results.items() if c == "200*"}
    known = {u: c for u, c in results.items()
             if c == "000" and any(h in u for h in BLOCKED_HOSTS)}
    ok = len(results) - len(dead) - len(blocked) - len(known) - len(tls)

    if args.all:
        for u, c in sorted(results.items(), key=lambda kv: kv[1]):
            print(f"  {c}  {u}")
    else:
        for u, c in sorted(dead.items()):
            print(f"  TOT   {c}  {u}\n        in: {', '.join(sorted(found[u]))}")
        for u, c in sorted(blocked.items()):
            print(f"  KEINE ANTWORT  {u}\n        in: {', '.join(sorted(found[u]))}")

    for u in sorted(tls):
        print(f"  TLS-Kette unvollstaendig (Inhalt erreichbar): {u}")
    print(f"\n{ok} ok, {len(dead)} tot, {len(blocked)} ohne Antwort, {len(tls)} nur mit -k erreichbar, "
          f"{len(known)} bekannt blockiert (Bot-Schutz, Inhalt per Browser geprueft)")
    return 0 if not dead and not blocked else 1


if __name__ == "__main__":
    sys.exit(main())
