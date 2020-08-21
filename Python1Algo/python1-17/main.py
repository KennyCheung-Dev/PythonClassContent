# Tuples, dictionary, sorting

#Define a tuple, to determine if a given
# content is inside the tuple

# Test if b is in the tuple
test = ("a", "b", "c", "d")

# Solution 1:
# def inTuple(char, test):
#     for item in test:
#         if char == item:
#             return True
#     return False
# print(inTuple("b", test))

# Solution 2:
# def inTuple(char, test):
#     if char in test:
#         return True
#     else:
#         return False
# print(inTuple("b", test))

# len()
# max()
# min()

# Tuple is immutable
tup = (1, 2, 3, 4, 5, 6, 7)
# print(tup[2])
# print(tup[2:6])
# print(tup.count(50))
# tup.append()

# ----------------------------------------
# 提供一个tuple元祖 和一个目标
# 在元祖里找到两个数字，加起来等于目标
# 返回两个数字的索 以tuple形式
# (2, 7, 11, 15), 9  -> (0, 1)

# def SumTarget(tup, target):
#     for i in range(len(tup)):
#         for j in range(i + 1, len(tup)):
#             if tup[i] + tup[j] == target:
#                 return (i, j)
# print(SumTarget((1, 2, 3, 4, 5, 6, 7), 6))

nums = (2, 7, 11, 15)
target = 9

# dict = {}
# for index, item in enumerate(nums):
#     if target - item in dict:
#         print("Found the two numbers:", index, dict[target  - item])
#     else:
#         dict[item] = index
#
# for i in enumerate(nums):
#     print(i)

#---------------------------------------------------

# Count the number of occurences of the second most frequent
# element in a tuple

# Use Dictionary!
tup = (1, 3, 5, 7, 8, 5, 20, 3, 5, 30, 41, 5, 6, 3)
dict = {}
for i in tup:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for item, times in dict.items():
    print("{} has appeared {} times.".format(item, times))

#---------------------------------------------------

# Find intersection between 2 tuple
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

#---------------------------------------------------

# Sorting Algorithm

# Bubble Sort
# nums = [4, 6, 1, 3, 2, 8, 7, 9, 5]
# n = len(nums)
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if nums[j] > nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]
# print(nums)

# Selection Sort
# nums = [4, 6, 1, 3, 2, 8, 7, 9, 5]
# n = len(nums)
# for i in range(0, len(nums) - 1):
#     min = i
#     for j in range(i+1, len(nums)):
#         if nums[j] < nums[min]:
#             min = j
#     nums[min], nums[i] = nums[i], nums[min]
# print(nums)



