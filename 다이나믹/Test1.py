import sys
input = sys.stdin.readline

x = int(input())
dp = [1e9] * (x + 1)
dp[1] = 1

for i in range(1, x + 1):
    if i + 1 <= (x) and dp[i + 1] > dp[i] + 1:
        dp[i + 1] = dp[i] + 1
    
    if i * 2 <= (x) and dp[i * 2] > dp[i] + 1:
        dp[i * 2] = dp[i] + 1
    
    if i * 3 <= (x) and dp[i * 3] > dp[i] + 1:
        dp[i * 3] = dp[i] + 1
    
    if i * 5 <= (x) and dp[i * 5] > dp[i] + 1:
        dp[i * 5] = dp[i] + 1

print(dp[x] - 1)

# n = int(input())
# dp = [0] * (n + 1)

# for i in range(2, n + 1):
#     dp[i] = dp[i - 1] + 1
    
#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i // 2] + 1)
#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i // 3] + 1)
#     if i % 5 == 0:
#         dp[i] = min(dp[i], dp[i // 5] + 1)

# print(dp[n])


# 답지
# x = int(input())
# d = [0] * 30001

# for i in range(2, x + 1):
#     d[i] = d[i - 1] + 1
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i // 5] + 1)
#     print(i, d[i])

# print(d[x])