n = int(input())
arr = list(map(int, input().split()))

def binary_search():
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if mid == arr[mid]:
            return mid
        elif mid > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


result = binary_search()
print(result)