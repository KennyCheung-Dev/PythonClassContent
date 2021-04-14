from collections import deque

class Graph:
    def __init__(self):
        self.order = []
        self.neighbour = {}

    def addNode(self, node):
        key, val = node
        if not isinstance(val, list):
            print("Node has to be a list with length of 2")
        else:
            self.neighbour[key] = val


    def BFS(self, root):
        search_queue = deque()
        search_queue.append(root)
        visited = []

        while search_queue:
            person = search_queue.popleft()
            self.order.append(person)

            if not person in visited and person in self.neighbour.keys():
                search_queue += self.neighbour[person]
                visited.append(person)

    def DFS(self, root):
        search_queue = deque()
        search_queue.append(root)
        visited = []

        while search_queue:
            person = search_queue.popleft()
            self.order.append(person)

            if not person in visited and person in self.neighbour.keys():
                tmp = self.neighbour[person]
                tmp.reverse()

                for index in tmp:
                    search_queue.appendleft(index)

                visited.append(person)



g = Graph()

g.addNode(["A", ["B", "C"]])
g.addNode(["B", ["D", "E"]])
g.addNode(["C", ["F"]])
g.addNode(["D", []])
g.addNode(["E", []])
g.addNode(["F", []])

g.DFS("A")
# g.BFS("A")

print(g.order)