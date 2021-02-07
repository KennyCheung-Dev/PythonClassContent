passedCoords = [
    [0, -1],
    [0, -2],
    [0, -3],
    [1, -3],
    [2, -3],
    [3, -3],
    [3, -4],
    [3, -5],
    [4, -5],
    [5, -5],
    [5, -4],
    [5, -3],
    [6, -3],
    [7, -3],
    [7, -4],
    [7, -5],
    [7, -6],
    [7, -7],
    [6, -7],
    [5, -7],
    [4, -7],
    [3, -7],
    [2, -7],
    [1, -7],
    [0, -7],
    [-1, -7],
    [-1, -6],
    [-1, -5],
]

currentCoord = [-1, -5]

safe = True
while True:
    line = input().split(" ")
    if line[0] == "q":
        break
    for i in range(int(line[1])):
        if line[0] == "u":
            currentCoord[1] += 1
        elif line[0] == "d":
            currentCoord[1] -= 1
        elif line[0] == "l":
            currentCoord[0] -= 1
        elif line[0] == "r":
            currentCoord[0] += 1
        if currentCoord in passedCoords:
            safe = False
        else:
            passedCoords.append(currentCoord.copy())
    print(str(currentCoord[0]) + " " + str(currentCoord[1]) + " " + ("safe" if safe else "DANGER"))
    if not safe:
        break

