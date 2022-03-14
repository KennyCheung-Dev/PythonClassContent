'''


Combination Problem

Wayne is learning combination, and wanted to solve the following question:
http://oj.ysacode.com/problem.php?id=1075


Tips: 
You can use math.factorial(x)

Tips: 
You can create a helper function to find combinations



'''

# import math
#
# def Combination(x, y):
#     xF = math.factorial(x)
#     yF = math.factorial(y)
#     xminusyF = math.factorial(x-y)
#     return xF / (yF * xminusyF)
#
# n, p, k, r = [int(i) for i in input().split()]
# i = 0
# accumulate = 0
# while (True):
#     x = i * k + r
#     y = n * k
#     if x > y:
#         break
#     accumulate = (accumulate + Combination(y, x)) % p
#     i += 1
#
# print(int(accumulate))




'''
http://oj.ysacode.com/problem.php?id=1029

'''

n, m, p = [int(i) for i in input().split()]

listOfPrime = []
overall = []
for i in range(2, m+1):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
    if isPrime:
        listOfPrime.append(i)

def Recur(usedNums, selectedNum, position):
    usedNums = usedNums.copy()
    usedNums.append(selectedNum)
    position += 1
    if position == n:
        sum = 0
        hasPrime = False
        for i in usedNums:
            if i in listOfPrime:
                hasPrime = True
            sum += i
        if not hasPrime:
            return 0
        if sum % p == 0:
            overall.append(usedNums)
            return 1
        else:
            return 0
    acc = 0
    for i in range(1, m + 1):
        if i not in usedNums:
            acc += Recur(usedNums, i, position)
    return acc

sum = 0
for i in range(1, m + 1):
    sum += Recur([], i, 0)
print(sum)
print(overall)