# Introduction to pandas & its relation to numpy
# Series, DataFrame (creation, viewing data, selection)
# Statistical operations on a DataFrame

# From their website:
# "Pandas is an open source, BSD-licensed library providing
# high-performance, eas-to-use data structures and
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

# The fundamental data type in  pandas, nust like arrays in numpy
# Similar to a numpy array, a pandas Series represents a one-dimensional
# array of data that can have axis labels

# pd.Series
# You can make a series with different things such as a numpy array,
# a dict, or even just a single number!

# # numpy array
# a = pd.Series(np.array([1, 2, 3, 4, 5]))
# print(a)
#
# # list
# b = pd.Series([1, 2, 3, 4, 5])
# print(b)
#
# # range
# c = pd.Series(range(5))
# print(c)
#
# # list from range
# d = pd.Series(list(range(5)))
# print(d)
#
# # Single number
# e = pd.Series(10)
# print(e)

# If a dictionary is used to create a Series,
# then the keys are automatically assigned as the labels/indices
# d = {
#     'a' : 1,
#     'b' : 2,
#     'c' : 3,
#     'd' : 4,
#     'e' : 5
# }
# a = pd.Series(d)
# print(a)

# Creating a Series from a single scalar value
# If a single scalar value (number) is used to create a series,
# then the index must be given, and the resulting Series will be
# the same length as index, with all values populated to
# the given scalar value.
# labels = ['a', 'b', 'c', 'd', 'e']
# a = pd.Series(100, index=labels)
# print(a)

# Naming a Series
# Optional argument name: Gives your Series a name
# Use Series.rename(newname) to rename a series
# a = pd.Series(np.array([6,7,8,9,0]), name="hello")
# print(a.name)
# a.rename("world")
# print(a.name)

# In-Class exercise:
# Create the following data into a series:
# Apples   :   3
# Oranges  :   1
# Pears    :   4
# Cherries :   1
# Peaches  :   5
# Coconuts :   9

# Answer:

# 1st approach
# amounts = [3, 1, 4, 1, 5, 9]
# labels = ["Apples", "Oranges", "Pears", "Cherries", "Peaches", "Coconuts"]
# a = pd.Series(amounts, index = labels, name = "Fruits")
# print(a)

# 2nd Approach : Use a dictionary
# amounts = {"Apples" : 3,
#            "Oranges" : 1,
#           "Pears" : 4,
#           "Cherries" : 1,
#           "Peaches" : 5,
#           "Coconuts" : 9}
# a = pd.Series(amounts, name="Amounts")
# print(a)

# Series Operations - array-like
# Much of operations work the same way as with numpy arrays
# and you can directly use many numpy array functions
# on panda Series.
# Slicing works the same way, and will grab the label/index
# for that element as well
# labels = ['a', 'b', 'c', 'd', 'e']
# a = pd.Series(np.array([6, 7, 8, 9, 0]),  index = labels)
# print(a[0]) # Using index
# print(a[::2]) # Operations
# print(a[[0, 2, 3]])
# Use a.array to grab only the values in a Series,
# and a.to_numpy() to grab the values as an actual numpy array
# print(a.array)
# print(a.to_numpy())

# Dict-Like
# Since each element also has a label, Series are similar to dicts as well
# Use a label to index into a Series the same way you would with dicts
# labels = ['a', 'b', 'c', 'd', 'e']
# a = pd.Series(np.array([6, 7, 8, 9, 0]),  index = labels)
# print(a['a'])
# print('b' in a)
# print('f' in a)
# print(6 in a.values)
# print(1 in a.values)
# print(6 in a.to_numpy())
# print(a.to_numpy()[0])

#In-Class exercise:
# Build a dictionary of animals and their numbers
# Build a panda Series with it
# Extract only the 2nd and 4th entry in the Series
# Turn it into a numpy array and print
# animals = {'mice' : 2,
#            'cats' : 4,
#            'dogs' : 5,
#            'birds': 12,
#            'ants' : 12345678911131517192}  # <- limit
# a = pd.Series(animals, name="animals")
# print(a[1::2].to_numpy())



# DataFrame
# The other fundamental object type in pandas, and
# probably the one you'll be using the most
# Represents a dict of Series objects, or you can
# think of them as a spreadsheet/table
# Basically an object that groups a bunch of Series together,
# with each one of them identified by a name/key

