import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    indegree[b] += 1

def toporogy_sort():
    q = deque([])

    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()

        for other_node in graph[node]:
            indegree[other_node] -= 1
            
            if indegree[other_node] == 0:
                q.append(other_node)
        
        print(node)

toporogy_sort()