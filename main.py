from kaggle.kaggle_read import *
from analytic.services import *


dataframe = create_dataframe()
# dataframe = count_total_sales(dataframe)
# dataframe = sales_percentage(dataframe)
dataframe = create_total_sales_dataframe(dataframe)
print(dataframe)