import sys
from collections import deque
input = sys.stdin.readline

n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dp = [1] * (n + 1)

for i in range(1, n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def set_graph(route):
    q1 = deque([route])
    q2 = deque([])
    visited = [False] * (n + 1)

    while q1:
        node = q1.popleft()
        visited[node] = True
        
        for number in graph[node]:
            if visited[number]:
                q2.append((number, node))
                continue
            
            q1.append(number)

    while q2:
        node, previous_node = q2.pop()
        dp[node] = dp[node] + dp[previous_node]

set_graph(r)
for i in range(q):
    q1 = int(input())
    print(dp[q1])