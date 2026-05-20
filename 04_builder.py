"""建造者模式 (Builder)

意图：将复杂对象的构建与表示分离，使同样的构建过程可以创建不同的表示。
适用：HTTP 请求、SQL、配置对象等分步组装。
"""

from dataclasses import dataclass, field


@dataclass
class HttpRequest:
    method: str = "GET"
    url: str = ""
    headers: dict[str, str] = field(default_factory=dict)
    body: str = ""

    def describe(self) -> str:
        header_str = ", ".join(f"{k}={v}" for k, v in self.headers.items())
        return f"{self.method} {self.url} | headers: {{{header_str}}} | body: {self.body!r}"


class HttpRequestBuilder:
    def __init__(self) -> None:
        self._request = HttpRequest()

    def method(self, method: str) -> "HttpRequestBuilder":
        self._request.method = method
        return self

    def url(self, url: str) -> "HttpRequestBuilder":
        self._request.url = url
        return self

    def header(self, key: str, value: str) -> "HttpRequestBuilder":
        self._request.headers[key] = value
        return self

    def body(self, body: str) -> "HttpRequestBuilder":
        self._request.body = body
        return self

    def build(self) -> HttpRequest:
        return self._request


def demo() -> None:
    req = (
        HttpRequestBuilder()
        .method("POST")
        .url("/api/orders")
        .header("Content-Type", "application/json")
        .body('{"sku": "A001", "qty": 2}')
        .build()
    )
    print(f"[Builder] {req.describe()}")

if __name__ == '__main__':
    demo()
