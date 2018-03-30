import pandas as pd
# print(pd.__version__)
datafram = pd.read_csv("california_housing_train.csv")
# print(datafram.describe())
# print(datafram.head())
datafram.hist('housing_median_age')
# print(datafram.hist('housing_median_age'))