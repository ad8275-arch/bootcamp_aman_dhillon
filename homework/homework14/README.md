# SPY Option Price Prediction using GRU, LSTM, and BS Model

This repository contains a Jupyter Notebook for a machine learning project focused on financial options data analysis and price prediction. The project uses historical S&P 500 (SPY) options data to preprocess, explore, and build predictive models. The primary goal is to use a **Gated Recurrent Unit (GRU)** neural network to forecast option prices. Additional models include **LSTM** and **Black-Scholes (BS)** for comparison.

---

## Features

- **Data Loading & Preprocessing**: Reads and cleans a large financial options dataset.
- **Memory Optimization**: Uses custom utility functions to reduce memory usage for efficient analysis.
- **Exploratory Data Analysis (EDA)**: Visualizes key relationships in the data using libraries like Plotly and Matplotlib.
- **Model Training**: Trains GRU, LSTM, and BS models to predict option prices based on various financial features.
- **Performance Evaluation**: Plots training and validation loss (e.g., RMSE) and compares predicted prices against actual prices to evaluate model performance.

---

## Prerequisites


pip install numpy pandas matplotlib seaborn plotly scikit-learn tensorflow
All required dependencies are also listed in requirements.txt.

The notebook relies on a local src/utils.py file, which contains custom functions for data processing. This file must be present in a directory one level up from the notebook.

## Usage
1. Clone the Repository
git clone https://github.com/ad8275-arch
cd bootcamp_aman_dhillon

2. Download the Data

Download the SPY_options_2020-2022.csv file from its source and place it in a data/ directory.

3. Ensure File Structure
.
├── data/
│   └── SPY_options_2020-2022.csv
├── src/
│   └── utils.py
└── notebooks/
    └── practice_notebook2.ipynb

4. Run the Notebook

Open practice_notebook2.ipynb in a Jupyter environment (e.g., JupyterLab, VS Code, Google Colab) and run all cells in sequence.

## Notes

Ensure all dependencies are installed and paths are correctly set.

Use the utils.py functions for memory optimization and feature engineering to maintain consistency.

For model performance comparison, check the plots and evaluation metrics at the end of the notebook.

Author
Aman Dhillon