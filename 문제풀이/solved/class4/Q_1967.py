import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a] = (b, c)

