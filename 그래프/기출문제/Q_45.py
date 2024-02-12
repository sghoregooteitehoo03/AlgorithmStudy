# https://www.acmicpc.net/problem/3665
case = int(input())

for i in range(case):
    n = int(input())
    t = list(map(int, input().split()))
    m = int(input())
    diff = []
    
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for i in range(m):
        a, b = map(int, input().split())
        diff.append((a, b))