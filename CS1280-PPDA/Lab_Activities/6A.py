def create_dataframe(file_path):
    """Creates a DataFrame from a CSV file."""
    return pd.read_csv(file_path)

def create_dataframe_scratch():
    """Creates a DataFrame from scratch."""
    data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
    return pd.DataFrame(data)
