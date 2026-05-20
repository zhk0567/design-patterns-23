"""访问者模式 (Visitor)

意图：表示一个作用于某对象结构中的各元素的操作，可在不改变元素类的前提下定义新操作。
适用：编译器 AST 遍历、文件系统统计、报表生成。

误用：
- 元素类型经常新增却不愿改所有访问者（违反开闭原则的一侧）。
- 访问者方法过多，每增加一种操作就要改访问者接口。
- 元素层次未稳定就引入访问者，双分派复杂度得不偿失。

类图 (Mermaid):
    classDiagram
        class FileNode {
            +name
            +size
        }
        class FolderNode {
            +name
            +children
        }
        class Visitor { <<abstract>> +visit_file() +visit_folder() }
        class SizeVisitor
        class PrintVisitor
        Visitor <|-- SizeVisitor
        Visitor <|-- PrintVisitor
        Visitor ..> FileNode
        Visitor ..> FolderNode
        FolderNode o--> FileNode"""

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


class PrintVisitor(Visitor):
    def __init__(self, indent: int = 0) -> None:
        self._indent = indent

    def visit_file(self, node: FileNode) -> None:
        prefix = "  " * self._indent
        print(f"{prefix}[Visitor] FILE {node.name} ({node.size}B)")

    def visit_folder(self, node: FolderNode) -> None:
        prefix = "  " * self._indent
        print(f"{prefix}[Visitor] DIR  {node.name}/")
        child_visitor = PrintVisitor(self._indent + 1)
        for child in node.children:
            accept(child, child_visitor)


def accept(node: FileNode | FolderNode, visitor: Visitor) -> None:
    if isinstance(node, FileNode):
        visitor.visit_file(node)
    else:
        visitor.visit_folder(node)


def build_sample_tree() -> FolderNode:
    return FolderNode(
        "root",
        [
            FileNode("a.txt", 100),
            FolderNode("docs", [FileNode("b.txt", 250)]),
        ],
    )


def demo_basic() -> None:
    tree = build_sample_tree()
    visitor = SizeVisitor()
    accept(tree, visitor)
    print(f"[Visitor] basic: total size = {visitor.total_size} bytes")


def demo_advanced() -> None:
    tree = build_sample_tree()
    print("[Visitor] advanced: tree structure:")
    accept(tree, PrintVisitor())


def demo() -> None:
    demo_basic()
    demo_advanced()


if __name__ == "__main__":
    demo()
