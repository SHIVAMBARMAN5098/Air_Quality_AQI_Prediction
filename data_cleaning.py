import pandas as pd

def clean_data(df):
    df = df.copy()
    
    # Strip spaces from column names
    df.columns = df.columns.str.strip()
    
    # Convert Timestamp
    timestamp_col = [col for col in df.columns if "time" in col.lower() or "date" in col.lower()]
    if timestamp_col:
        df[timestamp_col[0]] = pd.to_datetime(df[timestamp_col[0]], errors="coerce")
        df.rename(columns={timestamp_col[0]: "Timestamp"}, inplace=True)
    
    # Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    print(f"Duplicates removed: {before - len(df)}")
    
    # Forward fill & backward fill missing numeric values
    numeric_cols = ['PM2.5', 'PM10', 'SO2', 'CO', 'Ozone']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].ffill().bfill()
            
    if "Timestamp" in df.columns:
        df = df.sort_values("Timestamp")

    return df.reset_index(drop=True)