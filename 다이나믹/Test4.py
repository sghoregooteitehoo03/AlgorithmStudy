n, m = map(int, input().split())
money = []
dp = [1e9] * (m + 1)
dp[0] = 0

for i in range(n):
    money.append(int(input()))
    
for i in range(m):
    if dp[i] == 1e9:
        continue
    
    for c in money:
        if i + c <= m:
            dp[i + c] = min(dp[i + c], dp[i] + 1)

if dp[m] == 1e9:
    print(-1)
else:
    print(dp[m])