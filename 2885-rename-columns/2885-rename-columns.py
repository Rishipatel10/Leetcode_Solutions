import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    df = students
    df = df.rename(columns={'id': 'student_id'})
    df = df.rename(columns={'first': 'first_name'})
    df = df.rename(columns={'last': 'last_name'})
    df = df.rename(columns={'age': 'age_in_years'})
    return df