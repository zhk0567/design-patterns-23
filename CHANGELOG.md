# Changelog

All notable changes to this project are documented in this file.

## [1.1.0] - 2026-05-20

### Added

- Ecommerce demo: Chain approval + Command cancel/undo
- English docstring blocks in all 23 pattern modules
- `patterns/py.typed`, hatchling packaging (`pip install -e .`)
- `.github/workflows/release.yml` uploads CSV, UML_ALL, CHEATSHEET on tag
- `docs/PYPI.md`, `scripts/test_ecommerce_demo.py`

## [1.0.0] - 2026-05-20

### Added

- `scripts/ecommerce_demo.py` end-to-end order flow (Facade + State + Observer)
- `docs/PATTERN_MAP.md`, `docs/UML_ALL.md`, `docs/interview_cards.csv`
- `README.en.md`, root shortcuts (`run_all.py`, `learn.py`, `test_patterns.py`)
- `examples/anti_inheritance_abuse.py`, `examples/anti_singleton_god_object.py`
- `scripts/export_interview_cards.py`, `scripts/generate_uml_page.py`
- `scripts/test_unit_patterns.py`, `scripts/test_async_demos.py`
- `.pre-commit-config.yaml`
- `learn.py` category filter and module-name input
- CI badge in README

### Changed

- Project layout: `patterns/`, `scripts/`, `examples/`, `docs/`
- `pyproject.toml` version 1.0.0; stricter mypy on `patterns.*`
- CI runs unit tests and async demo tests

## [0.3.0] - 2026-05-20

### Changed

- Reorganize repo layout: `patterns/`, `scripts/`, `examples/`

### Added

- Phase 3–5 features: async demos, interview docs, anti-patterns, tooling (ruff/mypy/learn)

## [0.1.0] - 2025-11-15

### Added

- Initial GoF 23 Python examples and `run_all.py`
