SPY Option Price Prediction using GRU, LSTM and BS model

This repository contains a Jupyter Notebook for a machine learning project focused on financial options data analysis and price prediction. The project uses historical S&P 500 (SPY) options data to preprocess, explore, and build a predictive model. The primary goal is to use a Gated Recurrent Unit (GRU) neural network to forecast option prices.

📚 Features
Data Loading & Preprocessing: Reads and cleans a large financial options dataset.

Memory Optimization: Uses custom utility functions to optimize the memory usage of the DataFrame, making it efficient for analysis.

Exploratory Data Analysis (EDA): Visualizes key relationships in the data using libraries like plotly and matplotlib.

Model Training: Trains a GRU,LSTM and BS model to predict option prices based on various financial features.

Performance Evaluation: Plots training and validation loss (e.g., RMSE) and compares predicted prices against actual prices to evaluate model performance.

⚙️ Prerequisites
To run this notebook, you need to have Python installed along with the following libraries. You can install them using pip:

pip install numpy pandas matplotlib seaborn plotly scikit-learn tensorflow
Also the requirements are present in the requirement.txt
Note: The notebook also relies on a local src/utils.py file, which contains custom functions for data processing. This file must be present in a directory one level up from the notebook.

🚀 Usage
Clone the repository:

git clone [https://github.com/ad8275-arch]
cd [bootcamp_aman_dhillon]

Download the Data:
This repository does not include the raw data due to its large size. You will need to download the SPY_options_2020-2022.csv file from its source and place it in a data/ directory.

Ensure File Structure: Your project directory should look like this after you download the data and have the utils.py file:

.
├── data/
│   └── SPY_options_2020-2022.csv
├── src/
│   └── utils.py
└── notebooks/
    └── practice_notebook2.ipynb

Run the Notebook: Open the practice_notebook2.ipynb file in a Jupyter environment (e.g., JupyterLab, VS Code, Google Colab) and run all the cells in sequence.