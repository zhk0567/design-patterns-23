"""Inject English summary block into each pattern module docstring."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERNS_DIR = ROOT / "patterns"

EN_BLOCKS: dict[str, str] = {
    "01_singleton.py": """
English (Singleton):
- Intent: Ensure a class has only one instance and a global access point.
- Use when: Shared config, loggers, connection pools.
- Pitfalls: Not thread-safe; god-object singleton; unnecessary complexity.""",
    "02_factory_method.py": """
English (Factory Method):
- Intent: Let subclasses decide which class to instantiate.
- Use when: Product families grow (loggers, exporters).
- Pitfalls: Confused with simple factory; too many factory subclasses.""",
    "03_abstract_factory.py": """
English (Abstract Factory):
- Intent: Create families of related products without naming concrete classes.
- Use when: Switching UI themes, platform kits.
- Pitfalls: Overkill for single products; interface bloat.""",
    "04_builder.py": """
English (Builder):
- Intent: Separate construction of a complex object from its representation.
- Use when: HTTP requests, SQL, stepwise configs.
- Pitfalls: Over-engineering simple objects; invalid partial states.""",
    "05_prototype.py": """
English (Prototype):
- Intent: Clone existing instances instead of constructing from scratch.
- Use when: Expensive setup, document drafts.
- Pitfalls: Shallow copy sharing mutable state; cloning non-cloneable resources.""",
    "06_adapter.py": """
English (Adapter):
- Intent: Convert one interface into another clients expect.
- Use when: Legacy SDKs, third-party APIs.
- Pitfalls: Confused with Decorator; god adapter.""",
    "07_bridge.py": """
English (Bridge):
- Intent: Split abstraction and implementation so both vary independently.
- Use when: Shape x renderer, message x channel.
- Pitfalls: Confused with Strategy; too many layers.""",
    "08_composite.py": """
English (Composite):
- Intent: Treat individual objects and compositions uniformly.
- Use when: File trees, org charts, menus.
- Pitfalls: Leaf nodes with container-only APIs; deep recursion.""",
    "09_decorator.py": """
English (Decorator):
- Intent: Attach responsibilities dynamically without subclass explosion.
- Use when: Coffee add-ons, stream wrappers.
- Pitfalls: vs Python @decorator syntax; order of wrappers matters.""",
    "10_facade.py": """
English (Facade):
- Intent: Provide a simple interface to a complex subsystem.
- Use when: Checkout flows, boot sequences.
- Pitfalls: God facade; clients bypass facade.""",
    "11_flyweight.py": """
English (Flyweight):
- Intent: Share intrinsic state to support many fine-grained objects.
- Use when: Text glyphs, map tiles.
- Pitfalls: Extrinsic state inside flyweight; unbounded pool.""",
    "12_proxy.py": """
English (Proxy):
- Intent: Control access to another object (lazy load, protection).
- Use when: Heavy images, remote services.
- Pitfalls: vs Decorator; race on lazy init.""",
    "13_chain_of_responsibility.py": """
English (Chain of Responsibility):
- Intent: Pass a request along a chain until someone handles it.
- Use when: Approval flows, middleware, filters.
- Pitfalls: Silent drop at chain end; performance chains.""",
    "14_command.py": """
English (Command):
- Intent: Encapsulate a request as an object (undo, queue).
- Use when: Undo/redo, job queues.
- Pitfalls: Fat commands; unbounded undo stack.""",
    "15_interpreter.py": """
English (Interpreter):
- Intent: Define grammar and interpret sentences in the language.
- Use when: Simple DSLs, rule expressions.
- Pitfalls: Complex grammar; poor performance on hot paths.""",
    "16_iterator.py": """
English (Iterator):
- Intent: Sequential access without exposing internal structure.
- Use when: Custom collections, paging.
- Pitfalls: Concurrent modification; leaking internals.""",
    "17_mediator.py": """
English (Mediator):
- Intent: Centralize how colleagues interact.
- Use when: Chat rooms, form coordination.
- Pitfalls: God mediator; hidden direct references.""",
    "18_memento.py": """
English (Memento):
- Intent: Capture and restore internal state without breaking encapsulation.
- Use when: Editor undo, save games.
- Pitfalls: Huge history; unsafe pickle of mementos.""",
    "19_observer.py": """
English (Observer):
- Intent: Notify dependents automatically on state change.
- Use when: Events, stock ticks, MVC updates.
- Pitfalls: Notification loops; memory leaks without unsubscribe.""",
    "20_state.py": """
English (State):
- Intent: Change behavior when internal state changes.
- Use when: Order workflows, TCP states.
- Pitfalls: vs Strategy; state class explosion.""",
    "21_strategy.py": """
English (Strategy):
- Intent: Encapsulate interchangeable algorithms.
- Use when: Sorting, pricing, routing.
- Pitfalls: One algorithm only; client knows all strategies.""",
    "22_template_method.py": """
English (Template Method):
- Intent: Define algorithm skeleton; subclasses fill steps.
- Use when: Export pipelines, game turns.
- Pitfalls: Rigid inheritance; hidden step dependencies.""",
    "23_visitor.py": """
English (Visitor):
- Intent: Add operations on elements without changing their classes.
- Use when: AST walks, file trees, reports.
- Pitfalls: New element types break all visitors; interface growth.""",
}


def inject(path: Path, block: str) -> None:
    text = path.read_text(encoding="utf-8")
    if "English (" in text or "English (Singleton)" in text:
        print("skip", path.name)
        return
    marker = "\n类图 (Mermaid):"
    if marker not in text:
        print("no marker", path.name)
        return
    text = text.replace(marker, block + marker, 1)
    path.write_text(text, encoding="utf-8")
    print("updated", path.name)


def main() -> None:
    for name, block in EN_BLOCKS.items():
        inject(PATTERNS_DIR / name, block)


if __name__ == "__main__":
    main()
