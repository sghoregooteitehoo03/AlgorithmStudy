import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

n = int(input())
map_graph = []
result = 0

for i in range(n):
    map_graph.append(list(map(int, input().split())))

q = deque([((0, 0), (0, 1), 1), ((0, 0), (1, 1), 2), ((0, 0), (1, 0), 3)])
while q:
    pos1, pos2, pipe_type = q.popleft()

    if pos2[0] == n - 1 and pos2[1] == n - 1:
        result += 1
        continue

    if pipe_type == 1:
        if pos2[1] + 1 < n:
            q.append(((pos1[0], pos1[1] + 1), (pos2[0], pos2[1] + 1), 1))

            if pos2[0] + 1 < n:
                q.append(((pos1[0], pos1[1] + 1), (pos2[0] + 1, pos2[1] + 1), 2))
    elif pipe_type == 2:
        if pos2[1] + 1 < n:
            q.append(((pos1[0] + 1, pos1[1] + 1), (pos2[0], pos2[1] + 1), 1))

            if pos2[0] + 1 < n:
                q.append(((pos1[0] + 1, pos1[1] + 1), (pos2[0] + 1, pos2[1] + 1), 2))
        if pos2[0] + 1 < n:
            q.append(((pos1[0] + 1, pos1[1] + 1), (pos2[0] + 1, pos2[1]), 3))
    elif pipe_type == 3:
        if pos2[0] + 1 < n:
            q.append(((pos1[0] + 1, pos1[1]), (pos2[0] + 1, pos2[1]), 3))

            if pos2[1] + 1 < n:
                q.append(((pos1[0] + 1, pos1[1]), (pos2[0] + 1, pos2[1] + 1), 2))

print(result)