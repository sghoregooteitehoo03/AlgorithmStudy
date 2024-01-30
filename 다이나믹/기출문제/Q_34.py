# https://www.acmicpc.net/problem/18353
import copy

N = int(input())
sordiers = list(map(int, input().split()))
remove_pos = []
result = 0
dp = {}

for sordier in sordiers:
    if sordier in dp.keys():
        dp[sordier] += 1
    else:
        dp[sordier] = 1

for i in range(N - 1, 0, -1):
    for j in range(i + 1, -1, -1):
        if j in remove_pos:
            continue

        if sordiers[j] > sordiers[i]:
            break
        elif sordiers[j] < sordiers[i]:
            if i + 1 < N
            remove_pos.append(j)


# 12
# 12 2 5 3 2 10 8 7 15 5 4 3
# 7
# 15 11 4 8 5 2 4