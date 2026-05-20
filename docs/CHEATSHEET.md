# 设计模式速查表

> 由 `scripts/generate_cheatsheet.py` 从各模块 docstring 自动生成，请勿手改。
> 重新生成: `python scripts/generate_cheatsheet.py`

| # | 文件 | 模式 | 意图 | 适用 |
|---|------|------|------|------|
| 01 | `patterns/01_singleton.py` | 单例模式 (Singleton) | 确保一个类只有一个实例，并提供全局访问点。 | 配置中心、日志器、连接池等。 |
| 02 | `patterns/02_factory_method.py` | 工厂方法模式 (Factory Method) | 定义创建对象的接口，由子类决定实例化哪一个类。 | 日志、文档导出等需要按类型创建产品的场景。 |
| 03 | `patterns/03_abstract_factory.py` | 抽象工厂模式 (Abstract Factory) | 提供创建一系列相关或相互依赖对象的接口，而无需指定具体类。 | 跨平台 UI、主题套件（按钮+输入框成组切换）。 |
| 04 | `patterns/04_builder.py` | 建造者模式 (Builder) | 将复杂对象的构建与表示分离，使同样的构建过程可以创建不同的表示。 | HTTP 请求、SQL、配置对象等分步组装。 |
| 05 | `patterns/05_prototype.py` | 原型模式 (Prototype) | 通过复制现有实例来创建新对象，而不是通过 new/构造器。 | 克隆成本高或配置复杂的对象（文档、游戏实体等）。 |
| 06 | `patterns/06_adapter.py` | 适配器模式 (Adapter) | 将一个类的接口转换成客户希望的另一个接口，使原本不兼容的类可以合作。 | 对接第三方支付、遗留 API、第三方 SDK。 |
| 07 | `patterns/07_bridge.py` | 桥接模式 (Bridge) | 将抽象与实现分离，使它们可以独立变化。 | 形状×渲染器、消息×发送渠道等多维度扩展。 |
| 08 | `patterns/08_composite.py` | 组合模式 (Composite) | 将对象组合成树形结构以表示「部分-整体」层次，使客户端对单个对象与组合对象的使用一致。 | 文件系统、组织架构、菜单树。 |
| 09 | `patterns/09_decorator.py` | 装饰器模式 (Decorator) | 动态地给对象添加额外职责，比继承更灵活。 | 咖啡配料、数据流包装、权限叠加。 |
| 10 | `patterns/10_facade.py` | 外观模式 (Facade) | 为子系统中的一组接口提供统一的高层接口，降低使用复杂度。 | 启动流程、下单流程、多媒体播放等跨多个子模块的操作。 |
| 11 | `patterns/11_flyweight.py` | 享元模式 (Flyweight) | 运用共享技术有效地支持大量细粒度对象，减少内存占用。 | 文本编辑器字符、地图瓦片、图标缓存。 |
| 12 | `patterns/12_proxy.py` | 代理模式 (Proxy) | 为其他对象提供一种代理以控制对这个对象的访问。 | 懒加载、访问控制、远程代理、缓存代理。 |
| 13 | `patterns/13_chain_of_responsibility.py` | 责任链模式 (Chain of Responsibility) | 使多个对象都有机会处理请求，从而避免请求发送者与接收者耦合。 | 审批流、日志过滤链、中间件管道。 |
| 14 | `patterns/14_command.py` | 命令模式 (Command) | 将请求封装为对象，从而支持参数化、队列化、日志与撤销。 | 撤销/重做、任务队列、宏命令。 |
| 15 | `patterns/15_interpreter.py` | 解释器模式 (Interpreter) | 给定一种语言，定义其文法表示，并定义解释器来解释语言中的句子。 | 简单 DSL、规则引擎、表达式求值。 |
| 16 | `patterns/16_iterator.py` | 迭代器模式 (Iterator) | 提供一种方法顺序访问聚合对象中的各个元素，而不暴露其内部表示。 | 自定义集合遍历、分页、树形遍历。 |
| 17 | `patterns/17_mediator.py` | 中介者模式 (Mediator) | 用一个中介对象封装一系列对象交互，使对象之间不必显式相互引用。 | 聊天室、航空管制、表单联动。 |
| 18 | `patterns/18_memento.py` | 备忘录模式 (Memento) | 在不破坏封装的前提下，捕获对象的内部状态并在之后恢复。 | 编辑器撤销、游戏存档、配置快照。 |
| 19 | `patterns/19_observer.py` | 观察者模式 (Observer) | 定义对象间一对多依赖，当一个对象状态改变时，所有依赖者都会收到通知。 | 事件总线、股票行情、模型-视图更新。 |
| 20 | `patterns/20_state.py` | 状态模式 (State) | 允许对象在内部状态改变时改变其行为，对象看起来好像修改了类。 | 订单状态机、工作流、TCP 连接状态。 |
| 21 | `patterns/21_strategy.py` | 策略模式 (Strategy) | 定义一系列算法，把它们封装起来，并使它们可以互相替换。 | 排序方式、折扣计算、路径规划、压缩算法。 |
| 22 | `patterns/22_template_method.py` | 模板方法模式 (Template Method) | 在父类中定义算法骨架，将某些步骤延迟到子类实现。 | 数据导出、游戏回合流程、构建流程固定但细节可变。 |
| 23 | `patterns/23_visitor.py` | 访问者模式 (Visitor) | 表示一个作用于某对象结构中的各元素的操作，可在不改变元素类的前提下定义新操作。 | 编译器 AST 遍历、文件系统统计、报表生成。 |

## 运行

```powershell
python scripts/learn.py
python scripts/run_all.py
```
