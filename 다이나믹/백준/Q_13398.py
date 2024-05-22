import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = arr[0]
max_pos = (0, -1)

for i in range(1, n):
    dp[i] = max(arr[i], arr[i] + dp[i - 1])
    
    if arr[i] < 0 and i + 1 < n:
        if max_pos[0] < dp[i - 1] + dp[i + 1]:
            max_pos = (dp[i - 1] + dp[i + 1], i)

if max_pos[1] != -1:
    arr.pop(max_pos[1])
    dp = [0] * n
    dp[0] = arr[0]

    for i in range(1, n - 1):
        dp[i] = max(arr[i] + dp[i - 1], arr[i])

result = max(dp)
if result == 0:
    print(max(arr))
else:
    print(result)

# 6
# 3 -5 5 -4 5 4