# https://school.programmers.co.kr/learn/courses/30/lessons/60059

def rotate_array(arr):
    arr_len(arr)

def increase_array(arr):
    arr_len = len(arr)
    transce_arr = [[0] * (arr_len * 3) for _ in range(arr_len * 3)]

    for i in range(arr_len, arr_len * 2):
        for j in range(arr_len, arr_len * 2):
            transce_arr[i][j] = arr[i - arr_len][j-arr_len]
    return transce_arr

def solution(key, lock):
    transce_lock = increase_array(lock)
    lock_len = len(lock)
    arr_range = ((lock_len * 3) - lock_len + 1) - 1
    answer = [[1] * lock_len for _ in range(lock_len)]

    for i in range(1, arr_range):
        for j in range(1, arr_range):
            for k in range(4):
                copy_lock = transce_lock.copy()

                for i2 in range(i, i + lock_len):
                    for j2 in range(j, j + lock_len):
                        i_zero = i2 - i
                        j_zero = j2 - j

                        copy_lock[i2][j2] += key[i_zero][j_zero]

                if copy_lock[0:lock_len][0:lock_len] == answer:
                    return True

                    
# solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
# solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])