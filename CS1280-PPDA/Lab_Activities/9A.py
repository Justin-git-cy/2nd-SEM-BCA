import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}

print(df.describe())  

print("25th Percentile:", df["Salary"].quantile(0.25))
print("Median (50th Percentile):", df["Salary"].quantile(0.50))
print("75th Percentile:", df["Salary"].quantile(0.75))

print("Skewness:", df["Salary"].skew())

print("Kurtosis:", df["Salary"].kurt())

print(df["Name"].value_counts())
