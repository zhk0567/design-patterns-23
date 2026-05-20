"""组合模式 (Composite)

意图：将对象组合成树形结构以表示「部分-整体」层次，使客户端对单个对象与组合对象的使用一致。
适用：文件系统、组织架构、菜单树。

误用：
- 叶子节点实现容器才有的 add/remove，违反接口隔离。
- 在组合树上执行仅适用于叶子的操作且未做类型检查。
- 树过深时递归 display/遍历无节制，性能和栈溢出风险。

类图 (Mermaid):
    classDiagram
        class FileSystemNode { <<abstract>> +display() }
        class File
        class Folder {
            +children
            +add()
        }
        FileSystemNode <|-- File
        FileSystemNode <|-- Folder
        Folder o--> FileSystemNode : contains"""

from abc import ABC, abstractmethod


class FileSystemNode(ABC):
    @abstractmethod
    def display(self, indent: int = 0) -> str:
        pass


class File(FileSystemNode):
    def __init__(self, name: str) -> None:
        self.name = name

    def display(self, indent: int = 0) -> str:
        return "  " * indent + f"[FILE] {self.name}"


class Folder(FileSystemNode):
    def __init__(self, name: str) -> None:
        self.name = name
        self.children: list[FileSystemNode] = []

    def add(self, node: FileSystemNode) -> None:
        self.children.append(node)

    def display(self, indent: int = 0) -> str:
        lines = ["  " * indent + f"[DIR] {self.name}"]
        for child in self.children:
            lines.append(child.display(indent + 1))
        return "\n".join(lines)


def demo() -> None:
    root = Folder("project")
    src = Folder("src")
    src.add(File("main.py"))
    src.add(File("utils.py"))
    root.add(src)
    root.add(File("README.md"))
    print(f"[Composite]\n{root.display()}")

if __name__ == '__main__':
    demo()
