import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 1))

    while(q):
        now, count = heapq.heappop(q)
        
        if (distance[now] != 0 and count >= distance[now]):
            continue
        else:
            distance[now] = count

        for node in graph[now]:
            heapq.heappush(q, (node, count + 1))

dijkstra(1)

distance_result = max(distance)
hide_num = 0
same_distance = 0

for i in range(1, len(distance)):
    if distance[i] > distance_result:
        break

    if distance[i] == distance_result:
        if hide_num == 0:
            hide_num = i
        
        same_distance += 1

print(hide_num, distance_result - 1, same_distance)

# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2