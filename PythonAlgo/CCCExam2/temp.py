def RecursivePropegate(currentPos):  # [2, 4]
    if not currentPos in arr:
        arr.append([currentPos[0], currentPos[1]])

    if currentPos[0] + 1 < width:
        if matrix[currentPos[0] + 1][currentPos[1]] == ".":
            if not [currentPos[0] + 1, currentPos[1]] in arr:
                arr.append([currentPos[0] + 1, currentPos[1]])
                RecursivePropegate([currentPos[0] + 1, currentPos[1]])

    if currentPos[0] - 1 >= 0:
        if matrix[currentPos[0] - 1][currentPos[1]] == ".":
            if not [currentPos[0] - 1, currentPos[1]] in arr:
                arr.append([currentPos[0] - 1, currentPos[1]])
                RecursivePropegate([currentPos[0] - 1, currentPos[1]])

    if currentPos[1] - 1 >= 0:
        if matrix[currentPos[0]][currentPos[1] - 1] == ".":
            if not [currentPos[0], currentPos[1] - 1] in arr:
                arr.append([currentPos[0], currentPos[1] - 1])
                RecursivePropegate([currentPos[0], currentPos[1] - 1])

    if currentPos[1] + 1 < height:
        if matrix[currentPos[0]][currentPos[1] + 1] == ".":
            if not [currentPos[0], currentPos[1] + 1] in arr:
                arr.append([currentPos[0], currentPos[1] + 1])
                RecursivePropegate([currentPos[0], currentPos[1] + 1])




arr = []
width, height = [int(i) for i in input().split(" ")]
matrix = []
for i in range(width):
    matrix.append([])

#Grab Input:
for i in range(width):
    line = input()
    for j in range(height):
        matrix[i].append(line[j])

for i in range(width):
    for j in range(height):
        if matrix[i][j] == "*":
            arr.clear()
            RecursivePropegate([i, j])
            matrix[i][j] = len(arr) % 10

for i in range(width):
    for j in range(height):
        print(matrix[i][j], end="")
    print()
