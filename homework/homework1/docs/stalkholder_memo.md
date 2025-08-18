Project: Jump-Diffusion Enhanced BS model on European Option Pricing

Stage: Problem Framing & Scoping (Stage 01)
Date: August 18, 2025

Problem Statement :
Traditional Black–Scholes models are widely used for European option pricing, but they assume continuous price movements. In real markets, asset prices often experience sudden jumps due to news shocks, policy changes, or earnings announcements. Ignoring these jumps leads to systematic mispricing, especially for out-of-the-money options, which in turn exposes traders and risk managers to unrecognized risks.
This project will extend Black–Scholes with a jump diffusion model to provide more realistic pricing while keeping computational efficiency. The result will improve risk assessment, hedging strategies, and execution quality for options traders.

Stakeholder & User :
Decision Maker: The Risk Management Lead, responsible for ensuring that pricing models meet compliance and accurately reflect market risk.
Primary User: Options Traders and Quant Analysts, who need fast and accurate option values for hedging, risk monitoring, and trade execution in volatile markets.

Useful Answer & Decision :
Type: Predictive — the model forecasts option values under jump risk.
Metrics:
Accuracy: Error reduction compared to Black–Scholes baseline.
Robustness: Performance across stressed/jump-heavy scenarios.
Speed: Must run within sub-second latency for trading desk use.
Artifact: A Python-based pricing engine with a callable API, supporting scenario analyses for both traders and risk managers.

Assumptions & Constraints
Assumption: Sufficient market data is available for calibration of jump intensity and distribution.
Assumption: The jump diffusion framework improves pricing realism without excessive computational overhead.
Constraint: The model must be transparent and interpretable enough to pass internal model risk governance.
Constraint: Integration must fit existing trading system architecture with minimal disruption.

Known Unknowns / Risks
Calibration Risk: Limited historical data on extreme jumps may make parameter estimation unstable.
Model Risk: Jump diffusion may overfit to rare events, reducing generalizability.
Adoption Risk: Traders may initially distrust the new model compared to the familiar Black–Scholes framework.

Lifecycle Mapping
| Goal                                        | Stage                     | Deliverable                         |
| ------------------------------------------- | ------------------------- | ----------------------------------- |
| 1. Establish baseline Black–Scholes pricing | Problem Framing & Scoping | Scoping doc + repo skeleton         |
| 2. Extend with jump diffusion               | Model Development         | Trained model & validation notebook |
| 3. Deliver production-ready tool            | Deployment                | Python API + usage documentation    |



Repo Plan
/data/: Market and simulated option data for calibration and testing.
/src/: Implementation of Black–Scholes, jump diffusion, and API code.
/notebooks/: Exploratory analysis, calibration experiments, and validation.
/docs/: Stakeholder memo, validation reports, and explainability notes.