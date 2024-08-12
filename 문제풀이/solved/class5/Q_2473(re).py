import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = [1e9, 1e9, 1e9]

for k in range(n):
    i = k + 1
    j = n - 1

    while i < j:
        if abs(arr[i] + arr[j] + arr[k]) < abs(sum(result)):
            result = [arr[i], arr[j], arr[k]]

        if arr[i] + arr[j] + arr[k] < 0:
            i += 1
        else:
            j -= 1

result.sort()
print(result[0], end=' ')
print(result[1], end=' ')
print(result[2])