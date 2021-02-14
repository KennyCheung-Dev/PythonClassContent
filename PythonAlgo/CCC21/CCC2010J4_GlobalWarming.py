def ExposePattern(intList):
    stringList = []
    for i in range(1, len(intList)):
        stringList.append(str(intList[i] - intList[i-1]))
    return stringList

# print(ExposePattern([1, 3, 2, 2, 4, 3, 3, 5, 4]))

def ContainsPattern(list1, list2):
    match = True
    for i in range(len(list2)):
        if list1[i] != list2[i]:
            match = False
            break
    return match

# -1 -1 +2 -1 -1 +2 -1 -1
# Pattern : -1 -1 +2


def CheckPattern(length, list):
    pattern = list[0:length]
    for i in range(0, len(list), length):
        if len(list) - i < length:
            split = list[i:len(list)]
            if not ContainsPattern(pattern, split):
                return False
        else:
            split = list[i:i+length]
            if not pattern == split:
                return False
    return True


while True:
    num = []
    for i in input().strip().split(" "):
        num.append(int(i))
    if num[0] == 0:
        break
    num.pop(0)

    # [2, 3, 2, 3, 2, 3,2, 3,3,5,4]
    # +1 -1 +1 -1 ....
    pattern = ExposePattern(num)
    shortestPattern = len(pattern)
    for i in range(len(pattern), 0, -1):
        if CheckPattern(i, pattern):
            if i < shortestPattern:
                shortestPattern = i
    print(shortestPattern)



