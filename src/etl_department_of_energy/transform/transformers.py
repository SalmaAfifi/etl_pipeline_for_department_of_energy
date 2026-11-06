import pandas as pd

def transform_electricity_sales_data(raw_data: pd.DataFrame):
    """
    Transform electricity sales to find the total amount of electricity sold
    in the residential and transportation sectors.

    To transform the electricity sales data, you'll need to do the following:
    - Drop any records with NA values in the `price` column. Do this inplace.
    - Only keep records with a `sectorName` of "residential" or "transportation".
    - Create a `month` column using the first 4 characters of the values in `period`.
    - Create a `year` column using the last 2 characters of the values in `period`.
    - Return the transformed `DataFrame`, keeping only the columns `year`, `month`, `stateid`, `price` and `price-units`.
    """

    raw_data.dropna(axis=0, subset=['price'], inplace=True)
    sectorname_residential_or_transportation = raw_data.loc[raw_data["sectorName"].isin(["residential", "transportation"]),:]
    months = sectorname_residential_or_transportation["period"].str[:4]
    years = sectorname_residential_or_transportation["period"].str[-2:]
    full_data_frame = sectorname_residential_or_transportation.assign(year=years, month=months)
    final_data_frame = full_data_frame.loc[:, ["year", "month", "stateid", "price", "price-units"]]
    return final_data_frame