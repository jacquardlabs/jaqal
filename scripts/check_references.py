#!/usr/bin/env python3
"""Verify every @agent-* and internal-skill reference in commands/ and agents/ resolves.

Run from CI to catch broken cross-references (e.g. an agent rename that orphans a
command's @agent-* reference). Standard library only.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCAN_DIRS = ("commands", "agents")
AGENT_RE = re.compile(r"@agent-([a-z0-9-]+)")
# "the `<name>` skill" is the codebase's phrasing for a skill reference.
SKILL_RE = re.compile(r"the `([a-z0-9-]+)` skill")
# Skills referenced by name but legitimately shipped elsewhere, not in this repo.
EXTERNAL_SKILLS = {"web-design-guidelines"}


def find_broken(root: Path) -> list[str]:
    errors: list[str] = []
    for sub in SCAN_DIRS:
        base = root / sub
        if not base.is_dir():
            continue
        for md in sorted(base.rglob("*.md")):
            text = md.read_text(encoding="utf-8")
            rel = md.relative_to(root)
            for name in sorted(set(AGENT_RE.findall(text))):
                if not (root / "agents" / f"{name}.md").is_file():
                    errors.append(
                        f"@agent-{name} referenced in {rel} but agents/{name}.md missing"
                    )
            for name in sorted(set(SKILL_RE.findall(text))):
                if name in EXTERNAL_SKILLS:
                    continue
                if not (root / "skills" / name).is_dir():
                    errors.append(
                        f"skill `{name}` referenced in {rel} but skills/{name}/ missing"
                    )
    return errors


def main() -> int:
    errors = find_broken(REPO)
    if errors:
        print("Reference check FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("Reference check passed: all @agent-* and skill references resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
