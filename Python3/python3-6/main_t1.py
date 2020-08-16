import numpy as np
import pandas as pd

# DataFrame Modification

day1 = {
    'apples' : 3,
    'oranges' : 1,
    'pears' : 4,
    'cherries' : 1,
    'peaches' : 5,
    'chestnuts' : 9
}
day2 = {
    'apples' : 2,
    'oranges' : 7,
    'pears' : 1,
    'cherries' : 8,
    'peaches' : 2,
    'chestnuts' : 8
}
day3 = {
    'apples' : 2,
    'oranges' : 6,
    'pears' : 5,
    'cherries' : 3,
    'peaches' : 3,
    'chestnuts' : 3
}
dfData = {
    "day1" : day1,
    "day2" : day2,
    "day3" : day3
}
df = pd.DataFrame(dfData)
# print(df)

labels = ['apples', 'oranges', 'pears',
          'cherries', 'peaches', 'chestnuts']
day4 = pd.Series([8, 4, 5, 2, 7, 1], index=labels)

# add day4
df["day4"] = day4

# add day1 and day2
df["day1+2"] = df["day1"] + df["day2"]

# Delete day1
# del df["day1"]
d3 = df.pop("day3")

# print(df)
# print(d3)

df.insert(2, "day3", d3)
print(df)

# df.assign(): a more powerful function  for column insertion
# Returns a new DataFrame intead of changing the original
# great for method chaining)
# new_df = df.assign(day2diff = df["day2"] - df["day1"])\
#     .assign(day3diff = df["day3"] - df["day2"])\
#     .assign(totalDiff = lambda x: (x["day2diff"] + x["day3diff"]))
# print(new_df)

# Homework:
# Use Assign to add a "Price" column, and immediately
# in the second layer, use the price column and day1 column
# To calculate the day1Profit
# Profit = price * amount
# 2 layers of assign()
# Make up the price yourself

# df.assign(Add Price in).assign(price * day1)

#Answer:
new_df = df.assign(day2diff = df["day2"] - df["day1"])\
    .assign(day3diff = df["day3"] - df["day2"])\
    .assign(totalDiff = lambda x: (x["day2diff"] + x["day3diff"]))\
    .assign(price = pd.Series([8, 4, 5, 2, 7, 1], index=labels))\
    .assign(Profit=lambda x: (x["price"] * x["totalDiff"]))


print(new_df)