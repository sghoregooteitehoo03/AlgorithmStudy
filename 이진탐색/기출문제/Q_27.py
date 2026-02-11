import bisect

n, x = map(int, input().split())
arr = list(map(int, input().split()))

left_index = bisect.bisect_left(arr, x)
rigth_index = bisect.bisect_right(arr, x)
result = rigth_index - left_index

if result == 0:
    print(-1)
else:
    print(result)