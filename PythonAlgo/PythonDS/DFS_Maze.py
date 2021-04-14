# 5 6
# ....S*
# .***..
# .*..*.
# *.***.
# .T....

# Output:
# ....S*
# .***LL
# .*..*L
# *.***L
# .TLLLL

# S = Start
# T = Target

maze = []
line = input().split(" ")
m = int(line[0])
n = int(line[1])
turn = [[-1, 0], [0, -1], [1, 0], [0, 1]]
vis = [[0 for i in range(n)] for j in range(m)]
for i in range(m):
    maze.append(list(input()))
for i in range(m):
    for j in range(n):
        if maze[i][j] == "S":
            x = i
            y = j


def InRange(x, y):
    return 0 <= x < m and 0 <= y < n

def DFS(x, y):
    if maze[x][y] == "T":
        return True
    vis[x][y] = 1
    if maze[x][y] != "S":
        maze[x][y] = "L"
    for i in range(4):
        tx = x + turn[i][0]
        ty = y + turn[i][1]
        if not vis[tx][ty] and maze[tx][ty] != "*" and InRange(tx, ty):
            print(tx, ty)
            if DFS(tx, ty):
                return True
    vis[x][y] = 0
    maze[x][y] = "."
    return False

if DFS(x, y):
    for temp in maze:
        print(" ".join(temp))
else:
    print("Maze has no solution")


