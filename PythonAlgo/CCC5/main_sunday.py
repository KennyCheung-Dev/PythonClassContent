# def FindNucleotides(s):
#     for i in range(len(s) - 3):
#         if s[i:i+3] == "ATG":
#             #we found it! \o/
#             for j in range(len(s) - 3, -1, -1):
#                 if s[j:j+3] == "TAA" or s[j:j+3] == "TAG" or s[j:j+3] == "TGA":
#                     if (j - i) % 3 == 0 and (j - i) > 0:
#                         return s[i:j+3]
#             return "No Nucleotide Found"
#     return "No Nucleotide Found"
#
# print(FindNucleotides("ATATGTAGCTAGCATAATA"))
# print(FindNucleotides("TAAAAAAATTTTTTAAAAATTTTATG"))

# Warm ups:
# Return the number of even ints in the given array.
# count_evens([1, 2, 1, 3, 4])
# 2

# define an integer list and find the minimum of its element
# FindMinimum([10, 20, 4])
# 4

#def FindMinimum(li):
#     min = li[0]
#     for num in li:
#         if num < min:
#             min = num
#     return min
#
# print(FindMinimum([1,2,3,4,5,6,7,100]))


# def bruh(a):
#     b = 0
#     for i in a:
#         if int(i % 2) == 0:
#             b += 1
#     return b
#
# print(bruh([5, 2, 2, 2, 2, 2, 2]))


# Return the sum of the numbers in the array,
# returning 0 for an empty array.
# Except the number 13 is very unlucky,
# so it does not count and numbers that come
# immediately after a 13 also do not count

# Input
# sum13([1, 2, 2, 1])
# Output:
# 6

# Input
# sum13([1, 2])
# Output:
# 3

# Input
# sum13([1, 2, 2, 1, 13])
# Output:
# 6

# Input
# sum13([1, 2, 2, 1, 13, 5, 2])
# Output:
# 8


# def sum13(nums):
#     lenth = len(nums)
#     total = 0
#     if lenth==0:
#         return 0
#     for x in range(lenth):
#         if nums[x]!=13:
#             if x == 0 or nums[x-1] != 13:
#                 total+=nums[x]
#     return total
# print(sum13([1, 2, 2, 1, 13, 5, 6]))




# CCC 2000 J3
# Martha takes a jar of quarters to the casino with the intention of becoming rich.
# She plays three machines in turn. Unknown to her, the machines are entirely predictable.
# Each play costs one quarter.
# The first machine pays 30 quarters every 35th time it is played;
# the second machine pays 60 quarters every 100th time it is played;
# the third pays 9 quarters every 10th time it is played.
#
# Your program should take as input the number of quarters in Martha's jar
# (there will be at least one and fewer than 1000), and the number of
# times each machine has been played since it last paid.
#
# Your program should output the number of times Martha plays until she goes broke.
#
# Input/output is not from/to files for this question.
# Keyboard input and screen output is expected.
#
#
#
# Sample Session. User input is in italics
# How many quarters does Martha have in the jar?
# 48
#
# How many times has the first machine been played since paying out?
# 3 4 ....
#
# How many times has the second machine been played since paying out?
# 10 1 /....
#
# How many times has the third machine been played since paying out?
# 4 5.... 10   money + 9  0
#
# Martha plays 66 times before going broke.
# --------------------------------------------------------------------------------


# http://compsci.ca/v3/viewtopic.php?t=283