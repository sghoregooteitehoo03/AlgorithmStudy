from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
map_graph = []

for i in range(n):
    map_graph.append(list(map(int, input().split())))

q = deque([])
for i in range(n):
    for j in range(m):
        if map_graph[i][j] == 1:
            q.append((i, j, 0))

result = 0
while q:
    i, j, day = q.popleft()

    if result < day:
        result = day

    if i + 1 < n and map_graph[i + 1][j] == 0:
        map_graph[i + 1][j] = day + 1
        q.append((i + 1, j, day + 1))
    if i - 1 >= 0 and map_graph[i - 1][j] == 0:
        map_graph[i - 1][j] = day + 1
        q.append((i - 1, j, day + 1))
    if j + 1 < m and map_graph[i][j + 1] == 0:
        map_graph[i][j + 1] = day + 1
        q.append((i, j + 1, day + 1))
    if j - 1 >= 0 and map_graph[i][j - 1] == 0:
        map_graph[i][j - 1] = day + 1
        q.append((i, j - 1, day + 1))

for i in range(n):
    for j in range(m):
        if map_graph[i][j] == 0:
            result = -1
            break

print(result)