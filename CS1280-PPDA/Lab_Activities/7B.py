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

# Handling missing values
df.fillna(df.mean(), inplace=True)  # Replace NaN with column mean
df.dropna(inplace=True)  # Drop rows with NaN values

# Removing duplicate rows
df.drop_duplicates(inplace=True)

print("Cleaned Data:\n", df)
