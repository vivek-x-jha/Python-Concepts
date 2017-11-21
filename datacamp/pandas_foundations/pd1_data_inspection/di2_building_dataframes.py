import pandas as pd

"""Build a DataFrame via a zipped list"""
a = [1980, 1981, 1982]
b = ['Blondie', 'Chistorpher Cross', 'Joan Jett']
c = ['Call Me', 'Arthurs Theme', 'I Love Rock and Roll']
d = [6, 3, 7]
col_labels = ['year', 'artist', 'song', 'chart weeks']

li_df = pd.DataFrame(list(zip(a, b, c, d)), columns=col_labels)
print(li_df)

"""Build and inspect a DataFrame via a zipped dictionary"""
col_keys = ['Country', 'Total']
col_values = [['United States', 'Soviet Union', 'United Kingdom'], [1118, 473, 273]]

dic_df = pd.DataFrame(dict(zip(col_keys, col_values)))
print(dic_df)

"""Building DataFrames with Broadcasting"""
dic_df['Planet'] = 'Earth'
print(dic_df)
