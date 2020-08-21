# numpy array - finished
# Pandas

# What is panda
# From the website:
# panda s is high-performance, easy to use
# data structures and dat analysis tools

# Pandas is used to process "labeled"
# and "relational" data
# thikn of data that can be represented in a table

import numpy as np
import pandas as pd

# pd.Series()
# You can make a series with different things
# such as a numpy array,
# a dictionary, or even just a single number!
# labels = ['a', 'b', 'c', 'd', 'e']
# a = pd.Series(np.array([6,7,3,9,15]), index=labels)
# print(a)

# d = {'a' : 1,
#     'b' : 2,
#     'c' : 3,
#     'd' : 4,
#     'e' : 5}
# a = pd.Series(d)
# print(a)

# labels = ['a', 'b', 'c', 'd', 'e']
# a = pd.Series(5, index=labels, name="numbers")
# print(a)

# In-Class exercise:
# Build the following data into a series:
'''
apples : 3
oranges: 1
pears: 4
cherries: 1
peaches: 5
coconuts: 9
'''

# labels = ["apple", "oranges", "pears",
#           "cherries", "peaches" ,"coconuts"]
# a = pd.Series(np.array([3,1,4,1,5,9]), index=labels)
# print(a)

# d = {
# "apples" : 3,
# "oranges" : 1,
# "pears" : 4,
# "cherries" : 1,
# "peaches" : 5,
# "coconuts" : 9
# }
# a = pd.Series(d)
# print(a)

# print(a[[0, 2, 3]])

# print(a["coconuts"])

# print("peaches" in a)


# DataFrames
# pd.DataFrame()
# d = {
#     "item" : ['a', 'b', 'c'],
#     "amount" : [1, 2, 3]
# }
# df = pd.DataFrame(d)
# print(df)



# Homework:
# build the apples, oranges amount dictionary into a DataFrame
# Also adding a second dictionaries for "Price"
# make up your numbers
# Build the two Series into a DataFrame

# d = {
#     "apples" : 3,
#     "oranges" : 1,
#     "pears" : 4,
#     "cherries" : 1,
#     "peaches" : 5,
#     "coconuts" : 9
# }
#
# price = {
#     "apples" : 7,
#     "oranges" : 2,
#     "pears" : 1,
#     "cherries" : 9,
#     "peaches" : 5,
#     "coconuts" : 78
# }
#
#
# #Answer:
# fruits = {
#     "names" : d,
#     "price" : price
# }
#
# df = pd.DataFrame(fruits)
# print(df)

#  ----------------------------------------------

# First way to create DataFrame is Through Lists
# pd.DataFrame()
# d = {
#     "item" : ['a', 'b', 'c'],
#     "amount" : [1, 2, 3]
# }
# df = pd.DataFrame(d)
# print(df)


# Second way : with Dictionaries
# d = {
#     "amounts" : {
#         "apples" : 7,
#         "oranges" : 2,
#         "pears" : 1,
#         "cherries" : 9,
#         "peaches" : 5,
#         "coconuts" : 78
#     },
#     "prices" : {
#         "apples" : 3,
#         "oranges" : 1,
#         "pears" : 4,
#         "cherries" : 1,
#         "peaches" : 5,
#         "coconuts" : 9
#     }
# }
#
# df = pd.DataFrame(d)
# print(df)


#In Class Exercise:
# Covert the following data into a DataFrame
# using the numbers 1002, 1001, 1003, 1004 as the key
# They are all series right now, (treat them as dictionary)
# names = pd.Series(['Chad', 'John', 'Andrew', 'Peter', 'Zack', 'Jaymi', 'Kenny'],
#                    index = [1001, 1002, 1003, 1004, 1005, 1006, 1007],
#                    name="Name")
# grades = pd.Series({1001:48, 1002:65, 1003:25, 1004:73, 1005:24, 1006:95, 1007:0},
#                    name="Grade")
# ism = pd.Series({1001: False, 1002: True, 1004: False, 1006: True, 1007: True},
#                 name = "isStudyingMath")
# d = {
#     "names" : names,
#     "grades" : grades,
#     "IsStudyingMath" : ism
# }
#
# df = pd.DataFrame(d)
# print(df)

