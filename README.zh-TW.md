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

🏀 **NBA AI** 是一個智能 NBA 資料分析和預測系統，結合資料收集、機器學習和 LLM 驅動的洞察。

其他語言: [English](README.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh-CN.md)

## 🎯 專案概述

本專案由兩個主要階段組成：

### 第一階段：資料收集與歸檔（當前重點）

利用 `nba_api` 函式庫從 NBA.com 系統化地下載並儲存結構化的 NBA 資料：

- **比賽分數**：歷史和即時比賽結果及詳細數據統計
- **球員統計**：所有球員的單場表現資料（得分、籃板、助攻、投籃命中率等）
- **球員出場情況**：傷病報告、上場時間、輪換模式和陣容狀態
- **球隊統計**：球隊表現指標、排名和對戰紀錄
- **進階指標**：使用率、效率評分、正負值等進階統計資料

**資料來源**：所有資料透過 `nba_api` Python 函式庫收集，該函式庫提供了對 NBA.com 統計端點的全面存取。

### 第二階段：AI 驅動預測（未來）

#### 預測建模

- 使用歷史結構化資料訓練機器學習模型
- 預測比賽結果、球員表現和球隊統計
- 透過新資料持續改進模型

#### 基於 LLM 的新聞分析（規劃中）

- 整合新聞和媒體報導作為額外輸入
- 使用 LLM 提取情感和上下文因素
- 生成結合統計模型和新聞分析的加權預測
- 創建全面的比賽預覽和球員洞察

## ✨ 功能特色

### 當前實作

- **NBA API 整合**：利用 `nba_api` 函式庫從 NBA.com 可靠地取得資料
- **自動資料收集**：定時任務取得每日比賽結果、球員統計和球隊資料
- **結構化儲存**：組織良好的資料模式（SQLite/PostgreSQL），便於高效查詢和分析
- **資料驗證**：全面的資料品質檢查和去重
- **現代化開發**：使用 `uv`、`ruff`、`mypy` 和 `pytest` 建構

### 計畫功能

- **機器學習模型**：基於歷史資料訓練的統計預測模型
- **LLM 整合**：新聞分析和上下文預測加權
- **API 端點**：用於存取預測和歷史資料的 RESTful API
- **視覺化儀錶板**：互動式圖表和預測顯示
- **即時更新**：即時比賽追蹤和預測調整

## 🗂️ 專案結構

```
nba_ai/
├── src/nba_ai/
│   ├── data_collection/  # NBA API 資料取得模組
│   │   ├── games.py     # 比賽分數和詳細統計
│   │   ├── players.py   # 球員統計和資料
│   │   └── teams.py     # 球隊統計和排名
│   ├── models/           # 資料模型和 Pydantic 模式
│   ├── storage/          # 資料庫處理器（SQLite/PostgreSQL）
│   ├── ml/              # （未來）機器學習模型
│   ├── llm/             # （未來）新聞分析的 LLM 整合
│   └── api/             # （未來）FastAPI 端點
├── data/                # 本地資料儲存
│   ├── raw/            # nba_api 的原始 JSON 回應
│   ├── processed/      # 清洗和結構化資料
│   └── models/         # 訓練好的模型檔案
├── notebooks/          # 用於分析的 Jupyter notebooks
└── tests/              # 測試套件
```

## 🎯 開發路線圖

### 第一階段：資料基礎設施（2026年第1季度）

- [ ] 設定 `nba_api` 整合並測試端點
- [ ] 設計球員統計、比賽和球隊的資料庫模式
- [ ] 實作資料收集器：
    - [ ] 比賽分數和詳細統計
    - [ ] 球員單場統計資料
    - [ ] 球員出場情況和傷病報告
    - [ ] 球隊排名和統計
- [ ] 建構每日資料更新的 ETL 管道
- [ ] 創建資料驗證和品質檢查
- [ ] 設定自動資料歸檔和備份

### 第二階段：探索性分析（2026年第2季度）

- [ ] 分析歷史資料模式
- [ ] 識別關鍵預測特徵
- [ ] 建構基準統計模型
- [ ] 評估模型效能指標

### 第三階段：機器學習模型開發（2026年第3季度）

- [ ] 訓練分數預測的迴歸模型
- [ ] 建構勝負預測的分類模型
- [ ] 實作球員表現模型
- [ ] 創建集成方法以提高準確性

### 第四階段：LLM 整合（2026年第4季度 - 未來）

- [ ] 收集和預處理新聞資料
- [ ] 設計用於新聞分析的 LLM 提示
- [ ] 實作加權預測系統
- [ ] 評估組合模型效能
- [ ] 建構 API 和前端儀錶板

## 🚀 快速開始

### 環境需求

- Python 3.11 或更高版本
- `uv` 套件管理器（[安裝指南](https://docs.astral.sh/uv/)）

### 安裝

```bash
# 安裝 uv（如果尚未安裝）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 克隆倉庫
git clone https://github.com/Mai0313/nba_ai.git
cd nba_ai

# 安裝依賴
uv sync

# 安裝 nba_api
uv add nba_api
```

### 基本使用

```bash
# 執行 CLI
uv run nba_ai

# 執行測試
make test
```

## 💾 資料儲存

收集的資料將儲存在 `data/` 目錄中：

- `data/raw/` - nba_api 的原始 JSON 回應
- `data/processed/` - 清洗和結構化後的資料
- 資料庫：SQLite（預設）或 PostgreSQL（生產環境）

## 🤝 貢獻

歡迎貢獻！請隨時提交 Pull Request。

## 📄 授權

MIT — 詳見 [LICENSE](LICENSE)
