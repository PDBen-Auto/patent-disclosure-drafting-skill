from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_required_files_exist():
    required = [
        "SKILL.md",
        "agents/openai.yaml",
        "references/workflow.md",
        "references/intake-and-output-contract.md",
        "references/figure-numbering.md",
        "references/anonymization.md",
        "references/example-modular-desk-lamp.md",
        "tests/trigger-cases.md",
        "README.md",
        "LICENSE",
    ]
    missing = [path for path in required if not (ROOT / path).is_file()]
    assert not missing, missing


def test_frontmatter_and_boundary():
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    assert text.startswith("---\nname: patent-disclosure-drafting\n")
    assert "Implementation Basis And Dependencies" in text
    assert "## Inputs" in text
    assert "## Outputs" in text
    assert "不是律师意见" not in text
    assert "patent counsel" in text


if __name__ == "__main__":
    test_required_files_exist()
    test_frontmatter_and_boundary()
    print("patent disclosure drafting structure checks passed")
