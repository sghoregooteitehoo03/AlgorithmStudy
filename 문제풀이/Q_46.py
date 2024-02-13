# https://www.acmicpc.net/problem/16236
n = int(input())
map_array = []
fish_pos = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: []
}
shark = ()
result = 0

for i in range(n):
    map_array.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if map_array[i][j] == 9:
            shark = ((i, j, 2, 0))
        elif map_array[i][j] != 0:
            fish_pos[map_array[i][j]].append((i, j))

while(True):
    min_pos = (1e9, -1, -1)

    for i in range(1, shark[2]):
        for fp in fish_pos[i]:
            pos_i, pos_j = fp
                
            if map_array[pos_i][pos_j] != 0:
                distance = (abs(pos_i - shark[0]) + abs(pos_j - shark[1]))

                if min_pos[0] > distance:
                    min_pos = (distance, pos_i, pos_j)
                    
    if min_pos[0] == 1e9:
        break

    map_array[min_pos[1]][min_pos[2]] = 0
    result += min_pos[0]
    shark = (min_pos[1], min_pos[2], shark[2], shark[3] + 1)

    if shark[2] == shark[3] and shark[2] < 6:
        shark = (shark[0], shark[1], shark[2] + 1, 0)

print(result)