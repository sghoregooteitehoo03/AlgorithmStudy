# https://www.acmicpc.net/problem/14502
from collections import deque
from copy import deepcopy

def spread_virus(board, virus_pos):
    queue = deque(virus_pos)

    while queue:
        q = queue.popleft()
        i, j, is_start = q

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            continue
        if not is_start and board[i][j] != 0:
            continue

        board[i][j] = 2
        queue.append((i + 1, j, False))
        queue.append((i - 1, j, False))
        queue.append((i, j + 1, False))
        queue.append((i, j - 1, False))

    return board

def check_safe_area(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                count += 1

    return count


n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

area_pos = []
virus_pos = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus_pos.append((i, j, True))
        elif board[i][j] == 0:
            area_pos.append((i, j))

answer = 0
copy_board = deepcopy(board)
for i in range(len(area_pos)):
    copy_board[area_pos[i][0]][area_pos[i][1]] = 1
    
    for j in range(i + 1, len(area_pos)):
        copy_board[area_pos[j][0]][area_pos[j][1]] = 1
        
        for k in range(j + 1, len(area_pos)):
            copy_board[area_pos[k][0]][area_pos[k][1]] = 1
            virus_board = spread_virus(deepcopy(copy_board), virus_pos)
            answer = max(answer, check_safe_area(virus_board))
            
            copy_board[area_pos[k][0]][area_pos[k][1]] = 0
        copy_board[area_pos[j][0]][area_pos[j][1]] = 0
    copy_board[area_pos[i][0]][area_pos[i][1]] = 0


print(answer)