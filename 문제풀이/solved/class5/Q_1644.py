import sys
import math
input = sys.stdin.readline

n = int(input())
arr = [True] * (n + 1)
prime = []

for i in range(2, int(math.sqrt(n) + 1)):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

for i in range(2, len(arr)):
    if arr[i]:
        prime.append(i)

result = 0
interver_sum = 0
end = 0

for start in range(len(prime)):
    while interver_sum < n and end < len(prime):
        interver_sum += prime[end]
        end += 1

    if interver_sum == n:
        result += 1
    interver_sum -= prime[start]

print(result)