# Fill missing values with 0
df.fillna(0, inplace=True)
print(df)

# Fill missing values with the mean of the column
df["C"].fillna(df["C"].mean(), inplace=True)
print(df)
