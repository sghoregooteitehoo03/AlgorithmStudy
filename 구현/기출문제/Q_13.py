from itertools import combinations

n, m = map(int, input().split())
board = []

for i in range(n):
    board.append(list(map(int, input().split())))

homes = []
chickens = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            homes.append((i + 1, j + 1))
        elif board[i][j] == 2:
            chickens.append((i + 1, j + 1))

answer = 1e9
for chicken in list(combinations(chickens, m)):
    result = 0
    for home in homes:
        min_lenght = 1e9
        
        for c_pos in chicken:
            min_lenght = min(min_lenght, abs((home[0] - c_pos[0])) + abs((home[1] - c_pos[1])))

        result += min_lenght
    answer = min(answer, result)

print(answer)
