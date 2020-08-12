# Homework Answer:
# Prime Numbers

low = int(input("Starting From?"))
high = int(input("Ending At?"))
for i in range(low, high + 1):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
    if prime == True:
        print(str(i) + " is a Prime Number")

#-------------------------------------------------------------------------
# Warm Up

# Given n
# Function to print and determine,
# from 1 to n, whether the numbers are even or odd
# print the result "1 is odd" and "2 is even" so on

# upto = int(input("Up to?"))
def AreNumbersEven(upto):
    a = 1
    while a <= upto:
        if (a % 2 == 0):
            print(str(a) + " is even")
        else:
            print(str(a) + " is odd")
        a += 1

# AreNumbersEven(upto)

#-------------------------------------------------------------------------

# Armstrong number
# n-digit number equal to the sum of the nth powers of its digits
# 水仙花數
# 定义：
# 153 = 1^3 + 5^3 + 3^3。
# 370 = 3^3 + 7^3 + 0^3。
# 371 = 3^3 + 7^3 + 1^3。
# 407 = 4^3 + 0^3 + 7^3。

# 一万以下的 水仙花数
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 153
# 370
# 371
# 407
# 1634
# 8208
# 9474
#-------------------------------------------------------------------------
# 提供n
# 找出所有 从 0 到 n 的水仙花数
# 输入： 整数0 <= n <= inf.
# 输出： 列表

# Approach 1 : Using String
# def ArmstrongNum(num):
#     armList = []
#     for i in range(num+1): # 循环每个数字
#         l = len(str(i))
#         total = 0
#         for letter in str(i): # 循环数字里每个单位
#             total += int(letter) ** l
#         if total == i:
#             armList.append(i)
#     return armList
#
# print(ArmstrongNum(10000))


# Approach 2 : Using %
def ArmstrongNumMod(num):
    armList = []
    for i in range(num+1):
        l = len(str(i))
        total = 0
        temp = i
        while temp > 0: #一致到数目除为零
            digit = temp % 10  #得到个位数
            total += digit ** l
            temp //= 10   # 除10
        if total == i:
            armList.append(i)
    return armList

print(ArmstrongNumMod(10000))


#-------------------------------------------------------------------------

# 提供2个整数 和一个布林志negative
# 如果negative是False ：  如果一个整数是负数，另一个是正数 返回True， 其他情况False
# 但如果negative是True  ：  两个整数都是负数的时候 返回True，其他情况False
# 输入和输出：
# pos_neg(1, -1, False)  -> True
# pos_neg(-1, 1, False)  -> True
# pos_neg(-4, -5, True)  -> True
def pos_neg(a, b, negative):
    if negative:
        return  a < 0 and b < 0
    else:
        return a * b < 0

# Testing
print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))

#-------------------------------------------------------------------------

# Inverse the integer
# 123 -> 321
# 789 -> 987

def Inverse(num):
    temp = num
    output = ""
    while temp > 0:
        digit = temp % 10
        output += str(digit)
        temp //= 10
    return int(output)

print(Inverse(123467))

#-------------------------------------------------------------------------



