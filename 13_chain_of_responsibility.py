"""责任链模式 (Chain of Responsibility)

意图：使多个对象都有机会处理请求，从而避免请求发送者与接收者耦合。
适用：审批流、日志过滤链、中间件管道。
"""

from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self._next: Handler | None = None

    def set_next(self, handler: "Handler") -> "Handler":
        self._next = handler
        return handler

    def handle(self, amount: float) -> str | None:
        if self._next:
            return self._next.handle(amount)
        return None


class Manager(Handler):
    def handle(self, amount: float) -> str | None:
        if amount <= 1000:
            return f"经理审批通过 {amount} 元"
        return super().handle(amount)


class Director(Handler):
    def handle(self, amount: float) -> str | None:
        if amount <= 5000:
            return f"总监审批通过 {amount} 元"
        return super().handle(amount)


class CEO(Handler):
    def handle(self, amount: float) -> str | None:
        return f"CEO 特批通过 {amount} 元"


def demo() -> None:
    chain = Manager()
    chain.set_next(Director()).set_next(CEO())
    for amount in [500, 3000, 8000]:
        result = chain.handle(amount)
        print(f"[ChainOfResponsibility] {amount} 元 -> {result}")

if __name__ == '__main__':
    demo()
