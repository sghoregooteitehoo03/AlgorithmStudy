import sys
import heapq
input = sys.stdin.readline
INF = 1e9

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    q = []

    heapq.heappush(q, (INF, start, False, False))
    while q:
        dist, now, v1_visit, v2_visit = heapq.heappop(q)
        
        # if distance[now] < dist:
        #     continue

        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

dijkstra(1)
print(distance[n])