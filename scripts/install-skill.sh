#!/usr/bin/env bash
# Symlink a skill from this repo into a Hermes profile's skills directory.
# Usage: ./scripts/install-skill.sh legal/dsgvo-werbewiderspruch [target-skills-dir]
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "usage: $0 <category/skill-name> [target-skills-dir]" >&2
  echo "available:" >&2
  ( cd "$(dirname "$0")/../skills" && find . -maxdepth 2 -name SKILL.md | sed 's#^\./##; s#/SKILL.md##' | sort >&2 )
  exit 1
fi

rel="${1%/}"
src="$(cd "$(dirname "$0")/.." && pwd)/skills/$rel"
target="${2:-$HOME/.hermes/skills}"

[ -f "$src/SKILL.md" ] || { echo "no SKILL.md in $src" >&2; exit 1; }

mkdir -p "$target/$(dirname "$rel")"
dest="$target/$rel"
if [ -e "$dest" ] || [ -L "$dest" ]; then
  echo "exists, not touching: $dest" >&2
  exit 1
fi

ln -s "$src" "$dest"
echo "linked $dest -> $src"
echo "verify: the skill should now show up in Hermes' skills_list"
