# 后续任务清单

GoF 23 种设计模式 Python 扁平项目 — 进度跟踪。

---

## 已完成（MVP + 阶段 1/2 部分）

- [x] 创建型 5 个示例：`01_singleton.py` ~ `05_prototype.py`
- [x] 结构型 7 个示例：`06_adapter.py` ~ `12_proxy.py`
- [x] 行为型 11 个示例：`13_chain_of_responsibility.py` ~ `23_visitor.py`
- [x] 每个模式文件含 `demo()` + `if __name__ == "__main__"`
- [x] 脚手架：`README.md`、`requirements.txt`、`.gitignore`、`run_all.py`
- [x] `run_all.py` 全量运行 23 个示例
- [x] README 模式索引表与运行说明
- [x] Windows 控制台编码兼容
- [x] Git 初始化与推送至 `git@github.com:zhk0567/design-patterns-23.git`
- [x] **README 补充 Windows 编码说明**（`PYTHONIOENCODING`、`chcp 65001`）
- [x] **为每个模式补充「反例/误用」注释**（23 个文件 docstring）
- [x] **`test_patterns.py` smoke tests**（stdlib unittest）
- [x] **GitHub Actions CI**（`.github/workflows/ci.yml`）
- [x] **模式对比笔记** — `docs/PATTERNS_COMPARE.md`
- [x] **与 Python 标准库对照表** — `docs/STDLIB_MAPPING.md`
- [x] **学习路径与自测题** — `docs/STUDY.md`
- [x] **`CHANGELOG.md`**

---

## 一、巩固与质量（建议优先）

- [x] Git 初始化与首次提交
- [x] README 补充 Windows 编码说明
- [x] 为每个模式补充「反例/误用」注释
- [x] 添加 `test_patterns.py`
- [x] CI 流水线（GitHub Actions）

---

## 二、学习与文档深化

- [ ] **每个文件增加 UML 类图（Mermaid）** — 写在文件顶部 docstring 或 README 附录
- [x] **模式对比笔记** — `docs/PATTERNS_COMPARE.md`
- [x] **与 Python 标准库对照表** — `docs/STDLIB_MAPPING.md`
- [x] **学习路径与自测题** — `docs/STUDY.md`
- [x] **`CHANGELOG.md`**

---

## 三、示例代码增强（保持根目录扁平）

- [ ] **单例：线程安全版本** — `threading.Lock`，并与现有 demo 对比
- [ ] **责任链：动态增删处理器**
- [ ] **观察者：弱引用观察者**
- [ ] **访问者：第二种访问者** — 如 `PrintVisitor`
- [ ] **解释器：扩展加减乘**
- [ ] **复杂示例双入口** — `demo_basic()` / `demo_advanced()`

---

## 四、工程化扩展

- [ ] **类型检查** — `pyproject.toml` + `mypy` / `pyright`
- [ ] **代码格式化** — `ruff format` 或 `black`
- [ ] **交互式学习脚本 `learn.py`**
- [ ] **速查表生成** — 从 docstring 汇总 Markdown/HTML

---

## 五、进阶专题（第二阶段）

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
