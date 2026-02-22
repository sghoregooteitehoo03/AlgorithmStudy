# 플로이드 워셜 수행
INF = 1e9
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1

    if count == n:
        result += 1
print(result)


# INF = 1e9
# n, m = map(int, input().split())

# arr = [[INF] * (n + 1) for _ in range(n + 1)]
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             arr[i][j] = 1

# for i in range(m):
#     a, b = map(int, input().split())
#     arr[a][b] = 1

# for k in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

# result = 0
# for i in range(1, n + 1):
#     count = 0
#     for j in range(1, n + 1):
#         if arr[i][j] != INF or arr[j][i] != INF:
#             count += 1

#     if count == n:
#         result += 1

# print(result)

# INF = int(1e9)

# n, m = map(int, input().split())
# graph = [[INF] * (n + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             graph[i][j] = 0

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         for k in range(1, n + 1):
#             graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

# result = 0
# print(graph)
# for i in range(1, n + 1):
#     count = 0
#     for j in range(1, n + 1):
#         if graph[i][j] != INF or graph[j][i] != INF:
#             count += 1

#     if count == n:
#         result += 1

# print(result)
