from collections import deque

class Graph:
    def __init__(self):
        self.order = []
        self.neighbour = {}

    def addNode(self, node): # node : ["A", ["B", "C"]] ["B", ["D", "E"]],
        key, val = node
        self.neighbour[key] = val

    def BFS(self, root):
        search_queue = deque()
        search_queue.append(root)
        visited = []

        while search_queue:
            person = search_queue.popleft()
            self.order.append(person)

            if not person in visited and person in self.neighbour.keys():
                search_queue += self.neighbour[person]  #person = "B"
                visited.append(person)


g = Graph()
g.addNode(["A", ["B", "C"]])
g.addNode(["B", ["D", "E"]])
g.addNode(["C", ["F"]])
g.BFS("A")
print(g.order)
