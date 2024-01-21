# https://www.acmicpc.net/problem/1715
n = int(input())
array = []
result_arr = []

for i in range(n):
    array.append(int(input()))

if n == 1:
    print(array[0])
else:
    array.sort()

    result_arr.append(array[0] + array[1])
    for i in range(2, n - 1):
        if i + 1 < n:
            result_arr.append(array[i] + array[i + 1])
        else:
            print(result_arr)
            print(i)
            result_arr.append(result_arr[i - 2] + result_arr[i - 1])
    
    print(sum(result_arr))
# 110 140