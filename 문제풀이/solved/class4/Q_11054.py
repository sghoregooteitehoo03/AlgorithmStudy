import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (1001)
result = []

for data in arr:
    dp[data] += 1

max_value = max(arr)
min_value = min(arr)

for i in range(max_value + 1):
    if dp[i] != 0:
        if len(result) == 0:
            result.append(i)
        elif result[-1] < i:
            result.append(i)

        dp[i] -= 1

for i in range(max_value, 0, -1):
    if dp[i] != 0:
        if result[-1] > i:
            result.append(i)

        dp[i] -= 1

print(len(result))