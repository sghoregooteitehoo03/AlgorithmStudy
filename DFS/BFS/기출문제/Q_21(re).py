# https://www.acmicpc.net/problem/16234
import copy
from collections import deque

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def check_allience(value1, value2, L, R):
    diff_value = abs(value1 - value2)
    
    return diff_value >= L and diff_value <= R

def move_people(country, N, L, R):
    grouping_county = []

    for i in range((N * N) + 1):
        grouping_county.append(i)

    for i in range(N):
        for j in range(N):
            group_id = find_parent(grouping_county, grouping_county[i * N + j])

            if i - 1 >= 0:
                other_group_id = find_parent(grouping_county, grouping_county[(i - 1) * N + j])
                if other_group_id != group_id and check_allience(country[i - 1][j], country[i][j], L, R):
                    if group_id <= other_group_id:
                        grouping_county[(i - 1) * N + j] = (group_id, country[i - 1][j])
                    else:
                        grouping_county[i - 1][j] = (grouping_county[i - 1][j][0], country[i - 1][j])

            if i + 1 < N :
                if grouping_county[i + 1][j][0] != group_id and check_allience(country[i + 1][j], country[i][j], L, R):
                    if group_id <= grouping_county[i + 1][j][0]:
                        grouping_county[i + 1][j] = (group_id, country[i + 1][j])
                    else:
                        grouping_county[i + 1][j] = (grouping_county[i + 1][j][0], country[i + 1][j])

            if j - 1 >= 0:
                if grouping_county[i][j - 1][0] != group_id and check_allience(country[i][j - 1], country[i][j], L, R):
                    if group_id <= grouping_county[i][j - 1][0]:
                        grouping_county[i][j - 1] = (group_id, country[i][j - 1])
                    else:
                        grouping_county[i][j - 1] = (grouping_county[i][j - 1][0], country[i][j - 1])
                
            if j + 1 < N:
                if grouping_county[i][j + 1][0] != group_id and check_allience(country[i][j + 1], country[i][j], L, R):
                    if group_id <= grouping_county[i][j + 1][0]:
                        grouping_county[i][j + 1] = (group_id, country[i][j + 1])
                    else:
                        grouping_county[i][j + 1] = (grouping_county[i][j + 1][0], country[i][j + 1])
                    
    group = [[] for _ in range(N * N)]
    # print(country)
    print(grouping_county)

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
    
    # print(country)
    return 1 + move_people(country, N, L, R)

N, L, R = map(int, input().split())
country = []

for i in range(N):
    country.append(list(map(int, input().split())))

print(move_people(copy.deepcopy(country), N, L, R))