# Regression Model with Flask API

## Project Overview
This project demonstrates the full lifecycle of a simple machine learning regression model:
- **Data Generation**: Synthetic dataset created using `sklearn.datasets.make_regression`.
- **Model Training**: Linear regression model trained on the dataset.
- **Persistence**: Model saved with both `joblib` and `pickle` for reproducibility.
- **API Service**: Flask REST API providing prediction endpoints.
- **Visualization**: Sample plot endpoint returning a simple matplotlib chart.

The goal is to illustrate:
1. How to build and persist a model.
2. How to serve predictions via REST API.
3. How to evaluate and monitor model outputs.

---

## Objectives
- Build an end-to-end pipeline: **data → model → API → visualization**.
- Provide reproducibility (model saving & reloading).
- Offer both developer and stakeholder-friendly outputs.
- Enable easy API testing and dashboard extension.

---

##  Setup Instructions

### 1. Clone Repository
```bash
git clone <https://github.com/ad8275-arch/bootcamp_aman_dhillon/tree/main>
cd <bootcamp_aman_dhillon/homework/homework13>
