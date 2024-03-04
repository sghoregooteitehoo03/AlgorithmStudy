# https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
map_graph = []
house_pos = []
chiken_pos = []

for i in range(n):
    map_graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if map_graph[i][j] == 1:
            house_pos.append((i + 1, j + 1))
        elif map_graph[i][j] == 2:
            chiken_pos.append((i + 1, j + 1))

combine = (combinations(chiken_pos, m))
result = []
for possible in combine:
    value = 0
    
    for house in house_pos:
        min_value = 1e9
        
        for chicken in possible:
            cal = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

            if cal < min_value:
                min_value = cal

        value += min_value
    
    result.append(value)

print(min(result))