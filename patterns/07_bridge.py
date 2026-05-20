"""桥接模式 (Bridge)

意图：将抽象与实现分离，使它们可以独立变化。
适用：形状×渲染器、消息×发送渠道等多维度扩展。

误用：
- 仅有一个实现类时仍拆桥接，抽象与实现分离收益不足。
- 与策略模式混淆：桥接强调抽象维度稳定、实现可替换；策略强调算法互换。
- 过度拆分导致跳转层次过多，阅读成本高。

English (Bridge):
- Intent: Split abstraction and implementation so both vary independently.
- Use when: Shape x renderer, message x channel.
- Pitfalls: Confused with Strategy; too many layers.
类图 (Mermaid):
    classDiagram
        class Renderer { <<abstract>> +render_circle() }
        class VectorRenderer
        class RasterRenderer
        class Shape { <<abstract>> +draw() }
        class Circle
        Renderer <|-- VectorRenderer
        Renderer <|-- RasterRenderer
        Shape <|-- Circle
        Shape o--> Renderer : bridge"""

from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius: float) -> str:
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius: float) -> str:
        return f"VectorCircle(r={radius})"


class RasterRenderer(Renderer):
    def render_circle(self, radius: float) -> str:
        return f"RasterCircle(r={radius})"


class Shape(ABC):
    def __init__(self, renderer: Renderer) -> None:
        self._renderer = renderer

    @abstractmethod
    def draw(self) -> str:
        pass


class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: float) -> None:
        super().__init__(renderer)
        self.radius = radius

    def draw(self) -> str:
        return self._renderer.render_circle(self.radius)


def demo() -> None:
    for renderer in [VectorRenderer(), RasterRenderer()]:
        circle = Circle(renderer, 5)
        print(f"[Bridge] {circle.draw()}")


if __name__ == "__main__":
    demo()
