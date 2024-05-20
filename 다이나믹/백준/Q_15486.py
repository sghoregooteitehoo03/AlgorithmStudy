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
    if i + t[i] <= n:
        dp[i + t[i]] = max(dp[i + t[i]], dp[i] + p[i])
        
        if max_value < dp[i + t[i]]:
            max_value = dp[i + t[i]]

print(dp)
print(max(dp))