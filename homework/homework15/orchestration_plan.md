# Orchestration Plan for SPY Option Price Prediction

## Pipeline Overview: Directed Acyclic Graph (DAG)
The project's workflow can be represented as a Directed Acyclic Graph (DAG), showing the logical flow and dependencies of each task.

![Pipeline DAG Sketch](https://placehold.co/600x400/000/fff?text=Pipeline+DAG+Sketch)

1. **Ingest Data** – Retrieves the raw data.  
2. **Clean Data & Feature Engineering** – Cleans and engineers new features. Depends on *Ingest Data*.  
3. **Train Model** – Trains the GRU model. Depends on *Clean Data & Feature Engineering*.  
4. **Model Evaluation** – Evaluates the trained model. Depends on *Train Model*.  
5. **Report Generation** – Generates the final report. Depends on *Model Evaluation*.  

---

## Task Breakdown

| Task | Inputs | Outputs | Idempotency | Logging & Checkpoint Strategy |
|------|--------|---------|-------------|--------------------------------|
| **1. Ingest Data** | Raw data file (`SPY_options_2020-2022.csv`) | Raw data saved to staging area (`staging/raw_data.parquet`) | Yes (static input, deterministic output) | **Log:** INFO when file is found, ERROR if not found.<br>**Checkpoint:** Save as Parquet for fast future reads. |
| **2. Clean Data & Feature Engineering** | `staging/raw_data.parquet` | Processed data (`processed/clean_data.parquet`) | Yes (deterministic cleaning logic) | **Log:** INFO for each cleaning step (e.g., "Memory optimization complete").<br>**Checkpoint:** Save cleaned DataFrame to disk. |
| **3. Train Model** | `processed/clean_data.parquet` | Trained GRU model (`models/gru_model.h5`) | No (random weight initialization & shuffling) | **Log:** INFO on epoch completion, training loss, validation loss.<br>**Checkpoint:** Save trained model in `models/`. |
| **4. Model Evaluation** | Trained model (`models/gru_model.h5`), Processed data (`processed/clean_data.parquet`) | Evaluation metrics & plots (`metrics/evaluation.json`, `plots/rmse.png`) | Yes (given same model & data) | **Log:** INFO with RMSE, MAE, and other metrics.<br>**Checkpoint:** Store metrics and plots in `metrics/` and `plots/`. |
| **5. Report Generation** | Evaluation metrics, plots | Final report (`report.md`) | Yes (static inputs) | **Log:** INFO on successful report generation. |

---

## Failure Points and Retry Policy

- **Failure Point:** Ingest Data – first critical step. Failure occurs if the raw file is missing or corrupted.  
- **Retry Policy:** Retry up to 3 times with exponential backoff (1s → 2s → 4s).  
  - If failure persists after 3 attempts → job fails and alerts a team member.  

---

## Automation Strategy

- **Automate Now**  
  - Refactor **Clean Data & Feature Engineering** into a standalone script.  
  - Add a **CLI wrapper** for easy execution from terminal.  
  - Enables future integration into automated jobs.  

- **Keep Manual**  
  - Full pipeline orchestration (overkill for current project).  
  - Model training & evaluation (requires human oversight).  
  - Final report review (manual interpretation before decisions).  

---

## Summary

This plan balances **good software engineering practices** (modularity, logging, checkpoints) with **project constraints** (one-off analysis, small team). The most critical step to automate now is **data cleaning & feature engineering**, while training and reporting remain **manual** for oversight.

