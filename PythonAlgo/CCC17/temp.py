# if "C".isupper():
#
#
# print("C".lower())
# print("C".upper())

#
# word = input()
#
# for i in word:
#     if i.isupper():
#         print(i)

parentA = input()
parentB = input()
possibleAlelles = []
for i in range(0, 10, 2):
    for j in range(i, i+2):
        for k in range(i, i+2):
            if parentA[j].isupper() or parentB[k].isupper():
                if parentA[j].upper() not in possibleAlelles:
                    possibleAlelles.append(parentA[j].upper())
            else:
                if parentA[j].lower() not in possibleAlelles:
                    possibleAlelles.append(parentA[j].lower())

for i in range(int(input())):
    child = input()  #ABcDe
    isPossibleChild = True
    for alelle in child:
        if alelle not in possibleAlelles:
            isPossibleChild = False
    if isPossibleChild:
        print("Possible baby.")
    else:
        print("Not their baby!")
