from collections import deque

def reshape_to_2d_array(arr_1d, cols):
    return [arr_1d[i:i+cols] for i in range(0, len(arr_1d), cols)]

def get_max_gold(arr,n, m):
    q = deque([])
    map_table = [[0] * (m) for _ in range(n)]
    result = 0
    
    for i in range(n):
        value = arr[i][0]
        q.append((i, 0, value, 1))
        map_table[i][0] = value

    while(q):
        i, j, value, count = q.popleft()

        if count > m:
            continue
        
        if count != 1:
            value += arr[i][j]
        
            if value > map_table[i][j]:
                map_table[i][j] = value
                if result < value:
                    result = value

        if j + 1 < m:
            q.append((i, j + 1, value, count + 1))

            if i - 1 >= 0:
                q.append((i - 1, j + 1, value, count + 1))
            if i + 1 < n:
                q.append((i + 1, j + 1, value, count + 1))

    return result

T = int(input())
result_arr = []

for i in range(T):
    n, m = map(int, input().split())
    mine = list(map(int, input().split()))
    
    mine_map = reshape_to_2d_array(mine, m)
    result = get_max_gold(mine_map, n, m)
    result_arr.append(result)

for result in result_arr:
    print(result)