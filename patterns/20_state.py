"""状态模式 (State)

意图：允许对象在内部状态改变时改变其行为，对象看起来好像修改了类。
适用：订单状态机、工作流、TCP 连接状态。

误用：
- 状态少、转移简单时用大量状态类，样板过多（可用表驱动或 enum）。
- 与策略模式混淆：状态通常在内部自动切换；策略常由客户端选择。
- 非法转移未统一处理，散落在各状态类 if 分支。

类图 (Mermaid):
    classDiagram
        class OrderState { <<abstract>> +pay() +ship() }
        class PendingState
        class PaidState
        class ShippedState
        class Order {
            +state
            +pay()
            +ship()
        }
        OrderState <|-- PendingState
        OrderState <|-- PaidState
        OrderState <|-- ShippedState
        Order o--> OrderState"""

from abc import ABC, abstractmethod


class OrderState(ABC):
    @abstractmethod
    def pay(self, order: "Order") -> str:
        pass

    @abstractmethod
    def ship(self, order: "Order") -> str:
        pass


class PendingState(OrderState):
    def pay(self, order: "Order") -> str:
        order.state = PaidState()
        return "支付成功，订单已付款"

    def ship(self, order: "Order") -> str:
        return "未付款，无法发货"


class PaidState(OrderState):
    def pay(self, order: "Order") -> str:
        return "已付款，请勿重复支付"

    def ship(self, order: "Order") -> str:
        order.state = ShippedState()
        return "已发货"


class ShippedState(OrderState):
    def pay(self, order: "Order") -> str:
        return "订单已发货，无法支付"

    def ship(self, order: "Order") -> str:
        return "已发货，请勿重复操作"


class Order:
    def __init__(self) -> None:
        self.state: OrderState = PendingState()

    def pay(self) -> str:
        return self.state.pay(self)

    def ship(self) -> str:
        return self.state.ship(self)


def demo() -> None:
    order = Order()
    print(f"[State] {order.pay()}")
    print(f"[State] {order.ship()}")
    print(f"[State] {order.pay()}")


if __name__ == "__main__":
    demo()
