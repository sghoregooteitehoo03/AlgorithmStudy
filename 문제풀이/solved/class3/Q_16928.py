from collections import deque

n, m = map(int, input().split())
map_graph = [0] * 101
visited = [False] * 101

for i in range(n):
    pos, move_pos = map(int, input().split())
    map_graph[pos] = move_pos

for i in range(m):
    pos, move_pos = map(int, input().split())
    map_graph[pos] = move_pos

result = 0

q = deque([(1, 0)])
while(q):
    i, count = q.popleft()

    if i == 100:
        result = count
        break
    elif map_graph[i] != 0:
        i = map_graph[i]

    if not visited[i]:
        visited[i] = True
        if i + 1 < 101:
            q.append((i + 1, count + 1))
        if i + 2 < 101:
            q.append((i + 2, count + 1))
        if i + 3 < 101:
            q.append((i + 3, count + 1))
        if i + 4 < 101:
            q.append((i + 4, count + 1))
        if i + 5 < 101:
            q.append((i + 5, count + 1))
        if i + 6 < 101:
            q.append((i + 6, count + 1))

print(result)