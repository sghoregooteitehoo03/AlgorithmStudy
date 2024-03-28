from collections import deque

n = int(input())
map_graph = []
visited = [[False] * n for _ in range(n)]
result = 0
count_arr = []

for i in range(n):
    map_graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if map_graph[i][j] == 1 and not visited[i][j]:
            result += 1
            count = 0
            q = deque([(i, j)])

            while q:
                pos_i, pos_j = q.popleft()

                if not visited[pos_i][pos_j]:
                    visited[pos_i][pos_j] = True
                    count += 1

                    if pos_i + 1 < n and map_graph[pos_i + 1][pos_j] == 1:
                        q.append((pos_i + 1, pos_j))
                    if pos_i - 1 >= 0 and map_graph[pos_i - 1][pos_j] == 1:
                        q.append((pos_i - 1, pos_j))
                    if pos_j + 1 < n and map_graph[pos_i][pos_j + 1] == 1:
                        q.append((pos_i, pos_j + 1))
                    if pos_j - 1 >= 0 and map_graph[pos_i][pos_j - 1] == 1:
                        q.append((pos_i, pos_j - 1))

            count_arr.append(count)

count_arr.sort()

print(result)
for data in count_arr:
    print(data)