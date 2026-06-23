from validate_plugin import validate

GOOD = {
    "name": "studious",
    "description": "d",
    "version": "2.0.0",
    "author": {"name": "Jacquard Labs"},
    "repository": "https://github.com/jacquardlabs/studious",
    "license": "MIT",
    "keywords": ["review"],
}


def test_good_manifest_passes() -> None:
    assert validate(GOOD) == []


def test_missing_required_field() -> None:
    data = dict(GOOD)
    del data["license"]
    assert any("license" in e for e in validate(data))


def test_bad_semver() -> None:
    data = dict(GOOD)
    data["version"] = "2.0"
    assert any("semver" in e for e in validate(data))


def test_bad_name_pattern() -> None:
    data = dict(GOOD)
    data["name"] = "Studious_X"
    assert any("name" in e for e in validate(data))


def test_author_without_name() -> None:
    data = dict(GOOD)
    data["author"] = {}
    assert any("author.name" in e for e in validate(data))


def test_keywords_must_be_list() -> None:
    data = dict(GOOD)
    data["keywords"] = "review"
    assert any("keywords" in e for e in validate(data))
