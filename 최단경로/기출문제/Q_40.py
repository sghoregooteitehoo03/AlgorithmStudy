# 그래프 양방향 입력
# 다익스트라 수행
# 짜여진 distance에서 작은 수와 같은거리를 갖는 수 ㅊ루력
import heapq

INF = 1e9

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distances = [INF] * (n + 1)
distances[1] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijsktra():
    q = []
    heapq.heappush(q, (1, distances[1]))

    while q:
        now, dist = heapq.heappop(q)
        if distances[now] < dist:
            continue

        for g in graph[now]:
            cost = dist + g[1]
            if cost < distances[g[0]]:
                distances[g[0]] = cost
                heapq.heappush(q, (g[0], cost))


dijsktra()
result = {}

for i in range(2, len(distances)):
    dist = distances[i]

    if result.get(dist) != None:
        result[dist].append(i)
    else:
        result[dist] = [i]

max_distance = max(result.keys())
hide_value = result[max_distance][0]
count = len(result[max_distance])

print(hide_value, end=' ')
print(max_distance, end=' ')
print(count, end=' ')

# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2
