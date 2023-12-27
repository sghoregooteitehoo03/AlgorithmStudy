# https://www.acmicpc.net/problem/1439
str = input()
latest = -1
isFirst = False
result = [0, 0]

for s in str: 
    n = int(s)
    
    if latest != n:
        latest = n
        isFirst = True

    if isFirst:
        isFirst = False
        result[latest] += 1

print(min(result))