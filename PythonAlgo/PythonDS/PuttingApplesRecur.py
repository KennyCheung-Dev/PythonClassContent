# Put M identical apples on N identical plates,
# allow some plates to be left empty.
# how many different methods are there? (indicated by K).
# Notice that 5,1,1 and 1,5,1 are the same method.

# Input:
# The first line is the number t of test data (0 <= t <= 20).
# Each of the following t lines contains two integers M and N separated by space. 1<=M, N<=10.

# Output:
# For each set of data M and N entered, output the corresponding K in one line.

'''
Example:
Input
1
7 3

Output:
8

'''


'''
combinations = []

Method(applesLeft, platesLeft, distribution):
    if platesLeft = 1:
        Check if your final combinations has already been considered
        If its viable:
            return 1
        else
            return 0
    else:
        Recursively continue counting subsequent combinations
        Lets say you are at 2/4 slots
        For every possible 3rd slot option,
        You need to recursively count THEIR subsequent 
        number of combinations that works
        
        count = 0
        for i in range(MaxPossibleApple):
            count += Method(appleLeft - i, platesLeft - 1, distribution)
        return count
'''






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
    else:
        maxAppleThisPlate = applesLeft - platesLeft
        tempCount = 0
        for i in range(0, maxAppleThisPlate + 1):
            distributionCopy = distribution.copy()
            distributionCopy.append(i)
            tempCount += PuttingApplesRecur(applesLeft - i, platesLeft - 1, distributionCopy)
        return tempCount

for i in range(int(input())):
    test = input().split(" ")
    print(PuttingApplesRecur(int(test[0]), int(test[1]), []))

print(dict)

































