# 시뮬레이션 문제
# 이전 방문한 곳은 다시 돌아갈 필요없음
# 둘다 이동 조건에 만족했을때만 큐에 넣어서 처리
import sys
sys.setrecursionlimit(10000)

INF = 1e9
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(maze):
    answer = INF
    n = len(maze)
    m = len(maze[0])

    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                rx, ry = i, j
            elif maze[i][j] == 2:
                bx, by = i, j

    visited_red = [[False] * m for _ in range(n)]
    visited_blue = [[False] * m for _ in range(n)]
    visited_red[rx][ry] = True
    visited_blue[bx][by] = True

    def dfs(rx, ry, bx, by, count):
        nonlocal answer
        if maze[rx][ry] == 3 and maze[bx][by] == 4:
            answer = min(answer, count)
            return
        
        red_moves = []
        if maze[rx][ry] == 3:
            red_moves.append((rx, ry))
        else:
            for i in range(4):
                nx = rx + dx[i]
                ny = ry + dy[i]

                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 5 and not visited_red[nx][ny]:
                    red_moves.append((nx, ny))
        
        blue_moves = []
        if maze[bx][by] == 4:
            blue_moves.append((bx, by))
        else:
            for i in range(4):
                nx = bx + dx[i]
                ny = by + dy[i]

                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 5 and not visited_blue[nx][ny]:
                    blue_moves.append((nx, ny))

        for red_move in red_moves:
            for blue_move in blue_moves:
                if red_move[0] == blue_move[0] and red_move[1] == blue_move[1]:
                    continue
                if red_move[0] == bx and red_move[1] == by and blue_move[0] == rx and blue_move[1] == ry:
                    continue

                if maze[rx][ry] != 3: 
                    visited_red[red_move[0]][red_move[1]] = True
                if maze[bx][by] != 4: 
                    visited_blue[blue_move[0]][blue_move[1]] = True

                dfs(red_move[0], red_move[1], blue_move[0], blue_move[1], count + 1)

                if maze[rx][ry] != 3: 
                    visited_red[red_move[0]][red_move[1]] = False
                if maze[bx][by] != 4: 
                    visited_blue[blue_move[0]][blue_move[1]] = False
    
    dfs(rx, ry, bx, by, 0)
    if answer != INF:
        return answer
    else:
        return 0

# import sys
# sys.setrecursionlimit(10000)
# INF = 1e9

# def solution(maze):
#     n = len(maze)
#     m = len(maze[0])
    
#     # 상, 하, 좌, 우 방향 배열
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
    
#     # 1. 시작점과 도착점 찾기
#     rx, ry, bx, by = 0, 0, 0, 0
#     for i in range(n):
#         for j in range(m):
#             if maze[i][j] == 1: rx, ry = i, j
#             elif maze[i][j] == 2: bx, by = i, j
                
#     # 빨간 수레와 파란 수레의 독립적인 방문 배열
#     visited_r = [[False] * m for _ in range(n)]
#     visited_b = [[False] * m for _ in range(n)]
#     visited_r[rx][ry] = True
#     visited_b[bx][by] = True
    
#     answer = INF
    
#     # 2. DFS 함수 설계
#     def dfs(rx, ry, bx, by, count):
#         nonlocal answer
        
#         # [종료 조건] 두 수레 모두 도착점에 도달했으면 최소 턴 수 갱신
#         if maze[rx][ry] == 3 and maze[bx][by] == 4:
#             answer = min(answer, count)
#             return
        
#         # [빨간 수레] 다음 이동 후보지 구하기
#         red_moves = []
#         if maze[rx][ry] == 3:
#             red_moves.append((rx, ry)) # 이미 도착했으면 제자리 고정
#         else:
#             for i in range(4):
#                 nx, ny = rx + dx[i], ry + dy[i]
#                 # 격자 안이고, 벽(5)이 아니며, 방문하지 않은 곳
#                 if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 5 and not visited_r[nx][ny]:
#                     red_moves.append((nx, ny))
                    
#         # [파란 수레] 다음 이동 후보지 구하기
#         blue_moves = []
#         if maze[bx][by] == 4:
#             blue_moves.append((bx, by)) # 이미 도착했으면 제자리 고정
#         else:
#             for i in range(4):
#                 nx, ny = bx + dx[i], by + dy[i]
#                 if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 5 and not visited_b[nx][ny]:
#                     blue_moves.append((nx, ny))
                    
#         # [이동 및 백트래킹] 가능한 모든 이동 조합 맞춰보기
#         for nrx, nry in red_moves:
#             for nbx, nby in blue_moves:
#                 # 룰 1. 두 수레가 동시에 같은 칸으로 갈 수 없음
#                 if nrx == nbx and nry == nby:
#                     continue
#                 # 룰 2. 두 수레가 서로 자리를 바꿀 수 없음 (크로스 금지)
#                 if nrx == bx and nry == by and nbx == rx and nby == ry:
#                     continue
                    
#                 # 이동할 칸 방문 처리 (이미 도착해서 제자리인 수레는 굳이 처리 안 해도 됨)
#                 if maze[rx][ry] != 3: visited_r[nrx][nry] = True
#                 if maze[bx][by] != 4: visited_b[nbx][nby] = True
                
#                 # 다음 턴 진행
#                 dfs(nrx, nry, nbx, nby, count + 1)
                
#                 # 백트래킹 (다른 경로 탐색을 위해 방문 처리 원래대로 돌려놓기)
#                 if maze[rx][ry] != 3: visited_r[nrx][nry] = False
#                 if maze[bx][by] != 4: visited_b[nbx][nby] = False

#     # 3. DFS 탐색 시작
#     dfs(rx, ry, bx, by, 0)
    
#     # 끝까지 탐색했는데 도착할 수 없는 경우 0 반환
#     return answer if answer != INF else 0

print(solution([[1, 4], [0, 0], [2, 3]]))
print(solution([[1, 0, 2], [0, 0, 0], [5, 0, 5], [4, 0, 3]]))
# print(solution([[1, 5], [2, 5], [4, 5], [3, 5]]))
# print(solution([[4, 1, 2, 3]]))
