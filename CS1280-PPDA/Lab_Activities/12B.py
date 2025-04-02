def time_series_analysis(df, date_column, value_column):
    """Performs time series analysis on stock prices."""
    df[date_column] = pd.to_datetime(df[date_column])
    df.set_index(date_column, inplace=True)
    return df[value_column].resample('M').mean()  
