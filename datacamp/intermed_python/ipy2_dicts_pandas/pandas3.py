import pandas as pd
import numpy as np
cars = pd.read_csv('cars.csv', index_col=0)

"""Extract drives_right column as Series and use it to subset cars"""
sel = cars[cars['drives_right']]
# print(sel)

"""Create car_maniac: observations that have a cars_per_cap over 500"""
cpc = cars['cars_per_cap']
car_maniac = cars[cpc > 500]
# print(car_maniac)

"""Create medium: observations with cars_per_cap between 100 and 500"""
between = np.logical_and(cpc > 100, cpc < 500)
print(cars[between])

"""Iterate over rows of cars"""
for lab, row in cars.iterrows():
    print(lab)
    print(row)

"""Output should be in the form "country: cars_per_cap""""
for lab, row in cars.iterrows():
    print('{}: {}'.format(lab, row['cars_per_cap']))

"""Add column 'COUNTRY' using for loop & .iterrows()"""
for lab, row in cars.iterrows():
    cars.loc[lab, 'COUNTRY'] = row['country'].upper()
print(cars)

"""More efficient to use .apply() instead of for/.iterrows() since prior way creates a new panda series each time"""
cars['COUNTRY'] = cars['country'].apply(str.upper)
