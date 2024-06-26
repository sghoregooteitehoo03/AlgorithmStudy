import sys
from collections import deque
input = sys.stdin.readline

n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
table = [0] * (n + 1)

for i in range(n + 1):
    table[i] = (i, 1)

print(table)
for i in range(1, n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def set_graph(route):
    q = deque([route])
    visited = [False] * (n + 1)

    while q:
        node = q.popleft()
        visited[node] = True
        
        for number in graph[node]:
            if visited[graph[node][i][0]]:
                continue
            
            graph[node][i] = (graph[node][i][0], 0)
            q.append(graph[node][i][0])

def query(start):
    count = 1
    q = deque([start])

    while q:
        node = q.popleft()
        for i in range(len(graph[node])):
            if graph[node][i][1] == 1:
                continue

            count += 1
            q.append(graph[node][i][0])

    print(count)

set_graph(r)
for i in range(q):
    q1 = int(input())
    query(q1)