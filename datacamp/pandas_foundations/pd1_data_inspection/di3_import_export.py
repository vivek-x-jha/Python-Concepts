import pandas as pd

new_labels = ['year', 'population']

df1 = pd.read_csv('world_population.csv')
df2 = pd.read_csv('world_population.csv', header=0, names=new_labels)

print(df1)
print(df2)

df3 = pd.read_csv('messy_stock_data.tsv')
print(df3.head())

df4 = pd.read_csv('messy_stock_data.tsv', delimiter=' ', header=3, comment='#')
print(df4.head())

df4.to_csv('tmp_clean_stock_data.csv', index=False)
df4.to_excel('file_clean.xlsx', index=False)
