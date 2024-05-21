import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []
dp = [0] * (n + 1)

for i in range(n):
    t_data, p_data = map(int, input().split())
    
    t.append(t_data)
    p.append(p_data)

max_value = 0
for i in range(n):
    max_value = max(dp[i], max_value)
    
    if i + t[i] <= n:
        dp[i + t[i]] = max(dp[i + t[i]], max_value + p[i])

print(max(dp))