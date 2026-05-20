"""迭代器模式 (Iterator)

意图：提供一种方法顺序访问聚合对象中的各个元素，而不暴露其内部表示。
适用：自定义集合遍历、分页、树形遍历。

误用：
- 迭代过程中修改底层集合未做防护（应抛异常或快照）。
- 对外暴露内部列表引用，破坏封装。
- 已有 `__iter__` 可简洁实现时仍手写冗长 Iterator 类（本示例为教学目的）。

类图 (Mermaid):
    classDiagram
        class BookShelf {
            -_books
            +add()
            +__iter__()
        }
        class BookIterator {
            -_books
            -_index
            +__next__()
        }
        BookShelf ..> BookIterator : creates"""

from typing import Iterator


class BookShelf:
    def __init__(self) -> None:
        self._books: list[str] = []

    def add(self, title: str) -> None:
        self._books.append(title)

    def __iter__(self) -> Iterator[str]:
        return BookIterator(self._books)


class BookIterator:
    def __init__(self, books: list[str]) -> None:
        self._books = books
        self._index = 0

    def __iter__(self) -> "BookIterator":
        return self

    def __next__(self) -> str:
        if self._index >= len(self._books):
            raise StopIteration
        book = self._books[self._index]
        self._index += 1
        return book


def demo() -> None:
    shelf = BookShelf()
    for title in ["设计模式", "重构", "代码整洁之道"]:
        shelf.add(title)
    print("[Iterator] 遍历书架:")
    for book in shelf:
        print(f"  - {book}")

if __name__ == '__main__':
    demo()
