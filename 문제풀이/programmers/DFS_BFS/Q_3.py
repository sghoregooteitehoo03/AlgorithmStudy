# BFS로 풀이
# 각 위치 및 카운트를 담음
# 도착했을때의 카운트가 낮아야됨
from collections import deque
INF = 1e9

def bfs(maps):
    queue = deque([(0, 0, 1)])

    n = len(maps)
    m = len(maps[0])
    board = [[INF] * m for _ in range(n)]
    board[0][0] = 1

    while queue:
        a, b, count = deque.popleft(queue)

        if a + 1 < n and maps[a + 1][b] != 0 and board[a + 1][b] > count + 1:
            queue.append((a + 1, b, count + 1))
            board[a + 1][b] = count + 1
        if a - 1 >= 0 and maps[a - 1][b] != 0 and board[a - 1][b] > count + 1:
            queue.append((a - 1, b, count + 1))
            board[a - 1][b] = count + 1
        if b + 1 < m and maps[a][b + 1] != 0 and board[a][b + 1] > count + 1:
            queue.append((a, b + 1, count + 1))
            board[a][b + 1] = count + 1
        if b - 1 >= 0 and maps[a][b - 1] != 0 and board[a][b - 1] > count + 1:
            queue.append((a, b - 1, count + 1))
            board[a][b - 1] = count + 1

    return board[n - 1][m - 1]

def solution(maps):
    answer = bfs(maps)

    if answer == INF:
        return -1
    else:
        return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))