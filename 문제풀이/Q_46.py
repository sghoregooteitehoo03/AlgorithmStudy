# https://www.acmicpc.net/problem/16236
from collections import deque
import heapq

n = int(input())
map_array = []
shark_pos = ()
shark_level = 2
shark_eat = 0
result = 0

for i in range(n):
    map_array.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if map_array[i][j] == 9:
            map_array[i][j] = 0
            shark_pos = (i, j)

q = deque([(shark_pos[0], shark_pos[1], 0)])
visited = [[False] * n for _ in range(n)]
h = []

while(q):
    pos_i, pos_j, count = q.popleft()

    if not visited[pos_i][pos_j]:
        visited[pos_i][pos_j] = True

        if map_array[pos_i][pos_j] > 0 and map_array[pos_i][pos_j] < shark_level:
            heapq.heappush(h, (count, pos_i, pos_j))
        if pos_i - 1 >= 0 and map_array[pos_i - 1][pos_j] <= shark_level:
            q.append((pos_i - 1, pos_j, count + 1))
        if pos_j - 1 >= 0 and map_array[pos_i][pos_j - 1] <= shark_level:
            q.append((pos_i, pos_j - 1, count + 1))
        if pos_i + 1 < n and map_array[pos_i + 1][pos_j] <= shark_level:
            q.append((pos_i + 1, pos_j, count + 1))
        if pos_j + 1 < n and map_array[pos_i][pos_j + 1] <= shark_level:
            q.append((pos_i, pos_j + 1, count + 1))
            
    elif q.__len__() == 0 and len(h) != 0:
        cost, i, j = heapq.heappop(h)
        shark_eat += 1
        result += cost

        h.clear()
        q = deque([(i, j, 0)])
        visited = [[False] * n for _ in range(n)]
        map_array[i][j] = 0

        if shark_eat == shark_level:
            shark_level += 1
            shark_eat = 0

print(result)