T = int(input())
for _ in range(T):
    dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    N = int(input())

    if N < len(dp):
        print(dp[N - 1])
    else:
        for i in range(10, N):
            dp.append(dp[i - 5] + dp[i - 1])
        print(dp[N - 1])


# 2 + 1
# 3 + 1
# 4 + 1
# 5 + 2
# 7 + 2