# pd.DataFrame()
# The function we use to create DataFrames,
# from a variety of different types of inputs,
# with the simplest being a dict of one-dimensional ndarrays,
# lists, dicts, or Series
# d = {"item": ["a", "b", "c"], "amount": [1, 2, 3]}
# df = pd.DataFrame(d)
# print(df)

# Optional Parameters
# Optional parameter index and columns let you specify the
# the exact row and column headers you want in the exact order
# you give
# If the labels alraedy exist in the data given (the keys
# of the dict for columns and the labels/keys in the Series/dict
# then the values are kept; If no data available, fill with NaN
# If the label doesn't get selected, then the data is not included
# d = {"item" : {'a' : 'apples', 'b' : 'oranges', 'c' : 'pears'},
#      "amount" : {'a' : 1, 'b' : 3, 'c' : 3}}
# df = pd.DataFrame(d, index=['b', 'c', 'a'], columns=['item', 'price'])
# print(df)

#What if the dicts/Series in the input don't have
# the same set of labels?
# d = {"item" : {'a' : 'apples', 'b' : 'oranges', 'c' : 'pears'},
#      "amount" : {'b' : 2, 'c' : 3, 'd' : 4}}
# df = pd.DataFrame(d)
# print(df)
# Panda takes the UNION of the sets of labels: keeping every
# single unique key, filling with NaN for nonxistent elements

#In-Class exercise:
# Convert the following data into a dataFrame,
# using the first row/column as labels.
# d = {"Name" : {1001 : 'Jeff', 1002 : 'Annie', 1003 : 'Brita',
#                1004 : 'Troy', 1005 : 'Abed', 1006 : 'Shirley',
#                1007 : 'Pierce'},
#      "Grade" : {1001 : 65, 1002 : 93, 1003 : 72,
#                 1004 : 87, 1005 : 87, 1006 : 79, 1007 : 53},
#      "IsStudyingMath" : {1001 : False, 1002 : True, 1004 : False,
#                          1006 : True, 1007 : True}}
# df = pd.DataFrame(d)
# print(df)

# Another solution:
# names = pd.Series(['Jeff', 'Annie', 'Brita', 'Troy', 'Abed',
#                    'Shirley', 'Pierce'],
#                   index = [1001, 1002, 1003, 1004, 1005, 1006, 1007],
#                   name = "Name")
# grades = pd.Series({1001:65, 1002:93, 1003:72, 1005:87, 1006:79, 1007:53},
#                    name = "Grade")
# ism = pd.Series({1001:False, 1002:True, 1004:False, 1006:True, 1007:True},
#                    name = "IsStudyingMath")
# data = {"name" : names,
#         "grade": grades,
#         "is_studying_math": ism}
# df = pd.DataFrame(data)
# print(df)

# Viewing Data in a DataFrame
# df.head() & df.tail() gives you the first or last 5 (or however
# many you want) rows of your DataFrame
# d = {"Name" : {1001 : 'Jeff', 1002 : 'Annie', 1003 : 'Brita',
#                1004 : 'Troy', 1005 : 'Abed', 1006 : 'Shirley',
#                1007 : 'Pierce'},
#      "Grade" : {1001 : 65, 1002 : 93, 1003 : 72,
#                 1004 : 87, 1005 : 87, 1006 : 79, 1007 : 53},
#      "IsStudyingMath" : {1001 : False, 1002 : True, 1004 : False,
#                          1006 : True, 1007 : True}}
# df = pd.DataFrame(d)
# print(df.head())
# print(df.tail(2))

# Selecting Data from a DataFrame
# Since DataFrames are really just large dictionaries,
# we can index & slice into them similarly using the
# same syntax as  regular dicts with their labels
# Indexing with only one label gives you the column with that label
# d = {"item" : pd.Series(['apples', 'oranges', 'pears',
#                          'cherries', 'oears', 'coconuts'],
#                         index = ['a', 'b', 'c', 'd', 'e', 'f']),
#      "amount" : pd.Series([3, 1, 4, 1, 5, 9],
#                           index = ['a', 'b', 'c', 'd', 'e', 'f'])}
# df = pd.DataFrame(d)
# print(df["item"]) # <- only 1 column

