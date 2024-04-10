import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = []

for i in range(r):
    board.append(list(input()))

visited = [False] * 26
result = 0

def dfs(i, j, visited_copy, count):
    global result
    if i >= r or j >= c or i < 0 or j < 0:
        return
    
    if visited_copy[ord(board[i][j]) - 65]:
        result = max(result, count)
        return

    visited_copy[ord(board[i][j]) - 65] = True
    dfs(i + 1, j, visited_copy, count + 1)
    dfs(i - 1, j, visited_copy, count + 1)
    dfs(i, j + 1, visited_copy, count + 1)
    dfs(i, j - 1, visited_copy, count + 1)
    visited_copy[ord(board[i][j]) - 65] = False

dfs(0, 0, visited, 0)
print(result)