from collections import deque

n = int(input())
map_graph = []
visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]
result1 = 0
result2 = 0

for i in range(n):
    map_graph.append(list(input()))

for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            q = deque([(i, j)])
            result1 += 1

            while(q):
                pos_i, pos_j = q.popleft()
                
                if not visited1[pos_i][pos_j]:
                    visited1[pos_i][pos_j] = True

                    if pos_i + 1 < n and map_graph[pos_i + 1][pos_j] == map_graph[pos_i][pos_j]:
                        q.append((pos_i + 1, pos_j))
                    if pos_i - 1 >= 0 and map_graph[pos_i - 1][pos_j] == map_graph[pos_i][pos_j]:
                        q.append((pos_i - 1, pos_j))
                    if pos_j + 1 < n and map_graph[pos_i][pos_j + 1] == map_graph[pos_i][pos_j]:
                        q.append((pos_i, pos_j + 1))
                    if pos_j - 1 >= 0 and map_graph[pos_i][pos_j - 1] == map_graph[pos_i][pos_j]:
                        q.append((pos_i, pos_j - 1))
        if not visited2[i][j]:
            q = deque([(i, j)])
            result2 += 1

            while(q):
                pos_i, pos_j = q.popleft()
                
                if not visited2[pos_i][pos_j]:
                    visited2[pos_i][pos_j] = True

                    if pos_i + 1 < n:
                        if map_graph[pos_i + 1][pos_j] == map_graph[pos_i][pos_j]:
                            q.append((pos_i + 1, pos_j))
                        elif (map_graph[pos_i][pos_j] == 'R' or map_graph[pos_i][pos_j] == 'G') and map_graph[pos_i + 1][pos_j] != 'B':
                            q.append((pos_i + 1, pos_j))
                    if pos_i - 1 >= 0:
                        if map_graph[pos_i - 1][pos_j] == map_graph[pos_i][pos_j]:
                            q.append((pos_i - 1, pos_j))
                        elif (map_graph[pos_i][pos_j] == 'R' or map_graph[pos_i][pos_j] == 'G') and map_graph[pos_i - 1][pos_j] != 'B':
                            q.append((pos_i - 1, pos_j))
                    if pos_j + 1 < n:
                        if map_graph[pos_i][pos_j + 1] == map_graph[pos_i][pos_j]:
                            q.append((pos_i, pos_j + 1))
                        elif (map_graph[pos_i][pos_j] == 'R' or map_graph[pos_i][pos_j] == 'G') and map_graph[pos_i][pos_j + 1] != 'B':
                            q.append((pos_i, pos_j + 1))
                    if pos_j - 1 >= 0:
                        if map_graph[pos_i][pos_j - 1] == map_graph[pos_i][pos_j]:
                            q.append((pos_i, pos_j - 1))
                        elif (map_graph[pos_i][pos_j] == 'R' or map_graph[pos_i][pos_j] == 'G') and map_graph[pos_i][pos_j - 1] != 'B':
                            q.append((pos_i, pos_j - 1))

print(result1, result2)