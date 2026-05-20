"""Run asyncio demos for patterns that support demo_async()."""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from patterns import load  # noqa: E402

ASYNC_MODULES = [
    "12_proxy",
    "14_command",
    "19_observer",
]


async def _run_all() -> int:
    failed = 0
    for name in ASYNC_MODULES:
        print(f"\n{'=' * 50}\n>>> {name} (async)\n{'=' * 50}")
        try:
            module = load(name)
            await module.demo_async()
        except Exception as exc:
            failed += 1
            print(f"[ERROR] {name}: {exc}", file=sys.stderr)
    if failed:
        print(f"\nasync demos: {len(ASYNC_MODULES) - failed}/{len(ASYNC_MODULES)} ok")
        return 1
    print(f"\nasync demos: all {len(ASYNC_MODULES)} ok")
    return 0


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    return asyncio.run(_run_all())


if __name__ == "__main__":
    raise SystemExit(main())
