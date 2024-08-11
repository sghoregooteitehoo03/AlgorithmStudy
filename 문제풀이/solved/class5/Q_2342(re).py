import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

arr = list(map(int, input().split()))
arr.pop(-1)

def get_strength(n1, n2):
    if n2 == 0:
        if n1 == 0:
            return 0
        else:
            return 2
    elif n2 == n1:
        return 1
    elif abs(n2 - n1) == 1 or abs(n2 - n1) == 3:
        return 3
    else:
        return 4

dp = [[[400001 for _ in range(5)]for _ in range(5)] for _ in range(len(arr) + 1)]
dp[-1][0][0] = 0

for i in range(len(arr)):
    for r in range(5):
        for k in range(5):
            strength = get_strength(arr[i], k)
            dp[i][arr[i]][r] = min(dp[i][arr[i]][r], dp[i - 1][k][r] + strength)

    for l in range(5):
        for k in range(5):
            strength = get_strength(arr[i], k)
            dp[i][l][arr[i]] = min(dp[i][l][arr[i]], dp[i - 1][l][k] + strength)

result = 400001
for l in range(5):
    for r in range(5):
        result = min(result, dp[len(arr) - 1][l][r])

print(result)