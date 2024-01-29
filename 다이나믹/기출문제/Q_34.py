# https://www.acmicpc.net/problem/18353
N = int(input())
sordiers = list(map(int, input().split()))
dp = {}

for sordier in sordiers:
    if dp.keys in sordier:
        dp[sordiers] = 1
    else:
        dp[sordiers] += 1

print(dp)
# for i in range(len(sordiers) - 1):
#     if sordiers[i] < sordiers[i + 1]
