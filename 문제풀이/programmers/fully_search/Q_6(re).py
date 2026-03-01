# 그래프로 송전탑을 입력받음
# 연결된 그래프에서 입력받은 wires를 끊어내면서 카운트
# 카운트 한 값과 전체 값을 뺀 값을 비교해서 차이가 제일 낮은 값을 리턴
from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n + 1)]

    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)

    min_diff = 1e9
    for v1, v2 in wires:
        count1 = bfs(graph, v1, v2)
        count2 = n - count1

        min_diff = min(min_diff, abs(count1 - count2))

    return min_diff

def bfs(graph, start, ignore_node):
    visited = [False] * len(graph)
    queue = deque([start])
    count = 0
    
    while queue:
        node = deque.popleft(queue)
        if visited[node]:
            continue
        visited[node] = True
        count += 1

        for next_node in graph[node]:
            if next_node != ignore_node:
                queue.append(next_node)

    return count

solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]])
# solution(4, [[1, 2], [2, 3], [3, 4]])
