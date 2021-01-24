def ExposePattern(intList):
    stringList = []
    for i in range(1, len(intList)):
        stringList.append(str(intList[i] - intList[i-1]))
    return stringList

def ContainsPattern(list1, list2):
    match = True
    for i in range(len(list2)):
        if list1[i] != list2[i]:
            match = False
            break
    return match

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
    # nums = [int(i) for i in input().split(" ")]
    nums = []
    for i in input().split(" "):
        if i != "":
            nums.append(int(i))
    if nums[0] == 0:
        break
    nums.pop(0)

    pattern = ExposePattern(nums)
    shortestPattern = len(pattern)
    for i in range(len(pattern), 0, -1):
        if CheckPattern(i, pattern):
            if i < shortestPattern:
                shortestPattern = i

    print(shortestPattern)