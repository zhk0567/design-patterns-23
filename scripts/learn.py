"""Interactive menu to run design pattern demos."""

from __future__ import annotations

import sys
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from patterns import PATTERNS, load  # noqa: E402

PATTERN_META: list[tuple[str, str, str, str]] = [
    # (module, en, zh, category)
    ("01_singleton", "Singleton", "单例", "creational"),
    ("02_factory_method", "Factory Method", "工厂方法", "creational"),
    ("03_abstract_factory", "Abstract Factory", "抽象工厂", "creational"),
    ("04_builder", "Builder", "建造者", "creational"),
    ("05_prototype", "Prototype", "原型", "creational"),
    ("06_adapter", "Adapter", "适配器", "structural"),
    ("07_bridge", "Bridge", "桥接", "structural"),
    ("08_composite", "Composite", "组合", "structural"),
    ("09_decorator", "Decorator", "装饰器", "structural"),
    ("10_facade", "Facade", "外观", "structural"),
    ("11_flyweight", "Flyweight", "享元", "structural"),
    ("12_proxy", "Proxy", "代理", "structural"),
    ("13_chain_of_responsibility", "Chain of Responsibility", "责任链", "behavioral"),
    ("14_command", "Command", "命令", "behavioral"),
    ("15_interpreter", "Interpreter", "解释器", "behavioral"),
    ("16_iterator", "Iterator", "迭代器", "behavioral"),
    ("17_mediator", "Mediator", "中介者", "behavioral"),
    ("18_memento", "Memento", "备忘录", "behavioral"),
    ("19_observer", "Observer", "观察者", "behavioral"),
    ("20_state", "State", "状态", "behavioral"),
    ("21_strategy", "Strategy", "策略", "behavioral"),
    ("22_template_method", "Template Method", "模板方法", "behavioral"),
    ("23_visitor", "Visitor", "访问者", "behavioral"),
]

CATEGORY_LABEL = {
    "creational": "创建型",
    "structural": "结构型",
    "behavioral": "行为型",
}

_NAME_INDEX: dict[str, tuple[str, str, str, str]] = {m[0]: m for m in PATTERN_META}
_NAME_INDEX.update({m[0].split("_", 1)[-1]: m for m in PATTERN_META if "_" in m[0]})


def _configure_stdio() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")


def _filtered_meta(category: str | None) -> list[tuple[str, str, str, str]]:
    if not category or category == "all":
        return PATTERN_META
    return [m for m in PATTERN_META if m[3] == category]


def _print_menu(category: str | None = None) -> list[tuple[str, str, str, str]]:
    items = _filtered_meta(category)
    cat_label = CATEGORY_LABEL.get(category or "", "全部")
    print("\n" + "=" * 50)
    print(f"  23 种设计模式 — 交互学习 [{cat_label}]")
    print("=" * 50)
    for i, (mod, en, zh, _) in enumerate(items, start=1):
        print(f"  {i:2}. {mod:32} {zh} ({en})")
    print("   0. 退出")
    print("  c.   切换分类 (creational/structural/behavioral/all)")
    print("  all.  运行全部 demo()")
    print("  async. 运行异步 demo_async()")
    print("  支持输入编号、模块名 (如 12_proxy / proxy)")
    print("=" * 50)
    return items


def _run_module(name: str, mode: str) -> None:
    module = load(name)
    if mode == "async":
        import asyncio

        asyncio.run(_run_async(module, mode))
        return
    if mode == "basic" and hasattr(module, "demo_basic"):
        module.demo_basic()
    elif mode == "advanced" and hasattr(module, "demo_advanced"):
        module.demo_advanced()
    else:
        module.demo()


async def _run_async(module: ModuleType, mode: str) -> None:
    if mode == "async" and hasattr(module, "demo_async"):
        await module.demo_async()
    elif mode == "basic" and hasattr(module, "demo_basic"):
        module.demo_basic()
    elif mode == "advanced" and hasattr(module, "demo_advanced"):
        module.demo_advanced()
    else:
        module.demo()


def _pick_mode(module: ModuleType) -> str:
    has_basic = hasattr(module, "demo_basic")
    has_advanced = hasattr(module, "demo_advanced")
    has_async = hasattr(module, "demo_async")
    if not (has_basic or has_advanced or has_async):
        return "demo"
    opts = "[1] demo  [2] demo_basic  [3] demo_advanced"
    if has_async:
        opts += "  [4] demo_async"
    print(f"  运行模式: {opts}")
    choice = input("  选择 (默认 1): ").strip() or "1"
    return {"1": "demo", "2": "basic", "3": "advanced", "4": "async"}.get(choice, "demo")


def _resolve_selection(
    raw: str, items: list[tuple[str, str, str, str]]
) -> tuple[str, str, str] | None:
    if raw in _NAME_INDEX:
        mod, en, zh, _ = _NAME_INDEX[raw]
        return mod, en, zh
    try:
        idx = int(raw)
        if 1 <= idx <= len(items):
            mod, en, zh, _ = items[idx - 1]
            return mod, en, zh
    except ValueError:
        pass
    return None


def main() -> int:
    _configure_stdio()
    category: str | None = None

    while True:
        items = _print_menu(category)
        raw = input("编号/模块名 / c / all / async / 0: ").strip().lower()
        if raw in ("0", "q", "quit", "exit"):
            print("再见。")
            return 0
        if raw == "c":
            category = (
                input("分类 (creational/structural/behavioral/all): ").strip().lower() or None
            )
            if category == "all":
                category = None
            continue
        if raw == "all":
            from scripts import run_all

            return run_all.main()
        if raw == "async":
            from scripts import run_async_demos

            return run_async_demos.main()

        resolved = _resolve_selection(raw, items)
        if not resolved:
            print("无效输入，请重试。")
            continue

        mod, en, zh = resolved
        print(f"\n>>> {mod} — {zh} ({en})\n")
        module = load(mod)
        mode = _pick_mode(module)
        try:
            _run_module(mod, mode)
        except Exception as exc:
            print(f"[learn] 运行失败: {exc}", file=sys.stderr)
            return 1
        input("\n按 Enter 返回菜单...")


if __name__ == "__main__":
    raise SystemExit(main())
