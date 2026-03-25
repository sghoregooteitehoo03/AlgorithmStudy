n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]
answer = arr[0]

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])
    answer = max(answer, dp[i])
print(answer)