# https://school.programmers.co.kr/learn/courses/30/lessons/60059

def increase_array(arr):
    transce_arr = []
    arr_len = len(arr)

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                transce_arr.append(arr)
            else:
                transce_arr.append([[0] * arr_len for _ in range(arr_len)])
    return transce_arr

def solution(key, lock):
    transce_lock = increase_array(lock)
    arr_range = ((len(lock) * 3) - len(lock) + 1)

    # print(transce_lock[0])
    for i in range(arr_range):
        for j in range(arr_range):
            print(j)
            for i2 in range(i, i + len(lock)):
                for j2 in range(j, j + len(lock)):
                    print(transce_lock[j][i2][j2])


solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
# solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])