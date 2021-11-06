def Height(m, x):
    if m >= 1:
        power = 5 ** (m-1)
        location = x // power
        if location == 0 or location == 4:
            return 0
        elif location == 1 or location == 3:
            return 1 * power + Height(m-1, x % power)
        elif location == 2:
            return 2 * power + Height(m-1, x % power)
    return 0
for i in range(int(input())):
    m, x, y = [int(i) for i in input().split()]



    # if m >= 1:
    #     if x == 0 or x == 4:
    #         return 0
    #     elif x == 1 or x == 3:
    #         return 1 + Height(m - 1, x)
    #     elif x == 2:
    #         return 2



        # xForOneLevelLower = x // 5
        # xForThisLevel = x % (5 ** (m-1))
        # yForOneLevelLower = Height(m - 1, xForOneLevelLower)
        # if yForOneLevelLower == 0:
        #     return 0
        # bottomCubesHeight = yForOneLevelLower * 5
        # return Height(1, xForThisLevel) + bottomCubesHeight
# print(Height(3, 60))