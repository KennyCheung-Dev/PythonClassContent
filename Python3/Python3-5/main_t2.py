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

d = {
    "apples" : 3,
    "oranges" : 1,
    "pears" : 4,
    "cherries" : 1,
    "peaches" : 5,
    "coconuts" : 9
}

price = {
    "apples" : 7,
    "oranges" : 2,
    "pears" : 1,
    "cherries" : 9,
    "peaches" : 5,
    "coconuts" : 78
}


#Answer:
fruits = {
    "names" : d,
    "price" : price
}

df = pd.DataFrame(fruits)
print(df)














