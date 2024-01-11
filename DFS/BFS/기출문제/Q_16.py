# https://www.acmicpc.net/problem/14502
from collections import deque
import copy

def spread(map_table, start_pos):
    q = deque(start_pos)
    
    copy_map = copy.deepcopy(map_table)
    visited = [[False] * len(map_table[0]) for _ in range(len(map_table))]

    while q:
        pos_i, pos_j = q.popleft()

        if not visited[pos_i][pos_j]:
                visited[pos_i][pos_j] = True
                copy_map[pos_i][pos_j] = 2

                if pos_i - 1 >= 0 and copy_map[pos_i - 1][pos_j] == 0:
                    q.append((pos_i - 1, pos_j))
                if pos_i + 1 < len(map_table) and copy_map[pos_i + 1][pos_j] == 0:
                    q.append((pos_i + 1, pos_j))
                if pos_j - 1 >= 0 and copy_map[pos_i][pos_j - 1] == 0:
                    q.append((pos_i, pos_j - 1))
                if pos_j + 1 < len(map_table[0]) and copy_map[pos_i][pos_j + 1] == 0:
                    q.append((pos_i, pos_j + 1))

    print(copy_map)



n, m = map(int, input().split())
map_table = []
virus_pos = []

for i in range(n):
    map_table.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if map_table[i][j] == 2:
            virus_pos.append((i, j))

spread(map_table, virus_pos)