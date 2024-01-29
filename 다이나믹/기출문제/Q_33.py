# https://www.acmicpc.net/problem/14501
N = int(input())
map_table = [0] * N
T = []
P = []

for i in range(N):
    a, b = map(int, input().split())
    
    T.append(a)
    P.append(b)
    map_table[i] = b

result = 0
for i in range(N):
    if i + T[i] <= N:
        is_found = False
        
        for j in range(i + T[i], N):
            if j + T[j] <= N:
                is_found = True
                cal_value = P[j] + map_table[i]
                
                if map_table[j] < cal_value:
                    map_table[j] = cal_value

                    if result < cal_value:
                        result = cal_value
        
        if not is_found and result < map_table[i]:
            result = map_table[i]
                
print(result)