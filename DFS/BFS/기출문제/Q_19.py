# https://www.acmicpc.net/problem/14888
from itertools import permutations
INF = 1e9

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
operators_str = []

for i in range(len(operators)):
    if i == 0:
        for j in range(operators[i]):
            operators_str.append("+")
    elif i == 1:
        for j in range(operators[i]):
            operators_str.append("-")
    elif i == 2:
        for j in range(operators[i]):
            operators_str.append("*")
    else:
        for j in range(operators[i]):
            operators_str.append("/")

maxValue = int(-INF)
minValue = int(INF)

for operator_set in permutations(operators_str, len(operators_str)):
    result1 = numbers[0]
    for i in range(len(operator_set)):
        operator = operator_set[i]
        
        if operator == "+":
            result1 += numbers[i + 1]
        elif operator == "-":
            result1 -= numbers[i + 1]
        elif operator == "*":
            result1 *= numbers[i + 1]
        elif operator == "/":
            if result1 < 0:
                result1 = -(abs(result1) // numbers[i + 1])
            else:
                result1 //= numbers[i + 1]
    
    maxValue = max(maxValue, result1)
    minValue = min(minValue, result1)

print(maxValue)
print(minValue)