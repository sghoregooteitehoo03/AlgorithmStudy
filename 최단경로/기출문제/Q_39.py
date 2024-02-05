from collections import deque
INF = int(1e9)
result_arr = []

t = int(input())
for i in range(t):
    n = int(input())
    q = deque([])
    map_array = []
    result = [[INF] * n for _ in range(n)]

    for i in range(n):
        map_array.append(list(map(int, input().split())))

    result[0][0] = map_array[0][0]
    q.append((0, 0))
    while (q):
        pos_i, pos_j = q.popleft()
        current_value = result[pos_i][pos_j]

        if pos_i + 1 < n:
            cal_value = current_value + map_array[pos_i + 1][pos_j]

            if cal_value < result[pos_i + 1][pos_j]:
                result[pos_i + 1][pos_j] = cal_value
                q.append((pos_i + 1, pos_j))

        if pos_i - 1 >= 0:
            cal_value = current_value + map_array[pos_i - 1][pos_j]

            if cal_value < result[pos_i - 1][pos_j]:
                result[pos_i - 1][pos_j] = cal_value
                q.append((pos_i - 1, pos_j))

        if pos_j + 1 < n:
            cal_value = current_value + map_array[pos_i][pos_j + 1]

            if cal_value < result[pos_i][pos_j + 1]:
                result[pos_i][pos_j + 1] = cal_value
                q.append((pos_i, pos_j + 1))

        if pos_j - 1 >= 0:
            cal_value = current_value + map_array[pos_i][pos_j - 1]

            if cal_value < result[pos_i][pos_j - 1]:
                result[pos_i][pos_j - 1] = cal_value
                q.append((pos_i, pos_j - 1))

    result_arr.append(result[n - 1][n - 1])

for result in result_arr:
    print(result)