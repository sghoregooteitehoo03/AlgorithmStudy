# https://www.acmicpc.net/contest/problem/1244/3
t = int(input())
data = []

for i in range(t):
    data.append(list(map(int, input().split())))

for i in range(t):
    result = 0
    map_array = [[0] * data[i][0] for _ in range(data[i][1])]
    
    for j in range(data[i][1]):
        for k in range(data[i][0]):
            c = 1
            previous_x = k
            previous_y = j

            while map_array[j][k] != 1:
                
                move_x = data[i][2] * c
                move_y =  data[i][3] * c
                
                if k + move_x < data[i][0] and j + move_y < data[i][1]:
                    if map_array[j + move_y][k + move_x] != 1:
                        map_array[previous_y][previous_x] = 0
                        map_array[j + move_y][k + move_x] = 1
                        
                        is_found = True
                        previous_x = k + move_x
                        previous_y = j + move_y
                        c += 1
                    else:
                        map_array[previous_y][previous_x] = 1
                        break
                else:
                    if map_array[previous_y][previous_x] != 1:
                        map_array[previous_y][previous_x] = 1
                    break
    
    for j in range(data[i][1]):
        for k in range(data[i][0]):
            if map_array[j][k] == 1:
                result += 1
    
    print(result)