# Access a column
print(df["Name"])
# Accessing a row by label
print(df.loc[0])
# Access a row by index
print(df.iloc[1])
# Access a specific cell
print(df.at[0, "Age"])
# Slicing
print(df[1:3]) # Slicing rows
