<div align="center" markdown="1">

# NBA AI

[![PyPI version](https://img.shields.io/pypi/v/nba-ai.svg)](https://pypi.org/project/nba-ai/)
[![python](https://img.shields.io/badge/-Python_%7C_3.11%7C_3.12%7C_3.13%7C_3.14-blue?logo=python&logoColor=white)](https://www.python.org/downloads/source/)
[![uv](https://img.shields.io/badge/-uv_dependency_management-2C5F2D?logo=python&logoColor=white)](https://docs.astral.sh/uv/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://docs.pydantic.dev/latest/contributing/#badges)
[![tests](https://github.com/Mai0313/nba_ai/actions/workflows/test.yml/badge.svg)](https://github.com/Mai0313/nba_ai/actions/workflows/test.yml)
[![code-quality](https://github.com/Mai0313/nba_ai/actions/workflows/code-quality-check.yml/badge.svg)](https://github.com/Mai0313/nba_ai/actions/workflows/code-quality-check.yml)
[![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)](https://github.com/Mai0313/nba_ai/tree/main?tab=License-1-ov-file)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Mai0313/nba_ai/pulls)
[![contributors](https://img.shields.io/github/contributors/Mai0313/nba_ai.svg)](https://github.com/Mai0313/nba_ai/graphs/contributors)

</div>

🏀 **NBA AI** is a toolkit designed to download, archive, and analyze NBA data.

It serves two main purposes:

1. **Data Collection**: Fetching scores, player statistics, and availability data from NBA.com in a structured format.
2. **AI Analysis**: Future plans include training models on this data and using LLMs to analyze news for predictive insights.

## ✨ Features

- **Data Crawler**: Automated downloading of NBA stats (scores, player logs, usage rates).
- **Structured Storage**: Archiving data for historical analysis and model training.
- **AI Integration**: (Planned) Machine learning models for outcome prediction and LLM-driven news analysis.
- **Modern Tooling**: Built with `uv`, `ruff`, `mypy`, and `pytest` for a robust development environment.

## 🚀 Quick Start

Prerequisites:

- Python 3.11–3.14
- `uv` (install with `make uv-install`)

Local setup:

```bash
make uv-install               # once
uv sync                       # install base deps
uv tool install pre-commit    # or: uv sync --group dev
make format                   # run pre-commit hooks
make test                     # run tests
```

Run the CLI:

```bash
uv run nba_ai
```

## 🧰 Commands Reference

```bash
# Development
make help               # List available make targets
make clean              # Clean caches, artifacts and generated docs
make format             # Run all pre-commit hooks
make test               # Run pytest across the repository
make gen-docs           # Generate docs from src/ and scripts/

# Dependencies (via uv)
make uv-install         # Install uv on your system
uv add <pkg>            # Add production dependency
uv add <pkg> --dev      # Add development dependency
# Sync optional groups
uv sync --group dev     # Install dev-only deps (pre-commit, poe, notebook)
uv sync --group test    # Install test-only deps
uv sync --group docs    # Install docs-only deps
```

## 📚 Documentation

- Live docs are built with MkDocs Material.
- Generate API docs locally and serve:

```bash
uv sync --group docs
make gen-docs
uv run mkdocs serve    # http://localhost:9987
```

## 🐳 Docker and Local Services

`docker-compose.yaml` includes optional services for local development: `redis`, `postgresql`, `mongodb`, `mysql`.

Run services:

```bash
docker compose up -d redis postgresql

# Or run the app container
docker compose up -d app
```

## 🤝 Contributing

- Open issues/PRs
- Follow the coding style (ruff, type hints)
- Use Conventional Commit messages and descriptive PR titles

## 📄 License

MIT — see `LICENSE`.
