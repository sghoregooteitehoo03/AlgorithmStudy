n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + 2 * dp[i - 2] % 796796
    
print(dp[n])

# n = int(input())
# d = [0] * 1001

# d[1] = 1
# d[2] = 3
# for i in range(3, n + 1):
#     d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

# print(d[n])