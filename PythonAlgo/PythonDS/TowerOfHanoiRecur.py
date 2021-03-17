from copy import deepcopy

towers = [[], [], []]
numPlate = int(input())
for i in range(numPlate):
    towers[0].append(numPlate - i)

def Letter(i):
    return "A" if i == 0 else "B" if i == 1 else "C"

def HanoiRecur(num, fromRod, toRod, auxRod):
    global towers
    if num == 1:
        towers[toRod].append(towers[fromRod][-1])
        towers[fromRod].pop(-1)
        print(str(towers[toRod][-1]) + " " + Letter(fromRod) + " " + Letter(toRod))
    else:
        HanoiRecur(num - 1, fromRod, auxRod, toRod)
        towers[toRod].append(towers[fromRod][-1])
        towers[fromRod].pop(-1)
        print(str(towers[toRod][-1]) + " " + Letter(fromRod) + " " + Letter(toRod))
        HanoiRecur(num - 1, auxRod, toRod, fromRod)

HanoiRecur(numPlate, 0, 1, 2)
