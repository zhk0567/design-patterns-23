"""Smoke tests for demo_async() on proxy, command, observer."""

from __future__ import annotations

import asyncio
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from patterns import load, unload  # noqa: E402

ASYNC_MODULES = ["12_proxy", "14_command", "19_observer"]


class AsyncDemoTests(unittest.TestCase):
    def test_async_demos_run(self) -> None:
        for name in ASYNC_MODULES:
            with self.subTest(pattern=name):
                unload(name)
                module = load(name)
                asyncio.run(module.demo_async())


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(unittest.main(verbosity=2))
