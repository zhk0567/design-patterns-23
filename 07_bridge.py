"""桥接模式 (Bridge)

意图：将抽象与实现分离，使它们可以独立变化。
适用：形状×渲染器、消息×发送渠道等多维度扩展。
"""

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

if __name__ == '__main__':
    demo()
