def remove_known_outliers(df):
    """Remove specific known outliers"""
    before = df.shape[0]
    df_cleaned = df[~((df['gr_liv_area'] > 4000) & (df['saleprice'] < 300000))]
    after = df_cleaned.shape[0]
    print(f"Removed {before - after} known outliers based on GrLivArea and Saleprice.")
    return df_cleaned

def remove_iqr_outliers(df, column):
    """Remove outliers using IQR method for a single column."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    before = df.shape[0]
    df_cleaned = df[(df[column] >= lower) & (df[column] <= upper)]
    after = df_cleaned.shape[0]
    print(f"Removed {before - after} outlier(s) in {column} using IQR.")
    return df_cleaned

def remove_extreme_outliers(df, iqr_columns=None):
    """Run known + IQR-based outlier removal."""
    print("Starting outlier removal...")
    df = remove_known_outliers(df)
    
    if iqr_columns:
        for col in iqr_columns:
            df = remove_iqr_outliers(df, col)
            
    print(f"Final dataset has {df.shape[0]} rows and {df.shape[1]} columns.")
    return df