# 设计模式相关反模式

反模式：看似在用模式，实则增加复杂度或引入新问题。  
可运行对照见 [`patterns/99_anti_patterns.py`](../examples/99_anti_patterns.py)。

| 反模式 | 表现 | 更合适的做法 |
|--------|------|--------------|
| 万能单例 | 所有全局状态都塞进 Singleton | 依赖注入、显式传参；仅真正唯一资源用单例 |
| 模式滥用 | 简单 `if/else` 硬拆 10 个类 | YAGNI；需要扩展时再引入模式 |
| 上帝门面 | Facade 里写满业务规则 | Facade 只编排，规则下沉 Domain/Service |
| 观察者风暴 | 一个事件触发链式更新再触发事件 | 事件边界清晰、避免循环订阅 |
| 策略爆炸 | 每个小变体一个 Strategy 类 | 表驱动、配置化；策略用于算法族 |
| 装饰器链地狱 | 10 层 Decorator 难调试 | 限制层数；或管道/责任链更清晰 |
| 伪单例 | 模块级变量却套 Singleton 类 | Python 直接用模块即可 |
| 拷贝粘贴原型 | `clone` 浅拷贝共享可变状态 | `deepcopy` 或不可变数据结构 |
| 访问者滥用 | 元素类型每周都变却用 Visitor | 数据稳定、操作多变时才用 |
| 同步阻塞异步 | 在 `async` 里调阻塞 IO 不 offload | `asyncio.to_thread` 或原生 async API |

## 与本仓库正例的对应

| 正例文件 | 常见反模式 |
|----------|------------|
| `patterns/01_singleton.py` | 非线程安全单例用于多线程 Web |
| `patterns/09_decorator.py` | 与 Python `@decorator` 语法混为一谈 |
| `patterns/10_facade.py` | Facade 替代所有分层 |
| `patterns/19_observer.py` | 强引用观察者从不 unsubscribe |

| `examples/anti_inheritance_abuse.py` | 配料组合导致继承爆炸 |
| `examples/anti_singleton_god_object.py` | 单例充当全局上帝对象 |

运行演示：

```powershell
python examples/99_anti_patterns.py
python examples/anti_inheritance_abuse.py
python examples/anti_singleton_god_object.py
```
