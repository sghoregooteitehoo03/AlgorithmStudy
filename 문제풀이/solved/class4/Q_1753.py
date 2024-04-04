import sys
import heapq
input = sys.stdin.readline
INF = 1e9

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)
distance[k] = 0

for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now_node = heapq.heappop(q)
        if distance[now_node] < dist:
            continue

        for node in graph[now_node]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

dijkstra(k)
for i in range(1, len(distance)):
    if distance[i] != INF:
        print(distance[i])
    else:
        print("INF")