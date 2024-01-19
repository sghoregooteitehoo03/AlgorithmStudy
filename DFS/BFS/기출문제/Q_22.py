from collections import deque


def solution(board):
    answer = 0
    q = deque([((0, 0), (0, 1), 0)])

    while (q):
        boat_left, boat_right, count = q.popleft()

        boat_left_i, boat_left_j = boat_left
        boat_right_i, boat_right_j = boat_right

        if boat_right_i == len(board) - 1 and boat_right_j == len(board) - 1:
            answer = count
            print(count)
            break

        # 위로 이동
        if boat_left_i - 1 >= 0 and boat_right_i - 1 >= 0:
            if board[boat_left_i - 1][boat_left_j] != 1 and board[boat_right_i - 1][boat_right_j] != 1:
                q.append((
                    (boat_left_i - 1, boat_left_j),
                    (boat_right_i - 1, boat_right_j),
                    count + 1
                ))
        
        # 아래로 이동
        if boat_left_i + 1 < len(board) and boat_right_i + 1 < len(board):
            if board[boat_left_i + 1][boat_left_j] != 1 and board[boat_right_i + 1][boat_right_j] != 1:
                q.append((
                    (boat_left_i + 1, boat_left_j),
                    (boat_right_i + 1, boat_right_j),
                    count + 1
                ))

        # 왼쪽으로 이동
        if boat_left_j - 1 >= 0 and boat_right_j - 1 >= 0:
            if board[boat_left_i][boat_left_j - 1] != 1 and board[boat_right_i][boat_right_j - 1] != 1:
                q.append((
                    (boat_left_i, boat_left_j - 1),
                    (boat_right_i, boat_right_j - 1),
                    count + 1
                ))

        # 오른쪽으로 이동
        if boat_left_j + 1 < len(board) and boat_right_i + 1 < len(board):
            if board[boat_left_i][boat_left_j + 1] != 1 and board[boat_right_i][boat_right_j + 1] != 1:
                q.append((
                    (boat_left_i, boat_left_j + 1),
                    (boat_right_i, boat_right_j + 1),
                    count + 1
                ))

        # 배가 가로 상태인 경우
        if boat_left_i == boat_right_i:
            # 왼쪽기준 대각선 아래로 이동
            if boat_right_i + 1 < len(board) and boat_right_j - 1 >= 0:
                if board[boat_left_i + 1][boat_left_j] != 1 and board[boat_right_i + 1][boat_right_j] != 1:
                    q.append((
                        (boat_left_i, boat_left_j),
                        (boat_right_i + 1, boat_right_j - 1),
                        count + 1
                    ))

            # 왼쪽 기준 대각선 위로 이동
            if boat_right_i - 1 >= 0 and boat_right_j - 1 >= 0:
                if board[boat_left_i - 1][boat_left_j] != 1 and board[boat_right_i - 1][boat_right_j] != 1:
                    q.append((
                        (boat_right_i - 1, boat_right_j - 1), # 왼쪽이 무조건 위로 오게끔
                        (boat_left_i, boat_left_j),
                        count + 1
                    ))

            # 오른쪽 기준 대각선 아래로 이동
            if boat_left_i + 1 < len(board) and boat_right_j + 1 < len(board):
                if board[boat_left_i + 1][boat_left_j] != 1 and board[boat_right_i + 1][boat_right_j] != 1:
                    q.append((
                        (boat_right_i, boat_right_j),
                        (boat_left_i + 1, boat_left_j + 1), # 왼쪽이 무조건 위로 오게끔
                        count + 1
                    ))

            # 오른쪽 기준 대각선 위로 이동
            if boat_left_i - 1 >= 0 and boat_right_j + 1 < len(board):
                if board[boat_left_i - 1][boat_left_j] != 1 and board[boat_right_i - 1][boat_right_j] != 1:
                    q.append((
                        (boat_left_i - 1, boat_left_j + 1),
                        (boat_right_i, boat_right_j),
                        count + 1
                    ))
        else: # 배가 세로인 경우
            # 왼쪽 기준 왼쪽 대각선 위로 이동
            if boat_right_i - 1 >= 0 and boat_right_j - 1 >= 0:
                if board[boat_left_i][boat_left_j - 1] != 1 and board[boat_right_i][boat_right_j - 1] != 1:
                    q.append((
                        (boat_right_i - 1, boat_right_j - 1),
                        (boat_left_i, boat_left_j),
                        count + 1
                    ))

            # 왼쪽 기준 오른쪽 대각선 위로 이동
            if boat_right_i - 1 >= 0 and boat_right_j + 1 < len(board):
                if board[boat_left_i][boat_left_j + 1] != 1 and board[boat_right_i][boat_right_j + 1] != 1:
                    q.append((
                        (boat_left_i, boat_left_j),
                        (boat_right_i - 1, boat_right_j + 1),
                        count + 1
                    ))

            # 오른쪽 기준 왼쪽 대각선 아래로 이동
            if boat_left_i + 1 < len(board) and boat_left_j - 1 >= 0:
                if board[boat_left_i][boat_left_j - 1] != 1 and board[boat_right_i][boat_right_j - 1] != 1:
                    q.append((
                        (boat_left_i + 1, boat_left_j - 1),
                        (boat_right_i, boat_right_j),
                        count + 1
                    ))

            # 오른쪽 기준 오른쪽 대각선 아래로 이동 
            if boat_left_i + 1 < len(board) and boat_left_j + 1 < len(board):
                if board[boat_left_i][boat_left_j + 1] != 1 and board[boat_right_i][boat_right_j + 1] != 1:
                    q.append((
                        (boat_right_i, boat_right_j),
                        (boat_left_i + 1, boat_left_j + 1),
                        count + 1
                    ))

    return answer

solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])
