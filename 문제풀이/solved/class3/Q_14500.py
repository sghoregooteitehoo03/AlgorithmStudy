import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map_graph = []

for i in range(n):
    map_graph.append(list(map(int, input().split())))


def check_line(i, j):
    cal1 = 0
    cal2 = 0

    if j + 3 < len(map_graph[0]):
        cal1 = sum(map_graph[i][j:j+4])
    if i + 3 < len(map_graph):
        for k in range(i, i + 4):
            cal2 += map_graph[k][j]

    return max(cal1, cal2)

def check_sqaure(i, j):
    cal = 0
    if i + 1 < len(map_graph) and j + 1 < len(map_graph[0]):
        cal += sum(map_graph[i][j:j+2])
        cal += sum(map_graph[i + 1][j:j+2])

    return cal


def check_zigzag(i, j):
    cal1 = 0
    cal2 = 0
    cal3 = 0
    cal4 = 0

    if i + 2 < len(map_graph) and j + 1 < len(map_graph[0]):
        cal1 += map_graph[i][j]
        cal1 += sum(map_graph[i + 1][j:j+2])
        cal1 += map_graph[i + 2][j + 1]

        cal2 += map_graph[i][j + 1]
        cal2 += sum(map_graph[i + 1][j:j+2])
        cal2 += map_graph[i + 2][j]
    if i + 1 < len(map_graph) and j + 2 < len(map_graph[0]):
        cal3 += sum(map_graph[i][j + 1:j+3])
        cal3 += sum(map_graph[i + 1][j:j+2])

        cal4 += sum(map_graph[i][j:j+2])
        cal4 += sum(map_graph[i + 1][j + 1:j+3])

    return max(cal1, cal2, cal3, cal4)


def check_t(i, j):
    cal1 = 0
    cal2 = 0
    cal3 = 0
    cal4 = 0

    if i + 1 < len(map_graph) and j + 2 < len(map_graph[0]):
        cal1 += sum(map_graph[i][j:j+3])
        cal1 += map_graph[i + 1][j + 1]

        cal2 += map_graph[i][j + 1]
        cal2 += sum(map_graph[i + 1][j:j+3])
    if i + 2 < len(map_graph) and j + 1 < len(map_graph[0]):
        cal3 += map_graph[i][j + 1]
        cal3 += sum(map_graph[i + 1][j:j + 2])
        cal3 += map_graph[i + 2][j + 1]

        cal4 += map_graph[i][j]
        cal4 += sum(map_graph[i + 1][j:j + 2])
        cal4 += map_graph[i + 2][j]

    return max(cal1, cal2, cal3, cal4)


def check_l(i, j):
    cal_arr = [0] * 8

    if i + 2 < len(map_graph) and j + 1 < len(map_graph[0]):
        cal_arr[0] += map_graph[i][j]
        cal_arr[0] += map_graph[i + 1][j]
        cal_arr[0] += sum(map_graph[i + 2][j:j + 2])

        cal_arr[1] += map_graph[i][j + 1]
        cal_arr[1] += map_graph[i + 1][j + 1]
        cal_arr[1] += sum(map_graph[i + 2][j:j + 2])

        cal_arr[2] += sum(map_graph[i][j:j + 2])
        cal_arr[2] += map_graph[i + 1][j]
        cal_arr[2] += map_graph[i + 2][j]

        cal_arr[3] += sum(map_graph[i][j:j + 2])
        cal_arr[3] += map_graph[i + 1][j + 1]
        cal_arr[3] += map_graph[i + 2][j + 1]
    
    if i + 1 < len(map_graph) and j + 2 < len(map_graph[0]):
        cal_arr[4] += sum(map_graph[i][j:j + 3])
        cal_arr[4] += map_graph[i + 1][j]
        
        cal_arr[5] += sum(map_graph[i + 1][j:j + 3])
        cal_arr[5] += map_graph[i][j]

        cal_arr[6] += sum(map_graph[i][j:j + 3])
        cal_arr[6] += map_graph[i + 1][j + 2]

        cal_arr[7] += sum(map_graph[i + 1][j:j + 3])
        cal_arr[7] += map_graph[i][j + 2]

    return max(cal_arr)

result = 0
for i in range(n):
    for j in range(m):
        case1 = check_line(i, j)
        case2 = check_sqaure(i, j)
        case3 = check_zigzag(i, j)
        case4 = check_t(i, j)
        case5 = check_l(i, j)

        max_value = max(case1, case2, case3, case4, case5)

        if result < max_value:
            result = max_value

print(result)