import matplotlib.pyplot as plt
from mpl_data import (year, gdp_cap, life_exp, pop, life_exp1950, col)

"""Print the last item from year and pop"""
print(year[-1])
print(pop[-1])

"""Show a line plot: year on the x-axis, pop on the y-axis"""
plt.plot(year, pop)
plt.show()

"""Create histogram of life_exp csvdata"""
plt.hist(life_exp)
plt.show()
plt.clf()

"""Build histogram with 5 bins (default=10)"""
plt.hist(life_exp, bins=5)
plt.show()
plt.clf()
