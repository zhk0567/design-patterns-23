# 23 种设计模式（Python）

[![CI](https://github.com/zhk0567/design-patterns-23/actions/workflows/ci.yml/badge.svg)](https://github.com/zhk0567/design-patterns-23/actions/workflows/ci.yml)

GoF 23 种经典设计模式的 Python 示例。仅使用标准库，每个模式可单独运行。

[English README](README.en.md) · [学习指南](docs/GUIDE.md)

## 目录结构

```
design-patterns-23/
├── README.md
├── patterns/              # 23 个模式示例（含中英文 docstring、UML）
├── scripts/               # 运行与测试脚本
├── examples/              # 反模式演示
├── docs/
│   └── GUIDE.md           # 学习/对比/面试/反模式（唯一扩展文档）
├── run_all.py             # 快捷入口
├── learn.py
└── test_patterns.py
```

## 环境要求

- Python 3.10+

## 运行方式

```powershell
Set-Location f:\commercial\design-patterns-23

python patterns/01_singleton.py
python scripts/run_all.py
python scripts/learn.py
python scripts/ecommerce_demo.py
python scripts/run_async_demos.py
python examples/99_anti_patterns.py
python scripts/test_patterns.py
```

根目录 `python run_all.py` / `python learn.py` 等价于 `scripts/` 下对应脚本。

## 开发工具

```powershell
pip install -r requirements-dev.txt
pip install -e .
ruff format .
ruff check .
mypy .
```

## Windows 中文输出

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

## 说明

- 扩展阅读、模式对比、电商场景、面试题与反模式见 [docs/GUIDE.md](docs/GUIDE.md)
- 每个 `patterns/NN_*.py` 含 `demo()`，部分含 `demo_basic()` / `demo_advanced()` / `demo_async()`
- 加载示例：`from patterns import load` → `load("01_singleton").demo()`
