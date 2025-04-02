def advanced_pandas_operations(df1, df2, key):
    """Performs advanced Pandas operations like GroupBy, merging, joining, and concatenating."""
    grouped = df1.groupby(key).mean()  # GroupBy operation
    merged = pd.merge(df1, df2, on=key, how='inner')  # Merging
    joined = df1.join(df2.set_index(key), on=key)  # Joining
    concatenated = pd.concat([df1, df2], axis=0)  # Concatenation
    return grouped, merged, joined, concatenated
