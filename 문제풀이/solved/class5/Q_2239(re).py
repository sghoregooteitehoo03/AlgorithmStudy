import sys
input = sys.stdin.readline

quiz = []
for i in range(9):
    data = list(input().rstrip())
    quiz.append([int(x) for x in data])

zero_pos = []
for i in range(9):
    for j in range(9):
        if quiz[i][j] == 0:
            zero_pos.append((i, j))

def is_find(pos_i, pos_j, n):
    for i in range(9):
        if quiz[i][pos_j] == n:
            return False
        if quiz[pos_i][i] == n:
            return False

    start_i = (pos_i // 3) * 3
    start_j = (pos_j // 3) * 3

    for i in range(3):
        for j in range(3):
            if quiz[start_i + i][start_j + j] == n:
                return False

    return True

def dfs(start):
    if start == len(zero_pos):
        for number in quiz:
            print(*number, sep='')
        exit()

    pos_i, pos_j = zero_pos[start]
    for i in range(1, 10):
        if is_find(pos_i, pos_j, i):
            quiz[pos_i][pos_j] = i
            dfs(start + 1)
            quiz[pos_i][pos_j] = 0

dfs(0)