from .cfg import ColNames,platforms_present
import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data()
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

@st.cache_data()
def create_total_sales_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    total_sales = dict()
    for i in range(len(df)):
        if df.loc[i][ColNames.NAME] in total_sales:
            total_sales[df.loc[i][ColNames.NAME]] += float(df.loc[i][ColNames.GLOBAL_SALES])
        else:
            total_sales[df.loc[i][ColNames.NAME]] = float(df.loc[i][ColNames.GLOBAL_SALES])
    dataframe = pd.DataFrame(columns=[ColNames.NAME,ColNames.PUBLISHER,ColNames.TOTAL_SALES])
    i = 0
    for name,sales in total_sales.items():
        total_sales[name] = round(float(sales),5)
        dataframe.at[i,ColNames.NAME] = name
        dataframe.at[i,ColNames.TOTAL_SALES] = sales
        dataframe.at[i,ColNames.PUBLISHER] = df.loc[df[ColNames.NAME] == name].iloc[0][ColNames.PUBLISHER]
        dataframe.at[i,ColNames.TOTAL_SALES] = sales
        i += 1
    return dataframe


@st.cache_data()
def game_platform_sales_percentage(df: pd.DataFrame, game: str, platform:str) -> list[float,float]:
    if platform in platforms_present:
        for i in range(len(df)):
            if df.loc[i][ColNames.PLATFORM] == platform and df.loc[i][ColNames.NAME] == game:
                return [round(float(df.loc[i][ColNames.GLOBAL_SALES])/float(df.loc[i][ColNames.TOTAL_SALES])*100,2), float(df.loc[i][ColNames.GLOBAL_SALES])]


@st.cache_data()
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


@st.cache_data()
def create_sales_percentage_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df[ColNames.NA_PERCENT] = None
    df[ColNames.EU_PERCENT] = None
    df[ColNames.JP_PERCENT] = None
    df[ColNames.OTHER_PERCENT] = None
    for i in range(len(df)):
        df.at[i,ColNames.NA_PERCENT] = round(float(df.loc[i][ColNames.NA_SALES])/float(df.loc[i][ColNames.GLOBAL_SALES])*100,3)
        df.at[i,ColNames.EU_PERCENT] = round(float(df.loc[i][ColNames.EU_SALES])/float(df.loc[i][ColNames.GLOBAL_SALES])*100,3)
        df.at[i,ColNames.JP_PERCENT] = round(float(df.loc[i][ColNames.JP_SALES])/float(df.loc[i][ColNames.GLOBAL_SALES])*100,3)
        df.at[i,ColNames.OTHER_PERCENT] = round(float(df.loc[i][ColNames.OTHER_SALES])/float(df.loc[i][ColNames.GLOBAL_SALES])*100,3)
    return df 


@st.cache_data()
def create_first_tsd_presentation_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.groupby(ColNames.PUBLISHER, as_index=False)[ColNames.TOTAL_SALES].sum()
    df[ColNames.PERCENTAGE] = df[ColNames.TOTAL_SALES] / df[ColNames.TOTAL_SALES].sum() * 100
    border = 1
    major_publishers = df[df[ColNames.PERCENTAGE] >= border]
    other_publishers = df[df[ColNames.PERCENTAGE] < border]
    other_total = other_publishers[ColNames.TOTAL_SALES].sum()
    other_row = pd.DataFrame({
        ColNames.PUBLISHER: ["Others"],
        ColNames.TOTAL_SALES: [other_total],
        ColNames.PERCENTAGE: [other_total / df[ColNames.TOTAL_SALES].sum() * 100],
    })
    tsd_presentation_dataframe = pd.concat([major_publishers, other_row], ignore_index=True)
    return tsd_presentation_dataframe

@st.cache_data()
def create_games_by_publisher_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    count_games = df.groupby(ColNames.PUBLISHER)[ColNames.NAME].count().reset_index()
    count_games.columns = [ColNames.PUBLISHER, ColNames.TOTAL_COUNT]
    return count_games


@st.cache_data()
def create_second_tsd_presentation_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.groupby(ColNames.PUBLISHER, as_index=False)[ColNames.TOTAL_COUNT].sum()
    df[ColNames.PERCENTAGE] = df[ColNames.TOTAL_COUNT] / df[ColNames.TOTAL_COUNT].sum() * 100
    border = 1
    major_publishers = df[df[ColNames.PERCENTAGE] >= border]
    other_publishers = df[df[ColNames.PERCENTAGE] < border]
    other_total = other_publishers[ColNames.TOTAL_COUNT].sum()
    other_row = pd.DataFrame({
        ColNames.PUBLISHER: ["Others"],
        ColNames.TOTAL_COUNT: [other_total],
        ColNames.PERCENTAGE: [other_total / df[ColNames.TOTAL_COUNT].sum() * 100],
    })
    tsd_presentation_dataframe = pd.concat([major_publishers, other_row], ignore_index=True)
    return tsd_presentation_dataframe

@st.cache_data()
def spd_dataframes(df: pd.DataFrame) -> pd.DataFrame:
    spd_dataframe = pd.DataFrame(columns=[ColNames.GENRE,ColNames.YEAR,ColNames.SALES])
    for i in range(len(df)):
        spd_dataframe.at[i,ColNames.GENRE] = df.iloc[i][ColNames.GENRE]
        spd_dataframe.at[i,ColNames.YEAR] = df.iloc[i][ColNames.YEAR]
        spd_dataframe.at[i,ColNames.SALES] = df.iloc[i][ColNames.GLOBAL_SALES]
    spd_first_dataframe = spd_dataframe.groupby([ColNames.GENRE], as_index=False)[ColNames.SALES].sum()
    spd_second_dataframe = spd_dataframe.groupby([ColNames.GENRE,ColNames.YEAR], as_index=False)[ColNames.SALES].sum()
    return [spd_first_dataframe,spd_second_dataframe]

