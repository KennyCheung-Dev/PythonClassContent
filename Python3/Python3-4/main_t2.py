'''
Arrays : List of things
Limitations:
- You have define max size of the array at start
- Arrays have types

Numpy array is different, none of the above limitation applies

What do we use numpy arrays for?
To store and manipulate data in memory so we can do work on it
Add, Modify, Remove, Sort, Compare, Analytical operations
Arithmetic Operations
'''

import numpy as np

#Create a numpy array
# np.array
# a = np.array([])
# print(a)

# b = np.array([1, 2, 3])
# print(b)

# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(a)

# b = np.array([[0, 1], [2, 3]])
# print(b)

# a = np.array([[0, 1], [2, 3], [4, 5]])
# print(a)

# a = np.array(range(0, 1000))
# # 0, 1, 2, 3, 4, 5, ... 999
# b = a.reshape([500, 2])
# print(b)

#In-Class exercise
# Use Reshape
# [[1 2]
#  [3 4]
#  [5 6]]

# 1, 2, 3, 4, 5, 6

# a = np.arange(2, 22, 5)
# b = np.linspace(0, 9, 19)
# print(a)

# In-Class Exercise:
# 0, 0.25, 0.5, 0.75, .... 2

# random
# A few ways to make randomized arrays
# a = np.random.random(1000) * 5 + 10

# b = np.random.randint(10, 15, 1000)
# print(b)

# 0 - 1
# 0 - 5
# 10 - 15

# Zeroes, ones, identity, diag
# a = np.zeros(200)
# print(a)
# a = np.ones(100)
# print(a)
# a = np.identity(20)
# print(a)
# a = np.diag([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(a)

# Accessing
# indexing and slicing
# a = np.array([3, 1, 4, 1, 5])
# print(a)
# print(a[0])
# print(a[-1])
# # [1 4]
# print(a[0:2])
# print(a[[0, 2, 4]])

a = np.array([2, 7, 1, 8, 2, 8]).reshape([2, 3])
print(a)
print(a[0]) # [2 7 1]
print(a[0][1]) # 7
print(a[0, 1]) # 7
print(a[0, [1, 2]])
print(a[0:2, 2])

#Homework
# 1. Print then number at the
# second row and third column
# of this array

# 2. Print the numbers in order from largest to smallest by
# a series of indices (you will have to
# (figure out the index on your own)
# like (3, 5, 1 ...
a = np.array([2, 7, 1, 8, 2, 8]).reshape([2, 3])
















