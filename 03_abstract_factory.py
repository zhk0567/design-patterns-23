"""抽象工厂模式 (Abstract Factory)

意图：提供创建一系列相关或相互依赖对象的接口，而无需指定具体类。
适用：跨平台 UI、主题套件（按钮+输入框成组切换）。

误用：
- 只需创建单一产品时误用（应优先考虑工厂方法）。
- 产品族频繁增减导致抽象工厂接口臃肿。
- 与工厂方法边界不清：抽象工厂管「一族」，工厂方法管「一种」。
"""

from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class TextBox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class DarkButton(Button):
    def render(self) -> str:
        return "DarkButton"


class DarkTextBox(TextBox):
    def render(self) -> str:
        return "DarkTextBox"


class LightButton(Button):
    def render(self) -> str:
        return "LightButton"


class LightTextBox(TextBox):
    def render(self) -> str:
        return "LightTextBox"


class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_textbox(self) -> TextBox:
        pass


class DarkThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_textbox(self) -> TextBox:
        return DarkTextBox()


class LightThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_textbox(self) -> TextBox:
        return LightTextBox()


def paint_screen(factory: UIFactory) -> None:
    print(f"[AbstractFactory] {factory.create_button().render()}, "
          f"{factory.create_textbox().render()}")


def demo() -> None:
    paint_screen(DarkThemeFactory())
    paint_screen(LightThemeFactory())

if __name__ == '__main__':
    demo()
