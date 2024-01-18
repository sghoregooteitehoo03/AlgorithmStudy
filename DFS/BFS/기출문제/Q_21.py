# https://www.acmicpc.net/problem/16234
import copy

def check_allience(value1, value2, L, R):
    diff_value = abs(value1 - value2)
    
    return diff_value >= L and diff_value <= R

def move_people(country, N, L, R):
    grouping_county = []

    for i in range(N):
        l = []

        for j in range(N):
            l.append((i * N + j, country[i][j]))

        grouping_county.append(l)

    for i in range(N):
        for j in range(N):
            group_id = grouping_county[i][j][0]

            if i - 1 >= 0:
                if grouping_county[i - 1][j][0] != group_id and check_allience(country[i - 1][j], country[i][j], L, R):    
                    grouping_county[i - 1][j] = (group_id, country[i - 1][j])

            if i + 1 < N :
                if grouping_county[i + 1][j][0] != group_id and check_allience(country[i + 1][j], country[i][j], L, R):
                    grouping_county[i + 1][j] = (group_id, country[i + 1][j])

            if j - 1 >= 0:
                if grouping_county[i][j - 1][0] != group_id and check_allience(country[i][j - 1], country[i][j], L, R):
                    grouping_county[i][j - 1] = (group_id, country[i][j - 1])
                
            if j + 1 < N:
                if grouping_county[i][j + 1][0] != group_id and check_allience(country[i][j + 1], country[i][j], L, R):
                    grouping_county[i][j + 1] = (group_id, country[i][j + 1])
                    
    group = [[] for _ in range(N * N)]

    for i in range(N):
        l = []
        for j in range(N):
            value = grouping_county[i][j]
            group[value[0]].append((value[1], i, j))

    is_break = True
    for g in group:
        if len(g) > 1:
            is_break = False
        else:
            continue

        move_value = sum(item[0] for item in g) // len(g)
        
        for pos in g:
            country[pos[1]][pos[2]] = move_value

    if is_break:
        return 0
    
    return 1 + move_people(country, N, L, R)

N, L, R = map(int, input().split())
country = []

for i in range(N):
    country.append(list(map(int, input().split())))

print(move_people(copy.deepcopy(country), N, L, R))