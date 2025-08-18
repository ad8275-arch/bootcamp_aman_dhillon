Project: Jump-Diffusion Enhanced BS Model on European Option Pricing
This project aims to improve option pricing accuracy by extending the Black–Scholes model with a jump diffusion process, capturing sudden market shocks while maintaining computational efficiency.

Project Scope
European options are among the most widely traded derivatives, but the standard Black–Scholes model assumes continuous price paths. In reality, asset prices often exhibit jumps due to earnings announcements, macroeconomic shocks, or policy changes. Ignoring these jumps leads to systematic mispricing, particularly for out-of-the-money options, and exposes traders and risk managers to hidden risks.
Traditional extensions like Monte Carlo with jump processes are often too slow for real-time use. This project addresses the challenge by implementing a jump diffusion model that balances pricing realism with computational efficiency.
The primary stakeholder is a derivatives risk manager responsible for ensuring pricing models align with true market risks. The primary users are options traders and quants on the trading desk, who require accurate, fast pricing for hedging, execution, and risk monitoring. The useful answer is predictive: pricing options under jump risk. The final output will be a Python-based pricing engine, callable via an API or notebook, that computes European option prices under both standard Black–Scholes and jump diffusion dynamics.

Goals → Lifecycle → Deliverables
| Project Goal                                                 | Lifecycle Stage                | Key Deliverable(s)                                                                                                                  |
| ------------------------------------------------------------ | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| 1. Establish a baseline with Black–Scholes pricing.          | Problem Framing & Scoping      | A script (/src/black\_scholes.py) that computes prices and Greeks using the traditional Black–Scholes model.                        |
| 2. Extend the model with jump diffusion.                     | Model Development              | A Jupyter Notebook (/notebooks/jump\_diffusion.ipynb) implementing Merton’s jump diffusion, with calibration experiments.           |
| 3. Validate performance and compare models.                  | Model Evaluation               | A report (/docs/model\_validation.md) summarizing accuracy, robustness in jump scenarios, and runtime performance.                  |
| 4. Deliver a usable pricing tool for traders and risk teams. | Deployment & Artifact Creation | A final script (/src/pricer\_tool.py) or Python API providing callable functions for both Black–Scholes and jump diffusion pricing. |
