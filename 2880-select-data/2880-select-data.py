import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df = students
    ans = df[df["student_id"] == 101]
    return ans[["name", "age"]]