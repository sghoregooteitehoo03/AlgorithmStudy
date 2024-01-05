# https://www.acmicpc.net/problem/15686
import copy

def calcurator(house_table, chicken_table):
    result = 0
    
    for house in house_table:
            min = 1e9

            for chicken in chicken_table:
                house_col, house_row = house
                chicken_col, chicken_row = chicken

                cal = abs(house_col - chicken_col) + abs(house_row - chicken_row)

                if cal < min:
                    min = cal

            result += min

    return result

n, m = map(int, input().split())
map_table = []
house_table = []
chicken_table = []
result_list = []

for i in range(n):
    map_table.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        value = map_table[i][j]
        if value == 1:  # 집인 경우
            house_table.append((i, j))
        elif value == 2:  # 치킨집인 경우
            chicken_table.append((i, j))

close = len(chicken_table) - m
if close == 1:
    for i in range(len(chicken_table)):
        chicken_table_copy = copy.deepcopy(chicken_table)
        del chicken_table_copy[i]

        result = calcurator(house_table, chicken_table_copy)
        result_list.append(result)
elif m == 1:
    for i in range(len(chicken_table)):
        result = calcurator(house_table, [chicken_table[i]])
        result_list.append(result)
elif close > 1:
    for i in range(len(chicken_table)):
        chicken_table_copy = copy.deepcopy(chicken_table)
        
        del chicken_table_copy[i]
        temp = copy.deepcopy(chicken_table_copy)

        for j in range(i + 1, len(chicken_table)):
            remove_value = chicken_table[j]
            chicken_table_copy.remove(remove_value)

            if len(chicken_table_copy) == m:
                result = calcurator(house_table, chicken_table_copy)
                result_list.append(result)

                chicken_table_copy = copy.deepcopy(temp)
else:
    result = calcurator(house_table, chicken_table)
    result_list.append(result)

print(min(result_list))
# print(house_table)
# print(chicken_table)
# print(map_table)
