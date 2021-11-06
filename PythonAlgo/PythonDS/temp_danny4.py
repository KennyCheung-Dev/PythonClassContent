
# Introduction to pandas & its relation to numpy
# Series, DataFrame (creation, viewing data, selection)
# Statistical operations on a DataFrame

# From their website:
# "Pandas is an open source, BSD-licensed library providing
# high-performance, ease-to-use data structures and
# data analysis tools for the Python programming language.

#The leading Python data science library to manipulate data with
# Also has some visualization features built on top of matplotlib!

# Why do we want to learn panda?
# Pandas is used to process "labeled" and "relational"  data
# A set of data may represent a set of objects that have identifiable properties
# (e.g. a student may have name, age, grade, classes enrolled):
# think of data that can be represented in a table!
# This is often how data is represented in the real world &
# in databases/data sets
# Pandas makes it easier for us to handle & visualize this type of
# relational data, instead of only working with one simple
# array of numbers like we did before

# Panda uses the numpy array as a basis for its own data structures
# (many python libraries do!)
# You can use a lot of the knowledge from last class about
# how to handle numpy arrays for handling pands adata as well!
# The visualization component of the pandas library is built on top of
# matplotlib, and you can also directly use matplotlib with pandas data
# for more advanced data visualization!


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pd.Series
# You can make a series with different things such as a numpy array,
# a dict, or even just a single number

# numpy array
# a = pd.Series(np.array([2, 5, 8, 11, 14]))
# print(a)

# list
# a = pd.Series([2, 4, 6, 8, 10])
# print(a)

# range
# a = pd.Series(range(0, 10, 2))
# print(a)

# Single number
# a = pd.Series(10)
# print(a)

# dict = {
#     'a' : 1,
#     'b' : 2,
#     'c' : 3,
#     'd' : 4,
#     'e' : 5
# }
# a = pd.Series(dict)
# print(a)

# dict = {
#     'Hamburger' : { 'Name' : 'Ultimatum', 'price' : 20 }
# }

#Creating a Series from a singular scalar value
# labels = ['a', 'b', 'c', 'd', 'e']
# a = pd.Series(100, index=labels)
# print(a)

#Giving a name to a series
# a = pd.Series(np.array([6, 7, 8, 9, 10]), name="prices")
# print(a.name)
# a.name = "world"
# print(a.name)

#In-Class exericse: (20)
# Creating the following data into a series:
# Apple    :    3
# Oranges  :    1
# Pears    :    3
# Cherries :    1
# Peaches  :    5
# Coconuts :    9

#2nd Approach
# amounts = [3, 1, 4, 1, 5, 9]
# labels = ["Apple", "Oranges", "Pears", "Cherries", "Peaches", "Coconuts"]
# a = pd.Series(amounts, index=labels, name = "Fruits")
# print(a)

#Series Operations - list-like
# amounts = [3, 1, 4, 1, 5, 9]
# labels = ["Apple", "Oranges", "Pears", "Cherries", "Peaches", "Coconuts"]
# a = pd.Series(amounts, index=labels, name = "Fruits")

#Index operations on series
# print(a[0])
# print(a[::2])
# print(a[[0, 2, 3]])

#Extract list/arrays from series
# print(a.array)
# print(a.to_numpy())

#Series Operations - dict-like
# amounts = [3, 1, 4, 1, 5, 9]
# labels = ["Apple", "Oranges", "Pears", "Cherries", "Peaches", "Coconuts"]
# a = pd.Series(amounts, index=labels, name = "Fruits")

# print(a['Apple'])
# print('Apple' in a)
#Check if 6 is in the series values
# print(6 in a.values)
# print(1 in a.values)
# print(6 in a.to_numpy())

# In-class exercise:
# Build a dictionary of animals and their numbers
# Build a panda Series with it
# Extract only the 2nd and 4th entry in the Series
# Turn it in to an numpy array and print

# [19, 18, 17]       # Numpy_Array
# [price: 19, beforeTax: 18, employeeDiscount: 17]   # Series
# Data Frame
'''
McDonald Prices : {    
                    BigMac : { price: 19, beforeTax: 18, employeeDiscount: 17},
                    ChickenNuggets : { price: 1200, beforeTax: 120, employeeDiscount: 1.2}, / chicken
                    ChickenNugget : { price: 12000, beforeTax: 12, employeeDiscount: 0}, #one chicken nugget
                  }
'''

# pd.DataFrame()
# Create dataframes from lists, dicts, Series

# Dictionary
# d = { "item" : ["a", "b", "c"], "amount" : [1, 2, 3]}
# df = pd.DataFrame(d)
# print(df)

# Options: index and columns
# d = { "item" : ["a", "b", "c"], "amount" : [1, 2, 3]}
# df = pd.DataFrame(d, index=['e', 'f', 'g'], columns=['item', 'price', 'amount'])
# print(df)


'''
Create a dataframe from these: (30)
     Name    Scores   Grade   IsBadMath
0    Danny   2        A       False
1    Kenny   100      SSS     True
2    Rax     35       S       False
'''

