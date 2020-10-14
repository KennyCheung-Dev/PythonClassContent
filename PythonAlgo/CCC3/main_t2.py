# Question 2
# list1 = [23, 65, 19, 90]
# list1[0], list1[2] = list1[2], list1[0]
# print(list1)

# Finds Easter passing in the year
# Quotients  6 / 4 = 1
# Remainder  6 % 4 = 2

# print(int(30.999997))
# print(30//4)

# Requirements:
# Divide year by 19 and call the remainder a, Ignore the quotient
# Divide year by 100 to get a quotient b and a remainder c

# def FindEaster(year):
#     a = year % 19
#     b = year // 100
#     c = year % 100
#     ...
#     return (n, p)
#
# FindEaster(2001)[0]

# Prime numbers
# Numbers that can:
# Can be divided by Itself
# Can be divided by 1
# Nothing else

# Question:
# Input two number, find all prime numbers
# within that range inclusively

# Input:
# 1
# 10
# Output:
# 2
# 3
# 5
# 7
# Numberrange = int(input("Please input range:"))
# numberrange = int(input("Please input Range 2:"))
#
# for num in range(Numberrange,numberrange + 1):
#     isPrime = True
#     if num > 1:
#         for i in range(2, num):
#             if(num % i)==0:
#                 isPrime = False
#                 break
#         if isPrime:
#             print(num)

# Armstrong number

# Input:
# 153
# Output:
# True

# Input:
# 152
# Output:
# False!

# Input:
# 1634
# Ouput:
# True






















# ** //
# Task 2 # Check if a number is an Armstrong Number 
def checkArmstrong(number):
    questionInput = int(number)
    currentSum = 0
    digitList = [int(x) for x in str(number)]
    for items in digitList:
        currentResult = int(items) ** int(len(str(number)))
        currentSum = currentSum + int(currentResult)
        print(currentSum)
        currentSum = int(currentSum)
        if questionInput == currentSum:
            print(True)
        else:
            print(False)
print(checkArmstrong(1634))
