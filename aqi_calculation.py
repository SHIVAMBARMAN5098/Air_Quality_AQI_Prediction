import pandas as pd
import numpy as np

def calculate_pm25_subindex(pm25):
    if pd.isna(pm25): return np.nan
    if pm25 <= 30: return pm25 * 50 / 30
    elif pm25 <= 60: return 50 + (pm25 - 30) * 50 / 30
    elif pm25 <= 90: return 100 + (pm25 - 60) * 100 / 30
    elif pm25 <= 120: return 200 + (pm25 - 90) * 100 / 30
    elif pm25 <= 250: return 300 + (pm25 - 120) * 100 / 130
    else: return 400 + (pm25 - 250) * 100 / 130

def calculate_pm10_subindex(pm10):
    if pd.isna(pm10): return np.nan
    if pm10 <= 50: return pm10
    elif pm10 <= 100: return 50 + (pm10 - 50) * 50 / 50
    elif pm10 <= 250: return 100 + (pm10 - 100) * 100 / 150
    elif pm10 <= 350: return 200 + (pm10 - 250) * 100 / 100
    elif pm10 <= 430: return 300 + (pm10 - 350) * 100 / 80
    else: return 400 + (pm10 - 430) * 100 / 80

def add_cpcb_aqi(df):
    """
    Calculate CPCB AQI based on PM2.5 and PM10 sub-indices.
    """
    df = df.copy()
    sub_pm25 = df['PM2.5'].apply(calculate_pm25_subindex)
    sub_pm10 = df['PM10'].apply(calculate_pm10_subindex)

    # Sub-indices ka maximum value hi CPCB AQI hota hai
    df['AQI'] = np.maximum(sub_pm25.fillna(0), sub_pm10.fillna(0))
    df['AQI'] = df['AQI'].replace(0, np.nan)
    return df