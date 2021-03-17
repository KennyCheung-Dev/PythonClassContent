# N person forms a circle, everyone starts counting, the Mth person is killed
# Next round of counting starts with the next person
# Find the last person alive
# 6 5
# 1 2 3 4 5 6
# 1 2 3 4 6
# 1 2 3 6
# 1 2 3
# 1 3
# 1

def JosephsProblemRecur(N, M, personLeft, indexToStart):
    if N <= 1:
        return personLeft[0]
    else:
        indexToRemove = ((M % N) - 1 + indexToStart) % N
        personLeftCopy = personLeft.copy()
        personLeftCopy.pop(indexToRemove)
        indexToStart = indexToRemove % (N - 1)
        return JosephsProblemRecur(N-1, M, personLeftCopy, indexToStart)

personLeft = []
line = input().split(" ")
for i in range(int(line[0])):
    personLeft.append(i + 1)
print(JosephsProblemRecur(int(line[0]), int(line[1]), personLeft, 0))


# def JosephsProblemRecur(depth, N, M):
#     if depth == N:
#         personLeft = []
#         for i in range(N):
#             personLeft.append(i + 1)
#         indexToRemove = ((M % N) - 1) % depth
#         personLeft.pop(indexToRemove)
#         indexToStart = indexToRemove % (N - 1)
#         return [personLeft, indexToStart]
#     else:
#         result = JosephsProblemRecur(depth + 1, N, M)
#         if depth > 1:
#             personLeft = result[0].copy()
#             indexToStart = result[1]
#             indexToRemove = ((M % depth) - 1 + indexToStart) % depth
#             personLeft.pop(indexToRemove)
#             indexToStart = indexToRemove % (depth - 1)
#             return [personLeft, indexToStart]
#         else:
#             return result[0][0]
#
# line = input().split(" ")
# print(JosephsProblemRecur(1, int(line[0]), int(line[1])))