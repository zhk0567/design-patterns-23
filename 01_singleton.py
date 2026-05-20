"""单例模式 (Singleton)

意图：确保一个类只有一个实例，并提供全局访问点。
适用：配置中心、日志器、连接池等。

误用：
- 多线程下未加锁可能创建多个实例（本示例未做线程安全）。
- 把单例当作全局变量垃圾桶，导致隐式耦合与难以测试。
- 在不需要唯一实例时强行使用，增加复杂度。
"""


class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.theme = "light"
        self._initialized = True


def demo() -> None:
    a = AppConfig()
    b = AppConfig()
    b.theme = "dark"
    print(f"[Singleton] a is b: {a is b}")
    print(f"[Singleton] a.theme: {a.theme}")
    print(f"[Singleton] instance id: {id(a)}")

if __name__ == '__main__':
    demo()