# names = pd.Series(['Danny', 'Kenny', 'Rx-8'], index=[0, 1, 30])
# scores = pd.Series([0.02, 100, 35], index=[0, 1, 30])
# grades = pd.Series(['A', 'SSS', 'S'], index=[0, 1, 30])
# isBadMath = pd.Series([False, True, False], index=[0, 1, 30])

# data = {
#     "Names" : names,
#     "Scores" : scores,
#     "Grades" : grades,
#     "Is Bad at Math" : isBadMath
# }

# df = pd.DataFrame(data)
# print(df)

# head and tail gives you the first or last specified amount of entries
# print(df.head(1))
# print(df.tail(1))

# Get a certain column by ['Column name']
# print(df[['Names', 'Grades']])

# Retrieve entry by location and index location
# print()
# print(df.loc[30`]`)
# print()
# print(df.iloc[2])

# Slice df
# print(df.loc[0:30])
# print(df[0:1])

# In-Class exercise
# Retrieve from Kenny to Rx-8, Only Score to Grades column (40)

#Sort by values
# print(df.sort_values(by='Names', ascending=False))

# Get a high-level statistical summary on your data
# print(df.describe())

# Apply Functions on a DataFrame
# df.apply() :
# print(df.apply(np.cumsum))

# Adding columns after dataframe has been defined
# att = pd.Series([9000000000, 100, 75], index=[0, 1, 30])
# df['Attack'] = att

# Create new columns with existing columns
# Defense = Attack * Scores
# scores = df["Scores"]
# attack = df["Attack"]
# defense = scores * attack
# df["Defense"] = defense
# print(df)

# Delete columns:
# del df["Is Bad at Math"]
# deletedColumn = df.pop("Is Bad at Math")
# print(df)
# print(deletedColumn)

# Insert column
# speed = pd.Series([2001, 100, 2000], index=[0, 1, 30])
# df.insert(4, "Speed", speed)
# print(df)

# df.assign() a more powerful function for column insertion
# Returns a DataFrame (great for method chaining)
# newDf = df.assign(Stupidity=df["Scores"] / df["Speed"]).assign(Size=df["Defense"] / df["Speed"])
# print(newDf)

# pd.concat() : concatenate given DataFrames together
# along either axes
# Does not look at labels/indexes
# (if two Dataframes share some labels/indices, they'll both get included
# pieces = [newDf["Names"], newDf["Stupidity"], newDf["Defense"]]
# reordered = pd.concat(pieces)
# print(reordered)

# append DataFrame onto Dataframe!
# Create a dataframe of 1 entry (1 person)

# print(newDf.columns)
# 'Names', 'Scores', 'Grades', 'Attack', 'Speed', 'Defense', 'Stupidity', 'Size'
# ReddyData = {
#     "Names" : pd.Series({"60" : "Reddy"}),
#     "Scores" : pd.Series({"60" : 0}),
#     "Grades" : pd.Series({"60" : "F"}),
#     "Attack" : pd.Series({"60" : 20}),
#     "Speed" : pd.Series({"60" : 5000}),
#     "Defense" : pd.Series({"60" : 600000}),
#     "Stupidity" : pd.Series({"60" : 0}),
#     "NumberOfFins" : pd.Series({"60" : 17}),
# }

# reddyDF = pd.DataFrame(ReddyData)
# appended_df = newDf.append(reddyDF)
# print(appended_df)

#In-class exercise:
# Add a new entry, (new fish/person)
# appended_df.loc[1, "NumberOfFins"] = 20
# appended_df.loc[30, "NumberOfFins"] = 79
# print(appended_df["NumberOfFins"])

# 633

# Plot the Dataframe!
# plt.figure()
# df.plot()
# plt.show()

# plt.figure()
# appended_df.plot()
# plt.show()


labels = ["apples", "oranges", "pears", "cherries", "peaches", "coconuts"]
day1 = pd.Series([3, 1, 4, 1, 5, 8], index=labels)
day2 = pd.Series([2, 7, 1, 8, 2, 8], index=labels)
day3 = pd.Series([2, 6, 5, 3, 5, 3], index=labels)
d = { "day1":day1, "day2":day2, "day3":day3}
df = pd.DataFrame(d)
print(df)

# Default Line Graph
# df.plot()


# Reversing Axis
# df.T is what we want (Transposed)
print(df.T)
# df.T.plot()

# Box Graph
# df.T.plot(kind="box")

# Hist Graph
# df.T.plot(kind="hist")
# df.T.plot(kind="hist", subplots=True)

# Pie Graph
# df.plot(kind="pie", subplots=True, figsize=[15, 6], layout=(2, 2))

# bar Graph
# df.T.plot.bar()
# df.plot.barh()

# Legend
# df.plot(kind="pie", subplots=True, figsize=[15, 6], layout=(2, 2), legend=False)

# Table
# df.plot(kind="pie", subplots=True, figsize=[15, 6], layout=(2, 2), legend=False, table=True)

# Draw the plots
# plt.show()