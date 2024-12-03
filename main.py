from kaggle.kaggle_read import *
from analytic.services import *


dataframe = create_dataframe()
dataframe = count_total_sales(dataframe)
print(dataframe.head())

print(platform_sales(dataframe))