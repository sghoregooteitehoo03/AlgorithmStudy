# https://www.acmicpc.net/problem/19237
n, m, k = map(int, input().split())
map_graph = []
sharks = [0] * (m + 1)
sharks_moves = [[] for _ in range(m + 1)]

for i in range(n):
    map_graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        shark_index = map_graph[i][j]
        if shark_index != 0:
            sharks[shark_index] = (i, j)
            map_graph[i][j] = (shark_index, k)

direct_list = list(map(int, input().split()))
for i in range(1, m + 1):
    sharks[i] = (sharks[i][0], sharks[i][1], direct_list[i - 1])

for i in range(1, m + 1):
    for j in range(4):
        sharks_moves[i].append(list(map(int, input().split())))

time = 0
move_pos = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]

while time <= 1000:
    for i in range(1, m + 1):
        shark = sharks[i]
        is_moved = False

        if shark[2] == -1:
            continue

        for dic in sharks_moves[i][shark[2] - 1]:
            pos = move_pos[dic]
            move_i = shark[0] + pos[0]
            move_j = shark[1] + pos[1]

            if move_i < n and move_i >= 0 and move_j < n and move_j >= 0:
                if map_graph[move_i][move_j] == 0:
                    sharks[i] = (move_i, move_j, dic)

                    is_moved = True
                    break
        
        if not is_moved:
            for dic in sharks_moves[i][shark[2] - 1]:
                pos = move_pos[dic]
                move_i = shark[0] + pos[0]
                move_j = shark[1] + pos[1]

                if move_i < n and move_i >= 0 and move_j < n and move_j >= 0:
                    if map_graph[move_i][move_j][0] == i:
                        sharks[i] = (move_i, move_j, dic)

                        break
        
    for i in range(1, m + 1):
        current_shark = sharks[i]

        if current_shark[2] == -1:
            continue

        if map_graph[current_shark[0]][current_shark[1]] != 0 and map_graph[current_shark[0]][current_shark[1]][0] != i:
            if i < map_graph[current_shark[0]][current_shark[1]][0]:
                sharks[map_graph[current_shark[0]][current_shark[1]][0]] = (0, 0, -1)
                map_graph[current_shark[0]][current_shark[0]] = (i, k + 1)
            else:
                sharks[i] = (0, 0, -1)

        else:
            map_graph[current_shark[0]][current_shark[1]] = (i, k + 1)
        
    for i in range(n):
        for j in range(n):
            if map_graph[i][j] != 0:
                
                if map_graph[i][j][1] == 1:
                    map_graph[i][j] = 0
                else:
                    map_graph[i][j] = (map_graph[i][j][0], map_graph[i][j][1] - 1)
    
    time += 1
    is_finished = True
    for i in range(2, m + 1):
        if sharks[i][2] != -1:
            is_finished = False
            break
    
    if is_finished:
        break

if time <= 1000:
    print(time)
else:
    print(-1)