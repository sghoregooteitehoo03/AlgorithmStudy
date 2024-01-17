# https://www.acmicpc.net/problem/18428
from collections import deque
import copy
import sys
input = sys.stdin.readline

def check_student(map_table, start_pos):
    q = deque(start_pos)
    is_find = False

    while(q):
        previous_i, previous_j, pos_i, pos_j = q.popleft()

        if map_table[pos_i][pos_j] == 'O':
            continue

        if map_table[pos_i][pos_j] == 'S':
            is_find = True
            break

        if pos_i - 1 >= 0 and (previous_i == pos_i + 1 or previous_i == 0):
            q.append((pos_i, -2, pos_i - 1, pos_j))
        if pos_i + 1 < len(map_table) and (previous_i == pos_i - 1 or previous_i == 0):
            q.append((pos_i, -2, pos_i + 1, pos_j))
        if pos_j - 1 >= 0 and (previous_j == pos_j + 1 or previous_j == 0):
            q.append((-2, pos_j, pos_i, pos_j - 1))
        if pos_j + 1 < len(map_table[0]) and (previous_j == pos_j - 1 or previous_j == 0):
            q.append((-2, pos_j, pos_i, pos_j + 1))

    return is_find

def flatten_2d_array(arr_2d):
    return [element for sublist in arr_2d for element in sublist]

def reshape_to_2d_array(arr_1d, rows, cols):
    return [arr_1d[i:i+cols] for i in range(0, len(arr_1d), cols)]

n = int(input())
map_table = []
start_pos = []

for i in range(n):
    map_table.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if map_table[i][j] == 'T':
            start_pos.append((0, 0, i, j))

flat_map = flatten_2d_array(map_table)
is_find = True

for i in range(len(flat_map) - 2):
    copy_map = copy.deepcopy(flat_map)

    if copy_map[i] == 'X':
        copy_map[i] = 'O'
    else:
        continue

    for j in range(i + 1, len(flat_map) - 1):
        sub_map1 = copy.deepcopy(copy_map)

        if copy_map[j] == 'X':
            copy_map[j] = 'O'
        else:
            continue

        for k in range(j + 1, len(flat_map)):
            sub_map2 = copy.deepcopy(copy_map)
            if copy_map[k] == 'X':
                copy_map[k] = 'O'
            else:
                continue

            is_find = check_student(reshape_to_2d_array(copy_map, n, n), start_pos)    
            if not is_find:
                break
            
            copy_map = sub_map2
        
        if not is_find:
            break
        copy_map = sub_map1
    
    if not is_find:
        break

if is_find:
    print("NO")
else:
    print("YES")