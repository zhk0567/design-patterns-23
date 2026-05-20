"""Smoke test for ecommerce_demo main()."""

from __future__ import annotations

import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import ecommerce_demo  # noqa: E402


class EcommerceDemoTests(unittest.TestCase):
    def test_main_runs(self) -> None:
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = ecommerce_demo.main()
        self.assertEqual(code, 0)
        out = buf.getvalue()
        self.assertIn("[Ecommerce]", out)
        self.assertIn("[Ecommerce][Chain]", out)
        self.assertIn("Command", out)
        self.assertIn("取消", out)


if __name__ == "__main__":
    raise SystemExit(unittest.main(verbosity=2))
