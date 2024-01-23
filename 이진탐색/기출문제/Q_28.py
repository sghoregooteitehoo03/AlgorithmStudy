def binary_search(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return binary_search(arr, start, mid - 1)
    else:
        return binary_search(arr, mid + 1, end)


N = int(input())
array = list(map(int, input().split()))
result = binary_search(array, 0, N - 1)

if result != None:
    print(result)
else:
    print(-1)