"""工厂方法模式 (Factory Method)

意图：定义创建对象的接口，由子类决定实例化哪一个类。
适用：日志、文档导出等需要按类型创建产品的场景。
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
