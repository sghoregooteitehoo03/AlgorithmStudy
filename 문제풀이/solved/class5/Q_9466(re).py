import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
t = int(input())

def dfs(start):
    global result

    visited[start] = True
    team.append(start)
    next_node = arr[start]

    if visited[next_node]:
        if next_node in team:
            result -= len(team[team.index(next_node):])
    else:
        dfs(next_node)

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    result = n
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            team = []
            dfs(i)
    
    print(result)