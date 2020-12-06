sq = int(input())
side = 1
lastUsableSide = 1
while True:
    if side * side > sq:
        print(lastUsableSide)
        break
    else:
        lastUsableSide = side
    side += 1