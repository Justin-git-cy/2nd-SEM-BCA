# Handling missing values
df.fillna(df.mean(), inplace=True)  # Replace NaN with column mean
df.dropna(inplace=True)  # Drop rows with NaN values

# Removing duplicate rows
df.drop_duplicates(inplace=True)

print("Cleaned Data:\n", df)
