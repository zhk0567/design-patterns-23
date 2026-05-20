"""Smoke tests for all 23 design pattern demos (stdlib unittest only)."""

from __future__ import annotations

import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from patterns import PATTERNS, load, unload  # noqa: E402

EXPECTED_MARKERS: dict[str, str] = {
    "01_singleton": "[Singleton]",
    "02_factory_method": "[Console]",
    "03_abstract_factory": "[AbstractFactory]",
    "04_builder": "[Builder]",
    "05_prototype": "[Prototype]",
    "06_adapter": "[Adapter]",
    "07_bridge": "[Bridge]",
    "08_composite": "[Composite]",
    "09_decorator": "[Decorator]",
    "10_facade": "[Facade]",
    "11_flyweight": "[Flyweight]",
    "12_proxy": "[Proxy]",
    "13_chain_of_responsibility": "[ChainOfResponsibility]",
    "14_command": "[Command]",
    "15_interpreter": "[Interpreter]",
    "16_iterator": "[Iterator]",
    "17_mediator": "[Mediator]",
    "18_memento": "[Memento]",
    "19_observer": "[Observer]",
    "20_state": "[State]",
    "21_strategy": "[Strategy]",
    "22_template_method": "[TemplateMethod]",
    "23_visitor": "[Visitor]",
}


class PatternSmokeTests(unittest.TestCase):
    def test_pattern_count(self) -> None:
        self.assertEqual(len(PATTERNS), 23)

    def test_each_demo_runs(self) -> None:
        for name in PATTERNS:
            with self.subTest(pattern=name):
                unload(name)
                module = load(name)
                buffer = io.StringIO()
                with redirect_stdout(buffer):
                    module.demo()
                output = buffer.getvalue()
                self.assertTrue(output.strip(), f"{name}: demo() produced no output")
                marker = EXPECTED_MARKERS[name]
                self.assertIn(marker, output, f"{name}: missing marker {marker!r}")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(unittest.main(verbosity=2))
