"""Anti-pattern: Singleton used as a god object for unrelated global state."""

from __future__ import annotations


class AppSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.db_url = ""
        self.ui_theme = ""
        self.cache: dict[str, str] = {}
        self.debug_flags: dict[str, bool] = {}


def demo() -> None:
    app = AppSingleton()
    app.db_url = "postgres://..."
    app.ui_theme = "dark"
    app.cache["session"] = "xyz"
    app.debug_flags["verbose"] = True

    other = AppSingleton()
    print("[AntiPattern:Singleton] 任意模块都能读写同一全局桶:")
    print(f"  other is app: {other is app}")
    print(f"  other.db_url = {other.db_url}")
    print("  更好做法: 按职责拆分配置对象或依赖注入，见 patterns/01_singleton.py")


if __name__ == "__main__":
    demo()
