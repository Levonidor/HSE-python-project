from enum import StrEnum, IntEnum


class ColNames(StrEnum):
    RANK = "Rank"
    NAME = "Name"
    PLATFORM = "Platform"
    YEAR = "Year"
    GENRE = "Genre"
    PUBLISHER = "Publisher"
    NA_SALES = "NA_Sales"
    EU_SALES = "EU_Sales"
    JP_SALES = "JP_Sales"
    OTHER_SALES = "Other_Sales"
    GLOBAL_SALES = "Global_Sales"
    TOTAL_SALES = "Total_Sales"
    PERCENT = "Percent_of_total_sales"
    SALES = "Game_Sales"
    NA_PERCENT = "NA_Percent"
    EU_PERCENT = "EU_Percent"
    JP_PERCENT = "JP_Percent"
    OTHER_PERCENT = "Other_Percent"
    PERCENTAGE = "Percentage"
    TOTAL_COUNT = "Total_Count"
    REGION = 'Region'


genres_present = [
    "Sports",
    "Platform",
    "Racing",
    "Role-Playing",
    "Puzzle",
    "Misc",
    "Shooter",
    "Simulation",
    "Action",
    "Fighting",
    "Adventure",
    "Strategy",
]


platforms_present = [
    "DS",
    "N64",
    "PS3",
    "XB",
    "GC",
    "NG",
    "SAT",
    "GG",
    "NES",
    "PSV",
    "3DO",
    "X360",
    "GB",
    "GEN",
    "2600",
    "PS",
    "Wii",
    "TG16",
    "WS",
    "GBA",
    "WiiU",
    "3DS",
    "PCFX",
    "PS4",
    "PS2",
    "XOne",
    "DC",
    "SCD",
    "PSP",
    "SNES",
    "PC",
]
