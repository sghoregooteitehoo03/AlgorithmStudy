import sys
input = sys.stdin.readline

def binary_search(start, end, arr, number, standard):
    result = standard
    result_end = -1
    ordinary_start = start

    while start <= end:
        mid = (start + end) // 2

        if abs(arr[mid] + number) <= result and ordinary_start != mid:
            result = abs(arr[mid] + number)
            result_end = mid
            
        if abs(number) < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return (result, result_end)

n = int(input())
arr = list(map(int, input().split()))

result = 1e10
start_pos = -1
end_pos = -1

for i in range(n - 1):
    search = binary_search(i, n - 1, arr, arr[i], result)
    if search[0] <= result and search[1] != -1 and search[1] != i:
        result = search[0]
        
        start_pos = i
        end_pos = search[1]

print(arr[start_pos], end=' ')
print(arr[end_pos])