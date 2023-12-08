n, m = map(int, input().split())
rice_cake = list(map(int, input().split()))

start = 0
end = max(rice_cake)

result = 0
while start <= end:    
    mid = (start + end) // 2
    sum = 0

    for cakeLen in rice_cake:
        if cakeLen > mid:
            sum += (cakeLen - mid)

    if m <= sum:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)