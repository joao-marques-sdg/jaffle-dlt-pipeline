# Jaffle Shop dlt Pipeline

This repository contains a fully automated dlt pipeline that extracts data
from the Jaffle Shop public API and loads it into DuckDB.

## 🚀 Features
- dlt pipeline with REST API extraction
- Automatic pagination
- Parallel extraction enabled
- GitHub Actions CI/CD deployment
- Manual and scheduled runs
- Reproducible environment

## Run locally

```bash
pip install -r requirements.txt
python pipeline.py
