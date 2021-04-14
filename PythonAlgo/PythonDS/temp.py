dict = []

def PuttingApplesRecur(applesLeft, platesLeft, distribution):
    global dict
    if platesLeft == 1:
        distributionCopy = distribution.copy()
        distributionCopy.append(applesLeft)
        distributionCopy.sort()

        if not distributionCopy in dict:
            dict.append(distributionCopy)
            return 1
        else:
            return 0

    tempCount = 0
    for i in range(0, applesLeft + 1):
        distributionCopy = distribution.copy()
        distributionCopy.append(i)
        tempCount += PuttingApplesRecur(applesLeft - i,
                                        platesLeft - 1,
                                        distributionCopy)
    return tempCount

print(PuttingApplesRecur(7, 3, []))


















