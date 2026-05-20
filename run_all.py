"""按编号顺序运行全部 23 种设计模式示例。"""

import importlib
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

PATTERNS = [
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


def main() -> int:
    failed = 0
    for name in PATTERNS:
        print(f"\n{'=' * 60}\n>>> {name}\n{'=' * 60}")
        try:
            module = importlib.import_module(name)
            module.demo()
        except Exception as exc:
            failed += 1
            print(f"[ERROR] {name}: {exc}", file=sys.stderr)
    print(f"\n{'=' * 60}")
    if failed:
        print(f"完成：{len(PATTERNS) - failed}/{len(PATTERNS)} 成功，{failed} 个失败")
        return 1
    print(f"完成：全部 {len(PATTERNS)} 个示例运行成功")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
