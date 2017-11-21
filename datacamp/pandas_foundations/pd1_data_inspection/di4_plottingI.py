import pandas as pd
import matplotlib.pyplot as plt
from data import temp

df = pd.DataFrame(temp, columns=['Temperature (degrees F)'])

"""Plot Customizations"""
df.plot(c='red', title='Temperature in Austin')
plt.xlabel('Hours since midnight August 1, 2010')
plt.ylabel('Temperature (degrees F)')
plt.show()
