def FlipHorizontal(square):
    line1 = square[0]
    square[0] = square[1]
    square[1] = line1
    return square

def FlipVertical(square):
    topLeft = square[0][0]
    bottomLeft = square[1][0]
    square[0][0] = square[0][1]
    square[1][0] = square[1][1]
    square[0][1] = topLeft
    square[1][1] = bottomLeft
    return square

sequence = input()
h = sequence.count("H")
v = sequence.count("V")

square = [[1, 2], [3, 4]]

if h % 2 == 1:
    FlipHorizontal(square)
if v % 2 == 1:
    FlipVertical(square)

for i in square:
    print(i[0], end=" ")
    print(i[1])
