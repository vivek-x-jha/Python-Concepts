import pandas as pd

"""Import the cars.csv csvdata: cars"""
cars = pd.read_csv('cars.csv', index_col=0)
print(cars)

"""Print out country column as Pandas Series"""
print(cars['country'])

"""Print out country column as Pandas DataFrame"""
print(cars[['country']])

"""Print out DataFrame with country and drives_right columns"""
print(cars[['country', 'drives_right']])

"""Print out first 3 observations"""
print(cars[:3])

"""Print out fourth, fifth and sixth observation"""
print(cars[3:6])

"""Print out observations for Australia and Egypt using iloc"""
print(cars.iloc[[1, 6]])

"""Print out observation for Japan using loc"""
print(cars.loc[['JAP']])

"""Print out single cell: drives_right value of Morocco"""
print(cars.loc[['MOR'], ['drives_right']])

"""Print out sub-DataFrame, containing obsv for Russia and Morocco and the columns country and drives_right"""
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

"""Print out drives_right column as Series"""
print(cars.loc[:, 'drives_right'])

"""Print out drives_right column as DataFrame"""
print(cars.loc[:, ['drives_right']])

"""Print out cars_per_cap and drives_right as DataFrame"""
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
