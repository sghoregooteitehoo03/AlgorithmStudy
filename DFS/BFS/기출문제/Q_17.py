# https://www.acmicpc.net/problem/18405
from collections import deque

def BFS(map_table, virus_pos, k, s, x, y):
    q = deque(virus_pos)

    visited = [[False] * len(map_table) for _ in range(len(map_table[0]))]
    previous_virus_n = 0
    time = 0

    while(q):
        virus_n, pos_i, pos_j = q.popleft()

        if previous_virus_n == k and previous_virus_n != virus_n:
            time += 1

        if time == s:
            break
        
        previous_virus_n = virus_n
        if not visited[pos_i][pos_j]:
            visited[pos_i][pos_j] = True

            if pos_i - 1 >= 0 and map_table[pos_i - 1][pos_j] == 0:
                    map_table[pos_i - 1][pos_j] = virus_n
                    q.append((virus_n, pos_i - 1, pos_j))
            if pos_i + 1 < len(map_table) and map_table[pos_i + 1][pos_j] == 0:
                map_table[pos_i + 1][pos_j] = virus_n
                q.append((virus_n, pos_i + 1, pos_j))
            if pos_j - 1 >= 0 and map_table[pos_i][pos_j - 1] == 0:
                map_table[pos_i][pos_j - 1] = virus_n
                q.append((virus_n, pos_i, pos_j - 1))
            if pos_j + 1 < len(map_table[0]) and map_table[pos_i][pos_j + 1] == 0:
                map_table[pos_i][pos_j + 1] = virus_n
                q.append((virus_n, pos_i, pos_j + 1))

    return map_table[x - 1][y - 1]

n, k = map(int, input().split())
map_table = []
virus_pos = []

for i in range(n):
    map_table.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

for i in range(len(map_table)):
    for j in range(len(map_table[0])):
        if map_table[i][j] != 0:
            virus_pos.append((map_table[i][j], i, j))

virus_pos.sort()

print(BFS(map_table, virus_pos, k, s, x, y))