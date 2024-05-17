import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
dp = [[] for _ in range(n)]

for i in range(n):
    arr.append(int(input()))

for i in range(n):
    summary = 0

    while summary <= k:
        dp[i].append(summary)
        summary += arr[i]

for i in range(1, n):
    for j in range(len(dp[i])):
        