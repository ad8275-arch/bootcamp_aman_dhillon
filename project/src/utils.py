"""
Utility functions for data cleaning, normalization, standardization, and other common operations.
"""

import pandas as pd
import numpy as np
from typing import Union, List, Dict, Any, Optional, Tuple
import re
from datetime import datetime, date
import logging
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.impute import SimpleImputer
import warnings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ============================================================================
# DATA CLEANING FUNCTIONS
# ============================================================================

def clean_column_names(df: pd.DataFrame, 
                      lowercase: bool = True, 
                      replace_spaces: bool = True,
                      remove_special_chars: bool = True) -> pd.DataFrame:
    """
    Clean column names by standardizing format.
    
    Args:
        df: Input DataFrame
        lowercase: Convert to lowercase
        replace_spaces: Replace spaces with underscores
        remove_special_chars: Remove special characters
        
    Returns:
        DataFrame with cleaned column names
    """
    df_clean = df.copy()
    
    if lowercase:
        df_clean.columns = df_clean.columns.str.lower()
    
    if replace_spaces:
        df_clean.columns = df_clean.columns.str.replace(' ', '_')
    
    if remove_special_chars:
        df_clean.columns = df_clean.columns.str.replace(r'[^a-zA-Z0-9_]', '', regex=True)
    
    return df_clean

def remove_duplicates(df: pd.DataFrame, 
                     subset: Optional[List[str]] = None, 
                     keep: str = 'first') -> pd.DataFrame:
    """
    Remove duplicate rows from DataFrame.
    
    Args:
        df: Input DataFrame
        subset: Columns to consider for duplicates
        keep: Which duplicates to keep ('first', 'last', False)
        
    Returns:
        DataFrame with duplicates removed
    """
    return df.drop_duplicates(subset=subset, keep=keep)

