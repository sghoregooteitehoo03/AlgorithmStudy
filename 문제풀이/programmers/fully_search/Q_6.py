from collections import deque
INF = 1e9

def solution(n, wires):
    answer = INF
    graph = [[] for _ in range(n + 1)]

    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        count1 = bfs(graph, a, b)
        count2 = n - count1

        answer = min(answer, abs(count1 - count2))

    print(answer)
    return answer

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