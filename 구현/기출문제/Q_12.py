# https://school.programmers.co.kr/learn/courses/30/lessons/60061
import copy

def is_possible_pillar(map_graph, i, j):
    if i == 0:
        return True
    elif map_graph[i - 1][j] == 1 or map_graph[i - 1][j] == 3:
        return True
    elif (map_graph[i][j - 1] == 2 or map_graph[i][j] == 2) or (map_graph[i][j - 1] == 3 or map_graph[i][j] == 3):
        return True
    else:
        return False

def is_possible_line(map_graph, i, j):
    if map_graph[i - 1][j] == 1 or map_graph[i - 1][j + 1] == 1 or map_graph[i - 1][j] == 3 or map_graph[i - 1][j + 1] == 3:
        return True
    elif (map_graph[i][j - 1] == 2 or map_graph[i][j - 1] == 3) and (map_graph[i][j + 1] == 2 or map_graph[i][j + 1] == 3):
        return True
    else:
        return False

def is_possible_remove(map_graph):
    for i in range(len(map_graph)):
        for j in range(len(map_graph)):
            if map_graph[i][j] == 0:
                continue
            
            if map_graph[i][j] == 1:
                if not is_possible_pillar(map_graph, i, j):
                    return False
            elif map_graph[i][j] == 2:
                if not is_possible_line(map_graph, i, j):
                    return False
            else:
                is_remove = False
                if is_possible_pillar(map_graph, i, j) and is_possible_line(map_graph, i, j):
                    is_remove = True
                
                if not is_remove:
                    return False

    return True

def solution(n, build_frame):
    answer = []
    map_graph = [[0] * (n + 1) for _ in range(n + 1)]
    for build in build_frame:
        pos_i = build[1]
        pos_j = build[0]
        type = build[2]
        mode = build[3]

        if mode == 1:
            if type == 0:
                if is_possible_pillar(map_graph, pos_i, pos_j):
                    if map_graph[pos_i][pos_j] != 0:
                        map_graph[pos_i][pos_j] = 3
                    else:
                        map_graph[pos_i][pos_j] = 1
            else:
                if is_possible_line(map_graph, pos_i, pos_j):
                    if map_graph[pos_i][pos_j] != 0:
                        map_graph[pos_i][pos_j] = 3
                    else:
                        map_graph[pos_i][pos_j] = 2
        else:
            copy_map = copy.deepcopy(map_graph)
            if type == 0:
                copy_map[pos_i][pos_j] -= 1
            else:
                copy_map[pos_i][pos_j] -= 2
            
            if is_possible_remove(copy_map):
                map_graph[pos_i][pos_j] = copy_map[pos_i][pos_j]

    for i in range(n + 1):
        for j in range(n + 1):
            if map_graph[i][j] == 0:
                continue

            if map_graph[i][j] == 1:
                answer.append([j, i, 0])
            elif map_graph[i][j] == 2:
                answer.append([j, i, 1])
            else:
                answer.append([j, i, 0])
                answer.append([j, i, 1])

    sorted_data = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    return sorted_data

# solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]])
# solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
solution(5, [[0,0,0,1],[4,0,0,1],[0,1,1,1], [3,1,1,1], [3,1,0,1], [3,1,1,0]])
# print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[3,1,0,1], [2,1,1,0]]))
# print(solution(100, [[2, 0, 0, 1], [100, 0, 0, 1], [100, 1, 1, 1], [99, 1, 1, 1], [99, 1, 0, 1], [99, 0, 0, 1]]))