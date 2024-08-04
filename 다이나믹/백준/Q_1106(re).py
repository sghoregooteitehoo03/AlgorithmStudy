import sys
input = sys.stdin.readline

arr = []
c, n = map(int, input().split())
dp = [1e9 for _ in range(c + 100)]
dp[0] = 0

for i in range(n):
    cost, people = map(int, input().split())
    arr.append((cost, people))

for cost, people in arr:
    for i in range(people, c + 100):
        dp[i] = min(dp[i], dp[i-people] + cost)

print(min(dp[c:]))