"""原型模式 (Prototype)

意图：通过复制现有实例来创建新对象，而不是通过 new/构造器。
适用：克隆成本高或配置复杂的对象（文档、游戏实体等）。
"""

import copy
from dataclasses import dataclass, field


@dataclass
class Document:
    title: str
    content: str
    tags: list[str] = field(default_factory=list)

    def clone(self) -> "Document":
        return copy.deepcopy(self)


def demo() -> None:
    original = Document("方案", "第一版内容", tags=["draft"])
    draft = original.clone()
    draft.title = "方案-副本"
    draft.tags.append("review")

    print(f"[Prototype] original.title: {original.title}, tags: {original.tags}")
    print(f"[Prototype] draft.title: {draft.title}, tags: {draft.tags}")
    print(f"[Prototype] 深拷贝独立: {original.tags is not draft.tags}")

if __name__ == '__main__':
    demo()
