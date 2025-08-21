# Stakeholder Memo  
**Project:** Jump-Diffusion Enhanced Black–Scholes Model for European Option Pricing  
**Date:** August 18, 2025  
**Prepared For:** Risk Management Lead, Options Trading Desk  

---

## 📌 Executive Summary
The Black–Scholes (BS) model is the industry standard for pricing European options, but it assumes continuous price paths. In real-world markets, sudden jumps occur due to earnings releases, policy changes, and global events. These shocks are ignored in the BS model, leading to systematic mispricing and hidden risks.

Our project addresses this gap by developing a **Jump-Diffusion Enhanced BS model**, which incorporates both continuous dynamics and discrete jump processes. This approach preserves computational efficiency while improving realism and risk alignment.

---

## 🎯 Why This Matters
- **Risk Management** → Captures jump risk that traditional models overlook  
- **Trading Performance** → Improves accuracy in option pricing, especially out-of-the-money  
- **Compliance** → Transparent and interpretable enough to meet internal model governance  

---

## 📊 Deliverables
- A **baseline Black–Scholes implementation** (for reference and benchmarking)  
- An **extended jump-diffusion model** with calibration tools  
- A **Python pricing engine** (script or API) for real-time desk use  
- **Validation report** comparing BS vs. Jump-Diffusion pricing under stress scenarios  

---

## ✅ Next Steps
- Finalize baseline Black–Scholes implementation  
- Begin extending with jump-diffusion dynamics  
- Share calibration experiments with historical market data  

---

**Prepared by:** [Your Name]  
Quantitative Research Team  
