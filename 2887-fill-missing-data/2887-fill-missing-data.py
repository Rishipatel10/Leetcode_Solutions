import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    df = products
    df = df.fillna({"quantity":0})
    return df
