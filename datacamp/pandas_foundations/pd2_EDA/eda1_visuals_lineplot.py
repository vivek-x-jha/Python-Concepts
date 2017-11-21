import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('stocks.csv', header=0, index_col=0)

"""Generate a line plot of AAPL and IBM"""
df.plot(y=['AAPL', 'IBM'])
plt.title('Monthly stock prices')
plt.ylabel('Price ($US)')
plt.show()
