# https://www.acmicpc.net/contest/problem/1244/2
def check_reverse(input_str):
    if len(input_str) <= 2:
        return True

    length = len(input_str)
    midpoint = length // 2
    
    first_half = input_str[:midpoint]
    if length % 2 == 0:
        second_half = input_str[midpoint:]
    else:
        second_half = input_str[midpoint + 1:]
    reversed_second_half = second_half[::-1]

    return first_half == reversed_second_half

t = int(input())
data = []

for i in range(t):
    data.append(int(input()))

for n in data:
    start = 10 ** (n - 1)
    end = 10 ** n
    is_found = False
    j = start // 10
    i = j * 11
    
    while(i < end):
        if i % 11 == 0 and check_reverse(str(i)):
            print(i)
            is_found = True
            break

        i = j * 11
        j += 1

    if not is_found:
        print(-1)