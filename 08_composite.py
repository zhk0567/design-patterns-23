"""组合模式 (Composite)

意图：将对象组合成树形结构以表示「部分-整体」层次，使客户端对单个对象与组合对象的使用一致。
适用：文件系统、组织架构、菜单树。
"""

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
