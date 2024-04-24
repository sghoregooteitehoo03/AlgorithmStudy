import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

increase_dp = [1] * n
decrease_dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and increase_dp[i] <= increase_dp[j]:
            increase_dp[i] = increase_dp[j] + 1

        elif arr[j] == arr[i]:
            increase_dp[i] = increase_dp[j]

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[j] < arr[i] and decrease_dp[i] <= decrease_dp[j]:
            decrease_dp[i] = decrease_dp[j] + 1

        elif arr[j] == arr[i]:
            decrease_dp[i] = decrease_dp[j]

result = []
for i in range(n):
    result.append(increase_dp[i] + decrease_dp[i])

print(max(result) - 1)