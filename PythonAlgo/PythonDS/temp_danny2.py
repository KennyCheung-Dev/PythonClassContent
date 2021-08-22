#Numpy

import math
import numpy as np
import matplotlib.pyplot as plt

# numpy is to :
# Store and Manipulate data in an array, in batch.
# Manipulate them in order to learn about the dataset
# After getting data from source, we wrangle the data

# Generate an numpy version of the array

# a = np.array([1, 3, 5, 7])
# print(a)

# a = np.array(list(range(1, 101)))
# print(a)

# a = np.array([1, 2, 3, 4, 5, 6])
# a = a.reshape(2, 3)
# print(a)

# a = np.array([[1, 2, 3], [4, 5, 6]])
# print(a)

# a = np.linspace(0, 8, 5)
# print(a)

# Make an array of numbers: 3, 6, 9, ... 21
# a = np.linspace(3, 21, 7)
# print(a)

# a = np.linspace(0, 2, 100)
# print(a)

# Randomized arrays :
# a = np.random.random(100) #size
# print(a)

# a = np.random.random(100) #size
# for i in range(len(a)):
#     a[i] *= 100
#     a[i] = round(a[i])

# a = np.random.random(1) * 5 + 5 #size
# print(a)

# a = np.random.randint(5, 11, 1) #size #Exclusive on uppe range
# print(a)

# Zero, Ones, Identity, Diag
# a = np.zeros(25)
# a = a.reshape(5, 5)
# print(a)

# a = np.ones(5)
# print(a)

# a = np.identity(5)
# print(a)

# a = np.diag([100, 2, 3, 4])
# print(a)



#Accessing Values
# Similar to normal arrays, but more variety

# Indexing and slicing
# q = np.array([3, 1, 4, 1, 5, 1, 6, 1, 7])
# print(q)
# print(q[2])
# print(q[-1])
# print(q[1:4])
# print(q[:2])
# print(q[[1, 3, 5, 7]])
# print(q[::2])

# Multidimensional arrays:
a = np.array([2, 7, 1, 8, 2, 8]).reshape(2, 3)
# print(a)
# print(a[0])
# print(a[0][-1])
# print(a[0, 1])
# print(a[0, [1, 2]]) #Row 0, index 1 and 2
# print(a[0:2, 2]) # Row 0 to 1, index 2
# print(a[[0, 1], [1, 2]])

# In-Class exercise:
#Q1. Print the number at the second row, third column of the array:
#Q2. Print the numbers in order from largest to smallest by a
# series of indices (sort it yourself)
a = np.array([2, 7, 1, 8, 2, 8]).reshape(2, 3)

#Q3. Print the number at index 2 on each row (Use a for loop)
b = np.arange(2, 26).reshape(4, 6)



# 143

