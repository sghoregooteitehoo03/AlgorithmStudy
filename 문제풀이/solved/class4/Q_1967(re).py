from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def bfs(start):
    visited = [False] * len(graph)
    q = deque([(start, 0)])
    max_value = (-1, 0)

    while q:
        node, count = q.popleft()
        visited[node] = True

        if max_value[1] < count:
            max_value = (node, count)

        for i in graph[node]:
            if not visited[i[0]]:
                q.append((i[0], i[1] + count))

    return max_value

print(bfs(bfs(1)[0])[1])