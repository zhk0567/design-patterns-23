"""观察者模式 (Observer)

意图：定义对象间一对多依赖，当一个对象状态改变时，所有依赖者都会收到通知。
适用：事件总线、股票行情、模型-视图更新。

误用：
- 观察者更新主题时又修改主题，导致循环通知。
- 订阅后从不取消，造成内存泄漏（demo_advanced 演示 weakref 清理）。
- 通知顺序依赖隐式假设，多个观察者相互影响。
"""

import weakref
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, symbol: str, price: float) -> None:
        pass


class StockMarket:
    """强引用观察者列表。"""

    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def set_price(self, symbol: str, price: float) -> None:
        for observer in self._observers:
            observer.update(symbol, price)


class WeakStockMarket:
    """弱引用观察者，观察者被 GC 后自动从列表移除。"""

    def __init__(self) -> None:
        self._observers: list[weakref.ReferenceType[Observer]] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(weakref.ref(observer))

    def set_price(self, symbol: str, price: float) -> None:
        alive: list[weakref.ReferenceType[Observer]] = []
        for ref in self._observers:
            observer = ref()
            if observer is not None:
                observer.update(symbol, price)
                alive.append(ref)
        self._observers = alive

    @property
    def observer_count(self) -> int:
        return len(self._observers)


class Investor(Observer):
    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, symbol: str, price: float) -> None:
        print(f"[Observer] {self.name} 收到 {symbol} 报价: {price:.2f} 元")


def demo_basic() -> None:
    market = StockMarket()
    market.subscribe(Investor("张三"))
    market.subscribe(Investor("李四"))
    market.set_price("AAPL", 189.5)


def demo_advanced() -> None:
    market = WeakStockMarket()
    temp = Investor("临时投资者")
    market.subscribe(temp)
    market.subscribe(Investor("长期投资者"))
    print(f"[Observer] advanced: 订阅后 observer_count = {market.observer_count}")
    del temp
    market.set_price("AAPL", 200.0)
    print(f"[Observer] advanced: GC 临时观察者后 observer_count = {market.observer_count}")


def demo() -> None:
    demo_basic()
    demo_advanced()


if __name__ == "__main__":
    demo()
