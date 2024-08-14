import sys
input = sys.stdin.readline

n, m = map(int, input().split())
m_arr = [0] + list(map(int, input().split()))
c_arr = [0] + list(map(int, input().split()))
length = sum(c_arr) + 1
dp = [[0 for _ in range(length)] for _ in range(n + 1)]
result = 1e9

for i in range(1, n + 1):
    cost, memory = c_arr[i], m_arr[i]
    for j in range(length):
        dp[i][j] = dp[i - 1][j]
    for j in range(cost, length):
        dp[i][j] = max(dp[i-1][j-cost] + memory, dp[i][j])
        if dp[i][j] >= m:
            result = min(result, j)

print(result)