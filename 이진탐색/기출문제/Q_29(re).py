# https://www.acmicpc.net/problem/2110
N, C = map(int, input().split())
home_pos = []
result = 0

for i in range(N):
    home_pos.append(int(input()))

home_pos.sort()

start = 1
end = home_pos[-1] - home_pos[0]

while(start <= end):
    mid = (start + end) // 2
    value = home_pos[0]
    count = 1

    for i in range(1, N):
        if home_pos[i] >= value + mid:
            value = home_pos[i]
            count += 1

    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)