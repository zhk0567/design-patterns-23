"""Unit tests for selected pattern logic (not smoke print tests)."""

from __future__ import annotations

import sys
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from patterns import load  # noqa: E402


class SingletonTests(unittest.TestCase):
    def test_thread_safe_singleton_unique_instance(self) -> None:
        mod = load("01_singleton")

        def create_id() -> int:
            return id(mod.ThreadSafeAppConfig())

        with ThreadPoolExecutor(max_workers=8) as pool:
            ids = list(pool.map(lambda _: create_id(), range(32)))
        self.assertEqual(len(set(ids)), 1)


class ChainTests(unittest.TestCase):
    def test_dynamic_chain_remove_handler(self) -> None:
        mod = load("13_chain_of_responsibility")
        chain = mod.DynamicApprovalChain()
        manager = mod.Manager()
        director = mod.Director()
        chain.add_handler(manager)
        chain.add_handler(director)
        self.assertIn("总监", chain.handle(3000))
        chain.remove_handler(director)
        self.assertEqual(chain.handle(3000), "未审批")


class InterpreterTests(unittest.TestCase):
    def test_compound_expression(self) -> None:
        mod = load("15_interpreter")
        expr = mod.Subtract(
            mod.Multiply(mod.Add(mod.Variable("x"), mod.Number(10)), mod.Number(2)),
            mod.Number(3),
        )
        self.assertEqual(expr.interpret({"x": 5}), 27)


if __name__ == "__main__":
    raise SystemExit(unittest.main(verbosity=2))
