"""适配器模式 (Adapter)

意图：将一个类的接口转换成客户希望的另一个接口，使原本不兼容的类可以合作。
适用：对接第三方支付、遗留 API、第三方 SDK。

误用：
- 与装饰器混淆：适配器改变接口以兼容；装饰器保持接口并增强行为。
- 适配层堆积过多业务逻辑，变成「上帝适配器」。
- 双向适配未理清调用方向，维护困难。

English (Adapter):
- Intent: Convert one interface into another clients expect.
- Use when: Legacy SDKs, third-party APIs.
- Pitfalls: Confused with Decorator; god adapter.
类图 (Mermaid):
    classDiagram
        class PaymentGateway { <<abstract>> +pay() }
        class LegacyPaySDK { +send_money() }
        class LegacyPayAdapter
        PaymentGateway <|-- LegacyPayAdapter
        LegacyPayAdapter --> LegacyPaySDK : adapts"""

from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


class LegacyPaySDK:
    """第三方旧接口：方法名与参数格式不同。"""

    def send_money(self, cents: int) -> bool:
        return cents > 0


class LegacyPayAdapter(PaymentGateway):
    def __init__(self, sdk: LegacyPaySDK) -> None:
        self._sdk = sdk

    def pay(self, amount: float) -> str:
        ok = self._sdk.send_money(int(amount * 100))
        return f"支付{'成功' if ok else '失败'}: {amount:.2f} 元"


def demo() -> None:
    gateway: PaymentGateway = LegacyPayAdapter(LegacyPaySDK())
    print(f"[Adapter] {gateway.pay(128.5)}")


if __name__ == "__main__":
    demo()
