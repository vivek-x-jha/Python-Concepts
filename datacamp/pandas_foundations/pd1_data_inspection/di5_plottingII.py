import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('temp_data.csv', header=0)
df.plot()
plt.show()

"""Plot all columns as subplots"""
df.plot(subplots=True)
plt.show()

"""Plot just the Dew Point csvdata"""
df[['Dew Point (deg F)']].plot()
plt.show()

"""Plot the Dew Point and Temperature csvdata, but not the Pressure csvdata"""
df[['Temperature (deg F)', 'Dew Point (deg F)']].plot()
plt.show()
