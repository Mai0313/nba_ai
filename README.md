<div align="center" markdown="1">

# NBA AI

[![PyPI version](https://img.shields.io/pypi/v/nba-ai.svg)](https://pypi.org/project/nba-ai/)
[![python](https://img.shields.io/badge/-Python_%7C_3.11%7C_3.12%7C_3.13%7C_3.14-blue?logo=python&logoColor=white)](https://www.python.org/downloads/source/)
[![uv](https://img.shields.io/badge/-uv_dependency_management-2C5F2D?logo=python&logoColor=white)](https://docs.astral.sh/uv/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://docs.pydantic.dev/latest/contributing/#badges)
[![tests](https://github.com/Mai0313/nba_ai/actions/workflows/test.yml/badge.svg)](https://github.com/Mai0313/nba_ai/actions/workflows/test.yml)
[![code-quality](https://github.com/Mai0313/nba_ai/actions/workflows/code-quality-check.yml/badge.svg)](https://github.com/Mai0313/nba_ai/actions/workflows/code-quality-check.yml)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/Mai0313/nba_ai)
[![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)](https://github.com/Mai0313/nba_ai/tree/main?tab=License-1-ov-file)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Mai0313/nba_ai/pulls)
[![contributors](https://img.shields.io/github/contributors/Mai0313/nba_ai.svg)](https://github.com/Mai0313/nba_ai/graphs/contributors)

</div>

🏀 **NBA AI** is an intelligent NBA data analysis and prediction system that combines data collection, machine learning, and LLM-powered insights.

## 🎯 Project Overview

This project consists of two main phases:

### Phase 1: Data Collection & Archiving (Current Focus)

Leverage the `nba_api` library to systematically download and store NBA data from NBA.com in a structured format:

- **Game Scores**: Historical and real-time game results with box scores
- **Player Statistics**: Per-game performance data for all players (points, rebounds, assists, shooting percentages, etc.)
- **Player Availability**: Injury reports, playing time, rotation patterns, and roster status
- **Team Statistics**: Team performance metrics, standings, and head-to-head records
- **Advanced Metrics**: Usage rates, efficiency ratings, plus/minus, and other advanced stats

**Data Source**: All data is collected via the `nba_api` Python library, which provides comprehensive access to NBA.com's stats endpoints.

### Phase 2: AI-Powered Prediction (Future)

#### Predictive Modeling

- Train machine learning models using historical structured data
- Predict game outcomes, player performance, and team statistics
- Continuous model improvement with new data

#### LLM-Based News Analysis (Planned)

- Integrate news and media reports as additional input
- Use LLMs to extract sentiment and contextual factors
- Generate weighted predictions combining statistical models and news analysis
- Create comprehensive game previews and player insights

## ✨ Features

### Current Implementation

- **NBA API Integration**: Utilize `nba_api` library for reliable data access from NBA.com
- **Automated Data Collection**: Scheduled tasks to fetch daily game results, player stats, and team data
- **Structured Storage**: Well-organized data schema (SQLite/PostgreSQL) for efficient querying and analysis
- **Data Validation**: Comprehensive data quality checks and deduplication
- **Modern Development**: Built with `uv`, `ruff`, `mypy`, and `pytest`

### Planned Features

- **ML Models**: Statistical prediction models trained on historical data
- **LLM Integration**: News analysis and contextual prediction weighting
- **API Endpoints**: RESTful API for accessing predictions and historical data
- **Visualization Dashboard**: Interactive charts and prediction displays
- **Real-time Updates**: Live game tracking and prediction adjustments

## 🗂️ Project Structure

```
nba_ai/
├── src/nba_ai/
│   ├── data_collection/  # NBA API data fetching modules
│   │   ├── games.py     # Game scores and box scores
│   │   ├── players.py   # Player stats and profiles
│   │   └── teams.py     # Team stats and standings
│   ├── models/           # Data models and Pydantic schemas
│   ├── storage/          # Database handlers (SQLite/PostgreSQL)
│   ├── ml/              # (Future) Machine learning models
│   ├── llm/             # (Future) LLM integration for news analysis
│   └── api/             # (Future) FastAPI endpoints
├── data/                # Local data storage
│   ├── raw/            # Raw JSON responses from nba_api
│   ├── processed/      # Cleaned and structured data
│   └── models/         # Trained model artifacts
├── notebooks/          # Jupyter notebooks for analysis
└── tests/              # Test suite
```

## 🎯 Development Roadmap

### Phase 1: Data Infrastructure (Q1 2026)

- [ ] Set up `nba_api` integration and test endpoints
- [ ] Design database schema for player stats, games, and teams
- [ ] Implement data collectors for:
    - [ ] Game scores and box scores
    - [ ] Player per-game statistics
    - [ ] Player availability and injury reports
    - [ ] Team standings and statistics
- [ ] Build ETL pipeline for daily data updates
- [ ] Create data validation and quality checks
- [ ] Set up automated data archiving and backup

### Phase 2: Exploratory Analysis (Q2 2026)

- [ ] Analyze historical data patterns
- [ ] Identify key predictive features
- [ ] Build baseline statistical models
- [ ] Evaluate model performance metrics

### Phase 3: ML Model Development (Q3 2026)

- [ ] Train regression models for score prediction
- [ ] Build classification models for win/loss prediction
- [ ] Implement player performance models
- [ ] Create ensemble methods for improved accuracy

### Phase 4: LLM Integration (Q4 2026 - Future)

- [ ] Collect and preprocess news data
- [ ] Design LLM prompts for news analysis
- [ ] Implement weighted prediction system
- [ ] Evaluate combined model performance
- [ ] Build API and frontend dashboard

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- `uv` package manager ([installation guide](https://docs.astral.sh/uv/))

### Installation

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/Mai0313/nba_ai.git
cd nba_ai

# Install dependencies
uv sync

# Install nba_api
uv add nba_api
```

### Basic Usage

```bash
# Run the CLI
uv run nba_ai

# Run tests
make test
```

## 💾 Data Storage

Collected data will be stored in the `data/` directory:

- `data/raw/` - Raw JSON responses from nba_api
- `data/processed/` - Cleaned and structured data
- Database: SQLite (default) or PostgreSQL for production

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT — see [LICENSE](LICENSE).
