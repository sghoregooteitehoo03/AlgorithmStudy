# https://www.acmicpc.net/problem/1932
from collections import deque

n = int(input())
triangle = []
q = deque([])

for i in range(n):
    l = list(map(int, input().split()))
    
    triangle.append(l)

if n != 1:
    for i in range(len(triangle[n - 2])):
        q.append((n - 2, i))

    while(q):
        i, j = q.popleft()
        if triangle[i + 1][j] > triangle[i + 1][j + 1]:
            triangle[i][j] += triangle[i + 1][j]
        else:
            triangle[i][j] += triangle[i + 1][j + 1]

        if i - 1 >= 0 and j != len(triangle[i]) - 1:
            q.append((i - 1, j))

print(triangle[0][0])

# print(max(map_table[n - 1]))