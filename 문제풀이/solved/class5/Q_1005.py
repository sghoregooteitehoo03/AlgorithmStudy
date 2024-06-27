import sys
from collections import deque
input = sys.stdin.readline


def topology_sort(rule, graph, indegree, w):
    result = 0
    q = deque([])

    for i in range(1, len(indegree)):
        if indegree[i][0] == 0:
            if i == w:
                return rule[i - 1]

            q.append(i)
            result = rule[i - 1]

    while q:
        node = q.popleft()

        for other_node in graph[node]:
            indegree[other_node] = (
                indegree[other_node][0] -1, 
                indegree[other_node][1] - rule[other_node - 1]
            )
            if indegree[other_node][1] >= 0:
                result += rule[other_node - 1]
            else:
                result += rule[other_node - 1] + indegree[other_node][1]

            if indegree[other_node][0] == 0:
                if other_node == w:
                    return result

                q.append(other_node)

    return result


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    rule = list(map(int, input().split()))
    indegree = [(0, 0)] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for i in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] = (indegree[y][0] + 1, max(indegree[y][0], rule[x - 1]))
    w = int(input())

    print(indegree)
    result = topology_sort(rule, graph, indegree, w)
    print(result)
