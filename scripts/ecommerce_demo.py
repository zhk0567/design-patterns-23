"""E-commerce order flow: Facade, Chain, State, Observer, Command."""

from __future__ import annotations

import sys
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from patterns import load  # noqa: E402


class OrderStatusNotifier:
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


class TrackedOrder:
    """Wraps State pattern Order with a cancel flag for Command demo."""

    def __init__(self, state_module: ModuleType) -> None:
        self._inner = state_module.Order()
        self.cancelled = False

    def pay(self) -> str:
        if self.cancelled:
            return "[Ecommerce][State] 订单已取消，无法支付"
        return f"[Ecommerce][State] {self._inner.pay()}"

    def ship(self) -> str:
        if self.cancelled:
            return "[Ecommerce][State] 订单已取消，无法发货"
        return f"[Ecommerce][State] {self._inner.ship()}"


def _run_chain_approval(chain_mod: ModuleType, refund_amount: float) -> None:
    print(f"\n{'=' * 50}\n[Ecommerce] Chain — 退款审批 {refund_amount} 元\n{'=' * 50}")
    dynamic = chain_mod.DynamicApprovalChain()
    dynamic.add_handler(chain_mod.Manager())
    dynamic.add_handler(chain_mod.Director())
    dynamic.add_handler(chain_mod.CEO())
    result = dynamic.handle(refund_amount)
    print(f"[Ecommerce][Chain] 审批结果: {result}")


def _run_command_cancel(
    cmd_mod: ModuleType, order: TrackedOrder, bus: OrderEventBus, order_id: str
) -> None:
    print(f"\n{'=' * 50}\n[Ecommerce] Command — 取消订单（可撤销）\n{'=' * 50}")

    class CancelOrderCommand(cmd_mod.Command):  # type: ignore[name-defined]
        def __init__(self, tracked: TrackedOrder) -> None:
            self._tracked = tracked

        def execute(self) -> None:
            self._tracked.cancelled = True

        def undo(self) -> None:
            self._tracked.cancelled = False

    history = cmd_mod.CommandHistory()
    history.run(CancelOrderCommand(order))
    bus.publish(order_id, "已取消")
    print(order.ship())
    history.undo()
    bus.publish(order_id, "恢复取消前")
    print(order.ship())


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    order_id = "ORD-2026-001"
    sku, amount, address = "A001", 199.0, "上海市浦东新区"

    facade = load("10_facade")
    chain = load("13_chain_of_responsibility")
    state = load("20_state")
    cmd = load("14_command")
    bus = OrderEventBus()
    bus.subscribe(OrderStatusNotifier("短信"))
    bus.subscribe(OrderStatusNotifier("App推送"))

    print(f"\n{'=' * 50}\n[Ecommerce] 1. Facade — 下单\n{'=' * 50}")
    facade.OrderFacade().place_order(sku, amount, address)
    bus.publish(order_id, "已创建")

    _run_chain_approval(chain, 8000.0)

    print(f"\n{'=' * 50}\n[Ecommerce] 2. State — 支付与发货\n{'=' * 50}")
    order = TrackedOrder(state)
    bus.publish(order_id, "待支付")
    print(order.pay())
    bus.publish(order_id, "已付款")

    _run_command_cancel(cmd, order, bus, order_id)

    print(order.ship())
    bus.publish(order_id, "已发货")

    print(f"\n{'=' * 50}\n[Ecommerce] 完成\n{'=' * 50}")
    print("[Ecommerce] Facade + Chain + State + Observer + Command")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
