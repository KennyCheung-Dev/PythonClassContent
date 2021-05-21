# class Animal:
#     def __init__(self, Name ,EnteredHP):
#         self.HP = EnteredHP
#         self.Name = Name
#
#     def Speak(self):
#         print("hi I am " + str(self.HP) + " years old")
#
# myDog = Animal("Mojo", 100)
# mySecondDog = Animal("Blue", 20)
# myFirstrex = Animal("rex", 'always stupid and an idiot and no')
#
# print(myDog.Name)
# print(mySecondDog.Name)
# print(myFirstrex.Name)
# mySecondDog.Speak()
# myFirstrex.Speak()






# from collections import deque
#
# class Graph:
#     def __init__(self):
#         self.order = []
#         self.neighbour = {}
#
#     def addNode(self, node): # node : ["A", ["B", "C"]] ["B", ["D", "E"]],
#         key, val = node
#         self.neighbour[key] = val
#
#     def BFS(self, root):
#         search_queue = deque()
#         search_queue.append(root)
#         visited = []
#
#         while search_queue:
#             person = search_queue.popleft()
#             self.order.append(person)
#
#             if not person in visited and person in self.neighbour.keys():
#                 search_queue += self.neighbour[person]  #person = "B"
#                 visited.append(person)
#
#     def DFS(self, root):
#         search_queue = deque()
#         search_queue.append(root)
#         visited = []
#
#         while search_queue:
#             person = search_queue.popleft()
#             self.order.append(person)
#
#             if not person in visited and person in self.neighbour.keys():
#                 tmp = self.neighbour[person]
#
#                 tmp.reverse()
#
#                 for index in tmp:
#                     search_queue.appendleft(index)
#
#                 visited.append(person)
#         # Depth First Search
#         # Breadth First Search
#
# g = Graph()
# g.addNode(["A", ["Q", "B", "D"]])
# g.addNode(["B", ["C", "E"]])
# g.DFS("A")
# print(g.order)

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

# maze = []
# line = input().split(" ")
# m = int(line[0])
# n = int(line[1])
# turn = [[-1, 0], [0, -1], [1, 0], [0, 1]]
# vis = [[0 for i in range(n)] for j in range(m)]
# for i in range(m):
#     maze.append(list(input()))
# for i in range(m):
#     for j in range(n):
#         if maze[i][j] == "S":
#             x = i
#             y = j
#
# def InRange(x, y):
#     return 0 <= x < m and 0 <= y < n
#
# def DFS(x, y):
#     pass
#     #BaseCase Check if the current location from (x,y) is the target
#     #print soething in base case to ensure that it finds the target
#     #Visited has to record that you have visited this location
#
#     #Loop through all 4 directions I can go
#         # Check if previously visited
#         # Check if it is a wall
#         # Check if it is in range
#             # If so, Recursively call
#
# if DFS(x, y):
#     for temp in maze:
#         print(" ".join(temp))
# else:
#     print("Maze has no solution")



def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, high, x)
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
    else:
        return -1

num = [1, 1, 2, 3, 5, 8, 13]
print(binary_search(num, 0, len(num) - 1, -5))






















