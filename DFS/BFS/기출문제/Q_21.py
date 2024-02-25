# https://www.acmicpc.net/problem/16234
from collections import deque

def close_country(map_graph):
    for i in range(len(map_graph)):
        for j in range(len(map_graph)):
            map_graph[i][j] = (map_graph[i][j], (i * len(map_graph)) + j)

n, l, r = map(int, input().split())
map_graph = []

for i in range(n):
    map_graph.append(list(map(int, input().split())))

is_moved = True
result = -1

while is_moved:
    close_country(map_graph)
    result += 1

    is_moved = False
    visited = [[False] * n for _ in range(n)]
    dict = {}

    q = deque([(0, 0)])

    while q:
        pos_i, pos_j = q.popleft()

        if not visited[pos_i][pos_j]:
            visited[pos_i][pos_j] = True

            if pos_i - 1 >= 0:
                q.append((pos_i - 1, pos_j))

                diff = abs(map_graph[pos_i][pos_j][0] - map_graph[pos_i - 1][pos_j][0])
                if diff >= l and diff <= r:
                    if map_graph[pos_i][pos_j][1] < map_graph[pos_i - 1][pos_j][1]:
                        map_graph[pos_i - 1][pos_j] = (map_graph[pos_i - 1][pos_j][0], map_graph[pos_i][pos_j][1])
                    else:
                        map_graph[pos_i][pos_j] = (map_graph[pos_i][pos_j][0], map_graph[pos_i - 1][pos_j][1])

            if pos_i + 1 < n:
                q.append((pos_i + 1, pos_j))

                diff = abs(map_graph[pos_i][pos_j][0] - map_graph[pos_i + 1][pos_j][0])
                if diff >= l and diff <= r:
                    if map_graph[pos_i][pos_j][1] < map_graph[pos_i + 1][pos_j][1]:
                        map_graph[pos_i + 1][pos_j] = (map_graph[pos_i + 1][pos_j][0], map_graph[pos_i][pos_j][1])
                    else:
                        map_graph[pos_i][pos_j] = (map_graph[pos_i][pos_j][0], map_graph[pos_i + 1][pos_j][1])

            if pos_j - 1 >= 0:
                q.append((pos_i, pos_j - 1))

                diff = abs(map_graph[pos_i][pos_j][0] - map_graph[pos_i][pos_j - 1][0])
                if diff >= l and diff <= r:
                    if map_graph[pos_i][pos_j][1] < map_graph[pos_i][pos_j - 1][1]:
                        map_graph[pos_i][pos_j - 1] = (map_graph[pos_i][pos_j - 1][0], map_graph[pos_i][pos_j][1])
                    else:
                        map_graph[pos_i][pos_j] = (map_graph[pos_i][pos_j][0], map_graph[pos_i][pos_j - 1][1])

            if pos_j + 1 < n:
                q.append((pos_i, pos_j + 1))

                diff = abs(map_graph[pos_i][pos_j][0] - map_graph[pos_i][pos_j + 1][0])
                if diff >= l and diff <= r:
                    if map_graph[pos_i][pos_j][1] < map_graph[pos_i][pos_j + 1][1]:
                        map_graph[pos_i][pos_j + 1] = (map_graph[pos_i][pos_j + 1][0], map_graph[pos_i][pos_j][1])
                    else:
                        map_graph[pos_i][pos_j] = (map_graph[pos_i][pos_j][0], map_graph[pos_i][pos_j + 1][1])
    
    for i in range(n):
        for j in range(n):
            if dict.get(map_graph[i][j][1]) == None:
                dict[map_graph[i][j][1]] = [(map_graph[i][j][0], i, j)]
            else:
                dict[map_graph[i][j][1]].append((map_graph[i][j][0], i, j))

    for key in dict.keys():
        if len(dict[key]) == 1:
            map_graph[dict[key][0][1]][dict[key][0][2]] = map_graph[dict[key][0][1]][dict[key][0][2]][0]
            continue

        is_moved = True
        summary = 0
        for data in dict[key]:
            summary += data[0]

        summary = summary // len(dict[key])
        for data in dict[key]:
            map_graph[data[1]][data[2]] = summary

print(result)