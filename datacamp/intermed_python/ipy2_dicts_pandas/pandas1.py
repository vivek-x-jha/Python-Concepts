import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

my_dict = {'country': names,
           'drives_right': dr,
           'cars_per_cap': cpc}

"""Build a DataFrame cars from my_dict"""
cars = pd.DataFrame(my_dict, index=row_labels)
print(cars)
