x, y = [int(i) for i in input().split(' ')]
currentPos = x;
destination = x;
displacement = 1;
traveled = 0;
while True:
    destination = x + displacement
    if y >= currentPos and y <= destination or y <= destination and y >= currentPos:
        traveled += abs(currentPos - y)
        break
    else:
        traveled += abs(destination - currentPos)
        currentPos = destination
    displacement *= -2;
print(traveled);