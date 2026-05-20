"""命令模式 (Command)

意图：将请求封装为对象，从而支持参数化、队列化、日志与撤销。
适用：撤销/重做、任务队列、宏命令。

误用：
- 命令对象塞满业务逻辑，违背轻量封装请求的初衷。
- 撤销栈无界增长，长时间编辑导致内存占用过高。
- 未保存足够上下文导致 undo 后状态不一致。

English (Command):
- Intent: Encapsulate a request as an object (undo, queue).
- Use when: Undo/redo, job queues.
- Pitfalls: Fat commands; unbounded undo stack.
类图 (Mermaid):
    classDiagram
        class Command { <<abstract>> +execute() +undo() }
        class InsertCommand
        class TextEditor { +content +insert() +delete() }
        class CommandHistory { +run() +undo() }
        Command <|-- InsertCommand
        InsertCommand --> TextEditor
        CommandHistory o--> Command"""

from __future__ import annotations

import asyncio
from abc import ABC, abstractmethod
from collections import deque


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


class AsyncCommandQueue:
    """异步命令队列：顺序执行封装的操作。"""

    def __init__(self) -> None:
        self._queue: deque[Command] = deque()

    def enqueue(self, command: Command) -> None:
        self._queue.append(command)

    async def run_all(self) -> None:
        while self._queue:
            cmd = self._queue.popleft()
            await asyncio.sleep(0)
            cmd.execute()
            print(f"[Command] async executed {cmd.__class__.__name__}")


async def demo_async() -> None:
    editor = TextEditor()
    queue = AsyncCommandQueue()
    queue.enqueue(InsertCommand(editor, "async-"))
    queue.enqueue(InsertCommand(editor, "order"))
    await queue.run_all()
    print(f"[Command] async content: {editor.content!r}")


def demo() -> None:
    editor = TextEditor()
    history = CommandHistory()
    history.run(InsertCommand(editor, "Hello"))
    history.run(InsertCommand(editor, " World"))
    print(f"[Command] 执行后: {editor.content!r}")
    history.undo()
    print(f"[Command] 撤销后: {editor.content!r}")


if __name__ == "__main__":
    demo()
