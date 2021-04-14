pairs = []
# 6 5
line = input().split(" ")  #[6, 5]
x = int(line[0])
y = int(line[1])
line = input().split(" ")
targetX = int(line[0])
targetY = int(line[1])
stepDisplacements = [(1, 2),
                     (2, 1),
                     (2, -1),
                     (1, -2),
                     (-1, -2),
                     (-2, -1),
                     (-2, 1),
                     (-1, 2)]

def Horse(x, y, depth):
    global pairs
    global targetX
    global targetY
    if x == targetX and y == targetY:
        return depth

    if (x, y, depth) in pairs:
        return -1
    pairs.append((x, y, depth))

    if x < 1 or x > 8 or y < 1 or y > 8:
        return -1

    if depth >= 7:
        return -1

    global stepDisplacements
    lowestSteps = -1
    for xDis, yDis in stepDisplacements:
        temp = Horse(x + xDis, y + yDis, depth + 1)
        if temp != -1:
            if  lowestSteps == -1:
                lowestSteps = temp
            elif temp < lowestSteps:
                lowestSteps = temp
    return lowestSteps

print(Horse(x, y, 0))