# https://school.programmers.co.kr/learn/courses/30/lessons/60059
import copy

def rotate(key):
    n = len(key)
    new = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            new[j][n-i-1] = key[i][j]
    return new

def solution(key, lock):
    board = []
    n = len(key)
    m = len(lock)
    sum_value = 0
    
    for i in range(m * 3):
        line = []
        for j in range(m * 3):
            if i >= m and i < (m * 2) and j >= m and j < (m * 2):
                line.append(lock[i - m][j - m])
                sum_value += lock[i - m][j - m]
            else:
                line.append(1)
        board.append(line)
    
    if sum_value == m * m:
        return True
    
    for i in range((m - n) + 1, ((m * 3) - n)):
        for j in range((m - n) + 1, ((m * 3) - n)):
            for _ in range(4):
                key = rotate(copy.deepcopy(key))
                new_board = copy.deepcopy(board)
                
                for a in range(n):
                    for b in range(n):
                        new_board[i + a][j + b] += key[a][b]
                
                for a in range(m, m * 2):
                    is_break = False
                    for b in range(m, m * 2):
                        if new_board[a][b] != 1:
                            is_break = True
                            break
                    
                    if is_break:
                        break
                
                if not is_break:
                    return True
                sum_value = 0
            
    return False

# import copy

# def check(arr, start, end):
#     for i in range(start, end):
#         for j in range(start, end):
#             if arr[i][j] != 1:
#                 return False

#     return True

# def rotate_array(arr):
#     arr_len = len(arr)
#     rotated_arr = [[0] * arr_len for _ in range(arr_len)]

#     for i in range(arr_len):
#         for j in range(arr_len):
#             rotated_arr[j][arr_len - 1 - i] = arr[i][j]

#     return rotated_arr

# def increase_array(arr):
#     arr_len = len(arr)
#     transce_arr = [[0] * (arr_len * 3) for _ in range(arr_len * 3)]

#     for i in range(arr_len):
#         for j in range(arr_len):
#             transce_arr[i + arr_len][j + arr_len] = arr[i][j]
#     return transce_arr

# def solution(key, lock):
#     transce_lock = increase_array(lock)
#     lock_len = len(lock)
#     key_len = len(key)
#     arr_range = lock_len * 2

#     for i in range(arr_range):
#         for j in range(arr_range):
#             for _ in range(4):
#                 copy_lock = copy.deepcopy(transce_lock)

#                 for i2 in range(i, i + key_len):
#                     for j2 in range(j, j + key_len):
#                         copy_lock[i2][j2] += key[i2 - i][j2 - j]

#                 if check(copy_lock, lock_len, lock_len * 2) == True:
#                     return True
                
#                 key = rotate_array(key)

#     return False