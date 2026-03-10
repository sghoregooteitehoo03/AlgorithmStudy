# 다익스트라 알고리즘 수행
# 최대거리인 수를 가지는 노드가 몇개인지 반환
from collections import deque
INF = 1e9

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]

    for a, b in edge:
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    distances = [INF] * (n + 1)
    distances[0] = 0
    distances[1] = 0
    queue = deque([(1, 0)])

    while queue:
        current_node, dist = deque.popleft(queue)

        if distances[current_node] < dist:
            continue

        for node in graph[current_node]:
            cost = node[1] + dist

            if cost < distances[node[0]]:
                queue.append((node[0], cost))
                distances[node[0]] = cost

    max_distance = max(distances)
    answer = 0
    for distance in distances:
        if distance == max_distance:
            answer += 1

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))