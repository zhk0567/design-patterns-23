"""享元模式 (Flyweight)

意图：运用共享技术有效地支持大量细粒度对象，减少内存占用。
适用：文本编辑器字符、地图瓦片、图标缓存。

误用：
- 把会变化的外在状态（位置、选中态）放进享元内部，导致错误共享。
- 享元池无上限且不淘汰，内存泄漏式膨胀。
- 对象数量不多、创建成本极低时引入享元得不偿失。

English (Flyweight):
- Intent: Share intrinsic state to support many fine-grained objects.
- Use when: Text glyphs, map tiles.
- Pitfalls: Extrinsic state inside flyweight; unbounded pool.
类图 (Mermaid):
    classDiagram
        class GlyphStyle {
            +font
            +size
            +color
        }
        class CharacterFlyweight {
            -_pool$
            +char
            +style
            +get()
            +render()
        }
        CharacterFlyweight --> GlyphStyle"""

from dataclasses import dataclass


@dataclass(frozen=True)
class GlyphStyle:
    font: str
    size: int
    color: str


class CharacterFlyweight:
    _pool: dict[tuple, "CharacterFlyweight"] = {}

    def __init__(self, char: str, style: GlyphStyle) -> None:
        self.char = char
        self.style = style

    @classmethod
    def get(cls, char: str, style: GlyphStyle) -> "CharacterFlyweight":
        key = (char, style.font, style.size, style.color)
        if key not in cls._pool:
            cls._pool[key] = cls(char, style)
        return cls._pool[key]

    def render(self, position: int) -> str:
        return f"'{self.char}'@{position} [{self.style.font}/{self.style.size}]"


def demo() -> None:
    style = GlyphStyle("SimSun", 12, "black")
    text = "hello"
    glyphs = [CharacterFlyweight.get(c, style) for c in text]
    for i, g in enumerate(glyphs):
        print(f"[Flyweight] {g.render(i)}")
    print(f"[Flyweight] 池大小: {len(CharacterFlyweight._pool)} (5 个字符复用 4 个享元，'l' 重复)")


if __name__ == "__main__":
    demo()
