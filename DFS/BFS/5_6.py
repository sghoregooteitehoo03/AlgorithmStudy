from collections import deque

n, m = map(int, input().split())
board = []

for i in range(n):
    board.append(list(map(int, input())))

def find(start_pos):
    q = deque([start_pos])
    
    while q:
        pos_i, pos_j, next = q.popleft()

        if(pos_i == n - 1 and pos_j == m - 1):
            print(next)
            break
        
        visited = board[pos_i][pos_j] == 0
        if not visited:
            board[pos_i][pos_j] = 0

            if pos_i + 1 < n:
                q.append((pos_i + 1, pos_j, next + 1))
            if pos_i - 1 >= 0:
                q.append((pos_i - 1, pos_j, next + 1))
            if pos_j + 1 < m:
                q.append((pos_i, pos_j + 1, next + 1))
            if pos_j - 1 >= 0:
                q.append((pos_i, pos_j - 1, next + 1))

find((0, 0, 1))


# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111