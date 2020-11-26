# Q.
# Given an [] of integer, and a integer target.
# Find the first pair of elements a and b
# that satisfy a + b = target and return their INDEX
# Assume numbers within the [] of integers will not contain duplicates
# Output "Found the numbers at position n and position m.
# (0-based index is fine)
nums = [2, 7, 11, 15]
target = 26
# brk = False
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i != j:
#             if nums[i] + nums[j] == target:
#                 print("Found the numbers at position " + str(i) + " and position " + str(j) + ".")
#                 brk = True
#                 break
#     if brk:
#         break

# dict = {}
# for i in range(len(nums)):
#     if (target - nums[i] in dict):
#         print("Found the numbers at position " + str(dict[target - nums[i]]) + " and position " + str(i) + ".")
#     else:
#         dict[nums[i]] = i

# Counts the number of occurrences of the second most frequent element in a list
# USE dict
nums = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]
dict = {}
for i in nums:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

max = 0
second_max = 0
for (key, value) in dict.items():
    if value > max:
        second_max = max
        max = value
    elif value > second_max:
        second_max = value
print("The count of the second max is: " + str(second_max))
