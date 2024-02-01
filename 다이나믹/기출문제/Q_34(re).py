# https://www.acmicpc.net/problem/18353
N = int(input())
sordiers = list(map(int, input().split()))
sordiers.reverse()

dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if sordiers[j] < sordiers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)
print(N - max(dp))