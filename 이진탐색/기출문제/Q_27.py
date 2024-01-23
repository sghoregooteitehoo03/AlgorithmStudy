import bisect

def get_count(arr, find_value):
    left_index = bisect.bisect_left(arr, find_value)
    right_index = bisect.bisect_right(arr, find_value)

    return right_index - left_index

N, x = map(int, input().split())
array = list(map(int, input().split()))

result = get_count(array, x)
if result == 0:
    print(-1)
else:
    print(result)