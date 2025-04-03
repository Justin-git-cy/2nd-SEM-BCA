import pandas as pd

def analyze_csv(filename):
    df = pd.read_csv(filename)
    print("\nBasic Statistics:\n", df.describe())  

filename = "sample.csv"
analyze_csv(filename)
