from collections import deque

n, k = map(int, input().split())
q = deque([(n, 0)])
visited = [1e9] * 100001
result = 1e9

while q:
    value, time = q.popleft()

    if value == k:
        if result > time:
            result = time
        continue
    
    if value + 1 <= 100000 and visited[value + 1] > time + 1:
        visited[value + 1] = time + 1
        q.append((value + 1, time + 1))
    if value - 1 >= 0 and visited[value - 1] > time + 1:
        visited[value - 1] = time + 1
        q.append((value - 1, time + 1))
    if value * 2 <= 100000 and visited[value * 2] > time:
        visited[value * 2] = time
        q.append((value * 2, time))

print(result)