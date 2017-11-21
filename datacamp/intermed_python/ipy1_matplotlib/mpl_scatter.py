import matplotlib.pyplot as plt
import numpy as np
from data import *

"""
Plot a scatter plot: gdp_cap on the x-axis, life_exp on the y-axis
Make dots' size (s) vary with population size
Change colors (c) to match col list
Change opaqueness (alpha) to 80%
Put the x-axis on a logarithmic scale
"""

plt.scatter(x=gdp_cap, y=life_exp, s=np.array(pop) * 5, c=col, alpha=0.8)
plt.xscale('log')

"""Customization"""
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'
tick_val = [1000, 10000, 100000]  # Actual Values
tick_lab = ['1k', '10k', '100k']  # Displayed Values

"""Additional customizations"""
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

"""Add axis labels & title"""
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)

"""Adapt the ticks on the x-axis"""
plt.xticks(tick_val, tick_lab)

"""Add grid() call"""
plt.grid(True)

plt.show()
