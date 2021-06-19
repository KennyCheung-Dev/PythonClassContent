max = 999999
node = {
    "a" : [[["b", 3], ["c", 4]], 0, ""],
    "b" : [[["c", 0.5]], max, ""],
    "c" : [[["b", 0.5], ["d", 1]], max, ""],
    "d" : [[["c", 1]], max, ""]
}

visited = {
    "a" : False,
    "b" : False,
    "c" : False,
    "d" : False
}

currentNode = "a"

for i in range(4):
    visited[currentNode] = True
    # Updating distance on connecting points
    for n in node[currentNode][0]:
        if n[1] + node[currentNode][1] < node[n[0]][1]:
            node[n[0]][1] = n[1] + node[currentNode][1]
            node[n[0]][2] = currentNode
    #Choosing a next point to visit
    minCost = max
    nextNode = ""
    for n in node[currentNode][0]:
        if node[n[0]][1] < minCost:
            minCost = node[n[0]][1]
            nextNode = n[0]
    currentNode = nextNode

for i in node.items():
    print(i)

