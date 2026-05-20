# 23 种设计模式 UML 类图索引

各模式的 Mermaid `classDiagram` 位于对应 `NN_*.py` 文件顶部 docstring 中。  
在 GitHub、VS Code（Mermaid 插件）或支持 Mermaid 的 Markdown 预览中可渲染。

## 创建型

| 文件 | 模式 | 核心类 |
|------|------|--------|
| [01_singleton.py](../01_singleton.py) | Singleton | `AppConfig`, `ThreadSafeAppConfig` |
| [02_factory_method.py](../02_factory_method.py) | Factory Method | `LoggerFactory`, `Logger` |
| [03_abstract_factory.py](../03_abstract_factory.py) | Abstract Factory | `UIFactory`, `Button`, `TextBox` |
| [04_builder.py](../04_builder.py) | Builder | `HttpRequestBuilder`, `HttpRequest` |
| [05_prototype.py](../05_prototype.py) | Prototype | `Document` |

## 结构型

| 文件 | 模式 | 核心类 |
|------|------|--------|
| [06_adapter.py](../06_adapter.py) | Adapter | `LegacyPayAdapter`, `PaymentGateway` |
| [07_bridge.py](../07_bridge.py) | Bridge | `Shape`, `Renderer` |
| [08_composite.py](../08_composite.py) | Composite | `Folder`, `File` |
| [09_decorator.py](../09_decorator.py) | Decorator | `CoffeeDecorator`, `Coffee` |
| [10_facade.py](../10_facade.py) | Facade | `OrderFacade` |
| [11_flyweight.py](../11_flyweight.py) | Flyweight | `CharacterFlyweight`, `GlyphStyle` |
| [12_proxy.py](../12_proxy.py) | Proxy | `ImageProxy`, `RealImage` |

## 行为型

| 文件 | 模式 | 核心类 |
|------|------|--------|
| [13_chain_of_responsibility.py](../13_chain_of_responsibility.py) | Chain of Responsibility | `Handler`, `DynamicApprovalChain` |
| [14_command.py](../14_command.py) | Command | `Command`, `CommandHistory` |
| [15_interpreter.py](../15_interpreter.py) | Interpreter | `Expression`, `Add`, `Multiply` |
| [16_iterator.py](../16_iterator.py) | Iterator | `BookShelf`, `BookIterator` |
| [17_mediator.py](../17_mediator.py) | Mediator | `ChatRoom`, `User` |
| [18_memento.py](../18_memento.py) | Memento | `Editor`, `EditorMemento` |
| [19_observer.py](../19_observer.py) | Observer | `StockMarket`, `WeakStockMarket` |
| [20_state.py](../20_state.py) | State | `Order`, `OrderState` |
| [21_strategy.py](../21_strategy.py) | Strategy | `Sorter`, `SortStrategy` |
| [22_template_method.py](../22_template_method.py) | Template Method | `DataExporter` |
| [23_visitor.py](../23_visitor.py) | Visitor | `Visitor`, `SizeVisitor`, `PrintVisitor` |

## 如何查看

1. 打开任意 `NN_*.py`，阅读 docstring 中的 `类图 (Mermaid):` 段落。
2. 复制 `classDiagram` 及以下行到 [Mermaid Live Editor](https://mermaid.live) 预览。
3. 或在 IDE 中安装 Mermaid 预览插件后直接渲染 Markdown 代码块（若将类图复制到笔记中）。
