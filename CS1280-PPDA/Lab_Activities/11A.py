from sklearn.preprocessing import StandardScaler, Normalizer, MinMaxScaler
import numpy as np
import pandas as pd

data = {'Feature1': [10, 20, 30, 40, 50], 'Feature2': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data)

scaler = StandardScaler()
df_standard = scaler.fit_transform(df)
print("\nStandard Scaled Data:\n", df_standard)

minmax_scaler = MinMaxScaler()
df_minmax = minmax_scaler.fit_transform(df)
print("\nMin-Max Scaled Data:\n", df_minmax)

normalizer = Normalizer()
df_normalized = normalizer.fit_transform(df)
print("\nNormalized Data:\n", df_normalized)
