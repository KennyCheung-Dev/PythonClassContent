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

# a = np.array([2, 7, 1, 8, 2, 8]).reshape([2, 3])
# print(a)
# print(a[0]) # [2 7 1]
# print(a[0][1]) # 7
# print(a[0, 1]) # 7
# print(a[0, [1, 2]])
# print(a[0:2, 2])

#Homework
# 1. Print then number at the
# second row and third column
# of this array

# 2. Print the numbers in order from largest to smallest by
# a series of indices (you will have to
# (figure out the index on your own)
# like (3, 5, 1 ...
# a = np.array([2, 7, 1, 8, 2, 8]).reshape([2, 3])
#
# print(a[1, 2])
#
# print(a[1, 0], a[1, 2], a[0, 1], a[0, 0], a[1, 1], a[0, 2])

# Print the number at index 2 on each row
# for this array
# a = np.arange(2, 26).reshape(4, 6)
# Hint: 4 rows in this array!
# print(a)

# techniques:
# print(a[0:2, 2])
#          ^   ^
#         row column
#

# Remember append?
# myList = ["cat1", "cat2", "cat3"]
# myList.append("cat4")
# print(myList)

# #Original Numpy Array
# a = np.arange(5)
# print(a)
#
# #Adding 1 element
# b = np.append(a, 5)
# print(b)
#
# #Adding 3 elements at a time
# c = np.append(b, [6, 7, 8])
# print(c)
#
# #Accessing previous array's value and appending
# d = np.append(c, c[2:4])
# print(d)


# Original Numpy Array
# a = np.linspace(0, 4, 5)
# print(a)

# Insert
# 3 parameters
# 1st: the array
# 2nd: the position
# 3rd: the values
# b = np.insert(a, 0, -1)
# print(b)

# Adding in the middle
# c = np.insert(b, 4, 2.5)
# print(c)

# Multiple numbers
# d = np.insert(c, 0, [-3, -2])
# print(d)


#Modifying elements
# a = np.arange(5)
# print(a)
# a[1] = 10
# print(a)
# a[2:4] = [20, 30]
# print(a)

#Deleting Elements
# a = np.arange(5)
# print(a)
# b = np.delete(a, 0)
# print(b)
# c = np.delete(b, [1, 2])
# print(c)

# In-Class Exercise:
# 1. Make this list equal to np.arange(10)
# by adding the missing numbers
# Hint: np.arange(10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = np.array([0, 1, 3, 4, 6, 8])
print(a)

# 2. Make this list sorted (smallest to largest)
# by removing the out of place numbers,
# removing the least number of elements as possible
a = np.array([5, 2, 3, 1, 6, 8])
# Hint: You can remove 2 numbers

# Arithmetic Operations + - * /
balanceForBankUser = np.array([200, 300, 10, 900, -4])
newB = balanceForBankUser + 3000
print(newB)

newB = balanceForBankUser / 2
print(newB)


GovernmentsDebt = np.array([30, 600, 0, -400, -900000])
finalBalance = balanceForBankUser - GovernmentsDebt
print(finalBalance)

# Diff
# Ceil/Floor
# All/any
# Dot
# Average
# Sin/Cos
# Exp

# Homework Q3.
currentHeightOfBalls = [30, 700, 90, 2000] # in meters
# Initial speed is 0.0m/s
gravity = -9.8 #m/s/s  (unit for acceleration)
#Calculate the height of all the balls after 3 seconds

# After First second is passed, speed is -9.8,
# height of first ball 20.2

# After Second second is passed, speed is now -9.8 * 2
# height fo the first ball is now 0.6


print('''
 ,_     _
 |\\\\_,-~/
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. \\
|         _  \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'
''')















