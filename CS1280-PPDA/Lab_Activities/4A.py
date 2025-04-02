import pandas as pd

def read_csv_analysis(file_path):
    """Reads a CSV file and performs basic analysis."""
    df = pd.read_csv(file_path)
    return df.describe()
