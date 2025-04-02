import pandas as pd

df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'val1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'val2': [4, 5, 6]})
merged_df = df1.merge(df2, on='key', how='outer')
grouped_df = merged_df.groupby('key').sum()
concatenated_df = pd.concat([df1, df2], axis=0)
joined_df = df1.set_index('key').join(df2.set_index('key'))
