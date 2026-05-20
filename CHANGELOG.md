# Changelog

All notable changes to this project are documented in this file.

## [Unreleased]

### Changed

- Reorganize repo layout: `patterns/`, `scripts/`, `examples/`; root keeps config and docs only

### Added

- Phase 5: ecommerce scenario doc, framework mapping, interview Q&A, anti-patterns (`examples/99_anti_patterns.py`)
- Async demos: `demo_async()` on proxy/command/observer, `run_async_demos.py`
- Phase 4 tooling: `pyproject.toml`, `requirements-dev.txt`, `learn.py`, `generate_cheatsheet.py`, `docs/CHEATSHEET.md`
- CI: ruff format/lint, mypy, cheatsheet drift check
- Mermaid UML class diagrams in all 23 pattern module docstrings; `docs/UML.md` index
- Phase 3 enhancements: thread-safe singleton, dynamic approval chain, weakref observer, PrintVisitor, interpreter multiply/subtract; `demo_basic()` / `demo_advanced()` dual entry on affected modules

### Added (earlier)

- Windows UTF-8 notes in README
- `test_patterns.py` unittest smoke tests for all 23 demos
- GitHub Actions CI (`.github/workflows/ci.yml`)
- Docs: `docs/PATTERNS_COMPARE.md`, `docs/STDLIB_MAPPING.md`, `docs/STUDY.md`
- Pitfall / misuse notes in each pattern module docstring

## [0.1.0] - 2025-11-15

### Added

- Initial flat-layout GoF 23 Python examples (`01_singleton.py` … `23_visitor.py`)
- `run_all.py` batch runner
- `README.md`, `TASKS.md`, `requirements.txt`, `.gitignore`
