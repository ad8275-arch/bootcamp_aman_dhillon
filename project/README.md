
# Stage: Problem Framing & Scoping (Stage 01)
**Date:** August 18, 2025  

---

## Problem Statement

While theoretical models like **Black-Scholes** provide a baseline for option pricing, they often fail to capture the complex, non-linear dynamics observed in real-world markets. Factors like market microstructure, order flow, and behavioral biases create pricing patterns that these models miss.

**Problem:**  
Relying solely on theoretical models can lead to systematic mispricing and missed trading opportunities. Traders and risk managers need a pricing tool that learns directly from market data to generate more accurate, empirical valuations.

**Solution:**  
This project develops a **machine learning pipeline** to predict option prices using a rich set of engineered features. By training models like **Gradient Boosting** and **Recurrent Neural Networks (GRU)**, we can capture intricate market patterns that theoretical formulas cannot. The result will be a more accurate pricing model for improved trade execution, risk assessment, and alpha generation.

---

## Stakeholders & Users

- **Decision Maker — Head of Quantitative Trading**  
  Needs to approve and deploy models that are demonstrably more accurate than existing benchmarks and are robust to changing market conditions.

- **Primary Users — Options Traders & Quant Analysts**  
  Require fast and precise price predictions to identify arbitrage opportunities, manage risk, and execute trades efficiently, especially in volatile markets.

---

## Useful Answer & Decision

**Type:** Predictive — the models forecast option market prices based on historical data.

**Metrics:**
- **Accuracy** → Significant reduction in RMSE and MAE compared to a baseline model.  
- **Robustness** → Stable performance across various market conditions and out-of-sample data.  
- **Speed** → Model inference must be fast enough for practical use on the trading desk.  

**Final Artifact:**  
A trained ML model (e.g., the final GRU or LSTM model) serialized for use, and a comprehensive analysis notebook that validates its performance and explains the key feature drivers.

---

## Assumptions & Constraints

### Assumptions
- The historical options data (`syp_2020_2022.csv`) is a reliable representation of the market dynamics we want to model.  
- The engineered features (e.g., *moneyness*, time to expiration, Greeks) effectively capture the key drivers of option prices.  
- Market patterns learned from the training data will persist in the near future (i.e., the model is not overfit).  

### Constraints
- The model's predictions must be easily interpretable, or its feature importance must be explainable to pass internal model risk governance.  
- The final solution must be reproducible; all data processing and modeling steps are contained within the project's code.  

---

## Risks & Known Unknowns

- **Overfitting Risk** → The complex models (GRU, LSTM) might memorize the training data and perform poorly on unseen market data.  
- **Concept Drift Risk** → A fundamental shift in market regime (e.g., a sudden volatility spike) could invalidate the learned patterns, requiring the model to be retrained.  
- **Data Quality Risk** → Errors or gaps in the historical data could lead to a poorly performing model.  

---

## Lifecycle Mapping

| Project Goal                        | Stage                          | Deliverable                                  |
|-------------------------------------|--------------------------------|----------------------------------------------|
| 1. Scope the ML pricing project     | Problem Framing & Scoping      | This scoping document + repo skeleton        |
| 2. Develop and train ML models      | EDA, Feature Eng, & Modeling   | `practice_notebook2.ipynb`                   |
| 3. Deliver a robust pricing tool    | Productization & Deployment    | A modularized script/API for the best model  |


---

##  Repository Plan
/data/ → Market & simulated option data (raw + processed)
/src/ → Implementation of Black–Scholes, LSTM and GRU, API code
/notebooks/ → Exploratory analysis, calibration experiments, validation
/docs/ → Stakeholder memo, validation reports, explainability notes



---

##  Expected Output
The final Python-based pricing tool will:  
- Accept standard market inputs: stock price, strike price, volatility, risk-free rate, maturity, etc.
- Return empirically derived option prices based on the trained ML model.
- Support side-by-side comparison: e.g., predictions from the GRU model vs. the Gradient Boosting model. 
