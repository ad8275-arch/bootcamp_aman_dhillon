import pandas as pd
import numpy as np



def optimize_memory_usage(df: pd.DataFrame) -> pd.DataFrame:
    """
    Optimize memory usage of a DataFrame by changing the dtypes of its columns.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame to optimize.
    
    Returns:
    pd.DataFrame: The optimized DataFrame with reduced memory usage.
    """
    
    
    
    initial_memory = df.memory_usage(deep=True).sum() / 1024**2  # in MB
    
    print(f"Initial memory usage: {initial_memory:.2f} MB")
    
    for col in df.columns:
        col_type = df[col].dtype
        
        if col_type != object:
            if pd.api.types.is_integer_dtype(col_type):
                c_min = df[col].min()
                c_max = df[col].max()
                
                if c_min >= 0:
                    if c_max < np.iinfo(np.uint8).max:
                        df[col] = df[col].astype(np.uint8)
                    elif c_max < np.iinfo(np.uint16).max:
                        df[col] = df[col].astype(np.uint16)
                    elif c_max < np.iinfo(np.uint32).max:
                        df[col] = df[col].astype(np.uint32)
                    elif c_max < np.iinfo(np.uint64).max:
                        df[col] = df[col].astype(np.uint64)
                else:
                    if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                        df[col] = df[col].astype(np.int8)
                    elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                        df[col] = df[col].astype(np.int16)
                    elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                        df[col] = df[col].astype(np.int32)
                    elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                        df[col] = df[col].astype(np.int64)
            
            elif pd.api.types.is_float_dtype(col_type):
                df[col] = df[col].astype(np.float32)
                
        else:
            num_unique_values = df[col].nunique()
            num_total_values = len(df[col])
            
            if num_unique_values / num_total_values < 0.5:
                df[col] = df[col].astype('category')
                
    final_memory = df.memory_usage(deep=True).sum() / 1024**2  # in MB
    print(f"Final memory usage: {final_memory:.2f} MB")
    print(f"Reduced by: {initial_memory - final_memory:.2f} MB ({100 * (initial_memory - final_memory) / initial_memory:.2f}%)")
    
    return df


def find_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    numeric_df = df.select_dtypes(include=[np.number])
    return numeric_df


def convert_datetime_columns(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns:
        # Try to convert columns to datetime if they are not already
        if df[col].dtype == object:
            try:
                df[col] = pd.to_datetime(df[col], errors='raise')
            except (ValueError, TypeError):
                continue

    return df


def clean_and_convert_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:

    for col in df.select_dtypes(include=['category', 'object']).columns:
        print(col)
        df[col] = df[col].astype(str).str.strip()
        df = df[df[col].apply(lambda x: str(x).replace('.', '', 1).isdigit())]
        df[col] = pd.to_numeric(df[col])

    return df



def contract_size_handler(contract_size):
    contract_size = contract_size.split(' x ')
    return int(contract_size[0])* int(contract_size[1])


def black_scholes(S, K, T, r, sigma, option_type='call'):
    """
    Calculate the Black-Scholes price for a European call or put option.

    Parameters:
    S : float : Stock price
    K : float : Strike price
    T : float : Time to maturity (in years)
    r : float : Risk-free interest rate (annual rate)
    sigma : float : Volatility of the underlying stock (annual standard deviation)
    option_type : str : 'call' or 'put'

    Returns:
    price : float : Price of the option
    """
    try:
        d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)
    except: return np.nan
    if option_type == 'call':
        try:
            price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
        except: price=np.nan
    elif option_type == 'put':
        try:
            price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        except:price=np.nan
    return price