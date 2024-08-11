import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

min_value = 1e9
sum = 0
end = 0
for start in range(n):
    while sum < min_value and end < n:
        sum += arr[end]
        end += 1

    sum -= arr[start]

    