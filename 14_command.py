"""命令模式 (Command)

意图：将请求封装为对象，从而支持参数化、队列化、日志与撤销。
适用：撤销/重做、任务队列、宏命令。
"""

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class TextEditor:
    def __init__(self) -> None:
        self.content = ""

    def insert(self, text: str) -> None:
        self.content += text

    def delete(self, length: int) -> None:
        self.content = self.content[:-length]


class InsertCommand(Command):
    def __init__(self, editor: TextEditor, text: str) -> None:
        self._editor = editor
        self._text = text

    def execute(self) -> None:
        self._editor.insert(self._text)

    def undo(self) -> None:
        self._editor.delete(len(self._text))


class CommandHistory:
    def __init__(self) -> None:
        self._commands: list[Command] = []

    def run(self, command: Command) -> None:
        command.execute()
        self._commands.append(command)

    def undo(self) -> None:
        if self._commands:
            self._commands.pop().undo()


def demo() -> None:
    editor = TextEditor()
    history = CommandHistory()
    history.run(InsertCommand(editor, "Hello"))
    history.run(InsertCommand(editor, " World"))
    print(f"[Command] 执行后: {editor.content!r}")
    history.undo()
    print(f"[Command] 撤销后: {editor.content!r}")

if __name__ == '__main__':
    demo()
