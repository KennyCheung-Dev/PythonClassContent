parentA = input()
parentB = input()
possibleAlelles = []
for i in range(0, 10, 2):
    for j in range(i, i + 2):
        for k in range(i, i+2):
            if parentA[j].isupper() or parentB[k].isupper():
                possibleAlelles.append(parentA[j].upper())
            else:
                possibleAlelles.append(parentA[j].lower())

childNum = int(input())
for i in range(childNum):
    child = input()
    isPossibleChild = True
    for alelle in child:
        if alelle not in possibleAlelles:
            isPossibleChild = False
    print("Possible baby." if isPossibleChild else "Not their baby!")
