# Applied Financial Engineering — Framework Guide  

---

## Framework Guide Table  

| Lifecycle Stage | What You Did | Challenges | Solutions / Decisions | Future Improvements |
|-----------------|--------------|------------|-----------------------|---------------------|
| **1. Problem Framing & Scoping** | Defined the gap between Black–Scholes and real SPY option pricing in volatile markets. Goal: compare BS vs. ML (LSTM, GRU) for pricing accuracy. | Balancing mathematical rigor with ML flexibility; unclear stakeholder expectations. | Scoped to “benchmark BS vs. ML under different volatility regimes” with RMSE as main metric. 
| **2. Tooling Setup** | Configured Python env with TensorFlow, scikit-learn, pandas, matplotlib. Set up `src/utils.py` for custom helpers. | Dependency mismatches (TensorFlow, CUDA) and path issues with local modules. | Standardized environment via `requirements.txt` and ensured relative paths. | Containerize with Docker for reproducibility. |
| **3. Python Fundamentals** | Used core Python (loops, functions, OOP) and pandas/numpy for transformations. | Some gaps in clean code practices and error handling. | Adopted modular design (`utils.py`) and frequent testing in notebooks. | Improve fluency in vectorization and unit testing. |
| **4. Data Acquisition / Ingestion** | Loaded SPY options data (CSV) and ensured datetime parsing, quote times, strikes, and IV. | Missing records, misaligned timestamps. | Used pandas parsing with explicit dtypes and merged with market calendar. | Automate ingestion via API (e.g., CBOE, Polygon.io) for real-time data. |
| **5. Data Storage** | Stored intermediate datasets as CSV/parquet for reproducibility. | CSV reload caused type drift (dates reloaded as strings). | Standardized schema and used parquet for efficiency. | Move to SQLite/duckdb for better querying. |
| **6. Data Preprocessing** | Cleaned NaNs (forward/backward fill), normalized prices, engineered time-to-expiry. | Deciding when missing IV was meaningful vs. noise. | Used forward/backward fill for short gaps, dropped rows when gaps > threshold. | Add domain-aware imputation (e.g., implied vol surface smoothing). |
| **7. Outlier Analysis** | Detected abnormal IV spikes and unrealistic option prices. | Differentiating true volatility events from bad ticks. | Flagged outliers with z-score thresholds and cross-checked with VIX. | Use robust stats (MAD, quantile filters) + visualize via Missingno. |
| **8. Exploratory Data Analysis (EDA)** | Visualized IV term structures, moneyness buckets, histograms of option premiums. | IV skew interpretation was tricky at first. | Used heatmaps and maturity-by-strike plots to clarify patterns. | Add joint distribution plots (Δ vs Γ vs IV). |
| **9. Feature Engineering** | Constructed features: moneyness, time-to-expiry, IV, underlying returns, rolling vol. | Choosing features without overfitting. | Validated through feature importance and correlation checks. | Add Greeks (Δ, Γ, Vega) as engineered features. |
| **10. Modeling (Regression / Time Series / Classification)** | Trained BS baseline, GRU, LSTM on historical SPY options. | ML models risked overfitting; training was slow. | Used train/validation/test split, early stopping, tuned hyperparams. | Explore transformers or hybrid BS+NN models. |
| **11. Evaluation & Risk Communication** | Evaluated RMSE, MAPE, directional accuracy vs. BS. | Communicating error magnitude in financial terms. | Framed errors as potential mispricing → PnL risk. | Backtest hedging strategies with predicted vs. BS price. |
| **12. Results Reporting, Delivery Design & Stakeholder Communication** | Shared results via notebook, README, and stakeholder memo (executive summary). | Translating “RMSE” into risk terms for non-tech audience. | Framed results as “reduced mispricing during high vol regimes.” | Build dashboards with Plotly/Streamlit for live demos. |
| **13. Productization** | Packaged models into `model/` folder, structured repo with utils + requirements. | Keeping pipeline reproducible. | Joblib for model persistence; modular functions for preprocessing. | Wrap preprocessing + inference in a proper Python package. |
| **14. Deployment & Monitoring** | Local notebook deployment; designed API endpoint for predictions. | No real monitoring yet. | Planned API via FastAPI/Flask, logging predictions. | Add drift detection + auto-retraining pipeline. |
| **15. Orchestration & System Design** | Structured project folders, pipelines (ingest → clean → model → eval). | Path/dependency management. | Simple orchestration via scripts and notebooks. | Move to Airflow/Prefect for automated DAGs. |
| **16. Lifecycle Review & Reflection** | Biggest takeaway: BS is elegant but brittle in practice; ML adapts better under regime shifts. | Struggled most with preprocessing/missing data decisions. | Iterative design + modular repo structure helped a lot. 

---

## Reflection Prompts  

- **Most difficult stage:** Data preprocessing, especially deciding how to handle missing IV values and distinguishing bad data from real signals.  
- **Most rewarding stage:** Modeling, when GRU/LSTM showed clear improvement over BS during volatility spikes.  
- **Connection across stages:** Early preprocessing choices (e.g., imputation) directly constrained model performance later. Bad type drift in storage also risked misinterpretation downstream.  
- **What I’d do differently:** Automate ingestion + cleaning earlier, to reduce friction in iteration.  
- **Skills to strengthen:** MLOps, deployment, and feature engineering with domain-driven Greeks.  
