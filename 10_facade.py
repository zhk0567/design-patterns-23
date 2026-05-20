"""外观模式 (Facade)

意图：为子系统中的一组接口提供统一的高层接口，降低使用复杂度。
适用：启动流程、下单流程、多媒体播放等跨多个子模块的操作。

误用：
- 门面承担过多业务规则，变成新的上帝类。
- 客户端绕过门面直接调用子系统，破坏封装意图。
- 子系统本可独立演进却被门面绑死无法替换。
"""


class Inventory:
    def reserve(self, sku: str) -> str:
        return f"库存已锁定 {sku}"


class Payment:
    def charge(self, amount: float) -> str:
        return f"已扣款 {amount:.2f} 元"


class Shipping:
    def ship(self, address: str) -> str:
        return f"已发货至 {address}"


class OrderFacade:
    def __init__(self) -> None:
        self._inventory = Inventory()
        self._payment = Payment()
        self._shipping = Shipping()

    def place_order(self, sku: str, amount: float, address: str) -> None:
        steps = [
            self._inventory.reserve(sku),
            self._payment.charge(amount),
            self._shipping.ship(address),
        ]
        for step in steps:
            print(f"[Facade] {step}")


def demo() -> None:
    OrderFacade().place_order("A001", 199.0, "上海市浦东新区")

if __name__ == '__main__':
    demo()
