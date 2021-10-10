# https://codeforces.com/contest/1216/problem/C

'''
Samples:

inputCopy
2 2 4 4
1 1 3 5
3 1 5 5
outputCopy
NO

inputCopy
3 3 7 5
0 0 4 6
0 0 7 4
outputCopy
YES

inputCopy
5 2 10 5
3 1 7 6
8 1 11 7
outputCopy
YES

inputCopy
0 0 1000000 1000000
0 0 499999 1000000
500000 0 1000000 1000000
outputCopy
YES

'''


sheets = []
for i in range(3):
    sheets.append([int(i) for i in input().split()])

def White():
    return sheets[0]

def Black1():
    return sheets[1]

def Black2():
    return sheets[2]

def Area(sheet):
    return (sheet[3] - sheet[1]) * (sheet[2] - sheet[0])

def OverlapArea(sheets):
    bottomLeftXs = [sheet[0] for sheet in sheets]
    bottomLeftYs = [sheet[1] for sheet in sheets]
    topRightXs = [sheet[2] for sheet in sheets]
    topRightYs = [sheet[3] for sheet in sheets]
    overlappingX = max(0, min(topRightXs) - max(bottomLeftXs))
    overlappingY = max(0, min(topRightYs) - max(bottomLeftYs))
    return overlappingX * overlappingY

def FullyCover():
    whiteCovered = OverlapArea([White(), Black1()]) + OverlapArea([White(), Black2()])
    all3Overlap = OverlapArea(sheets)
    print(whiteCovered)
    print(all3Overlap)
    print(Area(White()))
    return (whiteCovered - all3Overlap) == Area(White())

print(FullyCover())