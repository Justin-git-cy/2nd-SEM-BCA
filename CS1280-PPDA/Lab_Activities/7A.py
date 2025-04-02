def descriptive_statistics(df):
    """Calculates central tendencies and dispersion."""
    return {
        'mean': df.mean(),
        'median': df.median(),
        'mode': df.mode(),
        'min': df.min(),
        'max': df.max(),
        'variance': df.var(),
        'std_dev': df.std()
    }
