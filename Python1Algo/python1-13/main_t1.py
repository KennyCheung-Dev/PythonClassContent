# Homework:
# Prime Numbers
# low = int(input("Starting From?"))
# high = int(int(input("Ending At?")))
# for i in range(low, high + 1):
#     prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             prime = False
#     if prime == True:
#         print(str(i) + " is a Prime Number")

# ----------------------------------------------------------------------

# Warm Up

# 提供2个整数 和一个布林值negative
# 如果negative 是False： 如果一个整数是负数  另一个是正数 返回True，其他情况返回False  [+/-] [-/+]
# 如果negative 是True： 两个整数都是负数的时候True  其他情况False  [-/-]

def pos_neg(a, b, negative):
    # Your code
    pass # 这个不用写

print(pos_neg(1, -1, False))

# if not xx == yy

# if x < 0 and y < 0:

# Example In/Output:
# 1, -1, False ->  True
# -1, 1, False ->  True
# -4, -5, True -> True
# 4, 5, True -> False


# def pos_neg(a,b,negative):
#     c=0
#     d=()
#     if negative == True:
#         if a<c and b<c:
#             return True
#         else:
#             return False
#
#     if negative == False:
#         if (a < c and b > c) or (a > c and b < c):
#             return True
#         else:
#             return False
# print(pos_neg(1, -1, False),
# pos_neg(-1, 1, False),
# pos_neg(-4, -5, True),
# pos_neg(4, 5, True))

# Answer
# def pos_neg(a, b, negative):
#     if negative:
#         return a<0 and b<0
#     else:
#         return a * b < 0
# print(pos_neg(1, -1, False),
# pos_neg(-1, 1, False),
# pos_neg(-4, -5, True),
# pos_neg(4, 5, True))

# --------------------------------------------------------------------------------------------

# 把数字 倒过来
# 123 -> 321
# 789 -> 987
# 64875 -> 57846


# def inverse(list):
#     list = str(list)
#     x=''
#     for step in range (len(list)):
#         x+=list[len(list)-step-1]
#     return x
#
# print(inverse(123445))

# x = x // y
# 10/4 = 2.5
# 10//4 = 2
# 678  // 10  = 67   // 10  = 6

# 678 % 10 = 8

# strA=input('请输入一串数字：')
# b=strA[::-1]
# print(b)


# ------------------------------------------------------------------------

# def Inverse(num):
#     result = ""
#     while num > 0:
#         digit = num % 10
#         result += str(digit)
#         num = num // 10
#     return int(result)
#
# print(Inverse(544321))

# ------------------------------------------------------------------------
# 水仙花数
# 153
# = 1 ** 3 + 5 ** 3 + 3 ** 3
# = 1 + 125 + 27
# = 153

# 153, 370, 371, 407

# 提供n
# 找出从 0 到 n 的所有水仙花数 不用包括n
# 输出方法随意

# 3 ** 3 = 9

# 作业：尝试完成 水仙花题目 用 数字计算的方法

# while num > 0:
#     digit = num % 10
#     result += str(digit)
#     num = num // 10

# ---------------------------------

# Approach 1 : Using String

# def Armstrongnum(num):
#     armList = []
#     for i in range(num):
#         l = len(str(i))
#         total = 0
#         for letter in str(i):
#             total += int(letter) ** l
#         if total == i:
#             armList.append(i)
#     return armList
#
# print(Armstrongnum(100000))


# Approach 2 : Using %
def Armstrongnum(num):
    armList = []
    for i in range(num):
        l = len(str(i))
        total = 0
        temp = i
        while temp > 0:
            digit = temp % 10
            total += digit ** l
            temp //= 10
        if total == i:
            armList.append(i)
    return armList
print(Armstrongnum(100000))






