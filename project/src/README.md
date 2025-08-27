# Python Utility Functions

This directory contains comprehensive Python utility functions for data science and machine learning workflows.

## Files

- `utils.py` - Main utility functions file
- `example_usage.py` - Example script demonstrating usage
- `README.md` - This documentation file

## Installation

Install the required dependencies:

```bash
pip install -r ../requirements.txt
```

## Main Utility Functions

### Data Cleaning Functions

#### `clean_column_names(df, lowercase=True, replace_spaces=True, remove_special_chars=True)`
Clean and standardize DataFrame column names.

**Parameters:**
- `df`: Input DataFrame
- `lowercase`: Convert to lowercase
- `replace_spaces`: Replace spaces with underscores
- `remove_special_chars`: Remove special characters

**Example:**
```python
from utils import clean_column_names

# Clean column names
df_clean = clean_column_names(df)
```

#### `remove_duplicates(df, subset=None, keep='first')`
Remove duplicate rows from DataFrame.

**Parameters:**
- `df`: Input DataFrame
- `subset`: Columns to consider for duplicates
- `keep`: Which duplicates to keep ('first', 'last', False)

#### `handle_missing_values(df, strategy='drop', fill_value=None, columns=None)`
Handle missing values using various strategies.

**Parameters:**
- `df`: Input DataFrame
- `strategy`: 'drop', 'fill', or 'interpolate'
- `fill_value`: Value to fill missing values with
- `columns`: Specific columns to process

**Example:**
```python
# Fill missing values with 0
df_clean = handle_missing_values(df, strategy='fill', fill_value=0)

# Drop rows with missing values
df_clean = handle_missing_values(df, strategy='drop')
```

#### `clean_string_columns(df, columns=None, strip_whitespace=True, remove_extra_spaces=True, lowercase=False)`
Clean string columns by removing whitespace, extra spaces, and converting case.

#### `remove_outliers(df, columns, method='iqr', threshold=1.5)`
Remove outliers using IQR or Z-score methods.

### Normalization Functions

#### `normalize_data(df, columns, method='minmax', range_min=0, range_max=1)`
Normalize numerical data using various methods.

**Methods:**
- `minmax`: Min-Max scaling (0-1 range)
- `zscore`: Z-score standardization
- `robust`: Robust scaling using median and IQR

**Example:**
```python
# Min-max normalization
df_norm, scaler = normalize_data(df, ['col1', 'col2'], method='minmax')

# Z-score standardization
df_std, scaler = normalize_data(df, ['col1', 'col2'], method='zscore')
```

#### `log_transform(df, columns, add_constant=1)`
Apply log transformation to specified columns.

#### `box_cox_transform(df, columns, lambda_param=0.5)`
Apply Box-Cox transformation to specified columns.

### Standardization Functions

#### `standardize_data(df, columns, method='zscore')`
Standardize numerical data (alias for normalize_data with zscore method).

#### `create_categorical_encoding(df, columns, method='onehot', drop_first=True)`
Create categorical encodings for categorical variables.

**Methods:**
- `onehot`: One-hot encoding
- `label`: Label encoding
- `ordinal`: Ordinal encoding

**Example:**
```python
# One-hot encoding
df_encoded, encodings = create_categorical_encoding(
    df, ['category_col'], method='onehot', drop_first=True
)
```

### Data Validation Functions

#### `validate_data_types(df, expected_types)`
Validate that columns have expected data types.

#### `check_data_quality(df)`
Comprehensive data quality check returning various metrics.

**Returns:**
- Total rows and columns
- Missing values count and percentage
- Duplicate rows count
- Data types
- Memory usage
- Numeric and categorical column lists

### File Utility Functions

#### `save_data_with_timestamp(df, filepath, format='csv', include_timestamp=True)`
Save DataFrame with optional timestamp in filename.

**Supported formats:**
- CSV
- Parquet
- Pickle

#### `load_data_with_auto_detect(filepath)`
Load data file with automatic format detection.

**Supported formats:**
- CSV
- Parquet
- Pickle
- Excel (xlsx, xls)

### Statistical Utility Functions

#### `calculate_summary_stats(df, columns=None)`
Calculate comprehensive summary statistics including skewness, kurtosis, and missing values.

#### `detect_skewed_columns(df, threshold=1.0)`
Detect columns with skewed distributions.

### Helper Functions

#### `get_memory_usage(df)`
Get memory usage of DataFrame in human-readable format.

#### `print_dataframe_info(df, name="DataFrame")`
Print comprehensive information about DataFrame.

#### `create_sample_data(n_rows=1000, n_cols=10, include_categorical=True)`
Create sample data for testing purposes.

## Usage Examples

### Basic Data Cleaning Pipeline

```python
from utils import *

# Load data
df = load_data_with_auto_detect('data.csv')

# Clean data
df_clean = clean_column_names(df)
df_clean = handle_missing_values(df_clean, strategy='fill', fill_value=0)
df_clean = clean_string_columns(df_clean, lowercase=True)

# Remove outliers
numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
df_clean = remove_outliers(df_clean, numeric_cols, method='iqr')

# Normalize data
df_normalized, scaler = normalize_data(df_clean, numeric_cols, method='minmax')

# Save processed data
save_data_with_timestamp(df_normalized, 'cleaned_data.csv')
```

### Data Quality Assessment

```python
# Check data quality
quality_report = check_data_quality(df)
print(f"Total rows: {quality_report['total_rows']}")
print(f"Missing values: {quality_report['missing_values']}")

# Get summary statistics
stats = calculate_summary_stats(df)
print(stats)

# Detect skewed columns
skewed_cols = detect_skewed_columns(df, threshold=1.0)
print(f"Skewed columns: {skewed_cols}")
```

### Categorical Data Processing

```python
# Encode categorical variables
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
df_encoded, encodings = create_categorical_encoding(
    df, categorical_cols, method='onehot', drop_first=True
)

print(f"Encoding mappings: {encodings}")
```

## Running the Example

To see all functions in action, run:

```bash
cd src/
python example_usage.py
```

This will create sample data, demonstrate all the utility functions, and show the results.

## Dependencies

- pandas >= 1.5.0
- numpy >= 1.21.0
- scikit-learn >= 1.1.0
- openpyxl >= 3.0.0 (for Excel files)
- pyarrow >= 10.0.0 (for Parquet files)

## Notes

- All functions return copies of DataFrames to avoid modifying original data
- Functions include comprehensive error handling and logging
- Type hints are provided for better code documentation
- Functions are designed to work together in data processing pipelines
