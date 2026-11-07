from extract.extractors import extract_json_data, extract_tabular_data
from transform.transformers import transform_electricity_sales_data
from load.loader import load

raw_electricity_capability_df = extract_json_data("../../data/raw/electricity_capability_nested.json")
raw_electricity_sales_df = extract_tabular_data("../../data/raw/electricity_sales.csv")

cleaned_electricity_sales_df = transform_electricity_sales_data(raw_electricity_sales_df)

load(raw_electricity_capability_df, "../../data/processed/loaded__electricity_capability.parquet")
load(cleaned_electricity_sales_df, "../../data/processed/loaded__electricity_sales.csv")