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
result = []

for i in range(m):
    cal, a, b = map(int, input().split())
    
    if cal == 0:
        union_graph(graph, a, b)
    elif cal == 1:
        if find_parent(graph, a) == find_parent(graph, b):
            result.append("YES")
        else:
            result.append("NO")

for s in result:
    print(s)