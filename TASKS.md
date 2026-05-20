# 后续任务清单

GoF 23 种设计模式 Python 扁平项目 — 进度跟踪。

---

## 已完成

- [x] MVP ~ 阶段四（示例、CI、UML、工具链、速查表）
- [x] **阶段五：进阶专题**
  - [x] [docs/ECOMMERCE_SCENARIO.md](docs/ECOMMERCE_SCENARIO.md) — 23 模式 × 电商订单
  - [x] [docs/FRAMEWORK_MAPPING.md](docs/FRAMEWORK_MAPPING.md) — Spring / Django 对照
  - [x] [docs/ANTI_PATTERNS.md](docs/ANTI_PATTERNS.md) + `99_anti_patterns.py`
  - [x] [docs/INTERVIEW.md](docs/INTERVIEW.md) — 面试题与参考答案
  - [x] 异步变体：`12_proxy` / `14_command` / `19_observer` 的 `demo_async()` + `run_async_demos.py`

---

## 可选后续

- [ ] 将电商场景写成可运行的迷你端到端脚本（跨文件编排）
- [ ] 面试题按模式拆分为 Anki / 闪卡格式

---

## 快速命令

```powershell
Set-Location f:\commercial\design-patterns-23
python learn.py
python run_async_demos.py
python 99_anti_patterns.py
python test_patterns.py
```