def handle_missing_values(df: pd.DataFrame, 
                         strategy: str = 'drop',
                         fill_value: Any = None,
                         columns: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Handle missing values in DataFrame.
    
    Args:
        df: Input DataFrame
        strategy: 'drop', 'fill', or 'interpolate'
        fill_value: Value to fill missing values with
        columns: Specific columns to process
        
    Returns:
        DataFrame with missing values handled
    """
    df_clean = df.copy()
    
    if columns is None:
        columns = df_clean.columns
    
    if strategy == 'drop':
        df_clean = df_clean.dropna(subset=columns)
    elif strategy == 'fill':
        df_clean[columns] = df_clean[columns].fillna(fill_value)
    elif strategy == 'interpolate':
        df_clean[columns] = df_clean[columns].interpolate(method='linear')
    
    return df_clean

def clean_string_columns(df: pd.DataFrame, 
                        columns: Optional[List[str]] = None,
                        strip_whitespace: bool = True,
                        remove_extra_spaces: bool = True,
                        lowercase: bool = False) -> pd.DataFrame:
    """
    Clean string columns in DataFrame.
    
    Args:
        df: Input DataFrame
        columns: Specific string columns to clean
        strip_whitespace: Remove leading/trailing whitespace
        remove_extra_spaces: Remove multiple consecutive spaces
        lowercase: Convert to lowercase
        
    Returns:
        DataFrame with cleaned string columns
    """
    df_clean = df.copy()
    
    if columns is None:
        # Auto-detect string columns
        columns = df_clean.select_dtypes(include=['object']).columns.tolist()
    
    for col in columns:
        if col in df_clean.columns:
            if strip_whitespace:
                df_clean[col] = df_clean[col].astype(str).str.strip()
            
            if remove_extra_spaces:
                df_clean[col] = df_clean[col].astype(str).str.replace(r'\s+', ' ', regex=True)
            
            if lowercase:
                df_clean[col] = df_clean[col].astype(str).str.lower()
    
    return df_clean

def remove_outliers(df: pd.DataFrame, 
                   columns: List[str],
                   method: str = 'iqr',
                   threshold: float = 1.5) -> pd.DataFrame:
    """
    Remove outliers from specified columns.
    
    Args:
        df: Input DataFrame
        columns: Columns to check for outliers
        method: 'iqr' (interquartile range) or 'zscore'
        threshold: Threshold for outlier detection
        
    Returns:
        DataFrame with outliers removed
    """
    df_clean = df.copy()
    
    for col in columns:
        if col in df_clean.columns:
            if method == 'iqr':
                Q1 = df_clean[col].quantile(0.25)
                Q3 = df_clean[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - threshold * IQR
                upper_bound = Q3 + threshold * IQR
                
                mask = (df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)
                df_clean = df_clean[mask]
                
            elif method == 'zscore':
                z_scores = np.abs((df_clean[col] - df_clean[col].mean()) / df_clean[col].std())
                mask = z_scores < threshold
                df_clean = df_clean[mask]
    
    return df_clean

# ============================================================================
# NORMALIZATION FUNCTIONS
# ============================================================================

def normalize_data(df: pd.DataFrame, 
                  columns: List[str],
                  method: str = 'minmax',
                  range_min: float = 0,
                  range_max: float = 1) -> Tuple[pd.DataFrame, Any]:
    """
    Normalize numerical data using various methods.
    
    Args:
        df: Input DataFrame
        columns: Columns to normalize
        method: 'minmax', 'zscore', 'robust', or 'custom'
        range_min: Minimum value for minmax scaling
        range_max: Maximum value for minmax scaling
        
    Returns:
        Tuple of (normalized DataFrame, scaler object)
    """
    df_norm = df.copy()
    
    if method == 'minmax':
        scaler = MinMaxScaler(feature_range=(range_min, range_max))
    elif method == 'zscore':
        scaler = StandardScaler()
    elif method == 'robust':
        scaler = RobustScaler()
    else:
        raise ValueError("Method must be 'minmax', 'zscore', or 'robust'")
    
    df_norm[columns] = scaler.fit_transform(df_norm[columns])
    
    return df_norm, scaler

def log_transform(df: pd.DataFrame, 
                 columns: List[str],
                 add_constant: float = 1) -> pd.DataFrame:
    """
    Apply log transformation to specified columns.
    
    Args:
        df: Input DataFrame
        columns: Columns to transform
        add_constant: Constant to add before log (to handle zeros/negatives)
        
    Returns:
        DataFrame with log-transformed columns
    """
    df_transformed = df.copy()
    
    for col in columns:
        if col in df_transformed.columns:
            # Add constant to handle zeros and negative values
            df_transformed[col] = np.log(df_transformed[col] + add_constant)
    
    return df_transformed

def box_cox_transform(df: pd.DataFrame, 
                     columns: List[str],
                     lambda_param: float = 0.5) -> pd.DataFrame:
    """
    Apply Box-Cox transformation to specified columns.
    
    Args:
        df: Input DataFrame
        columns: Columns to transform
        lambda_param: Lambda parameter for transformation
        
    Returns:
        DataFrame with Box-Cox transformed columns
    """
    df_transformed = df.copy()
    
    for col in columns:
        if col in df_transformed.columns:
            if lambda_param == 0:
                df_transformed[col] = np.log(df_transformed[col])
            else:
                df_transformed[col] = (df_transformed[col] ** lambda_param - 1) / lambda_param
    
    return df_transformed

# ============================================================================
# STANDARDIZATION FUNCTIONS
# ============================================================================

def standardize_data(df: pd.DataFrame, 
                     columns: List[str],
                     method: str = 'zscore') -> Tuple[pd.DataFrame, Any]:
    """
    Standardize numerical data.
    
    Args:
        df: Input DataFrame
        columns: Columns to standardize
        method: 'zscore' or 'robust'
        
    Returns:
        Tuple of (standardized DataFrame, scaler object)
    """
    return normalize_data(df, columns, method=method)

def create_categorical_encoding(df: pd.DataFrame, 
                               columns: List[str],
                               method: str = 'onehot',
                               drop_first: bool = True) -> Tuple[pd.DataFrame, Dict]:
    """
    Create categorical encodings for categorical variables.
    
    Args:
        df: Input DataFrame
        columns: Categorical columns to encode
        method: 'onehot', 'label', or 'ordinal'
        drop_first: Whether to drop first category in one-hot encoding
        
    Returns:
        Tuple of (encoded DataFrame, encoding mappings)
    """
    df_encoded = df.copy()
    encodings = {}
    
    for col in columns:
        if col in df_encoded.columns:
            if method == 'onehot':
                dummies = pd.get_dummies(df_encoded[col], prefix=col, drop_first=drop_first)
                df_encoded = pd.concat([df_encoded, dummies], axis=1)
                df_encoded.drop(col, axis=1, inplace=True)
                encodings[col] = 'onehot'
                
            elif method == 'label':
                from sklearn.preprocessing import LabelEncoder
                le = LabelEncoder()
                df_encoded[col] = le.fit_transform(df_encoded[col])
                encodings[col] = le.classes_
                
            elif method == 'ordinal':
                unique_values = df_encoded[col].unique()
                value_mapping = {val: idx for idx, val in enumerate(sorted(unique_values))}
                df_encoded[col] = df_encoded[col].map(value_mapping)
                encodings[col] = value_mapping
    
    return df_encoded, encodings

# ============================================================================
# DATA VALIDATION FUNCTIONS
# ============================================================================

def validate_data_types(df: pd.DataFrame, 
                       expected_types: Dict[str, str]) -> Dict[str, bool]:
    """
    Validate that columns have expected data types.
    
    Args:
        df: Input DataFrame
        expected_types: Dictionary mapping column names to expected types
        
    Returns:
        Dictionary with validation results
    """
    validation_results = {}
    
    for col, expected_type in expected_types.items():
        if col in df.columns:
            actual_type = str(df[col].dtype)
            validation_results[col] = actual_type == expected_type
        else:
            validation_results[col] = False
    
    return validation_results

def check_data_quality(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Comprehensive data quality check.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Dictionary with data quality metrics
    """
    quality_report = {
        'total_rows': len(df),
        'total_columns': len(df.columns),
        'missing_values': df.isnull().sum().to_dict(),
        'missing_percentage': (df.isnull().sum() / len(df) * 100).to_dict(),
        'duplicate_rows': df.duplicated().sum(),
        'data_types': df.dtypes.to_dict(),
        'memory_usage': df.memory_usage(deep=True).sum(),
        'numeric_columns': df.select_dtypes(include=[np.number]).columns.tolist(),
        'categorical_columns': df.select_dtypes(include=['object']).columns.tolist()
    }
    
    return quality_report

# ============================================================================
# FILE UTILITY FUNCTIONS
# ============================================================================

def save_data_with_timestamp(df: pd.DataFrame, 
                           filepath: str,
                           format: str = 'csv',
                           include_timestamp: bool = True) -> str:
    """
    Save DataFrame with optional timestamp in filename.
    
    Args:
        df: DataFrame to save
        filepath: Base filepath
        format: File format ('csv', 'parquet', 'pickle')
        include_timestamp: Whether to add timestamp to filename
        
    Returns:
        Full filepath where data was saved
    """
    if include_timestamp:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        name, ext = filepath.rsplit('.', 1)
        filepath = f"{name}_{timestamp}.{ext}"
    
    if format == 'csv':
        df.to_csv(filepath, index=False)
    elif format == 'parquet':
        df.to_parquet(filepath, index=False)
    elif format == 'pickle':
        df.to_pickle(filepath)
    else:
        raise ValueError("Format must be 'csv', 'parquet', or 'pickle'")
    
    logger.info(f"Data saved to: {filepath}")
    return filepath

def load_data_with_auto_detect(filepath: str) -> pd.DataFrame:
    """
    Load data file with automatic format detection.
    
    Args:
        filepath: Path to data file
        
    Returns:
        Loaded DataFrame
    """
    if filepath.endswith('.csv'):
        return pd.read_csv(filepath)
    elif filepath.endswith('.parquet'):
        return pd.read_parquet(filepath)
    elif filepath.endswith('.pickle') or filepath.endswith('.pkl'):
        return pd.read_pickle(filepath)
    elif filepath.endswith('.xlsx') or filepath.endswith('.xls'):
        return pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format")

# ============================================================================
# STATISTICAL UTILITY FUNCTIONS
# ============================================================================

def calculate_summary_stats(df: pd.DataFrame, 
                          columns: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Calculate comprehensive summary statistics.
    
    Args:
        df: Input DataFrame
        columns: Specific columns to analyze
        
    Returns:
        DataFrame with summary statistics
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    stats = df[columns].describe()
    
    # Add additional statistics
    stats.loc['skewness'] = df[columns].skew()
    stats.loc['kurtosis'] = df[columns].kurtosis()
    stats.loc['missing_count'] = df[columns].isnull().sum()
    stats.loc['missing_pct'] = (df[columns].isnull().sum() / len(df) * 100)
    
    return stats

def detect_skewed_columns(df: pd.DataFrame, 
                          threshold: float = 1.0) -> List[str]:
    """
    Detect columns with skewed distributions.
    
    Args:
        df: Input DataFrame
        threshold: Skewness threshold
        
    Returns:
        List of skewed column names
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    skewed_cols = []
    
    for col in numeric_cols:
        skewness = abs(df[col].skew())
        if skewness > threshold:
            skewed_cols.append(col)
    
    return skewed_cols

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_memory_usage(df: pd.DataFrame) -> str:
    """Get memory usage of DataFrame in human-readable format."""
    memory_bytes = df.memory_usage(deep=True).sum()
    
    for unit in ['B', 'KB', 'MB', 'GB']:
        if memory_bytes < 1024.0:
            return f"{memory_bytes:.2f} {unit}"
        memory_bytes /= 1024.0
    
    return f"{memory_bytes:.2f} TB"

def print_dataframe_info(df: pd.DataFrame, 
                        name: str = "DataFrame") -> None:
    """Print comprehensive information about DataFrame."""
    print(f"\n{'='*50}")
    print(f"INFORMATION FOR: {name}")
    print(f"{'='*50}")
    print(f"Shape: {df.shape}")
    print(f"Memory Usage: {get_memory_usage(df)}")
    print(f"Data Types:")
    print(df.dtypes)
    print(f"\nMissing Values:")
    print(df.isnull().sum())
    print(f"\nFirst 5 rows:")
    print(df.head())
    print(f"\nLast 5 rows:")
    print(df.tail())

def create_sample_data(n_rows: int = 1000, 
                      n_cols: int = 10,
                      include_categorical: bool = True) -> pd.DataFrame:
    """
    Create sample data for testing purposes.
    
    Args:
        n_rows: Number of rows
        n_cols: Number of columns
        include_categorical: Whether to include categorical columns
        
    Returns:
        Sample DataFrame
    """
    np.random.seed(42)
    
    data = {}
    
    # Numeric columns
    for i in range(n_cols // 2):
        data[f'num_col_{i}'] = np.random.normal(0, 1, n_rows)
    
    # Categorical columns
    if include_categorical:
        categories = ['A', 'B', 'C', 'D']
        for i in range(n_cols // 2):
            data[f'cat_col_{i}'] = np.random.choice(categories, n_rows)
    
    # Add some missing values
    df = pd.DataFrame(data)
    mask = np.random.random(df.shape) < 0.1
    df[mask] = np.nan
    
    return df

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Example usage
    print("Creating sample data...")
    sample_df = create_sample_data(100, 6)
    
    print("Original data:")
    print_dataframe_info(sample_df, "Sample Data")
    
    print("\nCleaning data...")
    cleaned_df = clean_column_names(sample_df)
    cleaned_df = handle_missing_values(cleaned_df, strategy='fill', fill_value=0)
    
    print("\nCleaned data:")
    print_dataframe_info(cleaned_df, "Cleaned Data")
    
    print("\nData quality report:")
    quality_report = check_data_quality(cleaned_df)
    for key, value in quality_report.items():
        print(f"{key}: {value}")
