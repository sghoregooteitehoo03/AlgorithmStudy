# https://school.programmers.co.kr/learn/courses/30/lessons/60061
def check_condition(board, x, y, a):
    if a == 1: #보
        if board[x][y - 1] == 0 or (x + 1 < len(board) and board[x + 1][y - 1] == 0):
            return True
        elif board[x][y - 1] == 2 or (x + 1 < len(board) and board[x + 1][y - 1] == 2):
            return True
        elif x + 1 < len(board) and x - 1 >= 0 and ((board[x - 1][y] == 1 and board[x + 1][y] == 1) or ((board[x - 1][y] == 2 and board[x + 1][y] == 2))):
            return True
    else: # 기둥
        if y == 0 or board[x][y - 1] == 0 or board[x][y - 1] == 2:
            return True
        elif board[x][y] == 1 or (x - 1 >= 0 and board[x - 1][y] == 1):
            return True
        
    return False

def check_all_board(board, n):
    for i in range(n + 1):
        for j in range(n + 1):
            if board[i][j] == 5:
                continue
            
            if not check_condition(board, i, j, board[i][j]):
                return False
            
    return True

def solution(n, build_frame):
    answer = []
    board = [[5] * (n + 1) for _ in range(n + 1)]
    
    for bf in build_frame:
        x, y, a, b = bf
        
        if b == 1: # 설치
            if check_condition(board, x, y, a):
                if board[x][y] != 5:
                    board[x][y] = 2
                else: 
                    board[x][y] = a
        else: # 삭제
            temp = board[x][y]
            board[x][y] = 5
            
            if not check_all_board(board, n):
                board[x][y] = temp
    
    for i in range(n + 1):
        for j in range(n + 1):
            if board[i][j] == 5:
                continue
            
            answer.append([i, j, board[i][j]])
    return answer

# solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
solution(5, [[0,0,0,1], [2,0,0,1], [4,0,0,1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])