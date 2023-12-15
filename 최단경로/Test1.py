import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance1 = [INF] * (n + 1)
distance2 = [INF] * (n + 1)

for _ in range(m):
    currentNode, nextNode = map(int, input().split())
    graph[currentNode].append((nextNode, 1))
    graph[nextNode].append((currentNode, 1))

x, k = map(int, input().split())

def dijkstra(start, distance):
    q = []
    visited = [False] * (n + 1)

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if visited[now]:
            continue

        visited[now] = True
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1, distance1)
dijkstra(k, distance2)

if distance1[k] == INF or distance2[x] == INF:
    print(-1)
else:
    print(distance1[k] + distance2[x])


# 답지
# INF = int(1e9)

# n, m = map(int, input().split())
# graph = [[INF] * (n + 1) for _ in range(n + 1)]

# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if a == b:
#             graph[a][b] = 0

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1

# x, k = map(int, input().split())

# for k in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# distance = graph[1][k] + graph[k][x]
# if distance >= INF:
#     print(-1)
# else:
#     print(distance)