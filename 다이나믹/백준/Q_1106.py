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
limit = max(arr)[0]

print(limit)

i = limit
while True:
    cal = dp[i - arr[j][0]] + arr[j][1]
# for i in range(1, c + 1):
#     for j in range(n):
#         if arr[j][0] < limit:
#             cal = dp[i - arr[j][0]] + arr[j][1]
            
#             if cal <= c:
#                 dp[i] = max(cal, dp[i])
#     if dp[i] == c:
#         result = i
#         break

print(dp)
print(result)