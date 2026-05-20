# 23 Design Patterns in Python

[![CI](https://github.com/zhk0567/design-patterns-23/actions/workflows/ci.yml/badge.svg)](https://github.com/zhk0567/design-patterns-23/actions/workflows/ci.yml)

Runnable GoF design pattern examples. Standard library only.

[中文 README](README.md) · [Guide](docs/GUIDE.md)

## Layout

```
design-patterns-23/
├── patterns/     # 23 demos
├── scripts/      # runners and tests
├── examples/     # anti-pattern demos
└── docs/GUIDE.md # single learning guide
```

## Quick start

```bash
python patterns/01_singleton.py
python scripts/run_all.py
python scripts/learn.py
python scripts/ecommerce_demo.py
pip install -e .
```

## Docs

All learning material is in [docs/GUIDE.md](docs/GUIDE.md): comparisons, e-commerce scenario, interview notes, anti-patterns, and install instructions.

UML class diagrams live in each `patterns/*.py` docstring (Mermaid).
