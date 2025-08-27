# Assumptions, Constraints, and Risks  

---

## Assumptions
- **Market Data Availability**: Historical option and jump event data are sufficient for parameter calibration.  
- **Computational Feasibility**: Jump-Diffusion adds realism without causing unacceptable runtime overhead.  
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
