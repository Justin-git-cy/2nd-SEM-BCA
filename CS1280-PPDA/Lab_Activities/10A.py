import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

data = {'Category': ['Red', 'Blue', 'Green', 'Red', 'Blue']}
df = pd.DataFrame(data)

label_encoder = LabelEncoder()
df["Category_Label"] = label_encoder.fit_transform(df["Category"])
print("\nLabel Encoded Data:\n", df)

one_hot_encoder = OneHotEncoder(sparse=False)
one_hot_encoded = one_hot_encoder.fit_transform(df[['Category']])

df_one_hot = pd.DataFrame(one_hot_encoded, columns=one_hot_encoder.get_feature_names_out(['Category']))
df = df.join(df_one_hot)

print("\nOne-Hot Encoded Data:\n", df)
