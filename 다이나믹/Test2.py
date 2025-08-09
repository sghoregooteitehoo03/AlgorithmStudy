import sys
import copy

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = copy.deepcopy(arr)

for i in range(len(arr) - 2):
    for j in range((i + 2), len(arr)):
        if dp[j] < dp[i] + arr[j]:
            dp[j] = dp[i] + arr[j]
            
print(max(dp))

# 1, 3, 1, 2, 5
# n = int(input())
# array = list(map(int, input().split()))

# d = [0] * 100
# d[0] = array[0]
# d[1] = array[1]

# for i in range(2, n):
#     d[i] = max(d[i - 1], d[i - 2] + array[i])

# print(d[n - 1])