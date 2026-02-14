def getMaxGold(n, m, arr):
    for j in range(1, m):
        for i in range(n):
            left_up = 0
            if i - 1 >= 0:
                left_up = arr[i - 1][j - 1]

            left = arr[i][j - 1]

            left_down = 0
            if i + 1 < n:
                left_down = arr[i + 1][j - 1]

            arr[i][j] = arr[i][j] + max(left_up, left, left_down)

    result = 0
    for i in range(n):
        result = max(result, arr[i][m - 1])
    return result


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr2 = [[] for _ in range(n)]

    j = m
    for i in range(n):
        arr2[i] = arr[i * m : j]
        j += m

    print(getMaxGold(n, m, arr2))
