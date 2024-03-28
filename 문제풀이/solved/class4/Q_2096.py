import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

arr[0][0] = (arr[0][0], arr[0][0])
arr[0][1] = (arr[0][1], arr[0][1])
arr[0][2] = (arr[0][2], arr[0][2])

for i in range(1, n):
    for j in range(3):
        cal_arr = []
        
        cal_arr.append(arr[i - 1][j][0] + arr[i][j])
        cal_arr.append(arr[i - 1][j][1] + arr[i][j])
        if j - 1 >= 0:
            cal_arr.append(arr[i - 1][j - 1][0] + arr[i][j])
            cal_arr.append(arr[i - 1][j - 1][1] + arr[i][j])
        if j + 1 < 3:
            cal_arr.append(arr[i - 1][j + 1][0] + arr[i][j])
            cal_arr.append(arr[i - 1][j + 1][1] + arr[i][j])

        arr[i][j] = (max(cal_arr), min(cal_arr))

print(arr)