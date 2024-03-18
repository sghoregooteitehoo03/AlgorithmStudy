from collections import deque

m, n = map(int, input().split())
map_graph = []

for i in range(n):
    map_graph.append(list(map(int, input().split())))

