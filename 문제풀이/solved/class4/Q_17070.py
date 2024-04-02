import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
map_graph = []
result = 0

for i in range(n):
    map_graph.append(list(map(int, input().split())))

if map_graph[n - 1][n - 1] != 1:
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    dp[0][1][0] = 1

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            
            if dp[i][j][0] != 0:
                if j + 1 < n and map_graph[i][j + 1] == 0:
                    dp[i][j + 1][0] += dp[i][j][0]

                    if i + 1 < n and map_graph[i + 1][j] == 0 and map_graph[i + 1][j + 1] == 0:
                        dp[i + 1][j + 1][2] += dp[i][j][0]

            if dp[i][j][1] != 0:
                if i + 1 < n and map_graph[i + 1][j] == 0:
                    dp[i + 1][j][1] += dp[i][j][1]

                    if j + 1 < n and map_graph[i + 1][j + 1] == 0 and map_graph[i][j + 1] == 0:
                        dp[i + 1][j + 1][2] += dp[i][j][1]

            if dp[i][j][2] != 0:
                if j + 1 < n and map_graph[i][j + 1] == 0:
                    dp[i][j + 1][0] += dp[i][j][2]

                    if i + 1 < n and map_graph[i + 1][j] == 0 and map_graph[i + 1][j + 1] == 0:
                        dp[i + 1][j + 1][2] += dp[i][j][2]

                if i + 1 < n and map_graph[i + 1][j] == 0:
                    dp[i + 1][j][1] += dp[i][j][2]

    for i in dp[n - 1][n - 1]:
        result += i
print(result)