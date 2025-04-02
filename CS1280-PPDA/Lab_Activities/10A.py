from sklearn.preprocessing import StandardScaler, Normalizer, MinMaxScaler

def scale_data(df):
    """Scales data using StandardScaler, Normalizer, and MinMaxScaler."""
    return {
        'StandardScaler': StandardScaler().fit_transform(df),
        'Normalizer': Normalizer().fit_transform(df),
        'MinMaxScaler': MinMaxScaler().fit_transform(df)
    }
