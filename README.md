# 23 种设计模式（Python）

GoF 23 种经典设计模式的 Python 示例，每个模式一个独立文件，全部位于项目根目录。仅使用标准库，每个文件均可单独运行。

## 环境要求

- Python 3.10+

## 运行方式

```powershell
# 进入项目目录
Set-Location f:\commercial\design-patterns-23

# 运行单个示例
python 01_singleton.py

# 运行全部 23 个示例
python run_all.py

# 交互式选择模式运行
python learn.py

# 异步 demo（代理 / 命令 / 观察者）
python run_async_demos.py

# 反模式演示
python 99_anti_patterns.py

# 运行 smoke 测试（标准库 unittest，无需 pytest）
python test_patterns.py
```

## 开发工具（阶段四）

```powershell
pip install -r requirements-dev.txt

ruff format .          # 格式化
ruff check .           # 静态检查
mypy .                 # 类型检查
python generate_cheatsheet.py   # 重新生成 docs/CHEATSHEET.md
```

## Windows 终端与中文输出

在 Windows PowerShell / CMD 下，若中文乱码或报 `gbk` 编码错误，可先设置 UTF-8 再运行：

```powershell
$env:PYTHONIOENCODING = "utf-8"
chcp 65001
python run_all.py
```

说明：

- `run_all.py` 会尝试将 stdout/stderr 重配置为 UTF-8。
- 示例中已避免 `¥`、emoji 等在 GBK 控制台下易出错的字符。
- 若仅单个文件乱码，同样可先执行 `$env:PYTHONIOENCODING = "utf-8"` 再运行该文件。

## 模式索引

### 创建型（5）

| 编号 | 文件 | 英文名 | 中文名 |
|------|------|--------|--------|
| 01 | `01_singleton.py` | Singleton | 单例 |
| 02 | `02_factory_method.py` | Factory Method | 工厂方法 |
| 03 | `03_abstract_factory.py` | Abstract Factory | 抽象工厂 |
| 04 | `04_builder.py` | Builder | 建造者 |
| 05 | `05_prototype.py` | Prototype | 原型 |

### 结构型（7）

| 编号 | 文件 | 英文名 | 中文名 |
|------|------|--------|--------|
| 06 | `06_adapter.py` | Adapter | 适配器 |
| 07 | `07_bridge.py` | Bridge | 桥接 |
| 08 | `08_composite.py` | Composite | 组合 |
| 09 | `09_decorator.py` | Decorator | 装饰器 |
| 10 | `10_facade.py` | Facade | 外观 |
| 11 | `11_flyweight.py` | Flyweight | 享元 |
| 12 | `12_proxy.py` | Proxy | 代理 |

### 行为型（11）

| 编号 | 文件 | 英文名 | 中文名 |
|------|------|--------|--------|
| 13 | `13_chain_of_responsibility.py` | Chain of Responsibility | 责任链 |
| 14 | `14_command.py` | Command | 命令 |
| 15 | `15_interpreter.py` | Interpreter | 解释器 |
| 16 | `16_iterator.py` | Iterator | 迭代器 |
| 17 | `17_mediator.py` | Mediator | 中介者 |
| 18 | `18_memento.py` | Memento | 备忘录 |
| 19 | `19_observer.py` | Observer | 观察者 |
| 20 | `20_state.py` | State | 状态 |
| 21 | `21_strategy.py` | Strategy | 策略 |
| 22 | `22_template_method.py` | Template Method | 模板方法 |
| 23 | `23_visitor.py` | Visitor | 访问者 |

## 项目结构

```
design-patterns-23/
├── README.md
├── TASKS.md
├── CHANGELOG.md
├── test_patterns.py
├── learn.py
├── run_async_demos.py
├── 99_anti_patterns.py
├── generate_cheatsheet.py
├── pyproject.toml
├── run_all.py
├── .github/workflows/ci.yml
├── docs/
│   ├── PATTERNS_COMPARE.md
│   ├── STDLIB_MAPPING.md
│   ├── STUDY.md
│   ├── UML.md
│   ├── CHEATSHEET.md
│   ├── ECOMMERCE_SCENARIO.md
│   ├── FRAMEWORK_MAPPING.md
│   ├── INTERVIEW.md
│   └── ANTI_PATTERNS.md
├── 01_singleton.py
├── ...
└── 23_visitor.py
```

## 文档

| 文件 | 说明 |
|------|------|
| [TASKS.md](TASKS.md) | 后续任务清单 |
| [CHANGELOG.md](CHANGELOG.md) | 版本变更记录 |
| [docs/PATTERNS_COMPARE.md](docs/PATTERNS_COMPARE.md) | 易混淆模式对比 |
| [docs/STDLIB_MAPPING.md](docs/STDLIB_MAPPING.md) | 与 Python 标准库对照 |
| [docs/STUDY.md](docs/STUDY.md) | 学习路径与自测题 |
| [docs/UML.md](docs/UML.md) | 23 个模式 Mermaid 类图索引 |
| [docs/CHEATSHEET.md](docs/CHEATSHEET.md) | 模式速查表（自动生成） |
| [docs/ECOMMERCE_SCENARIO.md](docs/ECOMMERCE_SCENARIO.md) | 23 模式 × 电商订单场景 |
| [docs/FRAMEWORK_MAPPING.md](docs/FRAMEWORK_MAPPING.md) | Spring / Django 对照 |
| [docs/INTERVIEW.md](docs/INTERVIEW.md) | 面试题与参考答案 |
| [docs/ANTI_PATTERNS.md](docs/ANTI_PATTERNS.md) | 反模式说明 |

## 说明

- 后续学习与工程化任务见 [TASKS.md](TASKS.md)
- 每个 `NN_*.py` 包含 `demo()` 函数，演示该模式的核心思想
- `run_all.py` 按编号顺序导入并执行全部示例
- 示例场景涵盖配置单例、日志工厂、UI 主题、HTTP 建造者、审批链、撤销命令等经典用例
