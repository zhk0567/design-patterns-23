"""Interactive menu to run design pattern demos."""

from __future__ import annotations

import importlib
import sys

from run_all import PATTERNS

# (module, English, Chinese)
PATTERN_META: list[tuple[str, str, str]] = [
    ("01_singleton", "Singleton", "单例"),
    ("02_factory_method", "Factory Method", "工厂方法"),
    ("03_abstract_factory", "Abstract Factory", "抽象工厂"),
    ("04_builder", "Builder", "建造者"),
    ("05_prototype", "Prototype", "原型"),
    ("06_adapter", "Adapter", "适配器"),
    ("07_bridge", "Bridge", "桥接"),
    ("08_composite", "Composite", "组合"),
    ("09_decorator", "Decorator", "装饰器"),
    ("10_facade", "Facade", "外观"),
    ("11_flyweight", "Flyweight", "享元"),
    ("12_proxy", "Proxy", "代理"),
    ("13_chain_of_responsibility", "Chain of Responsibility", "责任链"),
    ("14_command", "Command", "命令"),
    ("15_interpreter", "Interpreter", "解释器"),
    ("16_iterator", "Iterator", "迭代器"),
    ("17_mediator", "Mediator", "中介者"),
    ("18_memento", "Memento", "备忘录"),
    ("19_observer", "Observer", "观察者"),
    ("20_state", "State", "状态"),
    ("21_strategy", "Strategy", "策略"),
    ("22_template_method", "Template Method", "模板方法"),
    ("23_visitor", "Visitor", "访问者"),
]


def _configure_stdio() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")


def _print_menu() -> None:
    print("\n" + "=" * 50)
    print("  23 种设计模式 — 交互学习 (learn.py)")
    print("=" * 50)
    for i, (mod, en, zh) in enumerate(PATTERN_META, start=1):
        print(f"  {i:2}. {mod:32} {zh} ({en})")
    print("   0. 退出")
    print("  all. 运行全部 demo()")
    print("=" * 50)


def _run_module(name: str, mode: str) -> None:
    module = importlib.import_module(name)
    if mode == "basic" and hasattr(module, "demo_basic"):
        module.demo_basic()
    elif mode == "advanced" and hasattr(module, "demo_advanced"):
        module.demo_advanced()
    else:
        module.demo()


def _pick_mode(name: str) -> str:
    module = importlib.import_module(name)
    has_basic = hasattr(module, "demo_basic")
    has_advanced = hasattr(module, "demo_advanced")
    if not (has_basic or has_advanced):
        return "demo"
    print("  运行模式: [1] demo  [2] demo_basic  [3] demo_advanced")
    choice = input("  选择 (默认 1): ").strip() or "1"
    return {"1": "demo", "2": "basic", "3": "advanced"}.get(choice, "demo")


def main() -> int:
    _configure_stdio()
    if len(PATTERN_META) != len(PATTERNS):
        print("[learn] 警告: PATTERN_META 与 PATTERNS 数量不一致", file=sys.stderr)

    while True:
        _print_menu()
        raw = input("请输入编号 (1-23) / all / 0: ").strip().lower()
        if raw in ("0", "q", "quit", "exit"):
            print("再见。")
            return 0
        if raw == "all":
            import run_all

            return run_all.main()
        try:
            idx = int(raw)
            if idx < 1 or idx > len(PATTERN_META):
                print("无效编号，请重试。")
                continue
        except ValueError:
            print("无效输入，请重试。")
            continue

        mod, en, zh = PATTERN_META[idx - 1]
        print(f"\n>>> {mod} — {zh} ({en})\n")
        mode = _pick_mode(mod)
        try:
            _run_module(mod, mode)
        except Exception as exc:
            print(f"[learn] 运行失败: {exc}", file=sys.stderr)
            return 1
        input("\n按 Enter 返回菜单...")


if __name__ == "__main__":
    raise SystemExit(main())
