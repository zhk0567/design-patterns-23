# 后续任务清单

GoF 23 种设计模式 Python 扁平项目 — 进度跟踪。

---

## 已完成

- [x] MVP：23 个模式示例 + `run_all.py` + README
- [x] 阶段一：Windows 编码说明、`test_patterns.py`、CI、23 文件「误用」注释
- [x] 阶段二（部分）：`PATTERNS_COMPARE`、`STDLIB_MAPPING`、`STUDY`、`CHANGELOG`
- [x] **阶段三：示例代码增强**
  - [x] `01_singleton.py` — 线程安全 DCL + `demo_basic` / `demo_advanced`
  - [x] `13_chain_of_responsibility.py` — `DynamicApprovalChain` 动态增删处理器
  - [x] `19_observer.py` — `WeakStockMarket` 弱引用观察者
  - [x] `23_visitor.py` — `PrintVisitor` 第二种访问者
  - [x] `15_interpreter.py` — `Subtract` / `Multiply`，复合表达式

---

## 二、学习与文档深化（待办）

- [ ] **每个文件增加 UML 类图（Mermaid）**

---

## 四、工程化扩展

- [ ] **类型检查** — `pyproject.toml` + `mypy` / `pyright`
- [ ] **代码格式化** — `ruff format` 或 `black`
- [ ] **交互式学习脚本 `learn.py`**
- [ ] **速查表生成**

---

## 五、进阶专题

- [ ] **23 模式 × 同一业务场景**
- [ ] **与主流框架对照笔记**
- [ ] **并发/异步变体**
- [ ] **反模式合集**
- [ ] **面试题 + 参考答案**

---

## 快速命令

```powershell
Set-Location f:\commercial\design-patterns-23
python 01_singleton.py
python test_patterns.py
python run_all.py
```
