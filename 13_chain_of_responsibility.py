"""责任链模式 (Chain of Responsibility)

意图：使多个对象都有机会处理请求，从而避免请求发送者与接收者耦合。
适用：审批流、日志过滤链、中间件管道。

误用：
- 链条末端无默认处理，请求静默丢失。
- 处理器过多且每个都访问数据库，性能链过长。
- 动态改链顺序未通知调用方，行为不可预测。
"""

from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self._next: Handler | None = None

    def set_next(self, handler: "Handler") -> "Handler":
        self._next = handler
        return handler

    def handle(self, amount: float) -> str | None:
        result = self._try_handle(amount)
        if result is not None:
            return result
        if self._next:
            return self._next.handle(amount)
        return None

    @abstractmethod
    def _try_handle(self, amount: float) -> str | None:
        pass


class Manager(Handler):
    def _try_handle(self, amount: float) -> str | None:
        if amount <= 1000:
            return f"经理审批通过 {amount} 元"
        return None


class Director(Handler):
    def _try_handle(self, amount: float) -> str | None:
        if amount <= 5000:
            return f"总监审批通过 {amount} 元"
        return None


class CEO(Handler):
    def _try_handle(self, amount: float) -> str | None:
        return f"CEO 特批通过 {amount} 元"


class DynamicApprovalChain:
    """可运行时增删处理器的责任链。"""

    def __init__(self) -> None:
        self._handlers: list[Handler] = []

    def add_handler(self, handler: Handler) -> None:
        self._handlers.append(handler)
        self._relink()

    def remove_handler(self, handler: Handler) -> None:
        self._handlers.remove(handler)
        self._relink()

    def _relink(self) -> None:
        for i, handler in enumerate(self._handlers):
            handler._next = self._handlers[i + 1] if i + 1 < len(self._handlers) else None

    def handle(self, amount: float) -> str:
        if not self._handlers:
            return "无可用处理器"
        result = self._handlers[0].handle(amount)
        return result or "未审批"


def demo_basic() -> None:
    chain = Manager()
    chain.set_next(Director()).set_next(CEO())
    for amount in [500, 3000]:
        print(f"[ChainOfResponsibility] basic {amount} 元 -> {chain.handle(amount)}")


def demo_advanced() -> None:
    dynamic = DynamicApprovalChain()
    manager = Manager()
    director = Director()
    dynamic.add_handler(manager)
    dynamic.add_handler(director)
    print(f"[ChainOfResponsibility] advanced 3000 元 (含总监) -> {dynamic.handle(3000)}")
    dynamic.remove_handler(director)
    print(f"[ChainOfResponsibility] advanced 移除总监后 3000 元 -> {dynamic.handle(3000)}")
    dynamic.add_handler(CEO())
    print(f"[ChainOfResponsibility] advanced 8000 元 (含 CEO) -> {dynamic.handle(8000)}")


def demo() -> None:
    demo_basic()
    demo_advanced()


if __name__ == "__main__":
    demo()
