"""解释器模式 (Interpreter)

意图：给定一种语言，定义其文法表示，并定义解释器来解释语言中的句子。
适用：简单 DSL、规则引擎、表达式求值。
"""

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


def demo() -> None:
    # 表达式: x + 10，其中 x = 5
    expr = Add(Variable("x"), Number(10))
    result = expr.interpret({"x": 5})
    print(f"[Interpreter] x + 10 = {result} (x=5)")

if __name__ == '__main__':
    demo()
