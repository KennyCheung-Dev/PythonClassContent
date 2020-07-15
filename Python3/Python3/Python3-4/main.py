import numpy as np
import matplotlib.pyplot as plt

#Store and Manipulate data in an array, in batch.
#Manipulate them in order to learn about the dataset

#Generate an numpy version of the array
# a = np.array([])  #Generated an empty numpy array
# print(a)
#
# b = np.array([1,2,3])
# print(b)
#
# c = np.array([3,5,2,6])
# print(c)
#
# d = np.array(list(range(1, 11)))
#
# print(d.reshape([2, 5])) # 2 rows, 5 columns
#
# e = np.array([[1,2],[3,4]])
# print(e)

#In-class
#Build this:
#[[1 2]
# [3 4]
# [5 6]]
#Answer:
# f = np.array([1, 2, 3, 4, 5, 6])
# print(f.reshape([3, 2]))

#np.array, we can also use np.arange, np.linspace
# g = np.arange(10)
# print(g)
#
# h = np.linspace(0, 9, 10)
# print(h)

#Make an array of numbers: 3, 6, 9, ... 21
# i = np.arange(3, 22, 3)
# print(i)

#Make an array containing 0 numbers between 0 and 2
# j = np.linspace(0, 2, 9)
# print(j)

#Randomized arrays:
# k = np.random.random(5) #size
# print(k)
#
# l = np.random.randint(0, 10, 10) #min, max, size
# print(l)

#Zeros, Ones, Indeitity, Diag

# m = np.zeros(5)
#
# n = np.ones(5)
#
# o = np.identity(5)
#
# p = np.diag([1, 2, 3, 4])
#
# print(o)

# Accessing Values
# Similar to normal array, but more variety

# Indexing and slicing
# q = np.array([3, 1, 4, 1, 5])
# print(q)
# print(q[2])
# print(q[-1])
# print(q[1:3])
# print(q[::2])
# print(q[:4])
# print(q[[0, 2, 4]])

#Multidimensional arrays: use multiple numbers for each axis
# r = np.array([2, 7, 1, 8, 2, 8]).reshape([2, 3])
# print(r)
# print(r[0])
# print(r[0][1])
# print(r[0, 1])
# print(r[0, [1, 2]]) # Row 0, index 1 and 2
# print(r[0:2, 2]) # Row 0 to 1, index 2
# print(r[[0, 1], [1, 2]])

# In-Class exercise:
# Q1. Print the number at the second row, third column of the array:
# s = np.array([2, 7, 1, 8, 2, 8]).reshape([2, 3])
# print(s[1, 2])
# print(s[1][2])

# Q2. Print the numbers in order from largest to smallest by a series of indices (sort it yourself)
# t = np.array([2, 7, 1, 8, 2, 8])
# print(t[[3, 5, 1, 0, 4, 2]])

# Q3. Print the number at index 2 on each row
# u = np.arange(2, 26).reshape(4, 6)
# for z in range(4):
#     print(u[z, 2])

# Append elements

# np.append
# v = np.arange(5)
# print(v)
# w = np.append(v, 6)
# print(w)
# x = np.append(v, [5, 6, 7])
# print(x)
# y = np.append(v, v[2:4])
# print(y)

#np.insert
# a = np.arange(5)
# print(a)
# b = np.insert(a, 0, -1)
# print(b)
# c = np.insert(a, 0, [-2, -1])
# print(c)
# d = np.insert(a, 2, 5)
# print(d)

# index & modify
# a = np.arange(5)
# print(a)
# a[1:2] = 5
# print(a)
# a[2:4] = [6, 7]
# print(a)

# np.delete
# a = np.arange(5)
# print(a)
# b = np.delete(a, 0)
# print(b)

# In-Class:
# Q1. Make the list equal to np.arange(10) by adding the missing numbers:
# a = np.array([0, 1, 3, 4, 6, 8])
# a = np.insert(a, 2, 2)
# a = np.insert(a, 5, 5)
# a = np.insert(a, 7, 7)
# a = np.insert(a, 9, 9)
# print(a)

# Q2. Make the list sorted (smallest to largest)
# by removing the out of place numbers
# Remove the least number of elements possible
# a = np.array([5, 2, 3, 1, 6, 8])
# a = np.delete(a, 0)
# a = np.delete(a, 2)
# print(a)

# Arithmetic Operations on Array
# Can easily do arithmetic operations (+, -, *, /, etc.)
# on whole arrays
# Scalar operations operate between a number and an array
# element-wise
# a = np.array([1, 2, 3])
# print(a + 2)
# print(a - 2)
# print(a * 2)
# print(a ** 2)
# print(a / 2)
# print(a % 2)

# Arithmetic Ops between arrays still operate element-size
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
# b = np.arange(1, 101)
# print(b.cumsum())

# Other familiar functions, you can look them up :)
# Diff
# Ceil/floor
# All/any
# Dot
# Average
# Sin/cos
# Exp

# Convenient rank & order
# sort
# Simplest sort function, sort in place
# numpy.sort(a)
# Optional parameters:
# axis: if the array is multidimensional, specify an axis(layer)
# for the sort. Use None to flatten and then sort. Default is -1
# kind: choose between different sorting algorithms
# (quicksort, mergesort, heapsort, stable)

# a = np.array([5, 2, 3, 1, 6, 8])
# print(a)
# b = np.sort(a)
# print(b)

# Flatten & Sort
# a = np.array([[5, 2, 3], [1, 6, 8]])
# print(a)
# b = np.sort(a, axis=None, kind="mergesort")
# print(b)

# Sort the subarrays in array a
# a = np.array([[5, 2, 3], [1, 6, 8]])
# print(a)
# b = np.sort(a, axis=1, kind="mergesort")
# print(b)

# argsort
# instead of sorting the array, this function gives
# you the indices that would sort the array
# i.e. for each position in the sorted array, you just nee to
# take the element at the index from the argsort array
a = np.array([5, 2, 3, 1, 6, 8])
# print(a)
# b = np.argsort(a)
# print(b)
# print(a[b])

# In-Class Practice:
# Q1. Write a function with input array a that
# returns a sorted version of a

def sort_With_Argsort(a):
    indices = np.argsort(a)
    b = np.array([])
    for i in indices:
        b = np.append(b, a[i])
    return b

# def sort_With_Argsort(a):
#     indices = np.argsort(a)
#     b = a[indices]
#     return b

print(sort_With_Argsort(a))












