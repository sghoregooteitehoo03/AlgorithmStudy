N = int(input())
arr = []
dp = []

for i in range(N):
    r, g, b = map(int, input().split())
    arr.append((r, g, b))

dp.append((arr[0][0], arr[0][1], arr[0][2]))
for i in range(1, N):
    dp.append(
        (
            min(arr[i][0] + dp[i - 1][1], arr[i][0] + dp[i - 1][2]),
            min(arr[i][1] + dp[i - 1][0], arr[i][1] + dp[i - 1][2]),
            min(arr[i][2] + dp[i - 1][0], arr[i][2] + dp[i - 1][1]),
        )
    )

print(min(dp[N - 1]))