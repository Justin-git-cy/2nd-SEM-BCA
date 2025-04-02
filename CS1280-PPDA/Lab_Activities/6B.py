def clean_data(df):
    """Handles missing values and duplicates in DataFrame."""
    df = df.dropna()  # Remove missing values
    df = df.drop_duplicates()  # Remove duplicates
    return df
