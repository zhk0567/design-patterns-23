"""E-commerce order flow demo wiring Facade, State, and Observer patterns."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from patterns import load  # noqa: E402


class OrderStatusNotifier:
    """Observer-style listener for order status changes."""

    def __init__(self, name: str) -> None:
        self.name = name

    def on_status(self, order_id: str, status: str) -> None:
        print(f"[Ecommerce][Observer] {self.name}: 订单 {order_id} -> {status}")


class OrderEventBus:
    def __init__(self) -> None:
        self._listeners: list[OrderStatusNotifier] = []

    def subscribe(self, listener: OrderStatusNotifier) -> None:
        self._listeners.append(listener)

    def publish(self, order_id: str, status: str) -> None:
        for listener in self._listeners:
            listener.on_status(order_id, status)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    order_id = "ORD-2026-001"
    sku, amount, address = "A001", 199.0, "上海市浦东新区"

    facade = load("10_facade")
    state = load("20_state")
    bus = OrderEventBus()
    bus.subscribe(OrderStatusNotifier("短信"))
    bus.subscribe(OrderStatusNotifier("App推送"))

    print(f"\n{'=' * 50}\n[Ecommerce] 1. Facade — 下单子系统编排\n{'=' * 50}")
    facade.OrderFacade().place_order(sku, amount, address)
    bus.publish(order_id, "已创建")

    print(f"\n{'=' * 50}\n[Ecommerce] 2. State — 订单状态机\n{'=' * 50}")
    order = state.Order()
    bus.publish(order_id, "待支付")
    print(f"[Ecommerce][State] {order.pay()}")
    bus.publish(order_id, "已付款")
    print(f"[Ecommerce][State] {order.ship()}")
    bus.publish(order_id, "已发货")

    print(f"\n{'=' * 50}\n[Ecommerce] 3. 完成\n{'=' * 50}")
    print("[Ecommerce] 流程结束: 门面编排 + 状态转移 + 观察者通知")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
