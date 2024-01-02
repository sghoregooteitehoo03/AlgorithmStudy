# https://school.programmers.co.kr/learn/courses/30/lessons/60059
import copy

def check(arr, start, end):
    for i in range(start, end):
        for j in range(start, end):
            if arr[i][j] != 1:
                return False

    return True

def rotate_array(arr):
    arr_len = len(arr)
    rotated_arr = [[0] * arr_len for _ in range(arr_len)]

    for i in range(arr_len):
        for j in range(arr_len):
            rotated_arr[j][arr_len - 1 - i] = arr[i][j]

    return rotated_arr

def increase_array(arr):
    arr_len = len(arr)
    transce_arr = [[0] * (arr_len * 3) for _ in range(arr_len * 3)]

    for i in range(arr_len):
        for j in range(arr_len):
            transce_arr[i + arr_len][j + arr_len] = arr[i][j]
    return transce_arr

def solution(key, lock):
    transce_lock = increase_array(lock)
    lock_len = len(lock)
    key_len = len(key)
    arr_range = lock_len * 2

    for i in range(arr_range):
        for j in range(arr_range):
            for _ in range(4):
                copy_lock = copy.deepcopy(transce_lock)

                for i2 in range(i, i + key_len):
                    for j2 in range(j, j + key_len):
                        copy_lock[i2][j2] += key[i2 - i][j2 - j]

                if check(copy_lock, lock_len, lock_len * 2) == True:
                    return True
                
                key = rotate_array(key)

    return False
                    
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))