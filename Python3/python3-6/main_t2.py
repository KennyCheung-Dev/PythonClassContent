import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close("all")


labels = ['apples', 'oranges', 'pears',
          'cherries', 'peaches', 'coconuts']
day1 = pd.Series([3, 1, 4, 1, 5, 9], index=labels)
day2 = pd.Series([2, 7, 1, 8, 2, 8], index=labels)
day3 = pd.Series([2, 6, 5, 3, 5, 3], index=labels)
d = {
    "day1": day1,
    "day2": day2,
    "day3": day3
}
df = pd.DataFrame(d)
print(df)
print(df.T)

# Transposition - swap two axis, in data manipulation
# df.T.plot()
# plt.show()
# Line Graphs represents changes over time

# Bar Graphs
# df.plot(kind="bar")
# plt.show()
# Comparing between different entries

# Box
# df.plot(kind="box")
# plt.show()
# Useful on indicating overall spreads on values

# Histograms
# df.T.plot(kind="hist")
# plt.show()
# Frequencies of some entries' appearance

# Pie
# df.plot(kind="pie", subplots=True, figsize=[15, 6])
# plt.show()

# Scatter
# df.plot(kind="scatter", subplots=True, figsize=[15, 6])
# plt.show()

# Styling - legend
# df.plot(kind="pie", subplots=True, figsize=[15, 6], legend=False)
# plt.show()

# Styling - layout
# df.plot(kind="pie", subplots=True, figsize=[15, 6], layout=(3, 1))
# plt.show()

# Styling - table
# df.plot(kind="pie", subplots=True, figsize=[15, 6], table=True)
# plt.show()

# Styling - table
df.T.plot(kind="barh", colormap="spring")
# df.plot.barh() # not recommended
plt.show()







