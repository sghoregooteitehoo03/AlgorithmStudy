import sys
input = sys.stdin.readline

c, n = map(int, input().split())
arr = []
dp = [0] * (c + 1)

for i in range(n):
    cost, count = map(int, input().split())
    
    dp[cost] = count
    arr.append((cost, count))

result = 0
for i in range(1, c + 1):
    for j in range(n):
        if i % arr[j][0] == 0 and i != arr[j][0]:
            cal = arr[j][1] + dp[i - arr[j][0]]
            
            if cal <= c:
                dp[i] = max(cal, dp[i])
    if dp[i] == c:
        result = i
        break

print(result)