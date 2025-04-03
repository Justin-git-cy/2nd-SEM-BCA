import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}

mean_value = df["Salary"].mean()  
median_value = df["Salary"].median()  
mode_value = df["Salary"].mode()[0] 
min_value = df["Salary"].min()  
max_value = df["Salary"].max()  
variance = df["Salary"].var()  
std_dev = df["Salary"].std()  

print(f"Mean: {mean_value}, Median: {median_value}, Mode: {mode_value}")
print(f"Min: {min_value}, Max: {max_value}")
print(f"Variance: {variance}, Standard Deviation: {std_dev}")
