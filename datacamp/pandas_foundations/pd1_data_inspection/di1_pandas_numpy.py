import pandas as pd
import numpy as np

dates = list(range(1960, 2020, 10))
pop = [3034970564.0, 3684822701.0, 4436590356.0, 5282715991.0, 6115974486.0, 6924282937.0]

df = pd.DataFrame(pop, index=dates, columns=['Total Population'])
df.index.name = 'Year'
# print(df)

"""Create array of DataFrame value1s: np_vals"""
np_vals = df.values

"""Create new array of base 10 logarithm values: np_vals_log10"""
np_vals_log10 = np.log10(np_vals)

"""Create array of new DataFrame by passing df to np.log10(): df_log10"""
df_log10 = np.log10(df)

"""Print original and new csvdata containers"""
print(type(np_vals), type(np_vals_log10))
print(type(df), type(df_log10))
