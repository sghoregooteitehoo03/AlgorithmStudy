import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * 3 for _ in range(n - 1)]
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    if i == n - 1:
        print(dp)
    else:
        if i == 1:
            dp[i - 1][0] = (1, 2, arr[i - 1][1] + arr[i][0], arr[i - 1][2] + arr[i][0])
            dp[i - 1][1] = (0, 2, arr[i - 1][0] + arr[i][1], arr[i - 1][2] + arr[i][1])
            dp[i - 1][2] = (0, 1, arr[i - 1][0] + arr[i][2], arr[i - 1][1] + arr[i][2])
        else:
            dp[i - 1][0] = (dp[i - 2][1][0], dp[i - 2][2][1], dp[i - 2][1][2] + arr[i][0], dp[i - 2][2][3] + arr[i][0])
            dp[i - 1][1] = (dp[i - 2][0][0], dp[i - 2][2][1], dp[i - 2][0][2] + arr[i][1], dp[i - 2][2][3] + arr[i][1])
            dp[i - 1][2] = (dp[i - 2][0][0], dp[i - 2][1][1], dp[i - 2][0][2] + arr[i][2], dp[i - 2][1][3] + arr[i][2])