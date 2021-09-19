'''
1 2 3 5
6 0 10 4
2 1 8 3
'''

bill1 = [int(i) for i in input().split(" ")]
bill2 = [int(i) for i in input().split(" ")]
truck = [int(i) for i in input().split(" ")]

def FindOverlap(bill, truck):
    lowerLeftX = max(bill[0], truck[0])
    lowerLeftY = max(bill[1], truck[1])
    upperRightX = min(bill[2], truck[2])
    upperRightY = min(bill[3], truck[3])
    overlappingArea = (upperRightX - lowerLeftX) * (upperRightY - lowerLeftY)
    return overlappingArea

def CalculateArea(bill):
    return (bill[2] - bill[0]) * (bill[3] - bill[1])

print(CalculateArea(bill1) - FindOverlap(bill1, truck) + CalculateArea(bill2) - FindOverlap(bill2, truck))



