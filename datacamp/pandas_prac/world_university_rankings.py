import pandas as pd

# Import Times Higher Education World University Rankings data
times_df = pd.read_csv('data/timesData.csv', thousands=",")

# Import Academic Ranking of World Universities data
shanghai_df = pd.read_csv('data/shanghaiData.csv')

# Return the first rows of `times_df`
for dataframe in times_df, shanghai_df:
	print(dataframe.head())
	print(dataframe.describe())