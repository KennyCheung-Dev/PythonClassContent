
# CCC 2018 J3 - Are We There Yet

# Sample Input
# 3 10 12 5

# Sample Output
# 0 3 13 25 30
# 3 0 10 22 27
# 13 10 0 12 17
# 25 22 12 0 5
# 30 27 17 5 0

# Answer:
dist = [3, 10, 12, 5]

for i in range(-1, 4):
    currentDist = 0
    output = []
    for j in range(i, -1, -1):
        currentDist += dist[j]
        output.insert(0, currentDist)

    output.append(0)

    currentDist = 0
    for j in range(i + 1, 4, 1):
        currentDist += dist[j]
        output.append(currentDist)

    for num in output:
        print(num, end=" ")
    print()



# ------------------------------------------------------------

# CCC 2019 J3 - Cold Compress

# Input
# 4
# +++===!!!!
# 777777......TTTTTTTTTTTT
# (AABBC)
# 3.1415555

# Output
# 3 + 3 = 4 !
# 6 7 6 . 12 T
# 1 ( 2 A 2 B 1 C 1 )
# 1 3 1 . 1 1 1 4 1 1 4 5

# Approach 1: Using hard cord computing
# n = int(input())
# strings = []
# for i in range(n):
#     strings.append(input())
#
# for line in strings:
#     prev = ""
#     output = ""
#     counter = 1
#     for letter in line:
#         if prev == "":
#             prev = letter
#             continue
#         if letter != prev:
#             output += str(counter) + " " + str(prev) + " "
#             counter = 1
#         else:
#             counter += 1
#         prev = letter
#     output += str(counter) + " " + str(prev) + " "
#     print(output)

# Approach 2: Using dictionary to count

# for i in range(int(input())):
#     chars = {}
#     for j in input():
#         if j not in chars:
#             chars[j] = 1;
#         else:
#             chars[j] += 1;
#     for (key, value) in chars.items():
#         print(value, end=" ")
#         print(key, end=" ")
#     print("\n")



