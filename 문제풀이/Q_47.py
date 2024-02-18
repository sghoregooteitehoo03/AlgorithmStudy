from collections import deque
import heapq
import copy

def get_direction_number(direc):
    if direc + 1 > 8:
        direc = 0
    
    return direc + 1

def get_direction(direc):
    d = [(), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    return d[direc]

def change_fish(map_array):
    q = []
    pos_table = [0] * 17
    
    for i in range(len(map_array)):
        for j in range(len(map_array)):
            fish = map_array[i][j]
            
            if fish[0] > 0:
                heapq.heappush(q, (fish[0], fish[1]))
                pos_table[fish[0]] = (i, j)

    while q:
        fish = heapq.heappop(q)

        while True:
            direction = get_direction(fish[1])
            fish_pos = pos_table[fish[0]]
            plus_pos = (fish_pos[0] + direction[0], fish_pos[1] + direction[1])
            
            if plus_pos[0] < len(map_array) and plus_pos[0] >= 0 and plus_pos[1] < len(map_array) and plus_pos[1] >= 0:
                other_fish = map_array[plus_pos[0]][plus_pos[1]]
                if other_fish[0] != -1:
                    temp = map_array[fish_pos[0]][fish_pos[1]]
                    map_array[fish_pos[0]][fish_pos[1]] = other_fish
                    map_array[plus_pos[0]][plus_pos[1]] = temp

                    temp = pos_table[fish[0]]
                    pos_table[fish[0]] = pos_table[other_fish[0]]
                    pos_table[other_fish[0]] = temp

                    break
                else:
                    fish = (fish[0], get_direction_number(fish[1]))
            else:
                fish = (fish[0], get_direction_number(fish[1]))

map_array = []

for i in range(4):
    n1, d1, n2, d2, n3, d3, n4, d4 = map(int, input().split())
    map_array.append([(n1, d1), (n2, d2), (n3, d3), (n4, d4)])

shark_start = (map_array[0][0][0], map_array[0][0][1],  0, 0)
map_array[0][0] = (-1, 0)

q = deque([(shark_start, map_array)])

while q:
    shark, map = q.popleft()

    change_fish(map)
    
    next_pos = get_direction(shark[1])
    shark_ordinary_pos = (shark[2], shark[3])
    for i in range(3):
        next_shark_pos = (shark[2] + next_pos[0], shark[3] + next_pos[1])
        copy_map = copy.deepcopy(map)

        if next_shark_pos[0] < len(map_array) and next_shark_pos[0] >= 0 and next_shark_pos[1] < len(map_array) and next_shark_pos[1] >= 0:
            fish = map_array[next_shark_pos[0]][next_shark_pos[1]]
            if fish[0] != 0:
                copy_map[next_shark_pos[0]][next_shark_pos[1]] = (-1, 0)
                copy_map[shark_ordinary_pos[0]][shark_ordinary_pos[1]] = (0, 0)
                shark = (shark[0] + fish[0], fish[1], next_shark_pos[0], next_shark_pos[1])
                q.append((shark, copy_map))