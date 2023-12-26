def find_parent(graph, node):
    if graph[node] != node:
        graph[node] = find_parent(graph, graph[node])
    return graph[node]


def union_graph(graph, nodeA, nodeB):
    a = find_parent(graph, nodeA)
    b = find_parent(graph, nodeB)

    if a < b:
        graph[b] = a
    else:
        graph[a] = b


n, m = map(int, input().split())
graph = [i for i in range(n + 1)]
edges = []
result = 0

for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
maxValue = 0
for edge in edges:
    cost, a, b = edge

    if find_parent(graph, a) != find_parent(graph, b):
        union_graph(graph, a, b)
        result += cost
        maxValue = cost

print(result - maxValue)


# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4