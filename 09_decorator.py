"""装饰器模式 (Decorator)

意图：动态地给对象添加额外职责，比继承更灵活。
适用：咖啡配料、数据流包装、权限叠加。
"""

from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 10.0

    def description(self) -> str:
        return "美式"


class CoffeeDecorator(Coffee, ABC):
    def __init__(self, coffee: Coffee) -> None:
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost()

    def description(self) -> str:
        return self._coffee.description()


class Milk(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 2.0

    def description(self) -> str:
        return self._coffee.description() + "+牛奶"


class Sugar(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 1.0

    def description(self) -> str:
        return self._coffee.description() + "+糖"


def demo() -> None:
    coffee: Coffee = Sugar(Milk(SimpleCoffee()))
    print(f"[Decorator] {coffee.description()} = {coffee.cost():.1f} 元")

if __name__ == '__main__':
    demo()
