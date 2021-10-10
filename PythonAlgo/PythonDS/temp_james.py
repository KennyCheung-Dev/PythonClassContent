
# word = "abcde"

# for i in range(len(word)):
#     for j in range(i + 1, len(word) + 1):
#         print(i, j)
#         print(word[i:j])


#for i in range(4):
#     for j in range(4):
#         for k in range(4):
#             print(i, j, k)

# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             print(i, j, k)

firstLine = input()  # "3 3"
splitLine = firstLine.split()  # ['3', '3']
for i in range(len(splitLine)):
    splitLine[i] = int(splitLine[i])
    # [3, 3]
print(splitLine)


# line = [int(i) for i in input().split()]
# print(line)


