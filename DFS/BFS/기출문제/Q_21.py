# https://www.acmicpc.net/problem/16234
import copy
from collections import deque

def check_allience(value1, value2, L, R):
    diff_value = abs(value1 - value2)
    
    return diff_value >= L and diff_value <= R

def move_people(country, N, L, R):
    visited = [[False] * N for _ in range(N)]
    q = deque([(0, 0)])
    allience = []

    while(q):
        pos_i, pos_j = q.popleft()

        if not visited[pos_i][pos_j]:
            visited[pos_i][pos_j] = True

            if pos_i - 1 >= 0 and not visited[pos_i - 1][pos_j]:
                if check_allience(country[pos_i - 1][pos_j], country[pos_i][pos_j], L, R):
                    if len(allience) == 0:
                        allience.append(country[pos_i][pos_j])
                    allience.append(country[pos_i - 1][pos_j])

                q.append((pos_i - 1, pos_j))
            if pos_i + 1 < N and not visited[pos_i + 1][pos_j]:
                if check_allience(country[pos_i + 1][pos_j], country[pos_i][pos_j], L, R):
                    if len(allience) == 0:
                        allience.append(country[pos_i][pos_j])
                    allience.append(country[pos_i + 1][pos_j])

                q.append((pos_i + 1, pos_j))
            if pos_j - 1 >= 0 and not visited[pos_i][pos_j - 1]:
                if check_allience(country[pos_i][pos_j - 1], country[pos_i][pos_j], L, R):
                    if len(allience) == 0:
                        allience.append(country[pos_i][pos_j])
                    allience.append(country[pos_i][pos_j - 1])

                q.append((pos_i, pos_j - 1))
            if pos_j + 1 < N and not visited[pos_i][pos_j + 1]:
                if check_allience(country[pos_i][pos_j + 1], country[pos_i][pos_j], L, R):
                    if len(allience) == 0:
                        allience.append(country[pos_i][pos_j])
                    allience.append(country[pos_i][pos_j + 1])

                q.append((pos_i, pos_j + 1))

    if len(allience) == 0:
        return 0

    move_value = sum(allience) // len(allience)

    for i in range(N):
        for j in range(N):
            if country[i][j] in allience:
                country[i][j] = move_value
            
    return 1 + move_people(country, N, L, R)


N, L, R = map(int, input().split())
country = []

for i in range(N):
    country.append(list(map(int, input().split())))

print(move_people(copy.deepcopy(country), N, L, R))