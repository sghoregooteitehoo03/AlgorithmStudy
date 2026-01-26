# https://www.acmicpc.net/problem/3190
n = int(input())
board = [[0] * n for _ in range(n)]
board[0][0] = 1
snake = [(0, 0, 1)]

k = int(input())
for _ in range(k):
    i, j = map(int, input().split())
    board[i - 1][j - 1] = 5

l = int(input())
directions = []
for _ in range(l):
    t, d = input().split()
    directions.append((int(t), d))

time = 0
while True:
    time += 1
    previous_snake = 0
    tail_snake = 0
    isEatApple = False
    isEnd = False
    for i in range(len(snake)):
        current_snake = snake[i]
        tail_snake = snake[i]

        if current_snake[2] == 1:
            next_pos_snake = (current_snake[0], current_snake[1] + 1, 1)
        elif current_snake[2] == 3:
            next_pos_snake = (current_snake[0], current_snake[1] - 1, 3)
        elif current_snake[2] == 2:
            next_pos_snake = (current_snake[0] + 1, current_snake[1], 2)
        else:
            next_pos_snake = (current_snake[0] - 1, current_snake[1], 0)

        if (
            next_pos_snake[0] >= n
            or next_pos_snake[0] < 0
            or next_pos_snake[1] >= n
            or next_pos_snake[1] < 0
        ):
            isEnd = True
            break

        if board[next_pos_snake[0]][next_pos_snake[1]] == 1:
            isEnd = True
            break
        elif board[next_pos_snake[0]][next_pos_snake[1]] == 5:
            isEatApple = True

        board[next_pos_snake[0]][next_pos_snake[1]] = 1
        board[current_snake[0]][current_snake[1]] = 0

        if previous_snake != 0:
            snake[i] = (next_pos_snake[0], next_pos_snake[1], previous_snake[2])
        else:
            direction = current_snake[2]
            if len(directions) != 0 and directions[0][0] == time:
                if directions[0][1] == "L":
                    direction -= 1
                    if direction < 0:
                        direction = 3
                elif directions[0][1] == "D":
                    direction += 1
                    if direction > 3:
                        direction = 0

                directions.pop(0)

            snake[i] = (next_pos_snake[0], next_pos_snake[1], direction)

        previous_snake = current_snake

    if isEnd:
        break

    if isEatApple:
        board[tail_snake[0]][tail_snake[1]] = 1
        snake.append(tail_snake)

print(time)

# from collections import deque

# n = int(input())
# k = int(input())
# board = [[0] * (n + 1) for _ in range(n + 1)]

# for i in range(k):
#     a, b = map(int, input().split())
#     board[a][b] = 1

# l = int(input())
# movements = []
# way = {
#     'L': -1,
#     'D': 1
# }
# directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# for i in range(l):
#     x, c = input().split()
#     movements.append((int(x), c))

# is_collision = False

# next_move_index = 0
# current_direct_index = 1
# current_head_pos = (1, 1)
# q = deque([])
# time = 0

# while not is_collision:
#     if board[current_head_pos[0]][current_head_pos[1]] != 1:
#         if q:
#             previous_head_pos = q.popleft()
#             board[previous_head_pos[0]][previous_head_pos[1]] = 0

#     board[current_head_pos[0]][current_head_pos[1]] = 5

#     movement = movements[next_move_index]
#     if movement[0] == time:
#         current_direct_index = (current_direct_index + way[movement[1]]) % 4

#         if next_move_index + 1 < len(movements):
#             next_move_index += 1

#     next_pos = (current_head_pos[0] + directions[current_direct_index][0], current_head_pos[1] + directions[current_direct_index][1])
#     if next_pos[0] < 1 or next_pos[0] >= len(board) or next_pos[1] < 1 or next_pos[1] >= len(board):
#         is_collision = True
#     elif board[next_pos[0]][next_pos[1]] == 5:
#         is_collision = True

#     q.append(current_head_pos)
#     current_head_pos = next_pos
#     time += 1

# print(time)
