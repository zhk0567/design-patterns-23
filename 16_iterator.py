"""迭代器模式 (Iterator)

意图：提供一种方法顺序访问聚合对象中的各个元素，而不暴露其内部表示。
适用：自定义集合遍历、分页、树形遍历。
"""

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
