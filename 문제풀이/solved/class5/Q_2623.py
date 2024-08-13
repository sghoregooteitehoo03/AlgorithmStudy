import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr) - 1):
        a = arr[i]
        b = arr[i + 1]

        graph[a].append(b)
        indegree[b] += 1


def toporogy_sort():
    q = deque([])
    result = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()

        for other_node in graph[node]:
            indegree[other_node] -= 1
            if indegree[other_node] == 0:
                q.append(other_node)

        result.append(node)

    return result


result_arr = toporogy_sort()
if len(result_arr) != n:
    print(0)
else:
    for result in result_arr:
        print(result)
