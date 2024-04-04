import sys
import heapq
input = sys.stdin.readline
INF = 1e9

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end1, end2):
    q = []
    distance = [INF] * (n + 1)
    if start == end1 or start == end2:
        return 0, 0

    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)

        for node in graph[now]:
            cost = dist + node[1]
            
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

    return distance[end1], distance[end2]

a, d = dijkstra(1, v1, v2)
b, e = dijkstra(v1, v2, n)
c, f = dijkstra(v2, n, v1)
result = min(a + b + c, d + e + f)

if result >= INF:
    print(-1)
else:
    print(result)