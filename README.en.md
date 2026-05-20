# 23 Design Patterns in Python

Runnable examples for all **Gang of Four (GoF)** design patterns. Standard library only.

[![CI](https://github.com/zhk0567/design-patterns-23/actions/workflows/ci.yml/badge.svg)](https://github.com/zhk0567/design-patterns-23/actions/workflows/ci.yml)

[中文 README](README.md)

## Layout

```
design-patterns-23/
├── patterns/     # 23 pattern demos (01_singleton.py … 23_visitor.py)
├── scripts/      # runners and tooling
├── examples/     # anti-pattern demos
└── docs/         # guides, cheatsheet, interview Q&A
```

## Requirements

- Python 3.10+

## Quick start

```bash
cd design-patterns-23

# Single pattern
python patterns/01_singleton.py

# All 23 demos
python scripts/run_all.py

# Interactive menu
python scripts/learn.py

# E-commerce end-to-end (Facade + State + Observer)
python scripts/ecommerce_demo.py
```

## Dev tools

```bash
pip install -r requirements-dev.txt
ruff format .
ruff check .
mypy .
python scripts/test_patterns.py
python scripts/test_unit_patterns.py
```

## Docs

| File | Description |
|------|-------------|
| [docs/CHEATSHEET.md](docs/CHEATSHEET.md) | Auto-generated cheat sheet |
| [docs/PATTERN_MAP.md](docs/PATTERN_MAP.md) | Pattern relationship map |
| [docs/ECOMMERCE_SCENARIO.md](docs/ECOMMERCE_SCENARIO.md) | Same business scenario for all 23 |
| [docs/INTERVIEW.md](docs/INTERVIEW.md) | Interview Q&A (Chinese) |
| [docs/UML_ALL.md](docs/UML_ALL.md) | Mermaid class diagrams |

## License

Educational project. Feel free to learn and fork.
