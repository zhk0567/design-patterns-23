"""Anti-pattern: inheritance explosion for every coffee variant."""

from __future__ import annotations


class Coffee:
    def cost(self) -> float:
        return 10.0


class CoffeeWithMilk(Coffee):
    def cost(self) -> float:
        return super().cost() + 2.0


class CoffeeWithSugar(Coffee):
    def cost(self) -> float:
        return super().cost() + 1.0


class CoffeeWithMilkAndSugar(CoffeeWithMilk):
    def cost(self) -> float:
        return super().cost() + 1.0


def demo() -> None:
    print("[AntiPattern:Inheritance] 每种配料组合都要一个新子类:")
    print(f"  美式+牛奶+糖 = {CoffeeWithMilkAndSugar().cost():.1f} 元")
    print("  更好做法: 见 patterns/09_decorator.py 装饰器组合")


if __name__ == "__main__":
    demo()
