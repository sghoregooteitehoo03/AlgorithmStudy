import heapq

INF = 1e9

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

t = int(input())
for _ in range(t):
    n = int(input())
    graph = []
    distance = [[INF] * n for _ in range(n)]

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    distance[0][0] = graph[0][0]
    q = [(graph[0][0], 0, 0)]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n - 1][n - 1])