from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def categorical_encoding(df, column):
    """Applies OneHotEncoding and LabelEncoding."""
    le = LabelEncoder()
    df[column + '_label'] = le.fit_transform(df[column])
    ohe = OneHotEncoder()
    encoded = ohe.fit_transform(df[[column]]).toarray()
    return df, encoded
