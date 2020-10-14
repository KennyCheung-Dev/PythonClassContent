# Warm up question
# Input a number, determine if it is between 1 and 100 inclusively

# Input:
# 16
# Output:
# True

# Input:
# 120
# Output:
# False

# if 0 < int(input()) <= 100:
#     print("True")
# else:
#     print("False")
#
# def within100(x):
#     return 0 < x <= 100

# ------------- ------------- ------------- ------------- -------------

# From 1 to 6 inclusive, determine whether the numbers are
# even or odd
# Please use loops
# Input : None
# Output:
# 1 is an odd number
# 2 is an even number
# ....

# for i in range(1, 7, 1):
#     print(str(i), end="")
#     if i % 2 == 0:
#         print(" is an even number")
#     else:
#         print(" is an odd number")



# This year that is a multiple of 4 is usually a leap year
# However, those multiple of hundred, it has to be a multiple of
# 400 to be a leap year. For example
# 1900 is not a leap year. 2000 is a leap year

# Input:
# 1900
# Output:
# False

# Input:
# 2000
# Output:
# True

# import random
#
# x = 10
# y = 20
#
# x *= random.randint(1, 10)
# y *= random.randint(1, 10)
#
# print(x * y)

# year = int(input())
# flag = False
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             flag = True
#         else: # 1300, 1500, 1700
#             flag = False
#     else: # 104, 208 Not dividable by 100
#         flag = True
# else: # 3, 6, 1201
#     flag = False
#
# print(flag)

# A)
# Build a program, check if user's input is prime number  or not
# Not considering negative numbers
# Input:
# 9
# Output:
# False

# Input:
# 1
# Output:
# False

# Input:
# 2
# Output:
# True

# B)
# Have user input a range, between two numbers
# print all the prime numbers with in the range inclusively

# Input:
# 2
# 100
# Output:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47
# 53
# 59
# 61
# 67
# 71
# 73
# 79
# 83
# 89
# 97


min = int(input("min?"))
max = int(input("max?"))

for i in range(min, max + 1):
    if (i > 1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag:
            print(i)

