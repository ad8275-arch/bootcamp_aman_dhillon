# Jump-Diffusion Enhanced Black–Scholes Model for European Option Pricing  

## Project Scoping  

European options are fundamental instruments in global financial markets, but the standard **Black–Scholes (BS) model** assumes continuous asset price movements. In practice, markets often experience **sudden jumps** due to earnings announcements, geopolitical events, or policy changes. Ignoring these jumps leads to **systematic mispricing**, particularly for out-of-the-money options, which exposes traders and risk managers to hidden risks.  

Traditional jump-aware pricing methods, such as **Monte Carlo simulations with jump processes**, provide more realistic results but are often too computationally slow for real-time trading.  

This project aims to address this issue by implementing a **jump-diffusion extension** of the Black–Scholes model that:  
- Improves accuracy while maintaining computational efficiency  
- Allows traders and risk managers to better capture market realities without sacrificing speed  

### Stakeholders & Users  
- **Primary Stakeholder:** Derivatives Risk Manager  
  - Ensures that pricing models reflect true market risks  
  - Oversees internal model validation standards  
- **Primary Users:** Options traders & quantitative analysts  
  - Need fast, accurate pricing to make informed hedging and trading decisions  

### Expected Output  
The model’s answer will be **predictive**: it will forecast option prices under jump-diffusion dynamics.  

The final deliverable will be a **Python-based pricing tool** (script or Jupyter notebook) that:  
- Accepts standard market inputs:  
  - Stock price  
  - Strike price  
  - Volatility  
  - Risk-free interest rate  
  - Time to maturity  
- Accepts **jump parameters** (e.g., jump intensity, jump size distribution)  
- Returns **European option prices** that better reflect real-world market conditions  

