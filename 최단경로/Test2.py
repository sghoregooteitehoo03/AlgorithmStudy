import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    currentNode, nextNode, value = map(int, input().split())
    graph[currentNode].append((nextNode, value))

print(graph)
def dijkstra(start):
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

city = 0
time = 0

for dist in distance:
    if dist != INF and dist != 0:
        city += 1
        
        if time < dist:
            time = dist

print(city, time)