import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    df = products
    ans = df.fillna({"quantity":0})
    return ans
