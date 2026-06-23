from pathlib import Path

from check_references import find_broken


def _write(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def test_resolves_clean(tmp_path: Path) -> None:
    _write(tmp_path / "agents" / "security-auditor.md", "x")
    _write(tmp_path / "commands" / "gate.md", "Use @agent-security-auditor here")
    assert find_broken(tmp_path) == []


def test_flags_dangling_agent(tmp_path: Path) -> None:
    _write(tmp_path / "commands" / "gate.md", "Use @agent-ghost here")
    errors = find_broken(tmp_path)
    assert len(errors) == 1
    assert "agents/ghost.md missing" in errors[0]


def test_allows_external_skill(tmp_path: Path) -> None:
    _write(tmp_path / "commands" / "gate.md", "invoke the `web-design-guidelines` skill")
    assert find_broken(tmp_path) == []


def test_flags_missing_internal_skill(tmp_path: Path) -> None:
    _write(tmp_path / "commands" / "gate.md", "invoke the `ghost-skill` skill")
    errors = find_broken(tmp_path)
    assert any("skills/ghost-skill/ missing" in e for e in errors)


def test_passes_when_internal_skill_exists(tmp_path: Path) -> None:
    (tmp_path / "skills" / "real-skill").mkdir(parents=True)
    _write(tmp_path / "commands" / "gate.md", "invoke the `real-skill` skill")
    assert find_broken(tmp_path) == []
