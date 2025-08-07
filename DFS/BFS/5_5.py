def find(board, current_pos, max_size, visited):
    pos_i = current_pos[0]
    pos_j = current_pos[1]
    value = board[pos_i][pos_j]

    if(value != 1 and not visited[pos_i][pos_j]):
        visited[pos_i][pos_j] = True
        
        if(pos_i + 1 < max_size[0]):
            find(board, (pos_i + 1, pos_j), max_size, visited)
        if(pos_i - 1 >= 0):
            find(board, (pos_i - 1, pos_j), max_size, visited)
        if(pos_j - 1 >= 0):
            find(board, (pos_i, pos_j - 1), max_size, visited)
        if(pos_j + 1 < max_size[1]):
            find(board, (pos_i, pos_j + 1), max_size, visited)
        
        return True
    else:
        return False

n, m = map(int, input().split())
result = 0
board = []
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    board.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        if find(board, (i, j), (n, m), visited):
            result +=1

print(result)

# # 변수 선언에 중요성!! (인덱스간의 오류로 디버깅간 오래걸림)
# def dfs(graph, v, visited, movements):
#     for move in movements:
#         nextMove = [(v[0] + move[0]), (v[1] + move[1])]
#         dy = nextMove[0]
#         dx = nextMove[1]

#         if (dy < 0 or dx < 0):
#             continue
#         elif (dy > len(graph) - 1 or dx > len(graph[0]) - 1):
#             continue

#         hole = int(graph[dy][dx])
#         if hole == 0 and not visited[dy][dx]:
#             visited[dy][dx] = True
#             dfs(graph, nextMove, visited, movements)

# n, m = map(int, input().split())
# frame = []
# result = 0
# visited = [[False] * m for _ in range(n)]
# movements = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# for i in range(n):
#     data = input()
#     frame.append(data)

# for i in range(n):
#     for j in range(m):
#         hole = int(frame[i][j])

#         if hole == 0 and not visited[i][j]:
#             visited[i][j] = True
#             dfs(frame, [i, j], visited, movements)

#             result += 1

# print(result)