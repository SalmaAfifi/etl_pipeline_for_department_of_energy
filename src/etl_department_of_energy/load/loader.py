import pandas as pd

def load(dataframe: pd.DataFrame, file_path: str):
    """Load a DataFrame to a file in either CSV or Parquet format."""
    if file_path.endswith(".csv"):
        dataframe.to_csv(file_path, index=False)
    elif file_path.endswith(".parquet"):
        dataframe.to_parquet(file_path)
    else:
        raise ValueError(f"File type not supported: {file_path}")