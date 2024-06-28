import sys
from collections import deque
input = sys.stdin.readline

def topology_sort(rule, graph, indegree, w):
    dp = [0] * len(indegree)
    q = deque([])

    for i in range(1, len(indegree)):
        dp[i] = rule[i - 1]
        
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()

        for other_node in graph[node]:
            indegree[other_node] -= 1
            dp[other_node] = max(dp[other_node],dp[node] + rule[other_node - 1])

            if indegree[other_node] == 0:
                q.append(other_node)

    return dp[w]


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    rule = list(map(int, input().split()))
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for i in range(k):
        x, y = map(int, input().split())
        
        graph[x].append(y)
        indegree[y] += 1

    w = int(input())

    result = topology_sort(rule, graph, indegree, w)
    print(result)