"""解释器模式 (Interpreter)

意图：给定一种语言，定义其文法表示，并定义解释器来解释语言中的句子。
适用：简单 DSL、规则引擎、表达式求值。

误用：
- 语法复杂、变更频繁时仍手写解释器（应优先考虑解析器生成器或 AST）。
- 每条规则一个类导致类爆炸，维护困难。
- 解释执行性能差却用于高频热点路径。

English (Interpreter):
- Intent: Define grammar and interpret sentences in the language.
- Use when: Simple DSLs, rule expressions.
- Pitfalls: Complex grammar; poor performance on hot paths.
类图 (Mermaid):
    classDiagram
        class Expression { <<abstract>> +interpret() }
        class Number
        class Variable
        class Add
        class Subtract
        class Multiply
        Expression <|-- Number
        Expression <|-- Variable
        Expression <|-- Add
        Expression <|-- Subtract
        Expression <|-- Multiply
        Add o--> Expression : left/right"""

from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def interpret(self, context: dict[str, int]) -> int:
        pass


class Number(Expression):
    def __init__(self, value: int) -> None:
        self._value = value

    def interpret(self, context: dict[str, int]) -> int:
        return self._value


class Variable(Expression):
    def __init__(self, name: str) -> None:
        self._name = name

    def interpret(self, context: dict[str, int]) -> int:
        return context[self._name]


class Add(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self._left = left
        self._right = right

    def interpret(self, context: dict[str, int]) -> int:
        return self._left.interpret(context) + self._right.interpret(context)


class Subtract(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self._left = left
        self._right = right

    def interpret(self, context: dict[str, int]) -> int:
        return self._left.interpret(context) - self._right.interpret(context)


class Multiply(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self._left = left
        self._right = right

    def interpret(self, context: dict[str, int]) -> int:
        return self._left.interpret(context) * self._right.interpret(context)


def demo_basic() -> None:
    expr = Add(Variable("x"), Number(10))
    result = expr.interpret({"x": 5})
    print(f"[Interpreter] basic: x + 10 = {result} (x=5)")


def demo_advanced() -> None:
    # (x + 10) * 2 - 3, x = 5 -> 27
    expr = Subtract(
        Multiply(Add(Variable("x"), Number(10)), Number(2)),
        Number(3),
    )
    result = expr.interpret({"x": 5})
    print(f"[Interpreter] advanced: (x + 10) * 2 - 3 = {result} (x=5)")


def demo() -> None:
    demo_basic()
    demo_advanced()


if __name__ == "__main__":
    demo()
