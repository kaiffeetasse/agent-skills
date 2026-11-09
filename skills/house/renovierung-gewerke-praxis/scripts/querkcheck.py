#!/usr/bin/env python3
"""Quercheck: findet widersprüchliche Zahlen zwischen den Playbooks.

Zweck: derselbe Sachverhalt (z. B. "Estrich je Quadratmeter") steht in zwei Dateien mit
unterschiedlichen Bändern. Das fällt bei der Arbeit an einer Datei nicht auf, ist aber der
Fehler, den ein Leser zuerst bemerkt.

Vorgehen:
1. Alle Zahlenspannen ("12–18", "12 bis 18", "12-18") mit Einheit einsammeln.
2. Schluessel = die zwei inhaltsragenden Woerter vor der Zahl (Thema), plus Einheit.
3. Gruppen mit mehr als einer Spanne aus verschiedenen Dateien werden gemeldet.

Das ist eine Heuristik, kein Beweis: Treffer werden als "prüfen" ausgegeben, nicht als Fehler.
Exit-Code 1, wenn Treffer vorliegen (für CI nutzbar mit --fail).
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
PLAYBOOKS = BASE / "references" / "playbooks"
KNOWN_FILE = BASE / "references" / "querkcheck-bekannt.json"


def load_known() -> set[tuple[str, str]]:
    """Bereits geprueft und fuer unbedenklich erklaert: (Sachbegriff, Einheit)."""
    if not KNOWN_FILE.exists():
        return set()
    try:
        data = json.loads(KNOWN_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return set()
    return {(item["noun"], item["unit"]) for item in data if "noun" in item and "unit" in item}

UNITS = [
    "€/m²", "€/m2", "€/m³", "€/m", "€/kWh", "€/l", "€/h", "€/t", "€/Stück", "€/Tag", "€",
    "ct/kWh", "kWh/m²a", "kWh/a", "kWh", "W/m²K", "W/m²", "Bq/m³", "dB(A)", "dB",
    "mm", "cm", "m²", "m³", "Stunden", "Jahre", "Tage", "Wochen", "Monate", "%", "bar", "°C",
]

SPAN = re.compile(
    r"(\d+(?:[.,]\d+)?)\s*(?:–|—|-|bis)\s*(\d+(?:[.,]\d+)?)\s*(" + "|".join(re.escape(u) for u in UNITS) + r")\b"
)

STOPWORDS = {
    "der", "die", "das", "den", "dem", "des", "ein", "eine", "einer", "eines", "einem",
    "und", "oder", "bei", "für", "mit", "von", "im", "in", "am", "an", "auf", "aus",
    "je", "pro", "etwa", "rund", "circa", "ca", "bis", "sind", "ist", "wird", "werden",
    "kosten", "kostet", "liegt", "liegen", "zwischen", "nach", "vor", "als", "auch",
    "nicht", "nur", "mehr", "weniger", "maximal", "mindestens", "typisch", "realistisch",
    # generische Fuellwoerter, die keinen Sachverhalt beschreiben
    "preise", "preis", "inkl", "mwst", "orientierungswerte", "quelle", "quellen", "darüber",
    "alle", "gesamtpreis", "materialkosten", "variante", "beispiel", "tabelle", "zeile",
    "steht", "stehen", "gilt", "gelten", "wenn", "dann", "dass", "sich", "hier", "dort",
}


def normalize_num(value: str) -> float:
    return float(value.replace(".", "").replace(",", "."))


def context_tokens(text: str, start: int, end: int) -> set[str]:
    """Inhaltswoerter im Umfeld einer Spanne — Grundlage fuer den Themenvergleich."""
    chunk = text[max(0, start - 140): min(len(text), end + 90)]
    tokens = re.findall(r"[A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß\-]{2,}", chunk)
    return {t.lower() for t in tokens if t.lower() not in STOPWORDS}


# Sachbegriffe, bei denen ein unterschiedliches Zahlenband ein echter Widerspruch ist.
# Bewusst eine kuratierte Liste statt Ahnlichkeitsmass: "Pflaster Betonstein 110-135" und
# "Pflaster Naturstein 180-240" sind kein Widerspruch, "Zementestrich 20-35" und
# "Zementestrich 15-35" schon.
KEY_NOUNS = [
    "zementestrich", "calciumsulfat", "anhydrit", "fliessestrich", "fließestrich", "estrich",
    "fliesen", "fliesenleger", "verlegung", "abdichtung", "verbundabdichtung",
    "trockenbau", "trockenbaudecke", "vorsatzschale", "tragprofil", "cd-profil",
    "wdvs", "fassadendämmung", "aufsparrendämmung", "einblasdämmung", "kellerdeckendämmung",
    "mineralwolle", "holzfaser", "zellulose", "eps", "xps", "pu-schaum",
    "waermepumpe", "wärmepumpe", "luft-wasser", "sole", "heizlast", "jahresarbeitszahl",
    "fussbodenheizung", "fußbodenheizung", "heizkörper", "heizkoerper", "pufferspeicher",
    "photovoltaik", "pv-anlage", "batteriespeicher", "speicher", "wallbox",
    "zaehlerschrank", "zählerschrank", "unterverteilung", "stromkreis", "fi-schutzschalter",
    "rcd", "leitungsquerschnitt", "kabelkanal", "leerrohr",
    "fenster", "haustuer", "haustür", "tuerblatt", "türblatt", "zarge", "kompriband",
    "dachziegel", "dacheindeckung", "dachdaemmung", "dachdämmung", "dachstuhl",
    "treppe", "treppenstufe", "auftritt", "steigung", "gelaender", "geländer",
    "kueche", "küche", "arbeitsplatte", "arbeitshoehe", "arbeitshöhe",
    "bad", "dusche", "wanne", "wc", "waschtisch", "vorwand",
    "fliesenkleber", "daemmschicht", "dämmschicht", "ausgleichsmasse", "spachtelmasse",
    "farbe", "grundierung", "putz", "verputz",
    "pflaster", "pflastern", "asphalt", "terrasse", "terrassendielen",
    "kellerabdichtung", "mauerwerk", "radon", "legionellen", "trinkwasser",
]


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def collect():
    found = defaultdict(list)
    for path in sorted(PLAYBOOKS.glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in SPAN.finditer(text):
            low = normalize_num(match.group(1))
            high = normalize_num(match.group(2))
            if low > high:
                low, high = high, low
            unit = match.group(3)
            ctx = context_tokens(text, match.start(), match.end())
            if len(ctx) < 4:
                continue
            window = text[max(0, match.start() - 60): min(len(text), match.end() + 25)].lower()
            nouns = [n for n in KEY_NOUNS if n in window]
            if not nouns:
                continue
            found[unit].append(
                {
                    "file": path.name,
                    "span": f"{match.group(1)}–{match.group(2)} {unit}",
                    "low": low,
                    "high": high,
                    "line": text[: match.start()].count("\n") + 1,
                    "ctx": ctx,
                    "nouns": nouns,
                }
            )
    return found


# Nur bei diesen Einheiten ist ein abweichendes Band ein Widerspruch.
# Zeitangaben (Tage/Wochen/Jahre) sind zu kontextabhaengig und werden nicht ueber Sachbegriffe verglichen.
MEASURE_UNITS = {"€/m²", "€/m2", "€/m³", "€/m", "€/kWh", "€/l", "€/h", "€/t", "€/Stück", "€/Tag",
                 "ct/kWh", "W/m²K", "W/m²", "Bq/m³", "dB(A)", "dB", "bar"}


def conflicts(found, max_examples: int = 3):
    """Gruppiert nach (Sachbegriff neben der Zahl, Einheit) und meldet getrennte Bänder.

    Der Sachbegriff muss NAHE an der Zahl stehen (60 Zeichen davor) — "Putz" in einem Absatz
    ueber Fassade darf nicht jede Putzarbeit im Haus mit dem WDVS-Preis verbinden.
    """
    groups = {}
    for unit, hits in found.items():
        if unit not in MEASURE_UNITS:
            continue
        for hit in hits:
            for noun in hit["nouns"][:1]:
                groups.setdefault((noun, unit), []).append(hit)

    out = []
    for (noun, unit), hits in groups.items():
        if len(hits) < 2:
            continue
        # nur Stellen mit wirklich getrennten Baendern
        hits.sort(key=lambda h: h["low"])
        chosen = []
        for hit in hits:
            if any(
                (hit["high"] < c["low"] or c["high"] < hit["low"])
                and (hit["file"] != c["file"] or abs(hit["line"] - c["line"]) >= 15)
                for c in chosen
            ) or not chosen:
                chosen.append(hit)
        if len(chosen) < 2:
            continue
        clean = [
            {k: v for k, v in h.items() if k not in ("ctx", "nouns")} for h in chosen[:max_examples]
        ]
        out.append(
            {
                "noun": noun,
                "unit": unit,
                "files": sorted({h["file"] for h in chosen}),
                "hits": clean,
            }
        )
    out.sort(key=lambda x: (-len(x["files"]), x["noun"]))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true", help="Maschinenlesbar ausgeben")
    ap.add_argument("--fail", action="store_true", help="Exit 1, wenn Treffer vorliegen")
    ap.add_argument("--limit", type=int, default=40)
    args = ap.parse_args()

    found = collect()
    all_hits = conflicts(found)
    known = load_known()
    hits = [h for h in all_hits if (h["noun"], h["unit"]) not in known]
    suppressed = len(all_hits) - len(hits)
    if args.json:
        print(json.dumps(hits[: args.limit], ensure_ascii=False, indent=2))
    else:
        total = sum(len(v) for v in found.values())
        print(f"{total} Zahlenspannen mit Einheit erfasst, {len(hits)} offene Themen mit getrennten Bändern"
              f" ({suppressed} bereits geprüft und in references/querkcheck-bekannt.json als unbedenklich vermerkt)\n")
        for item in hits[: args.limit]:
            print(f"— {item['noun']} ({item['unit']})")
            for h in item["hits"]:
                print(f"    {h['span']:<22} {h['file']}:{h['line']}")
        if len(hits) > args.limit:
            print(f"\n… {len(hits) - args.limit} weitere")
        print(
            "\nHinweis: Heuristik. Ein Treffer heißt „zwei Dateien nennen für dasselbe Thema"
            " verschiedene Bänder\" — nicht automatisch Fehler (Ausstattung, Region, Jahrgang)."
        )
    return 1 if (hits and args.fail) else 0


if __name__ == "__main__":
    sys.exit(main())
