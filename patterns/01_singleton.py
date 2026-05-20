"""单例模式 (Singleton)

意图：确保一个类只有一个实例，并提供全局访问点。
适用：配置中心、日志器、连接池等。

误用：
- 多线程下未加锁可能创建多个实例（见 demo_basic 与非线程安全版对比）。
- 把单例当作全局变量垃圾桶，导致隐式耦合与难以测试。
- 在不需要唯一实例时强行使用，增加复杂度。

类图 (Mermaid):
    classDiagram
        class AppConfig {
            -_instance$
            -_initialized
            +theme
        }
        class ThreadSafeAppConfig {
            -_instance$
            -_lock$
            +theme
        }"""

from __future__ import annotations

import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import ClassVar


class AppConfig:
    """非线程安全单例（教学对比用）。"""

    _instance: ClassVar[AppConfig | None] = None
    _initialized: bool

    def __new__(cls) -> AppConfig:
        if cls._instance is None:
            obj = super().__new__(cls)
            obj._initialized = False
            cls._instance = obj
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return
        self.theme = "light"
        self._initialized = True


class ThreadSafeAppConfig:
    """双重检查锁定（DCL）线程安全单例。"""

    _instance: ClassVar[ThreadSafeAppConfig | None] = None
    _lock: ClassVar[threading.Lock] = threading.Lock()
    _initialized: bool

    def __new__(cls) -> ThreadSafeAppConfig:
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    inst = super().__new__(cls)
                    inst._initialized = False
                    cls._instance = inst
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return
        self.theme = "light"
        self._initialized = True


def demo_basic() -> None:
    a = AppConfig()
    b = AppConfig()
    b.theme = "dark"
    print(f"[Singleton] basic: a is b = {a is b}, theme = {a.theme}")


def demo_advanced() -> None:
    ids: list[int] = []

    def create_instance() -> int:
        return id(ThreadSafeAppConfig())

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(create_instance) for _ in range(32)]
        ids = [f.result() for f in as_completed(futures)]

    unique = len(set(ids))
    print(f"[Singleton] advanced: 32 threads -> {unique} unique instance(s)")
    print(f"[Singleton] advanced: thread-safe OK = {unique == 1}")


def demo() -> None:
    demo_basic()
    demo_advanced()


if __name__ == "__main__":
    demo()
