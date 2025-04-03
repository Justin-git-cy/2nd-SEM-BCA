import pandas as pd

# Creating a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}

# Converting dictionary into a DataFrame
df = pd.DataFrame(data)
print(df)
# Reading a CSV file into a DataFrame
df = pd.read_csv("data.csv")  # Replace "data.csv" with your file
print(df.head())  # Display first 5 rows
