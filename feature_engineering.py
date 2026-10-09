import pandas as pd

def extract_time_features(df):
    """
    Extract date and time components for ML model training.
    """
    df = df.copy()
    if 'Timestamp' in df.columns:
        df['Year'] = df['Timestamp'].dt.year
        df['Month'] = df['Timestamp'].dt.month
        df['Day'] = df['Timestamp'].dt.day
        df['DayOfWeek'] = df['Timestamp'].dt.dayofweek
        df['IsWeekend'] = df['DayOfWeek'].apply(lambda x: 1 if x >= 5 else 0)
    return df