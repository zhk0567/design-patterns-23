"""Generate docs/CHEATSHEET.md from pattern module docstrings."""

from __future__ import annotations

import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "docs" / "CHEATSHEET.md"
PATTERN_FILES = sorted(ROOT.glob("[0-9][0-9]_*.py"))


def _field(doc: str, label: str) -> str:
    match = re.search(rf"^{label}[：:]\s*(.+)$", doc, re.MULTILINE)
    return match.group(1).strip() if match else "—"


def _parse_file(path: Path) -> dict[str, str]:
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    doc = ast.get_docstring(tree) or ""
    first_line = doc.strip().split("\n")[0] if doc else path.stem
    return {
        "file": path.name,
        "title": first_line,
        "intent": _field(doc, "意图"),
        "use_case": _field(doc, "适用"),
    }


def _render(rows: list[dict[str, str]]) -> str:
    lines = [
        "# 设计模式速查表",
        "",
        "> 由 `generate_cheatsheet.py` 从各模块 docstring 自动生成，请勿手改。",
        "> 重新生成: `python generate_cheatsheet.py`",
        "",
        "| # | 文件 | 模式 | 意图 | 适用 |",
        "|---|------|------|------|------|",
    ]
    for i, row in enumerate(rows, start=1):
        lines.append(
            f"| {i:02} | `{row['file']}` | {row['title']} | {row['intent']} | {row['use_case']} |"
        )
    lines.extend(
        [
            "",
            "## 运行",
            "",
            "```powershell",
            "python learn.py",
            "python run_all.py",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    rows = [_parse_file(p) for p in PATTERN_FILES]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(_render(rows), encoding="utf-8")
    print(f"[cheatsheet] wrote {OUTPUT} ({len(rows)} patterns)")


if __name__ == "__main__":
    main()
