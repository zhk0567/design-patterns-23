"""Shortcut: python test_patterns.py -> scripts/test_patterns.py"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import test_patterns as tp

if __name__ == "__main__":
    raise SystemExit(unittest.main(module=tp, verbosity=2))
