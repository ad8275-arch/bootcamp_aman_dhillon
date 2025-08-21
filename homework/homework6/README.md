# Data Preprocessing  

For Stage 6, we added a modular cleaning layer to prepare raw data before analysis.  

## Cleaning Functions (`src/cleaning.py`)  

- **fill_missing_median(df, required_columns)**  
  - Fills missing values in specified numeric columns with the column median.  
  - *Assumption:* median is more robust to outliers than mean.  

- **drop_missing(df, threshold=0.5)**  
  - Drops rows with too many missing values.  
  - A row is kept if it has at least `threshold * total_columns` non-null values.  

- **normalize_data(df, required_columns)**  
  - Scales selected columns to `[0, 1]` range using min–max normalization.  
  - *Assumption:* normalization is appropriate for continuous numeric columns.  

## Workflow  

- Load raw dataset from `data/raw/`  
- Apply cleaning functions in sequence  
- Save cleaned dataset to `data/processed/`  
- Compare original vs cleaned data in the notebook to document tradeoffs  

## Assumptions  

- Missing values in key numeric columns are filled with the **median**, not mean  
- Rows with more than 50% missing values are dropped  
- Only continuous numeric columns are normalized — categorical data is left unchanged  

## Deliverables  

- `src/cleaning.py` with reusable functions  
- Jupyter notebook demonstrating preprocessing  
- Clean dataset saved in `data/processed/`  
- Updated `README.md` with this section  
