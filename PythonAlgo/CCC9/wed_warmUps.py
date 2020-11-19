# Warmup
# print the following:
'''
*
**
***
****
*****
'''

# for i in range(1, 30):
#     print("*" * i)


'''
Print the multiplication table:
1 * 1 = 1 | 1 * 2 = 2 | 1 * 3 ...
2 * 1 = 2 | ...
....... | 9 * 9 = 81
'''
for i in range(1, 10):
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i*j), end="")
        if j != 9:
            print(" | ", end="")
    print()






'''
There are 35 heads.
There was at least one chicken and at most 34.
There was 94 feet 
There was at least one rabbit and at most 23
Figure out how many chickens and rabbit there are
Output print: 
There are 23 chickens and 12 rabbit
'''
# for i in range(1, 35):
#     for j in range(1, 23):
#         if i + j == 35 and (2 * i) + (4 * j) == 94:
#             print("There are {} chicken and {} rabbit".format(i, j))
#
# for i in range(1, 35):
#     chicken = i
#     rabbit = 35 - i
#     if (2 * chicken) + (4 * rabbit) == 94:
#         print("There are {} chicken and {} rabbit".format(chicken, rabbit))





# Note Frequency
# def NoteFrequency(a, b):
#     return (440 * (2 ** ((a - 4) + ((b - 9) / 12))))
#
# print(NoteFrequency(0, 0))


import random
print(random.randint(1, 500))

# 1
# 1a. Instantiate an int 2-dimension array of random numbers (use random)
# 1b. Extract and print the number at 2nd row, 1st column
# 1c. Extract and print the 2nd row numbers into individual rows
# 1d. Print the 2d array in the following format:
# x / y / z
# x / y / z
# x / y / z

# 1e. Reverse and print the array :
# Example:
# 1 | 2 | 3
# 4 | 5 | 6
# 7 | 8 | 9
# Output:
# 9 | 8 | 7
# 6 | 5 | 4
# 3 | 2 | 1

# 1f. Make this into a function, that takes in a 2d list of int, with ANY SIZE 3x3, 5x5, 9x9

#1a
li = [[], [], []]
for i in range(3):
    for j in range(3):
        li[i].append(random.randint(0, 500))
#1b
print(li)
#1c
print(li[1][0])
for num in li[1]:
    print(num)

#1d
for i in range(len(li)):
    for j in range(len(li[0])):
        print(li[i][j], end="")
        if j != len(li[0]) - 1:
            print(" | ", end="")
    print()

print()

#1e
# for i in range(len(li[0])):
#     li[i].reverse()
# li.reverse()

# for i in range(len(li)):
#     for j in range(len(li[0])):
#         print(li[i][j], end="")
#         if j != len(li[0]) - 1:
#             print(" | ", end="")
#     print()

for i in range(len(li) - 1, -1, -1):
    for j in range(len(li[0]) - 1, -1, -1):
        print(li[i][j], end="")
        if j != 0:
            print(" | ", end="")
    print()






