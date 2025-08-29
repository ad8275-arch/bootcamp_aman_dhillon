
# Stage: Problem Framing & Scoping (Stage 01)
**Date:** August 18, 2025  

---

## Problem Statement

While theoretical models like **Black-Scholes** provide a baseline for option pricing, they often fail to capture the complex, non-linear dynamics observed in real-world markets. Factors like market microstructure, order flow, and behavioral biases create pricing patterns that these models miss.

**Problem:**  
Relying solely on theoretical models can lead to systematic mispricing and missed trading opportunities. Traders and risk managers need a pricing tool that learns directly from market data to generate more accurate, empirical valuations.

**Solution:**  
This project develops a **machine learning pipeline** to predict option prices using a rich set of engineered features. By training models like **LSTM** and **Recurrent Neural Networks (GRU)**, we can capture intricate market patterns that theoretical formulas cannot. The result will be a more accurate pricing model for improved market pricing of options.

---

## Stakeholders & Users

- **Decision Maker — Head of Quantitative Trading**  
  Needs to approve and deploy models that are demonstrably more accurate than existing benchmarks and are robust to changing market conditions.

- **Primary Users — Options Traders & Quant Analysts**  
  Require fast and precise price predictions to identify arbitrage opportunities, manage risk, and execute trades efficiently, especially in volatile markets.

---

# Assumptions, Constraints, and Risks  

---

## Assumptions
- **Market Data Availability**: Historical option and jump event data are sufficient for parameter calibration.  
- **Computational Feasibility**: ML adds realism without causing unacceptable runtime overhead.  
- **Model Applicability**: European-style options remain the scope; American options are out of scope for this project.  

---

## Constraints
- **Governance**: The model must be interpretable enough to pass internal model risk controls.  
- **Integration**: Deployment should fit seamlessly into the existing trading infrastructure.  
- **Scope**: Focused only on European vanilla options (calls & puts), not exotic derivatives.  

---

## Risks
- **Calibration Risk**: Parameter estimation for jumps may be unstable due to sparse jump data.  
- **Model Risk**: Overfitting to rare events could harm out-of-sample performance.  
- **Adoption Risk**: Traders may initially distrust a new model compared to the established BS framework.  

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
/src/ → Implementation of helper functions code
/notebooks/ → Exploratory analysis, calibration experiments, validation
/docs/ → Stakeholder memo



---

##  Expected Output
The final Python-based pricing tool will:  
- Accept standard market inputs: stock price, strike price, volatility, risk-free rate, maturity, etc.
- Return empirically derived option prices based on the trained ML model.
- Support side-by-side comparison: e.g., predictions from the GRU model and LSTM model vs. the BS model. 
