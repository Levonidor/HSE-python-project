import pandas as pd


def create_dataframe() -> pd.DataFrame:
    dataframe = pd.read_csv("./kaggle/vgsales.csv")
    dataframe = dataframe.dropna().reset_index(drop=True)
    return dataframe
