"""观察者模式 (Observer)

意图：定义对象间一对多依赖，当一个对象状态改变时，所有依赖者都会收到通知。
适用：事件总线、股票行情、模型-视图更新。
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, symbol: str, price: float) -> None:
        pass


class StockMarket:
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def set_price(self, symbol: str, price: float) -> None:
        for observer in self._observers:
            observer.update(symbol, price)


class Investor(Observer):
    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, symbol: str, price: float) -> None:
        print(f"[Observer] {self.name} 收到 {symbol} 报价: {price:.2f} 元")


def demo() -> None:
    market = StockMarket()
    market.subscribe(Investor("张三"))
    market.subscribe(Investor("李四"))
    market.set_price("AAPL", 189.5)

if __name__ == '__main__':
    demo()
