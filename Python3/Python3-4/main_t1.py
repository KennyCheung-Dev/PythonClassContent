import numpy as np

# myList = [1, 2, 3, 4]

# numpy array
# Store and manipulate data in an array, in batch

# Generate a numpy version of array
# np.array()
# a = np.array([])
# print(a)

# b = np.array([1, 2, 3])
# print(b)

# c = np.array(range(1, 1001))
# print(c)

# print(c.reshape([250, 4]))  # [rows, columns]

# d = np.array([[1, 2], [3, 4]])
# print(d)

#In-Class Exercise:
# Build this:
#[[1 2]
# [3 4]
# [5 6]]
# Use Reshape (Parameters will be [rows, column] for reshape)

# arange
# Make an array of numbers: 3, 6, 9, 12, .... 21
# a = np.arange(3, 22, 3)
# print(a)

# Randomized arrays
# k = np.random.random(3)
# k = k * 255
# print(k)

# a = np.random.randint(0, 255, 3) # min, max, size
# print(a)

# Math Constants - Zero, One, Identity
# m = np.zeros(10)
# print(m)
#
# n = np.ones(10)
# print(n)
#
# o = np.identity(24)
# print(o)
#
# p = np.diag([10, 20 ,30, 40])
# print(p)

# Accessing Values

# Index and slicing
# a = np.array([3, 1, 4, 1, 5, 1, 6])
# print(a)
# print(a[2]) #Third Element
# print(a[-1]) #Last Element
# print(a[0:3]) # From X element to Y element
# print(a[::2]) # Starting from X, every Y number
# print(a[:4])
# print(a[[0, 2, 4]])

# Multidimensional arrays:
# a = np.array([2, 7, 1, 8, 2, 8, 9, 4, 3]).reshape([3, 3])
# [[2 7 1]
#  [8 2 8]]
# print(a)
# print(a[0])
# print(a[0][1])
# print(a[0, 1])
# print(a[1, [0, 1]])
# print(a[0:3, 2]) #a[rows, columns]
# print(a[[0, 1], [1, 2]])

# In-Class exercise
#Q1. Print the number at the second row,
# third column of the array

#Q2. Print the numbers in order from
# Largest to Smallest by a series of indices
# (sort it yourself)

#Q3. Print the number at index 2 on each row
# a = np.array([2, 7, 1, 8, 2, 9]).reshape([2, 3])
# print(a[[5, 3, 1, 0, 4, 2]])

# Homework:
# Build the following matrix:
# 0, 1, 2, 3,
# 4, 5, 6, 7
# 8, 9, 10, 11
# changed the shape into 4 : 3 (4 rows and 3 columns)
# Access every 1st element in each line
# Access the last element in the second line
# Add them all up for a final answer
# We will simply test with that final answer

# a = np.array(list(range(0, 12))).reshape([4, 3])
# print(a)
# print(a[0:4, 0])
# print(a[1, 2])
# print(np.sum(a[0:4, 0]) + a[1, 2])

#Adding Elements in numpy array
# np.append
# a = np.arange(5)
# print(a)
# b = np.append(a, 5)
# print(b)
# c = np.append(a, [5, 6, 7])
# print(c)
# d = np.append(a, a[2:4])
# print(d)

# np.insert
# a = np.arange(5)
# print(a)
# b = np.insert(a, 0, -1)
# print(b)
# d = np.arange(-3, 0)
# c = np.insert(a, 3, d)
# print(c)

#Modifying
# a = np.arange(5)
# print(a)
#Change the 2nd element in the list to "5"
# [0, 1, 2, 3, 4]
# [0, 5, 2, 3, 4]
# a[1] = 5
# print(a)
# Normal way to  assign values : list[5] = 20
#Change the last two elements in the list to "[8, 9]"
# [0, 1, 2, 8, 9]
# a[3:5] = [8, 9]
# print(a)


# np.delete
# a = np.arange(5)
# print(a)
# b = np.delete(a, [2, 3, 4])
# print(b)

'''
In-Class Exercise:
Make this list equal to np.arange(10)
by adding the missing numbers
and deleting excessive numbers
'''
print(np.arange(10))

a = np.array([0, 1, 3, 572, 4, 6, 8])
print(a)


































