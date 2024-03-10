k, n = map(int, input().split())
data = []

for i in range(k):
    data.append(int(input()))

start = 1
end = max(data)
while(start <= end):
    mid = (start + end) // 2
    summary = 0

    for d in data:
        summary += (d // mid)

    if summary < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)