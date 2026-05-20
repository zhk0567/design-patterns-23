"""备忘录模式 (Memento)

意图：在不破坏封装的前提下，捕获对象的内部状态并在之后恢复。
适用：编辑器撤销、游戏存档、配置快照。

误用：
- 备忘录保存整个大文档历史，内存暴涨。
- 原发器对外暴露过多内部字段，破坏封装。
- 持久化备忘录未考虑版本迁移与安全（勿 pickle 不可信数据）。

类图 (Mermaid):
    classDiagram
        class EditorMemento {
            +content
        }
        class Editor {
            +content
            +type()
            +save()
            +restore()
        }
        class History {
            -_snapshots
            +push()
            +pop()
        }
        Editor ..> EditorMemento : save/restore
        History o--> EditorMemento"""

from dataclasses import dataclass


@dataclass
class EditorMemento:
    content: str


class Editor:
    def __init__(self) -> None:
        self.content = ""

    def type(self, text: str) -> None:
        self.content += text

    def save(self) -> EditorMemento:
        return EditorMemento(self.content)

    def restore(self, memento: EditorMemento) -> None:
        self.content = memento.content


class History:
    def __init__(self) -> None:
        self._snapshots: list[EditorMemento] = []

    def push(self, memento: EditorMemento) -> None:
        self._snapshots.append(memento)

    def pop(self) -> EditorMemento | None:
        return self._snapshots.pop() if self._snapshots else None


def demo() -> None:
    editor = Editor()
    history = History()
    editor.type("第一行")
    history.push(editor.save())
    editor.type("\n第二行")
    print(f"[Memento] 编辑后:\n{editor.content}")
    memento = history.pop()
    if memento:
        editor.restore(memento)
    print(f"[Memento] 恢复后:\n{editor.content}")

if __name__ == '__main__':
    demo()
