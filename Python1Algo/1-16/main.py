# 热身题：
# 乘数表

# 1 * 1 = 1 | 1 * 2 = 2 | 1 * 3 = 3 | ...
# ...
# ...
# ...
# ... ... 9 * 7 = 63 | 9 * 8 = 72 | 9 * 9 = 81 |

# 题目： 用上述格式 print出乘数表

# for i in range(sgkn):
#     for j in range(aksjb):

# --------------------------------------------------

# 新题目我们会回到J1 比较简单一点的
'''


*    *    *
*    *    *
*    *    *
***********
     *
     *
     *
     *
4
3
4
'''



# a = int(input())
# b = int(input())
# c = int(input())
#
# # 叉子脚部位置
# for i in range(a):
#     print("*" + c * " " + "*" + c * " " + "*")
#
# # 叉子 颈部 位置
# print(3 * "*" + c * 2 * "*")


#------------------------------------------------------------------------------------------------------------

# CCC 2001 J1 - Dressing Up

# 一个整数 input
# Example :  5
'''

*        *
***    ***
**********
***    ***
*        *

'''
# example:  7
'''
*            *
***        ***
*****    *****
**************
*****    *****
***        ***
*            *

'''


#----------------------------------------------------------------

# CCC 2012 J3 - Icon Scaling
# 历年最容易J3
'''

*x*
 xx
* *

以上是一个图标 我们想根据一个整数输入 - 倍数
将图标放大

例子：       3
***xxx***
***xxx***
***xxx***
   xxxxxx
   xxxxxx
   xxxxxx
***   ***
***   ***
***   ***
'''

# ------------------------------------------------------------

# CCC 2019 J2

'''
Input:
4
9 +
3 -
1 8
2 X


Output:
+++++++++
---
AAAAAAAAAAAA
XX

'''
#
# a   = "0 x"
# num, sym = a.split(" ")


# Answer:
# for i in range(int(input())):
#     num, sym = input().split(" ")
#     # for y in range(int(num)):
#     #     print(sym, end="")
#     # print()
#     print(sym * int(num))

# -----------------------------------------------------------------
#热身题
# 判断一个文字是不是palindrome
# mom  pop  poop  lol  anana

# def IsPalindrome(text):
#     #xxxxx
#
#     # for letter in text:
#     return True

#----------------------------------------
# 隐藏回文
# "anana"
# "banana" -> 5
# abracadabra -> 3
# HolloWorld -> 4
# abcdefg -> 1

# # ___________
# text = "abcde"
# for i in range(0, len(text)):
#     for j in range(i+1, len(text)):
#         print(text[i:j+1])

# def HiddenPalindrome(text):
#     return 5


#----------------------------

# 不知道有多少鸡和兔子被锁起来了
# 从上面看有35个头
# 从下面看 有94只 动物的脚

# 请计算 每种 动物的 数量

# 方法1 用单个循环
# 方法2 用嵌套循环

# for-loop (鸡的数量）:
#   for-loop (兔子的数量):
#         if 条件正确：
#             return 什么什么什么什么

# for chicken in range(1, 36):
#     for rabbit in range(1, 23):
#         if chicken + rabbit == 36 and chicken * 2 + rabbit * 4 == 94:
#             print("Rabbit: " + str(rabbit) + " Chickens: " + str(chicken))

# ------------------------------------------------------
# key, value
# 3, "Kenny"
# 5, "Hi"
# 8, "Hello"
# dict = {
#     3:"Kenny",
#     5:"Hi",
#     8:"Hello"
# }
# print(dict[8])

# ------------------------------
# Count the number of occurences of
# all the elements
num = [2, 2, 3, 3, 6, 8, 8, 9, 10, 11, 11, 11, 11]
# 2 出现过 2 次
# 3 出现过 2 次
# 11 出现过 4 次

# [2, 3, 6, 8, 9, 10, 11]
# [2, 2, 1, 2, 1, 1, 4]
for i in num:
    #赋值
    dict[i] = 1

    #改变值
    dict[i] += 1





