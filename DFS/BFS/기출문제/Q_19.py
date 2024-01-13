# https://www.acmicpc.net/problem/14888
from itertools import permutations

n = int(input())
number_list = list(map(int, input().split()))
operation_list = list(map(int, input().split()))
operation_list_flat = []

max_result = int(-1e9)
min_result = int(1e9)

for i in range(len(operation_list)):
    for j in range(operation_list[i]):
        operation_list_flat.append(i)

cases = list(set(permutations(operation_list_flat)))
for case in cases:
    result = 0
    for i in range(len(number_list)):
        if i == 0:
            result += number_list[i]
        else:
            if case[i - 1] == 0:
                result += number_list[i]
            elif case[i - 1] == 1:
                result -= number_list[i]
            elif case[i - 1] == 2:
                result *= number_list[i]
            elif case[i - 1] == 3:
                result = int(result / number_list[i])

    if result < min_result:
        min_result = result
    if result > max_result:
        max_result = result

print(max_result)
print(min_result)