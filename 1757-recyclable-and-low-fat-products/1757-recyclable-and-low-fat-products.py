import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products
    ans = df[(df["low_fats"] == 'Y') & (df["recyclable"] == 'Y')]
    return ans[["product_id"]]