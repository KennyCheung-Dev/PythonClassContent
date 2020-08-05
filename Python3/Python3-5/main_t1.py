import numpy as np
import pandas as pd


# Panda is used to process "labeled" and "relational" data
# A set of data may represent a set of  objects that have
# identifiable properties
# (e.g. a student may have name, age, grade, classes enrolled)
# This is often how data is represented in the real world & in databases
# Panda makes it easier for us to handle & visualize this type of
# relational data, instead of  only working with one simply
# array of numbers like we did before in numpy array

'''
StudentNumber:   Name:   Score
1001             Chad     10
1002             Kenny    2
1003             Peter    89
'''

# Panda uses the numpy array as a basis for its own data structure
# We ll still be using np.array after

# Fundamental data type in pandas, just like arrays in numpy

# pd.Series
# You can make a series with different things such as a numpy array
# a dictionary (dict), even just a single number
# a = pd.Series(np.array([1, 2, 3, 4, 5]))
# print(a)
# labels = ['Chad', 'Kenny', 'Peter', 'John', 'Andrew']
# a = pd.Series(np.array([100, 78, 98, 88, 97]), index=labels)
# print(a)

# Creating a panda Series with a dictionary
# d = {'chad' : 1000,
#         'zack' : {'car' : "lamborghini",
#                   'house' : "huge"},
#         'Kenny' : 5}
#
# dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
# a = pd.Series(d)
# print(a)

#Create Pandas series with just one number
# labels = ['Chad', 'Kenny', 'Peter', 'John', 'Andrew']
# a = pd.Series(100, index=labels)
# print(a)

# Optional argument name: Gives your Series a name
# Series.rename() to rename
# labels = ['Chad', 'Kenny', 'Peter', 'John', 'Andrew']
# a = pd.Series(100, index=labels, name = "Exam Score")
# print(a)
# a = a.rename("Exam Score Out Of 100")
# print(a)

# In-Class exercise:
# 1. convert the following data into a series,
# using the first column as labels
'''
apples   3
oranges  1
pears    4
cherries 1
peaches  5
chestnuts9
'''

dict = {
    'apples' : 3,
    'oranges' : 1,
    'pears' : 4,
    'cherries' : 1,
    'peaches' : 5,
    'chestnuts' : 9
}
a = pd.Series(dict, name="FruitsIEatInAMinute")
print(a)

#Accessing values just like before
# print(a['oranges'])
# print(a[0])
# print(a[::2])
# print(a[[0, 2, 5]])

# Represents a dict of Series objects as
# Spreadsheets / table
# # pd.DataFrame()
# d = {"item" : ["a", "b", "C"],
#      "amount" : [1, 2, 3]}
# df = pd.DataFrame(d)
# print(df)

d = {
    "item" : {
        'a' : 'apples',
        'b' : 'oranges',
        'c' : 'pears'
    },
    "amount" : {
        'b' : 1,
        'c' : 2,
        'd' : 3
    }
}

# df = pd.DataFrame(d)
# print(df)

#Optional parameters : index columns
# lets you specify the exact row and column headers you want
# in the exact order you give

# df = pd.DataFrame(d)
# print(df)

# In-Class / Homework:
# 1. Conver the following data into a DataFrame
# using the first row/column as labels
names = pd.Series(['Chad', 'John', 'Andrew', 'Peter', 'Zack', 'Jaymi'],
                   index = [1001, 1002, 1003, 1004, 1005, 1006, 1007],
                   name="Name")
grades = pd.Series({1001:65, 1002:93, 1003:72, 1005:87, 1006:79, 1007:53},
                   name="Grade")
ism = pd.Series({1001: False, 1002: True, 1004: False, 1006: True, 1007: True},
                name = "isStudyingMath")






