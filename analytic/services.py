from .cfg import ColNames,platforms_present
import pandas as pd
import numpy as np


def count_total_sales(df: pd.DataFrame) -> pd.DataFrame:
    total_sales = dict()
    for i in range(len(df)):
        if df.loc[i][ColNames.NAME] in total_sales:
            total_sales[df.loc[i][ColNames.NAME]] += float(df.loc[i][ColNames.GLOBAL_SALES])
        else:
            total_sales[df.loc[i][ColNames.NAME]] = float(df.loc[i][ColNames.GLOBAL_SALES])
    for name,sales in total_sales.items():
        total_sales[name] = round(float(sales),5)
    df[ColNames.TOTAL_SALES] = None
    for i in range(len(df)):
        df.at[i,ColNames.TOTAL_SALES] = total_sales[df.loc[i][ColNames.NAME]]
    return df

def game_platform_sales_percentage(df: pd.DataFrame, game: str, platform:str) -> list[float,float]:
    if platform in platforms_present:
        for i in range(len(df)):
            if df.loc[i][ColNames.PLATFORM] == platform and df.loc[i][ColNames.NAME] == game:
                return [round(float(df.loc[i][ColNames.GLOBAL_SALES])/float(df.loc[i][ColNames.TOTAL_SALES])*100,2), float(df.loc[i][ColNames.GLOBAL_SALES])]

def platform_sales(df: pd.DataFrame) -> pd.DataFrame:
    platform_amount = dict()
    all_sales_amount = 0
    for i in range(len(df)):
        if df.loc[i][ColNames.PLATFORM] in platform_amount:
            platform_amount[df.loc[i][ColNames.PLATFORM]] += float(df.loc[i][ColNames.GLOBAL_SALES])
        else:
            platform_amount[df.loc[i][ColNames.PLATFORM]] = float(df.loc[i][ColNames.GLOBAL_SALES])
        all_sales_amount += float(df.loc[i][ColNames.GLOBAL_SALES])
    all_sales_amount = round(all_sales_amount,3)
    platform_sales = pd.DataFrame(columns=[ColNames.PLATFORM,ColNames.SALES,ColNames.PERCENT])
    for name,sales in platform_amount.items():
        platform_sales.loc[len(platform_sales)] = [name,round(sales,3),round(sales/all_sales_amount*100,4)]
    return platform_sales