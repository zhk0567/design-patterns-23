"""单例模式 (Singleton)

意图：确保一个类只有一个实例，并提供全局访问点。
适用：配置中心、日志器、连接池等。
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
