# https://www.acmicpc.net/problem/3190
from collections import deque

n = int(input())
k = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1

l = int(input())
movements = []
way = {
    'L': -1,
    'D': 1
}
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(l):
    x, c = input().split()
    movements.append((int(x), c))

is_collision = False

next_move_index = 0
current_direct_index = 1
current_head_pos = (1, 1)
q = deque([])
time = 0

while not is_collision:
    if board[current_head_pos[0]][current_head_pos[1]] != 1:
        if q:
            previous_head_pos = q.popleft()
            board[previous_head_pos[0]][previous_head_pos[1]] = 0
    
    board[current_head_pos[0]][current_head_pos[1]] = 5
    
    movement = movements[next_move_index]
    if movement[0] == time:
        current_direct_index = (current_direct_index + way[movement[1]]) % 4
        
        if next_move_index + 1 < len(movements):
            next_move_index += 1
    
    next_pos = (current_head_pos[0] + directions[current_direct_index][0], current_head_pos[1] + directions[current_direct_index][1])
    if next_pos[0] < 1 or next_pos[0] >= len(board) or next_pos[1] < 1 or next_pos[1] >= len(board):
        is_collision = True
    elif board[next_pos[0]][next_pos[1]] == 5:
        is_collision = True
    
    q.append(current_head_pos)
    current_head_pos = next_pos
    time += 1

print(time)