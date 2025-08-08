def search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
        
    return False

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
search_arr = list(map(int, input().split()))

for number in search_arr:
    if search(arr, number, 0, n - 1):
        print('yes', end=' ')
    else:
        print('no', end=' ')

# def search(arr, start, end, findValue):
#     if start > end:
#         return 'no'
    
#     mid = (start + end) // 2

#     if findValue == arr[mid]:
#         return 'Yes'
#     elif findValue < arr[mid]:
#         return search(arr, start, mid-1, findValue)
#     else:
#         return search(arr, mid + 1, end, findValue)

# n = int(input())
# shopList = list(map(int, input().split()))
# shopList.sort()

# m = int(input())
# orderList = list(map(int, input().split()))

# for i in orderList:
#     print(search(shopList, 0, len(shopList) - 1, i), end=' ')