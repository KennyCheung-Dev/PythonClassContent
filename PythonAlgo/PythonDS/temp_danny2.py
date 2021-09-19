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
# a = np.array([2, 7, 1, 8, 2, 8]).reshape(2, 3)
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
# a = np.array([2, 7, 1, 8, 2, 8]).reshape(2, 3)

#Q3. Print the number at index 2 on each row (Use a for loop)
# b = np.arange(2, 26).reshape(4, 6)




# Append elements
# np.append(?)
# v = np.arange(5)
# v = np.append(v, 6)
# v = np.append(v, [5, 6, 7])
# v = np.append(v, list(range(8,10)))


# Insert
# v = np.insert(v, 1, 999)
# [-2 -1 0 999   1   2   3   4   6   5   6   7   8   9]
# v = np.insert(v, 0, [-2, -1])
# v = np.insert(v, len(v), 10)
# print(v)

# Zeroes, Ones, Indentity, Diag
# a = np.zeros(1000)
# a = np.identity(5)
# a = np.diag([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(a)

# Accessing Values
# Similar to normal lists, but more variety
# a = np.array([3, 1, 4, 1, 5, 1, 6])
# print(a[2])
# print(a[-1])
# print(a[1:3])
# print(a[::2])
# print(a[1::2])
# print(a[:4])
# print(a[[0, 2, 4]])


# Multidimensional arrays: use multiple numbers for each axis
# a = np.array([2, 7, 1, 8, 2, 8]).reshape(2, 3)
# print(a)
# print(a[0])
# print(a[0][1])
# print(a[0, 1])
# print(a[[0, 1]])
# print(a[0, [1, 2]]) # Row0, index 1 and 2
# print(a[0:2, 2]) # Row 0 to 1, index2
# print(a[[0, 1], [1, 2]])

# index and modify
# a = np.arange(5)
# a[1:2] = 5
# a[2:4] = [6, 7]
# print(a)

# np.delete
# a = np.arange(5)
# a = np.delete(a, 0)
# a = np.delete(a, list(range(0, len(a))))
# print(a)

# In-class:
# Q1. Make the list equal to np.arange(10) by adding and deleting the missing numbers:
# a = np.array([0, 1, 3, 4, 6, 8, 11])
# a = np.delete(a, 6)
# a = np.insert(a, 2, 2)
# a = np.insert(a, 5, 5)
# a = np.insert(a, 7, 7)
# a = np.insert(a, 9, 9)
# print(a)

# Q2. Make the list sorted (smallest to Largest)
# by removing the out of place numbers
# Remove the least number of elements possible
# a = np.array([5, 2, 3, 1, 6, 8])

# Arithmetic Operations on Arrays (+ = * / etc)
# Can easily do these on whole arrays
# a = np.array([1, 2, 3])
# print(a + 2)
# print(a - 2)
# print(a * 2)
# print(a ** 2)
# print(a / 2)
# print(a % 2)

# Arithmetic Ops between arrays
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# Unary arithmetic operations
# a = np.array([1, 2, 3])
# print(a.max())
# print(a.min())
# print(a.sum())
# print(a.cumsum())

# a = np.array(list(range(1, 101)))
# print(a.cumsum())


# Convenient rank & order
# sort
# numpy.sort(a)

# Optional Attributes:
# axis: if the array is multidimensional, specify an axis to sort
# kind: sorting algorithms (quicksort, mergesort, heapsort, stable)

# a = np.array([5, 2, 3, 1, 6, 8, 2, 5, 7, 9, 2, 1]).reshape([3, 4])
# print(a)
# print(np.sort(a, axis=2, kind="mergesort"))

# argsort
# instead of sorting the array, this function gives
# you the indices
# a = np.array([5, 2, 3, 1, 6, 8])
# print(np.argsort(a))

# In-Class Exerice:
# Q1. Write a funcion with input array a that
# returns a sorted version of a
# Using Argo Sort





# 173












