"""代理模式 (Proxy)

意图：为其他对象提供一种代理以控制对这个对象的访问。
适用：懒加载、访问控制、远程代理、缓存代理。

误用：
- 与装饰器职责重叠：代理侧重控制访问；装饰侧重增强功能（实际常需按意图区分）。
- 虚拟代理未处理并发下重复创建真实对象。
- 远程代理忽略超时、重试与序列化版本兼容。

类图 (Mermaid):
    classDiagram
        class RealImage {
            +filename
            +display()
        }
        class ImageProxy {
            -_filename
            -_real
            +display()
        }
        ImageProxy ..> RealImage : lazy create"""


class RealImage:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self._loaded = False

    def _load(self) -> None:
        if not self._loaded:
            print(f"[Proxy] 从磁盘加载 {self.filename}")
            self._loaded = True

    def display(self) -> str:
        self._load()
        return f"显示图片: {self.filename}"


class ImageProxy:
    def __init__(self, filename: str) -> None:
        self._filename = filename
        self._real: RealImage | None = None

    def display(self) -> str:
        if self._real is None:
            print(f"[Proxy] 首次访问，创建 RealImage('{self._filename}')")
            self._real = RealImage(self._filename)
        return self._real.display()


def demo() -> None:
    proxy = ImageProxy("photo.png")
    print(proxy.display())
    print(proxy.display())

if __name__ == '__main__':
    demo()
