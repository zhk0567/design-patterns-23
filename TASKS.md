# 后续任务清单

GoF 23 种设计模式 Python 扁平项目 — 进度跟踪。

---

## 已完成

- [x] MVP ~ 阶段三（示例、CI、UML、增强 demo）
- [x] **阶段四：工程化扩展**
  - [x] `pyproject.toml` + `mypy` 类型检查
  - [x] `ruff format` / `ruff check` 代码格式化与 lint
  - [x] `learn.py` 交互式学习菜单
  - [x] `generate_cheatsheet.py` → `docs/CHEATSHEET.md`
  - [x] `requirements-dev.txt`、CI 集成 ruff/mypy/速查表校验

---

## 五、进阶专题（待办）

- [ ] **23 模式 × 同一业务场景**
- [ ] **与主流框架对照笔记**
- [ ] **并发/异步变体**
- [ ] **反模式合集**
- [ ] **面试题 + 参考答案**

---

## 快速命令

```powershell
Set-Location f:\commercial\design-patterns-23
python learn.py
python test_patterns.py
pip install -r requirements-dev.txt
ruff format . && ruff check . && mypy .
python generate_cheatsheet.py
```
