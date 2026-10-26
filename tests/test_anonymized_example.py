import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = (ROOT / "references/example-modular-desk-lamp.md").read_text(encoding="utf-8")


def test_example_is_synthetic_and_contains_no_source_identifiers():
    assert "fully synthetic" in EXAMPLE
    assert not re.search(r"[A-Za-z]:[/\\]", EXAMPLE)
    assert not re.search(r"\b\d{2,}\.(?:3dm|step|stp|pptx?|docx?)\b", EXAMPLE, re.I)
    assert not re.search(r"\b(?:ASIN|SKU|patent number)\s*[:#]\s*\S+", EXAMPLE, re.I)


if __name__ == "__main__":
    test_example_is_synthetic_and_contains_no_source_identifiers()
    print("synthetic example redaction checks passed")
