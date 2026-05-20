# 23 种设计模式（Python）

GoF 23 种经典设计模式的 Python 示例。仅使用标准库，每个模式可单独运行。

## 目录结构

```
design-patterns-23/
├── README.md
├── TASKS.md
├── CHANGELOG.md
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── patterns/              # 23 个模式示例
│   ├── 01_singleton.py
│   └── ...
├── scripts/               # 运行与工具脚本
│   ├── run_all.py
│   ├── learn.py
│   ├── test_patterns.py
│   └── ...
├── examples/              # 反模式等补充示例
│   └── 99_anti_patterns.py
└── docs/                  # 文档与速查表
```

## 环境要求

- Python 3.10+

## 运行方式

```powershell
Set-Location f:\commercial\design-patterns-23

# 单个模式
python patterns/01_singleton.py

# 全部 23 个
python scripts/run_all.py

# 交互菜单
python scripts/learn.py

# 异步 demo（12 / 14 / 19）
python scripts/run_async_demos.py

# 反模式
python examples/99_anti_patterns.py

# 测试
python scripts/test_patterns.py
```

## 开发工具

```powershell
pip install -r requirements-dev.txt
ruff format .
ruff check .
mypy .
python scripts/generate_cheatsheet.py
```

## Windows 终端与中文输出

```powershell
$env:PYTHONIOENCODING = "utf-8"
chcp 65001
python scripts/run_all.py
```

## 模式索引

### 创建型（5）

| 编号 | 文件 | 英文名 | 中文名 |
|------|------|--------|--------|
| 01 | `patterns/01_singleton.py` | Singleton | 单例 |
| 02 | `patterns/02_factory_method.py` | Factory Method | 工厂方法 |
| 03 | `patterns/03_abstract_factory.py` | Abstract Factory | 抽象工厂 |
| 04 | `patterns/04_builder.py` | Builder | 建造者 |
| 05 | `patterns/05_prototype.py` | Prototype | 原型 |

### 结构型（7）

| 编号 | 文件 | 英文名 | 中文名 |
|------|------|--------|--------|
| 06 | `patterns/06_adapter.py` | Adapter | 适配器 |
| 07 | `patterns/07_bridge.py` | Bridge | 桥接 |
| 08 | `patterns/08_composite.py` | Composite | 组合 |
| 09 | `patterns/09_decorator.py` | Decorator | 装饰器 |
| 10 | `patterns/10_facade.py` | Facade | 外观 |
| 11 | `patterns/11_flyweight.py` | Flyweight | 享元 |
| 12 | `patterns/12_proxy.py` | Proxy | 代理 |

### 行为型（11）

| 编号 | 文件 | 英文名 | 中文名 |
|------|------|--------|--------|
| 13 | `patterns/13_chain_of_responsibility.py` | Chain of Responsibility | 责任链 |
| 14 | `patterns/14_command.py` | Command | 命令 |
| 15 | `patterns/15_interpreter.py` | Interpreter | 解释器 |
| 16 | `patterns/16_iterator.py` | Iterator | 迭代器 |
| 17 | `patterns/17_mediator.py` | Mediator | 中介者 |
| 18 | `patterns/18_memento.py` | Memento | 备忘录 |
| 19 | `patterns/19_observer.py` | Observer | 观察者 |
| 20 | `patterns/20_state.py` | State | 状态 |
| 21 | `patterns/21_strategy.py` | Strategy | 策略 |
| 22 | `patterns/22_template_method.py` | Template Method | 模板方法 |
| 23 | `patterns/23_visitor.py` | Visitor | 访问者 |

## 文档

| 文件 | 说明 |
|------|------|
| [TASKS.md](TASKS.md) | 任务清单 |
| [CHANGELOG.md](CHANGELOG.md) | 变更记录 |
| [docs/CHEATSHEET.md](docs/CHEATSHEET.md) | 速查表（自动生成） |
| [docs/UML.md](docs/UML.md) | UML 类图索引 |
| [docs/ECOMMERCE_SCENARIO.md](docs/ECOMMERCE_SCENARIO.md) | 电商场景对照 |
| [docs/FRAMEWORK_MAPPING.md](docs/FRAMEWORK_MAPPING.md) | Spring / Django 对照 |
| [docs/INTERVIEW.md](docs/INTERVIEW.md) | 面试题 |
| [docs/ANTI_PATTERNS.md](docs/ANTI_PATTERNS.md) | 反模式 |
| [docs/PATTERNS_COMPARE.md](docs/PATTERNS_COMPARE.md) | 模式对比 |
| [docs/STUDY.md](docs/STUDY.md) | 学习路径 |

## 说明

- 脚本通过 `patterns.load("01_singleton")` 加载示例模块
- 每个模式文件含 `demo()`，部分含 `demo_basic()` / `demo_advanced()` / `demo_async()`
