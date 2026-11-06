import pandas as pd
import json

def extract_tabular_data(file_path: str):
    """Extract data from a tabular file_format, with pandas."""
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".parquet"):
        return pd.read_parquet(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")


def extract_json_data(file_path):
    """Extract and flatten data from a JSON file."""
    with open(file_path) as f:
        nested_json = json.load(f)
    return pd.json_normalize(nested_json)
