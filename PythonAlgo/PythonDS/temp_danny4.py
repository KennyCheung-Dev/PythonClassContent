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

dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5
}
a = pd.Series(dict)
print(a)

# dict = {
#     'Hamburger' : { 'Name' : 'Ultimatum', 'price' : 20 }
# }

# 233