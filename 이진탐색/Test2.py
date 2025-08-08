def search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        result = 0
        
        for n in arr:
            if n > mid:
                result += n - mid
        
        if result == target:
            return mid
        elif target > result:
            end = mid - 1
        else:
            start = mid + 1
        
    return 0

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

print(search(arr, m, 0, arr[-1]))

# n, m = map(int, input().split())
# rice_cake = list(map(int, input().split()))

# start = 0
# end = max(rice_cake)

# result = 0
# while start <= end:    
#     mid = (start + end) // 2
#     sum = 0

#     for cakeLen in rice_cake:
#         if cakeLen > mid:
#             sum += (cakeLen - mid)

#     if m <= sum:
#         result = mid
#         start = mid + 1
#     else:
#         end = mid - 1

# print(result)