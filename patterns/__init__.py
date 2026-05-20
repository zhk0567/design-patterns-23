"""23 GoF design pattern demo modules (numbered filenames)."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType

PATTERNS_DIR = Path(__file__).resolve().parent

PATTERNS: list[str] = [
    "01_singleton",
    "02_factory_method",
    "03_abstract_factory",
    "04_builder",
    "05_prototype",
    "06_adapter",
    "07_bridge",
    "08_composite",
    "09_decorator",
    "10_facade",
    "11_flyweight",
    "12_proxy",
    "13_chain_of_responsibility",
    "14_command",
    "15_interpreter",
    "16_iterator",
    "17_mediator",
    "18_memento",
    "19_observer",
    "20_state",
    "21_strategy",
    "22_template_method",
    "23_visitor",
]


def load(name: str) -> ModuleType:
    """Load a pattern module by stem name (e.g. ``01_singleton``)."""
    path = PATTERNS_DIR / f"{name}.py"
    if not path.is_file():
        raise ModuleNotFoundError(f"pattern not found: {name}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load pattern: {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def unload(name: str) -> None:
    """Remove cached module so the next ``load`` re-executes the file."""
    import sys

    sys.modules.pop(name, None)
