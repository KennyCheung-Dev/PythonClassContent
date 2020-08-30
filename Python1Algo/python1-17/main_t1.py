list = [1, 2, 3, 4, 5, 6, 7]
list[1]
list[4] = 6
# print(list)

# Tuple 元祖
tup = (1, 2, 3, 4, 5, 6, 7)
# print(tup[1])
# print(tup[1:4])
# print(tup[::-1])

# for i in tup:
#     print(i)

# -------------------
# 提供 一个元祖 和一个目标
# 在元祖里 找到两个数字 他们的和等于目标
# 返回两个数字的索引 以元祖的方式
# Input:  (2, 7, 11, 15), 9
# Output: (0, 1)
tup = (2, 7, 11, 15)
target = 9


# def YourMethod(tup, target):
#     for i in range(len(tup)):
#         if target - tup[i] in tup:
#             if target - tup[i] == tup[i]:
#                 if (tup.count(tup[i]) <= 1):
#                     continue
#                 else:
#                     resultList = []
#                     count = 2
#                     for j in range(len(tup)):
#                         if tup[j] == tup[i]:
#                             count -= 1
#                             resultList.append(j)
#                             if count <= 0:
#                                 return (resultList[0], resultList[1])
#                                 break
#             return(tup.index(tup[i]), tup.index(target - tup[i]))

# def YourMethod(tup, target):
#     for i in range(len(tup)):
#         if target - tup[i] in tup:
#             return(tup.index(tup[i]), tup.index(target - tup[i]))
# print(YourMethod(tup, target))


# def YourMethod(tup, target):
#     dict = {}
#     for index, item in enumerate(tup):
#         if not target - item in dict:
#             dict[item] = index
#         else:
#             print("Found the two numbers:", dict[target - item], index)
#             break
# YourMethod(tup, target)

# ------------------------------------------------------------------------------

# Find the intersection between 2 tuple
# 找到 两个元祖的 交切点

# Intersected at "Is"
# Intersected at 9

#记录
# dict["数值"] = 次数

#累积
# dict["数值"] += 1

#检查 次数
# if dict["数值"] > ??:
#     print(Intersected at 数值)

tup1 = ("1", "abc", 3, 6, 9, "Is", 3, "1")
tup2 = (4, "bc", 8, "Is", 9, 9, 4)

dict = {}
for i in tup1:
    dict[i] = 1
for i in tup2:
    if i in dict:
        dict[i] += 1
for key, value in dict.items():
    if value > 1:
        print("Intersected at " + str(key))

#---------------------------------------------------------

'''
4
3 +
2 - 
3 8
12 a

+++
--
888
aaaaaaaaaaaa
'''


'''
Input:
4
+++===!!!!
777777......TTTTTTTTTTTT
(AABBC)
3.1415555

Output:
3 + 3 = 4 !
6 7 6 . 12 T
1 ( 2 A 2 B 1 C 1 )
1 3 1 . 1 1 1 4 1 1 4 5

'''














