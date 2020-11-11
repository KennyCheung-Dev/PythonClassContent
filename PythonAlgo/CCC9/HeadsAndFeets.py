'''
There were 35 heads
There was at least one chicken and at most 34
There were 94 feets
There was at least one rabbit and at most 23
Figure out how many chickens and how many rabbits there are

Output:
print:
Answer: XX chicken and YY rabbit
'''

# 23 chicken and 12 rabbit


[[print("Answer: {} chicken and {} rabbit".format(i, j)) if (i * 2 + j * 4 == 94 and i + j == 35) else print("", end="") for j in range(35)] for i in range(35)]

# for i in range(35):
#     for j in range(35):
#         if i * 2 + j * 4 == 94 and i + j == 35:
#             print("Answer: {} chicken and {} rabbit".format(i, j))

