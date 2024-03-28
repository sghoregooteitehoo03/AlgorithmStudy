from collections import deque

n, m = map(int, input().split())
map_grpah = []
visited = [[False] * m for _ in range(n)]
result = 0

for i in range(n):
    map_grpah.append(list(map(int, input())))

q = deque([(0, 0, 1)])
while q:
    i, j, count = q.popleft()

    if i == (n - 1) and j == (m - 1):
        result = count
        break

    if not visited[i][j]:
        visited[i][j] = True

        if i + 1 < n and map_grpah[i + 1][j] == 1:
            q.append((i + 1, j, count + 1))
        if i - 1 >= 0 and map_grpah[i - 1][j] == 1:
            q.append((i - 1, j, count + 1))
        if j + 1 < m and map_grpah[i][j + 1] == 1:
            q.append((i, j + 1, count + 1))
        if j - 1 >= 0 and map_grpah[i][j - 1] == 1:
            q.append((i, j - 1, count + 1))

print(result)