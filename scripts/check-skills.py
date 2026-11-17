#!/usr/bin/env python3
"""Repo-weiter Struktur-Check für alle Skills.

Prüft, was bei jedem neuen Skill schiefgeht und im Review leicht übersehen wird:
  1. Layout: skills/<category>/<name>/SKILL.md (genau eine Ebene Kategorie)
  2. Frontmatter: gültiges YAML, `name` == Verzeichnisname, `description` vorhanden
  3. Referenzen: jeder im SKILL.md genannte Pfad (references/, templates/, scripts/)
     existiert — und jede Datei in diesen Ordnern wird im SKILL.md erwähnt.

Aufruf: python3 scripts/check-skills.py [--repo <pfad>]
Exit 0 = alles grün, 1 = Fehler (mit Liste), 2 = Aufruffehler.
"""
import argparse
import glob
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML fehlt (python3 -m pip install pyyaml)")

REF_RE = re.compile(r"(?:references|templates|scripts|assets)/[A-Za-z0-9._<>-]+")
SKIP_DIRS = {"__pycache__", ".git"}


def frontmatter(text):
    """Frontmatter zwischen erster --- Zeile und dem nächsten \n--- ."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return text[3:end]


def check_skill(path, errors, warnings):
    skill_dir = os.path.dirname(path)
    dir_name = os.path.basename(skill_dir)
    category = os.path.basename(os.path.dirname(skill_dir))
    rel = os.path.relpath(path)

    text = open(path, encoding="utf-8").read()
    fm = frontmatter(text)
    if fm is None:
        errors.append(f"{rel}: kein Frontmatter-Block")
        return
    try:
        meta = yaml.safe_load(fm) or {}
    except yaml.YAMLError as exc:
        errors.append(f"{rel}: Frontmatter ist kein gültiges YAML ({exc.__class__.__name__})")
        return

    name = meta.get("name")
    desc = meta.get("description")
    if not name:
        errors.append(f"{rel}: 'name' fehlt im Frontmatter")
    elif name != dir_name:
        errors.append(f"{rel}: name '{name}' != Verzeichnis '{dir_name}'")
    if not desc:
        errors.append(f"{rel}: 'description' fehlt im Frontmatter")
    elif len(desc) > 200:
        warnings.append(f"{rel}: description {len(desc)} Zeichen (Kurzform < 200 hilft beim Auslösen)")

    # Genannte Pfade müssen existieren (Platzhalter mit <...> ausgenommen)
    for ref in sorted(set(REF_RE.findall(text))):
        if "<" in ref or ">" in ref:
            continue
        if not os.path.exists(os.path.join(skill_dir, ref)):
            errors.append(f"{rel}: verweist auf fehlende Datei {ref}")

    # Und umgekehrt: Dateien in den Beiblatt-Ordnern sollten erwähnt sein
    for sub in ("references", "templates", "scripts", "assets"):
        subdir = os.path.join(skill_dir, sub)
        if not os.path.isdir(subdir):
            continue
        mentioned = set(REF_RE.findall(text))
        for f in sorted(os.listdir(subdir)):
            if f.startswith(".") or f in SKIP_DIRS:
                continue
            full = os.path.join(subdir, f)
            if os.path.isdir(full) and not glob.glob(os.path.join(full, "**", "*"), recursive=True):
                continue
            relref = f"{sub}/{f}"
            if os.path.isdir(full):
                if not any(m.startswith(relref + "/") for m in mentioned):
                    warnings.append(f"{rel}: Ordner {relref}/ wird im SKILL.md nicht erwähnt")
            elif relref not in mentioned:
                warnings.append(f"{rel}: {relref} wird im SKILL.md nicht erwähnt")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    args = ap.parse_args()

    root = os.path.join(args.repo, "skills")
    if not os.path.isdir(root):
        sys.exit(f"kein skills/ unter {args.repo}")

    errors, warnings = [], []
    skills, stray = [], []
    for cat in sorted(os.listdir(root)):
        catdir = os.path.join(root, cat)
        if not os.path.isdir(catdir) or cat.startswith("."):
            continue
        entries = [e for e in sorted(os.listdir(catdir)) if not e.startswith(".")]
        if os.path.exists(os.path.join(catdir, "SKILL.md")):
            stray.append(f"skills/{cat}/SKILL.md liegt ohne Skill-Verzeichnis")
            continue
        for name in entries:
            skilldir = os.path.join(catdir, name)
            if not os.path.isdir(skilldir):
                continue
            md = os.path.join(skilldir, "SKILL.md")
            if not os.path.exists(md):
                errors.append(f"skills/{cat}/{name}: SKILL.md fehlt")
                continue
            skills.append(f"{cat}/{name}")
            check_skill(md, errors, warnings)

    for e in errors:
        print(f"FEHLER   {e}")
    for w in warnings:
        print(f"HINWEIS  {w}")
    print(f"\n{len(skills)} Skills geprüft: {len(errors)} Fehler, {len(warnings)} Hinweise")
    return 1 if errors or stray else 0


if __name__ == "__main__":
    sys.exit(main())
