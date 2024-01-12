# https://www.acmicpc.net/problem/14502
from collections import deque
import copy
import sys
input = sys.stdin.readline

def flatten_2d_array(arr_2d):
    return [element for sublist in arr_2d for element in sublist]

def reshape_to_2d_array(arr_1d, rows, cols):
    return [arr_1d[i:i+cols] for i in range(0, len(arr_1d), cols)]

def spread_check(map_table, start_pos):
    q = deque(start_pos)
    
    copy_map = copy.deepcopy(map_table)
    visited = [[False] * len(map_table[0]) for _ in range(len(map_table))]

    while q:
        pos_i, pos_j = q.popleft()

        if not visited[pos_i][pos_j]:
                visited[pos_i][pos_j] = True
                copy_map[pos_i][pos_j] = 2

                if pos_i - 1 >= 0 and copy_map[pos_i - 1][pos_j] == 0:
                    q.append((pos_i - 1, pos_j))
                if pos_i + 1 < len(map_table) and copy_map[pos_i + 1][pos_j] == 0:
                    q.append((pos_i + 1, pos_j))
                if pos_j - 1 >= 0 and copy_map[pos_i][pos_j - 1] == 0:
                    q.append((pos_i, pos_j - 1))
                if pos_j + 1 < len(map_table[0]) and copy_map[pos_i][pos_j + 1] == 0:
                    q.append((pos_i, pos_j + 1))

    result = 0
    for i in range(len(copy_map)):
        for j in range(len(copy_map[0])):
            if copy_map[i][j] == 0:
                result += 1
    
    return result

def placed(map_table, start_pos, n, m):
    flat_map = flatten_2d_array(map_table)
    result = 0
    
    for i in range(len(flat_map) - 2):
        copy_map = copy.deepcopy(flat_map)

        if copy_map[i] == 0:
            copy_map[i] = 1
        else:
            continue
        for j in range(i + 1, len(flat_map) - 1):
            sub_map1 = copy.deepcopy(copy_map)

            if copy_map[j] == 0:
                copy_map[j] = 1
            else:
                continue
            
            for k in range(j + 1,len(flat_map)):
                sub_map2 = copy.deepcopy(copy_map)
                if copy_map[k] == 0:
                    copy_map[k] = 1
                else:
                    continue

                big = spread_check(reshape_to_2d_array(copy_map, n, m), start_pos)
                if result < big:
                    result = big

                copy_map = sub_map2
            copy_map = sub_map1
                
    print(result)

n, m = map(int, input().split())
map_table = []
virus_pos = []

for i in range(n):
    map_table.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if map_table[i][j] == 2:
            virus_pos.append((i, j))

placed(map_table, virus_pos, n, m)