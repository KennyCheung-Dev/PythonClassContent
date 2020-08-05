#
# for i in range(5):
#     for j in range(5):
#         print("(" + str(j) + "," + str(i) + ")", end=" ")
#     print()
#
#
# counter  = 1
# for i in range(5):
#     for j in range(i):
#         print(counter, end=" ")
#         counter += 1
#     print()
#
#
# counter  = 1
# for i in range(5):
#     for j in range(i):
#         print(counter, end=" ")
#         counter += 1
#     print()
#
#
# counter  = 1
# for i in range(5):
#     for j in range(5 - i):
#         print("o", end=" ")
#     print("I")
# print("I")

# 1 and 2 and 3  multiply each with each others
# sum = 0
# nums = [1, 2, 3]
# for i in nums:
#     for j in nums:
#         sum += i * j
# print(sum)






# Nested For-loop 嵌套循环
# for i in range(5):
#     for j in range(5):
#         pass
#         # 重复五遍
#         print("(" + str(j) + ", " + str(i) + ")" , end=" ")
#     print()

# x = 0
# if x > 10:
#     pass
# print("Hello")

# 0 1 2 3 4
# 5 6 7 8 9
# 10 11 12 13 14
# 15 16 17 18 19
# 20 21 22 23 24

# num = 0
# for i in range(5):
#     for j in range(5):
#         print(num, end=" ")
#         num+=1
#     print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# num = 0
# for i in range(5):
#     for j in range(i):
#         print(num, end=" ")
#         num+=1
#     print()

# o o o o I
# o o o I
# o o I
# o I
# I

# . . . . .
# . . . .
# . . .
# . .
# .

# a = 0
# for i in range(5):
#     for p in range(5 - i):
#         print(a, end=" ")
#         a+=1
#     print("I", end=" ")
#     print()

# x='o'
# for i in range(5):
#     for j in range(5-i):
#         print('o',end='')
#     print('I')
# print('I')

number = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12],
          [13, 14, 15]]
print(number[2][0])
# 作业题目
# 不用上述方法 直接把列表写出来
# 把嵌套列表 用嵌套循环 造出来
# Hint1: 用嵌套循环for-loop
# Hint2: 如果想要赋值 可以number[2][0] = x
# Hint(optional): 也可以用number[x].append(y) 来赋值
# 最后把列表print出来

# [[],[],[],[],[]]


# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# 13 14 15

# o o o o o o o
# o o o o o o o
# o o o o o o o
# o o o o o o o















