# PyPI / 本地安装

本仓库可作为学习包本地安装，**默认不强制发布到 PyPI**。

## 本地可编辑安装

```powershell
Set-Location f:\commercial\design-patterns-23
pip install -e .
python -c "from patterns import load; load('01_singleton').demo()"
```

安装后获得：

- `patterns` 包（含 `py.typed`，供类型检查器识别）
- `patterns.load(name)` 加载各模式模块

## 发布到 PyPI（维护者）

1. 安装构建工具：`pip install build twine`
2. 更新 `pyproject.toml` 中 `version`
3. 构建：`python -m build`
4. 上传：`twine upload dist/*`

包名：`design-patterns-23`（与仓库一致）。

## 说明

- 模式文件以 `01_singleton` 等编号命名，通过 `patterns.load()` 加载，而非 `import patterns.singleton`
- 运行示例仍推荐克隆仓库后使用 `python patterns/01_singleton.py` 或 `python scripts/run_all.py`
