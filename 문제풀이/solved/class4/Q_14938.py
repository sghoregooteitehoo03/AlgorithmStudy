import sys
input = sys.stdin.readline
INF = 1e9

n, m, r = map(int, input().split())
item_table = list(map(int, input().split()))
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

for i in range(r):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost
    graph[b][a] = cost

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

result = []
for i in range(1, n + 1):
    item_count = 0
    
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            item_count += item_table[j - 1]

    result.append(item_count)

print(max(result))