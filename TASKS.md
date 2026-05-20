# 后续任务清单

GoF 23 种设计模式 Python 扁平项目 — 进度跟踪。

---

## 已完成

- [x] MVP：23 个模式示例 + `run_all.py` + README
- [x] 阶段一：Windows 编码、`test_patterns.py`、CI、误用注释
- [x] 阶段二：`PATTERNS_COMPARE`、`STDLIB_MAPPING`、`STUDY`、`CHANGELOG`
- [x] 阶段二：**UML 类图** — 23 个文件 docstring + [docs/UML.md](docs/UML.md) 索引
- [x] 阶段三：单例线程安全、动态责任链、weakref 观察者、PrintVisitor、解释器扩展

---

## 四、工程化扩展（待办）

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
