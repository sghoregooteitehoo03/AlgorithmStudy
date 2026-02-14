# https://www.acmicpc.net/problem/2110
n, c = map(int, input().split())
homes = []

for i in range(n):
    homes.append(int(input()))
homes.sort()

start = 1
end = homes[-1] + homes[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    current_pos = homes[0]
    count = 1

    for i in range(1, len(homes)):
        if homes[i] - current_pos >= mid:
            count += 1
            current_pos = homes[i]

    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)