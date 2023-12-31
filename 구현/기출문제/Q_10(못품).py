from collections import deque

def move_key(index_list, list_len, str, holes):
    move_dict = {
        'U':[-1, 0],
        'D':[1, 0],
        'L':[0, -1],
        'R':[0, 1]
    }
    count = 0
    move_list = [[1] * list_len for _ in range(list_len)]
    move_i, move_j = move_dict[str]

    for index in index_list:
        current_i, current_j = index
        sum_i = move_i + current_i
        sum_j = move_j + current_j

        if ((sum_i >= 0 and sum_i < list_len) and (sum_j >= 0 and sum_j < list_len)):
            move_list[sum_i][sum_j] = 0
            count += 1

    if count >= holes:
        return move_list
    else:
        return [[]]

def get_index_summary(_list, find_value):
    index_list = []
    count = 0

    for i in range(len(_list)):
        for j in range(len(_list[i])):
            if _list[i][j] == find_value:
                index_list.append((i, j))
                count += 1

    return (index_list, count)


def solution(key, lock):
    q = deque()
    key_index, key_holes = get_index_summary(key, 1)
    lock_holes = get_index_summary(lock, 0)[1]
    isFind = False

    q.append(key)
    history_key = []
    for i in range(10):
        current_key = q.popleft()
        print(current_key)

        if current_key == lock:
            isFind = True
            break

        if len(current_key) != 0:
            q.append(move_key(key_index, len(key), 'U', lock_holes))
            q.append(move_key(key_index, len(key), 'D', lock_holes))
            q.append(move_key(key_index, len(key), 'R', lock_holes))
            q.append(move_key(key_index, len(key), 'L', lock_holes))
        
    return isFind


solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
