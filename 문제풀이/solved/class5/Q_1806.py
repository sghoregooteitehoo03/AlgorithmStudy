import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

interver_sum = 0
count = 0
end = 0
result = 1e9

for start in range(n):
    while interver_sum < s and end < n:
        count += 1
        interver_sum += arr[end]
        end += 1

    if s <= interver_sum:
        if count < result:
            result = count
    
    interver_sum -= arr[start]
    count -= 1

if result == 1e9 or result < 0:
    print(0)
else:
    print(result)