# 3 ways so far to create DataFrames
# 1st - using lists
# 2nd - using Dictionaries
# 3rd - using Series

# Viewing Data in DataFrame
# df.head()   &   df.tail()
# first few   and  last few  entries

# print(df.head(3))
# print(df.tail(2))

# print(df["names"])

# Select some specific items inside
# use .loc and .iloc
# print(df.loc[1004]) # extract data with key
# print(df.iloc[0]) # extract data with index
# print(df.iloc[1:3])
# print(df)

# Sorting Data in DataFrame
# print(df.sort_index(axis=0, ascending=False))
# print(df.sort_values(by='names', ascending=False))

# Describe - High Level Statistical Summary
# print(df.describe())

# More Specific Operations
# print(df.apply(np.mean))


# ---------------

# names = pd.Series(['Chad', 'John', 'Andrew', 'Peter', 'Zack', 'Jaymi', 'Kenny'],
#                    index = [1001, 1002, 1003, 1004, 1005, 1006, 1007],
#                    name="Name")
# grades = pd.Series({1001:48, 1002:65, 1003:25, 1004:73, 1005:24, 1006:95, 1007:0},
#                    name="Grade")
# ism = pd.Series({1001: False, 1002: True, 1004: False, 1006: True, 1007: True},
#                 name = "isStudyingMath")
# d = {
#     "names" : names,
#     "grades" : grades,
#     "IsStudyingMath" : ism
# }
#
# df = pd.DataFrame(d)

labels = ['apples', 'oranges', 'pears', 'cherries', 'peaches', 'coconuts']
day1 = pd.Series([8, 4, 5, 2, 7, 1], index=labels, name="day1")
day2 = pd.Series([2, 7, 1, 8, 2, 8], index=labels, name="day2")
day3 = pd.Series([2, 6, 5, 3, 5, 3], index=labels, name="day3")

data = {
    "day1" : day1,
    "day2" : day2,
    "day3" : day3
}

df = pd.DataFrame(data)

# Add a new Column
day4 = pd.Series([8, 4, 5, 2, 7, 1], index=labels, name="day4")
df["day4"] = day4
df["day2+3"] = df["day2"] + df["day3"]

# Deleting a column
# del df["day1"]
# d3 = df.pop("day3")
# print(df)
# print(d3)

day2p5 = pd.Series([8, 4, 5, 2, 7, 1], index=labels, name="day2.5")
df.insert(2, "day2.5", day2p5)
print(df)

# Powerful function for column insertion
# df.assign()
# returns a new DataFrame instead of changing the original
# Great for method chaining
# new_df = df.assign(day2diff=df["day2"]-df["day1"])\
#     .assign(day3diff=df["day3"]-df["day2"])\
#     .assign(totalDifference=   lambda x : (x["day2diff"]+x["day3diff"])    )
# print(new_df)

# Homework:
# 1) Get Familiar with using assign lambda
# 2) Create a totalAmount from adding (day1, day2, day3) - (totalDifference)
# can be done in 2 assigns (having middle step in day1+day2+day3
# or can be done in 1 assigns

new_df = df.assign(day2diff=df["day2"]-df["day1"])\
    .assign(day3diff=df["day3"]-df["day2"])\
    .assign(totalDifference=   lambda x : (x["day2diff"]+x["day3diff"]))\
    .assign(day123 = df["day1"] + df["day2"] + df["day3"])\
    .assign(totalAmount= lambda x: (x["day123"] - x["totalDifference"]))

    # lambda(x):
    #     return x["day2diff"]+x["day3diff"]

print(new_df)










