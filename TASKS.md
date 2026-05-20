# 后续任务清单

> 可选增强已全部完成。新需求可追加到下方。

---

## 已完成（可选增强）

- [x] 电商脚本扩展：Chain 退款审批 + Command 取消/撤销
- [x] GitHub Release 工作流：推送 `v*` 标签时上传 CSV / UML / 速查表
- [x] `patterns/py.typed` + `pyproject.toml` 打包配置（`pip install -e .`）
- [x] 23 个模式文件 docstring 中英文对照（English 段落）

---

## 可追加想法

- [ ] 在 GitHub 网页手动创建 Release 并核对附件（若未跑过 `release.yml`）
- [ ] 正式发布到 PyPI（`twine upload`，见 [docs/PYPI.md](docs/PYPI.md)）

---

## 快速命令

```powershell
Set-Location f:\commercial\design-patterns-23
python scripts/ecommerce_demo.py
pip install -e .
python scripts/test_ecommerce_demo.py
```
