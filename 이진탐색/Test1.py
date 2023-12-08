def search(arr, start, end, findValue):
    if start > end:
        return 'no'
    
    mid = (start + end) // 2

    if findValue == arr[mid]:
        return 'Yes'
    elif findValue < arr[mid]:
        return search(arr, start, mid-1, findValue)
    else:
        return search(arr, mid + 1, end, findValue)

n = int(input())
shopList = list(map(int, input().split()))
shopList.sort()

m = int(input())
orderList = list(map(int, input().split()))

for i in orderList:
    print(search(shopList, 0, len(shopList) - 1, i), end=' ')