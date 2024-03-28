import heapq
import sys
input = sys.stdin.readline
INF = 1e9

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cost, node = heapq.heappop(q)

        if distance[node] < cost:
            continue

        for i in graph[node]:
            cal_cost = i[1] + cost

            if cal_cost < distance[i[0]]:
                distance[i[0]] = cal_cost
                heapq.heappush(q, (cal_cost, i[0]))

start, end = map(int, input().split())
dijkstra(start)

print(distance[end])