# Selecting
# To select rows, use df.loc and df.iloc
# for label and numeric location selection respectively
# These can be used to slice as well!
# d = {"item" : pd.Series(['apples', 'oranges', 'pears',
#                          'cherries', 'oears', 'coconuts'],
#                         index = ['a', 'b', 'c', 'd', 'e', 'f']),
#      "amount" : pd.Series([3, 1, 4, 1, 5, 9],
#                           index = ['a', 'b', 'c', 'd', 'e', 'f'])}
# df = pd.DataFrame(d)
# print(df.loc['a'])
# print(df.iloc[4])
# print(df.loc['c':'e'])
# # Row slicing directly is also available
# print(df['b':'d'])
# print(df[3:5])

# In-Class Exercise:
# Using the DataFrame we created earlier,
# Retrieve the names and grades for the students with IDs 1002 and 1006
# Answer:
# d = {"Name" : {1001 : 'Jeff', 1002 : 'Annie', 1003 : 'Brita',
#                1004 : 'Troy', 1005 : 'Abed', 1006 : 'Shirley',
#                1007 : 'Pierce'},
#      "Grade" : {1001 : 65, 1002 : 93, 1003 : 72,
#                 1004 : 87, 1005 : 87, 1006 : 79, 1007 : 53},
#      "IsStudyingMath" : {1001 : False, 1002 : True, 1004 : False,
#                          1006 : True, 1007 : True}}
# df = pd.DataFrame(d)
# print(df[['Name', 'Grade']].loc[[1002, 1006]])

# Sorting Data in a DataFrame
# We can easily sort data (along with their labels)
# in a DataFrame
# df.sort_index(): sorts data by indices/labels
# Hint: Axis 0 = row labels, axis 1 = column labels
# d = {"item" : pd.Series(['apples', 'oranges', 'pears',
#                          'cherries', 'oears', 'coconuts'],
#                         index = ['a', 'b', 'c', 'd', 'e', 'f']),
#      "amount" : pd.Series([3, 1, 4, 1, 5, 9],
#                           index = ['a', 'b', 'c', 'd', 'e', 'f'])}
# df = pd.DataFrame(d)
# print(df.sort_index(axis=1, ascending=True)) # <- only 0 or 1
#
# # df.sort_values(): sorts data by values in a column
# print(df.sort_values(by='amount'))

# In-Class exercise:
# Sort the DataFrame we created by student name in descending order
# d = {"Name" : {1001 : 'Jeff', 1002 : 'Annie', 1003 : 'Brita',
#                1004 : 'Troy', 1005 : 'Abed', 1006 : 'Shirley',
#                1007 : 'Pierce'},
#      "Grade" : {1001 : 65, 1002 : 93, 1003 : 72,
#                 1004 : 87, 1005 : 87, 1006 : 79, 1007 : 53},
#      "IsStudyingMath" : {1001 : False, 1002 : True, 1004 : False,
#                          1006 : True, 1007 : True}}
# df = pd.DataFrame(d)
# print(df.sort_values(by='Name', ascending = False))

# df.describe(): gives you a high-level statistical summary
# of the data in your DataFrame
# d = {"item" : pd.Series(['apples', 'oranges', 'pears',
#                          'cherries', 'pears', 'coconuts'],
#                         index = ['a', 'b', 'c', 'd', 'e', 'f']),
#      "amount" : pd.Series([3, 1, 4, 1, 5, 9],
#                           index = ['a', 'b', 'c', 'd', 'e', 'f'])}
# df = pd.DataFrame(d)
# print(df.describe())

# Applying Functions on a DataFrame
# df.apply(): gives a function, applies it to each row/column
# in the DataFrame/
# labels = ['apples', 'oranges', 'pears', 'cherries',
#           'peaches', 'coconuts']
# amounts = pd.Series([3, 1, 4, 1, 5, 9], index = labels)
# df = pd.DataFrame({"amount" : amounts})
# print(df.apply(np.sum))

#Summary of Today's Lesson
# Introduction to Pandas & its relation to Numpy
# pd.Series introduction, creation, operations
# pd.DataFrame introduction, creation, dataviewing, data selection,.
# data sorting
# Simple statistical information from DataFrame
# Applying functions on a DataFrame

# Next Lesson:
# DataFrame modification & merging, pivot tables, plotting





