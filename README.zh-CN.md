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

🏀 **NBA AI** 是一个智能 NBA 数据分析和预测系统，结合数据收集、机器学习和 LLM 驱动的洞察。

其他语言: [English](README.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh-CN.md)

## 🎯 项目概述

本项目由两个主要阶段组成：

### 第一阶段：数据收集与归档（当前重点）

利用 `nba_api` 库从 NBA.com 系统化地下载并存储结构化的 NBA 数据：

- **比赛分数**：历史和实时比赛结果及详细数据统计
- **球员统计**：所有球员的单场表现数据（得分、篮板、助攻、投篮命中率等）
- **球员出场情况**：伤病报告、上场时间、轮换模式和阵容状态
- **球队统计**：球队表现指标、排名和对战记录
- **高级指标**：使用率、效率评分、正负值等高级统计数据

**数据来源**：所有数据通过 `nba_api` Python 库收集，该库提供了对 NBA.com 统计端点的全面访问。

### 第二阶段：AI 驱动预测（未来）

#### 预测建模

- 使用历史结构化数据训练机器学习模型
- 预测比赛结果、球员表现和球队统计
- 通过新数据持续改进模型

#### 基于 LLM 的新闻分析（规划中）

- 整合新闻和媒体报道作为额外输入
- 使用 LLM 提取情感和上下文因素
- 生成结合统计模型和新闻分析的加权预测
- 创建全面的比赛预览和球员洞察

## ✨ 功能特色

### 当前实现

- **NBA API 集成**：利用 `nba_api` 库从 NBA.com 可靠地获取数据
- **自动数据收集**：定时任务获取每日比赛结果、球员统计和球队数据
- **数据验证**：全面的数据质量检查和去重
- **现代化开发**：使用 `uv`、`ruff`、`mypy` 和 `pytest` 构建

### 计划功能

- **机器学习模型**：基于历史数据训练的统计预测模型
- **LLM 集成**：新闻分析和上下文预测加权
- **API 端点**：用于访问预测和历史数据的 RESTful API
- **可视化仪表板**：交互式图表和预测显示
- **实时更新**：实时比赛跟踪和预测调整

## 🗂️ 项目结构

```
nba_ai/
├── src/nba_ai/
│   ├── data_collection/  # NBA API 数据获取模块
│   │   ├── games.py     # 比赛分数和详细统计
│   │   ├── players.py   # 球员统计和资料
│   │   └── teams.py     # 球队统计和排名
│   ├── models/           # 数据模型和 Pydantic 模式

│   ├── ml/              # （未来）机器学习模型
│   ├── llm/             # （未来）新闻分析的 LLM 集成
│   └── api/             # （未来）FastAPI 端点
├── data/                # 本地数据存储
│   ├── raw/            # nba_api 的原始 JSON 响应
│   ├── processed/      # 清洗和结构化数据
│   └── models/         # 训练好的模型文件
├── notebooks/          # 用于分析的 Jupyter notebooks
└── tests/              # 测试套件
```

## 🎯 开发路线图

### 第一阶段：数据基础设施（2026年第1季度）

- [ ] 设置 `nba_api` 集成并测试端点
- [ ] 实现数据收集器：
    - [ ] 比赛分数和详细统计
    - [ ] 球员单场统计数据
    - [ ] 球员出场情况和伤病报告
    - [ ] 球队排名和统计
- [ ] 构建每日数据更新的 ETL 管道
- [ ] 创建数据验证和质量检查
- [ ] 设置自动数据归档和备份

### 第二阶段：探索性分析（2026年第2季度）

- [ ] 分析历史数据模式
- [ ] 识别关键预测特征
- [ ] 构建基准统计模型
- [ ] 评估模型性能指标

### 第三阶段：机器学习模型开发（2026年第3季度）

- [ ] 训练分数预测的回归模型
- [ ] 构建胜负预测的分类模型
- [ ] 实现球员表现模型
- [ ] 创建集成方法以提高准确性

### 第四阶段：LLM 集成（2026年第4季度 - 未来）

- [ ] 收集和预处理新闻数据
- [ ] 设计用于新闻分析的 LLM 提示
- [ ] 实现加权预测系统
- [ ] 评估组合模型性能
- [ ] 构建 API 和前端仪表板

## 🚀 快速开始

### 环境需求

- Python 3.11 或更高版本
- `uv` 包管理器（[安装指南](https://docs.astral.sh/uv/)）

### 安装

```bash
# 安装 uv（如果尚未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 克隆仓库
git clone https://github.com/Mai0313/nba_ai.git
cd nba_ai

# 安装依赖
uv sync

# 安装 nba_api
uv add nba_api
```

### 基本使用

```bash
# 运行 CLI
uv run nba_ai

# 运行测试
make test
```

## 💾 数据存储

收集的数据将存储在 `data/` 目录中：

- `data/raw/` - nba_api 的原始 JSON 响应
- `data/processed/` - 清洗和结构化后的数据

## 🤝 贡献

欢迎贡献！请随时提交 Pull Request。

## 📄 授权

MIT — 详见 [LICENSE](LICENSE)
