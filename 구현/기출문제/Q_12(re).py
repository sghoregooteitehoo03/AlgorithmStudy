# https://school.programmers.co.kr/learn/courses/30/lessons/60061
# https://school.programmers.co.kr/learn/courses/30/lessons/60061
# a = 0(기둥), a = 1(보)
# b = 0(삭제), a = 1(설치)


# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
def checkPillar(board, x, y):
    return (
        y == 0
        or board[x][y] == "|"
        or board[x - 1][y] == "|"
        or board[x][y - 1] == "-"
        or board[x][y - 1] == "ㄱ"
    )


# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
def checkBeam(board, x, y):
    return (
        board[x][y - 1] == "-"
        or board[x + 1][y - 1] == "-"
        or (
            (board[x - 1][y] == "ㄱ" or board[x - 1][y] == "|")
            and (board[x + 1][y] == "ㄱ" or board[x + 1][y] == "|")
        )
    )


def checkBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "-":
                if not checkPillar(board, i, j):
                    return False
            elif board[i][j] == "|":
                if not checkBeam(board, i, j):
                    return False
            elif board[i][j] == "ㄱ":
                if not checkPillar(board, i, j):
                    return False
                if not checkBeam(board, i, j):
                    return False

    return True


def solution(n, build_frame):
    answer = []
    board = [[""] * (n + 1) for _ in range(n + 1)]

    for frame in build_frame:
        x, y, a, b = frame

        if b == 0:
            prevalue = board[x][y]
            board[x][y] = ""
            if a == 0 and board[x][y] == "ㄱ":
                board[x][y] = "|"
            elif a == 1 and board[x][y] == "ㄱ":
                board[x][y] = "-"

            if not checkBoard(board):
                board[x][y] = prevalue
        else:
            if a == 0:
                if checkPillar(board, x, y):
                    if board[x][y] == "|":
                        board[x][y] = "ㄱ"
                    else:
                        board[x][y] = "-"
            else:
                if checkBeam(board, x, y):
                    board[x][y] = "|"

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != "":
                if board[i][j] == "ㄱ":
                    answer.append([i, j, 1])
                    answer.append([i, j, 0])
                elif board[i][j] == "-":
                    answer.append([i, j, 0])
                elif board[i][j] == "|":
                    answer.append([i, j, 1])

    return answer

# def check_condition(board, x, y, a):
#     if a == 1: #보
#         if board[x][y - 1] == 0 or (x + 1 < len(board) and board[x + 1][y - 1] == 0):
#             return True
#         elif board[x][y - 1] == 2 or (x + 1 < len(board) and board[x + 1][y - 1] == 2):
#             return True
#         elif x + 1 < len(board) and x - 1 >= 0 and ((board[x - 1][y] == 1 and board[x + 1][y] == 1) or ((board[x - 1][y] == 2 and board[x + 1][y] == 2))):
#             return True
#     else: # 기둥
#         if y == 0 or board[x][y - 1] == 0 or board[x][y - 1] == 2:
#             return True
#         elif board[x][y] == 1 or (x - 1 >= 0 and board[x - 1][y] == 1):
#             return True

#     return False

# def check_all_board(board, n):
#     for i in range(n + 1):
#         for j in range(n + 1):
#             if board[i][j] == 5:
#                 continue

#             if not check_condition(board, i, j, board[i][j]):
#                 return False

#     return True

# def solution(n, build_frame):
#     answer = []
#     board = [[5] * (n + 1) for _ in range(n + 1)]

#     for bf in build_frame:
#         x, y, a, b = bf

#         if b == 1: # 설치
#             if check_condition(board, x, y, a):
#                 if board[x][y] != 5:
#                     board[x][y] = 2
#                 else:
#                     board[x][y] = a
#         else: # 삭제
#             temp = board[x][y]
#             board[x][y] = 5

#             if not check_all_board(board, n):
#                 board[x][y] = temp

#     for i in range(n + 1):
#         for j in range(n + 1):
#             if board[i][j] == 5:
#                 continue

#             answer.append([i, j, board[i][j]])
#     return answer

# solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
solution(
    5,
    [
        [0, 0, 0, 1],
        [2, 0, 0, 1],
        [4, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [2, 1, 1, 1],
        [3, 1, 1, 1],
        [2, 0, 0, 0],
        [1, 1, 1, 0],
        [2, 2, 0, 1],
    ],
)
