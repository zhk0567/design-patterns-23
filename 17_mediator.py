"""中介者模式 (Mediator)

意图：用一个中介对象封装一系列对象交互，使对象之间不必显式相互引用。
适用：聊天室、航空管制、表单联动。
"""


class ChatRoom:
    def __init__(self) -> None:
        self._users: dict[str, "User"] = {}

    def register(self, user: "User") -> None:
        self._users[user.name] = user
        user.room = self

    def send(self, sender: str, message: str) -> None:
        for name, user in self._users.items():
            if name != sender:
                user.receive(sender, message)


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.room: ChatRoom | None = None

    def send(self, message: str) -> None:
        if self.room:
            print(f"[Mediator] {self.name} 发送: {message}")
            self.room.send(self.name, message)

    def receive(self, sender: str, message: str) -> None:
        print(f"[Mediator] {self.name} 收到来自 {sender}: {message}")


def demo() -> None:
    room = ChatRoom()
    alice = User("Alice")
    bob = User("Bob")
    room.register(alice)
    room.register(bob)
    alice.send("大家好！")

if __name__ == '__main__':
    demo()
