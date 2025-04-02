def data_distribution(df):
    """Analyzes data distribution."""
    return {
        'describe': df.describe(),
        'quantile': df.quantile(),
        'skew': df.skew(),
        'kurtosis': df.kurt(),
        'value_counts': df.apply(pd.Series.value_counts)
    }
