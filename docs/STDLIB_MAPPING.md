# 设计模式与 Python 标准库对照

| 模式 | 标准库 / 内置机制 | 说明 |
|------|-------------------|------|
| 单例 | 模块对象、`functools.lru_cache` | 模块天然单例；慎用类单例 |
| 工厂方法 | `logging.getLogger` 等 | 由配置决定 Handler 类型 |
| 抽象工厂 | — | 较少内置，多在框架层 |
| 建造者 | `dataclasses`、链式 API | 常用手写 Builder 或 dataclass |
| 原型 | `copy.copy` / `copy.deepcopy` | 见 `05_prototype.py` |
| 适配器 | `io` 包装流 | `TextIOWrapper` 等 |
| 桥接 | — | 组合替代多继承 |
| 组合 | `os.walk`、树形 API | 统一遍历接口 |
| 装饰器 | `functools.wraps`、`@staticmethod` | 语法糖是函数装饰，模式是类组合 |
| 外观 | 高层 API 模块 | 如 `subprocess.run` 封装细节 |
| 享元 | `sys.intern` | 字符串驻留 |
| 代理 | `weakref.proxy`、`unittest.mock` | 延迟/替身 |
| 责任链 | `warnings` 过滤器链 | 中间件风格 |
| 命令 | — | 常自建 Command 对象 |
| 解释器 | `ast` 模块 | 复杂语法用 AST，非手写解释器 |
| 迭代器 | `iter()`、`collections.abc.Iterator` | 协议：`__iter__` / `__next__` |
| 中介者 | — | GUI 框架常见 |
| 备忘录 | `pickle`、快照 | 注意序列化安全 |
| 观察者 | — | 3.11+ 可参考异步事件；常用自建 |
| 状态 | `enum.Enum` | 状态可建模为枚举+转移表 |
| 策略 | `functools.cmp_to_key` 等 | 传入 key/callable |
| 模板方法 | `unittest.TestCase` | `setUp` / `test_*` 固定流程 |
| 访问者 | `ast.NodeVisitor` | AST 遍历的典型访问者 |

## 推荐阅读顺序

1. 创建型 `01`–`05`
2. 结构型 `06`–`12`
3. 行为型 `13`–`23`

每学完一类，运行 `python test_patterns.py` 做 smoke 验证。
