from collections import deque

def rotate_snake(current_direct, rotate):
    d = {
        'L': -1,
        'D': 1
    }

    result = current_direct + d[rotate]
    if result > 3:
        return 0
    elif result < 0:
        return 3
    else:
        return result

def move_snake(arr, current_pos, direct):
    move_pos_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    move_pos = move_pos_list[direct]

    move_row = move_pos[0] + current_pos[0]
    move_col = move_pos[1] + current_pos[1]
    if (move_row < len(arr) and move_row >= 0) and (move_col < len(arr) and move_col >= 0):
        if arr[move_row][move_col] != 0:
            if arr[move_row][move_col] == 7:

                arr[move_row][move_col] = 1
                return (move_row, move_col)    
            else:
                return current_pos
        else:
            arr[move_row][move_col] = 1
            arr[current_pos[0]][current_pos[1]] = 0
            return (move_row, move_col)
    else:
        return current_pos


n = int(input())
k = int(input())
q = deque()
result = 1
is_finished = False
snake_table = [[0] * n for _ in range(n)]
snake_table[0][0] = 1

move_list = []

for i in range(k):
    col, row = map(int, input().split())
    snake_table[row - 1][col - 1] = 7

l = int(input())
for i in range(l):
    time, rotate = input().split()
    move_list.append((int(time), rotate))

current_dict = 0
q.append((0, 0))
for move in move_list:
    if is_finished:
        break

    time, rotate = move
    time -= 1
    
    while q:
        current_pos = q.popleft()

        if time == 0:
            current_dict = rotate_snake(current_dict, rotate)
            q.append(current_pos)
            break

        time -= 1
        result += 1
        moved_pos = move_snake(snake_table, current_pos, current_dict)
        
        if current_pos == moved_pos:
            is_finished = True
            break
        
        q.append(moved_pos)
    
print(result)
print(snake_table)