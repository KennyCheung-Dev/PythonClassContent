'''
Beibao

There is a bag you can fill in with items
Items can be cut into different portions freely
Each item has the its amount worth, and the weight

First line contains m n   (e.g. 150 7) where m represents the weight that would fit
The next n lines will represents (n-1)th item's amount worth and weight

Please find out the max amount worth that can fit in the bag

Input:
150 7
10 35
40 30
30 60
50 50
35 40
40 10
30 25

Output:
190.625

'''

weightFit, numItem = [int(i) for i in input().split(" ")]
weightFilled = 0
amountFilled = 0
items = []
for i in range(numItem):
    newItem = [int(i) for i in input().split(" ")]
    newItem.append(newItem[0] / newItem[1])
    items.append(newItem)

def NextHighestRatioItem():
    global items
    tempHighestIndex = 0
    tempHighestRatio = items[0][2]
    for i in range(1, len(items)):
        if items[i][2] > tempHighestRatio:
            tempHighestIndex = i
            tempHighestRatio = items[i][2]
    highestItem = items.pop(tempHighestIndex)
    return highestItem

while weightFilled < weightFit and len(items) > 0:
    nextItem = NextHighestRatioItem()
    space = weightFit - weightFilled
    if space >= nextItem[1]:
        amountFilled += nextItem[0]
        weightFilled += nextItem[1]
    else:
        percentageCut = space / nextItem[1]
        amountFilled += nextItem[0] * percentageCut
        weightFilled += nextItem[1] * percentageCut
        break

print(amountFilled)

