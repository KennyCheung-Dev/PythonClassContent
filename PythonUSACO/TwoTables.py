'''
Problem:
https://codeforces.com/problemset/problem/1555/B
'''

'''
You have an axis-aligned rectangle room with width 𝑊 and height 𝐻, so the lower left corner is in point (0,0) and the upper right corner is in (𝑊,𝐻).

There is a rectangular table standing in this room. The sides of the table are parallel to the walls, the lower left corner is in (𝑥1,𝑦1), and the upper right corner in (𝑥2,𝑦2).

You want to place another rectangular table in this room with width 𝑤 and height ℎ with the width of the table parallel to the width of the room.

The problem is that sometimes there is not enough space to place the second table without intersecting with the first one (there are no problems with tables touching, though).

You can't rotate any of the tables, but you can move the first table inside the room.

Example of how you may move the first table.
What is the minimum distance you should move the first table to free enough space for the second one?

Input
The first line contains the single integer 𝑡 (1≤𝑡≤5000) — the number of the test cases.

The first line of each test case contains two integers 𝑊 and 𝐻 (1≤𝑊,𝐻≤108) — the width and the height of the room.

The second line contains four integers 𝑥1, 𝑦1, 𝑥2 and 𝑦2 (0≤𝑥1<𝑥2≤𝑊; 0≤𝑦1<𝑦2≤𝐻) — the coordinates of the corners of the first table.

The third line contains two integers 𝑤 and ℎ (1≤𝑤≤𝑊; 1≤ℎ≤𝐻) — the width and the height of the second table.

Output
For each test case, print the minimum distance you should move the first table, or −1 if there is no way to free enough space for the second table.

Your answer will be considered correct if its absolute or relative error doesn't exceed 10−6.

Example
inputCopy
5
8 5
2 1 7 4
4 2
5 4
2 2 5 4
3 3
1 8
0 3 1 6
1 5
8 1
3 0 6 1
5 1
8 10
4 5 7 8
8 5
outputCopy
1.000000000
-1
2.000000000
2.000000000
0.000000000
Note
The configuration of the first test case is shown in the picture. But the movement of the first table is not optimal. One of the optimal movement, for example, is to move the table by (0,−1), so the lower left corner will move from (2,1) to (2,0). Then you can place the second table at (0,3)−(4,5).

In the second test case, there is no way to fit both tables in the room without intersecting.

In the third test case, you can move the first table by (0,2), so the lower left corner will move from (0,3) to (0,5).
'''

for i in range(int(input())):
    room = [int(j) for j in input().split()]
    firstTable = [int(j) for j in input().split()]
    secondTable = [int(j) for j in input().split()]

    # Check if enough space is given
    if (firstTable[0] - 0) + (room[0] - firstTable[2]) >= secondTable[0]: # Enough space on width
        biggerGap = max(firstTable[0] - 0, room[0] - firstTable[2])
        difference = abs(biggerGap - secondTable[0])
        print(difference)
    elif (firstTable[1] - 0) + (room[1] - firstTable[3]) >= secondTable[1]:
        biggerGap = max(firstTable[1] - 0, room[1] - firstTable[3])
        difference = abs(biggerGap - secondTable[1])
        print(difference)
    else:
        print(-1)


