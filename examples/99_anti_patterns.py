"""设计模式相关反模式演示（非 GoF 正例）。

对照 docs/GUIDE.md#反模式，展示常见误用及后果。
"""

from __future__ import annotations

# --- 反模式 1: 伪单例 + 全局可变状态 ---

_CONFIG: dict[str, str] = {}


def get_config() -> dict[str, str]:
    """看似单例，实为模块级全局字典，任何调用方可随意改键值。"""
    return _CONFIG


# --- 反模式 2: 上帝函数门面 ---


def god_place_order(sku: str, amount: float, user_id: str, coupon: str) -> str:
    """一个函数完成校验、库存、支付、积分、短信——难以测试与扩展。"""
    if amount < 0:
        return "金额非法"
    if not sku:
        return "SKU 为空"
    if coupon == "INVALID":
        return "优惠券无效"
    # ...  imaginary 50 lines ...
    return f"订单完成 user={user_id} sku={sku} amount={amount}"


# --- 反模式 3: 观察者列表从不清理 ---


class LeakySubject:
    def __init__(self) -> None:
        self._observers: list[object] = []

    def subscribe(self, observer: object) -> None:
        self._observers.append(observer)

    def notify(self, msg: str) -> int:
        for obs in self._observers:
            if hasattr(obs, "on_msg"):
                obs.on_msg(msg)
        return len(self._observers)


class TempListener:
    def on_msg(self, msg: str) -> None:
        pass


def demo() -> None:
    print("[AntiPattern] 1. 全局 config 可被任意修改:")
    cfg = get_config()
    cfg["db"] = "production"
    print(f"  另一引用看到: {get_config()}")

    print("[AntiPattern] 2. 上帝函数门面:")
    print(f"  {god_place_order('A001', 99.0, 'u1', '')}")

    print("[AntiPattern] 3. 观察者泄漏 (订阅后不取消):")
    subject = LeakySubject()
    temp = TempListener()
    subject.subscribe(temp)
    subject.subscribe(TempListener())
    print(f"  订阅数: {subject.notify('hello')}")
    del temp
    print(f"  del temp 后订阅数仍为: {subject.notify('again')} (应 unsubscribe)")


if __name__ == "__main__":
    demo()
