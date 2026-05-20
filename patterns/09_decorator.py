"""装饰器模式 (Decorator)

意图：动态地给对象添加额外职责，比继承更灵活。
适用：咖啡配料、数据流包装、权限叠加。

误用：
- 与 Python `@decorator` 语法糖混为一谈（后者是函数包装，未必是 GoF 装饰器类结构）。
- 用继承层层子类导致组合爆炸时仍不用装饰器。
- 装饰顺序影响语义时未文档化（如先打折再加料）。

English (Decorator):
- Intent: Attach responsibilities dynamically without subclass explosion.
- Use when: Coffee add-ons, stream wrappers.
- Pitfalls: vs Python @decorator syntax; order of wrappers matters.
类图 (Mermaid):
    classDiagram
        class Coffee { <<abstract>> +cost() +description() }
        class SimpleCoffee
        class CoffeeDecorator { <<abstract>> }
        class Milk
        class Sugar
        Coffee <|-- SimpleCoffee
        Coffee <|-- CoffeeDecorator
        CoffeeDecorator <|-- Milk
        CoffeeDecorator <|-- Sugar
        CoffeeDecorator o--> Coffee : wraps"""

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


if __name__ == "__main__":
    demo()
