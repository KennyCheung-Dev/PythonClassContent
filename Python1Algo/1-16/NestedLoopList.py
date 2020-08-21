#热身

# *
# **
# ***
# ****
# *****

# for i in range(5):
#     for j in range(i+1):
#         print("*", end="")
#     print()

# -------------------------------------------------------

# 乘数表 1-9

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(str(i) + " * " + str(j) + " = " + str(i*j), end=" | ")
#     print()

# for i in range(1, 10):
# #     for j in range(1, 10):
# #         print("{} * {} = {}".format(i, j, i*j), end=" | ")
# #     print()

# -------------------------------------------------------

# Q3.
# An unknown number of rabbits and chicken were locked
# in a cage, count from top, there was 35 heads,
# count from  bottom, there were 94 feets.
# How many rabbits and chickens were locked in this cage?
# 不知道有多少鸡和兔被锁起来了
# 从上面看有35 个动物的头
# 从下面看有94 只动物的脚
# 请计算动物的数量

# My Answer:
# for i in range(0, 36):
#     if i * 4 + (36-i) * 2  == 94:
#         print("Rabbit: " + str(i) + "  Chickens: " + str(36-i))

# Official answer:
# 鸡 最少1 最多35
# 兔子 最少1 最多23 （因为四只脚）
# 我们可以循环过所有有可能的combination
# 然后看结果 等于94
# for chicken in range(1, 36):
#     for rabbit in range(1, 24):
#         if chicken + rabbit == 36 and chicken * 2 + rabbit * 4 == 94:
#             print("Rabbit: " + str(rabbit) + "  Chickens: " + str(chicken))

# -------------------------------------------------------

# CCC 2016 J3 Hidden Palindrome
# 隐藏回文
# 回文是一个 拼法倒过来也是一样的词
# mom anna wow
# 我们可以在一个词里面找到隐藏的回文
# banana -> "anana"

# 题目要求：
# 找到词里面隐藏回文 最大的长度
# banana -> 5
# abracadabra -> 3
# abba -> 4

# def HiddenPalindrome(text):
#     longest = 1
#     for i in range(0, len(text) + 1):
#         for j in range(i+1, len(text) + 1):
#             a = text[i:j]
#             b = a[::-1]
#             if a == b:
#                 if len(a) > longest:
#                     longest = len(a)
#                     print(a)
#     return longest
# print(HiddenPalindrome("banana"))

# -------------------------------------------------------

# Output the value of the given elements
# in the multidimensional list:
# The 3rd row  第三行
# The 3rd row, 1st column 第三行，第一列
x = [[2,6],[6,2],[8,2],[5,12]]
print(x[2])
print(x[2][0])

# Reversing a sublist
# a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
# a.reverse()
# for i in range(3):
#     a[i].reverse()
# print(a)

# -------------------------------------------------------

# CCC 2012 J3 - Icon Scaling

# *x*
#  xx
# * *

# 程序取一个整数 根据整数放大标志
# 例子：
# Input:  3
# Output:
# ***xxx***
# ***xxx***
# ***xxx***
#    xxxxxx
#    xxxxxx
#    xxxxxx
# ***   ***
# ***   ***
# ***   ***

# print("sh"*3)
# *x*
#  xx
# * *
# Answer:

def iconScale(k):
    icon = [["*", "x", "*"],
            [" ", "x", "x"],
            ["*", " ", "*"]]
    result = ""
    for lines in range(3): # For each line
        for l in range(k):
            for item in range(3): # for each item in a line
                result += icon[lines][item] * k
            result += "\n"

    return result

print(iconScale(2))
