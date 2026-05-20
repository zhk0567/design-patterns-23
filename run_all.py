"""Shortcut: python run_all.py -> scripts/run_all.py"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.run_all import main

if __name__ == "__main__":
    raise SystemExit(main())
