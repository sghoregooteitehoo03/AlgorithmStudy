# https://www.acmicpc.net/problem/2110
n, c = map(int, input().split())
arr = []

for i in range(n):
    arr.append(int(input()))
arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    current_pos = arr[0]
    count = 1

    for i in range(1, n):
        if arr[i] >= current_pos + mid:
            count += 1
            current_pos = arr[i]

    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
