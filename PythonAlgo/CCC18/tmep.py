def CheckDirEmpty(s, x, y):
    if s == "up":
        if x - 1 < 0:
            return False
        return True if spiral[x - 1][y] == -1 else False
    elif s == "down":
        if x + 1 >= layers:
            return False
        return True if spiral[x + 1][y] == -1 else False
    elif s == "left":
        if y - 1 < 0:
            return False
        return True if spiral[x][y - 1] == -1 else False
    elif s == "right":
        if y + 1 >= layers:
            return False
        return True if spiral[x][y + 1] == -1 else False
    else:
        return False

low = int(input())
high = int(input())

numAmount = high + 1 - low
layers = 2
while True:
    if numAmount <= layers ** 2:
        break
    layers += 1

# [[1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [],
#  [],
#  []]


spiral = []
for i in range(layers):
    spiral.append([])
    for j in range(layers):
        spiral[i].append(-1)

x = layers//2
y = layers//2
if layers % 2 == 0:
    x-=1
    y-=1

nextNum = low
spiral[x][y] = nextNum
currentMovingDirection = "down"
while True:
    if nextNum + 1 > high: break
    if currentMovingDirection == "up":
        while True:
            if nextNum + 1 > high: break
            nextNum += 1
            x -= 1
            # print("Accessing coordinates: " + str(x) + " " + str(y))
            spiral[x][y] = nextNum
            if CheckDirEmpty("left", x, y):
                currentMovingDirection = "left"
                break
    elif currentMovingDirection == "down":
        while True:
            if nextNum + 1 > high: break
            nextNum += 1
            x += 1
            # print("Accessing coordinates: " + str(x) + " " + str(y))
            spiral[x][y] = nextNum
            if CheckDirEmpty("right", x, y):
                currentMovingDirection = "right"
                break
    elif currentMovingDirection == "left":
        while True:
            if nextNum + 1 > high: break
            nextNum += 1
            y -= 1
            # print("Accessing coordinates: " + str(x) + " " + str(y))
            spiral[x][y] = nextNum
            if CheckDirEmpty("down", x, y):
                currentMovingDirection = "down"
                break
    elif currentMovingDirection == "right":
        while True:
            if nextNum + 1 > high: break
            nextNum += 1
            y += 1
            # print("Accessing coordinates: " + str(x) + " " + str(y))
            spiral[x][y] = nextNum
            if CheckDirEmpty("up", x, y):
                currentMovingDirection = "up"
                break

for i in range(layers):
    for j in range(layers):
        if spiral[i][j] != -1:
            print(spiral[i][j], end="")
            print(" ", end="")
    print()

    