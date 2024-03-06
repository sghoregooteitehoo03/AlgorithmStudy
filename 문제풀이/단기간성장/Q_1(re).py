import sys
input = sys.stdin.readline
dp = [[0] * 100001 for _ in range(101)]

n, k = map(int, input().split())
arr = []
for i in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))

def go(i, w):
    if dp[i][w] > 0:
         return dp[i][w]
    if i == n:
        return 0
    
    n1 = 0
    if (w + arr[i][0] <= k):
        n1 = arr[i][1] + go(i + 1, w + arr[i][0])

    n2 = go(i + 1, w)
    
    dp[i][w] = max(n1, n2)
    return dp[i][w]

print(go(0, 0))