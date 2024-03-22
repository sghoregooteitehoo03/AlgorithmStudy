from collections import deque

n, m = map(int, input().split())
map_graph = []
visited = [[False] * m for _ in range(n)]

for i in range(n):
    map_graph.append(list(map(int, input().split())))

start_pos = (-1, -1)
for i in range(n):
    for j in range(m):
        if map_graph[i][j] == 2:
            start_pos = (i, j, 0)
            break

q = deque([start_pos])
while q:
    i, j, count = q.popleft()

    if not visited[i][j]:
        visited[i][j] = True
        map_graph[i][j] = count

        if i + 1 < n and map_graph[i + 1][j] == 1: 
            q.append((i + 1, j, count + 1))
        if i - 1 >= 0 and map_graph[i - 1][j] == 1:
            q.append((i - 1, j, count + 1))
        if j + 1 < m and map_graph[i][j + 1] == 1:
            q.append((i, j + 1, count + 1))
        if j - 1 >= 0 and map_graph[i][j - 1] == 1:
            q.append((i, j - 1, count + 1))

for i in range(n):
    for j in range(m):
        if not visited[i][j] and map_graph[i][j] != 0:
            print(-1, end=' ')
        else:
            print(map_graph[i][j], end=' ')
            
    print()