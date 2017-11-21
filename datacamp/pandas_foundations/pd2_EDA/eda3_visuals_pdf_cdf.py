import pandas as pd
import matplotlib.pyplot as plt

tips = pd.read_csv('tips.csv', delim_whitespace=True)

"""Plots the PDF and CDF of "fraction""""
fig, axes = plt.subplots(nrows=2, ncols=1)  # Formats the plots such that they appear on separate rows

tips.fraction.plot(ax=axes[0], kind='hist', normed=True, bins=30, range=(0, .3))
tips.fraction.plot(ax=axes[1], kind='hist', normed=True, cumulative=True, bins=30, range=(0, .3))

plt.show()
