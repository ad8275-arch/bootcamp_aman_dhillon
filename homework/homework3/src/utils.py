def get_summary_stats(df):
    group_column = input("Enter the column you want grouping on:")
    target_column = input("Enter the target column")
    summary = df.groupby(group_column)[target_column].agg(['min','max','std']).reset_index(inplace=True)
    return summary
