import pandas as pd
import matplotlib.pyplot as plt
from size import sizes

df = pd.read_csv('cars.csv')

"""Generate a scatter plot"""
df.plot(kind='scatter', x='hp', y='mpg', s=sizes)
plt.title('Fuel efficiency vs Horse-power')
plt.xlabel('Horse-power')
plt.ylabel('Fuel efficiency (mpg)')
plt.show()

"""Generate the box plots of weight and mpg"""
df[['weight', 'mpg']].plot(kind='box', subplots=True)
plt.show()
