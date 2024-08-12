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
    

print(graph)
