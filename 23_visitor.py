"""访问者模式 (Visitor)

意图：表示一个作用于某对象结构中的各元素的操作，可在不改变元素类的前提下定义新操作。
适用：编译器 AST 遍历、文件系统统计、报表生成。
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class FileNode:
    name: str
    size: int


@dataclass
class FolderNode:
    name: str
    children: list["FileNode | FolderNode"]


class Visitor(ABC):
    @abstractmethod
    def visit_file(self, node: FileNode) -> None:
        pass

    @abstractmethod
    def visit_folder(self, node: FolderNode) -> None:
        pass


class SizeVisitor(Visitor):
    def __init__(self) -> None:
        self.total_size = 0

    def visit_file(self, node: FileNode) -> None:
        self.total_size += node.size

    def visit_folder(self, node: FolderNode) -> None:
        for child in node.children:
            accept(child, self)


def accept(node: FileNode | FolderNode, visitor: Visitor) -> None:
    if isinstance(node, FileNode):
        visitor.visit_file(node)
    else:
        visitor.visit_folder(node)


def demo() -> None:
    tree = FolderNode("root", [
        FileNode("a.txt", 100),
        FolderNode("docs", [FileNode("b.txt", 250)]),
    ])
    visitor = SizeVisitor()
    accept(tree, visitor)
    print(f"[Visitor] 文件总大小: {visitor.total_size} bytes")

if __name__ == '__main__':
    demo()
