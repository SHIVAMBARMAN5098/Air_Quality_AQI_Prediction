import pandas as pd
import glob
import os

def load_all_raw_data(raw_folder_path="data/raw"):
    """
    Load all CSV files from data/raw, clean column spaces, and combine them.
    """
    csv_files = glob.glob(os.path.join(raw_folder_path, "*.csv"))
    
    if not csv_files:
        print(f"No CSV files found in {raw_folder_path}")
        return None
        
    df_list = []
    print(f"Found {len(csv_files)} CSV files in {raw_folder_path}:")
    
    for file in csv_files:
        try:
            temp_df = pd.read_csv(file)
            # Strip trailing/leading spaces from column names immediately
            temp_df.columns = temp_df.columns.str.strip()
            print(f" - Loaded: {os.path.basename(file)} | Rows: {temp_df.shape[0]}, Cols: {temp_df.shape[1]}")
            df_list.append(temp_df)
        except Exception as e:
            print(f" - Error loading {file}: {e}")
            
    combined_df = pd.concat(df_list, ignore_index=True)
    print(f"\nTotal combined rows: {combined_df.shape[0]}")
    print(f"Total combined columns: {combined_df.shape[1]}")
    
    return combined_df