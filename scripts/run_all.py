"""Run all 23 design pattern demos in order."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from patterns import PATTERNS, load  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


def main() -> int:
    failed = 0
    for name in PATTERNS:
        print(f"\n{'=' * 60}\n>>> {name}\n{'=' * 60}")
        try:
            load(name).demo()
        except Exception as exc:
            failed += 1
            print(f"[ERROR] {name}: {exc}", file=sys.stderr)
    print(f"\n{'=' * 60}")
    if failed:
        print(f"完成：{len(PATTERNS) - failed}/{len(PATTERNS)} 成功，{failed} 个失败")
        return 1
    print(f"完成：全部 {len(PATTERNS)} 个示例运行成功")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
