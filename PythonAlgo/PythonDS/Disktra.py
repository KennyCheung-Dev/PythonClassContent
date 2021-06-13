def dijkstra(graph, startIndex, path, cost, max):
    lenth = len(graph)
    v = [0] * lenth
    # Initialize path，cost，V
    for i in range(lenth):
        if i == startIndex:
            v[startIndex] = 1
        else:
            cost[i] = graph[startIndex][i]
            path[i] = (startIndex if (cost[i] < max) else -1)

    for i in range(1, lenth):
        minCost = max
        curNode = -1
        for w in range(lenth):
            if v[w] == 0 and cost[w] < minCost:
                minCost = cost[w]
                curNode = w
        # for obtaining the lowest point already
        if curNode == -1: break
        v[curNode] = 1
        for w in range(lenth):
            if v[w] == 0 and (graph[curNode][w] + cost[curNode] < cost[w]):
                cost[w] = graph[curNode][w] + cost[curNode] # Update cost
                path[w] = curNode # Update Path
    return cost


if __name__ == '__main__':
    max = 2147483647
    graph = [
        [max, max, 10, max, 30, 100],
        [max, max, 5, max, max, max],
        [max, max, max, 50, max, max],
        [max, max, max, max, max, 10],
        [max, max, max, 20, max, 60],
        [max, max, max, max, max, max],
        ]
    path = [0] * 6
    cost = [0] * 6
    print(dijkstra(graph, 0, path, cost, max))

