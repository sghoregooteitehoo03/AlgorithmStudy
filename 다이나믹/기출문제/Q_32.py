# https://www.acmicpc.net/problem/1932
n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n - 2, -1, -1):
    for j in range(len(arr[i])):
        arr[i][j] = max(arr[i][j] + arr[i + 1][j], arr[i][j] + arr[i + 1][j + 1])

print(arr[0][0])