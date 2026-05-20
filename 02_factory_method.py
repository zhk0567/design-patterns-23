"""工厂方法模式 (Factory Method)

意图：定义创建对象的接口，由子类决定实例化哪一个类。
适用：日志、文档导出等需要按类型创建产品的场景。

误用：
- 与简单工厂混为一谈：简单工厂通常是一个函数 if/else 选类型，工厂方法强调子类化创建。
- 产品类型很少却引入大量工厂子类，过度设计。
- 客户端仍依赖具体工厂类而非抽象工厂接口。
"""

from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> str:
        pass


class ConsoleLogger(Logger):
    def log(self, message: str) -> str:
        return f"[Console] {message}"


class FileLogger(Logger):
    def log(self, message: str) -> str:
        return f"[File] {message}"


class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass

    def write(self, message: str) -> str:
        return self.create_logger().log(message)


class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()


class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()


def demo() -> None:
    factories = [ConsoleLoggerFactory(), FileLoggerFactory()]
    for factory in factories:
        print(factory.write("用户登录成功"))

if __name__ == '__main__':
    demo()
