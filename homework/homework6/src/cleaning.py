def fill_missing_median(df, required_columns):
    for column in required_columns:
        df[column] = df[column].fillna(df[column].median())
    return df

def drop_missing(df,threshold=0.5):
    required_non_na = int(threshold*df.shape[1])
    return df.dropna(thresh=required_non_na)



def normalize_data(df,required_columns):
    for column in required_columns:
        col_min = df[column].min()
        col_max = df[column].max()
        df[column] = (df[column] - col_min) / (col_max - col_min)
    return df

