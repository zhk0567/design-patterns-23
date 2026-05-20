"""策略模式 (Strategy)

意图：定义一系列算法，把它们封装起来，并使它们可以互相替换。
适用：排序方式、折扣计算、路径规划、压缩算法。

误用：
- 仅有一种算法却抽象策略接口，无扩展收益。
- 客户端必须知晓所有策略类名，违背开闭原则收益减半。
- 与状态模式混用：若行为由内部状态驱动，优先考虑状态模式。

类图 (Mermaid):
    classDiagram
        class SortStrategy { <<abstract>> +sort() }
        class BubbleSort
        class QuickSort
        class Sorter {
            -_strategy
            +sort()
        }
        SortStrategy <|-- BubbleSort
        SortStrategy <|-- QuickSort
        Sorter o--> SortStrategy"""

from abc import ABC, abstractmethod


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list[int]) -> list[int]:
        pass


class BubbleSort(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class QuickSort(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        mid = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + mid + self.sort(right)


class Sorter:
    def __init__(self, strategy: SortStrategy) -> None:
        self._strategy = strategy

    def sort(self, data: list[int]) -> list[int]:
        return self._strategy.sort(data)


def demo() -> None:
    data = [5, 2, 8, 1, 9]
    for name, strategy in [("Bubble", BubbleSort()), ("Quick", QuickSort())]:
        result = Sorter(strategy).sort(data)
        print(f"[Strategy] {name}: {result}")

if __name__ == '__main__':
    demo()
